# SRD Card Game 607 — Imagens D (entrega parcial atualizada)

## Preflight, lote e isolamento

- Repositório: `george-vepo/SRD-Card-Game-607-Supervisor`.
- Branch de trabalho exclusiva: `chatgpt/srd607-image-assets-d`.
- CSV-base em `a962c48a1169c2ef2be8137715a095a596753b32`: 607 criaturas, 23 imagens originalmente verificadas e 584 ainda não verificadas.
- Recorte autorizado: `pending_images.slice(0,195)`, iniciando em `AT-003` e terminando em `TF-058`.
- Arquivos adicionados/editados exclusivamente em `operational/assets/creature-images/` (14 binários e atualizações nos documentos D nesta continuidade); CSV global, imagens já verificadas e lotes E/F não foram alterados.

## Totais efetivos auditados

- **170 / 195** arquivos de imagem WebP reais registrados no GitHub; **25** IDs pendentes.
- **37.938.196 bytes** persistidos nas 170 imagens.
- Esta continuidade encontrou 156 imagens na branch e acrescentou **14 binários** em dois checkpoints de 7 imagens. Não atribuir a esta execução a aquisição das 156 anteriores.
- O manifesto contém todos os 195 IDs na ordem do CSV, com nome, fonte original, caminho, MIME, dimensões, bytes, SHA-256, Git blob SHA, commit e indicadores de verificação para imagens gravadas.

## Checagens executadas nesta continuidade

1. A listagem de arquivos GitHub já existentes foi comparada ao manifesto: **156 arquivos**, todos em IDs autorizados, com tamanho idêntico ao manifesto; não havia IDs extras fora do lote D no diretório.
2. Os 14 novos binários foram obtidos do repositório público `TheGiddyLimit/homebrew-img`, em arquivos de arte nomeados pela criatura, via `fetch_file(encoding=base64)` e gravados em Git blobs com `encoding=base64`, sem substituir URL por pseudoarquivo.
3. Para cada binário novo, o SHA Git do blob no destino coincidiu com o SHA Git da fonte; após commit e atualização do ref, o arquivo foi relido do GitHub em Base64 e teve SHA-256 recalculado (algoritmo testado com vetor conhecido), tamanho, assinatura RIFF/WEBP, subtipo VP8L/VP8X, tamanho do contêiner e dimensões conferidos.
4. Os **14 WebP novos foram efetivamente renderizados/decodificados a partir do Base64 persistido na branch**, incluindo as quatro mariposas com imagens e hashes diferentes.
5. Para as 156 imagens anteriores, nesta continuidade houve comparação do inventário, tamanho e SHA de blob no GitHub com o manifesto, mas **não houve nova decodificação raster nem recálculo integral do SHA-256 de todas elas**. As flags históricas correspondem aos checkpoints anteriores.
6. É recomendável revisão editorial humana de identidade visual, embora as 14 imagens tenham correspondência nominal explícita nas coleções de fonte. Não usamos imagens de outras criaturas para preencher lacunas.

## Checkpoints novos (limite: 10 imagens por checkpoint)

| Checkpoint | IDs | Imagens | Bytes | Commit com os binários |
|---|---|---:|---:|---|
| 34 | KP-A012, KP-A013, KP-A017, TF-001, TF-004, TF-006, TF-007 | 7 | 1.302.034 | `d77cfcfb0eccf3179fb8837596adb3bf75424b28` |
| 35 | TF-011, TF-014, TF-035, TF-036, TF-037, TF-038, TF-043 | 7 | 816.622 | `a058c30527568184ec72b3fb358744cdef43ad83` |

## Fontes identificadas

- `https://github.com/TheGiddyLimit/homebrew-img` — `img/CCodex/`, `img/CCodex/tokens/` e `img/ToB3/bestiary/tokens/` para 14 novas imagens.
- Fontes das 156 imagens anteriores preservadas individualmente no manifesto, inclusive `5etools-mirror-3/5etools-img` e `TheGiddyLimit/homebrew-img`.

## IDs pendentes (25, sem binário contabilizado)

Motivo: após conferir as coleções pesquisadas, não foi obtida uma imagem específica e distinta para estes IDs que pudesse ser armazenada e verificada no GitHub. Não reutilizar arte de variantes diferentes nem considerar como aquisição uma imagem apenas referenciada por URL.

- `KP-A019` — Crimson Shambler: **PENDENTE** (sem fonte binária própria verificada).
- `KP-S002` — Forest Emperor: **PENDENTE** (sem fonte binária própria verificada).
- `KP-S005` — Yaojing: **PENDENTE** (sem fonte binária própria verificada).
- `KP-S006` — Clockwork Archon: **PENDENTE** (sem fonte binária própria verificada).
- `KP-S007` — Animated Instruments (Animated Symphony): **PENDENTE** (sem fonte binária própria verificada).
- `KP-S014` — Pustulent Shambler: **PENDENTE** (sem fonte binária própria verificada).
- `TF-002` — Ahu-Nixta, Drudge: **PENDENTE** (sem fonte binária própria verificada).
- `TF-008` — Ahu-Nixta, Cataphract: **PENDENTE** (sem fonte binária própria verificada).
- `TF-009` — Astral Devourer: **PENDENTE** (sem fonte binária própria verificada).
- `TF-013` — Yavalnoi: **PENDENTE** (sem fonte binária própria verificada).
- `TF-017` — Ancient Aboleth: **PENDENTE** (sem fonte binária própria verificada).
- `TF-022` — Beetle, Giant Bombardier: **PENDENTE** (sem fonte binária própria verificada).
- `TF-023` — Beetle, Giant Snow: **PENDENTE** (sem fonte binária própria verificada).
- `TF-024` — Beetle, Lantern: **PENDENTE** (sem fonte binária própria verificada).
- `TF-025` — Beetle, Sniffer: **PENDENTE** (sem fonte binária própria verificada).
- `TF-026` — Bilby: **PENDENTE** (sem fonte binária própria verificada).
- `TF-034` — Giant Mongoose: **PENDENTE** (sem fonte binária própria verificada).
- `TF-041` — Giant Water Scorpion: **PENDENTE** (sem fonte binária própria verificada).
- `TF-042` — Akhlut: **PENDENTE** (sem fonte binária própria verificada).
- `TF-045` — Aaxte: **PENDENTE** (sem fonte binária própria verificada).
- `TF-048` — Astri: **PENDENTE** (sem fonte binária própria verificada).
- `TF-049` — Agonized Khyphon: **PENDENTE** (sem fonte binária própria verificada).
- `TF-053` — Thrummren: **PENDENTE** (sem fonte binária própria verificada).
- `TF-055` — Aklea: **PENDENTE** (sem fonte binária própria verificada).
- `TF-057` — Animated Bearskin Rug: **PENDENTE** (sem fonte binária própria verificada).

## Estado final

**ENTREGA PARCIAL, PR EM RASCUNHO.** Não houve merge. O manifesto `manifests/d.json` mantém as 25 pendências abertas sem inventar arquivos. Uma nova aquisição deve utilizar novo checkpoint de até dez imagens e repetir validação de leitura.
