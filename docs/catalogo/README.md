# Catálogo Geral — SRD Card Game

Site estático do bestiário, com **1.320 criaturas distintas** da megalista do projeto e cruzamento com dados do repositório.

## Como abrir

A partir da raiz do repositório:

```bash
python3 -m http.server 8000 --directory docs
```

Abra **http://localhost:8000/catalogo/**.

O site pode ser publicado via **GitHub Pages** apontando para a pasta `/docs` da branch que contém os arquivos, se as configurações/permissões de Pages do repositório permitirem. **Este commit não significa que o site já está publicamente hospedado.** Abrir `index.html` diretamente por `file://` não funciona para os arquivos JSON carregados por `fetch`: use servidor HTTP local ou Pages.

## Experiência

- A grade exibe **somente a ilustração e o nome**. Sem atributos, habilidades ou caixas de texto sobre a arte.
- Ao clicar, a carta abre ampliada; imagem inteira em `object-fit: contain`; zoom de 100–400%, arrastar e navegar para anterior/próxima.
- Busca por nome, ID e publicação; filtros por **14 tipos**, cinco raridades, origem/catálogo, imagem e presença de ficha ou suporte.
- A ficha aberta mostra, **somente quando existente na fonte**, ND, CA, PV, atributos, condições, ações, ficha integral do SRD, resumo mecânico estruturado, links de publicação, campos históricos da megalista e andamento de auditoria.
- Suportes das **40 cartas Celestiais** (36 espécies, quatro cópias extras) e das **40 cartas de Aberração** aparecem como **candidatos, não homologados**.
- Itens sem imagem aprovada ou adequada recebem um ícone neutro; nunca é usada arte de outro monstro como substituta.
- Os dados de pesquisa mais aprofundada nas trilhas `a/b/c` são indexados por ID e exibidos por links diretos aos arquivos correspondentes do repositório.


## Lote adicional de auditoria (15/10/2026)

Este snapshot adiciona dois arquivos de pesquisa, sem homologar itens automaticamente:

- `data/curadoria-artes-20261015.json`: **4 referências web** aprovadas visualmente para uso ilustrativo no catálogo (AT-003, AT-009, AT-012, AT-024) e **5 candidatas recusadas**. Imagens continuam como links externos com direitos de reprodução não concedidos.
- `data/fichas-referencia-verificadas.json`: **6 fichas mecânicas detalhadas de referência** recuperadas do lote E e **6 novos resumos próprios de fontes externas** no lote 5 (KP-S013 a KP-S018). O site já lê esse arquivo e exibe essas referências quando a carta é aberta; elas não alteram a ficha original, o SRD 5.2.1 ou a homologação de regras.

No snapshot integrado até o PR #19 havia **35 referências visuais** e 1.285 espécies sem imagem. O PR #20 propõe **36 referências** e 1.284 sem imagem; o lote 6 acrescenta **Mammoth (AT-015)** como referência artística histórica com proveniência de domínio público, chegando a **37 referências** e **1.283 pendentes** no cenário empilhado, **somente após os merges autorizados**. Arquivos binários não revisados não são aceitos automaticamente. Consulte os relatórios de auditoria dos lotes 2 a 6. 

## Lote 5 — referências de terceiros (15/10/2026)

Acrescentados ao painel existente **6 resumos próprios de fichas externas** (KP-S013 Giant, Jotun; KP-S014 Pustulent Shambler; KP-S015 Ooze, Scintillating; KP-S016 First Servant; KP-S017 Vesiculosa; KP-S018 Sinstar), mantendo os 6 detalhamentos anteriores. As páginas 5esrd foram conferidas diretamente para três espécies; as outras três utilizaram índices textuais de pesquisa, com acesso direto intermitente ou bloqueado. Cada registro identifica esse limite, origem e publicação.

**Esses seis registros são referências não homologadas**, não fichas SRD 5.2.1 ou integrações à engine. O painel mostra resumos factuais, não transcrições integrais dos livros. CA/PV/ND são dados já existentes no catálogo-base; habilidades adicionais ficam separadas da mecânica canônica. Nenhuma arte foi autorizada ou acrescentada. Relatório: `AUDITORIA_LOTE5_FICHAS_20261015.md`.

## Lote 6 — Mammoth e direitos da arte (15/10/2026)

Nova **referência visual de domínio público documentado** para **AT-015 Mammoth**: [pintura de Charles R. Knight, 1908](https://commons.wikimedia.org/wiki/File:Imperial_mammoth_by_Knight.jpg), [acervo do AMNH](https://digitalcollections.amnh.org/archive/Imperial-Mammoth-2URM1THLZ0V.html). A obra representa um mamute-colombiano (Mammuthus columbi), espécie real correspondente à denominação genérica **Mammoth**, não uma arte oficial de D&D. Sem arte cortada, textos ou moldura; dimensões de **1.009×689 px**, horizonte amplo e figura inteira. Domínio público EUA documentado pelo Wikimedia Commons; no Brasil o autor faleceu em 1953 e aplica-se o prazo geral do art. 41 da Lei 9.610/1998. Revisão jurídica de distribuição para outros países e de uso comercial final ainda pendente.

A antiga **candidata Mammoth rejeitada** continua registrada em `curadoria-artes-20261015.json` → `rejected_history`, e não foi apagada. **Apenas a URL de referência artística mudou**, sem copiar arquivo, alterar mecânicas, interface ou regras. Lote sujeito aos PRs #20–#23 e sua revisão. Consulte `AUDITORIA_LOTE6_MAMMOTH_20261015.md`.

## Dados versionados

| Arquivo local em `data/` | Fonte | Escopo |
|---|---|---|
| `megalista-1320.json` | `operational/research/mega-catalogo-1320-20261014/megalista-1320-distintos-provisorios.csv` | 1.320 registros, com os **19 campos originais** |
| `fichas-607.json` | `SRD_CYCLES/26-30/working/03_CONSTRUTOR/outputs/SRD_FICHAS_607.json` | 607 registros mecânicos **como dados originais**; 108 com texto integral local no snapshot, com status de completude individual preservado |
| `imagens-607.json` | `SRD_CYCLES/26-30/working/03_CONSTRUTOR/outputs/SRD_URLS_IMAGENS_607.csv` | 607 estados e fontes de imagem |
| `auditoria-607.json` | `operational/research/catalog-ledger-20261011-v27/catalog-status.csv` | 607 estados de auditoria |
| `deck-celestial-40.json` | Baralho Celestial versionado no repositório + pesquisas de imagens em 15/10/2026 | 40 IDs de cópia e suportes documentados |
| `deck-aberracao-40.json` | `operational/research/decks/aberracao-40-20261014/cards.csv` | 40 linhas da proposta de Aberrações |
| `suportes-aberracao.json` | `operational/research/decks/aberracao-40-20261014/DECISOES_COMBATE_E_SUPORTES_40_20261015.md` | 40 suportes candidatos, extraídos da tabela de pesquisa |
| `pesquisas-aprofundadas.json` | `operational/research/deep-mechanics/{a,b,c}/records/` | Índice de 395 fichas individuais de aprofundamento |

**Atenção:** a megalista foi publicada no repositório como **provisória**, com identidades/status editoriais distintos dos 607 canônicos. O administrador informou que as 1.320 criaturas podem ser consideradas aprovadas **para seleção em baralhos**; isso não implica homologação das fichas, das imagens e das cartas de suporte. O site preserva o estado documental original, sem sobrescrever fichas/ledger. Alguns IDs têm diferenças de tipo entre megalista e SRD (como Giant Owl); a interface sinaliza divergências.

As artes e os blocos de regras dos livros de terceiros não são redistribuídos indiscriminadamente: são exibidas apenas URLs previamente registradas de referências web. O site inclui os resumos próprios e fichas do SRD presentes no repositório, com vínculo à sua procedência.

## Atualização

Este é um **snapshot** dos dados em 15/10/2026. Atualizações posteriores dos arquivos-fonte exigem atualizar os JSONs estáticos correspondentes. A importação não altera `main`, coleção dos jogadores, estado de partida, cartas aprovadas nem a engine de combate.

### Divergência de identidade preservada

A megalista registra **TF-085 — Animated Instrument, Animated Symphony**, enquanto o conjunto mecânico de 607 contém também **KP-S007 — Animated Instruments (Animated Symphony)**, sem entrada própria na megalista. O site apresenta KP-S007 como **registro alternativo associado para consulta**, com aviso de reconciliação, sem uni-lo mecanicamente ao TF-085. Assim, o catálogo continua exibindo 1.320 criaturas da megalista sem perder o 607º registro de dados.
