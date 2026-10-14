# SRD Card Game 607 — auditoria cruzada dos cinco lotes (200 IDs)

**Data operacional:** 13/10/2026 (horário de Brasília).  
**Tipo:** fotografia documental de pesquisa / pré-reconciliação, sem integração ao catálogo.  
**Matriz auditável por ID:** [RECONCILIATION_AUDIT_200.json](RECONCILIATION_AUDIT_200.json).  
**Referência imutável:** `a962c48a1169c2ef2be8137715a095a596753b32`.  
**Ponto de corte:** PR #2 em `2de3746ca04b91bcbc82db7db1e008d6bde7bda2`; PR #4 em `bbc3f13e46bd15d539c1375eb251ff51d1d05d01`; PR #3 em `aedf87ef9c474785420e5c4643ce2ee1418438cd`. Alterações posteriores precisam de nova auditoria.  
**Conjunto auditado:** 5 checkpoints x 40 IDs, exclusivamente conforme `next_batches[0..4]` do ledger no commit de referência.

## 1. Resultado documentado

| Indicador | Total | Interpretação |
|---|---:|---|
| IDs dos cinco lotes com checkpoint publicado | **200/200** | Presença no repositório comprovada |
| IDs únicos, sem repetição ou colisão entre lotes | **200/200** | Ordem e identidade iguais às filas do ledger |
| Registros com resumo de ações | **199** | `TF-260` não teve ficha individual compatível confirmada |
| Registros com CA + PV + seis atributos presentes | **195** | Presença do campo não representa validação editorial |
| Registros com ao menos uma lacuna básica | **5** | IDs listados na seção 3 |
| Registros com conflito editorial/fonte bloqueante | **14** | 13 casos na PR #4 e TF-260 na PR #2 |
| Registros com ND nulo | **2** | TF-408 incongruente; TF-431 invocação de ND variável |
| Fichas individuais referenciadas do portal editorial A5E | **42** | Não significa licença aberta ou revisão independente |
| Verificação suplementar individual na PR #4 | **21/80** | 59 não rechecados nesse suplemento |
| Revisões mecânicas independentes concluídas | **0/200 nesta auditoria** | Gates de origem, licença e regras permanecem abertos |
| Novas fichas promovidas, merges ou ledger atualizado | **0** | Preservação de escopo |

As classificações exclusivas são: **184** com resumo e revisão pendente, **14** com conflito bloqueante, **1** com atributos ausentes e **1** com ND variável. **Todas** continuam pendentes de revisão editorial, jurídica e canônica.

## 2. Checkpoints e congelamento dos commits

| Lote | PR | IDs | Resumo de ações | Arquivo publicado |
|---|---|---:|---:|---|
| 1 | PR #2 | 40 | 40 | [checkpoint](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/2de3746ca04b91bcbc82db7db1e008d6bde7bda2/operational/research/checkpoints/20261013_parallel-a_TF-211_TF-251/research.json) |
| 2 | PR #2 | 40 | 39 | [checkpoint](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/2de3746ca04b91bcbc82db7db1e008d6bde7bda2/operational/research/checkpoints/20261013_parallel-a_TF-252_TF-301/research.json) |
| 3 | PR #4 | 40 | 40 | [checkpoint](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/bbc3f13e46bd15d539c1375eb251ff51d1d05d01/operational/research/checkpoints/20261013_TF-302_TF-355/research.json) |
| 4 | PR #4 | 40 | 40 | [checkpoint](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/bbc3f13e46bd15d539c1375eb251ff51d1d05d01/operational/research/checkpoints/20261013_TF-356_TF-411/research.json) |
| 5 | PR #3 | 40 | 40 | [checkpoint](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/aedf87ef9c474785420e5c4643ce2ee1418438cd/operational/research/checkpoints/20261013_parallel-c_TF-412_TF-522/research.json) |

- PR #2: [pesquisa A](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/pull/2). Houve revisão concorrente durante esta auditoria; antes, 64 registros só possuíam identificação/ND. No commit congelado agora são 79 resumos e o bloqueio TF-260.
- PR #4: [pesquisa B](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/pull/4), incluindo [suplemento de validação de 21 fontes](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/bbc3f13e46bd15d539c1375eb251ff51d1d05d01/operational/research/checkpoints/20261013_parallel_b_source_validation/source-validation.json).
- PR #3: [pesquisa C e auditoria](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/pull/3). Na revisão editorial C, confirmou-se TF-415 Gloomflower em **Creature Codex** e TF-416 Wind Witch em **Tome of Beasts 3**, pelo [índice oficial Kobold Press](https://koboldpress.com/tools/kobold-press-monsters/).

Todos os checkpoints foram analisados em **commits fixos**, não em nomes de branches mutáveis.

## 3. Lacunas técnicas e bloqueios identificados

### 3.1. Bloqueios de fonte, homônimo ou edição (14 IDs)

- **TF-260 — Vine Lord**, lote 2, PR #2: `BLOQUEIO_EDICAO_DIVERGENTE_SEM_ESTATISTICAS_CONFIAVEIS`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-309 — Living Wick**, lote 3, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-318 — Fellforged**, lote 3, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-319 — Gearforged Templar**, lote 3, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-320 — Gnarljak**, lote 3, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-325 — Lindwurm**, lote 3, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-334 — Far Darrig**, lote 3, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-356 — Grendel**, lote 4, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-361 — Elder Black Pudding**, lote 4, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-382 — Likho**, lote 4, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-386 — Grootslang**, lote 4, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-388 — Son of Fenris**, lote 4, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-401 — Mallqui**, lote 4, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.
- **TF-408 — Grove Swarm**, lote 4, PR #4: `PARCIAL_CONFLITO_EDICAO`. Não harmonizar CA/PV/ND/ações entre edições sem determinar a identidade editorial correta.

Prioridade especial: **TF-260** (Vine Lord, ND9 em índice Kobold Press versus ND7 em transcrição secundária), **TF-320** (Gnarljak com PV divergentes), **TF-382** (Likho ND5 no índice versus ND6 em transcrição), e **TF-408** (Grove Swarm, ND0 na ferramenta editorial mas PV217/CA16, incongruência registrada).

### 3.2. Registros com campos básicos ausentes (5)

| ID | Criatura | Falhas observadas | Tratamento |
|---|---|---|---|
| TF-260 | Vine Lord | CA_AUSENTE, PV_AUSENTE, ATRIBUTOS_AUSENTES | Resolver bloqueio editorial antes de completar. |
| TF-304 | Living Star | ATRIBUTOS_AUSENTES | Pesquisar valores contra edição correta. |
| TF-309 | Living Wick | ATRIBUTOS_AUSENTES | Resolver bloqueio editorial antes de completar. |
| TF-320 | Gnarljak | PV_AUSENTE, ATRIBUTOS_AUSENTES | Resolver bloqueio editorial antes de completar. |
| TF-382 | Likho | CA_AUSENTE, PV_AUSENTE, ATRIBUTOS_AUSENTES | Resolver bloqueio editorial antes de completar. |

### 3.3. ND especial ou pendente

- **TF-408 — Grove Swarm:** O catálogo da ferramenta A5E exibe ND 0, mas o bloco tem CA 16 e PV 217; a reconciliação do ND foi bloqueada até esclarecimento editorial.
- **TF-431 — Conjured Guardian:** Challenge — na ficha do Conjured Guardian; valores e proficiência dependem da magia/conjurador, não criar ND 0.

### 3.4. Divergências adicionais não bloqueadas formalmente

- **TF-414 Wallflower:** texto de ação menciona "grick"; provável termo editorial residual.
- **TF-468 Faerie Chimera:** descrição do sopro cita fogo ao lado de efeito de frio; preservar a incoerência para revisão.
- **TF-470 Fiendish Chimera:** nomenclatura de ataques nas ações lendárias requer conferência.
- **TF-500 Gorger Zombie Horde:** campo de publicação e índice de origem divergem.
- **TF-373 Kobold Wizard:** suplemento da PR #4 alerta para homônimo ND1 versus versão do índice Kobold Press ND5.

Os itens desta seção **não estão automaticamente resolvidos** pelo fato de haver CA, PV ou um texto resumido. Revisar também habilidades passivas, perícias, deslocamentos, CDs, alcance, resistências, imunidades, recargas, conjurações, reações e ações lendárias em todos os lotes.

## 4. Integridade do CSV e ledger de referência

- CSV `operational/research/catalog-ledger-20261011-v27/catalog-status.csv`, blob SHA `9b703f40bb33b778992d0ba06a20704b19b3c9eb`.
- **607 linhas de dados e 607 IDs únicos**, separador `;`, cabeçalho com 6 colunas: `ID;Criatura;Mecanica_completa;Checkpoint;Estado;Imagem`; todas as linhas testadas com 6 campos.
- Os 200 IDs dos lotes são 200 linhas distintas no CSV, todos `NAO` em `Mecanica_completa` e `PENDENTE_PESQUISA` no commit-base. Sem alteração do CSV nesta operação.
- Ledger `campaign.json`, blob SHA `cafc7c0c36e896bd7c7449a38415ca2f88f82ab2`. Mantêm-se, **sem mudança**: catálogo 607; canônicas completas 212; incompletas 395; pesquisas reconciliadas 195; ainda pendentes no ledger 200; imagens verificadas 23.
- Os 200 **checkpoints publicados** não são automaticamente 200 **pesquisas aprovadas**. O teto teórico de 395 pesquisas documentadas (195 anteriores + até 200 novas) dependerá de critério formal de aceite e reconciliação, sem converter fichas pesquisadas em canônicas completas.

## 5. Fontes, escopo da verificação e limites

- Material Kobold Press: índice editorial [Kobold Press Monsters](https://koboldpress.com/tools/kobold-press-monsters/) fundamenta identidade/publicação/ND, **não** todos os efeitos e atributos. Muitas mecânicas provêm de 5eSRD e outras reproduções de terceiros.
- Material EN Publishing: páginas individuais de [A5E Tools](https://a5e.tools/monsters) fornecem estatísticas diretas do publicador em vários registros. O próprio portal explicita que **não equivale ao A5E SRD** nem comprova permissão de republicação de regras ou imagens.
- O suplemento B rechecado no GitHub tem **21 IDs** e informa **59 sem checagem adicional**. A auditoria cruzada conferiu **presença, formato e domínio de URLs** para cada registro, mas **não atestou acesso e exatidão integral das 200 fontes externas**. Houve checagens públicas pontuais do índice Kobold Press e das páginas A5E TF-431/TF-448/TF-470, além da ficha 5eSRD TF-412.
- Verificações técnicas formais de licença, copyright, reprodutibilidade integral, teste do construtor de cartas, revisão visual e teste DOCX/PDF: **não executadas**.

## 6. Plano de reconciliação e autorização

1. **Resolver bloqueios:** fonte/edição de 14 casos, dados incompletos de 5 casos e ND especial dos dois registros. Cada alteração deve ser feita pelo responsável da branch original (A, B ou C) ou por correção controlada autorizada, sempre com vínculo ao ID.
2. **Completar e validar mecânicas:** fichas completas, habilidades e ações na edição correta; conferir diferenças A5E/D&D5e, licenças, fontes e direitos. Independente de o registro já conter resumos.
3. **Revisão cruzada independente:** revisar cada diff e checkpoint na versão mais recente; garantir nenhum ID duplicado ou fora do ledger, nenhum arquivo global alterado por concorrência, aprovação externa ao autor e gates de regras/licença/qualidade.
4. **Recontar e preparar patch global proposto:** estabelecer definição de `research_stage_count` e estados de CSV; simular atualização controlada sem aplicar, comparar o antes/depois e documentar os aceitos/pendentes/bloqueados.
5. **Só depois de autorização explícita e preflight de concorrência:** executar a integração pelo canal protegido, atualizar ledger global e PR #1 conforme governança, com revisão humana/independente, sem autoaprovação e sem merge desprotegido.

**Estado da auditoria:** documentação adicional somente na PR #3 (`parallel-c`); **nenhum** ledger/CSV/STATUS global, branch `main` ou PR #1 foi alterado por esta execução. Os trabalhos A e B permanecem sob suas próprias branches.

## 7. Inventário por ID — snapshot de 200 registros

A tabela abaixo é a classificação de **pesquisa documentada**, não de ficha canônica. ND, CA e PV refletem o checkpoint, sem normalização de edições. A matriz JSON tem URL(s), sinalizadores detalhados, checkpoint e situação de revisão para cada ID.

### Lote 1 — PR #2

| ID | Criatura | Situação | ND fonte | CA | PV | Alertas |
|---|---|---|---:|---:|---:|---|
| TF-211 | Ahuizotl | REVISÃO PENDENTE | 2 | 14 | 71 | — |
| TF-212 | Alabroza | REVISÃO PENDENTE | 1 | 12 | 45 | — |
| TF-213 | Alchemical Skunk | REVISÃO PENDENTE | 4 | 15 | 66 | — |
| TF-214 | Alke | REVISÃO PENDENTE | 5 | 14 | 114 | — |
| TF-215 | Aniwye | REVISÃO PENDENTE | 5 | 15 | 102 | — |
| TF-216 | Anophiloi | REVISÃO PENDENTE | 1 | 12 | 33 | — |
| TF-217 | Bearmit Crab | REVISÃO PENDENTE | 2 | 14 | 59 | — |
| TF-218 | Chupacabra | REVISÃO PENDENTE | 0.5 | 13 | 36 | — |
| TF-219 | Cobbleswarm | REVISÃO PENDENTE | 2 | 15 | 36 | — |
| TF-220 | Corpse Worm | REVISÃO PENDENTE | 3 | 14 | 76 | — |
| TF-221 | Crab, Duffel | REVISÃO PENDENTE | 3 | 15 | 60 | — |
| TF-222 | Crocotta | REVISÃO PENDENTE | 3 | 14 | 39 | — |
| TF-223 | Three-Headed Cobra | REVISÃO PENDENTE | 5 | 16 | 127 | — |
| TF-224 | Torch Mimic | REVISÃO PENDENTE | 0.5 | 12 | 21 | — |
| TF-225 | Aalpamac | REVISÃO PENDENTE | 7 | 16 | 136 | — |
| TF-227 | Coastline Reaper | REVISÃO PENDENTE | 9 | 16 | 144 | — |
| TF-228 | Colláis | REVISÃO PENDENTE | 10 | 16 | 150 | — |
| TF-229 | Conjoined Queen | REVISÃO PENDENTE | 10 | 18 | 168 | — |
| TF-230 | Cryoceros | REVISÃO PENDENTE | 6 | 15 | 133 | — |
| TF-231 | Accursed Guardian Naga | REVISÃO PENDENTE | 12 | 18 | 136 | — |
| TF-232 | Annelidast | REVISÃO PENDENTE | 12 | 18 | 184 | — |
| TF-233 | Chaos Raptor | REVISÃO PENDENTE | 13 | 18 | 248 | — |
| TF-234 | Chimera, Royal | REVISÃO PENDENTE | 15 | 17 | 189 | — |
| TF-235 | Tigebra | REVISÃO PENDENTE | 13 | 18 | 190 | — |
| TF-236 | Timingila | REVISÃO PENDENTE | 15 | 18 | 232 | — |
| TF-237 | Tosculi, Hive Queen | REVISÃO PENDENTE | 12 | 17 | 189 | — |
| TF-238 | Zaratan | REVISÃO PENDENTE | 26 | 25 | 507 | — |
| TF-239 | Aboleth, Nihileth, Nihilethic Dominator | REVISÃO PENDENTE | 5 | 13 | 82 | — |
| TF-240 | Aboleth, Nihileth, Nihilethic Zombie | REVISÃO PENDENTE | 1 | 8 | 37 | — |
| TF-241 | Accursed Defiler | REVISÃO PENDENTE | 4 | 12 | 75 | — |
| TF-242 | Ashwalker | REVISÃO PENDENTE | 1 | 12 | 31 | — |
| TF-243 | Chill Haunt | REVISÃO PENDENTE | 3 | 13 | 39 | — |
| TF-244 | Chimeric Phantom | REVISÃO PENDENTE | 2 | 11 | 36 | — |
| TF-245 | Old Salt | REVISÃO PENDENTE | 5 | 15 | 117 | — |
| TF-246 | Yowler | REVISÃO PENDENTE | 0.5 | 12 | 22 | — |
| TF-247 | Ash Phoenix | REVISÃO PENDENTE | 9 | 15 | 105 | — |
| TF-248 | Ogrepede | REVISÃO PENDENTE | 6 | 13 | 142 | — |
| TF-249 | Aboleth, Nihileth | REVISÃO PENDENTE | 13 | 17 | 157 | — |
| TF-250 | Black Crier | REVISÃO PENDENTE | 11 | 16 | 150 | — |
| TF-251 | Corpse Mound | REVISÃO PENDENTE | 11 | 16 | 207 | — |

### Lote 2 — PR #2

| ID | Criatura | Situação | ND fonte | CA | PV | Alertas |
|---|---|---|---:|---:|---:|---|
| TF-252 | Adult Black Dragon Lich | REVISÃO PENDENTE | 17 | 19 | 253 | — |
| TF-253 | Asp Vine | REVISÃO PENDENTE | 4 | 13 | 55 | — |
| TF-254 | Child of the Briar | REVISÃO PENDENTE | 1 | 13 | 50 | — |
| TF-255 | Citrullus | REVISÃO PENDENTE | 3 | 15 | 85 | — |
| TF-256 | Climbing Vine | REVISÃO PENDENTE | 0.1 | 11 | 13 | — |
| TF-257 | Viiret | REVISÃO PENDENTE | 3 | 13 | 85 | — |
| TF-258 | Vine Lord, Tendril Puppet | REVISÃO PENDENTE | 2 | 13 | 51 | — |
| TF-259 | Chaos Creeper | REVISÃO PENDENTE | 9 | 16 | 150 | — |
| TF-260 | Vine Lord | BLOQUEADO | 9 | — | — | CONFLITO_EDICAO_HOMONIMO_OU_FONTE, CA_AUSENTE, PV_AUSENTE, ATRIBUTOS_AUSENTES |
| TF-261 | Vines of Nemthyr | REVISÃO PENDENTE | 8 | 15 | 133 | — |
| TF-263 | Abrikandilu | REVISÃO PENDENTE | 5 | 16 | 65 | — |
| TF-264 | Abyssal Hordeling | REVISÃO PENDENTE | 0 | 11 | 20 | — |
| TF-265 | Alabroza, Bloodfiend | REVISÃO PENDENTE | 4 | 14 | 72 | — |
| TF-266 | Chemosit | REVISÃO PENDENTE | 5 | 15 | 119 | — |
| TF-267 | Arx | REVISÃO PENDENTE | 9 | 17 | 171 | — |
| TF-268 | Chatterlome | REVISÃO PENDENTE | 7 | 16 | 93 | — |
| TF-269 | Vexxeh | REVISÃO PENDENTE | 6 | 15 | 105 | — |
| TF-270 | Black Shuck | REVISÃO PENDENTE | 11 | 17 | 157 | — |
| TF-272 | Light Eater | REVISÃO PENDENTE | 0.5 | 14 | 26 | — |
| TF-273 | Shoth, Sooze | REVISÃO PENDENTE | 0.5 | 12 | 49 | — |
| TF-274 | Malleable, Minor | REVISÃO PENDENTE | 1 | 11 | 32 | — |
| TF-276 | Malleable, Moderate | REVISÃO PENDENTE | 5 | 12 | 136 | — |
| TF-277 | Shoth, Oth | REVISÃO PENDENTE | 5 | 15 | 119 | — |
| TF-278 | Snatch Bat | REVISÃO PENDENTE | 5 | 16 | 97 | — |
| TF-279 | Fate Eater | REVISÃO PENDENTE | 6 | 16 | 130 | — |
| TF-280 | Mamura | REVISÃO PENDENTE | 6 | 16 | 112 | — |
| TF-283 | Shukankor | REVISÃO PENDENTE | 9 | 17 | 115 | — |
| TF-284 | Malleable, Major | REVISÃO PENDENTE | 10 | 13 | 218 | — |
| TF-286 | Malleable, Massive | REVISÃO PENDENTE | 16 | 14 | 248 | — |
| TF-288 | Snake, Swamp Adder | REVISÃO PENDENTE | 0.3 | 13 | 18 | — |
| TF-289 | Porcellina | REVISÃO PENDENTE | 0.5 | 13 | 28 | — |
| TF-290 | Glass Gator | REVISÃO PENDENTE | 1 | 15 | 45 | — |
| TF-292 | Snake, Zanskaran Viper | REVISÃO PENDENTE | 1 | 14 | 34 | — |
| TF-293 | Planar Flora, Hallowed Reeds | REVISÃO PENDENTE | 0.5 | 13 | 22 | — |
| TF-296 | Angel, Psychopomp | REVISÃO PENDENTE | 4 | 14 | 68 | — |
| TF-297 | Simurg | REVISÃO PENDENTE | 5 | 15 | 108 | — |
| TF-298 | Angel, Song | REVISÃO PENDENTE | 6 | 15 | 76 | — |
| TF-299 | Angel, Sammael | REVISÃO PENDENTE | 7 | 16 | 104 | — |
| TF-300 | Angel, Zoryas | REVISÃO PENDENTE | 8 | 14 | 104 | — |
| TF-301 | Planar Flora, Ecstatic Bloom | REVISÃO PENDENTE | 11 | 15 | 171 | — |

### Lote 3 — PR #4

| ID | Criatura | Situação | ND fonte | CA | PV | Alertas |
|---|---|---|---:|---:|---:|---|
| TF-302 | Angel, Shrouded | REVISÃO PENDENTE | 13 | 18 | 161 | — |
| TF-303 | Angel, Uridimmu | REVISÃO PENDENTE | 14 | 18 | 150 | — |
| TF-304 | Living Star | DADOS FALTANTES | 19 | 19 | 207 | ATRIBUTOS_AUSENTES |
| TF-305 | Angel, Zirnitran | REVISÃO PENDENTE | 20 | 19 | 325 | — |
| TF-306 | Simian, Monkey King | REVISÃO PENDENTE | 21 | 21 | 262 | — |
| TF-309 | Living Wick | BLOQUEADO | 1/4 | 13 | 28 | CONFLITO_EDICAO_HOMONIMO_OU_FONTE, ATRIBUTOS_AUSENTES |
| TF-312 | Sigilian | REVISÃO PENDENTE | 2 | 14 | 65 | — |
| TF-316 | Soil Snake | REVISÃO PENDENTE | 4 | 14 | 115 | — |
| TF-317 | Faux-Garou | REVISÃO PENDENTE | 5 | 12 | 93 | — |
| TF-318 | Fellforged | BLOQUEADO | 5 | 15 | 135 | CONFLITO_EDICAO_HOMONIMO_OU_FONTE |
| TF-319 | Gearforged Templar | BLOQUEADO | 6 | 18 | 71 | CONFLITO_EDICAO_HOMONIMO_OU_FONTE |
| TF-320 | Gnarljak | BLOQUEADO | 6 | 16 | — | CONFLITO_EDICAO_HOMONIMO_OU_FONTE, PV_AUSENTE, ATRIBUTOS_AUSENTES |
| TF-325 | Lindwurm | BLOQUEADO | 6 | 15 | 136 | CONFLITO_EDICAO_HOMONIMO_OU_FONTE |
| TF-326 | Linnorm, Vent | REVISÃO PENDENTE | 16 | 19 | 247 | — |
| TF-327 | Azer Forgemaster | REVISÃO PENDENTE | 4 | 16 | 78 | — |
| TF-328 | Gnyan | REVISÃO PENDENTE | 4 | 14 | 90 | — |
| TF-329 | Living Soot | REVISÃO PENDENTE | 7 | 15 | 142 | — |
| TF-330 | Spark | REVISÃO PENDENTE | 7 | 15 | 104 | — |
| TF-331 | Liosalfar | REVISÃO PENDENTE | 10 | 17 | 132 | — |
| TF-332 | Slow Storm | REVISÃO PENDENTE | 15 | 19 | 220 | — |
| TF-333 | Living Shade | REVISÃO PENDENTE | 1/4 | 12 | 18 | — |
| TF-334 | Far Darrig | BLOQUEADO | 3 | 14 | 84 | CONFLITO_EDICAO_HOMONIMO_OU_FONTE |
| TF-335 | Woe Siphon | REVISÃO PENDENTE | 3 | 14 | 45 | — |
| TF-336 | Far Dorocha | REVISÃO PENDENTE | 5 | 14 | 82 | — |
| TF-338 | Somberweave | REVISÃO PENDENTE | 5 | 14 | 78 | — |
| TF-339 | Malphas | REVISÃO PENDENTE | 6 | 16 | 135 | — |
| TF-340 | Wilderness Crone | REVISÃO PENDENTE | 6 | 17 | 105 | — |
| TF-341 | Shurale | REVISÃO PENDENTE | 7 | 14 | 105 | — |
| TF-342 | Silenal | REVISÃO PENDENTE | 7 | 14 | 117 | — |
| TF-343 | Fear Smith | REVISÃO PENDENTE | 10 | 17 | 149 | — |
| TF-344 | Pumpkin King | REVISÃO PENDENTE | 10 | 15 | 138 | — |
| TF-345 | Animal Lord, Mouse King | REVISÃO PENDENTE | 11 | 17 | 150 | — |
| TF-346 | Animal Lord, Lord of Vultures | REVISÃO PENDENTE | 12 | 17 | 152 | — |
| TF-347 | Animal Lord, Bat King | REVISÃO PENDENTE | 13 | 17 | 150 | — |
| TF-348 | Life Broker | REVISÃO PENDENTE | 13 | 16 | 190 | — |
| TF-349 | Animal Lord, Brother Ox | REVISÃO PENDENTE | 16 | 18 | 187 | — |
| TF-350 | Ettin, Kobold | REVISÃO PENDENTE | 1 | 12 | 34 | — |
| TF-351 | Half-Demon Ogre | REVISÃO PENDENTE | 3 | 13 | 68 | — |
| TF-353 | Manggus | REVISÃO PENDENTE | 5 | 14 | 127 | — |
| TF-355 | Giant, Hill Chief | REVISÃO PENDENTE | 8 | 13 | 126 | — |

### Lote 4 — PR #4

| ID | Criatura | Situação | ND fonte | CA | PV | Alertas |
|---|---|---|---:|---:|---:|---|
| TF-356 | Grendel | BLOQUEADO | 9 | 15 | 114 | CONFLITO_EDICAO_HOMONIMO_OU_FONTE |
| TF-358 | Giant, Void | REVISÃO PENDENTE | 11 | 14 | 210 | — |
| TF-361 | Elder Black Pudding | BLOQUEADO | 8 | 7 | 171 | CONFLITO_EDICAO_HOMONIMO_OU_FONTE |
| TF-363 | Puffinfolk | REVISÃO PENDENTE | 1/2 | 15 | 22 | — |
| TF-364 | Simian, Kapi | REVISÃO PENDENTE | 1/2 | 14 | 13 | — |
| TF-365 | Erina, Defender | REVISÃO PENDENTE | 1 | 15 | 44 | — |
| TF-366 | Simian, Vanara | REVISÃO PENDENTE | 2 | 13 | 55 | — |
| TF-367 | Erina, Tussler | REVISÃO PENDENTE | 3 | 14 | 66 | — |
| TF-368 | Gnoll Slaver | REVISÃO PENDENTE | 3 | 15 | 71 | — |
| TF-369 | Gnoll, Havoc Runner | REVISÃO PENDENTE | 3 | 15 | 58 | — |
| TF-370 | Simian, Sulsha | REVISÃO PENDENTE | 4 | 16 | 90 | — |
| TF-372 | Gnomish Knife Cultist | REVISÃO PENDENTE | 5 | 16 | 97 | — |
| TF-373 | Kobold, Wizard | REVISÃO PENDENTE | 5 | 12 | 58 | HOMONIMO_KOBOLD_WIZARD_CR1_CR5 |
| TF-378 | Mahoru | REVISÃO PENDENTE | 3 | 15 | 105 | — |
| TF-379 | Snake with a Hundred Mage Hands | REVISÃO PENDENTE | 3 | 14 | 67 | — |
| TF-381 | Aracnecore | REVISÃO PENDENTE | 5 | 16 | 85 | — |
| TF-382 | Likho | BLOQUEADO | 5 | — | — | CONFLITO_EDICAO_HOMONIMO_OU_FONTE, CA_AUSENTE, PV_AUSENTE, ATRIBUTOS_AUSENTES |
| TF-384 | Mutant Rust Monster | REVISÃO PENDENTE | 8 | 16 | 126 | — |
| TF-385 | Mantik | REVISÃO PENDENTE | 9 | 16 | 168 | — |
| TF-386 | Grootslang | BLOQUEADO | 11 | 15 | 145 | CONFLITO_EDICAO_HOMONIMO_OU_FONTE |
| TF-388 | Son of Fenris | BLOQUEADO | 12 | 17 | 175 | CONFLITO_EDICAO_HOMONIMO_OU_FONTE |
| TF-389 | Supermutant Rust Monster | REVISÃO PENDENTE | 12 | 16 | 195 | — |
| TF-392 | Malmbjorn | REVISÃO PENDENTE | 15 | 18 | 218 | — |
| TF-393 | Minotaur Conqueror | REVISÃO PENDENTE | 16 | 19 | 262 | — |
| TF-394 | Shroud | REVISÃO PENDENTE | 1/8 | 13 | 9 | — |
| TF-395 | Skeleton, Cackling | REVISÃO PENDENTE | 1/2 | 9 | 26 | — |
| TF-396 | Skeleton, Clacking | REVISÃO PENDENTE | 2 | 14 | 45 | — |
| TF-397 | Fane Spirit | REVISÃO PENDENTE | 3 | 13 | 52 | — |
| TF-398 | Falsifier Fog | REVISÃO PENDENTE | 4 | 13 | 52 | — |
| TF-399 | Mari Lwyd | REVISÃO PENDENTE | 4 | 15 | 66 | — |
| TF-401 | Mallqui | BLOQUEADO | 8 | 14 | 120 | CONFLITO_EDICAO_HOMONIMO_OU_FONTE |
| TF-402 | Marsh Dire | REVISÃO PENDENTE | 8 | 15 | 142 | — |
| TF-403 | Lich, Hierophant | REVISÃO PENDENTE | 9 | 14 | 91 | — |
| TF-405 | Lich, Virtuoso | REVISÃO PENDENTE | 12 | 17 | 123 | — |
| TF-406 | Mask Wight | REVISÃO PENDENTE | 13 | 19 | 207 | — |
| TF-407 | Lich, Pact | REVISÃO PENDENTE | 15 | 17 | 195 | — |
| TF-408 | Grove Swarm | BLOQUEADO | — | 16 | 217 | CONFLITO_EDICAO_HOMONIMO_OU_FONTE, ND_NAO_CONCILIADO |
| TF-409 | Mandrake | REVISÃO PENDENTE | 1/2 | 8 | 22 | — |
| TF-410 | Fungi, Wirbeln | REVISÃO PENDENTE | 1 | 13 | 16 | — |
| TF-411 | Garlicle | REVISÃO PENDENTE | 1 | 12 | 31 | — |

### Lote 5 — PR #3

| ID | Criatura | Situação | ND fonte | CA | PV | Alertas |
|---|---|---|---:|---:|---:|---|
| TF-412 | Mandrake, Great | REVISÃO PENDENTE | 1 | 11 | 44 | — |
| TF-413 | Sinstar, Star Thrall | REVISÃO PENDENTE | 2 | 13 | 58 | — |
| TF-414 | Wallflower | REVISÃO PENDENTE | 2 | 14 | 33 | DIVERGENCIA_TERMO_EDITORIAL_GRICK |
| TF-415 | Gloomflower | REVISÃO PENDENTE | 3 | 12 | 44 | — |
| TF-416 | Wind Witch | REVISÃO PENDENTE | 3 | 13 | 66 | — |
| TF-417 | Mandriano | REVISÃO PENDENTE | 5 | 13 | 60 | — |
| TF-418 | Sodwose | REVISÃO PENDENTE | 6 | 15 | 127 | — |
| TF-419 | Witchalder | REVISÃO PENDENTE | 6 | 15 | 102 | — |
| TF-420 | Mandriano, Ancient | REVISÃO PENDENTE | 8 | 14 | 102 | — |
| TF-421 | Planar Flora, Execrable Shrub | REVISÃO PENDENTE | 1/2 | 14 | 40 | — |
| TF-423 | Spawn of Chernobog | REVISÃO PENDENTE | 4 | 14 | 95 | — |
| TF-424 | Soul Eater | REVISÃO PENDENTE | 7 | 16 | 105 | — |
| TF-425 | Snow Terror | REVISÃO PENDENTE | 8 | 16 | 127 | — |
| TF-426 | Planar Flora, Thorned Sulfurlord | REVISÃO PENDENTE | 11 | 17 | 171 | — |
| TF-428 | Cerberus Guardian | REVISÃO PENDENTE | 23 | 20 | 310 | — |
| TF-431 | Conjured Guardian | ND DINÂMICO | — | 17 | 55 | ND_VARIAVEL_CONJURACAO |
| TF-448 | Imprisoned Celestial | REVISÃO PENDENTE | 10 | 17 | 178 | — |
| TF-449 | Imprisoned Fiend | REVISÃO PENDENTE | 9 | 14 | 133 | — |
| TF-459 | Ankheg Empress | REVISÃO PENDENTE | 8 | 16 | 174 | — |
| TF-462 | Behir Magus | REVISÃO PENDENTE | 12 | 16 | 168 | — |
| TF-468 | Faerie Chimera | REVISÃO PENDENTE | 7 | 13 | 114 | DIVERGENCIA_TIPO_DANO_SOPRO |
| TF-470 | Fiendish Chimera | REVISÃO PENDENTE | 7 | 13 | 114 | — |
| TF-473 | Flying Lion | REVISÃO PENDENTE | 3 | 12 | 57 | — |
| TF-476 | Greater Sphinx | REVISÃO PENDENTE | 17 | 20 | 220 | — |
| TF-499 | Cloud of Ghasthoppers | REVISÃO PENDENTE | 4 | 14 | 78 | — |
| TF-500 | Gorger Zombie Horde | REVISÃO PENDENTE | 4 | 8 | 75 | DIVERGENCIA_INDICE_DE_PUBLICACAO |
| TF-501 | Lost Prospector | REVISÃO PENDENTE | 4 | 11 | 58 | — |
| TF-503 | Stuffed Crab | REVISÃO PENDENTE | 6 | 14 | 104 | — |
| TF-504 | Warlord's Ghost | REVISÃO PENDENTE | 4 | 13 | 58 | — |
| TF-505 | Demilich Mastermind | REVISÃO PENDENTE | 18 | 20 | 319 | — |
| TF-506 | Mariner Ghost Swarm | REVISÃO PENDENTE | 11 | 15 | 340 | — |
| TF-507 | Fogborn Skeleton Horde | REVISÃO PENDENTE | 4 | 13 | 65 | — |
| TF-509 | Fogborn Zombie Horde | REVISÃO PENDENTE | 4 | 8 | 75 | — |
| TF-510 | Infernal Mammoth | REVISÃO PENDENTE | 5 | 15 | 104 | — |
| TF-511 | Fiendbloom Awakened Tree | REVISÃO PENDENTE | 2 | 13 | 51 | — |
| TF-516 | Kanos Spawn | REVISÃO PENDENTE | 4 | 14 | 78 | — |
| TF-517 | Imp Flock | REVISÃO PENDENTE | 5 | 19 | 49 | — |
| TF-518 | Infernal Dwarf | REVISÃO PENDENTE | 3 | 16 | 65 | — |
| TF-521 | Bugbear Door Breaker | REVISÃO PENDENTE | 3 | 14 | 60 | — |
| TF-522 | Crime Boss | REVISÃO PENDENTE | 6 | 15 | 127 | — |

---

**Conclusão:** 200 identificadores presentes e sem duplicatas nos cinco lotes, **199 registros com ações resumidas**, **195 com dados básicos preenchidos**, **14 bloqueios de edição/fonte**, **0 pesquisas canônicas aprovadas nesta auditoria**, **0 atualizações globais**. A diferença entre publicação e aprovação foi preservada.
