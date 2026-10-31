#!/usr/bin/env python3
"""SRD Card Game: pré-verificação e ingestão auditável de recursos por modelo no DRAW.

Este módulo é um hook para o runtime chamá-lo após cada compra; não compra cartas,
não revela a mão e não faz chamadas de IA/web sem um executor conectado.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

MODEL_ID = re.compile(r"(?:ML-\d{4}|AT-\d{3}|TF-\d{3}|KP-[AS]\d{3}|EXT-\d{4})\Z")
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}
PRIVATE_FIELDS = {"copy_id", "card_instance_id", "hand", "deck", "deck_order", "draw_order", "pile", "player", "player_id", "shuffle_seed", "game_state", "private_state"}
ROOT_RESEARCH = Path("operational/research/creature-candidates")
ROOT_IMAGES = Path("docs/catalogo/assets/draw-candidates")


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as fh:
        return json.load(fh)


def canonical_model(root: Path, model_id: str) -> dict[str, str]:
    if not MODEL_ID.fullmatch(model_id):
        raise ValueError("ID de modelo inválido; não use ID de cópia do jogador")
    data = read_json(root / "docs/catalogo/data/megalista-1320.json")
    records = data["records"]
    if model_id.startswith("ML-"):
        number = int(model_id[3:])
        if number < 1 or number > len(records):
            raise ValueError("Posição ML fora da megalista")
        row = records[number - 1]
        if row.get("ID NO JOGO"):
            raise ValueError("Esse registro possui ID do catálogo; ML não é canônico aqui")
    else:
        matches = [r for r in records if r.get("ID NO JOGO") == model_id]
        if len(matches) != 1:
            raise ValueError("ID do catálogo ausente ou ambíguo na megalista")
        row = matches[0]
    return {"model_id": model_id, "name": row["NOME"], "type": row["TIPO"],
            "nd": str(row["ND"]), "rarity": row["RARIDADE"], "publication": row.get("FONTE", "")}


def inspect(root: Path, model_id: str, expected_name: str | None = None) -> dict[str, Any]:
    model = canonical_model(root, model_id)
    if expected_name and expected_name.casefold().strip() != model["name"].casefold().strip():
        raise ValueError("Nome da criatura diverge do ID do catálogo")
    candidates = [*sorted((root / "operational/assets/creature-images").glob(model_id + ".*")),
                  *sorted((root / ROOT_IMAGES).glob(model_id + "-*"))]
    images = [p.relative_to(root).as_posix() for p in candidates if p.is_file() and p.stat().st_size > 0 and p.suffix.lower() in IMAGE_EXTS]
    research_path = root / ROOT_RESEARCH / (model_id + ".json")
    research = read_json(research_path) if research_path.is_file() else None
    if research and research.get("model_id") != model_id:
        raise ValueError("Ficha de pesquisa com identidade divergente")
    original = None
    statblocks = root / "docs/catalogo/data/fichas-607.json"
    if statblocks.is_file() and not model_id.startswith("ML-"):
        original = next((f for f in read_json(statblocks).get("fichas", []) if f.get("id") == model_id and f.get("nome") == model["name"]), None)
    full = bool(original and original.get("status_ficha") == "FICHA INTEGRAL LOCAL" and original.get("ficha_integral_texto_local"))
    if not full and research:
        full = bool(research.get("statblock", {}).get("status") == "VERIFICADA_INTEGRAL" and research.get("statblock", {}).get("source_references"))
    support = (research or {}).get("support")
    support_approved = bool(support and support.get("approved") is True and support.get("usable_in_official_combat") is True)
    support_present = bool(support and support.get("source_ability") and support.get("status"))
    visual = (research or {}).get("visual") or {}
    preview_inadequate = visual.get("status") in {"PREVIA_INADEQUADA_PENDENTE_ARTE_FINAL", "IMAGEM_REJEITADA"}
    original_images = [p for p in images if p.startswith("operational/assets/creature-images/")]
    usable_images = original_images if preview_inadequate else images
    tasks = []
    if not usable_images:
        tasks.append({"kind": "GENERATE_IMAGE", "executor": "ChatGPT ImageGen", "required": True})
    if not full:
        tasks.append({"kind": "RESEARCH_5E_STATBLOCK", "executor": "Pesquisa 5e e curadoria", "required": True})
    if not support_present:
        tasks.append({"kind": "DERIVE_SUPPORT_FROM_REAL_ABILITY", "executor": "Curadoria 5e", "required": True})
    elif not support_approved:
        tasks.append({"kind": "REVIEW_SUPPORT", "executor": "Administrador", "required": True})
    return {"schema": "SRD_DRAW_MODEL_ENRICHMENT_V1", "model": model,
            "image": {"available": bool(usable_images), "paths": images, "approved": False,
                      "requires_final_art": preview_inadequate, "status": visual.get("status")},
            "statblock": {"full_verified": full, "catalogue_status": original.get("status_ficha") if original else None,
                          "research_status": research.get("status") if research else None},
            "support": {"present": support_present, "approved": support_approved,
                        "source_ability": support.get("source_ability") if support else None},
            "tasks": tasks, "draw_state_changed": False, "game_private_data_included": False}


def reject_private(data: Any) -> None:
    if isinstance(data, dict):
        for key, value in data.items():
            if str(key).casefold() in PRIVATE_FIELDS:
                raise ValueError("Campo privado proibido em ficha de pesquisa: " + str(key))
            reject_private(value)
    elif isinstance(data, list):
        for x in data:
            reject_private(x)


def stage(root: Path, model_id: str, research_file: Path | None, image_file: Path | None) -> list[str]:
    model = canonical_model(root, model_id)
    staged = []
    if research_file:
        research = read_json(research_file)
        reject_private(research)
        if research.get("model_id") != model_id or research.get("canonical_name") != model["name"]:
            raise ValueError("A ficha pesquisada não corresponde ao modelo")
        if research.get("status") in {"HOMOLOGADA", "APROVADA"}:
            raise ValueError("O enriquecimento não pode homologar automaticamente")
        support = research.get("support")
        if not isinstance(support, dict) or not support.get("source_ability") or not support.get("category"):
            raise ValueError("Ficha sem suporte incorporado ou origem mecânica")
        if support.get("approved") is not False or support.get("status") != "CANDIDATA_NAO_HOMOLOGADA":
            raise ValueError("Suporte só pode ser enviado como candidato não homologado")
        if support.get("category") not in {"Cura", "Buff", "Debuff", "Dano"}:
            raise ValueError("Categoria de suporte inválida")
        if not support.get("effect_text_candidate"):
            raise ValueError("Texto do efeito de suporte ausente")
        valid_sources = any(str(x).startswith(("https://", "http://")) for x in research.get("sources", []))
        ref = research.get("authoritative_statblock")
        if not valid_sources and not (isinstance(ref, dict) and ref.get("record_id") and ref.get("source_repo_path")):
            raise ValueError("É obrigatória uma fonte de ficha verificável")
        target = root / ROOT_RESEARCH / (model_id + ".json")
        if target.exists():
            existing = read_json(target)
            if existing.get("support", {}).get("approved"):
                raise ValueError("Não sobrescrever suporte homologado")
            if existing.get("status") in {"HOMOLOGADA", "APROVADA"}:
                raise ValueError("Não sobrescrever ficha homologada")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(research, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        staged.append(target.relative_to(root).as_posix())
    if image_file:
        if image_file.suffix.lower() not in IMAGE_EXTS or not image_file.is_file() or image_file.stat().st_size < 12:
            raise ValueError("Imagem deve ser arquivo de imagem não vazio")
        with image_file.open("rb") as fh:
            header = fh.read(16)
        is_png = header.startswith(b"\x89PNG\r\n\x1a\n") and image_file.suffix.lower() == ".png"
        is_jpg = header.startswith(b"\xff\xd8\xff") and image_file.suffix.lower() in {".jpg", ".jpeg"}
        is_webp = header[:4] == b"RIFF" and header[8:12] == b"WEBP" and image_file.suffix.lower() == ".webp"
        if not (is_png or is_jpg or is_webp):
            raise ValueError("Assinatura de arquivo de imagem incompatível com extensão")
        if image_file.stat().st_size > 15_000_000:
            raise ValueError("Imagem grande demais para ingestão automática")
        target = root / ROOT_IMAGES / (model_id + "-candidata" + image_file.suffix.lower())
        if target.exists():
            raise ValueError("Arte candidata já existe; revisar em vez de substituir")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(image_file, target)
        staged.append(target.relative_to(root).as_posix())
    return staged


def publish(root: Path, paths: list[str], branch: str) -> str:
    """Publica somente os caminhos de modelo via git; execução explícita sob credenciais externas."""
    if not paths:
        return "SEM_NOVOS_ARQUIVOS"
    if not re.fullmatch(r"research/[a-zA-Z0-9._/-]+", branch):
        raise ValueError("Somente branches de pesquisa autorizadas")
    def git(*args: str) -> str:
        return subprocess.check_output(["git", "-C", str(root), *args], text=True, stderr=subprocess.STDOUT).strip()
    if git("branch", "--show-current") != branch:
        raise ValueError("Branch atual diferente da branch de pesquisa")
    git("add", "--", *paths)
    staged = set(git("diff", "--cached", "--name-only").splitlines())
    if not staged:
        return "SEM_ALTERACOES"
    if not staged.issubset(set(paths)):
        raise ValueError("Há outros arquivos preparados para commit; risco de vazamento")
    git("commit", "-m", "research(srd): recursos de modelos encontrados no DRAW")
    git("push", "origin", branch)
    return git("rev-parse", "HEAD")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Hook de enriquecimento por modelo; não manipula mão, monte ou combate")
    parser.add_argument("command", choices=("inspect", "stage"))
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--expected-name")
    parser.add_argument("--research-file", type=Path)
    parser.add_argument("--image-file", type=Path)
    parser.add_argument("--publish-branch")
    args = parser.parse_args(argv)
    try:
        root = args.repo.resolve()
        if args.command == "inspect":
            result = inspect(root, args.model_id, args.expected_name)
        else:
            if not args.research_file and not args.image_file:
                raise ValueError("Nada novo para ingerir")
            paths = stage(root, args.model_id, args.research_file, args.image_file)
            result = {"schema": "SRD_DRAW_STAGE_V1", "model_id": args.model_id, "staged_paths": paths,
                      "publication": publish(root, paths, args.publish_branch) if args.publish_branch else "PENDENTE_PUBLICACAO",
                      "game_private_data_included": False}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"error": str(exc), "state_changed": False}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())