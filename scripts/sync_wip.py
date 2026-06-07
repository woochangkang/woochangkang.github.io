# -*- coding: utf-8 -*-
"""Regenerate Works-in-progress entries (_publications/*-wip-NN.md).

Source of truth = the Zotero "My Working Papers" collection (D3IVWRX8): any
manuscript added there is reflected automatically. A small hardcoded FALLBACK
list keeps papers that are not in Zotero yet (Zotero wins on title match).

Abstracts are cleaned of LaTeX. Papers with an abstract are auto-sorted to the
top by the publications-page rule.

    python scripts/sync_wip.py
"""
import os, re, json, datetime
PUB = os.path.expanduser("~/Library/CloudStorage/Dropbox/projects/woochangkang.github.io/_publications")
WIP_COLLECTION = "D3IVWRX8"
VOCAB = {"AI","Elections","Voting","Public Opinion","Polarization","Gender","Inequality",
         "Real Estate Price","Immigration","Weather","Face","Legacies","South Korea","US",
         "Australia","North Korea","Cross-national Studies"}

# Fallback: working papers not (yet) in the Zotero collection. (title, authors, tags)
FALLBACK = [
 ("Housing Prices, Rental Prices, and Perceptions about the Economy: Evidence from South Korea","Kang, Woo Chang and Sein Park",["Real Estate Price","Inequality","Public Opinion","South Korea"]),
 ("Depressive Symptoms Around the 2025 South Korean Presidential Election: The Roles of Voting, Electoral Outcomes, and Manipulation Beliefs","Kang, Woo Chang, June Kang, Kyu-Man Han",["Public Opinion","Elections","South Korea"]),
 ("Correcting Political Misperceptions to Rebuild Norms of Good Citizenship in Polarized Democracies: Evidence from South Korea","Kang, Woo Chang and Hannah Kim",["Polarization","Public Opinion","South Korea"]),
 ("Online Media Fragmentation and Political Polarization: A Cross-National Analysis of 51 Countries","Kang, Woo Chang and Hong-gie Kim",["Polarization","Cross-national Studies"]),
 ("Unraveling Gender Bias in Candidate Evaluations through the Analysis of Representativeness, Competence, and Electability","Kang, Woo Chang",["Gender","Public Opinion"]),
 ("How Does International Naming and Shaming Affect South Korean Attitudes Toward Refugees?","Kang, Woo Chang, Han Il Chang and Taejun Choi",["Immigration","Public Opinion","South Korea"]),
 ("Politics of Face: Gender Typicality, Perceived Competence and Electoral Viability","Kang, Woo Chang",["Face","Gender","South Korea"]),
 ("A Uniform Penalty: Babyfacedness and Candidate Evaluation in Korea","Kang, Woo Chang and Sumin Kim",["Face","Public Opinion","South Korea"]),
 ("Critical Mass, Critical Actors, and Men's Gender Discourse: Evidence from Korean National Assembly Standing Committees","Kang, Woo Chang, Taegyoon Kim and Sunkyoung Park",["Gender","Public Opinion","South Korea"]),
 ("Democratic Accountability in East Asia","Kang, Woo Chang, Sunkyoung Park, Osbern Huang, Koh Iwabuchi and Tetsuro Kobayashi",["Public Opinion","Cross-national Studies","US"]),
 ("Electoral Effect of Stop and Frisk","Kang, Woo Chang and Chris Dawes",["Elections","US"]),
]

LIGMAP = {'bene ts':'benefits','di erent':'different','e ect':'effect','signi cant':'significant',
          'speci c':'specific','di cult':'difficult','in uence':'influence','e ects':'effects'}

def clean_latex(t):
    if not t: return t
    t = re.sub(r'\\(?:textit|textbf|emph|text|mathrm|mathit|textsc|texttt)\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\(?:cite|citep|citet|ref|eqref|label|footnote)\{[^{}]*\}', '', t)
    t = re.sub(r'\$\$?(.*?)\$\$?', r'\1', t)               # math -> inner text
    t = (t.replace('\\%','%').replace('\\&','&').replace('\\_','_').replace('\\#','#')
          .replace('\\$','$').replace('~',' ').replace('\\,',' ').replace('\\;',' ')
          .replace('``','"').replace("''",'"').replace('\\textendash','–').replace('\\textemdash','—'))
    t = re.sub(r'\\[a-zA-Z]+\*?', '', t)                   # any remaining \command
    t = t.replace('{','').replace('}','')
    return re.sub(r'\s+', ' ', t).strip()

def tidy(t):
    t = (t or '').replace('\r\n','\n').replace('\r','\n')
    t = re.sub(r'^\s*abstract\s*[:.]?\s*','',t,flags=re.I)
    t = re.sub(r'([a-z])-\n([a-z])', r'\1\2', t)
    t = re.sub(r'\s*\n\s*',' ',t); t = re.sub(r'[ \t]{2,}',' ',t).strip()
    t = t.replace('---','—').replace('--','–')
    for k,v in LIGMAP.items(): t = re.sub(r'\b'+re.escape(k)+r'\b', v, t, flags=re.I)
    return clean_latex(t)

def cred():
    env = json.load(open(os.path.expanduser("~/.claude/settings.json"))).get("env",{})
    return os.environ.get("ZOTERO_USER_ID") or env.get("ZOTERO_USER_ID"), \
           os.environ.get("ZOTERO_API_KEY") or env.get("ZOTERO_API_KEY")

def bold(a):
    for n in ("Woo Chang Kang","Kang, Woo Chang","강우창"): a = a.replace(n, "<strong>%s</strong>"%n)
    return a
def q(s): return '"' + s.replace('"','\\"') + '"'
def norm(s): return re.sub(r'\s+',' ', re.sub(r'[^\w]',' ', (s or '').lower())).strip()
def fmt_authors(creators):
    parts=[]
    for c in creators:
        parts.append(c["name"] if c.get("name") else ("%s %s"%(c.get("firstName",""),c.get("lastName",""))).strip())
    if len(parts)<=1: return parts[0] if parts else ""
    return "%s and %s" % (", ".join(parts[:-1]), parts[-1])

def main():
    uid,key = cred()
    from pyzotero import zotero
    zot = zotero.Zotero(uid,"user",key)
    z_items = [it for it in zot.everything(zot.collection_items(WIP_COLLECTION))
               if it["data"].get("itemType")=="journalArticle"]
    fb_by_title = {norm(t): (t,a,tg) for (t,a,tg) in FALLBACK}

    entries, z_titles = [], set()
    for it in sorted(z_items, key=lambda x: x["data"].get("dateAdded",""), reverse=True):
        d = it["data"]; title = d.get("title","").strip()
        if norm(title) in z_titles: continue        # skip duplicate items within Zotero
        z_titles.add(norm(title))
        fb = fb_by_title.get(norm(title))
        tags = fb[2] if fb else [t["tag"] for t in d.get("tags",[]) if t["tag"] in VOCAB]
        authors = bold(fb[1]) if fb else bold(fmt_authors(d.get("creators",[])))
        entries.append((title, authors, tags, tidy(d.get("abstractNote",""))))
    for (t,a,tg) in FALLBACK:                       # not yet in Zotero
        if norm(t) not in z_titles:
            entries.append((t, bold(a), tg, ""))

    for f in os.listdir(PUB):
        if "wip-" in f: os.remove(os.path.join(PUB,f))
    n = len(entries)
    for i,(title,authors,tags,ab) in enumerate(entries):
        date = (datetime.date(2030, 1, 1) + datetime.timedelta(days=(n - i))).isoformat()  # valid dates, order preserved on date-reverse
        fm = ["---", "title: %s"%q(title), "collection: publications", "category: wip",
              'year: ""', "authors: %s"%q(authors), 'venue: ""', 'detail: ""',
              "date: %s"%date, "permalink: /publications/wip-%02d"%(i+1),
              "tags: [" + ", ".join(q(t) for t in tags) + "]", "---"]
        open(os.path.join(PUB, "%s-wip-%02d.md"%(date,i+1)), "w", encoding="utf-8").write(
            "\n".join(fm) + "\n" + ("\n"+ab+"\n" if ab else ""))
    print("wrote %d wip entries (%d from Zotero, %d fallback-only)" % (n, len(z_titles), n-len(z_titles)))

if __name__ == "__main__":
    main()
