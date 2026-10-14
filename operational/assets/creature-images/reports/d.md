# SRD Card Game 607 — Imagens D (relatório de entrega parcial)

## Preflight, partição e isolamento

- Repositório: `george-vepo/SRD-Card-Game-607-Supervisor`; branch exclusiva `chatgpt/srd607-image-assets-d`.
- Commit-base do CSV: `a962c48a1169c2ef2be8137715a095a596753b32`.
- CSV: `operational/research/catalog-ledger-20261011-v27/catalog-status.csv`.
- 607 linhas de criaturas, 23 imagens originalmente marcadas como VERIFICADA e 584 pendentes no CSV-base.
- Seleção exclusiva: `pending_images.slice(0,195)`, começando `AT-003` e terminando `TF-058`, na ordem do CSV.
- Nenhum arquivo fora de `operational/assets/creature-images/` foi alterado; não foi realizado merge, nem escrita no CSV ou nos lotes E/F.

## Resultado auditado

- **150 de 195** imagens binárias reais persistidas no GitHub; **45 pendentes**.
- **34.524.706 bytes** persistidos em arquivos WebP no conjunto D.
- Dos 150 binários, **95** já existiam na branch ao retomar este trabalho e **55** foram adquiridos nesta continuação em 19 checkpoints adicionais.
- Arquivos individuais: `operational/assets/creature-images/<ID>.webp`; um arquivo por ID verificado.
- A auditoria cruzou diretório GitHub com manifesto: 150 arquivos encontrados, todos com Git blob SHA e tamanho idênticos aos declarados, 150 hashes SHA-256 distintos.
- Manifesto detalhado: `operational/assets/creature-images/manifests/d.json` contém os 195 IDs na ordem original, com fonte, MIME real, dimensões, tamanho, SHA-256, commit e resultado de verificação, ou status pendente.

## Verificação efetivamente executada

1. Para os 55 novos arquivos, obtivemos o arquivo binário original em Base64 via GitHub do repositório público identificado no campo `source_url` e criamos Git blobs binários usando `encoding=base64`.
2. Cada Git blob resultante teve SHA Git comparado ao SHA do arquivo na fonte. Os blobs foram incorporados em Git trees e commits individuais de até três imagens por checkpoint (limite exigido: dez).
3. Após cada commit e atualização condicional do ref, recuperamos do GitHub os arquivos gravados em Base64 e verificamos igualdade de bytes com a origem, integridade dos blobs, quantidade de bytes, assinatura RIFF/WEBP, subtipo VP8/VP8L/VP8X e dimensões reais.
4. Calculamos o SHA-256 dos bytes recuperados e registramos no manifesto com o commit que contém cada arquivo; o algoritmo SHA-256 passou teste conhecido antes de cada lote de verificação.
5. Os 95 arquivos preexistentes já possuíam metadados de verificação no manifesto; nesta continuação, seus SHA Git e bytes foram comparados à listagem persistida do GitHub. Não houve recálculo integral de SHA-256 desses 95.
6. **Limitação:** a verificação nesta execução validou o contêiner e os bytes persistidos, não executou um decodificador raster completo para todos os arquivos. A identidade visual e a qualidade editorial também ainda requerem revisão humana.

## Fontes reais usadas

- [5etools-mirror-3/5etools-img](https://github.com/5etools-mirror-3/5etools-img), bestiary/XMM e tokens/XMM (arte identificada por criatura, incluindo estágios de dragões com Git blobs diferentes).
- [TheGiddyLimit/homebrew-img](https://github.com/TheGiddyLimit/homebrew-img), imagens e tokens das coleções ToB1-2023 e ToB3. Os nomes de algumas fontes invertem a ordem do catálogo sem mudar a criatura (por exemplo, `Siege Archon` / `Archon, Siege`).
- Os registros do manifesto apontam para URLs específicas e os commits dos arquivos. Não foram aceitos placeholders, URLs como substitutas de binários, nem imagens reaproveitadas de outra criatura.

## Checkpoints desta continuação

| Checkpoint | IDs persistidos | Commit da imagem |
|---:|---|---|
| 13 | KP-A003, KP-A006, KP-A008 | `8b5edf13322d9f066e8b1bac3f9a196203a64ac8` |
| 14 | KP-A011, KP-S008, KP-S009 | `12f6e02e57602b9da0c6ef9b6672c2a1b69de5b0` |
| 15 | KP-S010, KP-S012, KP-S015 | `878f4ee5e2d975244f8a3851116202bdef1ed7c0` |
| 16 | KP-S016, KP-S018, TF-005 | `caba7958a054361f2bf52a5d4e54143a66387f65` |
| 17 | TF-019, TF-020, TF-021 | `5a2879b61dcc05695f680f1a4b8b358e2806f3ae` |
| 18 | TF-027, TF-028, TF-029 | `726b807fee1314b374a06dc50f22784d984ae85a` |
| 19 | TF-030, TF-031, TF-032 | `4e94a81cff9ac288c10e63d45ebe21f4bc245ccf` |
| 20 | TF-033, TF-039, TF-040 | `cd54bf305b1263729aff9c9fcf19074718b9eb13` |
| 21 | TF-046, TF-047, TF-050 | `c8b22982b1d23611af5948b1faaf931c5a7a78b3` |
| 22 | TF-051, TF-052, TF-058 | `27a97aa91dc6cdb73330cf88592a4ae119f14dc8` |
| 23 | KP-A005, KP-A009, KP-A020 | `7f41a7e069f027030d79228dfafe0d00d212cbb6` |
| 24 | TF-054, KP-A010, KP-S013 | `da64dd14364cd9700c829bc6cd9be1c406df9bef` |
| 25 | AT-012, AT-014, AT-015 | `b53f6afa6770139b94c1740942e10c1b24299a62` |
| 26 | AT-016, AT-046, AT-047 | `b6d38f4d8baf52eda7b1b05dbd33cb99a72ea679` |
| 27 | AT-048, AT-050, AT-051 | `a4d979f1752628fcb4f241bf5a4f988d1d0d00b6` |
| 28 | AT-052, AT-053, AT-054 | `cc4e0e0aeae5afff80e3fd1f64b4261cb276ea0f` |
| 29 | AT-055, AT-056, AT-057 | `6eeb36b78e71324058b57ef0d2f91bbad1d48458` |
| 30 | AT-073, AT-096, AT-098 | `aa6ac5e76270d5c78b9587c02432908b1a888332` |
| 31 | AT-099 | `f73d83d05eb978e35b85ea3074c71485709abd37` |

## 45 pendências (sem binário contabilizado)

Motivo: não foi localizado e validado, entre as fontes examinadas nesta execução, um arquivo com representação suficientemente inequívoca de cada criatura pendente para armazenamento. Algumas alternativas encontradas pertenciam a outras variantes ou usavam uma arte genérica já aplicada a outra criatura; elas não foram contadas. A lista abaixo preserva os IDs reais.

### KP (15)

- `KP-A001` — Crystalline Monolith: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-A007` — Crinaea: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-A012` — Bearfolk Chieftain: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-A013` — Cultist, Psychophant: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-A014` — Tree Skinner: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-A015` — Corrupted Pixie: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-A016` — Tidehunter: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-A017` — Crimson Mist: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-A018` — Glacial Corrupter: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-A019` — Crimson Shambler: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-S002` — Forest Emperor: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-S005` — Yaojing: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-S006` — Clockwork Archon: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-S007` — Animated Instruments (Animated Symphony): **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `KP-S014` — Pustulent Shambler: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.

### TF (30)

- `TF-001` — Ahu-Nixta: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-002` — Ahu-Nixta, Drudge: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-004` — Astral Snapper: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-006` — Xenabsorber: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-007` — Yann-An-Oed: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-008` — Ahu-Nixta, Cataphract: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-009` — Astral Devourer: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-011` — Child of Yggdrasil: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-013` — Yavalnoi: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-014` — Ziphius: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-017` — Ancient Aboleth: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-022` — Beetle, Giant Bombardier: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-023` — Beetle, Giant Snow: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-024` — Beetle, Lantern: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-025` — Beetle, Sniffer: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-026` — Bilby: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-034` — Giant Mongoose: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-035` — Giant Moth: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-036` — Giant Moth, Rimewing: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-037` — Giant Moth, Shockwing: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-038` — Giant Moth, Sootwing: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-041` — Giant Water Scorpion: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-042` — Akhlut: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-043` — Oliphaunt: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-045` — Aaxte: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-048` — Astri: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-049` — Agonized Khyphon: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-053` — Thrummren: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-055` — Aklea: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.
- `TF-057` — Animated Bearskin Rug: **PENDENTE**; fonte específica ainda não adquirida e verificada no GitHub.

## Estado da entrega

**PARCIAL.** O PR permanece em **rascunho** para `chatgpt/srd607-research-checkpoints-20261011`. Nenhum merge foi executado. As imagens restantes exigem identificação e aquisição real do binário, sem substituição inventada.
