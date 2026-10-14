# SRD Card Game 607 — Auditoria final (parcial)

**Situação:** EM ANDAMENTO — lote 001/040, 10/395 fichas (385 restantes).

**Fonte:** branch `chatgpt/srd607-audit-imaged-cards-20261014`, snapshot anterior à auditoria `c75c62c616e34af98593ecc0de895dd2f7dabeaf`; CSV `operational/research/catalog-ledger-20261011-v27/catalog-status.csv` (`Mecanica_completa=NAO`: 395 de 607).

**Execução:** leitura e persistência via conector GitHub no chat interativo. **V-Bridge Windows e computer-use: não executados/não verificados neste ambiente**. Sem modificações do catálogo canônico nem merge.

## Resultado do primeiro lote

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
