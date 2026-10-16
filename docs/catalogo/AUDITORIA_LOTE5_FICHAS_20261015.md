# Lote 5 — seis referências mecânicas de terceiros (15/10/2026)

> **Pesquisa integrada ao painel, não homologação de combate.** Base: PR #22; sequência de dependência #20 → #21 → #22 → este lote. Os arquivos originais `fichas-607.json`, `auditoria-607.json`, engine, baralhos e arte binária não foram alterados. O `app.js` recebeu uma **alteração localizada somente na apresentação do painel ampliado**, preservando grade, filtros e navegação.

## Resultado verificável

- **6 referências novas** (KP-S013–KP-S018) acrescentadas a `data/fichas-referencia-verificadas.json`, preservando os seis registros detalhados de TF-059 a TF-065 e todo seu conteúdo.
- A aplicação **já consumia** `extraSheets.records` e cruzava o campo `id` com a megalista. Após merge, os seis resumos serão exibidos ao abrir as cartas. Foi adicionada somente uma apresentação específica no detalhe para indicar fonte parcial, não homologação e **link clicável à ficha original**.
- Todas as seis identidades, NDs, CAs e PVs coincidem com `fichas-607.json`; nada foi sobregravado. Fonte individual, obra e status de leitura registrados por criatura.
- Três páginas lidas diretamente; três entradas verificadas por índice textual indexado, com bloqueio intermitente da leitura direta. Nenhuma foi classificada como `COMPLETA_CANONICA`.

| ID | Criatura | Publicação identificada | ND | CA | PV | Qualidade da fonte |
|---|---|---|---:|---:|---:|---|
| KP-S013 | [Giant, Jotun](https://www.5esrd.com/database/creature/giant-jotun-3pp/) | Tome of Beasts 1 (2023) | 22 | 20 | 370 | Página lida; características resumidas |
| KP-S014 | [Pustulent Shambler](https://www.5esrd.com/database/creature/pustulent-shambler/) | Tome of Beasts 2 (2020) | 13 | 10 | 232 | Página lida; doença Bonerot e ataques resumidos |
| KP-S015 | [Ooze, Scintillating](https://www.5esrd.com/database/creature/ooze-scintillating/) | Tome of Beasts 3 (2022) | 12 | 15 | 165 | Página lida; reação e ações lendárias resumidas |
| KP-S016 | [First Servant](https://www.5esrd.com/database/creature/first-servant/) | Southlands (2021) | 12 | 17 | 162 | Índice textual, leitura direta intermitentemente bloqueada |
| KP-S017 | [Vesiculosa](https://www.5esrd.com/database/creature/vesiculosa-3pp/) | Tome of Beasts 1 (2023) | 11 | 15 | 232 | Índice textual, leitura direta intermitentemente bloqueada |
| KP-S018 | [Sinstar](https://www.5esrd.com/database/creature/sinstar/) | Tome of Beasts 3 | 17 | 17 | 275 | Índice textual, leitura direta bloqueada; ataques completos não conferidos |

## Precisão editorial

As páginas publicadas em `5esrd.com` exibem fichas de **Kobold Press/Open Design LLC**, com avisos de atribuição e copyright. O nome **5th Edition SRD** do portal **não transforma essas seis fichas no SRD 5.2.1 da Wizards of the Coast**. Elas permanecem material de terceiros da edição explicitada, com resumos redigidos para o catálogo, sem copiar integralmente statblocks, magias ou ilustrações. Algumas são OGL mas os direitos completos e as restrições editoriais ainda precisam ser revisados para produção, particularmente nomes e ilustrações.

A transcrição integral dos livros, direitos de redistribuição/impressão, compatibilidade da engine e habilidades de suporte não foram aprovados. Uma classificação histórica **`PÁGINA INDIVIDUAL NÃO CONFIRMADA; FICHA PENDENTE`** ainda pode aparecer no registro canônico até reconciliação administrativa; o novo overlay não a substitui e inclui proveniência e limitações de verificação próprias.

## Validação e limites

- IDs únicos nas 12 referências; 6 referências antigas preservadas sem mudanças; 6 novas verificadas contra o JSON original para nome, ND, CA e PV.
- 3 leituras diretas e 3 fontes indexadas explicitamente separadas; fontes e editoras versionadas.
- Contagens do catálogo visual não se alteram: após o PR #20 proposto, **36/1.320** possuem referência web exibível; **1.284** continuam sem referência.
- JavaScript compilado sintaticamente e verificado o mapeamento por ID. Não foram realizados testes de navegador HTTP/E2E, execução no Windows V-Bridge, licença de arte ou revisão independente; esses critérios continuam pendentes.

**Aceite específico deste lote:** os seis resumos ficam disponíveis no painel após merge pela lógica já existente, mas não são fichas completas homologadas do card game.
