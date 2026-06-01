# -*- coding: utf-8 -*-
"""Regenerate the Works-in-progress entries (_publications/*-wip-NN.md) from a
hardcoded paper list, pulling abstracts from the Zotero "My Working Papers"
collection (D3IVWRX8). Run after updating a working paper's abstract in Zotero:
    python scripts/sync_wip.py
Papers with an abstract are auto-sorted to the top by the publications page rule.
"""
import os, re, json
PUB=os.path.expanduser("~/Library/CloudStorage/Dropbox/projects/woochangkang.github.io/_publications")
for f in os.listdir(PUB):
    if "wip-" in f: os.remove(os.path.join(PUB,f))
def cred():
    env=json.load(open(os.path.expanduser("~/.claude/settings.json"))).get("env",{})
    return os.environ.get("ZOTERO_USER_ID") or env.get("ZOTERO_USER_ID"), os.environ.get("ZOTERO_API_KEY") or env.get("ZOTERO_API_KEY")
uid,key=cred()
from pyzotero import zotero
zot=zotero.Zotero(uid,'user',key)
def tidy(t):
    t=t.replace('\r\n','\n').replace('\r','\n'); t=re.sub(r'^\s*abstract\s*[:.]?\s*','',t,flags=re.I)
    t=re.sub(r'([a-z])-\n([a-z])',r'\1\2',t); t=re.sub(r'\s*\n\s*',' ',t); t=re.sub(r'[ \t]{2,}',' ',t).strip()
    return t.replace('---','—').replace('--','–').replace('bene ts','benefits')
absmap={}
for it in zot.everything(zot.collection_items('D3IVWRX8')):
    d=it['data']
    if d.get('itemType')=='journalArticle' and d.get('abstractNote'): absmap[d['title'][:30]]=tidy(d['abstractNote'])
def bold(a):
    for n in ("Woo Chang Kang","Kang, Woo Chang"): a=a.replace(n,"<strong>%s</strong>"%n)
    return a
def q(s): return '"'+s.replace('"','\\"')+'"'
# abstract-having papers FIRST
WIP=[
("Politics of Face: Gender Typicality, Perceived Competence and Electoral Viability","Kang, Woo Chang",["Face","Gender","South Korea"]),
("Democratic Accountability in East Asia: A Comparative Experimental Study of Voter Responses to Norm Violations","Kang, Woo Chang, Sunkyoung Park, Osbern Huang, Koh Iwabuchi and Tetsuro Kobayashi",["Public Opinion","Cross-national Studies","US"]),
("Housing Prices, Rental Prices, and Perceptions about the Economy: Evidence from South Korea","Kang, Woo Chang and Sein Park",["Real Estate Price","Inequality","Public Opinion","South Korea"]),
("Depressive Symptoms Around the 2025 South Korean Presidential Election: The Roles of Voting, Electoral Outcomes, and Manipulation Beliefs","Kang, Woo Chang, June Kang, Kyu-Man Han",["Public Opinion","Elections","South Korea"]),
("Correcting Political Misperceptions to Rebuild Norms of Good Citizenship in Polarized Democracies: Evidence from South Korea","Kang, Woo Chang and Hannah Kim",["Polarization","Public Opinion","South Korea"]),
("Online Media Fragmentation and Political Polarization: A Cross-National Analysis of 51 Countries","Kang, Woo Chang and Hong-gie Kim",["Polarization","Cross-national Studies"]),
("Unraveling Gender Bias in Candidate Evaluations through the Analysis of Representativeness, Competence, and Electability","Kang, Woo Chang",["Gender","Public Opinion"]),
("How Does International Naming and Shaming Affect South Korean Attitudes Toward Refugees?","Kang, Woo Chang and Han Il Chang",["Immigration","Public Opinion","South Korea"]),
("Electoral Effect of Stop and Frisk","Kang, Woo Chang and Chris Dawes",["Elections","US"]),
]
for i,(title,auth,tags) in enumerate(WIP):
    n=i+1; date="2030-%02d-01"%(10-i); ab=absmap.get(title[:30],"")
    fm=["---",f"title: {q(title)}","collection: publications","category: wip",'year: ""',
        f"authors: {q(bold(auth))}",'venue: ""','detail: ""',f"date: {date}",
        f"permalink: /publications/wip-{n:02d}","tags: ["+", ".join(q(t) for t in tags)+"]","---"]
    open(os.path.join(PUB,f"{date}-wip-{n:02d}.md"),"w",encoding="utf-8").write("\n".join(fm)+"\n"+("\n"+ab+"\n" if ab else ""))
print("regenerated; abstract papers first (wip-01,02)")
