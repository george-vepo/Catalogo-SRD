# Integração inicial do Google Drive — 21/10/2026

**Origem externa (lida, sem alteração):** Google Drive → `SRD Card Game` → `Imagens/{Existentes,Novas,Em Revisao}` e `Fichas/{Completas,Em Pesquisa}`.

Esta entrega integra **14 imagens autorais e 3 fichas complementares SRD 5.2.1** ao Catálogo SRD. As imagens foram geradas pelo usuário, que **autorizou explicitamente a publicação no Catálogo SRD em 21/10/2026**. Isso não homologa automaticamente a identidade visual de cada criatura ou as mecânicas. Não representa a importação de todas as imagens/fichas do Drive, nem substitui os dados canônicos do catálogo-base.

## Materiais preservados no repositório

| Identidade | Conteúdo | Proveniência | Tratamento |
| --- | --- | --- | --- |
| AT-001 · Gibbering Mouther | imagem WebP + ficha JSON | Drive / Imagens / Existentes; Fichas / Completas | Imagem **candidata**, ficha SRD complementar sem homologação |
| TF-002 · Ahu-Nixta, Drudge | imagem WebP | Drive / Imagens / Existentes | Arte candidata; ficha de terceiro **não** republicada sem revisão dos direitos |
| Cranium Rat · candidato externo (sem ID canônico no catálogo) | imagem WebP | Drive / Imagens / Existentes | **Não atribuir automaticamente `EXT-0001` ao jogo**: a megalista não aprova esse ID; imagem somente por nome exato e rotulada candidata |
| AT-002 · Roper | ficha JSON | Drive / Fichas / Completas | SRD 5.2.1, original preservado, não sobrescreve mecânicas |
| AT-023 · Giant Owl | ficha JSON | Drive / Fichas / Completas | SRD 5.2.1, original preservado, não sobrescreve mecânicas |

**Arquivo de controle:** `docs/catalogo/data/drive-import-20261021.json` contém IDs/nome canônico, caminhos relativos internos, origem de arquivos, status e aviso de direitos. Os 14 WebP estão em `docs/catalogo/assets/drive-candidatas-20261021/`, e as três fichas originais em `docs/catalogo/data/drive-fichas-srd-20261021/`.

A interface `docs/catalogo/app.js` consulta o manifesto. Quando há um ID canônico exato e nenhuma imagem principal existente, a arte autoral aparece **na grade e no detalhe**, com rótulo *Arte do autor · em revisão*. Imagens **sem ID aprovado** (Cranium Rat e Gazer) aparecem **somente no detalhe por nome**, sem criar identidade fictícia. Nenhuma substitui imagem principal preexistente nem recebe automaticamente classificação `REFERENCIA_VISUAL_ACEITA`. Fichas são carregadas **sob demanda**, com conferência de identidade por ID, e aparecem como JSON textual adicional. Os 1.320 registros e os `fichas-607.json` originais permanecem intactos.

## Auditoria, proteção de dados e limites

- `Fichas/Completas` contém vários arquivos de origens e versões diferentes; o rótulo de pasta **não equivale à aprovação administrativa**.
- A pasta `Imagens/Novas` possui centenas de candidatas, muitas com sufixo `candidata-nao-homologada`. `Imagens/Em Revisao` inclui imagens **rejeitadas** (espécie incorreta, anatomia errada etc.). Elas **não** foram promovidas.
- `Imagens/Existentes` mostrou 44 WebP no momento da consulta: após conciliar os nomes/IDs com os 30 registros em `artes-geradas-20261015.json`, foram arquivados **14 arquivos ainda não representados**. Não foram duplicados os 30 registros existentes, nem substituídas imagens principais aprovadas.
- **Direitos de publicação no Catálogo SRD:** o usuário declarou ser criador das imagens e solicitou expressamente sua publicação. A autorização está registrada no manifesto; não deve ser confundida com homologação editorial de espécie, fidelidade visual, licença de propriedades intelectuais de terceiros ou aprovação mecânica. Imagens classificadas como rejeitadas na pasta `Em Revisao` não foram importadas.
- Não publicar IDs privados do Google Drive, mãos, decks, checkpoints, ordem de montes ou conteúdo arbitrário de terceiros. Fichas não SRD não são copiadas integralmente neste lote.
- Não trocar ND, tipo, raridade, CA, PV nem habilidades canônicas com base somente em arquivos recém encontrados. Avaliar divergências antes de homologar.
- O GitHub Pages do catálogo é distinto do GitHub Pages do Ascend Card Game; a importação aqui altera **somente o catálogo**.

## Verificação automatizada

`python scripts/validar-ingestao-drive-20261021.py` valida os caminhos, assinaturas WebP, limites de tamanho, nomes e IDs cruzados com os 1.320 registros, conteúdo JSON, estatuto pendente, impedimento de substituição da ficha-base e preservação da megalista. `node --check docs/catalogo/app.js` valida a sintaxe do website.

## Próximo lote

Inventariar as fichas por ID canônico, SHA-256, fonte/edição e pendências, inclusive nomes `(1)`; comparar com o acervo já versionado. Para imagens, continuar pela triagem de `Novas`, **sem transformar automaticamente imagem candidata em aprovada**. Obter aceite explícito dos direitos/curadoria antes de publicação pública ou de uso em cartas comerciais. Os outros lotes estão fora do escopo deste PR.

## Ampliação do lote de imagens existentes

Além dos 3 arquivos iniciais, foram arquivados mais **11 WebP** sem duplicar os registros que já existiam: Gazer (sem ID canônico), Ahu-Nixta (TF-001), Asanbosam (TF-003), Astral Snapper (TF-004), Birgemon Seal (TF-005), Xenabsorber (TF-006), Yann-An-Oed (TF-007), Light Eater (TF-272), Shoth, Sooze (TF-273), Malleable, Minor (TF-274) e Maw Swarm (TF-275). Todas as 14 imagens são rotuladas como arte autoral com publicação autorizada e correspondência editorial em revisão.

**Ainda não concluído:** não foram importadas as centenas de imagens em `Imagens/Novas`, nem as fichas completas além das 3 SRD do primeiro lote. A pasta `Em Revisao` não deve ser aprovada automaticamente. O arquivo de manifesto não inclui dados pessoais, tokens ou URLs privados do Drive.

## Lote adicional — Imagens / Novas (21/10/2026)

Quatro PNGs originários da pasta **Novas** foram ligados por ID canônico exato: **TF-018 Voidling, TF-017 Ancient Aboleth, TF-015 Aboleth Brute e TF-012 Xhkarsh**. Os nomes dos arquivos incluem `candidata-nao-homologada`, portanto o manifesto guarda explicitamente `preview_na_grade: false`: estas imagens aparecem apenas no painel de detalhes com aviso de revisão e não substituem as imagens principais do catálogo. A autorização do usuário cobre sua publicação, não a homologação visual ou mecânica.

O inventário passa a **19 imagens autorais** e **12 fichas SRD complementares** no manifesto, preservando 1.320 registros. A pasta Novas contém mais arquivos do que a primeira página listada pelo Drive; não declarar inventário integral com base no retorno limitado da consulta. Priorizar próximos lotes após deduplicação por ID e revisão visual da espécie.

## Fichas originais SRD: Cat e Owl (21/10/2026)

Integração de mais **2 fichas estruturadas** em JSON diretamente de `Fichas/Completas`: **AT-009 Cat** e **AT-010 Owl**. Esses arquivos usam esquema plano com `id_catalogo` na raiz, diferente das fichas anteriores. O site e o validador passaram a conferir também esse campo; o conteúdo original foi preservado sem inferir habilidades e sem substituir a ficha-base. Ambas declaram edição SRD 5.2.1 e continuam sem homologação administrativa. Total atualizado: **19 artes candidatas e 14 fichas complementares**, com 1.320 criaturas intactas. O inventário da pasta Imagens/Novas agora está em `auditoria/drive-novas-inventario-20261021.json` (567 arquivos), distinto dos assets publicados.
