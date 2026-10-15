# Levantamento de criaturas para expansão SRD Card Game — versão de pesquisa 2026-10-14

> **NÃO É UM CATÁLOGO APROVADO.** Os números abaixo representam um levantamento editorial de pesquisa, não 1.320 cartas liberadas para jogo. Não altera o catálogo oficial de 607, as coleções dos jogadores nem os arquivos de fichas e imagens.

## Resultados e método

- **607** registros na base histórica monitorada do jogo (ledger v27; subset do catálogo ativo v2.0 de 635).
- **724** candidatos externos após deduplicação inicial de nomes e análise por tipo/ND; os mesmos podem exigir revisão de versão/alias.
- **1.331** registros na megalista anterior à segunda consolidação.
- **238** combinações de **tipo + ND** com pelo menos 2 criaturas na megalista anterior; **1.262** registros participam desses grupos. *Tipo + ND iguais por si só NÃO configuram duplicação.*
- **10** grupos com provável identidade nominal comum entre registros; total de **11** registros excluídos **apenas da vista depurada**, mantidos no arquivo de aliases.
- **1.320** registros distintos **provisórios**: **606** registros originais preservados na vista depurada e **714** candidatos externos.
- Um dos 607 originais (`KP-S007`, *Animated Instruments (Animated Symphony)*) foi movido **somente na cópia de pesquisa** para rastreabilidade como possível alias de `TF-085`; continua intacto no catálogo original.
- Nenhuma mudança de IDs/cópias, ND, raridade, zonas, pontuação ou estado oficial de partidas foi feita.

### Distribuição — tipo × raridade

| Tipo | Comum | Incomum | Rara | Lendária | Mítica | Total |
|---|---:|---:|---:|---:|---:|---:|
| Aberração | 41 | 27 | 16 | 5 | 5 | 94 |
| Besta | 79 | 9 | 2 | 1 | 0 | 91 |
| Celestial | 14 | 12 | 16 | 4 | 5 | 51 |
| Constructo | 52 | 27 | 8 | 4 | 4 | 95 |
| Dragão | 28 | 23 | 13 | 14 | 27 | 105 |
| Elemental | 28 | 20 | 6 | 3 | 2 | 59 |
| Feérico | 61 | 23 | 12 | 2 | 2 | 100 |
| Gigante | 24 | 29 | 12 | 2 | 2 | 69 |
| Gosma | 26 | 17 | 2 | 0 | 0 | 45 |
| Humanoide | 97 | 47 | 12 | 4 | 0 | 160 |
| Ínfero | 39 | 32 | 22 | 9 | 17 | 119 |
| Monstruosidade | 104 | 33 | 26 | 3 | 3 | 169 |
| Morto-vivo | 51 | 29 | 13 | 7 | 2 | 102 |
| Planta | 40 | 18 | 2 | 1 | 0 | 61 |
| TOTAL | 684 | 346 | 162 | 59 | 69 | 1320 |

Raridade calculada exclusivamente pelo **ND principal**, não pelo ND alternativo de covil: Comum 0–5, Incomum 6–10, Rara 11–15, Lendária 16–20, Mítica 21+.

## Arquivos versionados

| Arquivo | Conteúdo | Linhas de dados |
|---|---|---:|
| [megalista-1320-distintos-provisorios.csv](megalista-1320-distintos-provisorios.csv) | Lista depurada, nomes, ND, fonte, tipo, raridade, origem, ID e links de fonte; registra grupos/aliases e grau de validação | **1.320** |
| [megalista-1331-pre-consolidacao.csv](megalista-1331-pre-consolidacao.csv) | Preservação da base inicial, antes das 11 consolidações editoriais | **1.331** |
| [aliases-11-consolidados.csv](aliases-11-consolidados.csv) | Registro original, sobrevivente, IDs e justificativa de cada consolidação provisória | **11** |
| [grupos-10-duplicatas-provisorias.csv](grupos-10-duplicatas-provisorias.csv) | Identificação dos 10 grupos de aliases potenciais | **10** |
| [auditoria-238-grupos-tipo-nd.csv](auditoria-238-grupos-tipo-nd.csv) | Grupos de coincidência tipo + ND, componentes e IDs originais | **238** |
| [analise-238-grupos.csv](analise-238-grupos.csv) | Triagem nominal de todos os 238 grupos | **238** |
| [auditoria-1262-cartas-em-grupos-repetidos.csv](auditoria-1262-cartas-em-grupos-repetidos.csv) | As 1.262 linhas detalhadas das cartas agrupadas no levantamento anterior | **1.262** |
| [matriz-1320-tipo-raridade.csv](matriz-1320-tipo-raridade.csv) | Contagem por 14 tipos e 5 raridades; linha TOTAL | **15** |
| [deck-aberracao-40-proposta.csv](deck-aberracao-40-proposta.csv) | Baralho experimental de 40 Aberrações; 35 do ledger + 5 candidatos externos | **40** |

Todos os CSVs são UTF-8 e separados por ponto e vírgula. As linhas dos relatórios de coincidências se referem **à megalista original de 1.331**, não representam necessariamente a distribuição exata dos 1.320 após consolidar os aliases.

## Fontes de dados

- Catálogo ativo do projeto: `SRD_Card_Game_Catalogo_Ativo_v2_0_635.xlsx` (arquivo de origem fornecido na conversa) e ledger oficial `operational/research/catalog-ledger-20261011-v27/catalog-status.csv`.
- Fontes externas pesquisadas (levantamento **não exaustivo**, sujeito a revisões e traduções): *Tome of Beasts 3* (Kobold Press), *Fizban's Treasury of Dragons*, *Van Richten's Guide to Ravenloft*, *Eberron: Rising from the Last War* e *Mordenkainen Presents: Monsters of the Multiverse* (D&D).
- Índices estruturados auxiliares: [5etools dataset](https://github.com/5etools-mirror-3/5etools-src) e [Kobold Press dataset](https://github.com/TheGiddyLimit/homebrew); esses índices não substituem as fontes editoriais e podem apresentar erros.
- As colunas de URLs nas planilhas remetem aos catálogos e índices consultados; nem todas as 714 candidatas têm fichas, imagens ou licença individualmente verificadas.
- Para cruzamento com fichas/imagens já auditadas: `operational/reviews/20261014-imaged-cards/final-audit/`.
- Para pesquisa aprofundada de um deck de 40 Aberrações: [pacote de pesquisa](../decks/aberracao-40-20261014/README.md), com 3 fichas integrais SRD 5.2.1, evidências de 7 fichas pendentes, inventário de imagens e licenças.

## Critérios de homologação

1. **Identidade**: mesma criatura entre aliases e versões deve ser confirmada por fonte e bloco mecânico (não basta nome/ND/tipo). No levantamento houve exclusões **reversíveis**, não decisões canônicas.
2. **Tipo e ND**: conferir para cada edição; não mesclar versões com ND ou ações divergentes.
3. **Fichas**: não importar conteúdo incompleto ou protegido sem licença. O SRD 5.2.1 permite o uso de seu texto nos termos CC BY 4.0 com atribuição; outros livros possuem termos próprios.
4. **Imagens**: URLs e arquivos localizados são referências visuais, **não comprovação de direito de reprodução**. Nenhuma imagem desta pesquisa foi homologada automaticamente.
5. **Jogo**: cartas externas aguardam decisão do administrador, IDs individuais de cópia e autorização antes de serem consideradas elegíveis em decks oficiais.

**Status geral:** consolidação de pesquisa preservada para auditoria, sem merge automático para dados oficiais.
