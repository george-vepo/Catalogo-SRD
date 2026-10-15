# Auditoria de imagens e fichas — lote conservador de 15/10/2026

> **NÃO CONCLUÍDA.** Uma lista com 1.320 criaturas exige verificação individual da identidade, edição, enquadramento, fonte e direitos da arte, além de auditoria das regras. Este lote importa apenas itens verificáveis; todo o restante permanece pendente.

## Contagem do snapshot do site

| Métrica | Situação |
|---|---:|
| Criaturas únicas na grade | **1.320** |
| Registros mecânicos do acervo 607 | **607** (inclui KP-S007 associado, não fundido a TF-085) |
| Fichas com **texto integral local** já documentadas | **108** |
| Registros com mecânica externa integrada como resumo próprio | **113** |
| Fichas detalhadas adicionais da pesquisa E exibidas no novo painel | **6** |
| URLs de imagem verificadas pela auditoria antiga | **23** |
| Ilustrações identificadas pelo deck Celestial | **9 criaturas** |
| Novas imagens aceitas após análise individual neste lote | **4 IDs** |
| Total distinto de cartas com **uma referência visual para exibição** | **35** |
| Cartas sem referência visual exibível aprovada no snapshot | **1.285** |

**Atenção:** 35 não significa 35 imagens com licença de republicação comercial ou editorialmente homologadas. 23 tiveram arquivo/identidade/dimensões registrados no controle anterior; nove vieram da pesquisa visual Celestial (com ressalvas de origem/edição); quatro são novas revisões visuais, com uma sobreposição no Pegasus. Direitos de reprodução permanecem por verificar. As imagens são **links de referência web**, não arquivos distribuídos pelo jogo.

## 4 referências adicionadas ao catálogo

| ID | Criatura | Editora/página | Situação |
|---|---|---|---|
| AT-003 | Aboleth | D&D Beyond, ficha **Legacy** | Correspondência visual exata da espécie, com ressalva de edição |
| AT-009 | Cat | D&D Beyond | Arte da criatura correta, sem layout de carta |
| AT-012 | Giant Boar | D&D Beyond | Arte da criatura correta, isolada |
| AT-024 | Pegasus | D&D Beyond, ficha **Legacy** | Arte correta do Pegasus; substitui link de qualidade/origem inferior no deck |

As URLs exatas, versões, motivos da aceitação e observações sobre direitos estão no `data/curadoria-artes-20261015.json`.

## 5 candidatas rejeitadas e não integradas

| ID | Criatura | Razão |
|---|---|---|
| AT-016 | Giant Ape | Arte consultada com apêndices semelhantes a asas; risco de associação incorreta |
| AT-017 | Tyrannosaurus Rex | Enquadramento corta parte da criatura |
| AT-013 | Ankylosaurus | Enquadramento cortado, cauda não aparece adequadamente |
| AT-014 | Giant Crocodile | Ilustração de IA de origem visual não homologada ao D&D/SRD |
| AT-015 | Mammoth | Autoría, edição visual e direitos não suficientes para aprovação |

Também continuam recusadas para uso isolado as artes anteriores de **Archon, Word** (imagem de interface), **Aaxte/Aatxe** (imagem sem fidelidade comprovada à publicação da carta) e **Simurg** (arte integrada a outra carta com estatísticas/textos). Não usar outra espécie/edição incompatível como substituta.

## 6 fichas detalhadas integradas

- **TF-059 — Animated Instrument, Animated Quartet**
- **TF-060 — Clockwork Abomination**
- **TF-061 — Clockwork Armadillo**
- **TF-063 — Clockwork Beetle Swarm**
- **TF-064 — Clockwork Conductor**
- **TF-065 — Clockwork Hound**

Transcrições/reexpressões mecânicas em português já presentes nos arquivos `operational/research/complete-reference-e/statblocks/` do próprio repositório. Agora estão visíveis ao abrir a carta, **como referência D&D 5e; revisão independente e adaptação à engine do card game pendentes**. Não declarar novas fichas como `COMPLETA_CANONICA`.

## Pendências prioritárias

1. Validar visual e editorialmente cada uma das **519** imagens binárias preexistentes em `operational/assets/creature-images/`; existência de arquivo físico não é aprovação.
2. Validar fontes/licenças de imagens das trilhas de pesquisa profunda `a/b/c`, várias anotadas como tokens ou thumbnails de pesquisa, com **aprovação de produção = false**.
3. Buscar artes **isoladas, integrais, da criatura/edição certa** para os **1.285** registros sem imagem de referência aprovada. Pesquisa genérica por nome não é aceitação.
4. Completar auditoria de **atributos, ações, magias, resistências, CDs, condições e recursos** das fichas externas antes de promovê-las ao catálogo canônico.
5. Não misturar status da megalista provisória (aprovada somente para seleção) e fichas/habilidades homologadas.
6. Fazer revisão visual em diferentes tamanhos de tela após acesso via servidor HTTP, e checar link/HTTP de cada arte periodicamente.

## Método

Critério de importação: identificação por nome e origem; verificar que imagem mostra **a própria espécie**; descartar captura de interface, imagem com estatísticas impressas, watermark, corte severo, tokens minúsculos e artes de outra edição incompatível; manter link da página original, versão, ressalva de direitos e razão de aceitação. Não remover imagens originais do repositório nem alterar ledger sem decisão do administrador.

**Fonte canônica de dados:** `SRD_FICHAS_607.json`, `SRD_URLS_IMAGENS_607.csv`, `catalog-status.csv`, megalista e pesquisas E/`deep-mechanics` previamente versionadas. O site faz sobreposição visual/referencial; não modifica os dados desses arquivos.
