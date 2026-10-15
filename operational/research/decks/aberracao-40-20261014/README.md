# SRD Card Game — baralho experimental de 40 Aberrações (14/10/2026)

> **REVISÃO / PESQUISA, NÃO HOMOLOGADO.** Nenhuma das 5 criaturas externas foi inserida no catálogo canônico; nenhum arquivo de imagem externo foi reproduzido. Nenhuma ficha incompleta é apresentada como completa.

## Escopo e entregas

- `cards.csv`: **40 cartas**, com `NOME;ND;FONTE;TIPO;RARIDADE`, IDs dos 35 registros originais, classificação da ficha, caminhos de arte **já existente** e links de referência.
- `fichas_catalogo_35.json`: recorte dos **35 registros preexistentes** de `SRD_CYCLES/26-30/working/03_CONSTRUTOR/outputs/SRD_FICHAS_607.json`, sem criar CA, PV, ataques ou habilidades. Para pesquisas recentes, apontar à coluna `ARQUIVO_FICHA_EXISTENTE` e às fichas individuais da auditoria.
- As **5 externas** (Cranium Rat, Gazer, Mindwitness, Kalaraq Quori e Greater Star Spawn Emissary) aparecem como **candidatas**, apenas com fontes públicas de identificação, não com transcrições integrais ou imagens copiadas.

## Verificações objetivas

| Critério | Resultado |
|---|---:|
| Criaturas distintas na proposta | 40 |
| Existentes no catálogo controlado de 607 | 35 |
| Externas, sem registro aprovado | 5 |
| Controles históricos `Mecanica_completa=SIM` | 17 |
| Fichas `FICHA_COMPLETA_EM_CONTEUDO` (auditoria 2026-10-14) | 2 |
| Fichas `FICHA_COMPLETA_COM_RESSALVAS` (mesma auditoria) | 9 |
| Fichas `FICHA_INCOMPLETA` (mesma auditoria) | 7 |
| 35 originais com arquivo de imagem encontrado no Git | 25 |
| 35 originais sem arquivo de imagem local | 10 |
| Externas sem arquivo de imagem integrado | 5 |
| TOTAL sem arquivo de imagem integrado | 15 |

**Cuidado com o status histórico:** parte das 17 fichas com `SIM` contém `MECÂNICA INTEGRADA; RESUMO PRÓPRIO DA FONTE`, não um bloco integral de ações/regras pronto para engine. Para as outras 18, a auditoria final classifica conteúdo de forma mais granular. Campos vazios de CA/PV nos originais não foram preenchidos por inferência.

### Cartas externas / fonte editorial

| Criatura | ND | Referência pública | Situação |
|---|---:|---|---|
| Cranium Rat | 0 | [D&D Beyond — Monsters](https://www.dndbeyond.com/monsters?page=2&sort=size) | Usar edição **Monsters of the Multiverse**, em que é Aberração; a versão de *Volo* é Besta |
| Gazer | 1/2 | [D&D Beyond — Monsters](https://www.dndbeyond.com/monsters?page=4&sort=type) | Há versão de *Volo* e revisão MPMM; definir edição |
| Mindwitness | 5 | [Volo's Guide to Monsters](https://www.dndbeyond.com/sources/dnd/vgtm) | Material protegido, edição original |
| Kalaraq Quori | 19 | [Eberron: Rising from the Last War](https://marketplace.dndbeyond.com/settings/eberron-rising-from-the-last-war) | [Ilustração atribuída ao artista Christopher Burdett](https://christopherburdett.blogspot.com/2019/11/kalaraq-quori-dungeons-dragons-eberron.html) — referência somente, direitos Wizards of the Coast |
| Greater Star Spawn Emissary | 21 | [D&D Beyond — referência Legacy](https://www.dndbeyond.com/monsters?page=176&sort=-type) | Fixar edição 2014/2020; 2026 também tem versão atualizada |

### Regras/aceite antes de utilizar o deck

- Progressão: **20 Comuns, 12 Incomuns, 5 Raras, 2 Lendárias, 1 Mítica**. Apenas Comum invocada diretamente; evolução exige mesmo tipo + **raridade imediatamente superior**, carta na mão e fase legal.
- Para a partida oficial: validar inventário, IDs únicos das **cópias**, fichas integrais executáveis, recursos e imagens com licença confirmada.
- Os caminhos de imagem no CSV são apenas **arquivos já existentes** no Git; existência de bytes não prova autorização de reprodução ou pertinência da arte. As URLs externas apontam para **referência**; nenhuma foi baixada ou copiada para este PR.
- **Não alterar** `operational/research/catalog-ledger-20261011-v27/catalog-status.csv` nem o catálogo oficial até concluir os gates editoriais, mecânicos, visuais e jurídicos.
- Antes de promover esta proposta: completar as 7 fichas incompletas, resolver as 9 com ressalvas, reauditar as 17 históricas e conseguir licença/fichas das 5 externas.

### Fontes controladas

- [Controle histórico 607](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/main/operational/research/catalog-ledger-20261011-v27/catalog-status.csv)
- [Auditoria de 395 fichas pendentes](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/main/operational/reviews/20261014-imaged-cards/final-audit/audit-results.csv)
- [Fichas estruturadas históricas](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/main/SRD_CYCLES/26-30/working/03_CONSTRUTOR/outputs/SRD_FICHAS_607.json)
- [Índice de fontes de imagens e licenças não verificadas](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/main/SRD_CYCLES/26-30/working/03_CONSTRUTOR/outputs/SRD_URLS_IMAGENS_607.csv)

**NENHUMA IMPORTAÇÃO CANÔNICA / NENHUMA HOMOLOGAÇÃO.** Este pacote é para trabalho editorial e não modifica os estados da partida.
