# SRD Card Game 607 — pesquisa paralela B (13/10/2026)

## Escopo e procedência

- Repositório: `george-vepo/SRD-Card-Game-607-Supervisor`.
- Branch exclusiva de execução: `chatgpt/srd607-parallel-b`.
- Referência imutável consultada: `chatgpt/srd607-research-checkpoints-20261011` em `a962c48a1169c2ef2be8137715a095a596753b32`.
- Fonte da seleção de IDs: `operational/research/catalog-ledger-20261011-v27/campaign.json`, exclusivamente `next_batches[2].ids` e `next_batches[3].ids`. A contagem usa somente os IDs listados, sem preencher as lacunas numéricas.
- Os artefatos escritos são *exclusivamente* os dois checkpoints próprios e esta auditoria; não foram alterados `main`, a branch de referência, PR #1, ledger global, CSV global, STATUS compartilhado, política de lotes ou catálogo canônico.

## Checkpoints e resultados

| Lote | Arquivo | IDs únicos | Fontes mecânicas registradas | Fontes editoriais A5E diretas | Inconsistências de edição/homônimo explicitadas |
|---|---|---:|---:|---:|---:|
| 3 | `operational/research/checkpoints/20261013_TF-302_TF-355/research.json` | 40 | 40 | 3 | 6 |
| 4 | `operational/research/checkpoints/20261013_TF-356_TF-411/research.json` | 40 | 40 | 8 | 7 |
| **Total** | **dois checkpoints** | **80** | **80** | **11** | **13** |

Os 80 registros representam **pesquisa e síntese parcial**, não 80 fichas completas ou aprovadas. A origem editorial das criaturas Kobold Press foi cotejada com o índice oficial da editora, mas a maioria dos atributos e mecânicas individuais provém de reproduções abertas, não de uma edição impressa validada. O portal A5E tem fichas editoriais abertas de origem própria, mas exige avaliação de regras e direitos.

## Fontes usadas e limitações

- Índice oficial de monstros Kobold Press: https://koboldpress.com/tools/kobold-press-monsters/ . Indica criatura, ND e publicação; não substitui bloco detalhado de regra.
- Portal oficial Level Up A5E / EN Publishing: https://a5e.tools/monsters . Usado para dados individuais de Monstrous Menagerie, Gate Pass Gazette, Dungeon Delver's Guide, To Save A Kingdom, Adventurer's Guide e Mythological Figures & Maleficent Monsters.
- 5eSRD / Open Gaming Network: https://www.5esrd.com/database/creature/ . Reproduz blocos de fontes diversas; é **secundário**, inclusive quando atribui um editor.
- Here Be Taverns, Robinloft, 5ecompendium e KPOGL: índices/transcrições de terceiros, sujeitos a seleção de edição errada, omissões, atualização e divergência.
- AnyFlip/Flip eBooks: reproduções terceirizadas, **não fonte editorial autorizada comprovada**. Exigem validação de edição, integridade e licença antes de utilizar textos ou imagens.
- O resumo mecânico é original e de verificação limitada; nenhum bloco longo protegido foi copiado para o catálogo.

## Casos editoriais que não devem ser mesclados

- **TF-309 Living Wick**: edição revisada vs original têm diferenças de atributos, autonomia e CDs; sem fixar atributos.
- **TF-318 Fellforged e TF-319 Gearforged Templar**: fichas originais e revisadas divergem; TF-319 alterna glaive/três golpes e espadão/quatro golpes.
- **TF-320 Gnarljak**: PV 49/63/88 aparecem em três transcrições/edições; PV não aprovado.
- **TF-325 Lindwurm**: ND5 em exemplar original reproduzido, ND6 em índice/revisão.
- **TF-334 Far Darrig**: homônimo ND2/PV39, versão pesquisada ND3/PV84.
- **TF-356 Grendel**: A5E ND9/CA15/PV114 vs Viking Adventures ND12/CA19/PV147.
- **TF-361 Elder Black Pudding**: A5E ND8/PV171 vs outro 5e ND4/PV130.
- **TF-382 Likho**: ND5 no índice Kobold Press vs ND6 na reprodução aberta; atributos e PV não conciliados.
- **TF-386 Grootslang**: A5E ND11 versus versões ND8 e ND12.
- **TF-388 Son of Fenris**: publicação original e revisão com deslocamentos, resistências e outras regras distintos.
- **TF-401 Mallqui**: original e revisão diferem em SAB, deslocamento e regeneração.
- **TF-408 Grove Swarm**: site oficial A5E exibe ND0 ao lado de CA16/PV217 e mecânica de enxame gigantesco; **ND mantido pendente**. A reprodução 5eSRD diverge também em extensão territorial e tipagem.

Além das treze ocorrências acima, todos os registros estão pendentes de conferência das estatísticas técnicas detalhadas e da publicação correta. Criaturas de A5E não devem ser convertidas para 5e sem revisão mecânica.

## Histórico de commits e preservação

- `2be962eb0ce2221a9869085a3218c62b3b2f9500`: checkpoint do lote 3 com 40 registros.
- `eca5f595d07f867ff7f87347ee69e41eaa2806e3`: checkpoint do lote 4 com 40 registros.
- Esta auditoria e a retificação de fontes editoriais para TF-327/TF-351/TF-355 serão publicadas em commit subsequente exclusivo desta branch.
- Validações: SHA da branch verificado antes das escritas, atualizações condicionais por `expected_sha`, conferência pós-publicação de cada checkpoint e ordem dos IDs comparada com o ledger.
- Não houve reset, clean, force push, merge, aprovação própria, promoção de ficha, validação de imagem ou edição do ledger compartilhado.

## Próximos gates (todos pendentes)

1. Revisão editorial independente da edição exata e dos campos ND, CA, PV, atributos, deslocamentos, salvaguardas, características, ações, recargas e efeitos por ficha, com atenção às divergências acima.
2. Revisão jurídica da licença das regras/fontes, limites de reprodução e direitos de imagens.
3. Decisão específica sobre interoperabilidade A5E e D&D 5e e normalização de nomenclaturas.
4. Integração supervisionada futura ao catálogo e CSV globais **em processo próprio autorizado**, sem considerar este checkpoint suficiente.
5. Testes, validação visual, revisão da PR e aprovação por agente/pessoa independente. PR permanece em rascunho e não deve ser mesclada automaticamente.
