# DRAW — contrato de ficha enriquecida com suporte

Regra operacional solicitada em 2026-10-30. **Não publica mãos, ordem do monte, decks nem IDs de cópia.** É um fluxo de curadoria, não um gatilho automático implementado na engine.

## Unidade de armazenamento

Uma criatura = um modelo canônico e **uma ficha enriquecida**, indexada por `model_id`. A ficha deve conter:
- Identidade (ID canônico, nome, tipo, ND/raridade, edição correta).
- Fonte mecânica e situação da ficha (integral homologada, parcial, pesquisada ou pendente).
- Imagem por modelo com proveniência e status de homologação.
- Um objeto **`support` dentro da própria ficha enriquecida**, com habilidade original, categoria, texto do efeito, condições, CD/salvaguarda se houver, duração, gatilhos, recursos, limites, fontes, versão, `status` e `approved`.

**Nunca adicionar efeitos homebrew à ficha SRD oficial como se fossem ataques ou poderes originais.** Ficha original pode ser referenciada por `authoritative_statblock`; a seção `support` é do Card Game e deve ser diferenciada.

## Para cada modelo sacado em DRAW

1. Consultar por ID exato: ficha, suporte e imagem no catálogo/repositório e nas aprovações existentes.
2. Quando imagem estiver ausente: criar ilustração original com ImageGen e registrar arquivo, autoria/proveniência, hash e revisão visual; não substituir ilustração aprovada sem validação.
3. Quando ficha estiver ausente ou parcial: pesquisar **D&D 5e da edição correta** e registrar fonte, CA, PV, iniciativa, atributos, ações, economia de ações, resistências, testes, condições, duração, recursos e recargas, sem inventar valores. Distinguir ficha pesquisada de ficha integral homologada.
4. Quando `support` estiver ausente: **escolher uma habilidade REAL existente na ficha**, com preferência aprovada **Cura → Buff → Debuff → Dano**; preservar todos os gatilhos, CDs, valores, testes, limitações, usos e duração. Adaptar à criatura ativa apenas dentro das decisões do Card Game; marcar a transferência como homebrew e não inventar efeito independente.
5. Salvar o **efeito de suporte dentro do mesmo arquivo da ficha enriquecida** sob `support`. Se a fonte não permitir escolher habilidade real, registrar `support.status = PENDENTE_FICHA` com motivo, em vez de inventar.
6. Enviar ao GitHub apenas a **pesquisa por modelo**, fonte, arte, estado de revisão e suporte candidato. Nunca enviar a mão ou o estado do duelo. Usar commit/PR de revisão para conteúdo novo; não sobrescrever material homologado.
7. A carta de suporte **só é utilizável** quando `support.approved === true` e os requisitos da ficha/regras do jogo estiverem completos. `CANDIDATA_NAO_HOMOLOGADA` não autoriza execução em combate.

## Resolução de suporte e combate

- Uma carta de suporte selecionada ocupa a posição ao lado da criatura ativa.
- O administrador solicitou iniciativa própria das cartas de suporte antes da iniciativa de combate; registrar esta regra do Card Game separadamente do SRD, verificando aprovação/formalização e desempates.
- Suporte validado é aplicado **uma única vez por combate**, sem consumir ação/ação bônus/reação e segue ao descarte quando usado; efeitos em duração normal podem permanecer.
- Criaturas ativas utilizam suas próprias ações e recursos conforme SRD 5.2.1, sem ampliar o limite da carta de suporte.
- Em habilidades passivas/reativas, se não for possível aplicar uma única vez na janela pré-iniciativa sem inventar duração ou gatilho, o suporte deve ficar **bloqueado** para decisão administrativa.

## Abertura na interface ChatGPT

Ao selecionar uma carta da mão, mostrar ficha existente e uma seção **SUPORTE**: categoria, habilidade original, efeito, alvo, gatilho, CD, duração, limitações, estado de aprovação e fonte. Segundo toque abaixa a carta e fecha a seleção. **A seleção visual não executa o suporte**.

## Exemplo mínimo de campo

```json
{
  "model_id": "AT-096",
  "authoritative_statblock": {"source_repo_path": "docs/catalogo/data/fichas-607.json", "record_id": "AT-096"},
  "support": {
    "source_ability": "Bloodied Frenzy",
    "category": "Buff",
    "effect_text_candidate": "Texto derivado de uma habilidade real; transferência sujeita à aprovação",
    "status": "CANDIDATA_NAO_HOMOLOGADA",
    "approved": false,
    "uses_per_combat": 1,
    "usable_in_official_combat": false
  }
}
```

A documentação oficial do projeto (manual v0.9 e SRD 5.2.1) prevalece em conflitos; ausência de confirmação não autoriza homologação tácita.
