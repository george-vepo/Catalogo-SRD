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
