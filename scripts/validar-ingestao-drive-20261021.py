#!/usr/bin/env python3
"""Valida overlay não homologado importado do Drive; sem acessar Drive na CI."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "docs" / "catalogo"
manifest = json.loads((SITE / "data/drive-import-20261021.json").read_text("utf-8"))
mega = json.loads((SITE / "data/megalista-1320.json").read_text("utf-8"))
assert manifest["schema"] == "CATALOGO_DRIVE_IMPORT_V1"
assert len(mega["records"]) == 1320

by_id = {c["ID NO JOGO"]: c for c in mega["records"] if c["ID NO JOGO"]}
by_name = {c["NOME"]: c for c in mega["records"]}
assert len(manifest["artes"]) == 15
assert len(manifest["fichas"]) == 12
ids_art = set()
for art in manifest["artes"]:
    cid, name = art["id_catalogo"], art["nome"]
    assert (cid or name) not in ids_art
    ids_art.add(cid or name)
    assert art["status"].startswith("CANDIDATA_")
    assert art["substitui_arte_aprovada"] is False
    assert art["direitos"] == "CRIADA_PELO_USUARIO_PUBLICACAO_AUTORIZADA_20261021"
    assert "Autorização explícita do autor" in art["permissao_publicacao"]
    record = by_id[cid] if cid else by_name[name]
    assert record["NOME"] == name
    if not cid:
        assert record["ID NO JOGO"] == ""
    rel = Path(art["arquivo"])
    assert rel.parts[:2] == ("assets", "drive-candidatas-20261021")
    full = SITE / rel
    assert full.is_file(), str(full)
    raw = full.read_bytes()
    if rel.suffix.lower() == ".webp":
        assert 150_000 <= len(raw) <= 2_000_000, len(raw)
        assert raw[:4] == b"RIFF" and raw[8:12] == b"WEBP"
    elif rel.suffix.lower() == ".png":
        assert art["preview_na_grade"] is False, "Novas candidatas só no detalhe"
        assert 100_000 <= len(raw) <= 5_000_000, len(raw)
        assert raw.startswith(b"\x89PNG\r\n\x1a\n"), "Assinatura PNG inválida"
    else:
        raise AssertionError("Formato de imagem não permitido: " + str(rel))
    print("arte candidata OK:", cid or name, len(raw), "bytes")

ids_sheet = set()
for entry in manifest["fichas"]:
    cid, name = entry["id_catalogo"], entry["nome"]
    assert cid not in ids_sheet
    ids_sheet.add(cid)
    assert cid.startswith("AT-"), "Este lote importa apenas conteúdo SRD 5.2.1"
    assert by_id[cid]["NOME"] == name
    assert entry["edicao"] == "SRD 5.2.1"
    assert "SEM_HOMOLOGACAO" in entry["status"]
    assert entry["substitui_ficha_base"] is False
    rel = Path(entry["arquivo"])
    assert rel.parts[:2] == ("data", "drive-fichas-srd-20261021")
    full = SITE / rel
    assert full.is_file(), str(full)
    item = json.loads(full.read_text("utf-8"))
    identificacao = item.get("identificacao") or {}
    actual = identificacao.get("id_catalogo") or identificacao.get("ID_CATALOGO") or item.get("ID_CATALOGO")
    assert actual == cid, (cid, actual)
    print("ficha SRD complementar OK:", cid, len(full.read_bytes()), "bytes")

script = (SITE / "app.js").read_text("utf-8")
assert "driveImport.artes" in script and "driveImport.fichas" in script
assert "carregarFichaDrive" in script and "drive-candidatas-20261021" in script
assert "const existingArt=artSrc(web)?web:'';" in script, "Arte principal já existente deve ter precedência"
assert "const art=existingArt || (artIsDrive?driveArt.arquivo:'');" in script
assert "driveArt?.id_catalogo===id" in script, "Só a identidade canônica exata pode receber imagem"
assert "drive-art-notice" in script, "Prévia precisa de rótulo de revisão"
assert "const driveArt=driveArtById.get(id)" in script
assert "driveFicha:driveFichaById.get(id)" in script
assert "const artIsDrive=" in script
assert "driveArt?.id_catalogo===id" in script
assert "Arte do autor · em revisão" in script
assert "driveArt?.preview_na_grade!==false" in script
assert "ficha.identificacao?.ID_CATALOGO" in script
print("Validação completa: 1320 registros preservados; 15 artes autorais e 12 fichas SRD complementares.")
