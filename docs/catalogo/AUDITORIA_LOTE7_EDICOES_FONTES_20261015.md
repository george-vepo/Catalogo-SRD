# SRD Card Game — lote 7: edições e fontes mecânicas (15/10/2026)

> **Conferência de dados externos, não homologação da engine.** PR dependente do lote 6 (#24). Nenhum registro mecânico-base, deck, asset ou interface da grade foi alterado. A apresentação do painel ampliado foi ajustada apenas para distinguir fontes primárias e secundárias.

## Evidência da reedição e divergência — KP-S017 Vesiculosa

A editora [Kobold Press confirma](https://koboldpress.com/tome-of-beasts-1-what-changed/) que **Tome of Beasts 1 (2023)** é revisão da obra original publicada em **2016**, com mudanças em estatísticas, traços e ações de monstros. O registro de Vesiculosa em [5esrd, Tome of Beasts 1 (2023)](https://www.5esrd.com/database/creature/vesiculosa-3pp/) e a [referência secundária KPOGL](https://kpogl.wikidot.com/monster:vesiculosa) informam os valores abaixo:

| Estatística | Referência original 2016* | Referência revisada 2023 |
|---|---:|---:|
| PV | 203 (14d20+56) | **232 (16d20+64)** |
| Destreza | 10 | **15** |
| Escavação | 5 pés | **20 pés** |
| ND | 11 | **11** |

*Os números da edição de 2016 foram localizados em reproduções históricas não oficiais e **não foram conferidos diretamente no livro original licenciado**. Por isso foram registrados como **comparação histórica indicativa**, nunca como correção canônica. O resumo operacional existente e os dados externos do catálogo seguem a revisão **2023**. Não transportar ataques como Entrap/Engulf da publicação antiga para a ficha atual Root/Spit Sweet Water. A ausência de licença de arte permanece inalterada.*

Na revisão de 2023 foram resumidos, com nova redação, os traços de disfarce como oásis, perfume de atração, água que cura e pode causar sono, ataques de raiz e jato e recurso de enterrar uma vítima. Os detalhes são **referências D&D 5e de terceiros**, não cartas prontas para o SRD Card Game. O acesso direto ao portal 5esrd apresentou bloqueio JavaScript; houve conferência por índice textual completo e referência independente.

## Sinstar — KP-S018, Tome of Beasts 3

Fonte primária registrada: [5esrd](https://www.5esrd.com/database/creature/sinstar/) (leitura direta indisponível). Fonte secundária **integralmente legível**, sem vínculo oficial com a editora: [KPOGL — Sinstar](https://kpogl.wikidot.com/monster:sinstar).

- **CA 17, PV 275, ND 17**, Planta Minúscula. Atributos: FOR 5, DES 14, CON 17, INT 21, SAB 18, CAR 15.
- Resistências ácido, frio, fogo e elétrico; imunidade veneno. Resistência lendária 3/dia; doença Thrall Sickness (Constituição CD 19) e vínculo com star thralls.
- Ataque múltiplo com Alluring Whispers e três ataques de Spines ou Psychic Lash. Ataque de espinhos +8, chicote psíquico +11, e efeito encantador de Sabedoria CD 19. Resumos próprios da referência, não transcrições literais.
- **Ações lendárias:** ataque Spines, teleporte até 120 pés, explosão de star thrall (custo 2). **Covil:** fortalecer servos, cactos em área e nuvem incapacitante (Constituição CD 19). Efeitos regionais também resumidos.

A consulta da página KPOGL permite melhorar a referência técnica, mas **não substitui a revisão na publicação original, não concede direitos de reprodução editorial e não aprova adaptações de jogo**. Dados originais `fichas-607.json` não foram modificados.

## Alteração de interface estritamente localizada

A função `referenceDetails(extra)` em `docs/catalogo/app.js` agora mostra um aviso conservador para fontes indexadas/bloqueadas e um link opcional **Referência secundária (não oficial)** quando o registro contiver fonte complementar. A grade mantém apenas imagem/nome, filtros e zoom inalterados. O JSON `fichas-referencia-verificadas.json` contém **12 referências únicas**, seis referências detalhadas antigas e seis resumos externos; Sinstar e Vesiculosa foram os únicos registros alterados neste lote.

## Aceite e pendências

- Cotejar cada URL, edição e status de verificação por ID, preservar todos os campos antigos não envolvidos.
- Confirmar que o JavaScript continua válido, que as referências secundárias só aparecem quando declaradas e que os avisos são acionados para fontes bloqueadas.
- **Pendentes:** homologação/autorizações de terceiros e de artes, revisão de edição original 2016, leitura direta de First Servant, testes de navegador responsivo e CI. Nenhum merge foi realizado neste lote.
