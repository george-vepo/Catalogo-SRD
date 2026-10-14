#!/usr/bin/env python3
"""GitHub-native, binary-only image acquisition for SRD Card Game 607 group E."""
import base64, hashlib, io, json, os, pathlib, time, urllib.parse, urllib.request
from PIL import Image

REPO="george-vepo/SRD-Card-Game-607-Supervisor"
BRANCH="chatgpt/srd607-image-assets-e"
BASE="a962c48a1169c2ef2be8137715a095a596753b32"
ROOT="operational/assets/creature-images"
MPATH=ROOT+"/manifests/e.json"
RPATH=ROOT+"/reports/e.md"
TOKEN=os.environ["GITHUB_TOKEN"]
API="https://api.github.com/repos/"+REPO
HEADERS={"Authorization":"Bearer "+TOKEN,"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"SRD607-Image-E"}

def send(method,endpoint,payload=None):
    data=None if payload is None else json.dumps(payload,ensure_ascii=False).encode()
    for attempt in range(3):
        req=urllib.request.Request(API+"/"+endpoint,data=data,method=method,headers={**HEADERS,"Content-Type":"application/json"})
        try:
            with urllib.request.urlopen(req,timeout=75) as response:
                return json.loads(response.read().decode())
        except Exception:
            if attempt==2: raise
            time.sleep(attempt+1)

def remote(url):
    for attempt in range(3):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"SRD607-Image-E"})
            with urllib.request.urlopen(req,timeout=90) as response: return response.read()
        except Exception:
            if attempt==2: raise
            time.sleep(attempt+1)

def head():return send("GET","branches/"+BRANCH)["commit"]["sha"]
def tree(sha):return send("GET","git/commits/"+sha)["tree"]["sha"]
def blob(data,encoding):
    return send("POST","git/blobs",{"content":data,"encoding":encoding})["sha"]
def bin_blob(data):
    return blob(base64.b64encode(data).decode(),"base64")
def txt_blob(data):return blob(data,"utf-8")

def publish(entries,message):
    parent=head()
    obj=send("POST","git/trees",{"base_tree":tree(parent),"tree":[{"path":e[0],"mode":"100644","type":"blob","sha":e[1]} for e in entries]})
    commit=send("POST","git/commits",{"message":message,"tree":obj["sha"],"parents":[parent]})["sha"]
    if head()!=parent: raise RuntimeError("RACE: branch moved while creating commit")
    send("PATCH","git/refs/heads/"+BRANCH,{"sha":commit,"force":False})
    for verification_attempt in range(12):
        if head()==commit:break
        time.sleep(1)
    else:raise RuntimeError("RACE: new commit not branch HEAD after retries")
    return commit

def readback(path):
    item=send("GET","contents/"+urllib.parse.quote(path,safe="/")+"?ref="+urllib.parse.quote(BRANCH,safe=""))
    return base64.b64decode(item["content"]),item["sha"]

def inspect(data,extension):
    if len(data)<1024 or len(data)>20000000:raise ValueError("size invalid")
    if extension=="webp" and (data[:4]!=b"RIFF" or data[8:12]!=b"WEBP"):raise ValueError("WebP signature invalid")
    if extension=="png" and data[:8]!=b"\x89PNG\r\n\x1a\n":raise ValueError("PNG signature invalid")
    if extension in ("jpg","jpeg") and data[:2]!=b"\xff\xd8":raise ValueError("JPEG signature invalid")
    with Image.open(io.BytesIO(data)) as im:
        size=im.size;fmt=im.format.lower();im.verify()
    with Image.open(io.BytesIO(data)) as im:im.load()
    if min(size)<32 or max(size)>15000:raise ValueError("dimensions invalid")
    if fmt!=("jpeg" if extension in ("jpg","jpeg") else extension):raise ValueError("format invalid")
    return size

def scope_check(m):
    lines=pathlib.Path("operational/research/catalog-ledger-20261011-v27/catalog-status.csv").read_text(encoding="utf-8-sig").splitlines()[1:]
    parsed=[line.split(";") for line in lines if line.strip()]
    pending=[(r[0],r[1]) for r in parsed if not r[5].startswith("VERIFICADA")]
    selected=pending[195:390]
    if len(parsed)!=607 or len(pending)!=584 or len(selected)!=195:raise RuntimeError("CSV scope count mismatch")
    if [(r["id"],r["creature"]) for r in m["entries"]]!=selected:raise RuntimeError("manifest scope IDs mismatch")
    if m["base_commit"]!=BASE or m["scope"]!="pending_images.slice(195,390)":raise RuntimeError("manifest base mismatch")

def report(m):
    done=[x for x in m["entries"] if x["status"]=="verified"]
    missing=[x for x in m["entries"] if x["status"]!="verified"]
    lines=["# SRD Card Game 607 — Imagens E","", "**Armazenadas e verificadas: %d / 195.**" % len(done),
           "", "Branch: "+BRANCH, "Commit-base: "+BASE, "",
           "## Checkpoints de imagens (máximo dez arquivos por commit)", ""]
    for x in m["checkpoints"]:
        lines.append("- https://github.com/"+REPO+"/commit/"+x["commit"]+" — "+str(x["verified"])+"/"+str(x["total"])+" verificadas: "+", ".join(x["ids"]))
    lines.extend(["","## Binários publicados e conferidos",""])
    for x in done:
        lines.append("- "+x["id"]+" / "+x["creature"]+": "+x["path"]+
                     "; origem: "+x["source_url"]+"; "+str(x["bytes"])+" bytes; "+
                     str(x["width"])+"x"+str(x["height"])+" px; SHA-256: "+x["sha256"]+
                     "; commit: "+x["commit"])
    lines.extend(["","## Ressalvas de identidade e adequação editorial",""])
    noted=[x for x in done if x.get("source_note")]
    for x in noted:
        lines.append("- "+x["id"]+" / "+x["creature"]+": "+x["source_note"])
    if not noted: lines.append("Nenhuma ressalva adicional registrada.")
    lines.extend(["","## Não obtidos",""])
    for x in missing:
        lines.append("- "+x["id"]+" / "+x["creature"]+": "+x["status"]+"; "+x.get("error",""))
        if x.get("research_note"):
            lines.append("  - Investigação: "+x["research_note"])
        if x.get("source_reference"):
            lines.append("  - Referência: "+x["source_reference"])
        if x.get("rejected_candidate"):
            lines.append("  - Candidato rejeitado: "+x["rejected_candidate"])
    lines.extend(["","## Duplicações e ressalvas",""])
    dup=[x for x in missing if x["status"]=="duplicate_suspected"]
    lines.extend([x["id"]+": "+x["error"] for x in dup] if dup else ["Nenhuma duplicação de SHA-256 encontrada entre os binários aprovados."])
    lines.extend(["","Validações: formato, assinatura, dimensões, decodificação integral, tamanho, SHA-256, blob e releitura real do GitHub.",
                  "A correspondência da criatura usa o nome do arquivo da fonte, sem afirmar revisão visual humana.",
                  "Nenhuma alteração no CSV, ledger global, main, PR #1 ou imagens D/F.",""])
    return "\n".join(lines)

def checkpoint_manifest(m):
    m["verified"]=sum(x["status"]=="verified" for x in m["entries"])
    m["not_found"]=sum(x["status"]=="source_not_found" for x in m["entries"])
    m["remaining"]=195-m["verified"]
    commit=publish([(MPATH,txt_blob(json.dumps(m,ensure_ascii=False,indent=2)+"\n")),
                    (RPATH,txt_blob(report(m)))],
                   "docs(srd607/e): checkpoint manifest and integrity report")
    print("AUDIT",commit,m["verified"],"/195",flush=True)

def main():
    m=json.loads(pathlib.Path(MPATH).read_text(encoding="utf-8"))
    scope_check(m)
    existing={x["sha256"]:x["id"] for x in m["entries"] if x["status"]=="verified"}
    queue=[x for x in m["entries"] if x["status"]=="pending" and x.get("source_candidate")]
    batch=[]
    print("PREFLIGHT",head(),"queue",len(queue),"verified",len(existing),flush=True)
    if not queue:
        print("NO_PENDING_IMAGE_CANDIDATES: preserve existing report and manifest",flush=True)
        return
    def flush():
        nonlocal batch
        if not batch:return
        if len(batch)>10:raise RuntimeError("checkpoint image count > 10")
        image_commit=publish([(x["path"],x["blob"]) for x in batch],
                             "assets(srd607/e): real binaries "+batch[0]["entry"]["id"]+" to "+batch[-1]["entry"]["id"])
        verified=0
        for x in batch:
            e=x["entry"]
            try:
                returned,sha=readback(x["path"])
                if sha!=x["blob"] or hashlib.sha256(returned).hexdigest()!=x["digest"]:
                    raise ValueError("readback mismatched binary or SHA-256")
                e.update(status="verified",path=x["path"],source_url=x["source"],
                         bytes=x["size"],width=x["dimensions"][0],height=x["dimensions"][1],
                         extension=x["ext"],sha256=x["digest"],blob_sha=x["blob"],
                         commit=image_commit,verified_readback=True)
                existing[x["digest"]]=e["id"];verified+=1
            except Exception as error:
                e.update(status="published_unverified",path=x["path"],commit=image_commit,
                         verified_readback=False,error=str(error))
                m["errors"].append({"id":e["id"],"stage":"readback","error":str(error)})
        m["checkpoints"].append({"commit":image_commit,"ids":[x["entry"]["id"] for x in batch],
                                  "total":len(batch),"verified":verified})
        print("IMAGES",image_commit,verified,"/",len(batch),flush=True)
        batch=[]
        checkpoint_manifest(m)
    for e in queue:
        try:
            rel=e["source_candidate"]
            ext=rel.rsplit(".",1)[-1].lower()
            source_repo=e.get("source_repo","TheGiddyLimit/homebrew")
            source_ref=e.get("source_ref","master")
            address=e.get("source_url_direct") or "https://raw.githubusercontent.com/"+source_repo+"/"+source_ref+"/"+urllib.parse.quote(rel,safe="/")
            data=remote(address)
            dimensions=inspect(data,ext)
            digest=hashlib.sha256(data).hexdigest()
            repeated=existing.get(digest) or next((x["entry"]["id"] for x in batch if x["digest"]==digest),None)
            if repeated:
                e.update(status="duplicate_suspected",error="same SHA-256 as "+repeated)
                continue
            sha=bin_blob(data)
            batch.append({"entry":e,"path":ROOT+"/"+e["id"]+"."+ext,"blob":sha,"size":len(data),
                          "dimensions":dimensions,"digest":digest,"ext":ext,
                          "source":e.get("source_page") or "https://github.com/"+source_repo+"/blob/"+source_ref+"/"+urllib.parse.quote(rel,safe="/")})
            if len(batch)==10:flush()
        except Exception as error:
            e.update(status="blocked",error=str(error)[:500])
            m["errors"].append({"id":e["id"],"stage":"acquisition","error":e["error"]})
            print("BLOCKED",e["id"],e["error"],flush=True)
    flush()
    checkpoint_manifest(m)
    print("FINAL",m["verified"],"/195",flush=True)

if __name__=="__main__":main()
