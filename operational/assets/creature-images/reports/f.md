# SRD Card Game 607 — Imagens grupo F (parcial)

## Preflight e escopo

- Repositório: `george-vepo/SRD-Card-Game-607-Supervisor`
- Commit-base e destino da PR: `a962c48a1169c2ef2be8137715a095a596753b32` / `chatgpt/srd607-research-checkpoints-20261011`
- Branch de trabalho exclusiva: `chatgpt/srd607-image-assets-f`.
- CSV de referência: `operational/research/catalog-ledger-20261011-v27/catalog-status.csv` (blob `9b703f40bb33b778992d0ba06a20704b19b3c9eb`).
- 584 registros com `Imagem` não iniciando em `VERIFICADA`; exatamente 194 posições em `pending_images.slice(390,584)`, de `TF-270` a `TF-523`, sem assumir sequencialidade.
- Preflight: branch de destino estava no commit-base informado. Branches paralelas de pesquisa presentes; arquivos globais e lotes D/E não foram modificados.

## Resultado real

| Métrica | Valor |
|---|---:|
| Esperado neste grupo | 194 |
| Binários efetivamente persistidos no GitHub | 4 |
| Binários recuperados e validados após upload | 4 |
| Pendências de aquisição | 190 |
| Total de bytes em arquivos publicados | 113088 |
| Checkpoints de imagens | 1 (4 imagens, abaixo do limite de 10) |

**Commit que persistiu os PNGs:** `d5c3301e83107e2a994669536f992f2d54c0cc78`.

## Imagens publicadas e verificadas

| ID | Criatura | Fonte | Arquivo | Dimensões | Bytes | SHA-256 | Validação |
|---|---|---|---|---|---:|---|---|
| TF-270 | Black Shuck | [origem](https://github.com/seanperkins/isekai-game/blob/HEAD/assets/sheets/anim_wolf_black_shuck.png) | `TF-270.png` | 512×809 | 80532 | `811ad2b19e7381185f49cbc043a8c754446a8dc7a3de5041723ee2141a3468cb` | Validado |
| TF-285 | Snallygaster | [origem](https://github.com/Koopro/wizards_and_beasts/blob/HEAD/src/main/resources/assets/wizards_and_beasts/textures/entity/snallygaster.png) | `TF-285.png` | 64×80 | 3383 | `22fd75617163949e41d82203a4c3142d9cf499c6d1b20169111783b879bcf11c` | Validado |
| TF-409 | Mandrake | [origem](https://github.com/tpgame-spbstu/Tabletop-roguelike/blob/HEAD/Card/Textures/Earth%20Mandrake.png) | `TF-409.png` | 152×203 | 25756 | `4b1b747fed486975ef9715a0f8fc980ba86d6ddb8916eee96b39901ad950ce8a` | Validado |
| TF-519 | Frilled Lizard | [origem](https://github.com/ANTALLIS/grahams-game/blob/HEAD/rltiles/mon/animals/frilled_lizard.png) | `TF-519.png` | 32×32 | 3417 | `cce2fa7f14e82fa99082e2bb0b0e0c45f5a58dd78b05d697abbfd89bcb2ebbb2` | Validado |

Todos os quatro arquivos estão em `operational/assets/creature-images/`, com extensão PNG e MIME `image/png`. A verificação recuperou os arquivos binários por `fetch_file` na branch de trabalho, confirmou igualdade integral dos bytes com suas fontes originais e o SHA do blob Git. O SHA-256 foi calculado a partir dos bytes de origem que se mostraram idênticos aos bytes persistidos. Assinatura PNG e dimensões foram verificadas antes do upload.

**Nota de qualidade:** `TF-285` (64×80) e `TF-519` (32×32) são imagens pequenas, embora válidas; recomendável substituir por arte de maior resolução antes da etapa visual final das cartas.

## IDs ainda bloqueados para aquisição (190)

Estes IDs **não têm arquivo adquirido nesta branch**. Não há alegação de conclusão, nem placeholders. A pendência não equivale a prova de indisponibilidade de imagem na internet: exige pesquisa, identificação e validação individual posterior.

| ID | Criatura | Motivo |
|---|---|---|
| TF-272 | Light Eater | Fonte binária adequada ainda não obtida/verificada |
| TF-273 | Shoth, Sooze | Fonte binária adequada ainda não obtida/verificada |
| TF-274 | Malleable, Minor | Fonte binária adequada ainda não obtida/verificada |
| TF-275 | Maw Swarm | Fonte binária adequada ainda não obtida/verificada |
| TF-276 | Malleable, Moderate | Fonte binária adequada ainda não obtida/verificada |
| TF-277 | Shoth, Oth | Fonte binária adequada ainda não obtida/verificada |
| TF-278 | Snatch Bat | Fonte binária adequada ainda não obtida/verificada |
| TF-279 | Fate Eater | Fonte binária adequada ainda não obtida/verificada |
| TF-280 | Mamura | Fonte binária adequada ainda não obtida/verificada |
| TF-283 | Shukankor | Fonte binária adequada ainda não obtida/verificada |
| TF-284 | Malleable, Major | Fonte binária adequada ainda não obtida/verificada |
| TF-286 | Malleable, Massive | Fonte binária adequada ainda não obtida/verificada |
| TF-288 | Snake, Swamp Adder | Fonte binária adequada ainda não obtida/verificada |
| TF-289 | Porcellina | Fonte binária adequada ainda não obtida/verificada |
| TF-290 | Glass Gator | Fonte binária adequada ainda não obtida/verificada |
| TF-291 | Hlaupa | Fonte binária adequada ainda não obtida/verificada |
| TF-292 | Snake, Zanskaran Viper | Fonte binária adequada ainda não obtida/verificada |
| TF-293 | Planar Flora, Hallowed Reeds | Fonte binária adequada ainda não obtida/verificada |
| TF-295 | Greater Spirit Soldier | Fonte binária adequada ainda não obtida/verificada |
| TF-296 | Angel, Psychopomp | Fonte binária adequada ainda não obtida/verificada |
| TF-297 | Simurg | Fonte binária adequada ainda não obtida/verificada |
| TF-298 | Angel, Song | Fonte binária adequada ainda não obtida/verificada |
| TF-299 | Angel, Sammael | Fonte binária adequada ainda não obtida/verificada |
| TF-300 | Angel, Zoryas | Fonte binária adequada ainda não obtida/verificada |
| TF-301 | Planar Flora, Ecstatic Bloom | Fonte binária adequada ainda não obtida/verificada |
| TF-302 | Angel, Shrouded | Fonte binária adequada ainda não obtida/verificada |
| TF-303 | Angel, Uridimmu | Fonte binária adequada ainda não obtida/verificada |
| TF-304 | Living Star | Fonte binária adequada ainda não obtida/verificada |
| TF-305 | Angel, Zirnitran | Fonte binária adequada ainda não obtida/verificada |
| TF-306 | Simian, Monkey King | Fonte binária adequada ainda não obtida/verificada |
| TF-309 | Living Wick | Fonte binária adequada ainda não obtida/verificada |
| TF-311 | Bolt-Thrower | Fonte binária adequada ainda não obtida/verificada |
| TF-312 | Sigilian | Fonte binária adequada ainda não obtida/verificada |
| TF-316 | Soil Snake | Fonte binária adequada ainda não obtida/verificada |
| TF-317 | Faux-Garou | Fonte binária adequada ainda não obtida/verificada |
| TF-318 | Fellforged | Fonte binária adequada ainda não obtida/verificada |
| TF-319 | Gearforged Templar | Fonte binária adequada ainda não obtida/verificada |
| TF-320 | Gnarljak | Fonte binária adequada ainda não obtida/verificada |
| TF-321 | Blood Guardian | Fonte binária adequada ainda não obtida/verificada |
| TF-324 | Green Kobold Drake | Fonte binária adequada ainda não obtida/verificada |
| TF-325 | Lindwurm | Fonte binária adequada ainda não obtida/verificada |
| TF-326 | Linnorm, Vent | Fonte binária adequada ainda não obtida/verificada |
| TF-327 | Azer Forgemaster | Fonte binária adequada ainda não obtida/verificada |
| TF-328 | Gnyan | Fonte binária adequada ainda não obtida/verificada |
| TF-329 | Living Soot | Fonte binária adequada ainda não obtida/verificada |
| TF-330 | Spark | Fonte binária adequada ainda não obtida/verificada |
| TF-331 | Liosalfar | Fonte binária adequada ainda não obtida/verificada |
| TF-332 | Slow Storm | Fonte binária adequada ainda não obtida/verificada |
| TF-333 | Living Shade | Fonte binária adequada ainda não obtida/verificada |
| TF-334 | Far Darrig | Fonte binária adequada ainda não obtida/verificada |
| TF-335 | Woe Siphon | Fonte binária adequada ainda não obtida/verificada |
| TF-336 | Far Dorocha | Fonte binária adequada ainda não obtida/verificada |
| TF-338 | Somberweave | Fonte binária adequada ainda não obtida/verificada |
| TF-339 | Malphas | Fonte binária adequada ainda não obtida/verificada |
| TF-340 | Wilderness Crone | Fonte binária adequada ainda não obtida/verificada |
| TF-341 | Shurale | Fonte binária adequada ainda não obtida/verificada |
| TF-342 | Silenal | Fonte binária adequada ainda não obtida/verificada |
| TF-343 | Fear Smith | Fonte binária adequada ainda não obtida/verificada |
| TF-344 | Pumpkin King | Fonte binária adequada ainda não obtida/verificada |
| TF-345 | Animal Lord, Mouse King | Fonte binária adequada ainda não obtida/verificada |
| TF-346 | Animal Lord, Lord of Vultures | Fonte binária adequada ainda não obtida/verificada |
| TF-347 | Animal Lord, Bat King | Fonte binária adequada ainda não obtida/verificada |
| TF-348 | Life Broker | Fonte binária adequada ainda não obtida/verificada |
| TF-349 | Animal Lord, Brother Ox | Fonte binária adequada ainda não obtida/verificada |
| TF-350 | Ettin, Kobold | Fonte binária adequada ainda não obtida/verificada |
| TF-351 | Half-Demon Ogre | Fonte binária adequada ainda não obtida/verificada |
| TF-353 | Manggus | Fonte binária adequada ainda não obtida/verificada |
| TF-355 | Giant, Hill Chief | Fonte binária adequada ainda não obtida/verificada |
| TF-356 | Grendel | Fonte binária adequada ainda não obtida/verificada |
| TF-358 | Giant, Void | Fonte binária adequada ainda não obtida/verificada |
| TF-360 | Gelatinous Wall | Fonte binária adequada ainda não obtida/verificada |
| TF-361 | Elder Black Pudding | Fonte binária adequada ainda não obtida/verificada |
| TF-363 | Puffinfolk | Fonte binária adequada ainda não obtida/verificada |
| TF-364 | Simian, Kapi | Fonte binária adequada ainda não obtida/verificada |
| TF-365 | Erina, Defender | Fonte binária adequada ainda não obtida/verificada |
| TF-366 | Simian, Vanara | Fonte binária adequada ainda não obtida/verificada |
| TF-367 | Erina, Tussler | Fonte binária adequada ainda não obtida/verificada |
| TF-368 | Gnoll Slaver | Fonte binária adequada ainda não obtida/verificada |
| TF-369 | Gnoll, Havoc Runner | Fonte binária adequada ainda não obtida/verificada |
| TF-370 | Simian, Sulsha | Fonte binária adequada ainda não obtida/verificada |
| TF-372 | Gnomish Knife Cultist | Fonte binária adequada ainda não obtida/verificada |
| TF-373 | Kobold, Wizard | Fonte binária adequada ainda não obtida/verificada |
| TF-376 | Heshgarat Cat | Fonte binária adequada ainda não obtida/verificada |
| TF-378 | Mahoru | Fonte binária adequada ainda não obtida/verificada |
| TF-379 | Snake with a Hundred Mage Hands | Fonte binária adequada ainda não obtida/verificada |
| TF-380 | Stone Shark | Fonte binária adequada ainda não obtida/verificada |
| TF-381 | Aracnecore | Fonte binária adequada ainda não obtida/verificada |
| TF-382 | Likho | Fonte binária adequada ainda não obtida/verificada |
| TF-384 | Mutant Rust Monster | Fonte binária adequada ainda não obtida/verificada |
| TF-385 | Mantik | Fonte binária adequada ainda não obtida/verificada |
| TF-386 | Grootslang | Fonte binária adequada ainda não obtida/verificada |
| TF-388 | Son of Fenris | Fonte binária adequada ainda não obtida/verificada |
| TF-389 | Supermutant Rust Monster | Fonte binária adequada ainda não obtida/verificada |
| TF-392 | Malmbjorn | Fonte binária adequada ainda não obtida/verificada |
| TF-393 | Minotaur Conqueror | Fonte binária adequada ainda não obtida/verificada |
| TF-394 | Shroud | Fonte binária adequada ainda não obtida/verificada |
| TF-395 | Skeleton, Cackling | Fonte binária adequada ainda não obtida/verificada |
| TF-396 | Skeleton, Clacking | Fonte binária adequada ainda não obtida/verificada |
| TF-397 | Fane Spirit | Fonte binária adequada ainda não obtida/verificada |
| TF-398 | Falsifier Fog | Fonte binária adequada ainda não obtida/verificada |
| TF-399 | Mari Lwyd | Fonte binária adequada ainda não obtida/verificada |
| TF-400 | Headless Horseman | Fonte binária adequada ainda não obtida/verificada |
| TF-401 | Mallqui | Fonte binária adequada ainda não obtida/verificada |
| TF-402 | Marsh Dire | Fonte binária adequada ainda não obtida/verificada |
| TF-403 | Lich, Hierophant | Fonte binária adequada ainda não obtida/verificada |
| TF-405 | Lich, Virtuoso | Fonte binária adequada ainda não obtida/verificada |
| TF-406 | Mask Wight | Fonte binária adequada ainda não obtida/verificada |
| TF-407 | Lich, Pact | Fonte binária adequada ainda não obtida/verificada |
| TF-408 | Grove Swarm | Fonte binária adequada ainda não obtida/verificada |
| TF-410 | Fungi, Wirbeln | Fonte binária adequada ainda não obtida/verificada |
| TF-411 | Garlicle | Fonte binária adequada ainda não obtida/verificada |
| TF-412 | Mandrake, Great | Fonte binária adequada ainda não obtida/verificada |
| TF-413 | Sinstar, Star Thrall | Fonte binária adequada ainda não obtida/verificada |
| TF-414 | Wallflower | Fonte binária adequada ainda não obtida/verificada |
| TF-415 | Gloomflower | Fonte binária adequada ainda não obtida/verificada |
| TF-416 | Wind Witch | Fonte binária adequada ainda não obtida/verificada |
| TF-417 | Mandriano | Fonte binária adequada ainda não obtida/verificada |
| TF-418 | Sodwose | Fonte binária adequada ainda não obtida/verificada |
| TF-419 | Witchalder | Fonte binária adequada ainda não obtida/verificada |
| TF-420 | Mandriano, Ancient | Fonte binária adequada ainda não obtida/verificada |
| TF-421 | Planar Flora, Execrable Shrub | Fonte binária adequada ainda não obtida/verificada |
| TF-423 | Spawn of Chernobog | Fonte binária adequada ainda não obtida/verificada |
| TF-424 | Soul Eater | Fonte binária adequada ainda não obtida/verificada |
| TF-425 | Snow Terror | Fonte binária adequada ainda não obtida/verificada |
| TF-426 | Planar Flora, Thorned Sulfurlord | Fonte binária adequada ainda não obtida/verificada |
| TF-428 | Cerberus Guardian | Fonte binária adequada ainda não obtida/verificada |
| TF-429 | Clockwork Sentinel | Fonte binária adequada ainda não obtida/verificada |
| TF-431 | Conjured Guardian | Fonte binária adequada ainda não obtida/verificada |
| TF-434 | Crusher | Fonte binária adequada ainda não obtida/verificada |
| TF-442 | Flame-Spitting Statue | Fonte binária adequada ainda não obtida/verificada |
| TF-444 | Flesh Guardian | Fonte binária adequada ainda não obtida/verificada |
| TF-446 | Grave Guardian | Fonte binária adequada ainda não obtida/verificada |
| TF-447 | Hound Guardian | Fonte binária adequada ainda não obtida/verificada |
| TF-448 | Imprisoned Celestial | Fonte binária adequada ainda não obtida/verificada |
| TF-449 | Imprisoned Fiend | Fonte binária adequada ainda não obtida/verificada |
| TF-450 | Iron Guardian | Fonte binária adequada ainda não obtida/verificada |
| TF-456 | Scarecrow Harvester | Fonte binária adequada ainda não obtida/verificada |
| TF-459 | Ankheg Empress | Fonte binária adequada ainda não obtida/verificada |
| TF-461 | Ankheg Spawn | Fonte binária adequada ainda não obtida/verificada |
| TF-462 | Behir Magus | Fonte binária adequada ainda não obtida/verificada |
| TF-463 | Blood Maggot | Fonte binária adequada ainda não obtida/verificada |
| TF-465 | Canicore | Fonte binária adequada ainda não obtida/verificada |
| TF-467 | Corpse Fly | Fonte binária adequada ainda não obtida/verificada |
| TF-468 | Faerie Chimera | Fonte binária adequada ainda não obtida/verificada |
| TF-469 | Fateholder | Fonte binária adequada ainda não obtida/verificada |
| TF-470 | Fiendish Chimera | Fonte binária adequada ainda não obtida/verificada |
| TF-471 | Fiendish Dire Boar | Fonte binária adequada ainda não obtida/verificada |
| TF-473 | Flying Lion | Fonte binária adequada ainda não obtida/verificada |
| TF-474 | Giant Grick | Fonte binária adequada ainda não obtida/verificada |
| TF-475 | Giant Lanternfish | Fonte binária adequada ainda não obtida/verificada |
| TF-476 | Greater Sphinx | Fonte binária adequada ainda não obtida/verificada |
| TF-477 | Grimalkin | Fonte binária adequada ainda não obtida/verificada |
| TF-478 | Gourdling | Fonte binária adequada ainda não obtida/verificada |
| TF-480 | Sewer Walker | Fonte binária adequada ainda não obtida/verificada |
| TF-481 | Spell Shrieker | Fonte binária adequada ainda não obtida/verificada |
| TF-482 | Spore Thrall | Fonte binária adequada ainda não obtida/verificada |
| TF-483 | Squashling | Fonte binária adequada ainda não obtida/verificada |
| TF-485 | Goblin Boss | Fonte binária adequada ainda não obtida/verificada |
| TF-486 | Goblin Cursespitter | Fonte binária adequada ainda não obtida/verificada |
| TF-489 | Swarm of Skitterlings | Fonte binária adequada ainda não obtida/verificada |
| TF-490 | Goblin Lackey | Fonte binária adequada ainda não obtida/verificada |
| TF-491 | Blazing Black Pudding | Fonte binária adequada ainda não obtida/verificada |
| TF-492 | Slime Mold | Fonte binária adequada ainda não obtida/verificada |
| TF-493 | Rock Troll | Fonte binária adequada ainda não obtida/verificada |
| TF-494 | Askwise Keeper | Fonte binária adequada ainda não obtida/verificada |
| TF-495 | Mykand | Fonte binária adequada ainda não obtida/verificada |
| TF-496 | Tyskri | Fonte binária adequada ainda não obtida/verificada |
| TF-497 | Faun | Fonte binária adequada ainda não obtida/verificada |
| TF-499 | Cloud of Ghasthoppers | Fonte binária adequada ainda não obtida/verificada |
| TF-500 | Gorger Zombie Horde | Fonte binária adequada ainda não obtida/verificada |
| TF-501 | Lost Prospector | Fonte binária adequada ainda não obtida/verificada |
| TF-502 | Ghasthopper | Fonte binária adequada ainda não obtida/verificada |
| TF-503 | Stuffed Crab | Fonte binária adequada ainda não obtida/verificada |
| TF-504 | Warlord's Ghost | Fonte binária adequada ainda não obtida/verificada |
| TF-505 | Demilich Mastermind | Fonte binária adequada ainda não obtida/verificada |
| TF-506 | Mariner Ghost Swarm | Fonte binária adequada ainda não obtida/verificada |
| TF-507 | Fogborn Skeleton Horde | Fonte binária adequada ainda não obtida/verificada |
| TF-508 | Fogborn Zombie | Fonte binária adequada ainda não obtida/verificada |
| TF-509 | Fogborn Zombie Horde | Fonte binária adequada ainda não obtida/verificada |
| TF-510 | Infernal Mammoth | Fonte binária adequada ainda não obtida/verificada |
| TF-511 | Fiendbloom Awakened Tree | Fonte binária adequada ainda não obtida/verificada |
| TF-513 | Improved Spirit Soldier | Fonte binária adequada ainda não obtida/verificada |
| TF-514 | Drainpipe Gargoyle | Fonte binária adequada ainda não obtida/verificada |
| TF-515 | Malcubus | Fonte binária adequada ainda não obtida/verificada |
| TF-516 | Kanos Spawn | Fonte binária adequada ainda não obtida/verificada |
| TF-517 | Imp Flock | Fonte binária adequada ainda não obtida/verificada |
| TF-518 | Infernal Dwarf | Fonte binária adequada ainda não obtida/verificada |
| TF-521 | Bugbear Door Breaker | Fonte binária adequada ainda não obtida/verificada |
| TF-522 | Crime Boss | Fonte binária adequada ainda não obtida/verificada |
| TF-523 | Pugilist | Fonte binária adequada ainda não obtida/verificada |

## Controle de integridade e continuidade

- Nenhum arquivo `catalog-status.csv`, ledger, imagem verificada do catálogo ou imagem dos grupos D/E foi editado.
- Os hashes SHA-256 por criatura e seus caminhos completos estão em `manifests/f.json`.
- Não houve merge. A PR permanece em rascunho.
- Próxima execução: pesquisar fontes específicas para os 190 IDs pendentes, enviar somente binários válidos em checkpoints de até 10 e atualizar o relatório com contagem comprovada.
