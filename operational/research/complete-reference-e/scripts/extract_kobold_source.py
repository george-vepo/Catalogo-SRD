#!/usr/bin/env python3
"""Extract structured 5e Kobold Press source mechanics; NEVER canonize unreviewed records."""
import csv, hashlib, io, json, os, pathlib, re, time, unicodedata, urllib.request, urllib.parse

ROOT=pathlib.Path("operational/research/complete-reference-e")
REPO="george-vepo/SRD-Card-Game-607-Supervisor"
BRANCH="chatgpt/srd607-complete-statblocks-e"
SRC_REPO="TheGiddyLimit/homebrew"
SRC_BRANCH="master"
SOURCE_BOOKS=[
"Tome of Beasts",
"Tome of Beasts 1 (2023 Edition)",
"Tome of Beasts 2",
"Tome of Beasts 3",
"Creature Codex",
]
API="https://api.github.com/repos/"+REPO
TOKEN=os.environ.get("GITHUB_TOKEN","")
if not TOKEN:raise RuntimeError("Missing GITHUB_TOKEN")
HEADERS={"Authorization":"Bearer "+TOKEN,"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"SRD607-mechanics-reference"}
def request(url,headers=None,data=None,method="GET"):
    err=None
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers=headers or {"User-Agent":"SRD607-mechanics-reference"},data=data,method=method),timeout=120) as response:return response.read()
        except Exception as e:err=e;time.sleep(2*(i+1))
    raise RuntimeError(str(err))
def gh(method,path,payload=None):
    data=json.dumps(payload,ensure_ascii=False).encode() if payload is not None else None
    return json.loads(request(API+"/"+path,headers={**HEADERS,"Content-Type":"application/json"},data=data,method=method).decode())
def pub(data,label):
    parent=gh("GET","branches/"+BRANCH)["commit"]["sha"]
    tree=gh("GET","git/commits/"+parent)["tree"]["sha"]
    blob=gh("POST","git/blobs",{"content":data,"encoding":"utf-8"})["sha"]
    newtree=gh("POST","git/trees",{"base_tree":tree,"tree":[{"path":"operational/research/complete-reference-e/source-extractions/kobold_candidates_e.json","mode":"100644","type":"blob","sha":blob}]})["sha"]
    commit=gh("POST","git/commits",{"message":label,"tree":newtree,"parents":[parent]})["sha"]
    if gh("GET","branches/"+BRANCH)["commit"]["sha"]!=parent:raise RuntimeError("Race: branch moved before update")
    gh("PATCH","git/refs/heads/"+BRANCH,{"sha":commit,"force":False})
    return commit
def norm(v):
    return "".join(c for c in unicodedata.normalize("NFKD",v.lower()) if c.isalnum() and not unicodedata.combining(c))
def names(name):
    a=[name]
    parts=[v.strip() for v in name.split(",")]
    if len(parts)>1:
        a.extend([" ".join(parts[1:])," ".join(parts[1:])+" "+parts[0],parts[0]+" "+" ".join(parts[1:])])
    if name.startswith("Animated Instrument, "):a.append(name.split(", ",1)[1])
    if name.startswith("Aboleth, Nihileth, "):a.append(name.split(", ")[-1])
    if name=="Vine Lord, Tendril Puppet":a.append("Tendril Puppet")
    return {norm(v) for v in a}
def source_file(book):
    path="creature/Kobold Press; "+book+".json"
    return "https://raw.githubusercontent.com/"+SRC_REPO+"/"+SRC_BRANCH+"/"+urllib.parse.quote(path,safe="/")
def normalize_type(c):
    if isinstance(c,str):return c
    return json.dumps(c,ensure_ascii=False)
csv_file=pathlib.Path("operational/research/catalog-ledger-20261011-v27/catalog-status.csv")
rows=list(csv.DictReader(io.StringIO(csv_file.read_text(encoding="utf-8-sig")),delimiter=";"))
pending=[r for r in rows if not r["Imagem"].startswith("VERIFICADA")]
target=pending[195:390]
if len(rows)!=607 or len(pending)!=584 or len(target)!=195 or target[0]["ID"]!="TF-059" or target[-1]["ID"]!="TF-269":
    raise RuntimeError("Source CSV scope mismatch")
im=json.loads(pathlib.Path("operational/assets/creature-images/manifests/e.json").read_text(encoding="utf-8"))
image_by_id={r["id"]:r for r in im["entries"]}
source=[]
book_errors=[]
for book in SOURCE_BOOKS:
    try:
        data=json.loads(request(source_file(book)).decode("utf-8-sig"))
        monsters=data.get("monster",[])
        if not monsters:raise ValueError("No 'monster' records")
        for i,v in enumerate(monsters):
            if not v.get("name"):continue
            source.append({"book":book,"index":i,"monster":v,"source_url":source_file(book)})
        print("SOURCE",book,len(monsters),flush=True)
    except Exception as e:
        book_errors.append({"book":book,"error":str(e)})
        print("ERROR",book,str(e),flush=True)
if len(book_errors)>0:print("WARN source books unavailable",len(book_errors),flush=True)
lookup={}
for a in source:
    lookup.setdefault(norm(a["monster"]["name"]),[]).append(a)
core_fields=["name","size","type","ac","hp","speed","str","dex","con","int","wis","cha","cr"]
text_sections=["trait","action","bonus","reaction","legendary","spellcasting","mythic","legendaryGroup"]
data_fields=core_fields+["alignment","save","skill","resist","immune","vulnerable","conditionImmune","senses","passive","languages","environment","conditionInflict"]+text_sections
output=[]
for record in target:
    candidate_map={}
    for alias in names(record["Criatura"]):
        for c in lookup.get(alias,[]):candidate_map[(c["book"],c["index"])]=c
    candidates=list(candidate_map.values())
    img=image_by_id[record["ID"]]
    img_info={"status":img["status"],"path":img.get("path"),"sha256":img.get("sha256"),"verified":img["status"]=="verified"}
    entry={"id":record["ID"],"name":record["Criatura"],"catalog_mechanics":record["Mecanica_completa"],
           "image":img_info,"matches":len(candidates),"status":"NO_EXACT_SOURCE_MATCH","candidates":[]}
    for c in candidates:
        monster=c["monster"]
        present=[f for f in core_fields if f in monster and monster[f] is not None]
        sections=[f for f in text_sections if f in monster and monster[f] not in (None,[],"")]
        missing=[f for f in core_fields if f not in present]
        if not sections:missing.append("actions/traits/spellcasting")
        mechanics={k:monster[k] for k in data_fields if k in monster}
        item={"book":c["book"],"source_file":c["source_url"],"source_index":c["index"],
              "source_label":monster.get("source"),"name":monster["name"],"core_complete":not missing,
              "missing_required_fields":missing,"sections":sections,"mechanics":mechanics,
              "has_unresolved_copy":bool(monster.get("_copy"))}
        if monster.get("_copy"):item["copy_reference"]=monster["_copy"]
        entry["candidates"].append(item)
    if len(candidates)==1 and candidates[0]["monster"] and entry["candidates"][0]["core_complete"] and not entry["candidates"][0]["has_unresolved_copy"]:
        entry["status"]="STRUCTURED_SOURCE_CANDIDATE_PENDING_HUMAN_REVIEW"
    elif len(candidates)>1:
        entry["status"]="EDITION_CONFLICT_REQUIRES_DISAMBIGUATION"
    elif len(candidates)==1:
        entry["status"]="SOURCE_INCOMPLETE_REQUIRES_RESEARCH"
    output.append(entry)

counts={}
for item in output:counts[item["status"]]=counts.get(item["status"],0)+1
payload={"schema":"SRD607_UNREVIEWED_KOBOLD_5ETOOLS_SOURCE_CANDIDATES_V1",
         "warning":"This is a source DATA EXTRACTION, not 195 completed/canonical game cards. Source expressions may contain unexpanded 5etools inline markup. No stat block or artwork is promoted automatically.",
         "base_commit":"a962c48a1169c2ef2be8137715a095a596753b32",
         "partition":"pending_images.slice(195,390)","total":195,
         "books":SOURCE_BOOKS,"book_errors":book_errors,"status_counts":counts,
         "records":output}
text=json.dumps(payload,ensure_ascii=False,indent=2)+"\n"
commit=pub(text,"research(srd607/e): unreviewed full-source Kobold mechanical candidates with image joins")
print("SAVED",commit,"bytes",len(text.encode()),"status",json.dumps(counts),flush=True)
