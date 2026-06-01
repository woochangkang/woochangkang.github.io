#!/usr/bin/env python3
"""Incrementally add the author's Zotero papers that are not yet in
_publications/. Existing curated files are never modified. New items are
scaffolded with bibliographic data from Zotero (tags left for manual review).

Usage:
  python scripts/sync_publications.py --dry-run   # list what would be added
  python scripts/sync_publications.py             # write the new files
"""
import os, re, sys, glob, json, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB  = os.path.join(ROOT, "_publications")
ME   = ("Kang", "Woo Chang", "강우창")   # surname, given, korean

def cred():
    k = os.environ.get("ZOTERO_API_KEY"); u = os.environ.get("ZOTERO_USER_ID")
    if k and u: return u, k
    env = json.load(open(os.path.expanduser("~/.claude/settings.json"))).get("env", {})
    return os.environ.get("ZOTERO_USER_ID") or env.get("ZOTERO_USER_ID"), \
           os.environ.get("ZOTERO_API_KEY") or env.get("ZOTERO_API_KEY")

def norm(s): return re.sub(r"\s+", " ", re.sub(r"[^\w가-힣]", " ", (s or "").lower())).strip()

def clean_latex(t):
    if not t: return t
    t = re.sub(r'\\(?:textit|textbf|emph|text|mathrm|mathit|textsc|texttt)\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\(?:cite|citep|citet|ref|eqref|label|footnote)\{[^{}]*\}', '', t)
    t = re.sub(r'\$\$?(.*?)\$\$?', r'\1', t)
    t = (t.replace('\\%','%').replace('\\&','&').replace('\\_','_').replace('\\#','#')
          .replace('\\$','$').replace('~',' ').replace('\\,',' ').replace('``','"').replace("''",'"'))
    t = re.sub(r'\\[a-zA-Z]+\*?', '', t).replace('{','').replace('}','')
    return re.sub(r'\s+', ' ', t).strip()
def tnorm(s): return norm(re.sub(r"\[.*?\]", "", s or ""))   # title match, ignoring [..] suffixes

def is_me(d):
    for c in d.get("creators", []):
        ln = (c.get("lastName","") or "").lower(); fn = (c.get("firstName","") or "").lower()
        nm = (c.get("name","") or "")
        if ("kang" in ln and "woo" in fn) or "강우창" in nm or nm == "Woo Chang Kang":
            return True
    return False

def bold_me(s):
    for n in ("Woo Chang Kang", "Kang, Woo Chang", "강우창"):
        s = s.replace(n, "<strong>%s</strong>" % n)
    return s

def fmt_authors(creators):
    parts, korean = [], False
    for c in creators:
        if c.get("name"):
            parts.append(c["name"]); korean = korean or bool(re.search(r"[가-힣]", c["name"]))
        else:
            parts.append(("%s %s" % (c.get("firstName",""), c.get("lastName",""))).strip())
    if korean:
        return bold_me("·".join(parts))
    if len(parts) == 1: out = parts[0]
    elif len(parts) == 2: out = "%s and %s" % (parts[0], parts[1])
    else: out = "%s, and %s" % (", ".join(parts[:-1]), parts[-1])
    return bold_me(out)

def existing_keys():
    """DOIs and normalized titles already present in _publications."""
    dois, titles = set(), set()
    for f in glob.glob(PUB + "/*.md"):
        fm = open(f, encoding="utf-8").read().split("---", 2)[1]
        for line in fm.splitlines():
            m = re.match(r'(doi|title|title_en):\s*"?(.*?)"?\s*$', line.strip())
            if not m: continue
            if m.group(1) == "doi": dois.add(m.group(2).lower())
            else: titles.add(tnorm(m.group(2)))
    return dois, titles

def yq(s): return '"' + (s or "").replace('"', '\\"') + '"'

def main():
    dry = "--dry-run" in sys.argv
    uid, key = cred()
    from pyzotero import zotero
    zot = zotero.Zotero(uid, "user", key)
    items = zot.everything(zot.items(q="Woo Chang Kang", qmode="titleCreatorYear")) + \
            zot.everything(zot.items(q="강우창", qmode="titleCreatorYear"))
    # Working papers live in the "My Working Papers" collection — never treat
    # them as published articles (they have no venue/date and belong in the
    # Works-in-progress section, not the publication list).
    WIP_COLLECTION = "D3IVWRX8"
    try:
        wip_keys = set(x["key"] for x in zot.everything(zot.collection_items(WIP_COLLECTION)))
    except Exception:
        wip_keys = set()
    seen, mine = set(), []
    for it in items:
        if it["key"] in seen: continue
        seen.add(it["key"])
        if it["key"] in wip_keys: continue
        if it["data"].get("itemType") == "journalArticle" and is_me(it["data"]):
            mine.append(it)
    dois, titles = existing_keys()
    new = []
    for it in mine:
        d = it["data"]
        doi = (d.get("DOI","") or "").lower()
        if doi and doi in dois: continue
        if tnorm(d.get("title","")) in titles: continue
        new.append(it)
    print("authored journal articles in Zotero: %d | already on site: %d | NEW: %d"
          % (len(mine), len(mine) - len(new), len(new)))
    for it in new:
        d = it["data"]
        lang = (d.get("language","") or "").lower()
        cat = "korean" if lang.startswith("ko") else "english"
        year = (d.get("date","") or "")[:4] or "n.d."
        detail = d.get("volume","")
        if d.get("issue"): detail += "(%s)" % d["issue"]
        if d.get("pages"): detail += ": %s" % d["pages"]
        eng_title = ""
        for line in (d.get("extra","") or "").splitlines():
            mm = re.match(r"English Title:\s*(.+)", line.strip(), re.I)
            if mm: eng_title = mm.group(1).strip()
        slug = "z-" + it["key"].lower()
        date = "%s-01-01" % year if year.isdigit() else "1900-01-01"
        url = ("https://doi.org/%s" % d["DOI"]) if d.get("DOI") else d.get("url","")
        fm = ["---", "title: %s" % yq(d.get("title","")), "collection: publications",
              "category: %s" % cat, "year: %s" % yq(year),
              "authors: %s" % yq(fmt_authors(d.get("creators", []))),
              "venue: %s" % yq(d.get("publicationTitle","")), "detail: %s" % yq(detail),
              "date: %s" % date, "permalink: /publications/%s" % slug]
        if eng_title: fm.append("title_en: %s" % yq(eng_title))
        if url: fm.append("link: %s" % yq(url))
        if d.get("DOI"): fm.append("doi: %s" % yq(d["DOI"]))
        fm.append("tags: []   # TODO: add topic tags")
        fm.append("---")
        body = clean_latex((d.get("abstractNote","") or "").strip())   # abstract -> Show abstract
        out = "\n".join(fm) + "\n" + ("\n" + body + "\n" if body else "")
        path = os.path.join(PUB, "%s-%s.md" % (date, slug))
        print("  NEW [%s] %s — %s" % (cat, year, d.get("title","")[:64]))
        if not dry:
            open(path, "w", encoding="utf-8").write(out)
            print("       wrote %s" % os.path.basename(path))

if __name__ == "__main__":
    main()
