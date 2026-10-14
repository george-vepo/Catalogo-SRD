# SRD Card Game 607 — Aquisição real de imagens F (parcial)

## Escopo, preflight e integridade

- Repositório: `george-vepo/SRD-Card-Game-607-Supervisor`.
- Commit-base: `a962c48a1169c2ef2be8137715a095a596753b32`.
- CSV: `operational/research/catalog-ledger-20261011-v27/catalog-status.csv`; filtro `Imagem` não iniciando em `VERIFICADA` produz 584 IDs, seleção `pending_images.slice(390,584)` produz 194 IDs exclusivos de `TF-270` a `TF-523`.
- Branch: `chatgpt/srd607-image-assets-f`; destino da PR em rascunho: `chatgpt/srd607-research-checkpoints-20261011`. Não houve merge.
- Exclusividade preservada: nenhum arquivo global, CSV canônico, imagem D/E ou ficha mecânica alterada na comparação final. As três fichas adicionadas indevidamente antes da reafirmação do escopo foram retiradas no commit `8677f4c816bbb76a86af76f97b000d2273521fc3`.
- Persistência pela API de Git blobs em base64 com commits próprios, sem contabilizar URLs como arquivos. Verificações pós-upload por reabertura e igualdade binária com origem.

## Resultado comprovado

| Indicador | Valor |
|---|---:|
| Seleção exclusiva F | 194 |
| Arquivos de imagem binários existentes no GitHub | 81 |
| Validados após upload | 81 |
| Continuam sem imagem | 113 |
| Bytes armazenados | 10270130 |
| Checkpoints com até 10 imagens | 13 |

A listagem do GitHub foi confrontada com os 81 caminhos e tamanhos do manifesto. Os 81 hashes SHA-256 são distintos. Confere formato real, dimensões, tipo MIME, fonte e commit individual no manifesto.

**Limitações:** validação de integridade do arquivo não equivale a aprovação artística. Algumas miniaturas têm resolução baixa, especialmente TF-285 (64×80), TF-519 (32×32), tokens ToB3 próximos de 280×280. Precisam de substituição para uso em cartas de alta resolução. Nenhum placeholder ou imagem genérica foi usado para preencher pendência.

## Arquivos de imagem armazenados (81)

| ID | Criatura | Fonte | Extensão / MIME | Dimensões | Bytes | SHA-256 | Commit | Validação |
|---|---|---|---|---|---:|---|---|---|
| TF-270 | Black Shuck | [fonte](https://github.com/seanperkins/isekai-game/blob/HEAD/assets/sheets/anim_wolf_black_shuck.png) | .png / image/png | 512×809 | 80532 | `811ad2b19e7381185f49cbc043a8c754446a8dc7a3de5041723ee2141a3468cb` | `d5c3301e8310` | Validado |
| TF-272 | Light Eater | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Light%20Eater.webp) | .webp / image/webp | 280×280 | 84754 | `6c92a666b4d636da2f9cdeae6bae0d31be43576da2fa0db7c50def36c5a52eff` | `3592249f6fec` | Validado |
| TF-273 | Shoth, Sooze | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Sooze.webp) | .webp / image/webp | 373×669 | 58132 | `2f5d9b3c140aaa4fffb83f2b12ae82db571e0de4d3b0faf0ed47167bd5dfd874` | `f1f2c9a0dfae` | Validado |
| TF-277 | Shoth, Oth | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Oth.webp) | .webp / image/webp | 645×772 | 103398 | `27f610bccd814dee49461b37ee191b44151cebe5cb953b7c55364460da7c11c9` | `f1f2c9a0dfae` | Validado |
| TF-278 | Snatch Bat | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Snatch%20Bat.webp) | .webp / image/webp | 280×280 | 83964 | `415bae35a313b9751c41ed45f754b5644b01b53ef4a6c9474c1233e57bacf95f` | `3592249f6fec` | Validado |
| TF-279 | Fate Eater | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Fate%20Eater.webp) | .webp / image/webp | 1000×929 | 115858 | `7d3bf68d69971f8aa18eca22d836503d8f4340fad12c9d8aff11c6a0be0db38f` | `3592249f6fec` | Validado |
| TF-280 | Mamura | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Mamura.webp) | .webp / image/webp | 765×1000 | 123950 | `69c36edd346ab62831505cb463e2d73d57ca3b47b77f5e196b94ef6d7c2d6e0d` | `3592249f6fec` | Validado |
| TF-285 | Snallygaster | [fonte](https://github.com/Koopro/wizards_and_beasts/blob/HEAD/src/main/resources/assets/wizards_and_beasts/textures/entity/snallygaster.png) | .png / image/png | 64×80 | 3383 | `22fd75617163949e41d82203a4c3142d9cf499c6d1b20169111783b879bcf11c` | `d5c3301e8310` | Validado |
| TF-288 | Snake, Swamp Adder | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Swamp%20Adder.webp) | .webp / image/webp | 985×1000 | 179230 | `c75e7d8c7d26ad45102e5e6b9bc0590b41a3b6e9da26d08550180fd7d639b74b` | `9cb21b65cee8` | Validado |
| TF-289 | Porcellina | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Porcellina.webp) | .webp / image/webp | 280×280 | 85190 | `8acbf7c93e6ee056d7e837bac15ce461e009eeeb09fcb1a2f20142de900cd930` | `3592249f6fec` | Validado |
| TF-290 | Glass Gator | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Glass%20Gator.webp) | .webp / image/webp | 1000×793 | 217936 | `57dcc40e36ac9b5325bdf98bc87f09bbc79fbf19c15ab91b7c7a40dfb4ad2120` | `3592249f6fec` | Validado |
| TF-292 | Snake, Zanskaran Viper | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB/bestiary/tokens/Zanskaran%20Viper.webp) | .webp / image/webp | 560×560 | 230340 | `84bd070154a381f0ca04cd539bfa8085790f49b1a2acf5b50593b8641d043852` | `b97977b66897` | Validado |
| TF-293 | Planar Flora, Hallowed Reeds | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Hallowedreed.webp) | .webp / image/webp | 678×973 | 170512 | `07c1836e4765d205a37f44c3de6430b18e0017091be4aff4991f694097d01885` | `f1f2c9a0dfae` | Validado |
| TF-296 | Angel, Psychopomp | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Psychopomp.webp) | .webp / image/webp | 280×280 | 76808 | `147d7f4453b22f104f3993e66d2a1c87960ae7bb678b693d27af593f88281ac1` | `9cb21b65cee8` | Validado |
| TF-297 | Simurg | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Simurg.webp) | .webp / image/webp | 711×1249 | 282468 | `c6b8e47bff488c445de02c129e7dca0b883398b0c25bb75f41422dcf87c82f2c` | `02ec8bd8a5fc` | Validado |
| TF-298 | Angel, Song | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/angelsong.webp) | .webp / image/webp | 688×950 | 105296 | `59ea22d72f2fe09b7f341aafe6d044a3fe5b52d04409461442357950ae3c8943` | `02ec8bd8a5fc` | Validado |
| TF-299 | Angel, Sammael | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/angelsammael.webp) | .webp / image/webp | 786×956 | 174924 | `21aac7ce7a0d54023af186d31c3759b2465a02231ff136ee3edf6b60e1dbf6fd` | `02ec8bd8a5fc` | Validado |
| TF-300 | Angel, Zoryas | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/angelzoryas.webp) | .webp / image/webp | 706×858 | 108062 | `b60a39e4221a75024d741fccc55a4f50baeb126bd689a657d5c4cdd682fbe4ea` | `02ec8bd8a5fc` | Validado |
| TF-301 | Planar Flora, Ecstatic Bloom | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Ecstaticbloom.webp) | .webp / image/webp | 601×805 | 136916 | `ff635eb844363ee17320394130a208384c4923514b6fecf163a87c936310a035` | `f1f2c9a0dfae` | Validado |
| TF-302 | Angel, Shrouded | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Shrouded%20Angel.webp) | .webp / image/webp | 280×280 | 84230 | `0b4804ce928ed6b2c1321dc07ffbfb75e6a78fd8a6b18c91cd7571daee948481` | `9cb21b65cee8` | Validado |
| TF-304 | Living Star | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Livingstar.webp) | .webp / image/webp | 849×1002 | 264428 | `014dd9ca244d939a92d00b11a078392e76b9479af01bacc529449e992350e9b7` | `02ec8bd8a5fc` | Validado |
| TF-305 | Angel, Zirnitran | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Zirnitran.webp) | .webp / image/webp | 280×280 | 104226 | `a5d6328e90a68656715d4826f0e8f840de3838a6ccbb51cb245cc4fd83d382a6` | `9cb21b65cee8` | Validado |
| TF-306 | Simian, Monkey King | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Monkeyking.webp) | .webp / image/webp | 731×1187 | 144864 | `549fc595ad52890b695fdfbade1b357873b9abfaba73e1cf5ee08394eb6fe892` | `dd89b865389a` | Validado |
| TF-309 | Living Wick | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Living%20Wick.webp) | .webp / image/webp | 546×1000 | 73990 | `3688a78eac58b0aaabcaeb913a584833b12f596c05a01861a3ed248b97fab98f` | `3592249f6fec` | Validado |
| TF-312 | Sigilian | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Sigilian.webp) | .webp / image/webp | 769×938 | 158582 | `32dea5f1015c1bdbddc7de8f245a5c830cd61a3a0a7bd0cf5cef2ee07f2899f5` | `02ec8bd8a5fc` | Validado |
| TF-316 | Soil Snake | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Soil%20Snake.webp) | .webp / image/webp | 280×280 | 82030 | `87f11f10f38ee55b01b03244c1bcc9fa38a40b38c79e6c272ea45c5df3834daf` | `cb2efc6c0c32` | Validado |
| TF-317 | Faux-Garou | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Faux-Garou.webp) | .webp / image/webp | 280×280 | 85396 | `ed1efb084173c174aaa73c62169626786fb30e59f620691ee745ab39fa84eaad` | `cb2efc6c0c32` | Validado |
| TF-318 | Fellforged | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Fellforged.webp) | .webp / image/webp | 777×1000 | 275194 | `b52bef4f75925b376ab7fe765dc1b4915374571b8bc8083b6adaca4c9c350151` | `cb2efc6c0c32` | Validado |
| TF-319 | Gearforged Templar | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Gearforged%20Templar.webp) | .webp / image/webp | 929×1000 | 197712 | `be0c0fdaa05c55e0da4a0bf5de6562e7a62d91e214df7802ba99871ef9aceef8` | `cb2efc6c0c32` | Validado |
| TF-320 | Gnarljak | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Gnarljak.webp) | .webp / image/webp | 934×1000 | 218342 | `3c7cc6acae11c6a4a18108ec24247ed3223ebd01f532140d6a0241f21006896b` | `cb2efc6c0c32` | Validado |
| TF-325 | Lindwurm | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Lindwurm.webp) | .webp / image/webp | 1000×615 | 145090 | `9bbba64c9f9a27e78ce1b6107674e04bd52e898dd3da5bb886dd3b7503e13e17` | `cb2efc6c0c32` | Validado |
| TF-328 | Gnyan | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Gnyan.webp) | .webp / image/webp | 280×280 | 77614 | `67a32287765fffddd689099c1cd4854e625adff84e7835d77a0263ba7ba8e9fe` | `cb2efc6c0c32` | Validado |
| TF-329 | Living Soot | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Living%20Soot.webp) | .webp / image/webp | 280×280 | 85414 | `5c45d116be037e5dd2b8be4b2b54b4b2f68410a683f6210444e6257ef6ea2114` | `829ac622122a` | Validado |
| TF-330 | Spark | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Spark.webp) | .webp / image/webp | 1000×639 | 126638 | `eef10b1132a507136843c1db04c5511db5e4fff5d23afe8ba298d6e1c6812bc4` | `829ac622122a` | Validado |
| TF-331 | Liosalfar | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Liosalfar.webp) | .webp / image/webp | 413×1000 | 74908 | `d864fa18c07c2e125c8b320d6d595f4122bdd9eaffa4e977cec484d4d0b3a329` | `829ac622122a` | Validado |
| TF-332 | Slow Storm | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Slow%20Storm.webp) | .webp / image/webp | 665×1000 | 116472 | `5c576246d3be4ed0da51812bbc7287b67bbe9483c5816df8489bca957b26b89e` | `829ac622122a` | Validado |
| TF-333 | Living Shade | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Livingshade.webp) | .webp / image/webp | 702×997 | 92384 | `a24bf520fc2164532db9ccac787ec7aaa847e016eb91a684a59c478520e56b4c` | `02ec8bd8a5fc` | Validado |
| TF-334 | Far Darrig | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Far%20Darrig.webp) | .webp / image/webp | 742×1000 | 116728 | `34ee03edc0aee91984d997686c5cfced5003967d73f9bbd569f1785e20bbfd64` | `829ac622122a` | Validado |
| TF-339 | Malphas | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Malphas.webp) | .webp / image/webp | 685×1000 | 111352 | `cea72f8f615d3c0dfb50af7e43f98b13dc5acf22f146a3a44de0bfd92698510c` | `829ac622122a` | Validado |
| TF-340 | Wilderness Crone | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens-alt/Wilderness%20Crone.webp) | .webp / image/webp | 280×280 | 93256 | `bccde40a00dbd0ca7e1e56dfeba47f1561cdc469f2977d5a2e3c8b76e3638e47` | `829ac622122a` | Validado |
| TF-343 | Fear Smith | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Fear%20Smith.webp) | .webp / image/webp | 551×1000 | 103652 | `7d81531bd7130402d4b6284dc8cc530d3f5ba2b372ac2942534782170454b8b7` | `c2d81bd1449c` | Validado |
| TF-345 | Animal Lord, Mouse King | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/animallordmouseking.webp) | .webp / image/webp | 741×970 | 169384 | `cacb51e9799da56d006a9e3509024d75cec09a3cf0f72030522147b657f9eb27` | `b5404483493f` | Validado |
| TF-346 | Animal Lord, Lord of Vultures | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/lordofvultures.webp) | .webp / image/webp | 1129×1084 | 116080 | `834a2db0551343ab8e70f6d3cc51c415fe9d28f434a086b3c9d857bf6bd1bd66` | `dd89b865389a` | Validado |
| TF-347 | Animal Lord, Bat King | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/animallordbatking.webp) | .webp / image/webp | 795×1125 | 88368 | `b8cebf8b190f03a88f6416f9ae351550fe50fcfc476daba19646fdefa0070602` | `b5404483493f` | Validado |
| TF-348 | Life Broker | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Life%20Broker.webp) | .webp / image/webp | 280×280 | 86812 | `e56fe4f87b2010eb30c81411da7f3c3fe1ab5a2baf125ba886dcd55224c41795` | `c2d81bd1449c` | Validado |
| TF-349 | Animal Lord, Brother Ox | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/animallordbrotherox.webp) | .webp / image/webp | 879×1117 | 100050 | `9afefbd6fa467d5f0b6eb2183e2327021894a7b727f71476b5bc641160e61d7e` | `b5404483493f` | Validado |
| TF-350 | Ettin, Kobold | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Kobold%20Ettin.webp) | .webp / image/webp | 280×280 | 87682 | `4ce4eaa68b6a92be4846a2f1234e4b2ab70e4ca2b10dfba31156e5c441bd7335` | `9cb21b65cee8` | Validado |
| TF-363 | Puffinfolk | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Puffinfolk.webp) | .webp / image/webp | 280×280 | 82596 | `fecd7808b7b1e520db6e85f43ce7bb6702f576bdf5b34165e3f1370f58b203c2` | `c2d81bd1449c` | Validado |
| TF-364 | Simian, Kapi | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Kapi.webp) | .webp / image/webp | 667×862 | 97320 | `9495976ff79082fccfb9969861ab2f1603a218728bf0b8d4f4576c7b2aec9e42` | `f1f2c9a0dfae` | Validado |
| TF-365 | Erina, Defender | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB/bestiary/tokens/Erina%20Defender.webp) | .webp / image/webp | 280×280 | 86494 | `627761ad00c77dc1762f76d0c7fee6b82d8bff66eed7e47dcc264a9546a46a1d` | `c2d81bd1449c` | Validado |
| TF-366 | Simian, Vanara | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Vanara.webp) | .webp / image/webp | 766×1007 | 153172 | `7faf10bf711886dd20032bd85e673f00c2b266e00a9c826fe3a09f6f1c186179` | `dd89b865389a` | Validado |
| TF-367 | Erina, Tussler | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Erina%20Tussler.webp) | .webp / image/webp | 280×280 | 89006 | `21d4a924509e7f966149118f103627e9c6168c317411dc31e4cfe24342c719fa` | `c2d81bd1449c` | Validado |
| TF-368 | Gnoll Slaver | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/gnollslaver.webp) | .webp / image/webp | 930×1187 | 227612 | `7f7f22b77552c22461a0fba20590dc394f352c11754bb16bd965bbeca2ef83fd` | `b5404483493f` | Validado |
| TF-369 | Gnoll, Havoc Runner | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Gnoll%20Havoc%20Runner.webp) | .webp / image/webp | 833×1000 | 262474 | `fab480ebb2990f4df0b40d5e0a609a7068cf34e485031ee9e1d65b4602226d0e` | `c2d81bd1449c` | Validado |
| TF-372 | Gnomish Knife Cultist | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Gnomishknifecultist.webp) | .webp / image/webp | 374×649 | 63606 | `d1478f64f748ecc518ffe19a768f0617bdb7f390191d5f45e06e9f638b74fabf` | `b5404483493f` | Validado |
| TF-373 | Kobold, Wizard | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/wizardkobold.webp) | .webp / image/webp | 705×1015 | 169364 | `2712054b3c8609740114f91711b0171bbb19335f6e77bc976b65ecbab6030c74` | `bed2dca7b66e` | Validado |
| TF-378 | Mahoru | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Mahoru.webp) | .webp / image/webp | 1000×801 | 110202 | `c66c39c4a77b41247712862e600eb3c2fb01de8964f432cfcbe2fd287ac39529` | `c2d81bd1449c` | Validado |
| TF-382 | Likho | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Likho.webp) | .webp / image/webp | 630×1000 | 87404 | `9430957f8a575713fa916454aec8dffc6579f686d1fc3a685dbe718cc8d7c51e` | `1d09e3466e4a` | Validado |
| TF-385 | Mantik | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Mantik.webp) | .webp / image/webp | 955×930 | 158980 | `a612184e3e283e5269fda2f4c18473f454eabcb5b4391135bc031d86777f903b` | `b5404483493f` | Validado |
| TF-388 | Son of Fenris | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Son%20of%20Fenris.webp) | .webp / image/webp | 1000×571 | 106718 | `52a3d977f18583178978a46cb556712b11c86db3ad45443e9a7a7ec3a21748ba` | `1d09e3466e4a` | Validado |
| TF-392 | Malmbjorn | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Malmbjorn.webp) | .webp / image/webp | 280×280 | 79832 | `f032d5a239d3a624727de4c4ffd9c2728802f218e4de28370c5b3797c7c071af` | `1d09e3466e4a` | Validado |
| TF-394 | Shroud | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Shroud.webp) | .webp / image/webp | 530×1000 | 102362 | `ebca05ba47ac3c3782effc9caccff2d82cb2dc87c7d90806a61626d7051efd99` | `1d09e3466e4a` | Validado |
| TF-396 | Skeleton, Clacking | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Clackingskeleton.webp) | .webp / image/webp | 833×1215 | 202888 | `cfdecca370a07b825d97ef34442f8dd260d8aa651c1ffde380697d7ef06904dc` | `0a06d9a57637` | Validado |
| TF-401 | Mallqui | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Mallqui.webp) | .webp / image/webp | 709×1000 | 109534 | `0d710fa63dc05a382ac4523c61c3df696eff943d4dae5b518f8452529f97acfd` | `1d09e3466e4a` | Validado |
| TF-403 | Lich, Hierophant | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Hierophantlich.webp) | .webp / image/webp | 861×1188 | 191576 | `856b80f7b75acb55a06cedb91bb55adc6060b3da7b8708aeeab5526e941244a9` | `0a06d9a57637` | Validado |
| TF-406 | Mask Wight | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Mask%20Wight.webp) | .webp / image/webp | 660×1000 | 155278 | `42ee77601e51b23973451e18456f472f5b358d497440e40ff58eb3f1c435a0b7` | `1d09e3466e4a` | Validado |
| TF-407 | Lich, Pact | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Pactlich.webp) | .webp / image/webp | 920×1168 | 211940 | `02428085c3b3f3272cbc4e96cbf75b189c31785045b851206c7d331ce4d935da` | `0a06d9a57637` | Validado |
| TF-409 | Mandrake | [fonte](https://github.com/tpgame-spbstu/Tabletop-roguelike/blob/HEAD/Card/Textures/Earth%20Mandrake.png) | .png / image/png | 152×203 | 25756 | `4b1b747fed486975ef9715a0f8fc980ba86d6ddb8916eee96b39901ad950ce8a` | `d5c3301e8310` | Validado |
| TF-410 | Fungi, Wirbeln | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/wirbelnfungi.webp) | .webp / image/webp | 871×972 | 182470 | `c5e2f0407bad0ef3019b6d102e83b039ab656ef1842fb553b8f6b6a9b3e97bfd` | `bed2dca7b66e` | Validado |
| TF-412 | Mandrake, Great | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Mandrakegreat.webp) | .webp / image/webp | 548×822 | 89906 | `dd22f00b54d275897aef1c0d665ab133ed046bb02a9458da886d4f22c4cc2aeb` | `b5404483493f` | Validado |
| TF-413 | Sinstar, Star Thrall | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Star%20Thrall.webp) | .webp / image/webp | 300×300 | 94746 | `206c263886773688c422ee545363453bedf8cbb8a76938c11d997bc0d7112013` | `9cb21b65cee8` | Validado |
| TF-415 | Gloomflower | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/gloomflower.webp) | .webp / image/webp | 856×1060 | 128714 | `c9b79ca1642b22c155bf48ae9854a4423b3dcf14b673a40a35dfcf6785be1634` | `dd89b865389a` | Validado |
| TF-416 | Wind Witch | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Wind%20Witch.webp) | .webp / image/webp | 300×300 | 94464 | `b4c71760d500e11c07b9a4a4ad6e7b3abcd6fc34fcfddaf25fcbb93e405afbf8` | `1d09e3466e4a` | Validado |
| TF-417 | Mandriano | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Mandriano.webp) | .webp / image/webp | 549×670 | 105714 | `34804d3efb5d2c6533ee84ed4a373ca78eec50751bd61d18f3c103cb9fc06b53` | `dd89b865389a` | Validado |
| TF-418 | Sodwose | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Sodwose.webp) | .webp / image/webp | 280×280 | 92680 | `bd569407dbdfe04593275fbc0eb6a3fa7864c7d49b090c0356df9687a2a0fb3a` | `0a06d9a57637` | Validado |
| TF-419 | Witchalder | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB3/bestiary/tokens/Witchalder.webp) | .webp / image/webp | 280×280 | 94572 | `eb293e30ce3cc433d9019ac6329b221ea12c7e86564bcf1268401a57a6bea798` | `0a06d9a57637` | Validado |
| TF-421 | Planar Flora, Execrable Shrub | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Execrableshrub.webp) | .webp / image/webp | 840×1059 | 228706 | `56fa5d1abd28a75e037be13aa33cf9cab68961daaeeb5c2e71b3a4109c92b8a3` | `dd89b865389a` | Validado |
| TF-423 | Spawn of Chernobog | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Spawnofchernobog.webp) | .webp / image/webp | 587×1064 | 124690 | `0924f6b42405466c1ce589f48bf9b946ade2bb1198a422b7a6998e5101de23e1` | `dd89b865389a` | Validado |
| TF-424 | Soul Eater | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/ToB1-2023/bestiary/Soul%20Eater.webp) | .webp / image/webp | 781×1000 | 172536 | `1df39ab86f46bb32fabcf1989583b07faf1ee746e6c086a4c70c5b82682f8323` | `0a06d9a57637` | Validado |
| TF-426 | Planar Flora, Thorned Sulfurlord | [fonte](https://github.com/TheGiddyLimit/homebrew-img/blob/main/img/CCodex/Thornedsulfurlord.webp) | .webp / image/webp | 964×887 | 180870 | `945c9482deb9636e68c8d004f8e915f599220a4e812db472eaad25d646e64742` | `0a06d9a57637` | Validado |
| TF-519 | Frilled Lizard | [fonte](https://github.com/ANTALLIS/grahams-game/blob/HEAD/rltiles/mon/animals/frilled_lizard.png) | .png / image/png | 32×32 | 3417 | `cce2fa7f14e82fa99082e2bb0b0e0c45f5a58dd78b05d697abbfd89bcb2ebbb2` | `d5c3301e8310` | Validado |

## Pendentes e razões (113)

| ID | Criatura | Motivo de pendência |
|---|---|---|
| TF-274 | Malleable, Minor | Imagem individual adequada ainda nao adquirida e validada. |
| TF-275 | Maw Swarm | Imagem individual adequada ainda nao adquirida e validada. |
| TF-276 | Malleable, Moderate | Imagem individual adequada ainda nao adquirida e validada. |
| TF-283 | Shukankor | Imagem individual adequada ainda nao adquirida e validada. |
| TF-284 | Malleable, Major | Imagem individual adequada ainda nao adquirida e validada. |
| TF-286 | Malleable, Massive | Imagem individual adequada ainda nao adquirida e validada. |
| TF-291 | Hlaupa | Imagem individual adequada ainda nao adquirida e validada. |
| TF-295 | Greater Spirit Soldier | Imagem individual adequada ainda nao adquirida e validada. |
| TF-303 | Angel, Uridimmu | Imagem individual adequada ainda nao adquirida e validada. |
| TF-311 | Bolt-Thrower | Imagem individual adequada ainda nao adquirida e validada. |
| TF-321 | Blood Guardian | Imagem individual adequada ainda nao adquirida e validada. |
| TF-324 | Green Kobold Drake | Imagem individual adequada ainda nao adquirida e validada. |
| TF-326 | Linnorm, Vent | Imagem individual adequada ainda nao adquirida e validada. |
| TF-327 | Azer Forgemaster | Imagem individual adequada ainda nao adquirida e validada. |
| TF-335 | Woe Siphon | Imagem individual adequada ainda nao adquirida e validada. |
| TF-336 | Far Dorocha | Imagem individual adequada ainda nao adquirida e validada. |
| TF-338 | Somberweave | Imagem individual adequada ainda nao adquirida e validada. |
| TF-341 | Shurale | Imagem individual adequada ainda nao adquirida e validada. |
| TF-342 | Silenal | Imagem individual adequada ainda nao adquirida e validada. |
| TF-344 | Pumpkin King | Imagem individual adequada ainda nao adquirida e validada. |
| TF-351 | Half-Demon Ogre | Imagem individual adequada ainda nao adquirida e validada. |
| TF-353 | Manggus | Imagem individual adequada ainda nao adquirida e validada. |
| TF-355 | Giant, Hill Chief | Imagem individual adequada ainda nao adquirida e validada. |
| TF-356 | Grendel | Imagem individual adequada ainda nao adquirida e validada. |
| TF-358 | Giant, Void | Imagem individual adequada ainda nao adquirida e validada. |
| TF-360 | Gelatinous Wall | Imagem individual adequada ainda nao adquirida e validada. |
| TF-361 | Elder Black Pudding | Imagem individual adequada ainda nao adquirida e validada. |
| TF-370 | Simian, Sulsha | Imagem individual adequada ainda nao adquirida e validada. |
| TF-376 | Heshgarat Cat | Imagem individual adequada ainda nao adquirida e validada. |
| TF-379 | Snake with a Hundred Mage Hands | Imagem individual adequada ainda nao adquirida e validada. |
| TF-380 | Stone Shark | Imagem individual adequada ainda nao adquirida e validada. |
| TF-381 | Aracnecore | Imagem individual adequada ainda nao adquirida e validada. |
| TF-384 | Mutant Rust Monster | Imagem individual adequada ainda nao adquirida e validada. |
| TF-386 | Grootslang | Imagem individual adequada ainda nao adquirida e validada. |
| TF-389 | Supermutant Rust Monster | Imagem individual adequada ainda nao adquirida e validada. |
| TF-393 | Minotaur Conqueror | Imagem individual adequada ainda nao adquirida e validada. |
| TF-395 | Skeleton, Cackling | Imagem individual adequada ainda nao adquirida e validada. |
| TF-397 | Fane Spirit | Imagem individual adequada ainda nao adquirida e validada. |
| TF-398 | Falsifier Fog | Imagem individual adequada ainda nao adquirida e validada. |
| TF-399 | Mari Lwyd | Imagem individual adequada ainda nao adquirida e validada. |
| TF-400 | Headless Horseman | Imagem individual adequada ainda nao adquirida e validada. |
| TF-402 | Marsh Dire | Imagem individual adequada ainda nao adquirida e validada. |
| TF-405 | Lich, Virtuoso | Imagem individual adequada ainda nao adquirida e validada. |
| TF-408 | Grove Swarm | Imagem individual adequada ainda nao adquirida e validada. |
| TF-411 | Garlicle | Imagem individual adequada ainda nao adquirida e validada. |
| TF-414 | Wallflower | Imagem individual adequada ainda nao adquirida e validada. |
| TF-420 | Mandriano, Ancient | Fontes Ancient Mandriano e Mandriano exibem mesmo blob; requer arte distinta. |
| TF-425 | Snow Terror | Imagem individual adequada ainda nao adquirida e validada. |
| TF-428 | Cerberus Guardian | Imagem individual adequada ainda nao adquirida e validada. |
| TF-429 | Clockwork Sentinel | Imagem individual adequada ainda nao adquirida e validada. |
| TF-431 | Conjured Guardian | Imagem individual adequada ainda nao adquirida e validada. |
| TF-434 | Crusher | Imagem individual adequada ainda nao adquirida e validada. |
| TF-442 | Flame-Spitting Statue | Imagem individual adequada ainda nao adquirida e validada. |
| TF-444 | Flesh Guardian | Imagem individual adequada ainda nao adquirida e validada. |
| TF-446 | Grave Guardian | Imagem individual adequada ainda nao adquirida e validada. |
| TF-447 | Hound Guardian | Imagem individual adequada ainda nao adquirida e validada. |
| TF-448 | Imprisoned Celestial | Imagem individual adequada ainda nao adquirida e validada. |
| TF-449 | Imprisoned Fiend | Imagem individual adequada ainda nao adquirida e validada. |
| TF-450 | Iron Guardian | Imagem individual adequada ainda nao adquirida e validada. |
| TF-456 | Scarecrow Harvester | Imagem individual adequada ainda nao adquirida e validada. |
| TF-459 | Ankheg Empress | Imagem individual adequada ainda nao adquirida e validada. |
| TF-461 | Ankheg Spawn | Imagem individual adequada ainda nao adquirida e validada. |
| TF-462 | Behir Magus | Imagem individual adequada ainda nao adquirida e validada. |
| TF-463 | Blood Maggot | Imagem individual adequada ainda nao adquirida e validada. |
| TF-465 | Canicore | Imagem individual adequada ainda nao adquirida e validada. |
| TF-467 | Corpse Fly | Imagem individual adequada ainda nao adquirida e validada. |
| TF-468 | Faerie Chimera | Imagem individual adequada ainda nao adquirida e validada. |
| TF-469 | Fateholder | Imagem individual adequada ainda nao adquirida e validada. |
| TF-470 | Fiendish Chimera | Imagem individual adequada ainda nao adquirida e validada. |
| TF-471 | Fiendish Dire Boar | Imagem individual adequada ainda nao adquirida e validada. |
| TF-473 | Flying Lion | Imagem individual adequada ainda nao adquirida e validada. |
| TF-474 | Giant Grick | Imagem individual adequada ainda nao adquirida e validada. |
| TF-475 | Giant Lanternfish | Imagem individual adequada ainda nao adquirida e validada. |
| TF-476 | Greater Sphinx | Imagem individual adequada ainda nao adquirida e validada. |
| TF-477 | Grimalkin | Imagem individual adequada ainda nao adquirida e validada. |
| TF-478 | Gourdling | Imagem individual adequada ainda nao adquirida e validada. |
| TF-480 | Sewer Walker | Imagem individual adequada ainda nao adquirida e validada. |
| TF-481 | Spell Shrieker | Imagem individual adequada ainda nao adquirida e validada. |
| TF-482 | Spore Thrall | Imagem individual adequada ainda nao adquirida e validada. |
| TF-483 | Squashling | Imagem individual adequada ainda nao adquirida e validada. |
| TF-485 | Goblin Boss | Imagem individual adequada ainda nao adquirida e validada. |
| TF-486 | Goblin Cursespitter | Imagem individual adequada ainda nao adquirida e validada. |
| TF-489 | Swarm of Skitterlings | Imagem individual adequada ainda nao adquirida e validada. |
| TF-490 | Goblin Lackey | Imagem individual adequada ainda nao adquirida e validada. |
| TF-491 | Blazing Black Pudding | Imagem individual adequada ainda nao adquirida e validada. |
| TF-492 | Slime Mold | Imagem individual adequada ainda nao adquirida e validada. |
| TF-493 | Rock Troll | Imagem individual adequada ainda nao adquirida e validada. |
| TF-494 | Askwise Keeper | Imagem individual adequada ainda nao adquirida e validada. |
| TF-495 | Mykand | Imagem individual adequada ainda nao adquirida e validada. |
| TF-496 | Tyskri | Imagem individual adequada ainda nao adquirida e validada. |
| TF-497 | Faun | Imagem individual adequada ainda nao adquirida e validada. |
| TF-499 | Cloud of Ghasthoppers | Imagem individual adequada ainda nao adquirida e validada. |
| TF-500 | Gorger Zombie Horde | Imagem individual adequada ainda nao adquirida e validada. |
| TF-501 | Lost Prospector | Imagem individual adequada ainda nao adquirida e validada. |
| TF-502 | Ghasthopper | Imagem individual adequada ainda nao adquirida e validada. |
| TF-503 | Stuffed Crab | Imagem individual adequada ainda nao adquirida e validada. |
| TF-504 | Warlord's Ghost | Imagem individual adequada ainda nao adquirida e validada. |
| TF-505 | Demilich Mastermind | Imagem individual adequada ainda nao adquirida e validada. |
| TF-506 | Mariner Ghost Swarm | Imagem individual adequada ainda nao adquirida e validada. |
| TF-507 | Fogborn Skeleton Horde | Imagem individual adequada ainda nao adquirida e validada. |
| TF-508 | Fogborn Zombie | Imagem individual adequada ainda nao adquirida e validada. |
| TF-509 | Fogborn Zombie Horde | Imagem individual adequada ainda nao adquirida e validada. |
| TF-510 | Infernal Mammoth | Imagem individual adequada ainda nao adquirida e validada. |
| TF-511 | Fiendbloom Awakened Tree | Imagem individual adequada ainda nao adquirida e validada. |
| TF-513 | Improved Spirit Soldier | Imagem individual adequada ainda nao adquirida e validada. |
| TF-514 | Drainpipe Gargoyle | Imagem individual adequada ainda nao adquirida e validada. |
| TF-515 | Malcubus | Imagem individual adequada ainda nao adquirida e validada. |
| TF-516 | Kanos Spawn | Imagem individual adequada ainda nao adquirida e validada. |
| TF-517 | Imp Flock | Imagem individual adequada ainda nao adquirida e validada. |
| TF-518 | Infernal Dwarf | Imagem individual adequada ainda nao adquirida e validada. |
| TF-521 | Bugbear Door Breaker | Imagem individual adequada ainda nao adquirida e validada. |
| TF-522 | Crime Boss | Imagem individual adequada ainda nao adquirida e validada. |
| TF-523 | Pugilist | Encontrada apenas arte de Clockwork Pugilist; identidade diferente, nao reutilizar. |

## Controle de checkpoints

- #1: 4 imagens, commit `d5c3301e83107e2a994669536f992f2d54c0cc78`; IDs TF-270, TF-285, TF-409, TF-519.
- #2: 7 imagens, commit `3592249f6fec9b0b1f670f4c0e19bf1d86d62881`; IDs TF-272, TF-278, TF-279, TF-280, TF-289, TF-290, TF-309.
- #3: 7 imagens, commit `cb2efc6c0c32e9199159aed9b92019d8be54584e`; IDs TF-316, TF-317, TF-318, TF-319, TF-320, TF-325, TF-328.
- #4: 7 imagens, commit `829ac622122a801b48d748918c6d8c05f5df6c3a`; IDs TF-329, TF-330, TF-331, TF-332, TF-334, TF-339, TF-340.
- #5: 7 imagens, commit `c2d81bd1449c7af5461cdafad05e51e351033bd9`; IDs TF-343, TF-348, TF-363, TF-365, TF-367, TF-369, TF-378.
- #6: 7 imagens, commit `1d09e3466e4aa409332cf0633f8c63a10828e53c`; IDs TF-382, TF-388, TF-392, TF-394, TF-401, TF-406, TF-416.
- #7: 7 imagens, commit `9cb21b65cee8487bce8cd44db8a9002acb656879`; IDs TF-288, TF-292, TF-296, TF-302, TF-305, TF-350, TF-413.
- #8: 7 imagens, commit `02ec8bd8a5fc47be8867d4bc398a3f9b85b75ab3`; IDs TF-297, TF-298, TF-299, TF-300, TF-304, TF-312, TF-333.
- #9: 7 imagens, commit `b5404483493fb8f9c9330af7608f30ef8696c41f`; IDs TF-345, TF-347, TF-349, TF-368, TF-372, TF-385, TF-412.
- #10: 7 imagens, commit `dd89b865389ab6a379885ed5220ddf6bad85b3ab`; IDs TF-306, TF-346, TF-366, TF-415, TF-417, TF-421, TF-423.
- #11: 5 imagens, commit `f1f2c9a0dfae6b4d0582456d5a0e4f5bf0a7ae5d`; IDs TF-273, TF-277, TF-293, TF-301, TF-364.
- #12: 7 imagens, commit `0a06d9a576370c8a8c27b61f39e8f95294d2f48d`; IDs TF-418, TF-419, TF-424, TF-426, TF-396, TF-403, TF-407.
- #13: 2 imagens, commit `bed2dca7b66e22dfb2306d4dcbb758d026aab914`; IDs TF-373, TF-410.

**Estado:** parcial; **não** declarar 194 concluídos. Manter PR em rascunho, não executar merge.
