# SRD Card Game — Auditoria conservadora de artes e fichas, lote 2 (15/10/2026)

> **Lote auditável de referências web. Não é autorização de produção.** Base: `chatgpt/celestial-40-suportes-20261015`. Nenhuma engine, baralho, ficha homologada ou arte binária foi alterada.

## Estado verificado pelo GitHub

| Métrica | Antes | Após este lote |
|---|---:|---:|
| Criaturas distintas | 1.320 | **1.320** |
| Tipos | 14 | **14** |
| Fichas mecânicas no JSON-base | 607 | **607** |
| Fichas com texto integral local | 108 | **108** |
| Registros com `mecanica_externa_integrada` | 113 | **113** |
| Fichas detalhadas de referência (ainda não homologadas) | 6 | **6** |
| Referências de imagem exibíveis no site | 35 | **36** |
| Criaturas sem referência exibível | 1.285 | **1.284** |

Os valores de imagens foram reproduzidos com a mesma precedência do `docs/catalogo/app.js`: `curadoria.approved` → arte do deck Celestial → imagem com verificação do controle 607. O JSON `fichas-607.json` foi recontado pelo blob Git `44d786dffc72e3ba3e83435b072f81b7eb2876f9`: 607 IDs distintos, 108 textos integrais e 113 integrações externas. **O indicador histórico `fichas_mecanicamente_integradas_com_fatos_e_resumos_proprios=104` no cabeçalho do JSON diverge da contagem atual do campo `mecanica_externa_integrada` (113).** Pode haver diferença de definição ou de checkpoint; não foi alterado sem conciliação formal. A megalista liga explicitamente 606 IDs do conjunto 607; o registro `KP-S007` mantém-se como associação independente e não deve ser fundido.

## 1 referência visual adicionada

| ID | Criatura | Fonte, edição e avaliação | Direitos |
|---|---|---|---|
| **AT-089** | **Ochre Jelly** | [D&D Beyond — ficha Legacy 2014](https://www.dndbeyond.com/monsters/16967-ochre-jelly). [Arte de referência](https://www.dndbeyond.com/avatars/thumbnails/0/279/1000/1000/636252770058723674.jpeg): gosma ocre de corpo inteiro na prévia, isolada, sem texto, captura de interface, arte de outra espécie ou marca-d'água visível | Somente **link externo de referência**, sem licença de reprodução comercial ou redistribuição e sem autorização para imprimir |

A imagem é de edição anterior; **não** determina as regras da carta. A ficha SRD 5.2.1 permanece soberana. A verificação foi visual na prévia indexada e cruzada com a página oficial; o código HTTP numérico, o tipo MIME de uma requisição independente e a persistência futura do endereço **não** foram rechecados.

## 7 candidatas recusadas neste lote

| ID | Criatura | Candidata e motivo |
|---|---|---|
| AT-126 | Mimic | [D&D Beyond Legacy](https://www.dndbeyond.com/monsters/16957-mimic): arte da espécie correta, porém o apêndice/língua extrapola a borda direita da imagem |
| AT-060 | Gargoyle | [D&D Beyond Legacy](https://www.dndbeyond.com/monsters/16868-gargoyle): miniatura corta a porção inferior da criatura |
| AT-146 | Awakened Shrub | [Arcverse](https://www.enterthearcverse.com/dnd-glossary-pages/-awakened-shrub): a imagem contém o próprio título impresso abaixo da arte |
| AT-011 | Allosaurus | [World Anvil](https://www.worldanvil.com/w/astora-hamilcarbarca/a/allosaurus-article): cauda/corpo cortados e associação editorial à ficha do jogo insuficientemente comprovada |
| AT-033 | Homunculus | [5etools — Homunculus Servant (TCE)](https://5e.tools/bestiary/homunculus-servant-tce.html): variante de Artífice, não é o Homunculus do SRD |
| AT-061 | Air Elemental | [Chroniques Oubliées](https://www.co-drs.org/fr/bestiaire/creatures/elementaire-dair-enorme): outro sistema e criatura de porte/versão diferente |
| AT-040 | Pseudodragon | [Repost Pinterest](https://www.pinterest.com/pin/129337820536420427/): corte de composição e autoria/proveniência primária não comprovadas |

As URLs individuais rejeitadas estão preservadas, com justificativas, em `data/curadoria-artes-20261015.json`. **Não** devem ser utilizadas automaticamente pelo site. Rejeição da candidata não significa rejeição permanente da espécie.

## 5 comparações entre edições D&D 5e

**Escopo limitado: diferenças constatadas nas páginas oficiais 2014 Legacy versus 2024.** Nenhuma comparação alterou o JSON de fichas, CA, PV, ataques, reações ou engine.

| ID | Criatura | Legacy (2014) | Atual (2024/SRD 5.2.1) |
|---|---|---|---|
| AT-089 | [Ochre Jelly](https://www.dndbeyond.com/monsters/16967-ochre-jelly) | CA 8; PV 45; 10 ft., escalada 10 ft. | [CA 8; PV 52; 20 ft., escalada 20 ft.](https://www.dndbeyond.com/monsters/5195148-ochre-jelly) |
| AT-060 | [Gargoyle](https://www.dndbeyond.com/monsters/16868-gargoyle) | CA 15; PV 52; False Appearance; mordida e garras | [CA 15; PV 67; Flyby; dois Claw](https://www.dndbeyond.com/monsters/5195003-gargoyle) |
| AT-126 | [Mimic](https://www.dndbeyond.com/monsters/16957-mimic) | CA 12; PV 58; deslocamento 15 ft.; Shapechanger com ação | [CA 12; PV 58; 20 ft.; Shape-Shift com ação bônus](https://www.dndbeyond.com/monsters/5195123-mimic) |
| AT-033 | [Homunculus](https://www.dndbeyond.com/monsters/16926-homunculus) | CA 13; PV 5; CON 11; CD 10 do Bite | [CA 13; PV 4; CON 14; CD 12 do Bite](https://www.dndbeyond.com/monsters/5195080-homunculus) |
| AT-040 | [Pseudodragon](https://www.dndbeyond.com/monsters/16986-pseudodragon) | CA 13; PV 7; ataques separados Bite e Sting | [CA 14; PV 10; Multiattack e Sting reestruturados](https://www.dndbeyond.com/monsters/4775834-pseudodragon) |

Estas são **diferenças de edição**, não constatação de erro no catálogo canônico. Apenas uma comparação formal da versão canônica com SRD 5.2.1 poderá promover correções; não utilizar números da arte Legacy para resolver combates.

## Seis arquivos de arte preexistentes com ficha de pesquisa detalhada

IDs **TF-059, TF-060, TF-061, TF-063, TF-064, TF-065**: há metadados de caminho, dimensões, SHA-256 e fonte da imagem em `data/fichas-referencia-verificadas.json`. As fontes de ficha apontam para referências Kobold Press (Tome of Beasts 1/3). Sua presença e os metadados de integridade **não** equivalem à aprovação de arte, de licença comercial nem da mecânica no SRD Card Game.

A editora identifica a arte como **Product Identity** na [amostra editorial de Tome of Beasts 3](https://d1vzi28wh99zvq.cloudfront.net/pdf_previews/416964-sample.pdf). Por segurança, os seis itens continuam `PENDENTE_REVISAO_VISUAL_INDEPENDENTE_E_DIREITOS`. Não foram republicados novos arquivos binários nem incluídas as imagens no overlay do site.

## Testes e limites desta atualização

- O catálogo e os 14 tipos foram recontados no JSON real da branch de origem.
- Após adicionar somente **AT-089** ao overlay, a simulação da precedência do app chegou a **36 imagens**, **1.284 sem imagem**; nenhum ID de imagem aprovada repetido.
- As sete recusas possuem registros explícitos, não são carregadas pelo código do site e permanecem pesquisáveis no log.
- O `app.js`, HTML, CSS e os arquivos mecânicos canônicos **não** foram modificados; contrato de grade (imagem/nome) e modal preservado estruturalmente.
- **Não realizados:** teste visual em navegador com servidor HTTP e dispositivos, teste de resposta HTTP/MIME dos arquivos CDN ou auditoria integral dos 519 binários do acervo. Não afirmar que passaram.
- **Não realizada:** revisão independente das seis fichas Kobold Press ou concessão de direitos. Continuam como referências não homologadas.

**Estado após o lote:** 1 nova imagem de referência aceita; 7 novas candidatas rejeitadas; 5 diferenças de edição documentadas; 6 conjuntos imagem/ficha mantidos explicitamente pendentes; **1.284 criaturas sem ilustração de referência exibível**, mais auditoria editorial e de direitos para todas as demais.
