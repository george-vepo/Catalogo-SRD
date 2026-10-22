#!/usr/bin/env python3
"""Importa artes autorais locais do Drive como WebP candidatos, sem homologá-las.

Execução deliberadamente LOCAL: o GitHub Actions não possui acesso ao Drive privado.
Nenhuma transferência de ID/URL do Google Drive para o repositório.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "docs/catalogo"
MEGA = SITE / "data/megalista-1320.json"
MANIFEST = SITE / "data/drive-import-20261021.json"
ASSETS = SITE / "assets/drive-candidatas-20261021"
ID_RE = re.compile(r"^(AT-\d{3}|TF-\d{3}|EXT-\d{4}|KP-[A-Z]\d{3})-(.+)$", re.I)
ALLOWED_EXT = {".png", ".webp"}
MAX_IMAGE_BYTES = 2_000_000
MAX_PIXELS = 10_000_000


def slug(value: str) -> str:
    ascii_name = unicodedata.normalize("NFKD", value)
    ascii_name = "".join(ch for ch in ascii_name if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "-", ascii_name.casefold()).strip("-")


def index_source(source: Path, catalog: dict, existing_ids: set[str]):
    """Seleciona apenas candidatos inequívocos; variantes distintas exigem revisão."""
    grouped = defaultdict(list)
    refusals = Counter()
    blocked_hashes = set()
    all_candidates = []

    for path in sorted(source.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in ALLOWED_EXT:
            continue
        original = path.stem.lower()
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if "rejeitad" in original or "revisar" in original or "revisao" in original:
            blocked_hashes.add(digest)
            refusals["revisao_ou_rejeicao"] += 1
            continue
        if "candidata-nao-homologada" not in original and "candidata_nao_homologada" not in original:
            refusals["sem_rotulo_candidato_esperado"] += 1
            continue
        title = path.stem.split("__", 1)[0].strip()
        match = ID_RE.fullmatch(title)
        if not match:
            refusals["id_ausente_ou_formato_invalido"] += 1
            continue
        cid, file_slug = match.group(1).upper(), match.group(2)
        record = catalog.get(cid)
        if record is None:
            refusals["id_fora_catalogo"] += 1
            continue
        if slug(file_slug) != slug(record["NOME"]):
            refusals["nome_diverge_do_catalogo"] += 1
            continue
        if cid in existing_ids:
            refusals["ja_no_manifesto"] += 1
            continue
        all_candidates.append((cid, digest))
        grouped[cid].append((path, digest, record))

    digest_ids = defaultdict(set)
    for cid, digest in all_candidates:
        digest_ids[digest].add(cid)

    selected = []
    for cid, entries in sorted(grouped.items()):
        hashes = {digest for _, digest, _ in entries}
        if hashes & blocked_hashes:
            refusals["imagem_tambem_marcada_para_revisao"] += 1
        elif len(hashes) != 1:
            refusals["variantes_visuais_conflitantes"] += 1
        elif len(digest_ids[next(iter(hashes))]) > 1:
            refusals["mesma_imagem_para_criaturas_diferentes"] += 1
        else:
            selected.append((cid, min(entries, key=lambda x: (len(x[0].name), x[0].name))))
    return selected, refusals


def convert_webp(source: Path, *, strict: bool = True) -> bytes:
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise RuntimeError("Instale Pillow: python -m pip install Pillow") from exc
    import io

    with Image.open(source) as original:
        original.load()
        if strict and original.width * original.height > MAX_PIXELS:
            raise ValueError(f"Imagem grande demais: {source.name}")
        image = ImageOps.exif_transpose(original)
        image.thumbnail((960, 1440), Image.Resampling.LANCZOS)
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
        buffer = io.BytesIO()
        image.save(buffer, format="WEBP", quality=79, method=6)
        data = buffer.getvalue()
        if not data.startswith(b"RIFF") or data[8:12] != b"WEBP":
            raise ValueError("Codificação WebP inválida")
        if strict and not 5_000 <= len(data) <= MAX_IMAGE_BYTES:
            raise ValueError(f"Tamanho WebP inesperado ({len(data)}): {source.name}")
        return data


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path, help="Pasta local sincronizada de Imagens/Novas")
    parser.add_argument("--apply", action="store_true", help="Sem esta opção: apenas simula, sem escrever arquivos")
    parser.add_argument("--limit", type=int, default=20, help="Máximo de novas artes por execução (1 a 50)")
    parser.add_argument("--ids", help="Filtrar IDs separados por vírgula, ex.: AT-003,AT-009")
    args = parser.parse_args(argv)

    source = args.source.resolve()
    if not source.is_dir():
        parser.error(f"Pasta não encontrada: {source}")
    if not 1 <= args.limit <= 50:
        parser.error("--limit precisa estar entre 1 e 50")
    if source == ROOT or ROOT in source.parents:
        parser.error("A fonte precisa estar fora do repositório para evitar reimportar assets")

    mega = json.loads(MEGA.read_text("utf-8"))
    manifest = json.loads(MANIFEST.read_text("utf-8"))
    if len(mega["records"]) != 1320:
        raise RuntimeError("Catálogo mudou: interrompido para auditoria")
    catalog = {x["ID NO JOGO"]: x for x in mega["records"] if x["ID NO JOGO"]}
    existing_ids = {x["id_catalogo"] for x in manifest["artes"] if x["id_catalogo"]}
    selected, refusals = index_source(source, catalog, existing_ids)
    allowed_ids = {x.strip().upper() for x in args.ids.split(",")} if args.ids else None
    if allowed_ids is not None:
        unknown = allowed_ids - set(catalog)
        if unknown:
            parser.error("IDs inexistentes no catálogo: " + ", ".join(sorted(unknown)))
        selected = [x for x in selected if x[0] in allowed_ids]
    batch = selected[:args.limit]

    print(json.dumps({
        "modo": "APLICAR" if args.apply else "SIMULACAO",
        "elegiveis_univocos": len(selected), "lote": [x[0] for x in batch],
        "descartes_por_motivo": dict(refusals),
        "total_manifesto_antes": len(manifest["artes"]),
    }, ensure_ascii=False, indent=2))

    if not args.apply or not batch:
        return 0
    output = []
    for cid, (path, sha_original, record) in batch:
        name = f"{cid.lower()}-{slug(record['NOME'])}.webp"
        dest = ASSETS / name
        if dest.exists():
            raise FileExistsError(f"Não sobrescrever asset existente: {dest}")
        binary = convert_webp(path)
        output.append((dest, binary, {
            "id_catalogo": cid,
            "nome": record["NOME"],
            "arquivo": f"assets/drive-candidatas-20261021/{name}",
            "status": "CANDIDATA_NOVAS_NAO_HOMOLOGADA",
            "origem_arquivo": path.name,
            "revisao_visual": "Arte do autor ainda sem homologação. Exibir somente nos detalhes.",
            "direitos": "CRIADA_PELO_USUARIO_PUBLICACAO_AUTORIZADA_20261021",
            "permissao_publicacao": "Autorização explícita do autor no chat em 2026-10-21 para publicar as imagens no Catálogo SRD.",
            "preview_na_grade": False,
            "substitui_arte_aprovada": False,
            "sha256_origem": sha_original,
            "sha256_webp": hashlib.sha256(binary).hexdigest(),
        }))
    ASSETS.mkdir(parents=True, exist_ok=True)
    for path, binary, record in output:
        path.write_bytes(binary)
        manifest["artes"].append(record)
    manifest["contagens_lote"]["artes"] = len(manifest["artes"])
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print(f"Importadas {len(output)} artes EM REVISAO. Confira git diff e execute os testes antes de publicar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
