# SRD Card Game 607 — Grupo A — checkpoint 37 (14/10/2026)

**Estado auditado após importação de imagens e pesquisa adicional:** 132 registros JSON, **33/132** fichas detalhadas no nível do statblock individual online, **0/132** homologadas editorialmente, **131 parciais**, **1 bloqueada (KP-S011)**. Imagens reais no diretório A: **113/132**; faltam **19**, e **0** artes possuem autorização/aprovação final. Totais de imagens verificados por inspeção de SHA de blob Git, não por avaliação visual independente.

**Checkpoints de imagens #33 a #36:** 40 binários (35 da branch D, 5 da branch E) transferidos por referência aos blobs Git pré-existentes; 40 JSONs atualizados com SHA-256 da origem, blob SHA, resolução, caminho e proveniência. A maioria das imagens pequenas continua sendo miniatura não apta à impressão. Foram lidos os 10 JSONs de cada checkpoint e comparados os SHA dos blobs com a árvore Git; cada diff ficou restrito ao diretório A.

**Checkpoint mecânico #37:** fichas TF-221 (Duffel Crab), TF-222 (Crocotta) e TF-224 (Torch Mimic) tiveram estatísticas e mecânicas individuais estruturadas, seguindo as páginas [Duffel Crab](https://kpogl.wikidot.com/monster:duffel-crab), [Crocotta](https://kpogl.wikidot.com/monster:crocotta) e [Torch Mimic](https://kpogl.wikidot.com/monster:torch-mimic). Há uma possível inconsistência impressa de PV no TF-221 (Large, 8d8+24); preservada a fórmula textual, sem correção arbitrária. A wiki não substitui publicação/errata editorial e revisão independente da engine.

**Pendências prioritárias:** comparar fontes originais/erratas, validar 99 fichas ainda sem estrutura integral online, resolver divergências de TF-039, TF-041, TF-047, TF-052 e KP-S011, localizar 19 imagens ausentes, substituir miniaturas e obter análise de direitos/identidade visual.

---

# SRD Card Game 607 — Grupo A — checkpoint 32 (14/10/2026)

**Resultado atualizado:** 132 registros JSON, **30/132** fichas com mecânicas estruturadas segundo blocos individuais online, **0/132 homologadas editorialmente**, **131 parciais**, **1 bloqueada**, **73/132 imagens binárias**, **59 imagens ausentes**, **0 imagens aprovadas para produção**. Esta contagem substitui os resumos anteriores preservados abaixo.

**TF-216 (Anophiloi, Creature Codex p.39):** revisados ataques e anexação, com dados de dano e perda de PV, gatilhos, possibilidade de desprendimento e CDs. Foi eliminada do registro ativo a vulnerabilidade a frio antiga porque a ficha individual consultada em [CCodex](https://github.com/TheGiddyLimit/homebrew/blob/master/creature/Kobold%20Press%3B%20Creature%20Codex.json) não a declara. [Commit](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/fa02d2366a9d8be9c518e45b7a214f027d2dbc18). Não é uma homologação do livro físico ou errata; a confirmação editorial continua pendente.

**Pendências de pesquisa explícitas:** KP-S011 (edições), TF-039 (dados de Bite), TF-041 (Multiattack), TF-047 (4d8 vs 3d8), TF-052 (CD não explicitada) e revisão de outras fichas parciais. Nenhum valor conflitante foi adotado por suposição.

---

# SRD Card Game 607 — continuação no Grupo A — 2026-10-14

## Contagem confirmada após checkpoint 31

| Indicador | Total |
|---|---:|
| IDs e registros JSON do grupo A | **132** |
| Fichas online individualmente estruturadas no nível da fonte | **29** |
| Fichas homologadas integralmente contra edição primária e testes | **0** |
| Fichas parciais | **131** |
| Fichas bloqueadas | **1 (KP-S011)** |
| Binários de imagem fisicamente na branch A | **73** |
| Imagens ausentes | **59** |
| Imagens aprovadas para produção | **0** |

**Checkpoint [`3d5697adc3`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/3d5697adc3e76118b34cef2d314a437e0821debe): TF-058 Animated Instrument e TF-059 Animated Quartet.** Estruturados golpes, músicas, alcance, CDs, escolhas condicionais, recursos (1/dia, recarga 5–6), *Courageous Anthem* com ação bônus para continuação e *Four-Part Harmony*, incluindo sua redução de dados. Fonte individual: [dados comunitários OGL Tome of Beasts 3](https://github.com/TheGiddyLimit/homebrew/blob/master/creature/Kobold%20Press%3B%20Tome%20of%20Beasts%203.json). Ainda aguardam validação editorial/errata e revisão independente de implementação.

Permanecem divergências independentes nas fichas KP-S011, TF-039, TF-041, TF-047 e TF-052. TF-049 usa **Advanced 5E** e não deve ser convertido implicitamente para D&D 5e. O trabalho exige pesquisa continuada para os demais registros e aprovação de artes; os JSONs por si só não representam fichas homologadas.

---

# SRD Card Game 607 — Grupo A: checkpoint adicional de mecânicas completas online (2026-10-14)

## Estado atual — substitui métricas históricas deste relatório

| Métrica | Estado |
|---|---:|
| Escopo exclusivo e arquivos JSON presentes | **132/132** |
| Mecânicas completas com homologação editorial e revisão independente | **0/132** |
| Mecânicas integralmente estruturadas segundo fichas individuais online, sem homologação final | **27/132** |
| Registros parciais | **131** |
| Registros bloqueados | **1 (KP-S011)** |
| Imagens binárias existentes na branch A | **73/132** |
| Imagens ausentes | **59** |
| Imagens aprovadas para produção | **0** |

**A meta de 132 fichas homologadas ainda NÃO está atingida.** O termo "estruturada online" não é equivalente a "MECANICA_COMPLETA_VERIFICADA": falta validar a variante/impressão correta, erratas, resolução de divergências e comportamento da engine. As imagens permanecem em gate editorial/visual/autorizações.

## Pesquisa comprovável nesta retomada: 10 IDs distintos, 3 commits

- [`d0642b33`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/d0642b33e893b5e55d043abcac1bcce3b25d645d): TF-046, TF-047, TF-048, TF-050, TF-051; inseridas ações, conjuração e usos diários, bônus, reação, economia lendária e ataque em área.
- [`5b617abb`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/5b617abbd186c6766d59f17c4af6c237330495f2): TF-052, TF-053, TF-054, TF-057 e correção de TF-048. Dados de ataque, condições, recargas e substituições de Multiattack. TF-057 `Claws` corrigido de resumo incorreto para **1d10+4 perfurante**, conforme ficha OGL.
- [`fde4a598`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/fde4a59820f1b47256a8739d9b6ed5020273c26a): TF-049 (Agonized Khyphon) estruturado por [fonte digital oficial de Advanced 5E](https://www.a5e.tools/node/3400). Mantidos conceitos A5E exclusivos: bloodied 97, Maneuver DC 17, expertise die, disease tier, duas reações por rodada. Alinhamento/tipo corrigidos para TF-046, TF-047, TF-050, TF-051.

## Pendências bloqueadoras identificadas e preservadas

- **TF-047 (Ursan Archon):** `Celestial Weapons` declara dano adicional de força de 4d8 já incluído, mas `Greataxe` registra apenas 3d8. Corrigir apenas com edição/errata comprovadas, sem inferência.
- **TF-052 (Cosmic Symphony):** `Celestial Crescendo` exige salvaguarda de CON, mas o trecho publicado não especifica CD. Mantido **null**, sem presumir CD 18 de outras ações.
- **TF-049:** fonte digital é da **Advanced 5th Edition**, NÃO converter habilidades, perícias ou resistências para 5e genérico.
- Continuam pendentes **KP-S011** (2016 vs 2023), **TF-039** (fórmula Bite incompatível) e **TF-041** (Multiattack condicional ambíguo).

Fontes: [TheGiddyLimit/homebrew](https://github.com/TheGiddyLimit/homebrew/tree/master/creature) (dados OGL transcritos, não homologação do livro), [A5E oficial](https://www.a5e.tools/node/3400), [Kobold Press erratas](https://koboldpress.com/errata/).

**Auditoria:** foram lidos novamente os dez JSONs alterados a partir de commit remoto, conferindo IDs, campos e estrutura; o diff desde o commit anterior à rodada alterou apenas 10 registros sob `operational/research/deep-mechanics/a/`; total da árvore permanece **132 registros e 73 imagens**. Sem merge, sem alteração do ledger ou dos grupos B/C. PR #8 permanece draft.

---

# SRD Card Game 607 — Grupo A: continuação de pesquisa de 15 fichas (14/10/2026)

**PR #8 segue rascunho, sem merge; nenhuma ficha foi aprovada sem confrontação editorial.**

## Estado verificável após os três novos checkpoints

| Indicador | Total |
|---|---:|
| Escopo / JSONs preservados | 132 / 132 |
| Fichas mecanicamente completas e homologadas | **0** |
| Registros parciais | **131** |
| Registros bloqueados | **1** (KP-S011) |
| Statblocks com mecânicas completas no nível das fontes individuais online, ainda sem homologação editorial | **19** |
| Fichas aprofundadas e persistidas nesta rodada | **15** |
| Novas fichas com transcrição integral individual sem divergência detectada nesta rodada | **13** |
| Fichas aprofundadas com conflito explícito | **2** (TF-039, TF-041) |
| Imagens binárias mantidas na branch A | **73** |
| Imagens ausentes | **59** |
| Artes aprovadas para produção | **0** |

### Checkpoints novos

| Commit | IDs | Pesquisa real |
|---|---|---|
| [46292bb7](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/46292bb7e0507008db210cb6598f5752577570ba) | TF-028, TF-029, TF-030, TF-033, TF-034 | Fontes individuais com estatísticas, 15 características e ações, testes, economia de ações e reação |
| [7f765d0b](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/7f765d0b4c419289dd9a29b4ebed803cab071ec3) | TF-035, TF-036, TF-037, TF-038, TF-039 | Mariposas e Pufferfish: cargas, duração, efeitos condicionais, recursos e discrepância de dano |
| [0b0d5989](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/0b0d5989a5c575a4b24195e32658f84c53fa5365) | TF-040, TF-041, TF-042, TF-043, TF-045 | Ataques especiais, reações condicionais, ações lendárias, ações de covil e efeitos regionais |

### Divergências reais preservadas

- **TF-039 Giant Pufferfish:** a reprodução da edição apresenta Bite com média **7** associada a **2d8 + 3**, e Bite inflado de média **12** também com **2d8 + 3**. O dado impresso é internamente incompatível com a média e com a mecânica de dobrar dados em *Puff Up*. Não corrigir silenciosamente para 1d8 + 3 até confirmar errata/autorização editorial. A mecânica está registrada como **não resolvida** e não executável com segurança.
- **TF-041 Giant Water Scorpion:** a frase sobre *Multiattack* usando duas *Claws* e, caso esteja agarrando uma criatura, poder usar *Proboscis* uma vez, não explicita se a probóscide substitui ou acrescenta um ataque. O comportamento na engine depende de conferência editorial; não foi inventado.
- **TF-045 Aaxte/Aatxe:** o ID do catálogo é mantido, mas a transcrição individual e o índice oficial usam **Aatxe**; identidade alternativa registrada. Foram estruturadas as ações lendárias e de covil, além dos efeitos regionais. É necessária revisão independente de todos esses recursos.

**Fonte principal desta rodada:** fichas individuais de [KPOGL](https://kpogl.wikidot.com/) e [5eSRD](https://www.5esrd.com/); ambas são reproduções de conteúdo OGL, não homologação do exemplar físico e de erratas da Kobold Press. Os URLs de cada criatura estão em `records/<ID>.json`.

**Pendências:** validar edição e erratas oficiais, resolver ambiguidade dos casos sinalizados, revisar implementação na engine, obter as 59 imagens restantes e aprovar direitos/qualidade das 73 imagens atuais. A meta original permanece não concluída.

---

# SRD Card Game 607 — Grupo A — auditoria atualizada (2026-10-14)

**Branch:** `chatgpt/srd607-deep-mechanics-a`  
**PR:** [#8](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/pull/8) — rascunho, sem merge.  
**SHA auditado:** [`ade2f6873bc549ea1c5adcdc1db1567dd0f01b7e`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/ade2f6873bc549ea1c5adcdc1db1567dd0f01b7e).  
**Fonte de escopo:** 40 + 40 + 52 IDs (132 únicos).

## Situação efetiva (esta atualização prevalece sobre os números históricos abaixo)

| Métrica | Quantidade |
|---|---:|
| IDs exclusivos / JSONs presentes na árvore | 132 / 132 |
| Fichas com homologação mecânica editorial integral | **0** |
| Fichas parciais | **131** |
| Fichas bloqueadas | **1** (KP-S011) |
| Fichas estruturadas integralmente a partir de fontes individuais online, ainda sem homologação editorial | **6** |
| Imagens binárias fisicamente presentes na branch A | **73** |
| Imagens binárias ausentes | **59** |
| Imagens tecnicamente reaproveitadas de E/F nesta retomada | **71** (53 E + 18 F) |
| Imagens aprovadas visualmente, juridicamente e para produção | **0** |

**A meta de 132 fichas completas com 132 imagens validadas NÃO foi atingida.** Os 73 binários existem e seus blobs foram auditados, mas dois são miniaturas inadequadas; 71 reaproveitados exigem inspeção visual individual e análise dos direitos de uso. Nenhum desses status deve ser interpretado como arte editorial de produção aprovada.

### Pesquisa mecânica adicional

- **TF-027 — Chroma Lizard:** reconstituídas as características *Mirror Scales*, *Mirror Shy* e *Radiant Reflection*, além de *Dazzling Display*, *Multiattack*, *Bite*, *Claw*, CDs, alcance, dados e condições, com fontes por criatura. Mudança de **BLOQUEADA** para **PARCIAL**, pois falta comparação editorial primária e revisão da engine.
- **KP-S011 — Abominable Beauty:** estatísticas, ataques, testes e recursos detalhados conforme transcrição 5eSRD; incorporada a errata oficial da Kobold Press de 29/05/2025 que corrige o tipo de dano do *Slam* na revisão de 2023. **Mantida BLOQUEADA:** a transcrição contém *Undead Nature* referente a *accursed defiler*, outro monstro; sem prova da edição primária não é válido incluí-la.
- **TF-024, TF-025, TF-026, TF-031, TF-032:** incluídos XP da fonte, modificadores dos seis atributos e valores médios de ataques, conforme as fichas consultadas. Permanecem parciais aguardando a impressão/errata e revisão independente.
- Para as demais fichas, os JSONs existentes mantêm lacunas de parâmetros mecânicos e não foram homologados.

### Checkpoints novos, exclusivos do diretório A

| Checkpoint | IDs exatos | Total | Commit |
|---:|---|---:|---|
| 15 | TF-027, KP-S011 | 2 | [a6d619df34](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/a6d619df349da1c890ca54435fcbf2083131b003) |
| 16 | TF-211, TF-212, TF-213, TF-214, TF-215, TF-216, TF-217, TF-218, TF-219, TF-220 | 10 | [85a659169d](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/85a659169d8f9898d3537f838b1c79c27b01b5de) |
| 17 | TF-059, TF-221, TF-222, TF-223, TF-224, TF-225, TF-227, TF-228, TF-229, TF-230 | 10 | [3852e0f202](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/3852e0f202a3f9c3cc7f9203d279a7f9b2ca6be3) |
| 18 | TF-232, TF-233, TF-234, TF-235, TF-236, TF-237, TF-238, TF-240, TF-241, TF-242 | 10 | [d261bcac91](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/d261bcac917f8d5ea059d5c95ed7356391e7eeeb) |
| 19 | TF-243, TF-244, TF-245, TF-246, TF-247, TF-248, TF-249, TF-250, TF-251, TF-252 | 10 | [351f7dd7de](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/351f7dd7deb149f319e948b0997a6067b790c7bd) |
| 20 | TF-253, TF-254, TF-256, TF-257, TF-258, TF-259, TF-260, TF-261, TF-263, TF-265 | 10 | [9ce19dda2c](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/9ce19dda2c6e1b1a7faf8b101fc63ed7439e913c) |
| 21 | TF-266, TF-268, TF-269 | 3 | [56d6dd8c74](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/56d6dd8c74126ce14dcc75ace459eced0ca9f99b) |
| 22 | TF-270, TF-272, TF-273, TF-277, TF-278, TF-279, TF-280, TF-288, TF-289, TF-290 | 10 | [234df4c125](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/234df4c1250576acecb7682b1688c82380536a6b) |
| 23 | TF-292, TF-293, TF-296, TF-297, TF-298, TF-299, TF-300, TF-301 | 8 | [210bb5f5b7](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/210bb5f5b7ebedac747d69809439ce03ceed2b72) |
| 24 | TF-024, TF-025, TF-026, TF-031, TF-032 | 5 | [ade2f6873b](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/ade2f6873bc549ea1c5adcdc1db1567dd0f01b7e) |

### Evidências e pendências

- Registros em [records/](records/), imagens em [images/](images/) e índice de SHA-256, dimensões, origens e commits por imagem em [manifest.json](manifest.json), seção `image_assets`.
- As imagens transferidas vieram de `chatgpt/srd607-image-assets-e` e `chatgpt/srd607-image-assets-f` por **reuso do mesmo Git blob SHA** sem alterar essas branches. Os registros de origem têm hashes SHA-256 e dimensões.
- Auditoria da árvore do GitHub constatou **132 JSONs + 73 binários**, com os 71 blobs transferidos idênticos (SHA + tamanho) aos das branches de origem. Os 132 JSONs haviam sido parseados anteriormente; a rodada atual confirmou a árvore completa e validou pontos alterados, não constituiu nova releitura semântica independente de todos os JSONs.
- Ainda precisam de pesquisa editorial integral até 132 fichas, verificação de discrepâncias de impressão, implementabilidade das regras, direitos e avaliação visual das artes e aquisição/produção de **59** arquivos de imagens faltantes, além de substituição das duas miniaturas.

### Divergência editorial adicional — KP-S011: original vs revisão

A investigação encontrou **variantes mecanicamente incompatíveis** de Abominable Beauty. A edição original (2016) descreve Multiattack como dois Slam, Blinding Gaze de recarga 5–6 com CD 17 e dano de fogo 8d6, enquanto a revisão de 2023 inclui Blinding Gaze no Multiattack, CD 16, duração e salvaguardas repetidas, Slam com 6d6 fire, além de Deafening Voice com alcance e duração distintos. A errata oficial de 2025 acrescenta o tipo *bludgeoning* ao Slam **da revisão de 2023**. Os números salvos em `records/KP-S011.json` são **candidatos 2023, não uma resolução do registro histórico**. Bloqueio permanece até escolher a edição-alvo com suporte editorial. Evidências: [transcrição 2023](https://www.5esrd.com/database/creature/abominable-beauty/), [reprodução original 2016](https://anyflip.com/dhfzu/lcug/basic/) e [errata oficial](https://koboldpress.com/errata/).

---

## Histórico anterior (reproduzido para rastreabilidade; as contagens a seguir são antigas)

# SRD Card Game 607 — Pesquisa mecânica integral A: relatório real

**Data:** 2026-10-13  
**Branch exclusiva:** `chatgpt/srd607-deep-mechanics-a`  
**Commit-base:** [`a962c48a1169c2ef2be8137715a095a596753b32`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/a962c48a1169c2ef2be8137715a095a596753b32)  
**Base da PR:** `chatgpt/srd607-research-checkpoints-20261011`  
**Manifesto:** [manifest.json](manifest.json)  
**Registros:** [records/](records/)

## Estado da entrega

**A pesquisa mecânica integral das 132 criaturas NÃO está concluída.** Foram criados e conferidos 132 registros de evidências, mas isso não equivale a 132 fichas implementáveis. Somente dez fichas tiveram leitura e estruturação detalhada de transcrições individuais nesta rodada; essas dez seguem parciais porque a edição/errata editorial exata não foi confirmada.

| Métrica | Quantidade |
|---|---:|
| IDs de escopo, exclusivos | 132 |
| JSONs publicados e lidos de volta | 132 |
| JSONs inválidos e divergências nome/ID | 0 |
| Mecânicas completas e editorialmente confirmadas | **0** |
| Fichas parciais | **130** |
| Fichas bloqueadas | **2** |
| Fichas aprofundadas em transcrição individual (ainda parciais) | 10 |
| Restantes com mecânicas individuais ainda a aprofundar | 122 |

## Seleção reprodutível

1. `next_batches[0].ids`: 40 IDs exatos, sem preencher lacunas.
2. `next_batches[1].ids`: 40 IDs exatos, sem preencher lacunas.
3. `historical.slice(0,52)`: linhas do CSV na ordem original com `Mecanica_completa == "NAO"` e `Estado != "PENDENTE_PESQUISA"`; começa em `KP-S011` e termina em `TF-059`.

Ledger: [campaign.json](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/a962c48a1169c2ef2be8137715a095a596753b32/operational/research/catalog-ledger-20261011-v27/campaign.json). CSV: [catalog-status.csv](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/a962c48a1169c2ef2be8137715a095a596753b32/operational/research/catalog-ledger-20261011-v27/catalog-status.csv). Pesquisa anterior: [PR #2](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/pull/2), não tratada como completa.

## Aprofundamento mecânico efetivo — 10 fichas

IDs: `TF-211`, `TF-212`, `TF-213`, `TF-214`, `TF-215`, `TF-216`, `TF-217`, `TF-218`, `TF-219`, `TF-220`.

Para essas dez criaturas foram registradas individualmente as ações, ataques, bônus de acerto, dados e tipos de dano, CDs, condições, recargas e efeitos aplicáveis conforme fichas da KPOGL, além de suas estatísticas e fontes. Foram consultadas individualmente páginas como [Ahuizotl](https://kpogl.wikidot.com/monster:ahuizotl), [Alabroza](https://kpogl.wikidot.com/monster:alabroza), [Alchemical Skunk](https://kpogl.wikidot.com/monster:alchemical-skunk), [Aniwye](https://kpogl.wikidot.com/monster:aniwye) e [Corpse Worm](https://kpogl.wikidot.com/monster:corpse-worm). A KPOGL é uma transcrição secundária, não um atestado de identidade de impressão/errata. Por isso, as dez continuam `PARCIAL`.

## Bloqueios individualizados

- **KP-S011 — Abominable Beauty:** a fonte histórica apresenta referência inconsistente a um traço de outra criatura, com CA, PV e atributos ausentes no checkpoint. Não inferir valores nem promover antes da reconciliação.
- **TF-027 — Chroma Lizard:** apenas índice editorial e referências secundárias de reprodução no checkpoint anterior; falta ficha individual suficientemente confiável para confirmar integralmente ataques e Dazzling Display.

## Checkpoints efetivamente publicados

| Nº | IDs incluídos | Total | Commit persistido |
|---:|---|---:|---|
| 1 | `TF-211` → `TF-220` (IDs explícitos, não intervalo contínuo) | 10 | [`5589d720b02a`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/5589d720b02a096804a7f180bd36ca9a1f6df861) |
| 2 | `TF-221` → `TF-231` (IDs explícitos, não intervalo contínuo) | 10 | [`aa325e655033`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/aa325e6550337c2cd5c346eddc6e8a7d896ee585) |
| 3 | `TF-232` → `TF-241` (IDs explícitos, não intervalo contínuo) | 10 | [`ffe45411e8ad`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/ffe45411e8ad0faae14294bdac492ba31d73e884) |
| 4 | `TF-242` → `TF-251` (IDs explícitos, não intervalo contínuo) | 10 | [`7570a1d2c9de`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/7570a1d2c9de8f7adbf316ec5d715567c28bcb5d) |
| 5 | `TF-252` → `TF-261` (IDs explícitos, não intervalo contínuo) | 10 | [`99f1aa1ca6eb`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/99f1aa1ca6eb67f5987a05694d139948edca7378) |
| 6 | `TF-263` → `TF-273` (IDs explícitos, não intervalo contínuo) | 10 | [`b9e9269497d0`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/b9e9269497d0ea6f6142d0467f9695aac9b8ff91) |
| 7 | `TF-274` → `TF-288` (IDs explícitos, não intervalo contínuo) | 10 | [`c4422f15159d`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/c4422f15159d5236111cb73db824efd7b30d764f) |
| 8 | `TF-289` → `TF-301` (IDs explícitos, não intervalo contínuo) | 10 | [`84e538df0374`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/84e538df03749b7adf5c3c80c0a263a845403247) |
| 9 | `KP-S011` → `TF-011` (IDs explícitos, não intervalo contínuo) | 10 | [`fa6f6afd8bd3`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/fa6f6afd8bd369ec2b4f64cd844e8f58eccf7b66) |
| 10 | `TF-012` → `TF-024` (IDs explícitos, não intervalo contínuo) | 10 | [`2b62cdcac3a7`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/2b62cdcac3a73ddccb051226295b7f14ddeae1b4) |
| 11 | `TF-025` → `TF-034` (IDs explícitos, não intervalo contínuo) | 10 | [`0e54839a817e`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/0e54839a817e3c04e91a201d5783058b3ce5d646) |
| 12 | `TF-035` → `TF-045` (IDs explícitos, não intervalo contínuo) | 10 | [`66c274c11b62`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/66c274c11b62f16ffa1c73a7395fe8a61c6d0233) |
| 13 | `TF-046` → `TF-057` (IDs explícitos, não intervalo contínuo) | 10 | [`9d0257a06c21`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/9d0257a06c21d88c9cb3ca59333f16a69a511211) |
| 14 | `TF-058` → `TF-059` (IDs explícitos, não intervalo contínuo) | 2 | [`68d53861a4bf`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/68d53861a4bff6fd3dddd0af9f549deac796dccd) |

Correção de fonte aninhada nos históricos TF-026 a TF-030: [`6634f8ae018b15686b62b141cd5e4fa401c54fbb`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/6634f8ae018b15686b62b141cd5e4fa401c54fbb). Nenhum checkpoint tem mais de 10 registros novos.

## Pendências sem preenchimento artificial

- Nos 122 registros que ainda não tiveram leitura mecânica integral nesta rodada, resumos e nomes de habilidades dos checkpoints são **índices de pesquisa**, não regras prontas para execução. Todas as ações ausentes, CDs, bônus, dados, gatilhos e condições permanecem explicitamente pendentes.
- Confrontar ficha individual, edição exata, errata e eventuais variantes antes de aprovar os dados dos 132 monstros. Não misturar 5e/A5E nem revisões de Kobold Press.
- Concluir o detalhamento de ataques, multiataques, ações especiais, ações bônus, reações, ações lendárias, conjurações, CDs, duração, recursos e limites para todos os registros ainda parciais.
- Fazer verificação independente de integralidade mecânica. Nenhuma promoção canônica ou alteração do ledger/CSV global foi feita.

## Validação e isolamento

Foram lidos remotamente os 132 arquivos JSON publicados no commit [`68d53861a4bff6fd3dddd0af9f549deac796dccd`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/68d53861a4bff6fd3dddd0af9f549deac796dccd), todos com JSON válido, schema esperado, ID idêntico ao nome do arquivo e pendências declaradas. O conjunto de nomes foi confrontado com os IDs explícitos do ledger e com o filtro original do CSV, sem faltantes, duplicatas ou extras.

Arquivos alterados exclusivamente sob `operational/research/deep-mechanics/a/`. Não foram editados `campaign.json`, `catalog-status.csv`, `STATUS`, `main`, branch de referência, PR #1 ou PR #2; não houve merge.

**Conclusão:** publicação do catálogo de investigação, não conclusão da pesquisa integral. **Fichas efetivamente completas: 0/132**.

## Atualização — TF-026 (Bilby): fonte dupla + imagem binária

- [Ficha TF-026](records/TF-026.json) revisada contra duas páginas individuais: [5eSRD](https://www.5esrd.com/database/creature/bilby/) e [KPOGL](https://kpogl.wikidot.com/monster:bilby). O [índice da Kobold Press](https://koboldpress.com/tools/kobold-press-monsters/) confirma a identidade/ND e a [página editorial de 2020](https://koboldpress.com/tome-of-beasts-2/) confirma a edição 5e.
- Estruturados integralmente todos os elementos do statblock disponível: CA 10, PV 2 (1d4), seis atributos, deslocamentos, darkvision, percepção passiva, Shadow Camouflage, Bite com +2, 5 pés, 1 perfurante, ação normal, sem ações bônus, reações, lendárias ou magias no statblock.
- [Arquivo JPEG real](images/TF-026_bilby.jpg) de 4.241 bytes e 160×160 pixels, com SHA-256 `649da02715e1931192dd16d9cb86add1560c19607d07e730fe4a870a50ebb36b`. Arte gerada nesta execução, não oficial da editora. **É uma miniatura, não uma imagem aprovada para impressão.**
- Sem acesso à página da edição física/errata, a ficha permanece `PARCIAL`, embora sua mecânica publicada nas duas fontes individuais tenha sido inteiramente estruturada. O total editorialmente validado permanece **0/132**, com **130 parciais / 2 bloqueadas** e **1/132 imagem binária real persistida**.

## Atualização complementar — TF-024 e TF-025

- [TF-024 Lantern Beetle](records/TF-024.json): reconstrução da ficha KPOGL [individual](https://kpogl.wikidot.com/monster:lantern-beetle): Tiny Beast, ND0, CA13, PV2 (1d4), atributos completos; voo/escalada; `Illumination` com luz intensa a 10 pés, penumbra por 10 pés adicionais e persistência durante seis horas após a morte; `Horn` (+3, 5 pés, um alvo, 1 perfurante). O 5eSRD esteve inacessível por desafio JavaScript nesta verificação. Original impresso/errata e **imagem ainda pendentes**.
- [TF-025 Sniffer Beetle](records/TF-025.json): duas [fichas](https://www.5esrd.com/database/creature/beetle-sniffer/) [individuais](https://kpogl.wikidot.com/monster:sniffer-beetle) concordantes: Small Beast, ND 1/8, CA 12, PV 5 (1d6+2), seis atributos, movimento, voo, Perception+5, darkvision, `Keen Smell`, `Bite` (+3, 1d4+1 perfurante) e elegibilidade de familiar fora do statblock. Original impresso/errata e **imagem ainda pendentes**.
- **Agora são 3/132 statblocks inteiramente estruturados no nível da ficha individual, 0/132 validados editorialmente e 1/132 imagens binárias persistidas.** Os outros 129 continuam com mecânicas por detalhar. Nenhuma imagem externa foi marcada como salva apenas por sua URL.


## Continuação de 2026-10-14 — TF-031 e TF-032

- **TF-031 — Razorback Crab**: [JSON estruturado](records/TF-031.json), [ficha 5eSRD](https://www.5esrd.com/database/creature/crab-razorback/) e [índice oficial da editora](https://koboldpress.com/tools/kobold-press-monsters/). ND 2, CA 17, PV 58 (9d8+18), todos os atributos, velocidades e sentidos; *Bladed Shell*, *Pounce*, *Multiattack*, *Claw* e *Shell Bash* com gatilhos, CA, salvaguarda FOR CD 13, dados e bônus. Arte JPEG binária de prova [gravada](images/TF-031_razorback_crab_proof.jpg) (80×120); a arte de produção em alta resolução continua pendente.
- **TF-032 — Daeodon**: [JSON estruturado](records/TF-032.json), [5eSRD](https://www.5esrd.com/database/creature/daeodon/) e [KPOGL](https://kpogl.wikidot.com/monster:daeodon) concordantes. ND 3, CA 13, PV 76 (9d10+27); *Keen Smell*, *Relentless*, *Trampling Charge*, *Multiattack*, *Bite*, *Slam* e *Fierce Call* com bônus, recursos, alcance, CDs, condições e consequências. Imagem própria ainda pendente.
- Total agora: **5/132 fichas mecanicamente estruturadas no nível da fonte online**, mas **0/132 validadas editorialmente**; **130 parciais, 2 bloqueadas**, **2 imagens binárias no GitHub, ambas miniaturas não aprovadas para produção**. Nem URLs nem imagens locais são contabilizadas como binários publicados.
- A versão impressa e as erratas da edição exata ainda devem ser conferidas; não houve alteração no ledger, CSV global ou merge.
