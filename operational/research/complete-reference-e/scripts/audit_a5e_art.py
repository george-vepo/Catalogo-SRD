#!/usr/bin/env python3
"""Audit A5E named-monster webpage art links; no automatic asset promotion."""
from html.parser import HTMLParser
import json, urllib.parse, urllib.request
PAGES={
"TF-185":"https://a5e.tools/monsters?combine=Alleyway+Strangler",
"TF-200":"https://www.a5e.tools/node/2839",
"TF-201":"https://a5e.tools/node/1721",
"TF-226":"https://a5e.tools/node/1745",
"TF-231":"https://a5e.tools/node/1744",
"TF-232":"https://a5e.tools/monsters?combine=Annelidast",
"TF-263":"https://a5e.tools/node/3295",
"TF-264":"https://a5e.tools/monsters?combine=Abyssal+Hordeling",
}
class Images(HTMLParser):
    def __init__(self):super().__init__();self.images=[]
    def handle_starttag(self,tag,attrs):
        if tag=="img":
            d=dict(attrs)
            if d.get("src"):self.images.append({k:d.get(k) for k in ("src","alt","title","class","width","height")})
        if tag=="a":
            d=dict(attrs)
            if "href" in d and "/node/" in d["href"] and len(self.images)<20:self.images.append({"linked_node":d["href"]})
for id,url in PAGES.items():
    try:
        req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 compatible; SRD607 source audit"})
        with urllib.request.urlopen(req,timeout=30) as resp:html=resp.read().decode("utf-8","replace")
        images=Images();images.feed(html)
        named=[]
        for v in images.images:
            if v.get("src"):
                source=urllib.parse.urljoin(url,v["src"])
                if "/sites/default/files/" in source or "monsters" in source.lower():
                    named.append({**v,"src":source})
        print("IMAGE_AUDIT",id,url,"candidate_count",len(named),json.dumps(named[:15],ensure_ascii=False),flush=True)
    except Exception as e:print("IMAGE_AUDIT_ERROR",id,str(e),flush=True)
