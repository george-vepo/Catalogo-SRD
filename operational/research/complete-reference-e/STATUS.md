# SRD 607 — Fichas completas + imagens (lote E)

## Escopo verificado

- Catálogo-base: 607 criaturas.
- Imagens inicialmente pendentes: 584.
- Partição E: `pending_images.slice(195,390)`, exatamente 195 IDs, entre TF-059 e TF-269.
- Imagens binárias verificadas e disponíveis pela branch E: **181/195**.
- Imagens sem binário aprovado: **14/195**.
- Mecânicas marcadas `SIM` no CSV-base: **3/195**; as outras 192 não devem ser tratadas como fichas canônicas completas.

## Fichas que foram conferidas individualmente com a fonte

**6 fichas de referência D&D 5e detalhadas**, com atributos, CA, PV, deslocamentos, proficiência, salvaguardas, perícias, resistências, imunidades, sentidos, idiomas, traços e efeitos das ações, ações bônus e ausência explícita das ações não presentes:

- TF-059 — Animated Quartet
- TF-060 — Clockwork Abomination
- TF-061 — Clockwork Armadillo
- TF-063 — Clockwork Beetle Swarm
- TF-064 — Clockwork Conductor
- TF-065 — Clockwork Hound

[Galeria Markdown — seis fichas completas com imagens físicas](GALLERY.md)

Arquivos JSON:

- [TF-059, TF-060 e TF-061](statblocks/TF-059_TF-061.json)
- [TF-063, TF-064 e TF-065](statblocks/TF-063_TF-065.json)

Regras reescritas em português a partir das páginas individuais do KPOGL. Essas fichas são **referência de RPG**, não conversão aprovada para as regras específicas do card game.

## Extração ampliada para pesquisas sem invenção

Fonte consultada: JSONs do acervo TheGiddyLimit/homebrew das publicações Kobold Press (Tome of Beasts original, edição 2023, volumes 2 e 3 e Creature Codex). Em execução GitHub Actions bem-sucedida:

- **143 IDs**: um registro mecânico estruturado encontrado, com campos essenciais presentes; **ainda sem revisão individual**.
- **41 IDs**: duas ou mais variantes/edições encontradas; **não escolher automaticamente**.
- **11 IDs**: nenhuma correspondência exata nos cinco livros consultados.
- **0 promoções** automáticas para o CSV, ledger ou catálogo canônico.

[Extração JSON com dados e conflitos por criatura](source-extractions/kobold_candidates_e.json) (aproximadamente 1,13 MB).

[Resumo legível dos 195 IDs, com as 41 edições conflitantes e 11 sem correspondência](source-extractions/coverage_summary_e.json).

**Auditoria de imagens restantes:** a consulta às páginas oficiais A5E identificou ilustrações gerais de Aboleth, Werewolf, Spirit Naga e Guardian Naga nas páginas de variantes, mas essas artes não são comprovadamente as criaturas específicas TF-200, TF-201, TF-226 e TF-231. Não foram promovidas nem copiadas para simular cobertura. Para os demais IDs buscados não surgiu arte específica verificável. Evidência: [execução de auditoria de imagens](https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/actions/runs/38499323349).

Execução: https://github.com/george-vepo/SRD-Card-Game-607-Supervisor/actions/runs/38498936377

## Critério de conclusão

Uma ficha só pode avançar ao estado final do jogo quando houver:

1. Identificação e edição corretas, sem misturar versões.
2. Todos os dados de combate e exceções aplicáveis, inclusive ações, reações, magias e recargas, com fonte rastreável.
3. Tradução fiel das **mecânicas** e adaptação autoral às regras reais do card game.
4. Imagem específica em binário local e verificação por hash e decodificação.
5. Revisão independente e gates de integração.

Imagens ausentes e correspondências duplicadas precisam ser resolvidas individualmente; não usar uma imagem genérica para preencher o campo.

## Isolamento

Esta branch se origina de `chatgpt/srd607-image-assets-e`, que fornece os 181 arquivos reais. A branch E de imagens **não é modificada** pelos arquivos de mecânica desta PR. Não são alterados `main`, CSV, ledger global, PR #1, nem trabalhos atribuídos aos chats D/F e A/B/C.

**Não declarar 195 fichas concluídas. Não executar merge automático.**
