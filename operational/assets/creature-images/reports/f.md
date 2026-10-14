# SRD Card Game 607 — imagens e fichas, lote F (progresso real)

## Resumo verificavel

- Branch: `chatgpt/srd607-image-assets-f`; PR #5 em rascunho, sem merge; commit-base `a962c48a1169c2ef2be8137715a095a596753b32`.
- Selecao exatamente `pending_images.slice(390,584)`: **194 IDs**, em ordem de CSV `operational/research/catalog-ledger-20261011-v27/catalog-status.csv`.
- **67 imagens reais** gravadas no GitHub, todas recuperadas por arquivo e validadas por identidade com a fonte no respectivo checkpoint; listagem atual do diretório confirma 67 arquivos de imagem e **8.204.956 bytes**.
- **127 imagens continuam pendentes**. URLs, placeholders e apenas metadados nao contam.
- 10 checkpoints de no maximo 7 arquivos novos cada (primeiro com 4); manifesto atualizado em `manifests/f.json`.
- Duplicata encontrada entre as fontes Swamp Adder e Zanskaran Viper e corrigida: TF-292 foi substituida por um WebP distinto no commit `b97977b668979cfb72ea3f14728090b53a1ece58`.
- Imagens pequenas validas: TF-285 (64×80), TF-519 (32×32) — pedir substituicao de maior resolucao antes da etapa final de arte.
- Nenhum arquivo global, CSV canonico ou trabalho D/E foi modificado nesta PR.

## Fichas mecanicas estruturadas nesta continuacao

Foi iniciado um pacote **isolado**, sem sobrescrever as pesquisas concorrentes A/B/C. Os tres registros abaixo possuem estatisticas 5e, atributos, tracos, ataques/acoes, custos, CD, alcance, efeitos, reacoes e imagem registrada. A referencia e de transcricoes acessiveis; **a revisao editorial e a conversao para a mecanica propria do jogo de cartas permanecem pendentes**. Portanto nao foram promovidos a `Mecanica_completa=SIM` no CSV.

| ID | Criatura | ND | CA | PV | Pesquisa |
|---|---|---:|---:|---:|---|
| TF-270 | Black Shuck (Tome of Beasts 3, ND11; nao confundir homonimo ND5) | 11 | 17 | 157 | `operational/research/deep-mechanics/f/records/TF-270.json` |
| TF-272 | Light Eater | 1/2 | 14 | 26 | `operational/research/deep-mechanics/f/records/TF-272.json` |
| TF-278 | Snatch Bat | 5 | 16 | 97 | `operational/research/deep-mechanics/f/records/TF-278.json` |

O escopo atual e **3 fichas estruturadas sem homologacao**, mais 67 imagens verificadas; 191 fichas ainda nao receberam este nivel de detalhamento **neste pacote F**. Parte possui pesquisa em branches de mecanica A/B/C, tambem pendente de gates.

## Arquivos fisicos recuperados do GitHub (67)

| ID | Criatura | Formato | Dimensoes | Bytes | SHA-256 |
|---|---|---|---|---:|---|
| TF-270 | Black Shuck | .png | 512×809 | 80532 | `811ad2b19e7381185f49cbc043a8c754446a8dc7a3de5041723ee2141a3468cb` |
| TF-272 | Light Eater | .webp | 280×280 | 84754 | `6c92a666b4d636da2f9cdeae6bae0d31be43576da2fa0db7c50def36c5a52eff` |
| TF-278 | Snatch Bat | .webp | 280×280 | 83964 | `415bae35a313b9751c41ed45f754b5644b01b53ef4a6c9474c1233e57bacf95f` |
| TF-279 | Fate Eater | .webp | 1000×929 | 115858 | `7d3bf68d69971f8aa18eca22d836503d8f4340fad12c9d8aff11c6a0be0db38f` |
| TF-280 | Mamura | .webp | 765×1000 | 123950 | `69c36edd346ab62831505cb463e2d73d57ca3b47b77f5e196b94ef6d7c2d6e0d` |
| TF-285 | Snallygaster | .png | 64×80 | 3383 | `22fd75617163949e41d82203a4c3142d9cf499c6d1b20169111783b879bcf11c` |
| TF-288 | Snake, Swamp Adder | .webp | 985×1000 | 179230 | `c75e7d8c7d26ad45102e5e6b9bc0590b41a3b6e9da26d08550180fd7d639b74b` |
| TF-289 | Porcellina | .webp | 280×280 | 85190 | `8acbf7c93e6ee056d7e837bac15ce461e009eeeb09fcb1a2f20142de900cd930` |
| TF-290 | Glass Gator | .webp | 1000×793 | 217936 | `57dcc40e36ac9b5325bdf98bc87f09bbc79fbf19c15ab91b7c7a40dfb4ad2120` |
| TF-292 | Snake, Zanskaran Viper | .webp | 560×560 | 230340 | `84bd070154a381f0ca04cd539bfa8085790f49b1a2acf5b50593b8641d043852` |
| TF-296 | Angel, Psychopomp | .webp | 280×280 | 76808 | `147d7f4453b22f104f3993e66d2a1c87960ae7bb678b693d27af593f88281ac1` |
| TF-297 | Simurg | .webp | 711×1249 | 282468 | `c6b8e47bff488c445de02c129e7dca0b883398b0c25bb75f41422dcf87c82f2c` |
| TF-298 | Angel, Song | .webp | 688×950 | 105296 | `59ea22d72f2fe09b7f341aafe6d044a3fe5b52d04409461442357950ae3c8943` |
| TF-299 | Angel, Sammael | .webp | 786×956 | 174924 | `21aac7ce7a0d54023af186d31c3759b2465a02231ff136ee3edf6b60e1dbf6fd` |
| TF-300 | Angel, Zoryas | .webp | 706×858 | 108062 | `b60a39e4221a75024d741fccc55a4f50baeb126bd689a657d5c4cdd682fbe4ea` |
| TF-302 | Angel, Shrouded | .webp | 280×280 | 84230 | `0b4804ce928ed6b2c1321dc07ffbfb75e6a78fd8a6b18c91cd7571daee948481` |
| TF-304 | Living Star | .webp | 849×1002 | 264428 | `014dd9ca244d939a92d00b11a078392e76b9479af01bacc529449e992350e9b7` |
| TF-305 | Angel, Zirnitran | .webp | 280×280 | 104226 | `a5d6328e90a68656715d4826f0e8f840de3838a6ccbb51cb245cc4fd83d382a6` |
| TF-306 | Simian, Monkey King | .webp | 731×1187 | 144864 | `549fc595ad52890b695fdfbade1b357873b9abfaba73e1cf5ee08394eb6fe892` |
| TF-309 | Living Wick | .webp | 546×1000 | 73990 | `3688a78eac58b0aaabcaeb913a584833b12f596c05a01861a3ed248b97fab98f` |
| TF-312 | Sigilian | .webp | 769×938 | 158582 | `32dea5f1015c1bdbddc7de8f245a5c830cd61a3a0a7bd0cf5cef2ee07f2899f5` |
| TF-316 | Soil Snake | .webp | 280×280 | 82030 | `87f11f10f38ee55b01b03244c1bcc9fa38a40b38c79e6c272ea45c5df3834daf` |
| TF-317 | Faux-Garou | .webp | 280×280 | 85396 | `ed1efb084173c174aaa73c62169626786fb30e59f620691ee745ab39fa84eaad` |
| TF-318 | Fellforged | .webp | 777×1000 | 275194 | `b52bef4f75925b376ab7fe765dc1b4915374571b8bc8083b6adaca4c9c350151` |
| TF-319 | Gearforged Templar | .webp | 929×1000 | 197712 | `be0c0fdaa05c55e0da4a0bf5de6562e7a62d91e214df7802ba99871ef9aceef8` |
| TF-320 | Gnarljak | .webp | 934×1000 | 218342 | `3c7cc6acae11c6a4a18108ec24247ed3223ebd01f532140d6a0241f21006896b` |
| TF-325 | Lindwurm | .webp | 1000×615 | 145090 | `9bbba64c9f9a27e78ce1b6107674e04bd52e898dd3da5bb886dd3b7503e13e17` |
| TF-328 | Gnyan | .webp | 280×280 | 77614 | `67a32287765fffddd689099c1cd4854e625adff84e7835d77a0263ba7ba8e9fe` |
| TF-329 | Living Soot | .webp | 280×280 | 85414 | `5c45d116be037e5dd2b8be4b2b54b4b2f68410a683f6210444e6257ef6ea2114` |
| TF-330 | Spark | .webp | 1000×639 | 126638 | `eef10b1132a507136843c1db04c5511db5e4fff5d23afe8ba298d6e1c6812bc4` |
| TF-331 | Liosalfar | .webp | 413×1000 | 74908 | `d864fa18c07c2e125c8b320d6d595f4122bdd9eaffa4e977cec484d4d0b3a329` |
| TF-332 | Slow Storm | .webp | 665×1000 | 116472 | `5c576246d3be4ed0da51812bbc7287b67bbe9483c5816df8489bca957b26b89e` |
| TF-333 | Living Shade | .webp | 702×997 | 92384 | `a24bf520fc2164532db9ccac787ec7aaa847e016eb91a684a59c478520e56b4c` |
| TF-334 | Far Darrig | .webp | 742×1000 | 116728 | `34ee03edc0aee91984d997686c5cfced5003967d73f9bbd569f1785e20bbfd64` |
| TF-339 | Malphas | .webp | 685×1000 | 111352 | `cea72f8f615d3c0dfb50af7e43f98b13dc5acf22f146a3a44de0bfd92698510c` |
| TF-340 | Wilderness Crone | .webp | 280×280 | 93256 | `bccde40a00dbd0ca7e1e56dfeba47f1561cdc469f2977d5a2e3c8b76e3638e47` |
| TF-343 | Fear Smith | .webp | 551×1000 | 103652 | `7d81531bd7130402d4b6284dc8cc530d3f5ba2b372ac2942534782170454b8b7` |
| TF-345 | Animal Lord, Mouse King | .webp | 741×970 | 169384 | `cacb51e9799da56d006a9e3509024d75cec09a3cf0f72030522147b657f9eb27` |
| TF-346 | Animal Lord, Lord of Vultures | .webp | 1129×1084 | 116080 | `834a2db0551343ab8e70f6d3cc51c415fe9d28f434a086b3c9d857bf6bd1bd66` |
| TF-347 | Animal Lord, Bat King | .webp | 795×1125 | 88368 | `b8cebf8b190f03a88f6416f9ae351550fe50fcfc476daba19646fdefa0070602` |
| TF-348 | Life Broker | .webp | 280×280 | 86812 | `e56fe4f87b2010eb30c81411da7f3c3fe1ab5a2baf125ba886dcd55224c41795` |
| TF-349 | Animal Lord, Brother Ox | .webp | 879×1117 | 100050 | `9afefbd6fa467d5f0b6eb2183e2327021894a7b727f71476b5bc641160e61d7e` |
| TF-350 | Ettin, Kobold | .webp | 280×280 | 87682 | `4ce4eaa68b6a92be4846a2f1234e4b2ab70e4ca2b10dfba31156e5c441bd7335` |
| TF-363 | Puffinfolk | .webp | 280×280 | 82596 | `fecd7808b7b1e520db6e85f43ce7bb6702f576bdf5b34165e3f1370f58b203c2` |
| TF-365 | Erina, Defender | .webp | 280×280 | 86494 | `627761ad00c77dc1762f76d0c7fee6b82d8bff66eed7e47dcc264a9546a46a1d` |
| TF-366 | Simian, Vanara | .webp | 766×1007 | 153172 | `7faf10bf711886dd20032bd85e673f00c2b266e00a9c826fe3a09f6f1c186179` |
| TF-367 | Erina, Tussler | .webp | 280×280 | 89006 | `21d4a924509e7f966149118f103627e9c6168c317411dc31e4cfe24342c719fa` |
| TF-368 | Gnoll Slaver | .webp | 930×1187 | 227612 | `7f7f22b77552c22461a0fba20590dc394f352c11754bb16bd965bbeca2ef83fd` |
| TF-369 | Gnoll, Havoc Runner | .webp | 833×1000 | 262474 | `fab480ebb2990f4df0b40d5e0a609a7068cf34e485031ee9e1d65b4602226d0e` |
| TF-372 | Gnomish Knife Cultist | .webp | 374×649 | 63606 | `d1478f64f748ecc518ffe19a768f0617bdb7f390191d5f45e06e9f638b74fabf` |
| TF-378 | Mahoru | .webp | 1000×801 | 110202 | `c66c39c4a77b41247712862e600eb3c2fb01de8964f432cfcbe2fd287ac39529` |
| TF-382 | Likho | .webp | 630×1000 | 87404 | `9430957f8a575713fa916454aec8dffc6579f686d1fc3a685dbe718cc8d7c51e` |
| TF-385 | Mantik | .webp | 955×930 | 158980 | `a612184e3e283e5269fda2f4c18473f454eabcb5b4391135bc031d86777f903b` |
| TF-388 | Son of Fenris | .webp | 1000×571 | 106718 | `52a3d977f18583178978a46cb556712b11c86db3ad45443e9a7a7ec3a21748ba` |
| TF-392 | Malmbjorn | .webp | 280×280 | 79832 | `f032d5a239d3a624727de4c4ffd9c2728802f218e4de28370c5b3797c7c071af` |
| TF-394 | Shroud | .webp | 530×1000 | 102362 | `ebca05ba47ac3c3782effc9caccff2d82cb2dc87c7d90806a61626d7051efd99` |
| TF-401 | Mallqui | .webp | 709×1000 | 109534 | `0d710fa63dc05a382ac4523c61c3df696eff943d4dae5b518f8452529f97acfd` |
| TF-406 | Mask Wight | .webp | 660×1000 | 155278 | `42ee77601e51b23973451e18456f472f5b358d497440e40ff58eb3f1c435a0b7` |
| TF-409 | Mandrake | .png | 152×203 | 25756 | `4b1b747fed486975ef9715a0f8fc980ba86d6ddb8916eee96b39901ad950ce8a` |
| TF-412 | Mandrake, Great | .webp | 548×822 | 89906 | `dd22f00b54d275897aef1c0d665ab133ed046bb02a9458da886d4f22c4cc2aeb` |
| TF-413 | Sinstar, Star Thrall | .webp | 300×300 | 94746 | `206c263886773688c422ee545363453bedf8cbb8a76938c11d997bc0d7112013` |
| TF-415 | Gloomflower | .webp | 856×1060 | 128714 | `c9b79ca1642b22c155bf48ae9854a4423b3dcf14b673a40a35dfcf6785be1634` |
| TF-416 | Wind Witch | .webp | 300×300 | 94464 | `b4c71760d500e11c07b9a4a4ad6e7b3abcd6fc34fcfddaf25fcbb93e405afbf8` |
| TF-417 | Mandriano | .webp | 549×670 | 105714 | `34804d3efb5d2c6533ee84ed4a373ca78eec50751bd61d18f3c103cb9fc06b53` |
| TF-421 | Planar Flora, Execrable Shrub | .webp | 840×1059 | 228706 | `56fa5d1abd28a75e037be13aa33cf9cab68961daaeeb5c2e71b3a4109c92b8a3` |
| TF-423 | Spawn of Chernobog | .webp | 587×1064 | 124690 | `0924f6b42405466c1ce589f48bf9b946ade2bb1198a422b7a6998e5101de23e1` |
| TF-519 | Frilled Lizard | .png | 32×32 | 3417 | `cce2fa7f14e82fa99082e2bb0b0e0c45f5a58dd78b05d697abbfd89bcb2ebbb2` |

Fontes individuais, MIME, extensao, commit de persistencia e SHA-256 constam de `manifests/f.json`. Hashes confirmados pela leitura binaria. As imagens nao foram consideradas finalizadas apenas por terem URL.

## Imagens bloqueadas (127)

| ID | Criatura | Causa |
|---|---|---|
| TF-273 | Shoth, Sooze | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-274 | Malleable, Minor | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-275 | Maw Swarm | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-276 | Malleable, Moderate | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-277 | Shoth, Oth | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-283 | Shukankor | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-284 | Malleable, Major | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-286 | Malleable, Massive | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-291 | Hlaupa | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-293 | Planar Flora, Hallowed Reeds | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-295 | Greater Spirit Soldier | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-301 | Planar Flora, Ecstatic Bloom | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-303 | Angel, Uridimmu | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-311 | Bolt-Thrower | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-321 | Blood Guardian | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-324 | Green Kobold Drake | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-326 | Linnorm, Vent | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-327 | Azer Forgemaster | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-335 | Woe Siphon | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-336 | Far Dorocha | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-338 | Somberweave | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-341 | Shurale | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-342 | Silenal | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-344 | Pumpkin King | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-351 | Half-Demon Ogre | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-353 | Manggus | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-355 | Giant, Hill Chief | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-356 | Grendel | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-358 | Giant, Void | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-360 | Gelatinous Wall | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-361 | Elder Black Pudding | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-364 | Simian, Kapi | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-370 | Simian, Sulsha | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-373 | Kobold, Wizard | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-376 | Heshgarat Cat | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-379 | Snake with a Hundred Mage Hands | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-380 | Stone Shark | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-381 | Aracnecore | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-384 | Mutant Rust Monster | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-386 | Grootslang | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-389 | Supermutant Rust Monster | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-393 | Minotaur Conqueror | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-395 | Skeleton, Cackling | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-396 | Skeleton, Clacking | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-397 | Fane Spirit | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-398 | Falsifier Fog | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-399 | Mari Lwyd | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-400 | Headless Horseman | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-402 | Marsh Dire | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-403 | Lich, Hierophant | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-405 | Lich, Virtuoso | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-407 | Lich, Pact | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-408 | Grove Swarm | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-410 | Fungi, Wirbeln | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-411 | Garlicle | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-414 | Wallflower | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-418 | Sodwose | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-419 | Witchalder | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-420 | Mandriano, Ancient | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-424 | Soul Eater | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-425 | Snow Terror | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-426 | Planar Flora, Thorned Sulfurlord | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-428 | Cerberus Guardian | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-429 | Clockwork Sentinel | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-431 | Conjured Guardian | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-434 | Crusher | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-442 | Flame-Spitting Statue | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-444 | Flesh Guardian | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-446 | Grave Guardian | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-447 | Hound Guardian | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-448 | Imprisoned Celestial | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-449 | Imprisoned Fiend | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-450 | Iron Guardian | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-456 | Scarecrow Harvester | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-459 | Ankheg Empress | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-461 | Ankheg Spawn | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-462 | Behir Magus | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-463 | Blood Maggot | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-465 | Canicore | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-467 | Corpse Fly | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-468 | Faerie Chimera | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-469 | Fateholder | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-470 | Fiendish Chimera | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-471 | Fiendish Dire Boar | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-473 | Flying Lion | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-474 | Giant Grick | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-475 | Giant Lanternfish | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-476 | Greater Sphinx | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-477 | Grimalkin | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-478 | Gourdling | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-480 | Sewer Walker | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-481 | Spell Shrieker | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-482 | Spore Thrall | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-483 | Squashling | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-485 | Goblin Boss | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-486 | Goblin Cursespitter | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-489 | Swarm of Skitterlings | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-490 | Goblin Lackey | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-491 | Blazing Black Pudding | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-492 | Slime Mold | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-493 | Rock Troll | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-494 | Askwise Keeper | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-495 | Mykand | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-496 | Tyskri | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-497 | Faun | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-499 | Cloud of Ghasthoppers | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-500 | Gorger Zombie Horde | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-501 | Lost Prospector | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-502 | Ghasthopper | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-503 | Stuffed Crab | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-504 | Warlord's Ghost | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-505 | Demilich Mastermind | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-506 | Mariner Ghost Swarm | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-507 | Fogborn Skeleton Horde | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-508 | Fogborn Zombie | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-509 | Fogborn Zombie Horde | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-510 | Infernal Mammoth | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-511 | Fiendbloom Awakened Tree | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-513 | Improved Spirit Soldier | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-514 | Drainpipe Gargoyle | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-515 | Malcubus | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-516 | Kanos Spawn | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-517 | Imp Flock | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-518 | Infernal Dwarf | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-521 | Bugbear Door Breaker | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-522 | Crime Boss | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |
| TF-523 | Pugilist | Imagem adequada ainda não adquirida e validada individualmente; nenhum placeholder ou URL foi contabilizado como arquivo. |

**Conclusao:** trabalho parcial. Nao alegar 194 imagens ou 194 fichas completas; manter PR em draft e continuar somente com imagens especificas e regras confirmadas.
