# SRD Card Game 607 — Imagens D (entrega parcial atualizada)

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
