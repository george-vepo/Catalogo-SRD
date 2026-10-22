"""Importação local do Drive. Analisa por padrão; --aplicar grava no catálogo."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
from importar_artes_drive import slug, convert_webp

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs/catalogo'
MANIFEST = SITE / 'data/drive-import-20261021.json'
ID = re.compile(r'^(AT-\d{3}|TF-\d{3}|EXT-\d{4}|KP-[A-Z]\d{3})-(.+)$', re.I)


def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def plan_images(images, manifest, by_id, by_name):
    known = set()
    for art in manifest['artes'] + manifest.get('artes_locais', []):
        known.update(h for h in (art.get('sha256_origem'), art.get('sha256_webp')) if h)
        asset = SITE / art['arquivo']
        if asset.is_file():
            known.add(hashlib.sha256(asset.read_bytes()).hexdigest())
    known = {h.lower() for h in known}
    groups, rows = {}, []
    for path in sorted(images.rglob('*')):
        if not path.is_file() or path.suffix.lower() not in {'.png', '.webp', '.jpg', '.jpeg'}:
            continue
        row = {'arquivo': str(path.relative_to(images))}
        rows.append(row)
        if 'rejeitada' in path.name.casefold():
            row['status'] = 'EXCLUIDA_REJEITADA'; continue
        try:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError as exc:
            row.update(status='ERRO_LEITURA', motivo=str(exc)); continue
        row['sha256_origem'] = digest
        if digest in known:
            row['status'] = 'JA_INTEGRADO'; continue
        title = path.stem.split('__', 1)[0]
        title = re.sub(r'(\s*\(\d+\))+$', '', title).strip()
        match = ID.fullmatch(title)
        cid, name = (match.group(1).upper(), match.group(2)) if match else ('', title)
        record = by_id.get(cid)
        if record and slug(record['NOME']) != slug(name):
            record = None
        elif not record:
            matches = by_name.get(slug(name), [])
            if len(matches) == 1 and (not cid or not matches[0]['ID NO JOGO']):
                record = matches[0]
        identity = (record['ID NO JOGO'], record['NOME']) if record else None
        row.update(status='IMPORTAR', vinculo='CONFIRMADO' if identity else 'SEM_VINCULO_CONFIRMADO')
        if digest not in groups:
            groups[digest] = {'path': path, 'rows': [], 'identities': set()}
        groups[digest]['rows'].append(row)
        groups[digest]['identities'].add(identity)
    return groups, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--drive-root', type=Path, default=Path('G:/Meu Drive/SRD Card Game'))
    parser.add_argument('--aplicar', action='store_true')
    parser.add_argument('--relatorio', type=Path, default=ROOT / 'logs/importacao-local.json')
    args = parser.parse_args()
    sheets = args.drive_root / 'Fichas/Completas'
    images = args.drive_root / 'Imagens/Novas'
    if not sheets.is_dir() or not images.is_dir():
        parser.error('DriveRoot precisa conter Fichas/Completas e Imagens/Novas.')
    manifest = load(MANIFEST)
    catalog = load(SITE / 'data/megalista-1320.json')['records']
    by_id = {r['ID NO JOGO']: r for r in catalog if r['ID NO JOGO']}
    by_name = defaultdict(list)
    for record in catalog:
        by_name[slug(record['NOME'])].append(record)
    existing = {(r['id_catalogo'] or r['nome']): r for r in manifest['fichas']}
    grouped, rows = defaultdict(list), []
    for path in sorted(sheets.rglob('*')):
        if not path.is_file() or path.suffix.lower() not in {'.json', '.md'}:
            continue
        row = {'arquivo': path.name, 'status': 'PENDENTE'}
        rows.append(row)
        stem = re.sub(r' \(\d+\)$', '', path.stem)
        stem = re.sub(r'-ficha$', '', stem, flags=re.I)
        match = ID.fullmatch(stem)
        if not match:
            row['status'] = 'NOME_SEM_IDENTIDADE'; continue
        cid, file_name = match.group(1).upper(), match.group(2)
        matches = by_name.get(slug(file_name), [])
        record = by_id.get(cid)
        if record:
            pass  # O nome interno pode confirmar uma ordem diferente no filename.
        elif len(matches) == 1 and not matches[0]['ID NO JOGO']:
            record = matches[0]
        else:
            row['status'] = 'IDENTIDADE_A_CONCILIAR'; continue
        raw = path.read_bytes()
        try:
            data = json.loads(raw.decode('utf-8-sig')) if path.suffix.lower() == '.json' else None
            if data is not None:
                if not isinstance(data, dict):
                    raise ValueError('A raiz JSON precisa ser um objeto')
                ident = data.get('identificacao') or {}
                declared_id = data.get('id_catalogo') or data.get('ID_CATALOGO') or ident.get('id_catalogo') or ident.get('ID_CATALOGO')
                name_keys = ('nome', 'nome_original', 'nome_canonico', 'nome_catalogo', 'nome_na_fonte', 'criatura', 'NOME')
                names = [data.get(k) for k in name_keys]
                names += [ident.get(k) for k in name_keys]
                names = [n for n in names if isinstance(n, str) and n]
                if declared_id and declared_id != record['ID NO JOGO']:
                    raise ValueError('ID declarado diverge do catálogo')
                if not names or slug(record['NOME']) not in {slug(n) for n in names}:
                    # Alguns esquemas declaram somente a chave ID-nome.
                    key = data.get('chave') or ident.get('chave') or data.get('CHAVE') or ident.get('CHAVE')
                    if names or key != stem or slug(record['NOME']) != slug(file_name):
                        raise ValueError('Nome interno não confirma identidade do arquivo')
            elif slug(record['NOME']) != slug(file_name):
                raise ValueError('Nome do documento diverge do catálogo')
        except (ValueError, UnicodeError) as exc:
            row.update(status='CONTEUDO_A_CONCILIAR', motivo=str(exc)); continue
        key = record['ID NO JOGO'] or record['NOME']
        row.update(id_catalogo=record['ID NO JOGO'], nome=record['NOME'], sha256=hashlib.sha256(raw).hexdigest())
        grouped[key].append((path, row, data, record))

    planned = []
    for key, group in grouped.items():
        jsons = [x for x in group if x[2] is not None]
        if not jsons or len({x[1]['sha256'] for x in jsons}) != 1:
            for _, row, _, _ in group: row['status'] = 'VARIANTES_A_CONCILIAR'
            continue
        path, row, data, record = jsons[0]
        if key in existing:
            old = existing[key]
            same = old.get('sha256_origem') == row['sha256']
            if not same:
                old_data = load(SITE / old['arquivo'])
                same = old_data.get('conteudo_original', old_data) == data
            if same:
                old_data = load(SITE / old['arquivo'])
                if old_data.get('schema') == 'CATALOGO_FICHA_LOCAL_V1':
                    old_docs = {x['nome']: x['sha256'] for x in old_data['documentos_complementares']}
                    new_docs = {p.name: r['sha256'] for p, r, obj, _ in group if obj is None}
                    same = old_docs == new_docs
            for _, r, _, _ in group: r['status'] = 'JA_INTEGRADO' if same else 'VERSAO_EXISTENTE_DIFERENTE'
            continue
        rel = 'data/drive-fichas-local/' + slug(key + '-' + record['NOME']) + '.json'
        dest = SITE / rel
        if dest.exists():
            for _, r, _, _ in group: r['status'] = 'DESTINO_EXISTENTE_NAO_SOBRESCRITO'
            continue
        envelope = {'schema': 'CATALOGO_FICHA_LOCAL_V1', 'id_catalogo': record['ID NO JOGO'], 'nome_catalogo': record['NOME'], 'origem_arquivo': path.name, 'sha256_origem': row['sha256'], 'conteudo_original': data, 'documentos_complementares': []}
        for p, r, obj, _ in group:
            r['status'] = 'IMPORTADO' if args.aplicar else 'IMPORTAR'
            if obj is None:
                envelope['documentos_complementares'].append({'nome': p.name, 'sha256': r['sha256'], 'texto': p.read_text(encoding='utf-8-sig')})
        ident = data.get('identificacao') or {}
        entry = {'id_catalogo': record['ID NO JOGO'], 'nome': record['NOME'], 'arquivo': rel, 'edicao': str(data.get('edicao') or ident.get('edicao') or 'Não informada na origem'), 'status': 'FICHA_LOCAL_SEM_HOMOLOGACAO_ADMINISTRATIVA', 'substitui_ficha_base': False, 'sha256_origem': row['sha256']}
        planned.append((dest, envelope, entry))

    image_plan, image_rows = plan_images(images, manifest, by_id, by_name)
    art_count = len(image_plan)
    if args.aplicar:
        if image_plan:
            from PIL import Image  # confirmar dependência antes de qualquer gravação
        for dest, envelope, entry in planned:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(json.dumps(envelope, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            manifest['fichas'].append(entry)
        manifest['contagens_lote']['fichas'] = len(manifest['fichas'])
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        for digest, group in image_plan.items():
            try:
                binary = convert_webp(group['path'], strict=False)
                rel = 'assets/drive-locais/' + digest + '.webp'
                dest = SITE / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                if dest.exists() and dest.read_bytes() != binary:
                    raise FileExistsError('Destino existente com conteúdo diferente: ' + str(dest))
                dest.write_bytes(binary)
                if hashlib.sha256(dest.read_bytes()).hexdigest() != hashlib.sha256(binary).hexdigest():
                    raise RuntimeError('Hash da imagem gravada diverge')
                identity = next(iter(group['identities'])) if len(group['identities']) == 1 else None
                entry = {'id_catalogo': identity[0] if identity else '', 'nome_catalogo': identity[1] if identity else None,
                         'arquivo': rel, 'origens': [r['arquivo'] for r in group['rows']],
                         'sha256_origem': digest, 'sha256_webp': hashlib.sha256(binary).hexdigest(),
                         'status': 'IMPORTADA_LOCAL_SEM_HOMOLOGACAO', 'vinculo': 'CONFIRMADO' if identity else 'SEM_VINCULO_CONFIRMADO'}
                manifest.setdefault('artes_locais', []).append(entry)
                # Registrar cada imagem permite retomar após uma interrupção.
                MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
                for row in group['rows']:
                    row.update(status='IMPORTADO', destino=rel, vinculo=entry['vinculo'])
            except Exception as exc:
                for row in group['rows']:
                    row.update(status='ERRO_CONVERSAO', motivo=str(exc))
        for dest, envelope, entry in planned:
            if load(dest) != envelope:
                raise RuntimeError('Verificação de ficha gravada falhou: ' + str(dest))
    report = {'data': datetime.now().isoformat(timespec='seconds'), 'modo': 'APLICAR' if args.aplicar else 'ANALISE', 'novas_fichas': len(planned), 'resumo_fichas': dict(Counter(r['status'] for r in rows)), 'artes_planejadas': art_count, 'resumo_imagens': dict(Counter(r['status'] for r in image_rows)), 'arquivos_imagens': image_rows, 'arquivos_fichas': rows, 'publicado': False}
    args.relatorio.parent.mkdir(parents=True, exist_ok=True)
    args.relatorio.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if not k.startswith('arquivos_')}, ensure_ascii=True, indent=2))
    print('Relatorio:', args.relatorio)
    return 1 if any(r['status'].startswith('ERRO_') for r in image_rows) else 0


if __name__ == '__main__':
    raise SystemExit(main())
