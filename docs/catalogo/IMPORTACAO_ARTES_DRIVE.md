# Importador local de artes do Drive (candidatas)

O Google Drive privado não é acessível aos runners do GitHub Actions. Por isso este script **não usa tokens, URLs ou IDs do Drive**, nem publica imagens automaticamente. Execute-o no PC que tenha a pasta \`Imagens/Novas\` sincronizada.

## Requisitos

- Python 3.11+ e \`python -m pip install Pillow\`.
- Repositório \`george-vepo/Catalogo-SRD\` clonado localmente, com Git autenticado.
- Diretório local contendo os PNG/WebP autorais da pasta \`Imagens/Novas\`.

## Simular (nenhuma escrita)

\`\`\`powershell
python scripts/importar_artes_drive.py --source "D:\SRD Card Game\Imagens\Novas"
\`\`\`

## Importar lote pequeno

\`\`\`powershell
git switch -c feat/drive-webp-lote-local
python scripts/importar_artes_drive.py --source "D:\SRD Card Game\Imagens\Novas" --apply --limit 20
python scripts/validar-ingestao-drive-20261021.py
git status --short
git diff -- docs/catalogo/data/drive-import-20261021.json
\`\`\`

Após conferir visualmente, fazer commit e PR pelo fluxo normal. O script **não faz push nem merge**. Pode filtrar \`--ids AT-003,AT-009,AT-010,AT-024\`. Os arquivos citados são exemplos de IDs; os caminhos acima devem ser adaptados à pasta real.

## Proteções

- Usa **apenas IDs canônicos e nome correspondente à megalista de 1.320 criaturas**.
- Recusa rejeitadas e arquivos com \`revisar\`/ \`revisao\` no nome; também bloqueia candidatos com hash idêntico a uma imagem sinalizada para revisão.
- Deduplica arquivos idênticos da mesma criatura; quando existem versões diferentes, **não escolhe uma imagem arbitrariamente**.
- Se a mesma imagem for atribuída a IDs de criaturas diferentes, não importa automaticamente.
- Ignora IDs que já estão no manifesto, não substitui a arte principal nem as fichas base.
- Converte para WebP otimizado e gera SHA-256 do original e do WebP.
- Novas artes são \`CANDIDATA_NOVAS_NAO_HOMOLOGADA\`, só nos detalhes (\`preview_na_grade: false\`).
- O importador limita cada execução a 20 artes (máximo configurável de 50); requer \`--apply\` para escrever.

Os dados de status derivam dos nomes dos arquivos: passam apenas por verificação técnica. **Isso não equivale à homologação visual.** Um revisor deve confirmar anatomia, variante, tipo e direitos antes de promover uma arte.
