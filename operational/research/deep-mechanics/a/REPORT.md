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
