## Evidência de persistência pós-checkpoint — 14/10/2026

Na branch B, TF-351, TF-384, TF-389 e TF-393 foram individualmente reabertos após [`940cfbad52bf`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/940cfbad52bf82043be96ab660027c48325db321). O GitHub confirmou **4/4 assinaturas WebP, SHA Git e tamanhos**, com identidade de blob igual à fonte. A árvore contém **112 arquivos binários reais**, sem discrepância com os registros do manifesto; faltam 20 imagens. Os dois Rust Monsters usam a mesma imagem genérica como no módulo fonte, com revisão de identidade da variante pendente; licenças restritas a uso não comercial.

---

## Quatro WebPs reais adicionais — 14/10/2026 — imagens 112/132

Arquivos gravados: [TF-351](TF-351.webp), [TF-384](TF-384.webp), [TF-389](TF-389.webp), [TF-393](TF-393.webp). Fontes editoriais do módulo A5E confirmam que os atores das variantes apontam às imagens listadas; contudo **não são artes exclusivas da variante**. TF-384 e TF-389 compartilham o mesmo blob `327bdaa2d6b66ddae5701b064e32c276d0093056`, por decisão do próprio módulo A5E, e devem receber artes próprias se a diferenciação artística for requisito de publicação. TF-351 e TF-393 usam ogro/minotauro sem identificação exclusiva. Não foi importada a manticore de TF-381 por erro de identidade.

**Licença e saída comercial bloqueadas:** [README oficial do módulo A5E](https://github.com/Pjb518/FoundryVTT-Level-Up-Official/blob/main/README.md) concede uso das artes de `public/assets` apenas para fins não comerciais. Hashes, origem, dimensões e notas individuais foram registrados. Nenhum arquivo fictício, placeholder ou URL isolada foi aceito.

**20 imagens ainda sem binário.** Confirmar SHA e tamanho após persistência GitHub.

---

## Releitura física confirmada — 14/10/2026

**108/132 imagens são arquivos binários efetivamente presentes**, com Git SHA e tamanho de cada arquivo da árvore Git iguais aos registros do manifesto. As quatro imagens A5E do checkpoint [`0e0ed70e2f66`](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/0e0ed70e2f665f3afc61acca208ad4779161a362) foram individualmente reabertas em Base64, com assinatura RIFF/WEBP e bytes confirmados. Restam **24 arquivos sem binário correspondente** no diretório B.

**Ressalva obrigatória:** integridade física ≠ comprovação de identidade artística exclusiva, licença comercial ou homologação visual. As quatro imagens A5E têm restrição de **uso não comercial** informada na fonte; avaliação de direitos de todos os recursos permanece necessária antes de uso final.

---

## Checkpoint imagens B — 14/10/2026 — quatro assets oficiais A5E com uso não comercial

**4 arquivos reais de origem** da [implementação oficial do A5E para Foundry](https://github.com/Pjb518/FoundryVTT-Level-Up-Official), associados por nome e `img` no JSON do ator correspondente. Copiados sem recodificar; verificação pré-gravação: 4 WebPs com assinatura RIFF/WEBP/VP8X, tamanhos internos iguais aos bytes, SHA-256, dimensões e Git SHA iguais aos de origem.

| ID | Arquivo B | Imagem no repositório-fonte | Ator que usa a arte | Dimensões | Bytes | SHA-256 |
|---|---|---|---|---:|---:|---|
| TF-094 | [TF-094.webp](TF-094.webp) | [river-dragon.webp](https://github.com/Pjb518/FoundryVTT-Level-Up-Official/blob/d986361631f97f248f57b8c5b3c090ba770e0024/public/assets/river-dragon.webp) | [Adult River Dragon](https://github.com/Pjb518/FoundryVTT-Level-Up-Official/blob/d986361631f97f248f57b8c5b3c090ba770e0024/packs/monsters/adult-river-dragon.json) | 600×600 | 398578 | `4d11aaea00b1ee3850acf74a422b5dbd76d5518ee322562f4822c99fa61db6b5` |
| TF-095 | [TF-095.webp](TF-095.webp) | [sapphire-dragon.webp](https://github.com/Pjb518/FoundryVTT-Level-Up-Official/blob/d986361631f97f248f57b8c5b3c090ba770e0024/public/assets/sapphire-dragon.webp) | [Adult Sapphire Dragon](https://github.com/Pjb518/FoundryVTT-Level-Up-Official/blob/d986361631f97f248f57b8c5b3c090ba770e0024/packs/monsters/adult-sapphire-dragon.json) | 600×600 | 393128 | `83dce3faaec07da48c5f6493f69c51f6ed76fced0a424986de2736c83f6e4aca` |
| TF-355 | [TF-355.webp](TF-355.webp) | [hill-giant.webp](https://github.com/Pjb518/FoundryVTT-Level-Up-Official/blob/d986361631f97f248f57b8c5b3c090ba770e0024/public/assets/hill-giant.webp) | [Hill Giant Chief](https://github.com/Pjb518/FoundryVTT-Level-Up-Official/blob/d986361631f97f248f57b8c5b3c090ba770e0024/packs/monsters/hill-giant-chief.json) | 900×900 | 708384 | `2dd2e9e79dd754467e38ca3f04232038c8dab161c0bf28d6eab8f1d3bce53793` |
| TF-361 | [TF-361.webp](TF-361.webp) | [black-pudding.webp](https://github.com/Pjb518/FoundryVTT-Level-Up-Official/blob/d986361631f97f248f57b8c5b3c090ba770e0024/public/assets/black-pudding.webp) | [Elder Black Pudding](https://github.com/Pjb518/FoundryVTT-Level-Up-Official/blob/d986361631f97f248f57b8c5b3c090ba770e0024/packs/monsters/elder-black-pudding.json) | 600×600 | 342354 | `4722cf84e9279715377ea95471b509d5088988ebab699f0fe56e6998a0f8f1f2` |

**Direitos: restritos a uso não comercial**, conforme [README da fonte](https://github.com/Pjb518/FoundryVTT-Level-Up-Official/blob/main/README.md). Não autoriza aprovação automática de comercialização, licenciamento do produto final ou reprodução sem revisão jurídica. Não se confundem com obras oficialmente liberadas pelo A5ESRD. Imagens associadas a mais de uma idade/variante não comprovam desenho exclusivo daquela ficha. Finalização artística e legal pendentes.

**Cobertura física prevista:** 108/132, ainda 24 arquivos ausentes. **Não foram importados sprites genéricos de 32×32 pixels** de TF-355, TF-361 e TF-395 encontrados em F por inadequação para card art final. A correspondência dos hashes no GitHub destino precisa de confirmação após publicação deste checkpoint.

---

## Auditoria visual B — 14/10/2026 — 104 imagens físicas, 28 pendentes

**Conferência no GitHub após [commit 5dd0a6bccac2](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/commit/5dd0a6bccac2c057fe4365bdbf278e1cadfe97c1):** 104 arquivos binários foram encontrados fisicamente na árvore Git e seus SHAs/tamanhos coincidem com os campos do manifesto; TF-327, TF-344, TF-399 foram reabertos em Base64 e as assinaturas WebP/JPEG confirmadas. Mesmo Git SHA de origem na branch F garante identidade dos blobs (sem recodificação). Nenhuma imagem ficou substituída apenas por URL, texto Base64 ou placeholder.

**28 imagens restantes (IDs reais):** TF-303, TF-326, TF-335, TF-336, TF-341, TF-342, TF-351, TF-353, TF-355, TF-356, TF-358, TF-361, TF-370, TF-379, TF-381, TF-384, TF-386, TF-389, TF-393, TF-395, TF-397, TF-398, TF-402, TF-405, TF-408, TF-411, TF-094, TF-095.

**Investigação:** em snapshots das branches D (`c6129862bfe2`), E (`6c12c9153163`) e F (`6ff8218b9e9`), nenhum dos 28 IDs restantes possui arquivo correspondente em `operational/assets/creature-images/`. Será necessária nova fonte legitimamente reutilizável ou ilustração original, seguida de persistência binária, hashes, dimensões, licença e revisão de identidade. A adequação visual de TF-327/344/399 é preliminar, e direitos/atribuição dos recursos não foram homologados. Não copiar conteúdo incerto automaticamente.

---

## Checkpoint de imagens B — 14/10/2026 — 104/132 binários, 28 pendentes

Três imagens reais **reutilizadas por SHA Git idêntico da branch F**, sem gerar placeholders ou links em lugar do arquivo. Fontes, bytes, dimensões, formato, SHA-256 de origem e licença pendente constam no manifesto.

| ID | Criatura | Arquivo real B | Origem | Bytes | Dimensões | SHA Git |
|---|---|---|---|---:|---|---|
| TF-327 | Azer Forgemaster | [WEBP](TF-327.webp) | [Fonte](https://github.com/Pjb518/FoundryVTT-Level-Up-Official/blob/main/public/assets/azer.webp) | 113414 | 300×300 | `a0a515c1cd74460e7f111b2213b7e65fd5230a8c` |
| TF-344 | Pumpkin King | [WEBP](TF-344.webp) | [Fonte](https://github.com/GNchoo/dicekeep-art/blob/HEAD/casual/bosses/pumpkin-king.webp) | 116036 | 360×279 | `e8c7875ec2c764636c3f5ba50762c5be9367c5a4` |
| TF-399 | Mari Lwyd | [JPG](TF-399.jpg) | [Fonte](https://github.com/WaffleFlayer/winter-ornaments/blob/HEAD/images/mari-lwyd.jpg) | 188641 | 1024×1024 | `f854d21482e9bb530c1c2983c6c657e96a0c7669` |

**Ressalvas:** TF-344 é um sprite estilizado de resolução moderada; TF-399 usa arte simplificada; TF-327 usa arte de azer com martelo, associada à identidade Forgemaster. Não foi certificada adequação editorial, licença de republicação nem homogeneidade estética. SHA-256 e correspondência byte a byte com os objetos F documentados no [manifesto](manifest.json). A persistência precisa de readback GitHub após commit.

---

## Checkpoint 14/10/2026 — 101/132 arquivos binários reais verificados

A partir desta continuação, **101 imagens** estão fisicamente no diretório B, com **31 ainda faltantes**. Importada a ilustração [TF-338 Somberweave](TF-338.webp) do lote F, por cópia do objeto Git binário real SHA `7345296a5c5f285194a5072edbe99486e5ca9608`, WebP 63.466 bytes, dimensões 850×758 e SHA-256 no manifesto `c285a415677fcd7bfccaebbb6f2cc1776cc7f993f90f0b02ce4f846916fc32fc`. Foi conferido o readback do objeto Git e a assinatura WebP. A fonte gráfica está identificada em *Book of Ebon Tides* como Somberweave; a adequação à edição de *Tome of Beasts 2* ainda exige homologação de identidade da imagem. Não foi usada URL como substituto do arquivo, e os demais 31 IDs permanecem pendentes.

[Manifesto com origem e hashes](manifest.json) · [Manifesto de fichas](../records/manifest.json) · [PR #6](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/pull/6). Relatos anteriores abaixo são checkpoints históricos.

---

## Atualização 14/10/2026 — 100/132 binários reais no grupo B

**Cinco novas imagens foram gravadas e verificadas no GitHub; faltam 32 de 132.** Todas estas cinco foram copiadas como objetos Git binários reais da branch `chatgpt/srd607-image-assets-f` e relidas na branch B. Verificados: SHA do blob idêntico à fonte, quantidade de bytes e assinatura WebP. Metadados SHA-256 e links à ilustração original estão no [manifesto](manifest.json).

| ID | Criatura | Arquivo binário | Bytes | Dimensões | Git blob SHA |
|---|---|---|---:|---|---|
| TF-373 | Kobold, Wizard | [WebP](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-373.webp) | 169364 | 705×1015 | `f9a1425c5a2a6efef01eea63969a46cc190a4c4d` |
| TF-396 | Skeleton, Clacking | [WebP](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-396.webp) | 202888 | 833×1215 | `14fec1a4cb7ba2e76c8e24b530e49dab96be6e3b` |
| TF-403 | Lich, Hierophant | [WebP](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-403.webp) | 191576 | 861×1188 | `435e829ce72cbfb4ad477766e6abf788d21c69e7` |
| TF-407 | Lich, Pact | [WebP](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-407.webp) | 211940 | 920×1168 | `cbeb7fce6cb45fa770a387c5e9493f0e16ed9264` |
| TF-410 | Fungi, Wirbeln | [WebP](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-410.webp) | 182470 | 871×972 | `24a662a994094e7f7195f4821e078f475fb960cc` |

O registro das 32 imagens faltantes permanece explicitamente pendente, sem substituições artificiais, links disfarçados de arquivo ou imagens inventadas.

---

## Atualização 14/10/2026 — três imagens físicas importadas

**95/132 imagens binárias reais, 37 pendentes.** Nesta execução foram adicionadas e relidas: 

| ID | Criatura | Arquivo real | Tamanho | Blob SHA verificado |
|---|---|---|---:|---|
| TF-069 | Clockwork Servant | [TF-069.webp](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-069.webp) | 86490 | `6198f481b27aa834977ddf74263b96a9a1534322` |
| TF-099 | Ankou Soul Herald | [TF-099.webp](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-099.webp) | 300594 | `b8e866d5dc3160f0b60d6a856090433ef6658759` |
| TF-364 | Kapi | [TF-364.webp](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-364.webp) | 82158 | `5089690fa8cefa644b5bdfe20fd456016b72dcf1` |

Origem: `TheGiddyLimit/homebrew-img/img/CCodex/tokens/`. O Git confirmou SHA dos blobs binários idênticos ao arquivo de origem. As seções abaixo documentam os 92 arquivos incorporados anteriormente e constituem histórico de 13/10/2026.

# Imagens reais — lote B

**92/132 imagens binárias copiadas e verificadas na branch B; 40 pendentes.** Cada imagem possui Git blob SHA idêntico ao arquivo físico de origem (branches E/F), tamanho e caminho conferidos na nova branch.
Branch chatgpt/srd607-deep-mechanics-b, sem alterações globais.
[Manifesto por criatura](manifest.json)

## Arquivos incorporados (92)

| ID | Arquivo binário | Fonte/branch | Bytes |
|---|---|---|---:|
| TF-302 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-302.webp) | chatgpt/srd607-image-assets-f | 84230 |
| TF-304 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-304.webp) | chatgpt/srd607-image-assets-f | 264428 |
| TF-305 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-305.webp) | chatgpt/srd607-image-assets-f | 104226 |
| TF-306 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-306.webp) | chatgpt/srd607-image-assets-f | 144864 |
| TF-309 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-309.webp) | chatgpt/srd607-image-assets-f | 73990 |
| TF-312 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-312.webp) | chatgpt/srd607-image-assets-f | 158582 |
| TF-316 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-316.webp) | chatgpt/srd607-image-assets-f | 82030 |
| TF-317 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-317.webp) | chatgpt/srd607-image-assets-f | 85396 |
| TF-318 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-318.webp) | chatgpt/srd607-image-assets-f | 275194 |
| TF-319 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-319.webp) | chatgpt/srd607-image-assets-f | 197712 |
| TF-320 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-320.webp) | chatgpt/srd607-image-assets-f | 218342 |
| TF-325 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-325.webp) | chatgpt/srd607-image-assets-f | 145090 |
| TF-328 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-328.webp) | chatgpt/srd607-image-assets-f | 77614 |
| TF-329 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-329.webp) | chatgpt/srd607-image-assets-f | 85414 |
| TF-330 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-330.webp) | chatgpt/srd607-image-assets-f | 126638 |
| TF-331 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-331.webp) | chatgpt/srd607-image-assets-f | 74908 |
| TF-332 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-332.webp) | chatgpt/srd607-image-assets-f | 116472 |
| TF-333 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-333.webp) | chatgpt/srd607-image-assets-f | 92384 |
| TF-334 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-334.webp) | chatgpt/srd607-image-assets-f | 116728 |
| TF-339 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-339.webp) | chatgpt/srd607-image-assets-f | 111352 |
| TF-340 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-340.webp) | chatgpt/srd607-image-assets-f | 93256 |
| TF-343 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-343.webp) | chatgpt/srd607-image-assets-f | 103652 |
| TF-345 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-345.webp) | chatgpt/srd607-image-assets-f | 169384 |
| TF-346 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-346.webp) | chatgpt/srd607-image-assets-f | 116080 |
| TF-347 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-347.webp) | chatgpt/srd607-image-assets-f | 88368 |
| TF-348 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-348.webp) | chatgpt/srd607-image-assets-f | 86812 |
| TF-349 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-349.webp) | chatgpt/srd607-image-assets-f | 100050 |
| TF-350 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-350.webp) | chatgpt/srd607-image-assets-f | 87682 |
| TF-363 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-363.webp) | chatgpt/srd607-image-assets-f | 82596 |
| TF-365 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-365.webp) | chatgpt/srd607-image-assets-f | 86494 |
| TF-366 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-366.webp) | chatgpt/srd607-image-assets-f | 153172 |
| TF-367 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-367.webp) | chatgpt/srd607-image-assets-f | 89006 |
| TF-368 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-368.webp) | chatgpt/srd607-image-assets-f | 227612 |
| TF-369 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-369.webp) | chatgpt/srd607-image-assets-f | 262474 |
| TF-372 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-372.webp) | chatgpt/srd607-image-assets-f | 63606 |
| TF-378 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-378.webp) | chatgpt/srd607-image-assets-f | 110202 |
| TF-382 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-382.webp) | chatgpt/srd607-image-assets-f | 87404 |
| TF-385 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-385.webp) | chatgpt/srd607-image-assets-f | 158980 |
| TF-388 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-388.webp) | chatgpt/srd607-image-assets-f | 106718 |
| TF-392 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-392.webp) | chatgpt/srd607-image-assets-f | 79832 |
| TF-394 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-394.webp) | chatgpt/srd607-image-assets-f | 102362 |
| TF-401 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-401.webp) | chatgpt/srd607-image-assets-f | 109534 |
| TF-406 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-406.webp) | chatgpt/srd607-image-assets-f | 155278 |
| TF-409 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-409.png) | chatgpt/srd607-image-assets-f | 25756 |
| TF-060 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-060.webp) | chatgpt/srd607-image-assets-e | 74578 |
| TF-061 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-061.webp) | chatgpt/srd607-image-assets-e | 65732 |
| TF-062 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-062.webp) | chatgpt/srd607-image-assets-e | 70904 |
| TF-063 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-063.webp) | chatgpt/srd607-image-assets-e | 103266 |
| TF-064 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-064.webp) | chatgpt/srd607-image-assets-e | 102796 |
| TF-065 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-065.webp) | chatgpt/srd607-image-assets-e | 78038 |
| TF-066 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-066.webp) | chatgpt/srd607-image-assets-e | 48670 |
| TF-067 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-067.webp) | chatgpt/srd607-image-assets-e | 117610 |
| TF-068 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-068.webp) | chatgpt/srd607-image-assets-e | 133620 |
| TF-070 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-070.jpg) | chatgpt/srd607-image-assets-e | 51722 |
| TF-071 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-071.webp) | chatgpt/srd607-image-assets-e | 43552 |
| TF-072 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-072.webp) | chatgpt/srd607-image-assets-e | 56986 |
| TF-074 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-074.webp) | chatgpt/srd607-image-assets-e | 112080 |
| TF-075 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-075.webp) | chatgpt/srd607-image-assets-e | 197980 |
| TF-077 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-077.jpg) | chatgpt/srd607-image-assets-e | 45935 |
| TF-078 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-078.webp) | chatgpt/srd607-image-assets-e | 238608 |
| TF-079 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-079.webp) | chatgpt/srd607-image-assets-e | 73812 |
| TF-080 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-080.webp) | chatgpt/srd607-image-assets-e | 107518 |
| TF-081 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-081.webp) | chatgpt/srd607-image-assets-e | 149206 |
| TF-082 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-082.webp) | chatgpt/srd607-image-assets-e | 222186 |
| TF-083 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-083.webp) | chatgpt/srd607-image-assets-e | 246980 |
| TF-084 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-084.webp) | chatgpt/srd607-image-assets-e | 473666 |
| TF-085 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-085.webp) | chatgpt/srd607-image-assets-e | 162844 |
| TF-087 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-087.webp) | chatgpt/srd607-image-assets-e | 120004 |
| TF-089 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-089.webp) | chatgpt/srd607-image-assets-e | 146844 |
| TF-090 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-090.jpg) | chatgpt/srd607-image-assets-e | 75629 |
| TF-091 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-091.webp) | chatgpt/srd607-image-assets-e | 181394 |
| TF-097 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-097.webp) | chatgpt/srd607-image-assets-e | 365288 |
| TF-100 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-100.webp) | chatgpt/srd607-image-assets-e | 202858 |
| TF-101 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-101.jpg) | chatgpt/srd607-image-assets-e | 48109 |
| TF-102 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-102.webp) | chatgpt/srd607-image-assets-e | 93876 |
| TF-103 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-103.webp) | chatgpt/srd607-image-assets-e | 64532 |
| TF-104 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-104.webp) | chatgpt/srd607-image-assets-e | 225554 |
| TF-105 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-105.webp) | chatgpt/srd607-image-assets-e | 25076 |
| TF-106 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-106.webp) | chatgpt/srd607-image-assets-e | 85334 |
| TF-107 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-107.webp) | chatgpt/srd607-image-assets-e | 36492 |
| TF-108 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-108.webp) | chatgpt/srd607-image-assets-e | 120238 |
| TF-109 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-109.webp) | chatgpt/srd607-image-assets-e | 57066 |
| TF-110 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-110.webp) | chatgpt/srd607-image-assets-e | 61242 |
| TF-111 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-111.webp) | chatgpt/srd607-image-assets-e | 75726 |
| TF-112 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-112.webp) | chatgpt/srd607-image-assets-e | 74098 |
| TF-113 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-113.webp) | chatgpt/srd607-image-assets-e | 70112 |
| TF-114 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-114.webp) | chatgpt/srd607-image-assets-e | 75940 |
| TF-115 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-115.webp) | chatgpt/srd607-image-assets-e | 33706 |
| TF-116 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-116.jpg) | chatgpt/srd607-image-assets-e | 53166 |
| TF-117 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-117.webp) | chatgpt/srd607-image-assets-e | 148180 |
| TF-118 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-118.webp) | chatgpt/srd607-image-assets-e | 68188 |
| TF-119 | [Abrir imagem](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/blob/chatgpt/srd607-deep-mechanics-b/operational/research/deep-mechanics/b/images/TF-119.webp) | chatgpt/srd607-image-assets-e | 250012 |

## Faltam imagens (40)

TF-303, TF-326, TF-327, TF-335, TF-336, TF-338, TF-341, TF-342, TF-344, TF-351, TF-353, TF-355, TF-356, TF-358, TF-361, TF-364, TF-370, TF-373, TF-379, TF-381, TF-384, TF-386, TF-389, TF-393, TF-395, TF-396, TF-397, TF-398, TF-399, TF-402, TF-403, TF-405, TF-407, TF-408, TF-410, TF-411, TF-069, TF-094, TF-095, TF-099.

Estes 40 IDs não foram substituídos por URLs ou placeholders. A pesquisa mecânica das 132 criaturas é independente da cobertura visual. Este relatório não declara conclusão das 132 fichas.
