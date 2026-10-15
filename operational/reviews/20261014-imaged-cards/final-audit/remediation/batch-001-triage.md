# SRD Card Game 607 — Tratamento seguro, lote 001 (10 cartas)

**Data da triagem:** 2026-10-14. **Estado:** EM INVESTIGAÇÃO; nenhum problema mecânico ou de arte foi declarado resolvido. Documento operacional, não ficha canônica.

**Base de evidência:** `operational/reviews/20261014-imaged-cards/final-audit/batches/batch-001.json` (Git blob `89652fb16bdf0ce2ecc9cfc11dc707bbbfe48700`), cruzado com `audit-results.csv` e com os registros individuais onde indicado. Branch `chatgpt/srd607-audit-imaged-cards-continuation-20261014`. A auditoria documental 395/395 foi reconciliada, porém a validação editorial, visual, de licenças, builds e E2E permanece pendente.

## Resultado do lote

- 10 IDs conferidos em sua ordem original; 9 fichas incompletas, 1 não verificável; nenhuma ficha promovida a completa.
- 10 vínculos diretos de imagens documentados no GitHub. Nenhuma imagem foi rehomologada visualmente ou para uso comercial nesta triagem.
- 3 arquivos com dimensões declaradas de 280×280 (KP-S015, KP-S016, KP-S018). Essas dimensões são metadados históricos, não nova medição dos binários.
- Licença de uso no jogo: `NAO_COMPROVADA` em todos os 10 registros. Não promover imagens a assets finais sem autorização verificável.

## Pendências priorizadas por cartão

### 01. KP-S011 — Abominable Beauty

- **Situação:** `FICHA_NAO_VERIFICAVEL`; P0 — seleção de edição.
- **Fonte operacional:** `operational/research/deep-mechanics/a/records/KP-S011.json`.
- **Imagem:** `IMAGEM_VINCULADA_DIRETAMENTE`; dimensões declaradas 555×1000; licença `NAO_COMPROVADA`.
- **Problemas documentados:** Edição canônica não definida: a versão original de 2016 e a edição revisada de 2023 divergem em Multiattack, Slam, Burning Touch, Blinding Gaze e Deafening Voice. O JSON estrutura o candidato 2023, mas registra mechanics_source_statblock_full=false e ainda não cotejou a publicação primária. A transcrição secundária mistura Undead Nature de outra criatura; não incorporá-la sem confirmação. Divergência mecânica explícita 2016 x 2023; seleção editorial pendente.
- **Próxima ação:** Definir edição-alvo, cotejar livro/errata e reconstruir somente se necessário; depois revisar arte e licença.

### 02. KP-S013 — Giant, Jotun

- **Situação:** `FICHA_INCOMPLETA`; P1 — estruturação editorial.
- **Fonte operacional:** `operational/research/deep-mechanics/a/records/KP-S013.json`.
- **Imagem:** `IMAGEM_VINCULADA_DIRETAMENTE`; dimensões declaradas 905×1000; licença `NAO_COMPROVADA`.
- **Problemas documentados:** 11 habilidade(s) registrada(s) apenas como resumo com status PENDENTE_ESTRUTURACAO_INTEGRAL; completar campos e regras individuais.
- **Próxima ação:** Estruturar as mecânicas pendentes individualmente contra fonte autorizada, verificar versões, depois adaptar ao card game e revisar arte/licença.

### 03. KP-S014 — Pustulent Shambler

- **Situação:** `FICHA_INCOMPLETA`; P1 — estruturação editorial.
- **Fonte operacional:** `operational/research/deep-mechanics/a/records/KP-S014.json`.
- **Imagem:** `IMAGEM_VINCULADA_DIRETAMENTE`; dimensões declaradas 941×813; licença `NAO_COMPROVADA`.
- **Problemas documentados:** 8 habilidade(s) registrada(s) apenas como resumo com status PENDENTE_ESTRUTURACAO_INTEGRAL; completar campos e regras individuais.
- **Próxima ação:** Estruturar as mecânicas pendentes individualmente contra fonte autorizada, verificar versões, depois adaptar ao card game e revisar arte/licença.

### 04. KP-S015 — Ooze, Scintillating

- **Situação:** `FICHA_INCOMPLETA`; P1 — estruturação editorial.
- **Fonte operacional:** `operational/research/deep-mechanics/a/records/KP-S015.json`.
- **Imagem:** `IMAGEM_VINCULADA_DIRETAMENTE`; dimensões declaradas 280×280; licença `NAO_COMPROVADA`.
- **Problemas documentados:** 11 habilidade(s) registrada(s) apenas como resumo com status PENDENTE_ESTRUTURACAO_INTEGRAL; completar campos e regras individuais. Quatro ações lendárias ainda em resumos; estruturar custo, gatilhos e efeitos.
- **Próxima ação:** Estruturar as mecânicas pendentes individualmente contra fonte autorizada, verificar versões, depois adaptar ao card game e revisar arte/licença.

### 05. KP-S016 — First Servant

- **Situação:** `FICHA_INCOMPLETA`; P1 — mecânicas complexas.
- **Fonte operacional:** `operational/research/deep-mechanics/a/records/KP-S016.json`.
- **Imagem:** `IMAGEM_VINCULADA_DIRETAMENTE`; dimensões declaradas 280×280; licença `NAO_COMPROVADA`.
- **Problemas documentados:** 6 habilidade(s) registrada(s) apenas como resumo com status PENDENTE_ESTRUTURACAO_INTEGRAL; completar campos e regras individuais. Conjuração de nível 18 sem repertório integral verificado, slots, magias e ações relevantes.
- **Próxima ação:** Estruturar as mecânicas pendentes individualmente contra fonte autorizada, verificar versões, depois adaptar ao card game e revisar arte/licença.

### 06. KP-S017 — Vesiculosa

- **Situação:** `FICHA_INCOMPLETA`; P1 — estruturação editorial.
- **Fonte operacional:** `operational/research/deep-mechanics/a/records/KP-S017.json`.
- **Imagem:** `IMAGEM_VINCULADA_DIRETAMENTE`; dimensões declaradas 1000×812; licença `NAO_COMPROVADA`.
- **Problemas documentados:** 1 habilidade(s) registrada(s) apenas como resumo com status PENDENTE_ESTRUTURACAO_INTEGRAL; completar campos e regras individuais. A ficha não apresenta ações estruturadas; confirmar ações e efeitos aplicáveis na fonte original.
- **Próxima ação:** Estruturar as mecânicas pendentes individualmente contra fonte autorizada, verificar versões, depois adaptar ao card game e revisar arte/licença.

### 07. KP-S018 — Sinstar

- **Situação:** `FICHA_INCOMPLETA`; P1 — mecânicas complexas.
- **Fonte operacional:** `operational/research/deep-mechanics/a/records/KP-S018.json`.
- **Imagem:** `IMAGEM_VINCULADA_DIRETAMENTE`; dimensões declaradas 280×280; licença `NAO_COMPROVADA`.
- **Problemas documentados:** 17 habilidade(s) registrada(s) apenas como resumo com status PENDENTE_ESTRUTURACAO_INTEGRAL; completar campos e regras individuais. Ações lendárias e ações de covil não estão operacionalmente estruturadas.
- **Próxima ação:** Estruturar as mecânicas pendentes individualmente contra fonte autorizada, verificar versões, depois adaptar ao card game e revisar arte/licença.

### 08. TF-004 — Astral Snapper

- **Situação:** `FICHA_INCOMPLETA`; P1 — estruturação editorial.
- **Fonte operacional:** `operational/research/deep-mechanics/a/records/TF-004.json`.
- **Imagem:** `IMAGEM_VINCULADA_DIRETAMENTE`; dimensões declaradas 820×961; licença `NAO_COMPROVADA`.
- **Problemas documentados:** 3 habilidade(s) registrada(s) apenas como resumo com status PENDENTE_ESTRUTURACAO_INTEGRAL; completar campos e regras individuais.
- **Próxima ação:** Estruturar as mecânicas pendentes individualmente contra fonte autorizada, verificar versões, depois adaptar ao card game e revisar arte/licença.

### 09. TF-010 — Chelicerae

- **Situação:** `FICHA_INCOMPLETA`; P1 — estruturação editorial.
- **Fonte operacional:** `operational/research/deep-mechanics/a/records/TF-010.json`.
- **Imagem:** `IMAGEM_VINCULADA_DIRETAMENTE`; dimensões declaradas 1000×771; licença `NAO_COMPROVADA`.
- **Problemas documentados:** 9 habilidade(s) registrada(s) apenas como resumo com status PENDENTE_ESTRUTURACAO_INTEGRAL; completar campos e regras individuais. Confirmar habilidades de conjuração, ação bônus Siphon Magic e divergência entre versões.
- **Próxima ação:** Estruturar as mecânicas pendentes individualmente contra fonte autorizada, verificar versões, depois adaptar ao card game e revisar arte/licença.

### 10. TF-011 — Child of Yggdrasil

- **Situação:** `FICHA_INCOMPLETA`; P1 — estruturação editorial.
- **Fonte operacional:** `operational/research/deep-mechanics/a/records/TF-011.json`.
- **Imagem:** `IMAGEM_VINCULADA_DIRETAMENTE`; dimensões declaradas 756×1108; licença `NAO_COMPROVADA`.
- **Problemas documentados:** 5 habilidade(s) registrada(s) apenas como resumo com status PENDENTE_ESTRUTURACAO_INTEGRAL; completar campos e regras individuais.
- **Próxima ação:** Estruturar as mecânicas pendentes individualmente contra fonte autorizada, verificar versões, depois adaptar ao card game e revisar arte/licença.

## Gates e próximas ações

1. **KP-S011:** decisão editorial explícita de 2016 vs 2023, seguida de cotejo com publicação/erratas. Não consolidar habilidades de edições diferentes.
2. **KP-S013, KP-S014, KP-S015, KP-S016, KP-S017, KP-S018, TF-004, TF-010, TF-011:** estruturar mecanicamente apenas regras confirmadas na fonte autorizada, incluindo ações, duração, alcances, dano, CDs e recargas quando pertinentes. Manter campos desconhecidos como pendentes.
3. **Licenciamento e identidade:** avaliar as dez imagens e priorizar as três 280×280; nenhum arquivo de arte foi substituído.
4. **Imagens ausentes em outros lotes:** iniciar pelo TF-022 (lote 002), que tem registro mecânico parcial e nenhuma imagem vinculada na auditoria. Buscar autorização e correspondência antes de incorporar arte.
5. **Saída:** produzir evidências de cotejo e, somente depois, propor alterações em registros operacionais. Fichas/ativos canônicos exigem gates próprios e autorização.

**Execução nesta etapa:** leitura direta de evidências e escrita apenas deste documento operacional; sem agentes/revisores de IA, sem alteração de fichas ou imagens, sem build, CI Windows, teste de jogo, E2E ou merge.
