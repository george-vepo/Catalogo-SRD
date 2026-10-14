# Política operacional de lotes de pesquisa SRD — 13/10/2026

## Regra vigente

A partir deste registro, pesquisar e publicar **20 criaturas por lote**. O checkpoint futuro deve conter até 20 registros em um arquivo `research.json` do novo lote, e o ledger deve avançar conforme os registros realmente pesquisados. Para a fila atual (280 IDs pendentes) há **14 lotes de 20**.

- **Fonte de verdade para o agendamento:** `operational/research/catalog-ledger-20261011-v23/campaign.json`, campos `research_checkpoint_batch_size=20`, `research_queue_batches_of_twenty=14` e `next_batches[].ids`. 
- **Índice de verdade:** `operational/research/catalog-ledger-20261011-v23/catalog-status.csv`, UTF-8, separador `;`; identificar registros pendentes pela coluna `Estado=PENDENTE_PESQUISA`.
- Os **23 checkpoints históricos de cinco criaturas não são reescritos**, e nenhuma ficha ou imagem canônica é promovida como efeito da mudança de configuração.
- Não aumentar `research_stage_count` nem escrever checkpoint de 20 até que as 20 fichas tenham sido efetivamente investigadas. Registrar pendências/ambiguidades com clareza, inclusive para fichas parciais.
- A publicação de novos checkpoints deve ser feita na branch de pesquisa da PR #1, com SHA esperado e verificação de contagens/IDs únicos antes e após a gravação. Atualizar índice, ledger e descrição da PR com evidências da publicação.
- Revisão independente, direitos de regras e imagens, e integração ao construtor permanecem gates separados e não aprovados pela simples conclusão de pesquisa. Sem merge por suposição.
- Se um lote contiver fontes inacessíveis, registrar estado **PARCIAL** e pendências objetivas para os IDs afetados; não preencher atributos ou estatísticas por inferência.

## Migração

| Item | Antes | Depois |
|---|---:|---:|
| Tamanho da próxima unidade de pesquisa | 5 | **20** |
| Criaturas ainda sem pesquisa | 280 | 280 |
| Grupos restantes | 56 | **14** |
| Criaturas já pesquisadas | 115 | 115 |
| Checkpoints históricos | 23 (de cinco) | 23 (preservados) |
| Fichas canônicas completas | 212 | 212 |
| Imagens verificadas | 23 | 23 |

O ledger `v22` é a última versão com a fila antiga e foi preservado. O ledger `v23` armazena a nova fila. O campo `legacy_research_queue_batches_of_five_at_migration` é **histórico**, não representa grupos ativos.
