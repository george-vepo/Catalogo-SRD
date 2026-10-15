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
- `data/fichas-referencia-verificadas.json`: **6 fichas mecânicas de referência** recuperadas dos JSONs detalhados do lote E (TF-059, TF-060, TF-061, TF-063, TF-064 e TF-065). O site exibe a referência detalhada separadamente, sem tratar a ficha como nova homologação do jogo.

Atualmente, **35 das 1.320** espécies têm URL de imagem exibível a partir de qualquer uma das fontes registradas no site; **1.285 ainda não têm**. Arquivos binários não revisados do repositório **não são aceitos automaticamente**. Consulte o relatório `AUDITORIA_IMAGENS_FICHAS_20261015.md` para contagens, rejeições e pendências. 

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
