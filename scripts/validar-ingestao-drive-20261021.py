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
assert len(manifest["artes"]) >= 19
assert manifest["contagens_lote"]["artes"] == len(manifest["artes"])
assert len(manifest["fichas"]) >= 14
assert manifest["contagens_lote"].get("fichas", len(manifest["fichas"])) == len(manifest["fichas"])
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
        assert 5_000 <= len(raw) <= 2_000_000, len(raw)
        assert raw[:4] == b"RIFF" and raw[8:12] == b"WEBP"
        if art.get("sha256_webp"):
            import hashlib
            assert hashlib.sha256(raw).hexdigest() == art["sha256_webp"], "Hash WebP incorreto"
    elif rel.suffix.lower() == ".png":
        assert art["preview_na_grade"] is False, "Novas candidatas só no detalhe"
        assert 100_000 <= len(raw) <= 5_000_000, len(raw)
        assert raw.startswith(b"\x89PNG\r\n\x1a\n"), "Assinatura PNG inválida"
    else:
        raise AssertionError("Formato de imagem não permitido: " + str(rel))
    print("arte candidata OK:", cid or name, len(raw), "bytes")

ids_sheet = set()
local_hashes = set()
for art in manifest.get("artes_locais", []):
    import hashlib
    assert art["sha256_origem"] not in local_hashes
    local_hashes.add(art["sha256_origem"])
    assert all("rejeitada" not in name.casefold() for name in art["origens"])
    rel = Path(art["arquivo"])
    assert rel.parts[:2] == ("assets", "drive-locais")
    raw = (SITE / rel).read_bytes()
    assert raw[:4] == b"RIFF" and raw[8:12] == b"WEBP"
    assert hashlib.sha256(raw).hexdigest() == art["sha256_webp"]
    if art["nome_catalogo"]:
        record = by_id[art["id_catalogo"]] if art["id_catalogo"] else by_name[art["nome_catalogo"]]
        assert record["NOME"] == art["nome_catalogo"]
print("Acervo local OK:", len(local_hashes), "imagens")
for entry in manifest["fichas"]:
    cid, name = entry["id_catalogo"], entry["nome"]
    identity = cid or name
    assert identity not in ids_sheet
    ids_sheet.add(identity)
    rel = Path(entry["arquivo"])
    if rel.parts[:2] == ("data", "drive-fichas-local"):
        record = by_id[cid] if cid else by_name[name]
        assert record["NOME"] == name and record["ID NO JOGO"] == cid
        item = json.loads((SITE / rel).read_text("utf-8"))
        assert item["schema"] == "CATALOGO_FICHA_LOCAL_V1"
        assert item["id_catalogo"] == cid and item["nome_catalogo"] == name
        assert isinstance(item["conteudo_original"], dict)
        assert item["sha256_origem"] == entry["sha256_origem"]
        assert len(item["sha256_origem"]) == 64
        assert entry["substitui_ficha_base"] is False
        assert "SEM_HOMOLOGACAO" in entry["status"]
        print("ficha local complementar OK:", identity)
        continue
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
    actual = identificacao.get("id_catalogo") or identificacao.get("ID_CATALOGO") or item.get("ID_CATALOGO") or item.get("id_catalogo")
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
assert "driveFicha:(id?driveFichaById.get(id):driveFichaByName.get(m.NOME))" in script
assert "const artIsDrive=" in script
assert "driveArt?.id_catalogo===id" in script
assert "Arte do autor · em revisão" in script
assert "driveArt?.preview_na_grade!==false" in script
assert "ficha.identificacao?.ID_CATALOGO" in script
assert "ficha.id_catalogo" in script, "Fichas JSON planas do Drive precisam de validação de ID"
print(f"Validação completa: 1320 registros preservados; {len(manifest['artes'])} artes candidatas e {len(manifest['fichas'])} fichas complementares.")


# Auditoria de metadados do Drive Novas (não altera catálogo nem aprova arte).
auditoria = json.loads((ROOT / "auditoria/drive-novas-inventario-20261021.json").read_text("utf-8"))
assert auditoria["schema"] == "CATALOGO_DRIVE_NOVAS_AUDITORIA_V1"
resumo = auditoria["resumo"]
correspondencias = auditoria["correspondencias"]
assert resumo["arquivos"] == 567 and resumo["paginas"] == 6
assert sum(resumo["por_rotulo"].values()) == resumo["arquivos"]
assert resumo["correspondencias_com_catalogo"] == len(correspondencias)
assert len(set(x["id_catalogo"] for x in correspondencias)) == resumo["ids_distintos"]
assert resumo["sem_correspondencia"] + len(correspondencias) == resumo["arquivos"]
assert sum(not x["ja_no_manifesto"] for x in correspondencias) == resumo["correspondencias_nao_manifestadas"]
for item in correspondencias:
    assert item["id_catalogo"] in by_id
    assert by_id[item["id_catalogo"]]["NOME"] == item["nome"]
    assert item["status"] in {"CANDIDATA", "REVISAR", "REJEITADA"}
    # ja_no_manifesto registra a fotografia da auditoria de 21/10, não o estado atual.
    # Novas integrações podem adicionar um ID que naquela data ainda não estava importado.
    if item["ja_no_manifesto"]:
        assert any(a["id_catalogo"] == item["id_catalogo"] for a in manifest["artes"]), item["id_catalogo"]
print("Auditoria Drive Novas OK: 567 arquivos; correspondências cruzadas sem homologação.")

# Reconciliação não destrutiva entre catálogo ativo 635 e megalista histórica.
concil = json.loads((ROOT / "auditoria/catalogo-ativo-v2-635-vs-megalista-1320-20261021.json").read_text("utf-8"))
assert concil["schema"] == "SRD_CATALOGO_CONCILIACAO_V1"
ids_ativos = concil["ids_ativos_635"]
ausentes = concil["ids_ativos_ausentes_web"]
assert len(ids_ativos) == len(set(ids_ativos)) == 635
assert len(ausentes) == 29
assert len(by_id) == 606
assert len(mega["records"]) - len(by_id) == 714
ids_ausentes = {item["id_catalogo"] for item in ausentes}
assert len(ids_ausentes) == len(ausentes)
assert set(ids_ativos) - set(by_id) == ids_ausentes
assert set(by_id) - set(ids_ativos) == set()
assert sum(item["situacao_catalogo"] == "PRESERVADA" for item in ausentes) == 28
assert sum(item["situacao_catalogo"] != "PRESERVADA" for item in ausentes) == 1
assert {item["id_catalogo"] for item in ausentes if item["situacao_catalogo"] != "PRESERVADA"} == {"KP-S007"}
assert all(item["id_catalogo"] not in by_id for item in ausentes)
print("Conciliação ativa 635 × megalista 1320 OK: 606 IDs comuns, 29 sem correspondência.")


# Consulta isolada, somente leitura, com 635 IDs reais extraídos do XLSX canônico.
preview_path = SITE / "data/catalogo-ativo-635-consulta-20261021.json"
consulta = json.loads(preview_path.read_text("utf-8"))
assert consulta["schema"] == "SRD_CATALOGO_ATIVO_CONSULTA_PRELIMINAR_V1"
assert consulta["resumo"] == {
    "total_ativos_planilha": 635,
    "ids_ja_na_megalista_web": 606,
    "ids_ausentes_megalista_web": 29,
}
assert len(consulta["sha256_fonte_xlsx"]) == 64
linhas = consulta["registros"]
assert len(linhas) == 635
ids_consulta = [r["id"] for r in linhas]
assert len(ids_consulta) == len(set(ids_consulta)) == 635
assert set(ids_consulta) == set(concil["ids_ativos_635"])
assert sum(bool(r["id_na_megalista_web"]) for r in linhas) == 606
assert sum(not r["id_na_megalista_web"] for r in linhas) == 29
assert sum(r["elegivel_booster_origem"] == "SIM" for r in linhas) == 136
assert len({r["tipo"] for r in linhas}) == 14
faltantes_por_id = {r["id_catalogo"]: r for r in concil["ids_ativos_ausentes_web"]}
for row in linhas:
    cid = row["id"]
    assert cid and row["nome"] and row["tipo"] and row["nd"] and row["raridade"]
    assert row["id_na_megalista_web"] == (cid in by_id)
    # Para os 606 IDs comuns, a fonte ativa e o arquivo web devem concordar
    # sobre identidade, tipo, ND e raridade; jamais aplicar correções automáticas.
    if cid in by_id:
        historical = by_id[cid]
        for active_field, web_field in (
            ("nome", "NOME"), ("tipo", "TIPO"),
            ("nd", "ND"), ("raridade", "RARIDADE"),
        ):
            assert str(row[active_field]).strip().casefold() == str(historical[web_field]).strip().casefold(), (cid, active_field)
    assert not any(k in row for k in ("ca", "pv", "ataques", "habilidades", "acoes"))
    assert isinstance(row["linha_planilha"], int) and 2 <= row["linha_planilha"] <= 636
    if cid in faltantes_por_id:
        previous = faltantes_por_id[cid]
        for key, older in (
            ("nome", "nome"), ("tipo", "tipo"), ("nd", "nd"), ("raridade", "raridade"),
            ("situacao_catalogo", "situacao_catalogo"),
            ("status_ficha_origem", "status_ficha_origem"),
            ("elegivel_booster_origem", "elegivel_booster_origem"),
        ):
            assert row[key] == previous[older], (cid, key)
html = (SITE / "consulta-ativos-635.html").read_text("utf-8")
js = (SITE / "consulta-ativos-635.js").read_text("utf-8")
assert "catalogo-ativo-635-consulta-20261021.json" in js
assert 'id="show-missing"' in html and "id_na_megalista_web" in js
assert "textContent" in js and "innerHTML" not in js
assert "nenhuma informação foi homologada" in js.lower()
print("Consulta preliminar 635 OK: IDs, metadados canônicos, 29 faltantes, 136 booster SIM, sem mecânicas.")


# Auditoria não destrutiva das fichas v2.1 localizadas no Drive (sem homologação).
v21_audit_path = ROOT / "auditoria/fichas-v21-29-ids-ausentes-20261021.json"
v21 = json.loads(v21_audit_path.read_text("utf-8"))
assert v21["schema"] == "SRD_AUDITORIA_FICHAS_V21_IDS_AUSENTES_V1"
assert v21["indicadores_extraidos_do_resumo"]["criaturas_distintas_com_json"] == 139
assert v21["indicadores_extraidos_do_resumo"]["json_vinculados_ao_catalogo_ativo"] == 68
assert v21["indicadores_extraidos_do_resumo"]["documentos_integrais_no_acervo"] == 146
assert v21["ids_ausentes_web_total"] == len(v21["registros"]) == 29
assert v21["ids_homebrew_preservados_sem_json"] == 28
assert v21["id_terceiros_sem_json"] == "KP-S007"
assert {r["id_catalogo"] for r in v21["registros"]} == {
    r["id_catalogo"] for r in concil["ids_ativos_ausentes_web"]
}
for item in v21["registros"]:
    assert item["declaracao_json_v2_1"] == "SEM JSON NESTE ACERVO"
    assert item["documento_integral_associado_na_v2_1"] is False
    assert item["conclusao"] == "FICHA_INTEGRAL_NAO_RECUPERADA"
    assert item["nao_inferir_mecanicas"] is True
    assert item["id_catalogo"] not in by_id
    if item["id_catalogo"] != "KP-S007":
        assert item["situacao_indice_v2_0"] == "PRESERVADA"
        assert item["declaracao_ficha_v2_0"] == "FICHA COMPLETA ORIGINAL"
print("Auditoria v2.1 OK: 29 IDs ausentes sem JSON (28 homebrew preservados, 1 referência externa).")
