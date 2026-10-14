# SRD Card Game 607 — auditoria inicial de fichas com imagens (14/10/2026)

**Natureza:** triagem documental e de integridade; não é homologação independente, nem verificação visual individual, nem autorização de licenças.

**Repositório:** `george-vepo/SRD-Card-Game-607-Supervisor`  
**Snapshot imutável auditado:** `634f88491786b8c6b4b67a764866684c54df02a6` (`main`).  
**Ledger:** `operational/research/catalog-ledger-20261011-v27/catalog-status.csv`.  
**Evidências:** registros e manifestos `operational/research/deep-mechanics/{a,b,c}/`, árvores Git e imagens `operational/assets/creature-images/`.

## Escopo e correção da contagem

O levantamento anterior havia informado **296** fichas estruturadas com imagem (A 83, B 115, C 98). Durante a releitura de todos os 132 registros individuais A, foram observados **99** com indicadores de estruturação em fonte individual, embora o manifesto consolidado A ainda conte **90**. Desses 99, **92 possuem imagem**. Não excluir arbitrariamente nove registros nem promover seus estados sem reconciliação.

**Triagem ampliada e conservadora: 305 candidatos físicos** (A 92, B 115, C 98); engloba o lote anteriormente estimado em 296. Os outros itens estruturados sem imagem devem ser tratados separadamente.

| Verificação | Resultado |
|---|---:|
| Catálogo total | 607 |
| Marcados `Mecanica_completa=NAO` | 395 |
| Pendentes com ao menos um arquivo físico de imagem | 348 |
| Candidatos estruturados com imagem nesta triagem | 305 |
| Grupo A (indicadores individuais, não homologados) | 92 |
| Grupo B (inventário individualizado) | 115 |
| Grupo C (pesquisa detalhada na fonte individual) | 98 |
| Entre os candidatos B, com bloqueio/conflito identificado no manifesto | 108 |
| Entre os candidatos C, com estado iniciado por BLOQUEADA | 25 |
| Candidatos sem SHA individual de imagem no manifesto do grupo | 12 |
| Candidatos A com alguma dimensão abaixo de 500 px | 21 |
| Fichas promovidas a completas por esta revisão | **0** |

## Evidência de integridade

Os 334 binários registrados nos manifestos A/B/C (124+114+96) estão presentes na árvore Git consultada e têm SHA e tamanho coerentes nos campos de manifesto verificados. Nem toda imagem central tem uma entrada no manifesto do grupo correspondente. No CSV por ID, `SHA_TAMANHO_CONFERIDOS` certifica só a integridade do objeto do Git; `ARQUIVO_PRESENTE_SEM_SHA_MANIFESTO_GRUPO` exige conciliação da procedência. Não é um selo de adequação artística.

**IDs candidatos que têm imagem mas carecem de SHA no manifesto individual do grupo (12):** TF-200, TF-201, TF-405, TF-428, TF-431, TF-459, TF-476, TF-503, TF-504, TF-505, TF-510, TF-511.

**Possível reutilização da mesma arte (SHA igual):** TF-384/TF-389 327bdaa2d6b6; TF-417/TF-420 bdd6eaad0308. Examinar contexto e identidade da criatura antes de usar em cartas distintas.


## Impedimentos para a promoção canônica

1. **Mecânica:** os registros A/B/C ainda não apresentam homologação editorial integral, cotejo independente de obra/errata e validação em engine. Inventários preenchidos não bastam. Alguns contêm divergências entre edições, fórmulas e regras externas; os bloqueios são preservados no CSV de auditoria.
2. **Imagem:** há binários de miniatura ou token com resolução insuficiente para arte final; 21 candidatos A já exigem especial atenção à resolução. Nenhuma imagem dos grupos tem aprovação visual/editorial de produção documentada.
3. **Direitos:** referências a acervos `homebrew` e módulos A5E não equivalem a licença reutilizável/comercial. Direitos devem ser comprovados por ativo, inclusive quando o Git confirma a existência do binário.
4. **Governança:** o CSV de controle v27 ainda não reflete estas revisões; esse atraso de atualização não demonstra que as fichas estejam completas. Não alterar `Mecanica_completa`, `Imagem` ou `Estado` no ledger sem cumprir gates.

## Problemas individuais já identificados em registros

- **TF-026 Bilby:** ficha estruturada, mas ilustração de 160×160 é miniatura não adequada para carta final.
- **TF-031 Razorback Crab:** prévia de 80×120, sem aceite de arte de produção.
- **TF-237 Tosculi Hive Queen:** regras de Stinger e remoção de veneno necessitam reconciliação editorial.
- **TF-293 Hallowed Reeds:** a identidade publicada é *Celestial*, apesar do nome de flora; a interpretação do Rebirth necessita validação.
- **TF-395 Cackling Skeleton:** arte genérica de esqueleto reaproveitada, oriunda de módulo com restrições a uso comercial; não presumir aprovação visual nem direitos comerciais.
- **TF-412 Great Mandrake:** inconsistência de modificador de Sabedoria, apesar de existir imagem.
- **TF-200 e TF-201:** mecânicas A5E condicionadas à validação de regras e direitos de uso, ainda que um arquivo de imagem exista no diretório central.

## Próximas ações por prioridade

1. **Conciliação dos inventários:** corrigir divergência 90/99 no manifesto A após cotejo de indicadores com o conteúdo de cada JSON; conferir os 12 vínculos de imagem sem manifesto do grupo.
2. **Bloqueios mecânicos:** conferir com edição e erratas corretas as fichas com conflito explícito (ao menos 108 casos B e 25 casos C na seleção física; conjuntos podem ter outras pendências).
3. **Qualidade da arte e licença:** retirar miniaturas, arte genérica inadequada e recursos sem direito de uso comprovado da fila pronta para produção; verificar fonte, dimensões, composição e autorização.
4. **Homologação:** executar revisão independente de estatísticas, ações, efeitos e testes da engine para cada ficha candidata. Só promover o registro se cumprir todos os gates.

## Arquivo de auditoria

`candidates-imaged.csv` lista **305 IDs**, em ordem do CSV v27, com evidência mecânica declarada, arquivo físico, SHA Git, contagem de bytes, estado dos gates, bloqueios e indicação de fonte. UTF-8 com separador ponto e vírgula.

**Atenção:** esta revisão é suficiente para triagem e localização de inconsistências documentais, mas **não substitui** análise individual de gameplay, confrontação com a fonte editorial de cada criatura ou inspeção humana de todas as imagens.

Nenhum dado canônico, ficha ou binário de imagem foi modificado. Nenhuma ficha foi homologada e nenhuma mudança foi feita em `main`.
