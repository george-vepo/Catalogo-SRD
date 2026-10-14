# SRD Card Game 607 — Auditoria final (parcial)

**Situação:** EM ANDAMENTO — 11 lotes validados, 110/395 fichas (285 restantes).

**Fonte:** branch `chatgpt/srd607-audit-imaged-cards-20261014`, snapshot anterior à auditoria `c75c62c616e34af98593ecc0de895dd2f7dabeaf`; CSV `operational/research/catalog-ledger-20261011-v27/catalog-status.csv` (`Mecanica_completa=NAO`: 395 de 607).

**Execução:** leitura e persistência via conector GitHub no chat interativo. **V-Bridge Windows e computer-use: não executados/não verificados neste ambiente**. Sem modificações do catálogo canônico nem merge.

## Resultado do primeiro lote (detalhe histórico)

| ID | Criatura | Classificação da ficha | Imagem | Observação principal |
|---|---|---|---|---|
| KP-S011 | /A/b/o/m/i/n/a/b/l/e/ /B/e/a/u/t/y/ | FICHA_NAO_VERIFICAVEL | Vinculada diretamente (Git SHA/tamanho conferidos) | Conflito entre versões 2016/2023, sem definição da edição-alvo |
| KP-S013 | /G/i/a/n/t/,/ /J/o/t/u/n/ | FICHA_INCOMPLETA | Vinculada diretamente (Git SHA/tamanho conferidos) | 11 mecânica(s) ainda em resumo não executável |
| KP-S014 | /P/u/s/t/u/l/e/n/t/ /S/h/a/m/b/l/e/r/ | FICHA_INCOMPLETA | Vinculada diretamente (Git SHA/tamanho conferidos) | 8 mecânica(s) ainda em resumo não executável |
| KP-S015 | /O/o/z/e/,/ /S/c/i/n/t/i/l/l/a/t/i/n/g/ | FICHA_INCOMPLETA | Vinculada diretamente (Git SHA/tamanho conferidos) | 11 mecânica(s) ainda em resumo não executável |
| KP-S016 | /F/i/r/s/t/ /S/e/r/v/a/n/t/ | FICHA_INCOMPLETA | Vinculada diretamente (Git SHA/tamanho conferidos) | 6 mecânica(s) ainda em resumo não executável |
| KP-S017 | /V/e/s/i/c/u/l/o/s/a/ | FICHA_INCOMPLETA | Vinculada diretamente (Git SHA/tamanho conferidos) | 1 mecânica(s) ainda em resumo não executável |
| KP-S018 | /S/i/n/s/t/a/r/ | FICHA_INCOMPLETA | Vinculada diretamente (Git SHA/tamanho conferidos) | 17 mecânica(s) ainda em resumo não executável |
| TF-004 | /A/s/t/r/a/l/ /S/n/a/p/p/e/r/ | FICHA_INCOMPLETA | Vinculada diretamente (Git SHA/tamanho conferidos) | 3 mecânica(s) ainda em resumo não executável |
| TF-010 | /C/h/e/l/i/c/e/r/a/e/ | FICHA_INCOMPLETA | Vinculada diretamente (Git SHA/tamanho conferidos) | 9 mecânica(s) ainda em resumo não executável |
| TF-011 | /C/h/i/l/d/ /o/f/ /Y/g/g/d/r/a/s/i/l/ | FICHA_INCOMPLETA | Vinculada diretamente (Git SHA/tamanho conferidos) | 5 mecânica(s) ainda em resumo não executável |

**Totais verificados neste lote:** 9 incompletas, 1 não verificável, 10 com imagem física vinculada diretamente, 0 homologadas; 3 imagens com alguma dimensão declarada menor que 500 px (KP-S015, KP-S016, KP-S018). Nenhuma identidade visual nem licença foi aprovada.

**Matriz (somente 10 auditadas):** fichas completas com imagem 0; completas sem imagem 0; incompletas ou não verificáveis com imagem 10; incompletas ou não verificáveis sem imagem 0.

**Próxima etapa:** lote 002 a partir de `TF-012`; verificar cada JSON, arquivo/vínculo de imagem e regras, persistindo evidências por lote.

**Limites da auditoria:** a existência de arquivo Git com SHA/tamanho compatíveis não prova que a imagem é adequada, licenciada ou utilizada pelo motor do jogo; a presença de atributos no JSON não prova fidelidade à fonte nem adaptação ao jogo de cartas. Evidências individuais estão em `batches/batch-001.json` e `audit-results.csv`.

## Lote 002 — TF-012 a TF-024 (seleção exata por CSV)

9 fichas incompletas, 1 completa com ressalvas (TF-024), 9 imagens vinculadas diretamente, 1 imagem ausente (TF-022). Três imagens de resolução baixa: TF-019 280×280, TF-020 190×190 e TF-021 280×280. TF-024 tem Illumination e Horn estruturadas, mas nota sobre dependência alimentar precisa de cotejo com a fonte editorial. Os outros nove registros têm habilidades com `status=INCOMPLETA` e `legacy_summary`, não mecânicas completas para execução. Não houve homologação nem verificação visual/licença.

## Lote 003 — 10 fichas (TF-025 a TF-034 conforme CSV)

**10 fichas completas em conteúdo**, pendentes de edição/licença/adaptação; 9 imagens diretamente vinculadas, 1 ausente (TF-034); 8 imagens têm ao menos uma dimensão menor que 500 px conforme metadados. TF-026 referencia miniatura 160×160 e TF-031 referencia prova 80×120, embora haja alternativas no diretório central ainda não vinculadas diretamente às fichas. TF-025 tem arquivo físico apesar da anotação legado de ausência. Nenhuma ficha/arte foi homologada.

## Consolidação validada após lote 003

Foram processadas **30 fichas de 395**: 10 completas em conteúdo, 1 completa com ressalvas, 18 incompletas e 1 não verificável. Imagens: 28 vínculos diretos confirmados e 2 ausentes. A matriz é: completas em conteúdo com imagem 9, completas sem imagem 1; com ressalvas e imagem 1; incompletas/não verificáveis com imagem 18 e sem imagem 1. A classificação de conteúdo não concede autorização de uso/produção. Corrigida soma da matriz provisória após o lote 002.

## Lote 004 — 10 fichas (TF-035–TF-045, ordem do CSV)

8 completas em conteúdo e 2 completas com ressalvas: TF-039 possui divergência numérica Bite/Puff Up e TF-041 possui interpretação pendente do Multiattack/Proboscis. Todas as 10 têm arquivo de imagem diretamente vinculado com SHA/tamanho confirmado. 5 imagens têm dimensão declarada inferior a 500 px. TF-045 exige conciliar a nomenclatura Aaxte/Aatxe. Nenhuma foi homologada para publicação.

## Lote 005 — 10 fichas (TF-046 a TF-057 conforme CSV)

8 completas em conteúdo, 1 completa com ressalvas (TF-047, Celestial Weapons +4d8 vs Greataxe +3d8), e 1 incompleta (TF-052, CD ausente em Celestial Crescendo). 9 imagens vinculadas e 1 ausente (TF-049). 5 imagens de resolução baixa pelos metadados. TF-049 usa mecânicas A5E completas na fonte RPG, mas depende de adaptação explícita ao card game; não foi validada em engine nem aprovada para publicação.

**Consolidado após lote 005:** 50/395 auditadas; 26 completas em conteúdo, 4 com ressalvas, 19 incompletas, 1 não verificável; 47 com vínculo direto e 3 sem imagem. Nenhuma licenciada/homologada nesta execução.

## Lote 006 — transição A/B

10 fichas avaliadas: 6 completas em conteúdo e 4 completas com ressalvas (TF-059, TF-060, TF-062, TF-065). Duas imagens ligadas diretamente pelo JSON do grupo A; oito associadas explicitamente pelo manifesto de aquisição E no grupo B, com SHA/tamanho equivalentes aos binários Git consultados. TF-058 usa arte 300×434, baixa resolução. Divergências: Four-Part Harmony, Bite entre edições, PV TF-062 e versão Clockwork Hound. Não confundir o campo `bloqueado` editorial dos B com ausência de mecânicas no JSON.

**Consolidado 6 lotes:** 60/395; 32 fichas completas em conteúdo, 8 com ressalvas, 19 incompletas, 1 não verificável; 49 imagens diretamente vinculadas, 8 por manifesto, 3 ausentes. Nenhuma conclusão/homologação de produção.

## Lote 007 — TF-068 a TF-079 (dez IDs da ordem canônica)

9 completas em conteúdo, 1 com ressalvas (TF-079: Heavy Pick citado mas ataque War Pick definido). Dez imagens existentes e vinculadas pelo manifesto E, não pelo JSON individual do grupo B; TF-070 (373×700) e TF-071 (475×800) abaixo de 500 px. **TF-069** tem imagens distintas no diretório B (WebP) e central (JPG) e o manifesto referencia a central; a identidade precisa de verificação visual. Todas pendentes de validação de edição/licença e adaptação ao card game.

**Consolidado:** 70/395 auditadas; 41 completas em conteúdo, 9 com ressalvas, 19 incompletas, 1 não verificável; 49 vínculos diretos, 18 por manifesto, 3 imagens ausentes. A fase não é homologação final.

## Lote 008 — TF-080–TF-091 (10 IDs da ordem de CSV)

7 fichas completas em conteúdo, 3 completas com ressalvas: TF-083 exige conferência literal de `exhausted`, TF-089 tem divergência de idiomas/volume e duração de Enthralling Speech, TF-091 apresenta variantes editoriais entre 2016/2023. Dez imagens vinculadas pelo manifesto E; SHA e tamanho conferidos. Nenhuma arte homologada nem licença aprovada.

**Consolidado:** 80/395; 48 fichas completas em conteúdo, 12 completas com ressalvas, 19 incompletas, 1 não verificável; 49 imagens diretas, 28 por manifesto, 3 ausentes.

## Lote 009 — TF-094–TF-105 (dez IDs na ordem do CSV)

7 completas em conteúdo; 3 completas com ressalvas: TF-094 (Whirlpool indefinido em caso de sucesso), TF-095 (poder Prophesy Doom citado mas ausente) e TF-099 (INT +5/+3, atribuição das mecânicas de toca e discrepância de artes). Dez imagens vinculadas via manifestos com SHA e bytes conferidos: TF-094/095 no grupo B com direitos restritos **a uso não comercial**, demais oito pelo manifesto E; TF-099 dispõe de duas imagens diferentes nos diretórios B e central, sem validação da escolha final. TF-101 (472×700) e TF-103 (459×800) apresentam largura inferior a 500 px. Qualidade visual e licenças restantes não homologadas.

**Consolidado:** 90/395, 55 completas, 15 com ressalvas, 19 incompletas e 1 não verificável; 49 imagens diretas, 38 por manifesto e 3 ausentes. O próximo ID correto após a reconciliação é TF-106; o checkpoint anterior indicava TF-092 indevidamente.


## Lote 010 — TF-106–TF-115 (dez IDs da ordem do CSV)

7 completas em conteúdo, 3 completas com ressalvas: TF-110 (origem editorial divergente Tome of Beasts 1 vs 2), TF-113 (homônimo/edições distintas do Clurichaun) e TF-115 (Acrobatics +3 apesar de DES 18, valor a conferir). As dez imagens físicas estão vinculadas pelo manifesto E, com SHA Git e bytes conferidos; TF-115 tem largura 481 px. TF-107 é a versão 2023 explicitamente escolhida, distinta da edição antiga. Não representa autorização de direitos, inspeção visual ou adaptação concluída.

**Consolidado:** 100/395, 62 completas em conteúdo, 18 com ressalvas, 19 incompletas, 1 não verificável; 49 imagens diretas, 48 vinculadas por manifesto e 3 ausentes.


## Lote 011 — TF-116–TF-125 (10 IDs da ordem do CSV)

6 completas em conteúdo, 3 com ressalvas (TF-121: Multiattack por forma e typo original; TF-123: conflito de copyright/proveniência da fonte que contém ações lendárias; TF-125: Trunk Slam sem restrição inequívoca de forma) e 1 incompleta (**TF-124**: Bestowal of Trust sem custo/ação e alcance). A partir de TF-120 começa o grupo C, com referência direta a imagens no JSON; quatro primeiras imagens vinculadas via manifesto E. Dez imagens presentes com SHA e bytes verificados. Duas com dimensão inferior a 500 px. Não houve cotejo integral do original impresso, homologação de arte ou adaptação de card game.

**Consolidado:** 110/395; 68 completas em conteúdo, 21 com ressalvas, 20 incompletas, 1 não verificável; 55 imagens diretas, 52 via manifesto, 3 ausentes.

