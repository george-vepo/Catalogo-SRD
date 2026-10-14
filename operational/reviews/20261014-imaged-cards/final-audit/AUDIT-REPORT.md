# SRD Card Game 607 — Auditoria final (parcial)

**Situação:** EM ANDAMENTO — 16 lotes validados, 160/395 fichas (235 restantes).

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


## Lote 012 — TF-126–TF-135 (dez IDs da ordem do CSV)

9 fichas completas em conteúdo e 1 completa com ressalvas: TF-132 (Gravel Spray condicionado a Chew Rock; fonte não esclarece se a carga triturada é consumida por disparo). As dez imagens são vinculadas diretamente pelos JSONs no diretório C e seus SHAs/tamanhos foram conferidos. TF-127 tem largura de 476 pixels, inferior a 500 px. A comparação com obras originais e erratas, inspeção visual independente e licenças comerciais continuam pendentes.

**Consolidado:** 120/395; 77 completas em conteúdo, 22 com ressalvas, 20 incompletas e 1 não verificável. Imagens: 65 diretas, 52 via manifesto e 3 ausentes.


## Lote 013 — TF-136–TF-147 (10 IDs conforme ordem do CSV)

6 completas em conteúdo, 3 com ressalvas: TF-136 (erro de digitação na DC), TF-138 (Rock +2 descompassado de FOR22) e TF-144 (combinação de ataques no Multiattack sem confirmação). **TF-143 é incompleta**: fonte não relaciona cada espírito a um traço perdido ao expulsá-lo. Dez imagens físicas diretamente vinculadas nos JSONs C, com SHA/tamanho conferidos; três imagens têm dimensão inferior a 500 px (TF-138, TF-139 e TF-143). Não houve homologação de arte, fonte editorial ou direitos.

**Consolidado:** 130/395; 83 completas em conteúdo, 25 com ressalvas, 21 incompletas, 1 não verificável; 75 vínculos diretos, 52 via manifesto, 3 imagens ausentes.


## Lote 014 — TF-148–TF-157 (dez IDs do CSV)

8 fichas completas em conteúdo e 2 completas com ressalvas: TF-154 (fórmula de HP conflitante em livro/republicação), TF-157 (3 vs 4 ações lendárias entre fontes). Dez imagens diretamente vinculadas e hashes/tamanhos conferidos; TF-157 tem largura 490 px. Sem homologação de direito comercial ou identidade visual.

**Consolidado:** 140/395; 91 completas em conteúdo, 27 com ressalvas, 21 incompletas e 1 não verificável. Imagens: 85 diretas, 52 por manifesto, 3 ausentes.


## Lote 015 — TF-158–TF-167 (dez IDs)

7 completas em conteúdo e 3 com ressalvas: TF-161 (CHA8 impresso como -2), TF-165 (Split causado por slashing ao qual figura imunidade) e TF-166 (Multiattack com nome Slam indefinido enquanto ataque listado é Pseudopod). As 10 imagens estão diretamente vinculadas; 2 com largura inferior a 500 px (TF-158 e TF-167). Identidade artística, licença e fontes impressas/erratas ainda aguardam validação.

**Consolidado:** 150/395; 98 fichas completas, 30 com ressalvas, 21 incompletas e 1 não verificável; 95 imagens diretas, 52 por manifesto e 3 ausentes.


## Lote 016 — TF-168–TF-177 (dez IDs)

9 fichas completas em conteúdo e 1 completa com ressalvas: TF-176 (Lightning Storm: conferir se danos do alvo inicial e da área metálica são cumulativos no mesmo alvo). Dez imagens existem e estão diretamente vinculadas por JSON, com hashes e tamanhos conferidos na árvore Git. Nenhuma tem largura inferior a 500 px. Direitos, adequação visual, edição original e erratas não foram homologados.

**Consolidado:** 160/395 (235 restantes); 107 completas em conteúdo, 31 com ressalvas, 21 incompletas, 1 não verificável; 105 imagens diretas, 52 via manifesto, 3 ausentes.

## Lote 017 — TF-178–TF-190 (10 IDs conforme ordem do CSV)

9 fichas completas em conteúdo e 1 completa com ressalvas: **TF-182**, por interação não resolvida entre Fire Hazard (ativação ao sofrer dano de fogo) e imunidade da criatura a dano de fogo. A ficha de TF-178 não especifica a duração/remoção da petrificação de Acid Spray; o conteúdo disponível foi preservado sem inventar regra. As dez imagens estão vinculadas diretamente aos registros, com presença física, SHA e tamanho conferidos no GitHub. TF-190 possui largura declarada de 469 px, inferior a 500 px. Revisão visual, licença, edição original/erratas e adaptação ao card game permanecem pendentes.

**Consolidado:** 170/395 (225 restantes); 116 completas em conteúdo, 32 com ressalvas, 21 incompletas, 1 não verificável; 115 imagens diretas, 52 por manifesto e 3 ausentes.

## Lote 018 — TF-191–TF-200 (10 IDs do CSV)

5 completas em conteúdo, 4 com ressalvas (TF-194, TF-195, TF-196 por divergências entre fontes/edições; TF-200 por origem Level Up A5E não-SRD e restrições de licença) e 1 incompleta (**TF-199**: condição temporal de Consume Heart truncada, sem extrapolar). 9 imagens diretamente vinculadas com SHA/tamanho correspondentes; TF-200 vinculada via manifesto E, arte gerada por IA não oficial. Imagens declaradas de baixa largura (<500 px): TF-193, TF-194. Não houve homologação editorial, visual ou jurídica.

**Consolidado:** 180/395 (215 restantes); 121 completas, 36 com ressalvas, 22 incompletas, 1 não verificável; 124 imagens diretas, 53 por manifesto e 3 ausentes.

## Lote 019 — TF-201–TF-212 (10 IDs do CSV)

2 fichas completas em conteúdo (TF-211, TF-212), 2 com ressalvas (TF-201 A5E não-SRD/licença e TF-202 Book of Ebon Tides vs Tome of Beasts 3) e 6 incompletas (**TF-203, TF-204, TF-205, TF-206, TF-208, TF-210**: registros C contêm apenas sínteses, não mecânicas nem atributos estruturados). Nove imagens diretamente vinculadas e uma (TF-201) via manifesto E, com SHA/tamanho conferidos; TF-210 tem largura declarada de 452 px. Edição, identidade visual e licenciamento não homologados.

**Consolidado:** 190/395 (205 restantes); 123 completas, 38 com ressalvas, 28 incompletas, 1 não verificável; 133 imagens diretas, 54 por manifesto e 3 ausentes.

## Lote 020 — TF-213–TF-222 (10 IDs da ordem do CSV)

8 fichas completas em conteúdo e 2 com ressalvas: **TF-216**, divergência de vulnerabilidade a frio entre versões; **TF-221**, fórmula de dados de vida possivelmente incompatível com criatura Large. As dez imagens estão diretamente vinculadas ao grupo A, com SHA/tamanho correspondentes. Nenhuma imagem apresenta dimensão declarada inferior a 500 px. Sem homologação visual, editorial, de licença ou adaptação.

**Consolidado:** 200/395 (195 restantes); 131 completas, 40 com ressalvas, 28 incompletas e 1 não verificável; 143 imagens diretas, 54 por manifesto, 3 ausentes.

## Lote 021 — TF-223–TF-233 (10 IDs da ordem do CSV)

9 fichas completas em conteúdo e 1 com ressalva (**TF-231**, descrição Spit Poison de A5E como ataque melee com distância 20/60 ft, pendente cotejo). Dez imagens com vínculo direto aos JSONs A, presentes com SHA e tamanho conferidos. Nenhuma possui dimensão declarada inferior a 500 px. Publicação original, adequação visual e licença permanecem sem homologação.

**Consolidado:** 210/395 (185 restantes); 140 completas, 41 com ressalvas, 28 incompletas, 1 não verificável; 153 imagens diretas, 54 via manifesto, 3 ausentes.
