# SRD Card Game 607 — caso TF-022: imagem e mecânicas pendentes

**Data:** 2026-10-14. **Lote:** 002. **Status:** INVESTIGADO, BLOQUEADO PARA INTEGRAÇÃO; nenhuma imagem ou mecânica corrigida.

## Evidência no repositório

- ID `TF-022`, criatura `Beetle, Giant Bombardier`.
- Fonte operacional: `operational/research/deep-mechanics/a/records/TF-022.json` (blob `fd0ee14586d738347bbc28f7c7a8aec418c1f332`).
- Auditoria: `operational/reviews/20261014-imaged-cards/final-audit/batches/batch-002.json` (blob `19ad39922380cb091810fe5046d7dd4432df0429`): `FICHA_INCOMPLETA`, `IMAGEM_AUSENTE`.
- O objeto `imagem` do lote possui `caminho=null`, `sha_git=null`, `bytes=null`, `licenca=NAO_COMPROVADA`, `production_approved=false`.
- Verificação de diretórios feita via API GitHub na branch de auditoria: não foi encontrada entrada com `TF-022`, `bombardier` ou `beetle` entre os nomes dos 124 arquivos em `operational/research/deep-mechanics/a/images/` nem nas 519 entradas do primeiro nível de `operational/assets/creature-images/`. **Isto não prova ausência no repositório inteiro nem exclui arquivos de nomes diferentes.**

## Fontes e riscos de licenciamento

- O registro histórico atribui a origem a Kobold Press, sem edição/printing exatos confirmados. A fonte secundária de texto mecânico registrada é `https://www.5esrd.com/database/creature/beetle-giant-bombardier/`; o próprio registro indica verificação integral pendente.
- A licença OGL 1.0a publicada por Kobold Press distingue conteúdo mecânico aberto de **identidade de produto e arte**. Referência: https://koboldpress.com/open-game-license-version-1-0a/ . Isso **não prova** a licença específica de qualquer imagem encontrada em outra página ou repositório.
- A política de uso comunitário de Kobold Press é expressamente **não comercial**, autoriza apenas materiais específicos e não constitui autorização genérica para reproduzir ilustrações de bestiários: https://koboldpress.com/kobold-press-community-use-policy/ .
- Uma imagem encontrada em busca pública, mesmo que retrate um inseto semelhante, **não foi identificada como arte da criatura desta edição nem teve licença comprovada**. Não a incorporar no jogo.

## Pendências de mecânica e aceite

- `Bite` e `Spray` permanecem `status=INCOMPLETA` no registro original: campos estruturados, CD, alcance, dano, gatilhos e publicação exata dependem de cotejo com fonte autorizada.
- Definir edição-alvo, confirmar licenciamento e autoria de uma arte efetivamente correspondente, conferir a identidade visual e a dimensão real do arquivo.
- Só alterar assets e fichas canônicos mediante autorização específica, direitos comprovados e gates aplicáveis.

**Resultado:** 1 de 49 casos de imagens ausentes teve investigação documental inicial; **0 imagens recuperadas ou aprovadas e 0 lacunas mecânicas solucionadas**.
