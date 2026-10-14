# SRD Card Game 607 — auditoria da pesquisa mecânica C

**Commit-base:** `a962c48a1169c2ef2be8137715a095a596753b32`. **Branch:** `chatgpt/srd607-deep-mechanics-c`. **Data:** 14/10/2026.

## Checkpoint 28 — quatro blocos oficiais A5E (14/10/2026)

- TF-507 **Fogborn Skeleton Horde**: HP 65 (10d8+20), AC13, resistência a terreno via Fogwalk com trajetória horizontal e névoa 1 turno, Water Walker, Area Vulnerability, Horde, Horde Dispersal em 1d4 skeletons com 6 PV cada, Shortsword e Shortbow +4 (5d6+10; metade se bloodied). Fonte https://a5e.tools/node/3460.
- TF-509 **Fogborn Zombie Horde**: HP 75 (10d8+30), AC8, Fogwalk/Water Walker e regras de horda distintas, dispersão em 1d4 zombies com 7 PV, Grab +3 agarrando Medium ou menor (escape CD11), Bite +3 somente em grappled e cura igual ao dano. Fonte https://a5e.tools/node/3462.
- TF-518 **Infernal Dwarf**: INT 15, armadura óssea, 5º nível de spellcasting 4/3/2 spell slots, cantrips, United in Action, Bone Warhammer +4, 5 magias de ação e Shield reação. **BLOQUEADA**: Ray of Frost remete erroneamente à duração do 'noble's next turn'. Fonte https://a5e.tools/node/3425.
- TF-521 **Bugbear Door Breaker**: gauntlets com Loading Weapon/Reload, duas gauntlets para Multiattack, breaker, Smoke Screen reação (4–6), Clear the Way, Smoky Sight e Long Arms. **BLOQUEADA**: 60 PV impresso vs 5d10+10 (média 37,5), alcance 5 vs 10 ft e texto de sucesso de Clear the Way truncado. Fonte https://a5e.tools/node/4185.
- Nenhuma correção especulativa nem imagem física nova. Contagens: **45 aprofundadas; 86 ainda sem revalidação; 92 parciais, 39 bloqueadas; 0 verificadas integralmente**.


## Checkpoint 27 — confronto com fonte editorial Gate Pass Gazette (14/10/2026)

- Commit `9d6386ea894bfbb62d4e72f68b2dfe140fc44508` confirmado com read-back independente de TF-503 e TF-499; ambos JSONs válidos, IDs corretos e evidências no arquivo individual.

- **TF-503 Stuffed Crab:** confrontado com o SRD editorial original [Gate Pass Gazette #2](https://static1.squarespace.com/static/63d11ec201a57a0efa51a168/t/65f3132a921c356dd0ee11ab/1710428970230/!GPG%2BIssue%2B%232%2BSRD.pdf), página PDF 15. Confirmados CR 6, **2.300 XP**, CA14 e PV104. O texto da saída dos ghouls após 0 PV já está truncado no material original; **mantém bloqueio até errata**, sem assumir como funciona. Dano de queda de ghoul no piso perfurado é regra situacional do encontro, separada das habilidades.
- **TF-499 Cloud of Ghasthoppers:** publicação individual confirmada em [Gate Pass Gazette #24](https://a5e.tools/node/3976) na lista da editora. A fonte oficial continua omitindo o teste de salvaguarda da Despair Aura; **permanece bloqueada**.
- **Checkpoint 26 confirmado por read-back:** TF-126, TF-127, TF-129, TF-131, commit `e24797b798bf94163a4efa80e2df4ba681e9e85b`.
- Não cria imagens ou preenche campos por suposição; **41 fichas aprofundadas, 90 sem revisão detalhada, 94 parciais, 37 bloqueadas, 0 integralmente aprovadas**.


## Checkpoint 26 — gigantes e ogre Kobold Press (14/10/2026)

- Commit mecânico `e24797b798bf94163a4efa80e2df4ba681e9e85b`, leitura de retorno confirmada para os quatro JSONs do checkpoint.

- TF-126 Giant, Abbanith: One with the Earth, Siege Monster com multiplicadores distintos de objetos, dois Thumb Claw e Earth Counter (reação recarga 6 apenas earth/stone spells, sem check de spell level). https://www.5esrd.com/database/creature/giant-abbanith/
- TF-127 Giant, Laestrigonian: Multiattack Greatclub+Bite, Rock melee/ranged e doença por Bite que impede cura não mágica e reduz PV máximos a cada 24h. https://www.5esrd.com/database/creature/giant-laestrigonian/
- TF-129 Giant, Snow: imunidade cold, vulnerabilidade fire, regeneração condicional à neve, camuflagem, duas Club e Giant Snowball com cegueira após falha DES CD16. https://www.5esrd.com/database/creature/giant-snow/
- TF-131 Ogre, Rainforest: Multiattack separado por forma ogre/boar; Spear apenas ogre, Tusk apenas boar, Bite em ambas, Devouring Charge com bônus condicional e Change Shape sem alteração de equipamento. https://www.5esrd.com/database/creature/ogre-rainforest/
- As 4 imagens binárias já existiam no diretório C, sem aprovação visual; as quatro fichas permanecem parciais por pendência de confronto com publicação editorial original e erratas. Total: **41 aprofundadas, 90 sem revalidação**, 94 parciais e 37 bloqueadas.

## Checkpoint 25 — Kanos Spawn e Imp Flock (14/10/2026)

- Commit `97b58fda82c41a311d7a3f149907600daadceea3` relido, JSONs TF-516 e TF-517 válidos por leitura sintática e ID.


- TF-516 Kanos Spawn: Pack Tactics, Wall Walker, dois ataques Claw, Icy Breath com recarga 6, frio, restrição, obscurecimento e Hide em ação bônus. **Bloqueio editorial:** 'raptor' aparece em texto de Pack Tactics e Skills Stealth não informa bônus. Fonte: https://a5e.tools/node/2991.
- TF-517 Imp Flock: Chaos of Combat CON CD(5 + nível da magia), Devil's Sight, Evil, Swarm com tamanho Large/Medium, Hellswarm + dano condicionado de poison, Innate Spellcasting shatter. **Bloqueio editorial:** usos de shatter não declarados. Fonte: https://a5e.tools/node/3394.
- Sem novas imagens físicas; 0 fichas promovidas integrais. Total **37** detalhadas, **94** pendentes de revalidação, 95 parciais e 36 bloqueadas.

## Checkpoint 24 — Fiendbloom e Crime Boss (14/10/2026)

- Commit `e6f46a3ac27d748e564076e7cf2d904f346fa619` relido; TF-511 e TF-522 válidos, IDs confirmados.
- Bloqueio adicional TF-511: Hellspore Seeding afeta cada criatura, mas regra específica da doença se refere a humanoides; resolver antes de aplicar a outros tipos.


- TF-511 Fiendbloom Awakened Tree: False Appearance, Doubletyped Fiend+Plant, Dreaded Winter, Hellspore Seeding, Slam e referência estruturada à regra externa Hellspore Blight (tier 2 DC14). Fontes https://a5e.tools/node/3414 e https://a5e.tools/rules/disease-hellspore-blight-tier-2-3.
- TF-522 Crime Boss: 3 Shortsword, Dagger, Mark for Death, Command Bodyguard e Offhand Dagger com bônus, alcance, duração e gatilhos. Dano adicional de Mark for Death sem tipo explícito mantido indeterminado. Fonte https://a5e.tools/node/1895.
- Nenhuma imagem física adicional; permanecem parciais e aguardam revisão editorial. Acumulado: **35 detalhadas**, **96 sem nova revisão**, 97 parciais, 34 bloqueadas.

## Checkpoint 23 — Demilich, Mariner e Mammoth (14/10/2026)

- Commit mecânico `86e088bb6e7d1e66982f927166813e6887d49e7a`; leitura de retorno de TF-505, TF-506 e TF-510: OK.

- TF-505 Demilich Mastermind: 319 HP / CR18, cinco Legendary Resistance, quatro soul gems, Devour Soul, Reflection Arcane/Skull Shock bloodied, quatro ações lendárias com custos; optional lair features mantidas separadas de ações de covil. Fonte: https://a5e.tools/node/1478. Dust Storm omite resultado no sucesso; ainda parcial.
- TF-506 Mariner Ghost Swarm: Elite Recovery, Ethereal Sight, Swarm, Turn Resistance, Withering Cutlasses, Magic Blast, Etherealness, Spirit Absorption e Painful Wail estruturadas com limites e efeitos. Fonte: https://a5e.tools/node/3406.
- TF-510 Infernal Mammoth: Siege Platform, Trampling Charge, Gore, Stomp e Opportunity Step; **bloqueada** por 104 HP / 11d12+33 com CON20 (+5), que conflita com fórmula padrão. Fonte: https://a5e.tools/node/3426.
- Nenhuma imagem nova persistida nem promoção mecânica completa. Acumulado: **33 detalhadas, 98 ainda sem revisão; 97 parciais, 34 bloqueadas**.


## Checkpoint 22 — fontes oficiais A5E (14/10/2026)

- Commit mecânico `397757486790b6d31c911f95b18d821ceff018ff`; leitura confirmada de TF-499, TF-501, TF-503 e TF-504 pela API GitHub, IDs/JSON válidos.

- TF-499 Cloud of Ghasthoppers: Swarm, Incorporeal Movement, Smoky Signals, Bleak Vibrations e Drain Health estruturados, variantes bloodied. **BLOQUEADA**: Despair Aura menciona salvaguarda sem CD, atributo ou momento do teste. Fonte: https://a5e.tools/node/4002.
- TF-501 Lost Prospector: estatísticas, seis traços, Withering Touch, Ethereal Jaunt, Horrifying Visage, Possession com condições, fim/repetição de salvaguardas, recurso bônus de encerrar e reação. Fonte: https://a5e.tools/node/2965.
- TF-503 Stuffed Crab: sete ghouls, quadrados do alvo, Multiattack com duas Pincer, grapple CD16, ação bônus Stuffing. **BLOQUEADA** por texto de saída de ghouls truncado e fuga de Stuffing incompleta. Fonte: https://a5e.tools/node/2213.
- TF-504 Warlord's Ghost: Death Howl, Unquiet Spirit, Presage Death, Baleful Wail e reação Wounded Warning estruturados. **BLOQUEADA**: fonte mistura 'banshee' com nome da variante e não informa efeito de teste bem-sucedido no Wail. Fonte: https://a5e.tools/node/1464.
- Sem novo arquivo de imagem física, 0 fichas promovidas como mecanicamente completas. **30 aprofundadas, 101 ainda sem revalidação, 98 parciais, 33 bloqueadas**.


## Checkpoint 21 — variantes A5E e Greater Sphinx (14/10/2026)

- Commit mecânico `456458a009be9af1972e54e7568a7f313f29c706` publicado com 4 fichas; leitura de retorno da API confirmou JSON sintático e ID exato para TF-468, TF-470, TF-473 e TF-476.

- TF-468 **Faerie Chimera**: White Stag Headbutt, Black Wolf Bite, Silver Dragon Claw, Breath Weapon cone 15 ft, Tail Swipe e Winged Charge. Fonte oficial descreve literalmente **fire** no sopro mas dano **cold**; ações lendárias genéricas Bite/Claw não correspondem literalmente aos nomes da variante; estado **BLOQUEADA**. [Ficha](https://a5e.tools/node/3239).
- TF-470 **Fiendish Chimera**: Nightmare Trample, Bat Bite, Hellhound Claw, sopro fire; Winged Charge referencia headbutt não listado, e ações lendárias possuem nomes genéricos; **BLOQUEADA**. [Ficha](https://a5e.tools/node/3240).
- TF-473 **Flying Lion**: Keen Smell, Bite, Talons com bônus de altura/agarre; fonte escreve Multiattack 'griffon attacks with beak and talons', mas variante não possui Beak. Não converter para Bite por suposição; **BLOQUEADA**. [Ficha](https://a5e.tools/node/1663).
- TF-476 **Greater Sphinx CR 17**: 220 PV, 3 níveis progressivos de Roar, magia inata e CDs, Speed Time e Planar Jaunt estruturados. Site oficial tem tag Legendary e texto de Combat com Claw/Teleport/Slow Time, mas **não apresenta seção de ações lendárias**; marcar categoria desconhecida e bloquear validação, jamais considerar ausência confirmada. [Ficha](https://a5e.tools/node/1797).
- Estado após checkpoint: **26** fichas aprofundadas (antes 24), **105** sem revalidação; **0** integrais, **101** parciais e **30** bloqueadas. Não foram adicionados binários de imagem; 35 continuam faltando.
- Todos os 4 JSONs mantêm evidências individuais e pendências específicas para revisão de Monstrous Menagerie/errata; nenhuma alteração fora de `operational/research/deep-mechanics/c/`.

## Checkpoint 20 — A5E (14/10/2026)

- Commit publicado e relido pela API: `2c8b33b00f2b463f76bebe8ed4cf731e2d7ad906`. 4 IDs confirmados, 4 JSONs válidos e branch mantida em rascunho.

- TF-448 Imprisoned Celestial: Divine Absorption, forma imutável, resistência mágica, Slam, Radiant Blast (5–6) e bônus Slow (5–6). Fonte oficial: https://a5e.tools/node/5406.
- TF-449 Imprisoned Fiend: Acid Absorption, Berserk, Bloodied Fury, Slam reduz PV máximo, Fiendfire Breath aplica strife A5E. Não converter conceitos A5E. Fonte: https://a5e.tools/node/5407.
- TF-459 Ankheg Empress: Bite 10 ft; Claws 15 ft; Acid Glob 30/90 ft; Acid Spray linha 60×10 ft ou no agarrado sem salvaguarda; Burrowing Ambush, Grabby, Monarch's Command, Cinch. **Divergência bloodied 65 contra metade de 174 = 87 mantida bloqueada**. Fonte: https://a5e.tools/node/3424.
- TF-462 Behir Magus: mordida, agarrar/engolir, Lightning Breath e **quatro reações individuais** (Vengeful Breath, Blindness, Invisibility, Drain Charge). Fonte: https://a5e.tools/node/1465.
- Referências visuais da espécie encontradas em site A5E para Ankheg e Behir. Não comprovam variantes Empress/Magus e nenhum arquivo binário foi gravado a partir das URLs; permanecem como candidatos.
- Acumulado: 24 fichas aprofundadas, 107 sem revalidação; 0 completas, 101 parciais, 30 bloqueadas; 96 imagens físicas e 35 faltantes.

## Auditoria de read-back — 14/10/2026

- **Checkpoints 18 e 19 efetivamente publicados**: `f869eacf0239a31a56bf2cd9e019862aa498680f` (TF-417/420/425) e `d128143197cd7cb21f2d5da96dda87cc738eafb7` (TF-414/428/431). Seis JSONs reabertos na branch, IDs exatos e sintaxe JSON verificados.
- Número de registros mecanicamente aprofundados com fonte individual: **20/131**. Outros **111** sem revalidação detalhada. **0** declarados completos; **104** parciais e **27** bloqueados.
- Diferenças preservadas: limitações de zombies TF-420, Beak/grick TF-414, mecânicas dependentes de conjurador TF-431, dependência de cabeças TF-428.
- Campos ausentes explicitados como ausentes no bloco, sem confundi-los com desconhecidos. Para A5E, XP não declarado permanece `null` e ND da invocação TF-431 continua indefinido, não `0`.
- Nenhuma imagem nova foi adquirida nos checkpoints; **96 arquivos físicos existentes e 35 IDs sem imagem** são os valores de referência anteriores, sujeitos a uma nova conferência de hash nesta execução.

## Checkpoint 18/19 — pesquisa adicional de 14/10/2026

Foram reconstruídas as fichas individuais **TF-417 Mandriano**, **TF-420 Mandriano Ancient** e **TF-425 Snow Terror**, consultando blocos completos e preservando a variante (sem reutilização mecânica). A diferença entre limite 12 undead via Consume the Spark e limite 20 zombies via Call the Dead da variante Ancient não foi resolvida por suposição. A imagem dos dois Mandrianos usa o mesmo blob e não está aprovada. As 3 fichas mantêm pendência de exemplar editorial/errata. Fonte: [Mandriano](https://kpogl.wikidot.com/monster:mandriano), [Ancient Mandriano](https://kpogl.wikidot.com/monster:ancient-mandriano), [Snow Terror](https://www.5esrd.com/database/creature/snow-terror/), [Tome of Beasts 2 transcrição](https://anyflip.com/aqmdu/uasq/basic/301-350).

Aprofundadas também **TF-414 Wallflower**, **TF-428 Cerberus Guardian** e **TF-431 Conjured Guardian** em fontes oficiais [A5E Wallflower](https://a5e.tools/node/1660), [A5E Cerberus Guardian](https://a5e.tools/node/2854), [A5E Conjured Guardian](https://a5e.tools/node/5171). TF-414 permanece bloqueada por referência a `grick` na ação bônus Beak. TF-428 preserva cabeças ativas/inativas, 4 ações lendárias e seus requisitos; evitar supor seleção automática de cabeça e efeito de falhas repetidas. TF-431 conserva ND textual `—` apesar do índice `0`; bônus de ataque, CD e proficiência dependem do conjurador.

**Nenhuma promoção mecânica integral.** Imagens faltantes para TF-414, TF-428 e TF-431; os outros três têm imagens persistidas ainda sem aprovação visual.


## Checkpoint 17 — 14/10/2026

- Commit: `4bb79b4994ca6529053ce0419279db889bc7d605`; read-back de `TF-424.json` e `TF-426.json`: **OK**.
- **TF-424 Soul Eater:** todos atributos/defesas e sentidos; resistência mágica, Soul Sense, dois ataques Claw, Hasten Consumption, penalidade condicional e reação Soul Drain, incluindo gatilho, CD, tempo/alcance de liberação e exceções de ressurreição. **Revisão de Tome of Beasts 1 original vs revisão posterior permanece pendente**; fonte comunitária [KPOGL](https://kpogl.wikidot.com/monster:soul-eater).
- **TF-426 Thorned Sulfurlord:** todas estatísticas e auras; Root como ação bônus 3/dia, Multiattack com alternativas exclusivas, Sulfur Slam, Fiery Spike e The World Shall Know Fire, inclusive pré-condição do dano de fogo anterior. Fonte [5eSRD](https://www.5esrd.com/database/creature/thorned-sulfurlord/), edição [Creature Codex](https://koboldpress.com/tools/kobold-press-monsters/).
- **Ainda são fichas PARCIAIS**, sujeitas a confronto editorial e revisão visual. Nenhuma promoção para MECANICA_COMPLETA_VERIFICADA.
- Auditoria cumulativa: **17** detalhadas e **114** sem revalidação integral; 96 imagens binárias, 35 pendentes.

## Checkpoint 16 — aprofundamento de 14/10/2026

- Commit mecânico: `5dbcc3dea2004ecdb999b6f81bdbee6e3d088620`; read-back dos JSONs **TF-416, TF-421 e TF-423 confirmado**.
- **TF-416 Wind Witch:** PV e atributos, Cursed Plant (retorno após 0 PV), Flammable, Tumbleweed Form, combinações de Multiattack, Slam, captura e libertação, reação Bouncy Escape. Bloqueio: dado de vida `12d8` publicado para criatura Large; conferir material editorial.
- **TF-421 Planar Flora / Execrable Shrub:** ficha como tipo **fiend** (não plant), bônus, HP, imunidades, ataques, curas por mortes próximas, telepatia seletiva e Smolder. Sem reação ou habilidade lendária na publicação individual.
- **TF-423 Spawn of Chernobog:** testes de infecção, dois sucessos para cura, cinco estágios progressivos de Night's Blood, transformação ao morrer, sensibilidade solar, Bite e Claws.
- TF-412 permanece bloqueada pela discrepância `SAB 11 (+1)` da fonte; TF-419 pela `Perception +6`/passiva `15` da fonte. Não aplicar reparos automáticos.
- Fontes: [Kobold Press](https://koboldpress.com/tools/kobold-press-monsters/), [Wind Witch](https://www.5esrd.com/database/creature/wind-witch/), [Execrable Shrub](https://www.5esrd.com/database/creature/execrable-shrub/), [Spawn of Chernobog](https://www.5esrd.com/database/creature/spawn-of-chernobog/).
- Auditoria acumulada: **15 aprofundadas; 116 ainda sem revalidação detalhada; 0 mecanicamente integrais; 101 parciais; 30 bloqueadas; 96 imagens físicas e 35 faltantes**.

## Checkpoint 15 — aprofundamento mecânico de 14/10/2026

- Commit de registros (3 criaturas): `c87f47a474ed19561178eb8b117750588f59fc46`; leitura de retorno: **OK**; exatamente os arquivos `records/TF-412.json`, `records/TF-418.json`, `records/TF-419.json`.
- **TF-412 Mandrake, Great**: estatísticas, mordida, Multiattack, Shriek, recarga 3–6, margens de falha e duração detalhados. **Divergência impressa**: SAB 11 (+1) não corresponde à fórmula usual (+0). Preservada com modificador não resolvido.
- **TF-418 Sodwose**: estatísticas, camuflagem, Scarecrow, Multiattack, Grass Whip, Entangle, Grass Step e Set Snare incluindo alvos, CDs, frequências, gatilhos e encerramento.
- **TF-419 Witchalder**: estatísticas, Deep Roots, False Appearance, Sunlight Regeneration, Speak with Plants, Slam, Shape Wood, Throttle e Pollen Cloud. **Divergência impressa**: Perception +6 x Perception passiva 15; valor original preservado.
- Identidade, ND e origem editoriais confirmados no [índice Kobold Press](https://koboldpress.com/tools/kobold-press-monsters/), com mecânicas individuais estruturadas a partir de [Mandrake Great](https://www.5esrd.com/database/creature/mandrake-great/), [Sodwose](https://www.5esrd.com/database/creature/sodwose/) e [Witchalder](https://www.5esrd.com/database/creature/witchalder/).
- As três permanecem **parciais**, sem aprovação integral contra publicação editorial/errata; arquivos de imagem já existentes mantidos sem alteração e aguardam conferência visual.
- Métrica acumulada: **12 aprofundadas em detalhe, 119 ainda sem revalidação detalhada, 0 integrais, 96 imagens persistidas, 35 imagens faltantes**.

## Resultado mensurável

- **131/131 JSONs publicados**, cobrindo exatamente 40 IDs de `next_batches[4]` e 91 de `historical.slice(104,195)` em ordem do CSV; nenhum repetido.
- **33 fichas consultadas diretamente em detalhe no histórico acumulado** (TF-414, TF-428, TF-431, TF-468, TF-470, TF-500, TF-502).
- **98 fichas receberam consolidação estruturada de checkpoints anteriores**, mas NÃO foram revalidadas integralmente nesta rodada; suas lacunas estão explícitas.
- **0 criaturas declaradas mecanicamente completas**, **104 parciais**, **27 bloqueadas** por conflito editorial, ausência de fonte ou mecânica específica.
- Nenhuma alteração do CSV, ledger, `main`, branch base, PR #1 ou pesquisas A/B; nenhuma promoção canônica ou merge.
- **JSONs válidos por serialização e leitura de retorno** ao publicar checkpoints de no máximo 10; cada registro mantém referência ao arquivo-fonte e os valores desconhecidos como `null`.

## Persistência: 14 checkpoints

| N.º | Primeiro–último ID | Commit GitHub | Confirmação |
|---:|---|---|---|
| 1 | TF-412–TF-421 | `878c67f0b4c4313c6787a94808ab11ec2a39a2b9` | read-back de JSON: OK |
| 2 | TF-423–TF-462 | `41283bead2dec0ed6646271ffb45153ee4ec5018` | read-back de JSON: OK |
| 3 | TF-468–TF-505 | `039fd608cb74a648aebb04368df8eb74c45252cb` | read-back de JSON: OK |
| 4 | TF-506–TF-522 | `46b55be00f5ad75a303870fd7522ebdb4666a29d` | read-back de JSON: OK |
| 5 | TF-120–TF-129 | `0488c3a02c3cce12db65c4478c6cab0e45841495` | read-back de JSON: OK |
| 6 | TF-130–TF-139 | `f749e3876ff3a16abdb2f9c62760075909888eec` | read-back de JSON: OK |
| 7 | TF-140–TF-151 | `d6b5a6738c2dd0b7349ca279c13e03709e298dd6` | read-back de JSON: OK |
| 8 | TF-152–TF-161 | `2c42a0e62128f204b77b0e24cbb1d70c0b871e96` | read-back de JSON: OK |
| 9 | TF-162–TF-171 | `bc86b2adfdb8341ba552d8edeac10c0fe80772b1` | read-back de JSON: OK |
| 10 | TF-172–TF-181 | `330613ec75a608fc402c2a7ec6f3cffe659f77d5` | read-back de JSON: OK |
| 11 | TF-182–TF-194 | `f0ffc0b144239b213176a533c7727177be4c1ef7` | read-back de JSON: OK |
| 12 | TF-195–TF-204 | `96c581caf3c3f383a6cd023e60181de2b97df236` | read-back de JSON: OK |
| 13 | TF-205–TF-502 | `9720a96e82d194b5bad3c57dba7818eea15da942` | read-back de JSON: OK |
| 14 | TF-512–TF-512 | `4fd97b161de6b468b827b2eb014c547775d047c6` | read-back de JSON: OK |

**Enriquecimento A5E:** `29ba80ad47084ddb342d943beaddf65031400718` (sete JSONs com mecânicas detalhadas, verificados novamente na branch).

## Auditoria individual: todos os 131 IDs

| ID | Criatura | Estado | Detalhe novo | Fonte | Pendência principal |
|---|---|---|---|---|---|
| TF-412 | Mandrake, Great | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/mandrake-great/) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-413 | Sinstar, Star Thrall | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/star-thrall/) | Não confundir com a criatura Sinstar principal, ND 17: a ficha do catálogo é Star Thrall. |
| TF-414 | Wallflower | BLOQUEADA | sim | [individual](https://a5e.tools/node/1660) | Texto editorial da ação Beak referencia grick, não Wallflower; falta determinar interpretação correta. |
| TF-415 | Gloomflower | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/gloomflower/) | Publicação e ND conferidos no índice editorial Kobold Press; conferir ficha mecânica e eventuais erratas no volume correto. |
| TF-416 | Wind Witch | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/wind-witch/) | Publicação e ND conferidos no índice editorial Kobold Press; conferir ficha mecânica e eventuais erratas no volume correto. |
| TF-417 | Mandriano | PARCIAL | sim | [individual](https://kpogl.wikidot.com/monster:mandriano) | Fonte KPOGL independente; comparar uso e limite de mortos-vivos com Creature Codex original. |
| TF-418 | Sodwose | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/sodwose/) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-419 | Witchalder | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/witchalder/) | Confirmar termos/recargas da nuvem de pólen contra livro. |
| TF-420 | Mandriano, Ancient | PARCIAL | sim | [individual](https://kpogl.wikidot.com/monster:ancient-mandriano) | Variante Ancient distinta de TF-417; KPOGL independente, confirmar edição. |
| TF-421 | Planar Flora, Execrable Shrub | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/execrable-shrub/) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-423 | Spawn of Chernobog | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/spawn-of-chernobog/) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-424 | Soul Eater | PARCIAL | sim | [individual](https://kpogl.wikidot.com/monster:soul-eater) | Revisar edição original vs revisão de Tome of Beasts 1 e condição precisa de Soul Drain; referência comunitária. |
| TF-425 | Snow Terror | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/snow-terror/) | Conferir ações e CDs em detalhe na fonte e suplemento original. |
| TF-426 | Planar Flora, Thorned Sulfurlord | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/thorned-sulfurlord/) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-428 | Cerberus Guardian | PARCIAL | sim | [individual](https://a5e.tools/node/2854) | A5E: limite de ações lendárias e Legendary Resistance mudam conforme cabeças ativas. |
| TF-431 | Conjured Guardian | PARCIAL | sim | [individual](https://a5e.tools/node/5171) | Challenge — no bloco editorial; CD e ataque dependem do conjurador, não fixar ND 0. |
| TF-448 | Imprisoned Celestial | PARCIAL | sim | [individual](https://a5e.tools/node/5406) | Publicação associada a Gate Pass Gazette #31; confirmar número da edição editorial. |
| TF-449 | Imprisoned Fiend | PARCIAL | sim | [individual](https://a5e.tools/node/5407) | Publicação ligada a Gate Pass Gazette #31; tratar strife como A5E. |
| TF-459 | Ankheg Empress | PARCIAL | sim | [individual](https://a5e.tools/node/3424) | Confirmar alcance exato de cada ataque ácido. |
| TF-462 | Behir Magus | PARCIAL | sim | [individual](https://a5e.tools/node/1465) | Conferir quais reações são apenas da variante Magus e o texto de suas CDs. |
| TF-468 | Faerie Chimera | BLOQUEADA | sim | [individual](https://a5e.tools/node/3239) | Breath Weapon descreve fire mas inflige cold; sem correção presumida. |
| TF-470 | Fiendish Chimera | BLOQUEADA | sim | [individual](https://a5e.tools/node/3240) | Ações lendárias Bite/Claw e reação headbutt não correspondem aos nomes de ações da variante. |
| TF-473 | Flying Lion | PARCIAL | sim | [individual](https://a5e.tools/node/1663) | Texto da publicação possui terminologia de griffon; validar como variante, não como griffon genérico. |
| TF-476 | Greater Sphinx | PARCIAL | sim | [individual](https://a5e.tools/node/1797) | Não confundir com esfinge comum CR 11; diferenciar regras de covil opcionais. |
| TF-499 | Cloud of Ghasthoppers | PARCIAL | sim | [individual](https://a5e.tools/node/4002) | Revisar trechos editoriais truncados do teste de resistência da Despair Aura. |
| TF-500 | Gorger Zombie Horde | BLOQUEADA | sim | [individual](https://a5e.tools/node/2522) | Página editorial individual Source Gate Pass Gazette, divergente da atribuição histórica. |
| TF-501 | Lost Prospector | PARCIAL | sim | [individual](https://a5e.tools/node/2965) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-503 | Stuffed Crab | PARCIAL | sim | [individual](https://a5e.tools/node/2213) | Confirmar número de ghouls e procedimento de libertação dos presos. |
| TF-504 | Warlord's Ghost | PARCIAL | sim | [individual](https://a5e.tools/node/1464) | Ficha editorial mantém termos banshee: distinguir variante Warlord's Ghost do monstro-base. |
| TF-505 | Demilich Mastermind | PARCIAL | sim | [individual](https://a5e.tools/node/1478) | Não confundir com demilich padrão (PV 159, outro bloco). |
| TF-506 | Mariner Ghost Swarm | PARCIAL | sim | [individual](https://a5e.tools/node/3406) | Conferir lacunas de formatação na descrição da ferramenta editorial. |
| TF-507 | Fogborn Skeleton Horde | PARCIAL | sim | [individual](https://a5e.tools/node/3460) | Tratar bloodied e manejo da horda segundo A5E, não converter sem revisão. |
| TF-509 | Fogborn Zombie Horde | PARCIAL | sim | [individual](https://a5e.tools/node/3462) | Regra de grupo e atributos podem coincidir com Gorger Zombie Horde, mas variantes são distintas. |
| TF-510 | Infernal Mammoth | PARCIAL | sim | [individual](https://a5e.tools/node/3426) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-511 | Fiendbloom Awakened Tree | PARCIAL | sim | [individual](https://a5e.tools/node/3414) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-516 | Kanos Spawn | PARCIAL | sim | [individual](https://a5e.tools/node/2991) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-517 | Imp Flock | PARCIAL | sim | [individual](https://a5e.tools/node/3394) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-518 | Infernal Dwarf | PARCIAL | sim | [individual](https://a5e.tools/node/3425) | Confirmar seleção de magias preparada e gatilhos de United in Action. |
| TF-521 | Bugbear Door Breaker | PARCIAL | sim | [individual](https://a5e.tools/node/4185) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-522 | Crime Boss | PARCIAL | sim | [individual](https://a5e.tools/node/1895) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-120 | Ashen Custodian | BLOQUEADA | não | [individual](https://www.5esrd.com/database/creature/ashen-custodian/) | A página inclui 'Alternate Critical (Source: Monster Crits for 5e)' após Cleansing Strike. Esse texto é de outro suplemento, foi EXCLUÍDO da mecânica-base. |
| TF-121 | Animal Lord, Queen of Birds | BLOQUEADA | não | [individual](https://www.5esrd.com/database/creature/animal-lord-queen-of-birds/) | Multiattack na página tem erro de digitação 'oOne' em descrição de ataques da forma verdadeira; tratado como leitura contextual, sem substituir fonte editorial original. |
| TF-122 | Animal Lord, Queen of Cats | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/animal-lord-queen-of-cats/) | As formas determinam ações disponíveis; não permitir bite/claw em forma humana. |
| TF-123 | Animal Lord, Queen of Scorpions | BLOQUEADA | não | [individual](https://www.5esrd.com/database/creature/animal-lord-queen-of-scorpions/) | A página 5eSRD inclui parágrafo narrativo sobre a apresentação dos Animal Lords NO MEIO das linhas de REGIONAL EFFECTS. Esse trecho não é habilidade, foi descartado. |
| TF-124 | Animal Lord, Queen of Serpents | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/animal-lord-queen-of-serpents/) | As ações são restritas às formas humana/serpente/híbrida; ações lendárias não podem ser tratadas como ações comuns. |
| TF-125 | Animal Lord, Queen of Mammoths | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/queen-of-mammoths/) | A fonte intercala um parágrafo narrativo depois das ações lendárias; não registrar como mecânica. |
| TF-126 | Giant, Abbanith | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/giant-abbanith/) | Earth Counter é reação com limitação temática, não counterspell genérico. |
| TF-127 | Giant, Laestrigonian | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/giant-laestrigonian/) | A doença possui efeitos persistentes próprios; não transformar em veneno. |
| TF-128 | Giant, Phase | PARCIAL | não | [individual](https://www.robinloft.com/monsters/phase-giant/tome-of-beasts-2) | Página individual /giant-phase/ do 5eSRD indisponível; dados conferidos em resumo de terceiros e em reprodução de Tome of Beasts 2, não em publicação editorial oficial acessível. |
| TF-129 | Giant, Snow | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/giant-snow/) | Imune a frio e vulnerável a fogo; regeneração depende de terreno nevado. |
| TF-130 | Giant, Thursir Hearth Priestess | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/thursir-hearth-priestess/) | Três opções de Hearth Blessing são variantes da mesma ação, não três ações distintas. |
| TF-131 | Ogre, Rainforest | PARCIAL | sim | [individual](https://www.5esrd.com/database/creature/ogre-rainforest/) | Change Shape não transforma equipamento; spear somente na forma ogre. |
| TF-132 | Ogre, Rockchewer | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ogre-rockchewer/) | Gravel Spray depende de Chew Rock prévio, não é ação livre independente. |
| TF-133 | Ogre, Tusked Crimson | PARCIAL | não | [individual](https://runerollers.com/apps/platform/library/bestiary/tusked-crimson-ogre-ccodex) | A ficha do Ogre Tusked Crimson não abriu como página individual do 5eSRD; mecânica corroborada por bestiário de terceiros e referência do Creature Codex. |
| TF-134 | Zimwi | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/zimwi-3pp) | A página é rotulada como revisão de Tome of Beasts 1; comparar com versão original para aprovação. |
| TF-135 | Abaasy | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/abaasy/) | Há restrição de mãos quando usa Spear com ambas; não permitir Iron Axe simultâneo. |
| TF-136 | Belu | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/belu/) | Rever se 'cures any diseases or conditions' da pomada possui restrições editoriais; não presumir que remove qualquer estado sem exceção. |
| TF-137 | Berberoka | BLOQUEADA | não | [individual](https://anyflip.com/lphgc/rjrj/basic/51-100) | Página individual /berberoka/ do 5eSRD não encontrada; mecânica verificada em reprodução não oficial de Tome of Beasts 3 e índice da Kobold Press. |
| TF-138 | Chuhaister | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/chuhaister/) | Página do 5eSRD não identifica publicação no rodapé; a identidade Creature Codex e ND7 são confirmados pelo índice oficial Kobold Press. |
| TF-139 | Giant, Cacus | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/giant-cacus/) | Há homônimo em 5E RPG: Ancient Adventures ND14, CA14/PV162, na URL /giant-cacus-2/; descartado para o catálogo. |
| TF-140 | Giant, Cave | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/giant-cave/) | Homônimo /giant-cave-3/ pertence a Tome of Horrors, ND6 e CA14/PV137, portanto descartado. |
| TF-141 | Giant, Desert | BLOQUEADA | não | [individual](https://www.5esrd.com/database/creature/giant-desert-3pp/) | A página 5eSRD inclui trecho de descrição narrativa colado à ação Rock; removê-lo da mecânica. |
| TF-142 | Giant, Firestorm | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/firestorm-giant/) | A fonte chama a criatura Firestorm Giant, enquanto o catálogo ordena Giant, Firestorm; mesma identidade pelo índice Kobold Press. |
| TF-143 | Giant, Haunted | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/giant-haunted/) | Três espíritos reconstituem-se segundo regras narrativas; traços dados por espíritos são removidos individualmente. |
| TF-144 | Giant, Hellfire | PARCIAL | não | [individual](https://kpogl.wikidot.com/monster%3Ahellfire-giant) | Imagem final e revisão independente pendentes. |
| TF-147 | Giant, Shire | PARCIAL | não | [individual](https://www.dndgrove.com/bestiary/8/giant-shire) | Página individual 5eSRD não localizada; confirmar seção de habilidades e ações na publicação de origem. |
| TF-148 | Giant, Thin | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/giant-thin/) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-149 | Giant, Thursir Armorer | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/thursir-armorer/) | Conferir regras de armadura quebrada e gatilhos dos acertos críticos na revisão. |
| TF-150 | Ogre, Void-Blessed | PARCIAL | não | [individual](https://kpogl.wikidot.com/monster%3Avoid-blessed-ogre) | Revisão de duração dos efeitos de Volatile Stomach. |
| TF-151 | Titan, Degenerate | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/titan-degenerate-3pp/) | Conferir versão 2023 do Tome of Beasts 1; não misturar com edição anterior. |
| TF-152 | Giant, Cave Shaman | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/giant-cave-giant-shaman/) | Revisar lista de magias e atribuição do material antes de publicação. |
| TF-153 | Giant, Lantern | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/lantern-giant/) | Verificar duração e raio luminoso na revisão independente. |
| TF-154 | Giant, Shadow | BLOQUEADA | não | [individual](https://www.5esrd.com/database/creature/giant-shadow/) | A página publica 209 PV (22d20+66); essa fórmula é incompatível com 209 PV e deve ser corrigida por errata/editor antes da integração, preservando ambos os valores originais. |
| TF-155 | Xing Tian | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/xing-tian/) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-156 | Giant, Hraesvelgr | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/giant-corpse-swallower-3pp/) | Publicação de 2023 difere mecanicamente da versão antiga; não misturar Shapechanger e conjuração de 2016. |
| TF-157 | Giant, Mountain | BLOQUEADA | não | [individual](https://www.5esrd.com/database/creature/Giant-Mountain/) | Seção de ações comuns incompleta na resposta de busca; bloco de Mountain Master contaminado por efeitos regionais. |
| TF-158 | Ooze, Alchemical Apprentice | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-alchemical-apprentice/) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-159 | Ooze, Amber | BLOQUEADA | não | [individual](https://anyflip.com/jfxvv/vjtj/basic/251-300) | A criatura de CR 4 do Tome of Beasts 2 não é a versão homônima CR 1/2 do 5eSRD (AC8 PV13). |
| TF-160 | Ooze, Corrupting | PARCIAL | não | [individual](https://anyflip.com/usqxr/fcko/basic/301-350) | Confirmação editorial e imagem pendentes. |
| TF-161 | Ooze, Eldritch | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-eldritch/) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-162 | Ooze, Ichor | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-ichor/) | Revisar limitações de Life Drain; arte pendente. |
| TF-163 | Ooze, Ink Guardian | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-ink-guardian/) | Revisar exceção ao dano de thunder e frasco de ressurgimento na publicação. |
| TF-164 | Ooze, Leavesrot | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-leavesrot/) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-165 | Ooze, Manure | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-manure/) | Verificar interação entre imunidade a slashing e reação Split; a fonte lista ambos e não deve ser silenciosamente reinterpretada. |
| TF-166 | Ooze, Mineral | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-mineral/) | Multiattack cita Slam mas única opção de ataque impressa na página é Pseudopod; confirmar nome na publicação. |
| TF-167 | Ooze, Shadow | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-shadow/) | Variante Freezing Shadow Ooze aparece na página; não misturar com ficha principal. |
| TF-168 | Ooze, Sinkhole | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/sinkhole-ooze/) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-169 | Ooze, Suppurating | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-suppurating/) | Variante Seeping Death Skeleton é entidade distinta, não integrar à ficha de ooze. |
| TF-170 | Voidpool | BLOQUEADA | não | ausente | Índice da editora identifica Voidpool, Tome of Beasts 2, ND5, mas página 5eSRD /database/creature/voidpool/ retornou 404. |
| TF-171 | Yaga Goo | PARCIAL | não | [individual](https://www.herebetaverns.com/srd/dnd-5e/monsters/yaga-goo) | Fonte mecânica reproduzida em terceiros; ficha editorial deve ser revisada. |
| TF-172 | Animated Offal | PARCIAL | não | [individual](https://kpogl.wikidot.com/monster:animated-offal) | KPOGL é wiki independente; acesso integral ao livro não comprovado. |
| TF-173 | Black Patch | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/black-patch/) | Regra de encantamento inclui salvaguardas repetidas: exigir verificação antes de implementar. |
| TF-174 | Oozasis | BLOQUEADA | não | [individual](https://www.5esrd.com/database/creature/oozasis-3pp) | ATENÇÃO: página 5eSRD revisão 2023 diverge da versão original CR9, inclusive nos atributos/salvaguardas; CA/PV compatíveis, mas não combinar demais mecânicas das duas edições. |
| TF-175 | Ooze, Blood | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-blood/) | Não usar homônimo /ooze-blood-2/, que é uma besta Tiny CR0. |
| TF-176 | Ooze, Foxfire | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-foxfire/) | Espalhamento de dano elétrico a alvos que portam metal exige revisão. |
| TF-177 | Ooze, Giant Shark Bowl | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-giant-shark-bowl/) | Estrutura representa criatura composta; não assumir que o tubarão separado seja uma ficha independente. |
| TF-178 | Ooze, Ruby | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-ruby) | Corrosão permanente depende de material e regras de equipamento; revisar antes de implementar. |
| TF-179 | Ooze, Shoal | BLOQUEADA | não | [individual](https://anyflip.com/myubd/nuoj/basic/301-350) | Fonte secundária reproduzida; só dados básicos e identificação ND10/CA9/PV232 conferidos; bloco completo ainda pendente. |
| TF-180 | Ooze, Sinoper | PARCIAL | não | [individual](https://anyflip.com/myubd/nuoj/basic/301-350) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-181 | Ooze, Snow | BLOQUEADA | não | [individual](https://kpogl.wikidot.com/monster:snow-ooze) | Wiki não oficial; dados CA/PV/ND conferidos mas ações não transcritas integralmente. |
| TF-182 | Ooze, Tar | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/ooze-tar/) | O fogo recebido não deve causar dano à gosma imune ao fogo, mas pode incendiá-la. |
| TF-186 | Atavist | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/npc-atavist/) | Identificado como NPC Atavist, evitar homônimo de outras fontes. |
| TF-187 | Bearfolk | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/bearfolk-3pp/) | Edição de 2023, possível diferença com Tome of Beasts original. |
| TF-188 | Behtu | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/behtu-3pp) | Não tratar infusão carregada como suprimento ilimitado. |
| TF-189 | Black Knight Commander | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/black-knight-commander-3pp/) | Não aplicar ataques da montaria sem tê-la presente. |
| TF-190 | City Watch Captain | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/city-watch-captain-3pp/) | A edição 2023 usa iniciativa coletiva opcional; não misturar com mecânicas SRD padrão. |
| TF-191 | Corpse Thief | PARCIAL | não | [individual](https://anyflip.com/myubd/zdka/basic/51-100) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-192 | Cueyatl Moon Priest | PARCIAL | não | [individual](https://www.herebetaverns.com/srd/dnd-5e/monsters/cueyatl-moon-priest) | Página 5eSRD individual não encontrada; reproduções com estatísticas consistentes. |
| TF-193 | Cueyatl Sea Priest | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/cueyatl-sea-priest/) | Referência a regras de comunicação com vida marinha requer classificação das espécies. |
| TF-194 | Cueyatl Warrior | BLOQUEADA | não | [individual](https://www.5esrd.com/database/creature/cueyatl-warrior/) | Robinloft apresenta CA12 e a ficha 5eSRD mostra CA13; reavaliar armor/stats e errata, sem mesclar dados. |
| TF-195 | Tosculi, Drone | BLOQUEADA | não | [individual](https://dr-eigenvalue.github.io/bestiary/creature/tosculi-drone) | Duas redações diferentes dos traços Skittering/Crowd Tactics entre edições; manter status parcial até comparação. |
| TF-196 | Tosculi, Elite Bow Raider | PARCIAL | não | [individual](https://dr-eigenvalue.github.io/bestiary/creature/tosculi-elite-bow-raider) | Fonte secundária, mas CR5/CA16/PV97 também constam da edição original; verificar alteração de 2023. |
| TF-197 | Tosculi, Jeweled Drone | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/tosculi-jeweled-drone/) | Não acumular múltiplos dados de Pheromones. |
| TF-198 | Tosculi, Warrior | BLOQUEADA | não | [individual](https://www.5esrd.com/database/creature/tosculi-warrior-3pp/) | Tome of Beasts original indexado como ND2 com três ataques; catálogo oficial revisado e arquivo local indicam ND3. Preservar revisão 2023 como referência e NÃO combinar duas edições. |
| TF-199 | Yakirian | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/yakirian/) | Resistência a frio e deslocamento 40 pés devem ser preservados. |
| TF-200 | Aboleth Champion | PARCIAL | não | [individual](https://a5e.tools/node/2839) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-201 | Alpha Werewolf | PARCIAL | não | [individual](https://a5e.tools/node/1721) | A5E ND6 HP104 difere do 'Alpha Werewolf' 5eSRD ND13 HP180; não utilizar homônimo nem mesclar sistemas. |
| TF-202 | Bearfolk Thunderstomper | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/bearfolk-thunderstomper/) | A página apresenta regra externa Alternate Critical de Monster Crits for 5e; foi EXCLUÍDA do resumo mecânico-base. |
| TF-203 | Cueyatl Warchief | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/cueyatl-warchief/) | A montaria tem bloco separado e só participa se presente. |
| TF-204 | Thripper | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/thripper/) | Fonte tem typo 'tripper' na multiattack, não confundir criatura ou generalizar counterspell. |
| TF-205 | Yathon | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/yathon/) | O bloco web mostra modificador CHA corrompido '7 (?2)' e alcance de Claw redundante; preservar dados claros e marcar tipografias. |
| TF-206 | Zeitgeist | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/zeitgeist/) | Uma ficha humanoide viva, não fantasma morto-vivo, apesar do nome; registrar duas CA. |
| TF-208 | Acid Ant | PARCIAL | não | [individual](https://www.wobblerocket.com/2025/07/20/acid-ants-worldbuilding-with-the-creature-codex/) | ND0.3 no catálogo representa CR1/4; descrição contém variante Fungi Bloom opcional, não incorporar ao bloco base. |
| TF-210 | Agnibarra | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/agnibarra/) | Dano adicional de fogo por turno termina quando apagado, não aplicar permanentemente. |
| TF-285 | Snallygaster | PARCIAL | não | [individual](https://www.5esrd.com/database/creature/snallygaster/) | Distinguir variante Tome of Beasts 3 CR15 de homônimo; revisão mecânica independente |
| TF-469 | Fateholder | BLOQUEADA | não | [individual](https://a5e.tools/node/2194) | revisão integral de todos os gatilhos, resultados de testes, recargas, frequência, duração, custos e variantes |
| TF-483 | Squashling | BLOQUEADA | não | [individual](https://a5e.tools/node/3666) | Lacunas nos efeitos Seed Shot e Charming Aspect |
| TF-493 | Rock Troll | PARCIAL | não | [individual](https://www.a5e.tools/node/2270) | Não aplicar lore geral de troll; conferir frio e trovejante no bloco específico |
| TF-494 | Askwise Keeper | PARCIAL | não | [individual](https://www.a5e.tools/node/2206) | Texto menciona voo, mas não há velocidade de voo no bloco |
| TF-502 | Ghasthopper | BLOQUEADA | sim | [individual](https://a5e.tools/node/4001) | CA/PV e ataques recuperados da ficha individual A5E, mas Despair Aura cita saving throw sem CD/atributo. |
| TF-512 | Anzû | PARCIAL | não | [individual](https://www.a5e.tools/node/2393) | Fonte Mythological Figures & Maleficent Monsters; comparar variante do catálogo |

## Divergências a preservar

- **TF-414** — fonte menciona grick na bicada de Wallflower: não corrigir por inferência.
- **TF-431** — não possui ND fixo na ficha; dependente de CD, ataque, proficiência e slot do conjurador.
- **TF-468** — texto do sopro fala fire, valores de dano falam cold; manter ambos e bloquear resolução.
- **TF-470** — inconsistência dos nomes nas ações lendárias e na reação Winged Charge.
- **TF-500** — campo Source da página aponta Gate Pass Gazette, diferente da atribuição anterior.
- **TF-502** — página atual fornece CA13 PV31 atributos e ataques, mas falta salvaguarda completa de Despair Aura.
- Registros históricos sinalizados como BLOQUEADA mantêm incertezas específicas, incluindo fontes contaminadas, variantes e edições divergentes.

## Validação e encaminhamento

- A5E e D&D 5e são mantidos como linhas distintas. Regras de `bloodied`, `rattled`, `fatigue`, `horde`, conjuração dinâmica e outras não foram automaticamente traduzidas.
- O registro `checkpoint_anterior` preserva a evidência preexistente sem tratá-la como conferência integral nova.
- Para concluir o escopo integral, é necessário conferir página/bloco integral de cada um dos 124 IDs restantes, resolver as divergências e preencher os campos ainda desconhecidos; sem isso, 0/131 está completo.
- O manifesto lista cada arquivo e suas pendências individualmente. Nenhum merge autorizado.

## Atualização: fichas acompanhadas de imagens binárias (13/10/2026)

- **96/131** imagens binárias reais publicadas em `operational/research/deep-mechanics/c/images/`, com SHA Git conferido após publicação; não são placeholders ou referências remotas.
- **82** reaproveitadas da branch isolada E, **1** da branch isolada F e **13** importadas do repositório público TheGiddyLimit/homebrew por igualdade exata do SHA de origem e destino.
- **35 imagens ainda não existem** neste diretório: TF-414, TF-428, TF-431, TF-448, TF-449, TF-459, TF-462, TF-468, TF-470, TF-473, TF-476, TF-499, TF-500, TF-501, TF-503, TF-504, TF-505, TF-506, TF-507, TF-509, TF-510, TF-511, TF-516, TF-517, TF-518, TF-521, TF-522, TF-200, TF-201, TF-469, TF-483, TF-493, TF-494, TF-502, TF-512.
- As **96 imagens ainda não passaram por revisão visual editorial**. TF-285 (64×80) é baixa resolução; TF-417 e TF-420 utilizam o mesmo blob de arte no acervo de origem. Nenhuma das 96 está aprovada como arte final.
- Todos os 96 JSONs correspondentes contêm `imagem.arquivo` e hash do blob binário persistido. O manifesto documenta os 35 casos sem imagem.
- **TF-413 Star Thrall**: estatísticas, ataques, gatilhos, salvaguardas, dano e recarga reconstruídos da ficha individual 5eSRD (2026-10-13), com imagem binária no repositório. Conferência independente com o volume/errata permanece pendente; não foi promovida a conclusão canônica.
- **TF-415 Gloomflower**: traços, ações, multiataque e três variantes opcionais detalhadas; variante Soul Splice bloqueada por CD textual contraditória ('successful 20 DC 14') e dependência de magic jar. Imagem real já publicada.
- **Situação atual verificável:** 131 JSONs; 96 imagens; 35 imagens faltantes; 9 aprofundamentos diretos na execução; 0 fichas integralmente aprovadas; 108 parciais e 23 bloqueadas. Nenhum merge.

### Checkpoints das imagens (até 10 por commit)

| N.º | Commit |
|---:|---|
| 1 | `d70f09d41eb4c1fbebc96d9f512d23125c7371bf` |
| 2 | `9b976f2f8e6bdf14ba46de2e24b5457993567e51` |
| 3 | `ea70ea62b56d6c181f0b395b7773bb58471f6b66` |
| 4 | `67fa0bf1e8d2492ec9d89e6e4e1c8b796d27840b` |
| 5 | `7687efd7fec0dbc3f3cc1d6fcaf3ab9ad2b68a34` |
| 6 | `1c5318c7e0538cc807595dd8ec45c615aadb0485` |
| 7 | `b63373cffe76fd8822d288b7cefc4da4353af3ac` |
| 8 | `b467e0d10a5e758c7f264d7c231bfa0dd0074814` |
| 9 | `45f9250340c874a7ce3fea7a90342781f36b35d2` |
| 10 | `f9b15dfbcc0e3f456471667efea7dee1a8c2f45c` |
| 11 | `b8d3f53441c5b895bb2f8cd5d31b83c9b795cce6` |
| 12 | `605cb4550304f286e6b489e045045908b4afc05b` |
