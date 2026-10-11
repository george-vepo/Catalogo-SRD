from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree


REPO = Path(r"D:\Repos\SRD-Card-Game-607-Supervisor")
PACKAGE = REPO / r"SRD_CYCLES\26-30\SRD_PACOTE_CONTINUIDADE_LOTE30_2026-10-11.zip"
BASE_SHA = "04614280e4a25b744b47d111517a105170c1f4ea4e3da4f4865d9ac69e068dbc"
PACKAGE_SHA = "2f04c5fc9a31215b9a92b5e009bc1d231b042a22c8530551e62fa804543cb218"
BASE_ENTRY = "00_PACOTE_BASE/SRD_PACOTE_CONTINUIDADE_LOTE25_2026-10-11.zip"
JSON_ENTRY = "02_SAIDA_v2.1.0/SRD_FICHAS_607.json"
DOCX_ENTRY = "02_SAIDA_v2.1.0/SRD_FICHAS_607_COMPLETAS.docx"
URL_DOCX_ENTRY = "02_SAIDA_v2.1.0/SRD_URLS_IMAGENS_607.docx"
IMAGE_ZIP_ENTRY = "02_SAIDA_v2.1.0/SRD_FICHAS_IMAGENS_607_v2.1.0_2026-10-11.zip"
CURRENT_IDS = ["KP-S008", "KP-S009", "KP-S010", "KP-S011", "KP-S012"]
COMPLETE_IDS = ["KP-S008", "KP-S009", "KP-S010", "KP-S012"]
PARTIAL_IDS = ["KP-S011"]
URLS = {
    "KP-S008": "https://www.5esrd.com/database/creature/arcane-leviathan/",
    "KP-S009": "https://www.5esrd.com/database/creature/primordial-surge/",
    "KP-S010": "https://www.5esrd.com/database/creature/primordial-matriarch/",
    "KP-S011": "https://www.5esrd.com/database/creature/abominable-beauty/",
    "KP-S012": "https://kpogl.wikidot.com/monster:hvalfiskr",
}
MARKER = re.compile(r"turn\d+(?:view|search)\d+", re.IGNORECASE)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def docx_text(data: bytes) -> str:
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        xml = archive.read("word/document.xml")
    root = ElementTree.fromstring(xml)
    return "\n".join(node.text or "" for node in root.iter() if node.tag.endswith("}t"))


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    errors: list[str] = []
    try:
        actual_package_sha = sha256_path(PACKAGE)
        if actual_package_sha != PACKAGE_SHA:
            fail(f"package SHA {actual_package_sha} != {PACKAGE_SHA}")

        with zipfile.ZipFile(PACKAGE) as archive:
            names = archive.namelist()
            if len(names) != 20 or len(set(names)) != 20:
                fail(f"outer ZIP entries={len(names)} unique={len(set(names))}")
            if any(info.CRC != (zipfile.crc32(archive.read(info.filename)) & 0xFFFFFFFF) for info in archive.infolist()):
                fail("outer ZIP CRC mismatch")

            manifest = json.loads(archive.read("01_CONTINUIDADE/MANIFESTO_SHA256.json"))
            entries = manifest["arquivos"]
            if len(entries) != 19:
                fail(f"manifest entries={len(entries)}")
            entry_names = {item["arquivo"] for item in entries}
            if entry_names != set(names) - {"01_CONTINUIDADE/MANIFESTO_SHA256.json"}:
                fail("manifest file set mismatch")
            for item in entries:
                payload = archive.read(item["arquivo"])
                if len(payload) != item["tamanho_bytes"]:
                    fail(f"size mismatch: {item['arquivo']}")
                if sha256_bytes(payload) != item["sha256"]:
                    fail(f"manifest SHA mismatch: {item['arquivo']}")

            base_payload = archive.read(BASE_ENTRY)
            if sha256_bytes(base_payload) != BASE_SHA:
                fail("embedded base SHA mismatch")
            if sha256_path(REPO / r"SRD_CYCLES\21-25\SRD_PACOTE_CONTINUIDADE_LOTE25_2026-10-11.zip") != BASE_SHA:
                fail("source base SHA mismatch")

            data = json.loads(archive.read(JSON_ENTRY))
            if data["total"] != 607 or len(data["fichas"]) != 607:
                fail("607 ID count mismatch")
            stats = data["estatisticas"]
            expected_stats = {
                "fichas_integral_local": 108,
                "fichas_mecanicamente_integradas_com_fatos_e_resumos_proprios": 104,
                "fichas_incompletas": 395,
                "paginas_individuais_conhecidas_total": 119,
                "paginas_individuais_conhecidas_ainda_nao_integradas": 15,
                "fichas_pendentes_sem_pagina_individual_confirmada": 380,
                "imagens_diretas_verificadas": 23,
                "urls_diretas_antigas_retestadas": 7,
                "ids_unicos": 607,
            }
            for key, expected in expected_stats.items():
                if stats.get(key) != expected:
                    fail(f"stat {key}={stats.get(key)!r} != {expected!r}")

            audit = data["auditoria_lote"]
            if audit["lote"] != "26-30" or audit["registros_analisados_ids_neste_lote"] != CURRENT_IDS:
                fail("current batch audit IDs mismatch")
            if audit["fichas_completas_integradas_ids_neste_lote"] != COMPLETE_IDS:
                fail("current complete IDs mismatch")
            if audit["fichas_parciais_ids_neste_lote"] != PARTIAL_IDS:
                fail("current partial IDs mismatch")

            by_id = {record["id"]: record for record in data["fichas"]}
            for current_id in CURRENT_IDS:
                record = by_id[current_id]
                mechanics = record["mecanica_externa_integrada"]
                if record["source_verification_date"] != "2026-10-11":
                    fail(f"current date mismatch: {current_id}")
                if URLS[current_id] not in record["fonte_citacao_web"]:
                    fail(f"current citation URL missing: {current_id}")
                if mechanics.get("fonte_url") != URLS[current_id]:
                    fail(f"current source URL mismatch: {current_id}")
            for record in data["fichas"]:
                if record.get("id") not in CURRENT_IDS and record.get("source_verification_date") == "2026-10-11":
                    fail(f"historical date overwritten: {record.get('id')}")
            historical_external_dates = sum(
                1
                for record in data["fichas"]
                if record.get("id") not in CURRENT_IDS
                and record.get("mecanica_externa_integrada")
                and record.get("source_verification_date") == "2026-10-10"
                and record["mecanica_externa_integrada"].get("data_verificacao") == "2026-10-10"
            )
            if historical_external_dates != 108:
                fail(f"historical external date count={historical_external_dates}")

            s011 = by_id["KP-S011"]["mecanica_externa_integrada"]
            if not any(item.get("nome") == "Undead Nature" for item in s011["tracos"]):
                fail("KP-S011 Undead Nature is not in tracos")
            if any(item.get("nome") == "Undead Nature" for item in s011.get("acoes", [])):
                fail("KP-S011 Undead Nature incorrectly appears in acoes")

            s009 = by_id["KP-S009"]["mecanica_externa_integrada"]
            primordial_form = next(item for item in s009["tracos"] if item["nome"] == "Primordial Form")
            if "come\u00e7ar seu pr\u00f3prio turno fora do espa\u00e7o do surge" not in primordial_form["resumo_mecanico"]:
                fail("KP-S009 Primordial Form trigger/duration mismatch")

            s010 = by_id["KP-S010"]["mecanica_externa_integrada"]
            storm_blast = next(item for item in s010["acoes"] if item["nome"] == "Storm Blast")
            storm_text = storm_blast["resumo_mecanico"]
            for fragment in ["Cold", "Lightning", "Thunder", "a\u00e7\u00e3o apagar", "repeti\u00e7\u00e3o"]:
                if fragment not in storm_text:
                    fail(f"KP-S010 Storm Blast missing {fragment!r}")
            create_elementals = next(item for item in s010["acoes"] if item["nome"] == "Create Elementals")
            if "a\u00e7\u00e3o b\u00f4nus" not in create_elementals["resumo_mecanico"]:
                fail("KP-S010 Create Elementals missing bonus-action dismissal")
            consume = next(item for item in s010["acoes_de_covil"] if item["nome"] == "Consume")
            if "ponto vis\u00edvel" not in consume["resumo_mecanico"]:
                fail("KP-S010 Consume missing visible-point restriction")
            economy = s010.get("economia_de_covil", "")
            for fragment in ["iniciativa 20", "perdendo empates", "mesmo efeito"]:
                if fragment not in economy:
                    fail(f"KP-S010 lair economy missing {fragment!r}")
            weather = next(item for item in s010["caracteristicas_de_covil"] if item["nome"] == "Erratic Weather")
            for fragment in ["raramente duram mais de 1 hora", "1d10 dias"]:
                if fragment not in weather["resumo_mecanico"]:
                    fail(f"KP-S010 Erratic Weather missing {fragment!r}")

            senses = by_id["KP-S012"]["mecanica_externa_integrada"]["sentidos"]
            if senses != ["blindsight 120 ft. (somente forma de baleia)", "darkvision 120 ft."]:
                fail(f"KP-S012 senses mismatch: {senses!r}")
            chained_anchor = next(item for item in by_id["KP-S012"]["mecanica_externa_integrada"]["acoes"] if item["nome"].startswith("Chained Anchor"))
            if chained_anchor.get("teste_atributo") != "Strength DC 19" or "salvaguarda" in chained_anchor:
                fail("KP-S012 Chained Anchor does not distinguish Strength check from saving throw")
            for fragment in ["espa\u00e7o desocupado", "n\u00e3o pode usar Reel Anchor"]:
                if fragment not in chained_anchor["resumo_mecanico"]:
                    fail(f"KP-S012 Chained Anchor missing {fragment!r}")

            textual_current: list[tuple[str, bytes]] = []
            for name in names:
                if name == BASE_ENTRY or name == IMAGE_ZIP_ENTRY:
                    continue
                suffix = Path(name).suffix.lower()
                if suffix in {".py", ".txt", ".md", ".json", ".csv"}:
                    textual_current.append((name, archive.read(name)))
                elif suffix == ".docx":
                    textual_current.append((name + "::xml", docx_text(archive.read(name)).encode("utf-8")))
            current_marker_count = sum(len(MARKER.findall(payload.decode("utf-8", errors="ignore"))) for _, payload in textual_current)
            if current_marker_count != 0:
                fail(f"current artifact internal marker count={current_marker_count}")

            readme = archive.read("03_CONSTRUTOR/LEIA-ME.txt").decode("utf-8")
            if "00_PACOTE_BASE" not in readme or "não é reescrito" not in readme:
                fail("readme missing historical base scan scope")
            if "31–35" not in readme and "31-35" not in readme and "31 a 35" not in readme:
                fail("readme missing next cycle")

            for name in [
                "02_SAIDA_v2.1.0/SRD_AUDITORIA_PENDENCIAS_607.csv",
                "02_SAIDA_v2.1.0/SRD_Card_Game_Fichas_607_Fontes_Web_Lote1.csv",
                "02_SAIDA_v2.1.0/SRD_URLS_IMAGENS_607.csv",
                "03_CONSTRUTOR/SRD_Card_Game_Fichas_607_Fontes_Web_Lote2.csv",
                "03_CONSTRUTOR/SRD_Card_Game_Fichas_607_Indice_e_Textos_Extraidos.json",
                "03_CONSTRUTOR/SRD_Card_Game_Referencia_URL_Imagens_607_v3.csv",
                "03_CONSTRUTOR/SRD_Worker_Base_Pendencias_607.csv",
            ]:
                if name.endswith(".json"):
                    value = json.loads(archive.read(name))
                    if isinstance(value, dict) and value.get("total") not in (None, 607):
                        fail(f"CSV/JSON count mismatch: {name}")
                else:
                    rows = list(csv.reader(io.StringIO(archive.read(name).decode("utf-8-sig"))))
                    if len(rows) < 608:
                        fail(f"CSV row count {len(rows)} < 608: {name}")

            audit_rows = list(csv.DictReader(io.StringIO(archive.read("02_SAIDA_v2.1.0/SRD_AUDITORIA_PENDENCIAS_607.csv").decode("utf-8-sig")), delimiter=";"))
            audit_by_id = {row["ID"]: row for row in audit_rows}
            external_ids = {record["id"] for record in data["fichas"] if record.get("mecanica_externa_integrada")}
            historical_ids = external_ids - set(CURRENT_IDS)
            historical_audit_rows = [audit_by_id[record_id] for record_id in historical_ids]
            if len(historical_audit_rows) != 108 or not all("2026-10-10" in row.get("Observacoes_auditoria", "") for row in historical_audit_rows):
                fail("historical audit CSV dates are not preserved at 2026-10-10")
            if not all("2026-10-11" in audit_by_id[current_id].get("Observacoes_auditoria", "") for current_id in CURRENT_IDS):
                fail("current audit CSV dates are not marked 2026-10-11")

            main_docx = docx_text(archive.read(DOCX_ENTRY))
            if "Economia de covil." not in main_docx or "iniciativa 20" not in main_docx or "perdendo empates" not in main_docx:
                fail("main DOCX missing lair economy")
            for fragment in ["espa\u00e7o desocupado", "n\u00e3o pode usar Reel Anchor", "teste de For\u00e7a CD 19"]:
                if fragment not in main_docx:
                    fail(f"main DOCX missing KP-S012 Chained Anchor detail {fragment!r}")
            if not docx_text(archive.read(URL_DOCX_ENTRY)):
                fail("URL DOCX has no text")

            with zipfile.ZipFile(io.BytesIO(archive.read(IMAGE_ZIP_ENTRY))) as image_zip:
                if len(image_zip.namelist()) != 7:
                    fail(f"inner image ZIP entries={len(image_zip.namelist())}")
                if any(info.CRC != (zipfile.crc32(image_zip.read(info.filename)) & 0xFFFFFFFF) for info in image_zip.infolist()):
                    fail("inner image ZIP CRC mismatch")
                inner_main_docx = docx_text(image_zip.read("SRD_FICHAS_607_COMPLETAS.docx"))
                if "Economia de covil." not in inner_main_docx:
                    fail("inner DOCX missing lair economy")
                for fragment in ["espa\u00e7o desocupado", "n\u00e3o pode usar Reel Anchor", "teste de For\u00e7a CD 19"]:
                    if fragment not in inner_main_docx:
                        fail(f"inner DOCX missing KP-S012 Chained Anchor detail {fragment!r}")

            report = archive.read("02_SAIDA_v2.1.0/SRD_RELATORIO_DE_COLETA.md").decode("utf-8")
            state = archive.read("01_CONTINUIDADE/ESTADO_ATUAL.md").decode("utf-8")
            prompt = archive.read("01_CONTINUIDADE/PROMPT_PROXIMO_PROCESSO.txt").decode("utf-8")
            for name, text in [("report", report), ("state", state), ("prompt", prompt)]:
                if "26-30" not in text and "26–30" not in text:
                    fail(f"{name} missing cycle 26-30")
            for name, text in [("state", state), ("prompt", prompt)]:
                if "31-35" not in text and "31–35" not in text and "31 a 35" not in text:
                    fail(f"{name} missing next cycle")
            if re.search(r"(execut|rod|inici).*31[-–]35", report, re.IGNORECASE):
                fail("report suggests 31-35 execution")

            summary = {
                "package_sha256": actual_package_sha,
                "outer_entries": len(names),
                "manifest_entries": len(entries),
                "base_sha256": BASE_SHA,
                "ids": 607,
                "complete_fichas": 212,
                "pending_fichas": 395,
                "verified_images": 23,
                "current_complete": COMPLETE_IDS,
                "current_partial": PARTIAL_IDS,
                "historical_external_dates_preserved": historical_external_dates,
                "current_source_urls": len(URLS),
                "current_artifacts_internal_markers": current_marker_count,
                "visual_gate": "NOT_TESTED_NO_SOFFICE",
                "base_historical_markers": "PRESERVED_IMMUTABLE_NOT_SCANNED_AS_CURRENT",
            }
            print("FINAL_PACKAGE_AUDIT_PASS")
            print(json.dumps(summary, ensure_ascii=False, separators=(",", ":")))
            return 0
    except Exception as exc:
        errors.append(f"{type(exc).__name__}: {exc}")
    for error in errors:
        print(f"FINAL_PACKAGE_AUDIT_FAIL: {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
