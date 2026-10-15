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


## Atualização técnica — complementação da pesquisa (14/10/2026)

**Fichas completas vinculadas ao SRD 5.2.1:** `fichas_srd521_integral_3.json` preserva os blocos integrais originais de **AT-001 Gibbering Mouther**, **AT-002 Roper** e **AT-003 Aboleth** que já constavam no arquivo de 607. Esses textos são do *SRD 5.2.1*, disponibilizado pela Wizards of the Coast sob **CC BY 4.0**. A atribuição exigida consta no novo arquivo. **Não se aplica licença CC às ilustrações de D&D Beyond.** Conferir a fidelidade e engine antes da homologação.

**Sete incompletas:** `pesquisa_fichas_incompletas_7.json` incorpora apenas evidências numéricas e índices de mecânicas com URLs públicas, sem promover as fichas. Encontradas fontes para todos os sete IDs, sujeitas à revisão editorial, OGL, versão e engine.

- **TF-004 Astral Snapper:** [Creature Codex 2018](https://www.5esrd.com/database/creature/astral-snapper/), ND 3, CA 12, PV 78.
- **TF-013 Yavalnoi:** [Tome of Beasts 2](https://www.5esrd.com/database/creature/yavalnoi/), ND 6, CA 16, PV 126.
- **TF-010 Chelicerae:** [Tome of Beasts 2023](https://www.5esrd.com/database/creature/chelicerae-3pp/), ND 7, CA 16, PV 153; ações revistas não devem ser mescladas com 2016.
- **TF-014 Ziphius:** [Creature Codex 2018](https://www.5esrd.com/database/creature/ziphius/), ND 8, CA 16, PV 135.
- **TF-012 Xhkarsh:** [Tome of Beasts 2023](https://www.5esrd.com/database/creature/xhkarsh-3pp/), ND 9, CA 18, PV 171. A versão original de 2016 tem **ND 8, CA 19, PV 133**; manter ambas separadas.
- **TF-018 Voidling:** [Tome of Beasts 2023](https://www.5esrd.com/database/creature/voidling-3pp/), ND 11, CA 15, PV 180.
- **TF-285 Snallygaster:** [Tome of Beasts 3](https://www.5esrd.com/database/creature/snallygaster/), ND 15, CA 16, PV 207; **não confundir** com Snallygast / ND 10 / Dragão de outra fonte.

### Autorização de mecânicas versus imagens

1. **SRD 5.2.1:** texto mecânico sob [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode), com atribuição; a licença não libera automaticamente as artes.
2. **Kobold Press:** a licença [OGL 1.0a](https://koboldpress.com/open-game-license-version-1-0a/) abre somente o conteúdo designado como Open Game Content; **ilustração, certos nomes e outros elementos de identidade** podem ser reservados. Completar a referência e o aviso de copyright aplicável a cada livro antes de redistribuir o texto integral.
3. **Livros D&D Beyond fora do SRD:** as cinco criaturas externas podem ter textos e imagens reservados. A existência de statblock em fontes auxiliares não concede autorização de reprodução.
4. **Imagens no Git:** 25/40 possuem arquivos físicos existentes, mas **0/40 possuem licença/aceite visual documentados neste trabalho**. Os 15 restantes necessitam de imagem original ou explicitamente licenciada. A coluna `IMAGEM_APROVADA_PARA_CARDGAME` foi marcada `NAO` em todos os 40 registros, até evidência e aceite do administrador.
5. **Combate:** não integrar à engine mecânicas que carecem de economia de ações, eventos, duração, alcance, condições, concentração, testes, recarga e recursos completos; esses campos ainda dependem da revisão de suas fontes e testes.

### Estado real da entrega

| Item | Evidência documentada | Pendente |
|---|---:|---|
| Cartas da proposta | 40 | validação final para jogar |
| Fichas integrais SRD 5.2.1 reproduzidas com atribuição | 3 | teste de implementação SRD 5.2.1 |
| Sete fichas incompletas com fonte individual e resumo auditável | 7 | extração e adaptação integral OGL + testes |
| Outras 30 cartas | 30 com seus registros e fontes originais (algumas só em resumo, 5 candidatas externas) | auditoria, consolidação, eventual licença e testes |
| Imagens locais já existentes | 25 | verificação de identidade, dimensões, créditos, licença e aceite |
| Imagens ainda não incorporadas | 15 | pesquisar licenças ou criar arte original e obter aprovação |
| Imagens homologadas | **0** | 40 aprovações individualizadas |

**O PR é de pesquisa e integração documental.** NÃO é uma declaração de 40 fichas completas e 40 imagens aprovadas; alterações no catálogo ativo e no estado oficial seguem bloqueadas.

## Atualização visual — imagens realmente gravadas na pesquisa

- **7 arquivos WebP adicionados** em `images-web-pesquisa/`: Cranium Rat, Gazer, Mindwitness, Kalaraq Quori, Greater Star Spawn Emissary, Gibbering Mouther (AT-001) e Roper (AT-002).
- O índice `cards.csv` referencia esses sete caminhos físicos; contagem atual **32/40 com arquivo local** (25 anteriores + 7 novos).
- O arquivo `imagens-pesquisadas-15.csv` rastreia as 15 pendências originais e inclui as **8 que continuam sem imagem local**: Minor/Moderate/Major/Massive Malleable, Maw Swarm, Mayday, Shukankor e Aboleth Brute.
- A galeria visual `IMAGENS_PESQUISADAS.md` mostra as 7 imagens incorporadas e documenta os links de pesquisa restantes. Não confundir imagem localizada/referenciada com arquivo binário integrado.
- **Arte de pesquisa, não homologação**; a proveniência está documentada e versões visuais de edições distintas não substituem atributos.
