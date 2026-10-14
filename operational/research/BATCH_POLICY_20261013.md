# SRD Card Game 607 — Política de pesquisa em lotes de 40

**Vigência:** 13/10/2026. **Substitui a política anterior de 20** para os próximos checkpoints. A versão de 20 permanece preservada no histórico Git.

## Regra vigente e controles

- Executar e contabilizar **40 criaturas por lote**, na ordem de `operational/research/catalog-ledger-20261011-v26/campaign.json`. Campos de controle: `research_checkpoint_batch_size=40`, `research_queue_batches_of_forty=6`, `next_batches[].ids`.
- A fila de 240 IDs pendentes foi reagrupada em **seis lotes de 40**, sem reordenar, excluir nem adicionar registros.
- Checkpoints parciais menores podem ser publicados para segurança de persistência, como já ocorreu em lotes antigos, **mas não devem ser contabilizados antecipadamente como um lote de 40 concluído**.
- Há um checkpoint parcial **TF-166 a TF-170 (cinco criaturas)** já gravado em `checkpoints/20261013_TF-166_TF-170/research.json` e não reconciliado no ledger v25. **Reutilizá-lo**, não pesquisar novamente nem somar sua contagem duas vezes. A pesquisa restante do primeiro lote começa em TF-171.
- Não substituir nem excluir os 28 checkpoints anteriores. Os cinco registros TF-166 a TF-170 também permanecem intactos como WIP.
- Não elevar `research_stage_count` sem incluir os respectivos IDs e checkpoints no CSV de 607 entradas; não preencher estatísticas sem fonte confiável. Para conteúdos parcialmente pesquisados, registrar estado PARCIAL com limitações.
- Confirmar SHA da branch e ausência de alterações concorrentes antes de escrever; atualizar por `expected_sha`, sem force push. Conferir depois os IDs únicos, contagens, PR e o próximo grupo.
- Preservar `main`, ZIP canônico, imagens e fichas aprovadas. Nenhum gate de revisão, licença, teste ou homologação é satisfeito pela pesquisa.

## Estado na migração

| Indicador | Confirmado |
|---|---:|
| Catálogo total | 607 |
| Fichas canônicas completas | 212 |
| Fichas canônicas incompletas | 395 |
| Pesquisas reconciliadas no ledger | 155 |
| Pesquisas pendentes no ledger | 240 |
| Subcheckpoint iniciado, não reconciliado | TF-166 a TF-170 (5/40) |
| Checkpoints anteriores no ledger | 28 |
| Imagens verificadas | 23 |
| Lotes futuros | 6 de 40 |

**Próxima janela (40 IDs):** TF-166, TF-167, TF-168, TF-169, TF-170, TF-171, TF-172, TF-173, TF-174, TF-175, TF-176, TF-177, TF-178, TF-179, TF-180, TF-181, TF-182, TF-186, TF-187, TF-188, TF-189, TF-190, TF-191, TF-192, TF-193, TF-194, TF-195, TF-196, TF-197, TF-198, TF-199, TF-200, TF-201, TF-202, TF-203, TF-204, TF-205, TF-206, TF-208, TF-210.

O arquivo `catalog-ledger-20261011-v25` continua sendo o registro histórico da pesquisa em grupos de 20; o novo `v26` altera somente a configuração do tamanho da fila, não aprova fichas.
