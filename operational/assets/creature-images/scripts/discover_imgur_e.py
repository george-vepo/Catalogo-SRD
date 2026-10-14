#!/usr/bin/env python3
"""Read-only Imgur gallery discovery for unresolved SRD607 E creature images.
Only publishes an auditable candidate report. Does NOT mark images verified.
"""
import datetime, json, pathlib, re, urllib.request
from acquire_e import MPATH, ROOT, publish, txt_blob, head, BASE, BRANCH

ID="2iqzhTv"
URLS=[
 "https://api.imgur.com/post/v1/albums/"+ID+"?client_id=546c25a59c58ad7&include=media",
 "https://imgur.com/ajaxalbums/getimages/"+ID+"/hit.json",
 "https://api.imgur.com/3/album/"+ID+"/images",
]
def get(url):
 headers={"User-Agent":"Mozilla/5.0 (compatible; SRD607-creature-asset-research/1.0)",
          "Accept":"application/json"}
 if "/3/album/" in url:headers["Authorization"]="Client-ID 546c25a59c58ad7"
 req=urllib.request.Request(url,headers=headers)
 with urllib.request.urlopen(req,timeout=35) as res:
  raw=res.read(20000000)
  return json.loads(raw),len(raw)
def find(o, parent="",depth=0):
 if depth>12:return
 if isinstance(o,dict):
  for key,val in o.items():
   if isinstance(val,(dict,list)):yield from find(val,parent+"/"+key,depth+1)
  if any(isinstance(o.get(k),str) for k in ("title","description","caption","name","alt")):
   yield parent,o
 elif isinstance(o,list):
  for i,val in enumerate(o):
   yield from find(val,parent+"/"+str(i),depth+1)
def main():
 m=json.loads(pathlib.Path(MPATH).read_text())
 outstanding=[x for x in m["entries"] if x["status"]!="verified"]
 report={"schema":"SRD607_IMGUR_DISCOVERY_V1","timestamp":datetime.datetime.now(datetime.timezone.utc).isoformat(),
         "manifest_verified_at_start":m["verified"],"scope":m["scope"],"album":"https://imgur.com/gallery/tome-of-beasts-ready-3d-printing-free-2iqzhTv",
         "queries":[{"id":x["id"],"creature":x["creature"]} for x in outstanding],
         "endpoints":[],"matches":[],"note":"Research only. No binary acquired or validated by this script."}
 for url in URLS:
  try:
   obj,size=get(url)
   listing=list(find(obj))
   result={"url":url,"ok":True,"response_bytes":size,"matched_media_records":len(listing),"top_level_keys":list(obj)[:20] if isinstance(obj,dict) else None}
   report["endpoints"].append(result)
   for loc,it in listing:
    text=" ".join(str(it.get(k,"")) for k in ("title","description","caption","name","alt"))
    normalized=re.sub(r"[^a-z0-9]+"," ",text.lower()).strip()
    for target in outstanding:
     name=target["creature"].lower()
     variants=[name]
     if target["id"]=="TF-239":variants.append("nihilethic dominator")
     if target["id"]=="TF-099":variants.append("ankou")
     for phrase in variants:
      p=re.sub(r"[^a-z0-9]+"," ",phrase).strip()
      if p and p in normalized:
       report["matches"].append({"id":target["id"],"creature":target["creature"],
          "location":loc,"snippet":text[:600],
          "url":it.get("url") or it.get("link") or it.get("original") or it.get("hash"),
          "record":{k:it.get(k) for k in ("id","url","link","type","mime_type","title","description","name","alt","width","height") if k in it}})
       break
   if listing:break
  except Exception as ex:
   report["endpoints"].append({"url":url,"ok":False,"error":str(ex)[:300]})
 out=ROOT+"/reports/imgur-discovery-e.json"
 data=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
 if not any(r["ok"] for r in report["endpoints"]):
  print("NO IMGUR DATA",[(x["url"],x.get("error")) for x in report["endpoints"]],flush=True)
 print("DISCOVERY RESULTS",len(report["matches"]),flush=True)
 for hit in report["matches"][:40]:print(hit["id"],hit["url"],hit["snippet"][:160],flush=True)
 commit=publish([(out,txt_blob(data))],"research(srd607/e): audit Imgur 400+ creature minis for missing image IDs")
 print("RESEARCH_REPORT",out,"COMMIT",commit,flush=True)

if __name__=="__main__":main()
