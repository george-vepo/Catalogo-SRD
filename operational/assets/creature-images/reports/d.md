# SRD Card Game 607 — Imagens D (entrega parcial, atualização 2026-10-14)

> **Status vigente: 191/195 imagens verificadas, 4 pendentes, 41.375.642 bytes.** Os checkpoints de 173/195 e 190/195 abaixo são históricos; a atualização mais recente está no final.

## Preflight, lote e isolamento

- Repositório: `george-vepo/SRD-Card-Game-607-Supervisor`.
- Branch de trabalho exclusiva: `chatgpt/srd607-image-assets-d`.
- CSV-base em `a962c48a1169c2ef2be8137715a095a596753b32`: 607 criaturas, 23 imagens originalmente verificadas e 584 ainda não verificadas.
- Recorte autorizado: `pending_images.slice(0,195)`, iniciando em `AT-003` e terminando em `TF-058`.
- Arquivos adicionados/editados exclusivamente em `operational/assets/creature-images/` (17 binários e atualizações nos documentos D nesta continuidade); CSV global, imagens já verificadas e lotes E/F não foram alterados.

## Totais efetivos auditados

- **173 / 195** arquivos de imagem WebP reais registrados no GitHub; **22** IDs pendentes.
- **38.311.386 bytes** persistidos nas 173 imagens.
- Esta continuidade encontrou 156 imagens na branch e acrescentou **17 binários** em quatro checkpoints (7, 7, 2 e 1 imagens). Não atribuir a esta execução a aquisição das 156 anteriores.
- O manifesto contém todos os 195 IDs na ordem do CSV, com nome, fonte original, caminho, MIME, dimensões, bytes, SHA-256, Git blob SHA, commit e indicadores de verificação para imagens gravadas.

## Checagens executadas nesta continuidade

1. A listagem de arquivos GitHub já existentes foi comparada ao manifesto: **156 arquivos**, todos em IDs autorizados, com tamanho idêntico ao manifesto; não havia IDs extras fora do lote D no diretório.
2. Dos 17 novos binários, 15 vieram de `TheGiddyLimit/homebrew-img` e 2 de `chaidgpt/TheBardicLexicon`, em arquivos de arte nomeados pela criatura, via `fetch_file(encoding=base64)` e gravados em Git blobs com `encoding=base64`, sem substituir URL por pseudoarquivo.
3. Para cada binário novo, o SHA Git do blob no destino coincidiu com o SHA Git da fonte; após commit e atualização do ref, o arquivo foi relido do GitHub em Base64 e teve SHA-256 recalculado (algoritmo testado com vetor conhecido), tamanho, assinatura RIFF/WEBP, subtipo VP8/VP8L/VP8X, tamanho do contêiner e dimensões conferidos.
4. Os **14 WebP dos checkpoints 34–35 foram renderizados a partir do Base64 persistido**, incluindo as quatro mariposas com imagens e hashes diferentes. Os outros 3 tiveram arquivo original renderizado e Git blob no destino idêntico ao da origem; a releitura persistida também passou nas verificações de contêiner, dimensões, tamanho e SHA-256.
5. Para as 156 imagens anteriores, nesta continuidade houve comparação do inventário, tamanho e SHA de blob no GitHub com o manifesto, mas **não houve nova decodificação raster nem recálculo integral do SHA-256 de todas elas**. As flags históricas correspondem aos checkpoints anteriores.
6. É recomendável revisão editorial humana de identidade visual, embora as 17 imagens tenham correspondência nominal explícita nas coleções de fonte. Não usamos imagens de outras criaturas para preencher lacunas.

## Checkpoints novos (limite: 10 imagens por checkpoint)

| Checkpoint | IDs | Imagens | Bytes | Commit com os binários |
|---|---|---:|---:|---|
| 34 | KP-A012, KP-A013, KP-A017, TF-001, TF-004, TF-006, TF-007 | 7 | 1.302.034 | `d77cfcfb0eccf3179fb8837596adb3bf75424b28` |
| 35 | TF-011, TF-014, TF-035, TF-036, TF-037, TF-038, TF-043 | 7 | 816.622 | `a058c30527568184ec72b3fb358744cdef43ad83` |

## Checkpoints desta retomada adicional

| Checkpoint | IDs | Bytes | Commit da imagem |
|---|---|---:|---|
| 36 | TF-002, TF-042 | 243.062 | `49b7f2e184838a934a243594f61ad581b08010fe` |
| 37 | TF-045 | 130.128 | `d9c28d7befb03ed8de92035a972b070dc8a08f8d` |

## Fontes identificadas

- `https://github.com/TheGiddyLimit/homebrew-img` — `img/CCodex/`, `img/CCodex/tokens/` e `img/ToB3/bestiary/tokens/` para 15 novas imagens, incluindo `Aatxe.webp` (fonte do ID `TF-045`, grafado `Aaxte` no CSV).
- `https://github.com/chaidgpt/TheBardicLexicon` — imagens próprias de `Ahu-Nixta Drudge` e `Akhlut` (2 novos arquivos).
- Fontes das 156 imagens anteriores preservadas individualmente no manifesto, inclusive `5etools-mirror-3/5etools-img` e `TheGiddyLimit/homebrew-img`.

## IDs pendentes (22, sem binário contabilizado)

Motivo: não foi localizada uma fonte de arte específica suficientemente inequívoca com binário adquirido, salvo quando o nome da imagem correspondia inequivocamente à criatura. Não se consideraram arte de outra variante ou pseudoarquivos.

- `KP-A019` — Crimson Shambler: **PENDENTE** (sem binário específico persistido).
- `KP-S002` — Forest Emperor: **PENDENTE** (sem binário específico persistido).
- `KP-S005` — Yaojing: **PENDENTE** (sem binário específico persistido).
- `KP-S006` — Clockwork Archon: **PENDENTE** (sem binário específico persistido).
- `KP-S007` — Animated Instruments (Animated Symphony): **PENDENTE** (sem binário específico persistido).
- `KP-S014` — Pustulent Shambler: **PENDENTE** (sem binário específico persistido).
- `TF-008` — Ahu-Nixta, Cataphract: **PENDENTE** (sem binário específico persistido).
- `TF-009` — Astral Devourer: **PENDENTE** (sem binário específico persistido).
- `TF-013` — Yavalnoi: **PENDENTE** (sem binário específico persistido).
- `TF-017` — Ancient Aboleth: **PENDENTE** (sem binário específico persistido).
- `TF-022` — Beetle, Giant Bombardier: **PENDENTE** (sem binário específico persistido).
- `TF-023` — Beetle, Giant Snow: **PENDENTE** (sem binário específico persistido).
- `TF-024` — Beetle, Lantern: **PENDENTE** (sem binário específico persistido).
- `TF-025` — Beetle, Sniffer: **PENDENTE** (sem binário específico persistido).
- `TF-026` — Bilby: **PENDENTE** (sem binário específico persistido).
- `TF-034` — Giant Mongoose: **PENDENTE** (sem binário específico persistido).
- `TF-041` — Giant Water Scorpion: **PENDENTE** (sem binário específico persistido).
- `TF-048` — Astri: **PENDENTE** (sem binário específico persistido).
- `TF-049` — Agonized Khyphon: **PENDENTE** (sem binário específico persistido).
- `TF-053` — Thrummren: **PENDENTE** (sem binário específico persistido).
- `TF-055` — Aklea: **PENDENTE** (sem binário específico persistido).
- `TF-057` — Animated Bearskin Rug: **PENDENTE** (sem binário específico persistido).

## Estado final

**ENTREGA PARCIAL — PR #11 EM RASCUNHO.** 173 imagens verificadas no GitHub, 22 pendentes, 38.311.386 bytes. Nenhum merge executado; preservar os IDs não adquiridos.

## Auditoria adicional de integridade — 2026-10-14

- Retomada direta pelo GitHub, **sem V-Bridge**. A branch D e o PR draft #11 já existiam antes desta auditoria; nenhum binário novo foi publicado nesta retomada.
- CSV integral do commit-base novamente lido: 607 linhas, 23 registros com `Imagem` iniciando por `VERIFICADA` e 584 não verificados; `pending_images.slice(0,195)` preservado de `AT-003` a `TF-058`.
- Árvore Git completa do HEAD anterior à auditoria (`85a2968256735bc6cacd50f528057ce215fb8180`): 173 imagens no diretório do lote, sem arquivos extras, com correspondência exata para **todos os 173** registros marcados como armazenados no manifesto, incluindo caminho, Git blob SHA e tamanho. Somatório exato de **38.311.386 bytes**; nenhuma duplicação de SHA-256 registrada no manifesto; 22 IDs pendentes continuam sem arquivo.
- Auditoria de releitura direta GitHub (`fetch_file` em Base64) sobre 10 arquivos distribuídos pelo lote: `AT-003`, `AT-033`, `AT-056`, `AT-083`, `AT-115`, `AT-138`, `KP-A012`, `KP-S017`, `TF-029`, `TF-058`. **10/10 passaram** na comparação SHA-256 recalculado do binário, tamanho em bytes, Git blob SHA, assinatura RIFF/WEBP, tamanho interno do contêiner e dimensões declaradas. O SHA-256 implementado para a leitura foi previamente testado com o vetor padrão `abc`.
- Escopo da auditoria: verificação de estrutura, hashes e metadados em amostra; **não houve nova decodificação raster integral das 173 imagens nesta retomada**, nem revisão humana da identidade visual. Checkpoints e validações raster anteriores permanecem descritos acima.
- Pesquisa adicional de correspondências nominais em fontes abertas e repositórios públicos não resultou em 22 novos arquivos de arte inequivocamente atribuíveis às criaturas. Preservadas as pendências e seus motivos em `d.json` e neste relatório, sem substituir variantes nem fabricar binários.
- Nenhum merge, nenhuma alteração no CSV global, nas 23 imagens verificadas de origem, nem nos lotes E/F.

## Consolidação atualizada — lote D (2026-10-14)

**Estado efetivo:** **190/195** imagens WebP persistidas e verificadas por leitura GitHub, **5 pendentes**, total **41.022.998 bytes**. O CSV do commit-base tem 607 criaturas, 23 verificadas e 584 inicialmente pendentes; seleção D preservada de AT-003 a TF-058. O manifesto contém 195 registros na ordem original, com a origem, MIME, dimensões, bytes, SHA-256, Git blob SHA, commit de origem e indicadores de leitura para cada imagem aceita.

**Checkpoints novos (máximo 10 imagens):**

| Checkpoint | Arquivos reais | Commit Git | Total |
|---|---|---|---:|
| 38 | KP-A019, KP-S002, KP-S005, KP-S006, KP-S014, TF-008, TF-009, TF-013 | `5a451230bfec3bafd5288fdd6253bc37408653ee` | 8 |
| 39 | TF-023, TF-024, TF-025, TF-026, TF-041, TF-048, TF-053, TF-057 | `6b558de9b5b36341e4484076724dab891df1cd9a` | 8 |
| 40 | KP-S007 (Animated Symphony, arte específica de orquestra de instrumentos animados) | `da260b52dc31a54599c13a3424f1eb8615b10f61` | 1 |

As 16 imagens dos checkpoints 38–39 foram publicadas em processo concorrente na branch D; esta auditoria **não reivindica a autoria dessas 16**. Nesta execução, foi publicado exclusivamente o binário de KP-S007 via Git blob em Base64. As 17 imagens foram relidas do GitHub: **17/17** coincidiram com o Git blob SHA identificado nas imagens-fonte, e passaram pela verificação independente de assinatura RIFF/WEBP, comprimento interno, dimensões e SHA-256 recalculado (algoritmo SHA-256 validado com vetor conhecido). A arte KP-S007 foi adicionalmente renderizada. As fontes originais apontam para os arquivos nominativos WebP de `TheGiddyLimit/homebrew`, em `_img/ToB2/creature/` e `_img/ToB3/creature/`. A validação raster completa dos 173 arquivos anteriores não foi repetida nesta execução.

Dois arquivos PNG brevemente publicados para TF-022 e TF-034 foram **excluídos em `4db82f917fd9678a3f1bae9f921e89e3f19ad609`** por serem imagens de placeholder sem ilustração da criatura, e não foram contabilizados.

**Pendências efetivas (sem binário aceito):**

- `TF-017` — Ancient Aboleth: não encontrada arte inequívoca com binário adequado e verificado para esta criatura.
- `TF-022` — Beetle, Giant Bombardier: não encontrada arte inequívoca com binário adequado e verificado para esta criatura.
- `TF-034` — Giant Mongoose: não encontrada arte inequívoca com binário adequado e verificado para esta criatura.
- `TF-049` — Agonized Khyphon: não encontrada arte inequívoca com binário adequado e verificado para esta criatura.
- `TF-055` — Aklea: não encontrada arte inequívoca com binário adequado e verificado para esta criatura.

**Escopo:** nenhum arquivo de imagens E/F, nenhuma das 23 imagens originalmente verificadas e nenhuma linha do CSV global alterados; PR #11 permanece draft e sem merge.

## Continuidade de pesquisa e auditoria — 2026-10-14, checkpoint 41

- **Status atualizado e efetivo: 191/195 imagens persistidas, 4 pendentes, 41.375.642 bytes**. A contagem anterior de 190/195 e os checkpoints 38–40 permanecem acima como histórico, não são o status corrente.
- **Novo arquivo:** `TF-017.webp` (Ancient Aboleth), publicado diretamente no GitHub por blob binário Base64 no checkpoint 41, commit `1b5a1b5232ecb7b697a92907a21b85bb583dc075`. A associação de origem é explícita: `Pjb518/FoundryVTT-Level-Up-Official/packs/monsters/ancient-aboleth.json` atribui `systems/a5e/assets/aboleth.webp` à entrada **Ancient Aboleth**. O arquivo real é `public/assets/aboleth.webp` no mesmo repositório.
- **Integridade confirmada:** SHA Git blob `cafbcd7e2534075f85a5468baa10e3ed1cb63554` idêntico à fonte; leitura de volta do arquivo persistido no GitHub idêntica byte a byte ao Base64 original; formato real WebP, 600×600 px, 352.644 bytes, SHA-256 recalculado `8d44b4d987d207a959485af96ae1d0636ed783f047c4fb741373614762ed9cae`; contêiner RIFF/WEBP e tamanho interno válidos.
- **Ressalva visual relevante:** o catálogo oficial de A5E usa arte de Aboleth para a variante Ancient Aboleth. A arte não foi retirada de outra espécie e é distinta do arquivo `AT-003.webp`; contudo, **não é uma ilustração exclusiva da forma ancestral**. Revisão editorial recomendada se o jogo exigir distinção de idade explicitamente visível.

### Quatro pendências e motivos concretos

- `TF-022` — **Beetle, Giant Bombardier**: A criatura Giant Bombardier Beetle consta no Tome of Beasts 2, mas não foi localizado um binário inequivocamente correspondente em repositório GitHub acessível para armazenamento; arquivos PNG anteriormente encontrados foram excluídos por serem placeholders. Há uma ilustração externa de besouro bombardeiro gigante, mas ela não foi adquirida nem persistida neste GitHub.
- `TF-034` — **Giant Mongoose**: Giant Mongoose consta no Tome of Beasts 2 / Margreve Player's Guide. A coleção nominal '_img/ToB2/creature/' não contém arte específica sob o nome Giant Mongoose; não substituir por foto de mangusto comum ou outro animal.
- `TF-049` — **Agonized Khyphon**: Agonized Khyphon consta em 'To Save A Kingdom'; a página A5E tem descrição visual detalhada de bandagens, olhos, pus e aura magenta, porém não disponibiliza a ilustração específica. O registro Foundry correspondente usa 'icons/svg/mystery-man.svg', que é placeholder e não uma imagem válida.
- `TF-055` — **Aklea**: Aklea é uma variante feminina nomeada de Empyrean, filha de um deus da guerra. A página A5E associa uma ilustração de tiefling guerreira, e o Foundry associa um avatar masculino genérico de empyrean; nenhuma representa adequadamente Aklea, então ambas rejeitadas.

As fontes de definição das criaturas foram confirmadas no catálogo Kobold Press (para besouro e mangusto) e no A5E (para Khyphon e Aklea), mas páginas descritivas e URLs externas isoladas **não foram contabilizadas como aquisição de binário**. Não houve substituição por sprites genéricos, placeholders ou criaturas diferentes.

O PR continua em **DRAFT**, sem merge. Não houve modificação do CSV global, das 23 imagens previamente verificadas ou dos lotes E e F.
