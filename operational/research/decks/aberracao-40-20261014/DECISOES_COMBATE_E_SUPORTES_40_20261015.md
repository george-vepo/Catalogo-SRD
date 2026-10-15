# SRD Card Game — Decisões de combate e 40 suportes candidatos (15/10/2026)

> **REGISTRO DE DISCUSSÃO / PROPOSTA NÃO HOMOLOGADA.** Este documento transcreve decisões e seleções discutidas com o administrador para o deck experimental de 40 Aberrações. Não promove cartas ao catálogo, não altera fichas, não implementa a engine, não altera estado de partida e **não comprova** a ficha integral de todas as criaturas.

## 1. Escopo e fontes

- Deck e identidade/ordem das 40 cartas: [cards.csv](cards.csv).
- Registros mecânicos históricos (resumos e fichas não necessariamente integrais): [fichas_catalogo_35.json](fichas_catalogo_35.json).
- Blocos integrais controlados de Gibbering Mouther, Roper e Aboleth: [fichas_srd521_integral_3.json](fichas_srd521_integral_3.json).
- Pendências mecânicas identificadas: [pesquisa_fichas_incompletas_7.json](pesquisa_fichas_incompletas_7.json).
- Fichas aprofundadas parciais: `operational/research/deep-mechanics/a/records/<ID>.json`.
- Referências web não constituem, por si, comprovação de licença, versão ou homologação.
- Prevalência documental a conferir com o manual completo do jogo e o SRD 5.2.1; toda divergência deve ir ao administrador.

## 2. Diretrizes explicitamente definidas pelo administrador na conversa

**2.1. Combate.** Duelo segue as mecânicas de combate de D&D 5e / SRD 5.2.1, **exceto movimentação, posicionamento e alcance**, que não existem no Card Game. As criaturas ativas de J1 e J2 podem atingir-se com ataques corpo a corpo e à distância sem verificar número de pés, deslocamento, linha de aproximação, distância de aura ou alcance de magia. Não adicionar penalidades inventadas de distância.

**2.2. Mecânicas preservadas.** Manter, quando pertinentes, CA, PV, iniciativa, rolagens, ataques, modificadores, dano, críticos, resistências, imunidades, vulnerabilidades, testes e CDs, condições, magias, concentração, duração (1 minuto = 10 rodadas), ações, ações bônus, reações, ações lendárias, recargas e usos da ficha de origem. Efeitos de condições vinculados **exclusivamente a deslocamento** não produzem movimentação; os demais efeitos continuam funcionando. Ignorar alcance **não significa ignorar** tipo de alvo, condição de escuta/visão, componentes, gatilhos, requisitos de agarrão, custo de ação e pré-requisitos que não sejam distância.

**2.3. Suporte e prioridade.** Cada carta candidata deve ter **uma habilidade de assinatura da criatura**. Escolher prioritariamente buff útil; senão debuff útil; por último ataque/dano fiel. Se o buff original age apenas na própria criatura, mas tem utilidade real no duelo, propor transferência do benefício à **criatura ativa em combate**. Quando for situacional/raramente aplicável (ex.: absorção de dano psíquico que depende de receber aquele dano), preferir ataque com dano real da mesma ficha. **Nenhum dado, condição, CD ou efeito pode ser inventado** para preencher lacuna. A origem dos números de um ataque de suporte é a ficha da **carta de suporte**, não a ficha da criatura ativa.

**2.4. Natureza homebrew.** A transferência de buffs próprios para a criatura ativa e o uso de ações de outra criatura como suporte são propostas específicas do Card Game, **não regras do SRD**. A escolha da assinatura não é a homologação de sua ativação. Em particular, não foi decidido se a ativação consome ação, bônus ou reação do usuário/aliado; nem limite por combate, acúmulo, tempo de aplicação ou consumo/destino da carta. **Não inventar esses parâmetros durante os testes.** Enquanto não forem regulamentados, registrar como pendência.

**2.5. Áreas.** Como não há alcance, não se verificam pés ou raio para selecionar o oponente ativo, mas isso não transforma automaticamente habilidades de múltiplos alvos em dano exclusivo de um só alvo nem apaga efeitos colaterais em outros alvos elegíveis. Com apenas uma criatura ativa por lado, definir explicitamente como afetar aliados, si próprio e outros alvos, se necessário.

## 3. Lista de 40 habilidades de suporte — seleção discutida (NÃO HOMOLOGADA)

Convenções: **B→Ativa** = buff que originalmente protege/beneficia a criatura fonte e cuja transferência à ativa é proposta homebrew; **E** = controle/debuff; **D** = dano; **M** = combinado. Valores e nomes abaixo vêm de discussões e recortes de pesquisa do deck. **Não equivalem a 40 verificações editoriais integrais.** Cada uso permanece sujeito a pré-condições não espaciais, economia de ações, versões e efeitos integrais da fonte.

### 3.1. Comuns (20)

| # | Carta | Seleção (classe) | Efeito resumido registrado | Revisão necessária |
|---:|---|---|---|---|
| 1 | Ahu-Nixta, Drudge | Fear (E) | Magia inata de medo; ficha de pesquisa registra CD 11, 1/dia. | Conferir a magia integral e recursos. |
| 2 | Cranium Rat | Bite (D) | Ataque +4; 1 perfurante (valor citado na conversa). | **Ficha externa MPMM não integrada**: verificar edição e ataque. |
| 3 | Gazer | Eye Rays (E/D) | Dois raios determinados aleatoriamente, com controle/dano conforme edição. | **Ficha externa**; sortear raios, não escolher livremente. |
| 4 | Light Eater | Tentacle (D) | Ataque +4; 1d6+2 contundente. | Troca de Emergency Flare por depender de gatilho e envolver área. |
| 5 | Shoth, Sooze | Warrior (B→Ativa) | Proposta: transferir +2 CA da variante Warrior. | **Dependente da escolha de variante**; não transformar vantagem condicional em vantagem irrestrita. |
| 6 | Malleable, Minor | Flesh Tendril (D/E) | 2d6+3 contundente e Agarrado conforme a ficha. | Substitui Psychic Absorption por ser situacional. |
| 7 | Birgemon Seal | Tendril (E) | Agarrado; dois tentáculos no mesmo alvo podem impor Contido; escape CD 13. | Dois tentáculos exigem duas aplicações válidas, não apenas um acerto. |
| 8 | Gibbering Mouther | Gibbering (E) | Sabedoria CD 10; falha e 1d8 determinam comportamento. | **SRD 5.2.1**; preservar resultados completos do d8. |
| 9 | Yann-An-Oed | Tentacles (E/D) | +4, 2d4+2 contundente; Agarrado/Contido, escape CD 12. | Manter pré-condições de tamanho e limite de alvos não espaciais. |
| 10 | Ahu-Nixta | Fear (E) | Magia de medo, CD 14. | Confirmar a versão de conjuração e todos os requisitos. |
| 11 | Astral Snapper | Claws (D) | +4, 2d6+2 cortante. | Substitui Astral Devour (parasitismo fora do fluxo de turno); ficha parcial. |
| 12 | Xenabsorber | Slam (D) | +5, 1d10+3 contundente. | Trait Mimicry depende de imitação e alvo elegível; fonte em resumo. |
| 13 | Maw Swarm | Bites (D) | +5, 4d6+3 perfurante; 2d6+3 quando bloodied. | Não confundir redução de dado de dano com redução de PV do suporte. |
| 14 | Mayday | Pseudopod (D/E) | +6, 4d8+4 contundente; aplica Sticky conforme ficha. | Preservar restrições de alvo não aderido e regras de sair do agarrão/adesão. |
| 15 | Asanbosam | Claws (E/D) | +7, 3d10+4 perfurante; Agarrado/Contido, fuga CD 14 e possível doença. | Verificar condições, salvaguarda de doença e duração. |
| 16 | Malleable, Moderate | Flesh Tendril (D/E) | +7, 3d6+4 contundente; Agarrado. | Substitui Psychic Absorption/Psychic Drain dependente de agarrão prévio. |
| 17 | Roper | Tentacle (E) | +7; Agarrado e Envenenado, fuga CD 14. | **SRD 5.2.1**; não inventar dano para o tentáculo. |
| 18 | Shoth, Oth | Paladin of Shoth (B→Ativa) | Proposta: +2 CA da variante Paladino transferidos à ativa. | **Variante escolhida é requisito**; manter outros efeitos só se elegíveis. |
| 19 | Snatch Bat | Pilfering Bite (D) | Ataque +8, 2d4+5 perfurante na opção de dano. | Não aplicar roubo de item sem regras de equipamentos. |
| 20 | Mindwitness | Eye Rays (E/D) | Três raios aleatórios com efeitos de controle/dano. | **Ficha externa Volo não integrada**; fixar sorteio e edição. |

### 3.2. Incomuns (12)

| # | Carta | Seleção (classe) | Efeito resumido registrado | Revisão necessária |
|---:|---|---|---|---|
| 21 | Fate Eater | Alter Fate (E/D) | Carisma CD 15; na falha, 8d8 psíquico e efeito de destino sorteado 1d6, conforme ficha. | Recarga 5–6; não simplificar tabela de efeitos. |
| 22 | Mamura | Whiptail Stinger (E/D) | +7, 1d8+4 perfurante; Constituição CD 15 para veneno/Envenenado e efeitos subsequentes. | Preservar dano adicional, duração e novos testes. |
| 23 | Yavalnoi | Luminous Burst (E) | Sabedoria CD 15; marca alvo e facilita ataques contra ele. | Recarga 5–6; confirmar ficha integral e respiração aquática. |
| 24 | Chelicerae | Magical Discharge (D) | Destreza CD 15; 8d8 força, metade no sucesso. | Edição revisada versus original: **não misturar**; recarga especial. |
| 25 | Crystalline Monolith | Psychic Burst (E/D) | Inteligência CD 15; 8d6 psíquico e Atordoado na falha. | Recarga 5–6 e novos testes; confirmar fonte bibliográfica. |
| 26 | Ahu-Nixta, Cataphract | Fear (E) | Magia inata de medo, CD 15. | Confirmar recursos de magia integral. |
| 27 | Astral Devourer | Serpent Spray (D/B→Ativa) | Destreza CD 16; 4d6 perfurante + 4d6 veneno, metade em sucesso; cura pelo maior dano perfurante individual transferida à ativa. | Recarga 6; **transferência da cura é homebrew**. |
| 28 | Ziphius | Telepathic Foresight (B→Ativa/E) | Sabedoria CD 15; vínculo concede vantagem ofensiva ou desvantagem nos ataques do alvo. | **Transferir beneficiário é homebrew**; confirmar duração/edição. |
| 29 | Shukankor | Beak (D) | +10, 2d8+6 perfurante. | Many Eyes beneficiaria só testes raros; dano mais aplicável. |
| 30 | Xhkarsh | Fate-Altering Stinger (E/D) | +8, 2d10+4 perfurante; Carisma CD 16 pode corromper o destino. | Fixar edição 2023 antes de executar. |
| 31 | Aboleth | Dominate Mind (E) | SRD 5.2.1: Sabedoria CD 16, 2/dia; Enfeitiçado e controle conforme ficha. | Não tratar como vitória automática; usar gatilhos de fim do efeito. |
| 32 | Malleable, Major | Flesh Tendril (D/E) | +10, 4d6+6 contundente e possível Agarrado. | Evita bônus de absorção psíquica muito situacional. |

### 3.3. Raras (5), Lendárias (2) e Mítica (1)

| # | Carta | Seleção (classe) | Efeito resumido registrado | Revisão necessária |
|---:|---|---|---|---|
| 33 | Ancient Aboleth | Legendary Resistance (B→Ativa) | Proposta: a ativa pode transformar falha em resistência em sucesso. | Fonte tem 3/dia; **quantos usos são transferidos permanece INDEFINIDO**; verificar custo de ativação. |
| 34 | Voidling | Shadow's Grasp (E/D) | Destreza CD 17; 14d6 necrótico e Contido na falha, conforme ficha. | Recarga 5–6, duração/testes, edição. |
| 35 | Aboleth Brute | Bite (E/D) | +11; 4d12+6 perfurante, Agarrado e Contido, fuga CD 19. | Preservar impossibilidade de morder outro alvo durante o agarrão se pertinente. |
| 36 | Forest Emperor | Rattle (E) | Sabedoria CD 18; pode impor Amedrontado. | Regra original de som, novos testes e imunidade após sucessos. |
| 37 | Snallygaster | Regeneration (B→Ativa) | Proposta: ativa recupera 15 PV no início do seu turno se tiver ao menos 1 PV. | **Duração do efeito transferido ainda não definida**; conferir demais limitações da ficha. |
| 38 | Malleable, Massive | Flesh Tendril (D/E) | +13, 5d6+8 contundente e Agarrado, fuga CD 18. | **Substitui Psychic Absorption** por ser pouco aplicável. |
| 39 | Kalaraq Quori | Swarm of Eyes (E/D) | Sabedoria CD 21; 10d8 psíquico e possível Cego. | **Ficha externa Eberron não integrada**; recarga 6, novos testes. |
| 40 | Greater Star Spawn Emissary | Mind Cloud (E/D) | Sabedoria CD 23; 5d12 psíquico e encerramento de magias em alvos elegíveis. | **Ficha externa Legacy não integrada**; ação lendária custa 3 ações lendárias na proposta — verificar edição e economia de ações. |

## 4. Pontos críticos de implementação (NÃO DECIDIDOS)

1. **Custo de uso da carta de suporte:** ação, ação bônus, reação, janela especial, ou outra regra, conforme manual/decisão administrativa. Não permitir ações adicionais por omissão.
2. **Transferência dos buffs à ativa:** definir ativação, duração, eventual uso único ou repetível, remoção do efeito, consumo da carta, recursos e acumulação. Não presumir duração de 1 turno nem "até acabar a batalha" por padrão.
3. **Recargas e usos originais:** se a carta fornece ataque com Recharge 5–6, 6 ou X/dia, preservar/reconciliar conforme regra de suporte; não transformar livremente em habilidade à vontade.
4. **Passivos contínuos:** Shoth (CA), Snallygaster (regeneração), Legendary Resistance e Ziphius exigem janela de início/fim de efeito e eventos claros.
5. **Agarrado, Contido e Cego:** ainda aplicam efeitos não relacionados a movimento. Escape, fim de condição e pré-requisitos devem ser preservados; não criar regras espaciais.
6. **Várias formas/variantes:** Shoth Sooze/Warrior, Shoth Oth/Paladino e criaturas com transformação só recebem traços específicos quando a edição/variante escolhida os possuir.
7. **Áreas/auras e magias:** definir alvo elegível e consequências em J1/J2; ausência de alcance não elimina efeitos sobre o próprio usuário ou aliados quando a ficha os incluir.
8. **Desequilíbrio em duelo 1 × 1:** Dominate Mind, Stunned, Legendary Resistance e regeneração contínua exigem teste de jogo, sem mexer arbitrariamente na mecânica publicada.
9. **Revisão editorial:** arquivos aprofundados do catálogo com `mecanica_integral_validada: false`, as sete fichas incompletas e cinco monstros externos **não** podem ser tratados como validados apenas por constarem nesta tabela.

## 5. Identidade, baralho, histórico e arte

- Ordem/ID canônico/ND/raridade permanecem os de [cards.csv](cards.csv); cópias individuais devem ter IDs próprios no duelo.
- Composição da pesquisa: 20 Comuns, 12 Incomuns, 5 Raras, 2 Lendárias, 1 Mítica. Cinco nomes externos são **candidatos não aprovados**.
- Arquivos de imagem continuam **32/40 integrados fisicamente** na branch de pesquisa, **sem homologação visual**. Oito pendências: quatro Malleables, Maw Swarm, Mayday, Shukankor e Aboleth Brute; ver [IMAGENS_PESQUISADAS.md](IMAGENS_PESQUISADAS.md). Pesquisa de novas artes não altera atributos.
- Este documento registra o histórico de decisões; **não** altera placar, mãos, montes, cemitério ou qualquer estado de partida; **não** modifica o catálogo oficial.

## 6. Critério de aceite futuro

Aprovar uma habilidade individual somente após: confirmar identificação + edição da criatura; localizar habilidade na ficha; validar números e condições de uso; estabelecer forma de ativação do suporte e transferência se cabível; verificar economia de ações/recursos e persistência; testar o motor sem movimento/alcance. Enquanto isso, **40 escolhas candidatas / 0 homologações**.
