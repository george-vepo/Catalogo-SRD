# Integração inicial do Google Drive — 21/10/2026

**Origem externa (lida, sem alteração):** Google Drive → `SRD Card Game` → `Imagens/{Existentes,Novas,Em Revisao}` e `Fichas/{Completas,Em Pesquisa}`.

Esta entrega integra **somente um lote piloto auditável de 3 imagens e 3 fichas SRD** ao Catálogo SRD. Não representa a importação de todas as imagens/fichas do Drive, nem substitui os dados canônicos do catálogo-base.

## Materiais preservados no repositório

| Identidade | Conteúdo | Proveniência | Tratamento |
| --- | --- | --- | --- |
| AT-001 · Gibbering Mouther | imagem WebP + ficha JSON | Drive / Imagens / Existentes; Fichas / Completas | Imagem **candidata**, ficha SRD complementar sem homologação |
| TF-002 · Ahu-Nixta, Drudge | imagem WebP | Drive / Imagens / Existentes | Arte candidata; ficha de terceiro **não** republicada sem revisão dos direitos |
| Cranium Rat · candidato externo (sem ID canônico no catálogo) | imagem WebP | Drive / Imagens / Existentes | **Não atribuir automaticamente `EXT-0001` ao jogo**: a megalista não aprova esse ID; imagem somente por nome exato e rotulada candidata |
| AT-002 · Roper | ficha JSON | Drive / Fichas / Completas | SRD 5.2.1, original preservado, não sobrescreve mecânicas |
| AT-023 · Giant Owl | ficha JSON | Drive / Fichas / Completas | SRD 5.2.1, original preservado, não sobrescreve mecânicas |

**Arquivo de controle:** `docs/catalogo/data/drive-import-20261021.json` contém IDs/nome canônico, caminhos relativos internos, origem de arquivos, status e aviso de direitos. Os três WebP estão em `docs/catalogo/assets/drive-candidatas-20261021/`, e as três fichas originais em `docs/catalogo/data/drive-fichas-srd-20261021/`.

A interface `docs/catalogo/app.js` consulta o manifesto. As imagens **aparecem apenas dentro do painel de detalhes**, sob aviso explícito de candidatura; **não** substituem a arte da grade nem recebem classificação `REFERENCIA_VISUAL_ACEITA`. Fichas são carregadas **sob demanda**, com conferência de identidade por ID, e aparecem como JSON textual adicional. Os 1.320 registros e os `fichas-607.json` originais permanecem intactos.

## Auditoria, proteção de dados e limites

- `Fichas/Completas` contém vários arquivos de origens e versões diferentes; o rótulo de pasta **não equivale à aprovação administrativa**.
- A pasta `Imagens/Novas` possui centenas de candidatas, muitas com sufixo `candidata-nao-homologada`. `Imagens/Em Revisao` inclui imagens **rejeitadas** (espécie incorreta, anatomia errada etc.). Elas **não** foram promovidas.
- `Imagens/Existentes` mostrou 44 WebP no momento da consulta; parte já estava representada no catálogo em `artes-geradas-20261015.json`. **Não duplicar** os 30 registros existentes, nem substituir artes aprovadas.
- O uso/republicação dessas novas imagens em mídia pública continua **pendente de confirmação de direitos e curadoria**. A inclusão técnica dos arquivos não equivale a autorização jurídica/estética. Antes de merge/publicação pública, o administrador deve confirmar esses pontos.
- Não publicar IDs privados do Google Drive, mãos, decks, checkpoints, ordem de montes ou conteúdo arbitrário de terceiros. Fichas não SRD não são copiadas integralmente neste lote.
- Não trocar ND, tipo, raridade, CA, PV nem habilidades canônicas com base somente em arquivos recém encontrados. Avaliar divergências antes de homologar.
- O GitHub Pages do catálogo é distinto do GitHub Pages do Ascend Card Game; a importação aqui altera **somente o catálogo**.

## Verificação automatizada

`python scripts/validar-ingestao-drive-20261021.py` valida os caminhos, assinaturas WebP, limites de tamanho, nomes e IDs cruzados com os 1.320 registros, conteúdo JSON, estatuto pendente, impedimento de substituição da ficha-base e preservação da megalista. `node --check docs/catalogo/app.js` valida a sintaxe do website.

## Próximo lote

Inventariar as fichas por ID canônico, SHA-256, fonte/edição e pendências, inclusive nomes `(1)`; comparar com o acervo já versionado. Para imagens, começar pelas 44 em `Existentes` e triagem de `Novas`, **sem transformar automaticamente imagem candidata em aprovada**. Obter aceite explícito dos direitos/curadoria antes de publicação pública ou de uso em cartas comerciais. Os outros lotes estão fora do escopo deste PR.
