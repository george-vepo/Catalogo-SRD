# Integração DRAW → Pesquisa + ImageGen + ficha + suporte → GitHub

**Estado real:** hook de inspeção e ingestão criado. O `Catalogo-SRD` não contém o runtime do duelo que efetua `draw` / reposição. Por isso este hook **não é automaticamente disparado** no jogo até o árbitro/engine invocá-lo. Não usa nem cria credenciais, não altera estado de partida e não expõe cartas ocultas.

## Chamadas a partir do árbitro

Após **cada compra validada** no Chat Principal ou no chat privado autorizado, extraia **apenas o ID canônico do modelo** da cópia, sem comunicar o ID da cópia, conteúdo da mão, sequência do monte ou semente de embaralhamento. Dispare **uma vez por modelo por evento**, mantendo idempotência.

```bash
python scripts/srd_draw_enrichment.py inspect --model-id ML-0719 --expected-name Avestruzii
```

Retorna JSON com `image.available`, `statblock.full_verified`, `support.present` e uma fila `tasks`. O retorno não contém dados da partida.

- `GENERATE_IMAGE`: chamar o **ChatGPT ImageGen** para criar imagem original de espécie e variante verificadas; guardar arquivo local e registrar origem/revisão. *O hook Python não possui acesso à ferramenta ImageGen.*
- `RESEARCH_5E_STATBLOCK`: pesquisar ficha 5e da edição correta, erratas e fonte; preencher atributos, CDs, ações, dados, condições, duração, requisitos, recursos. Ficha pesquisada não vira homologada automaticamente.
- `DERIVE_SUPPORT_FROM_REAL_ABILITY`: usar uma habilidade da ficha real com ordem **Cura → Buff → Debuff → Dano**, preservando números e limites; incluir objeto `support` **dentro da ficha do modelo**.
- `REVIEW_SUPPORT`: se há proposta não homologada, reusar sem inventar outra nem executá-la no combate.

As tarefas de pesquisa e geração são realizadas pelo executor ChatGPT com ferramentas conectadas ou por implementação externa equivalente; não são simuladas pelo script.

Depois que uma **imagem/ficha/suporte novos foram efetivamente obtidos**, entregar a ficha integral/estruturada de pesquisa em JSON e o caminho da arte gerada ao hook de ingestão:

```bash
python scripts/srd_draw_enrichment.py stage --model-id ML-0719 \
  --research-file /caminho/para/ML-0719.json --image-file /caminho/para/ML-0719.webp
```

Para publicar via Git no **repositório local autenticado**, trabalhar numa branch `research/...`, com revisão antes do merge:

```bash
python scripts/srd_draw_enrichment.py stage --model-id ML-0719 \
  --research-file /caminho/para/ML-0719.json \
  --publish-branch research/creatures-5e-20261030
```

`--publish-branch` exige que a branch ativa seja exatamente essa e somente insere no commit caminhos recém-enriquecidos. Sem credencial Git ou sem o runtime chamador, a publicação automática não acontecerá. **No ChatGPT, quando o jogo estiver em andamento, o árbitro também pode publicar os novos artefatos por meio do conector GitHub**, mantendo os mesmos controles de privacidade e revisão.

## Formato da ficha candidata

```json
{
  "schema": "SRD_CREATURE_RESEARCH_CANDIDATE_V2",
  "model_id": "ML-0719",
  "canonical_name": "Avestruzii",
  "status": "PENDENTE_HOMOLOGACAO",
  "sources": ["URL da fonte de ficha 5e"],
  "support": {
    "status": "CANDIDATA_NAO_HOMOLOGADA",
    "approved": false,
    "source_ability": "Dig In",
    "category": "Buff",
    "effect_text_candidate": "Efeito condicionado aos limites originais, sujeito a revisão"
  }
}
```

## Proteções e pendências

- `inspect` é somente leitura e jamais compra cartas.
- Ninguém transforma pesquisa em ficha aprovada sem homologação explícita.
- Se a ficha estiver parcial, deve pesquisar antes do combate; o DRAW não é cancelado por falta de arte.
- Arte existente, mesmo candidata, bloqueia geração duplicada; candidato não é automaticamente arte aprovada.
- Suporte precisa ter origem em habilidade real da ficha, com limites e aplicação única; passivas e reações futuras exigem revisão individual para compatibilizar a preparação pré-iniciativa.
- Nenhuma informação de mão, monte, ID de cópia, jogador ou sorteio pode ser serializada nos arquivos públicos; `stage` rejeita campos privados mais comuns.
- Para automatizar *todo* o processo sem intervenção, faltam a integração com o motor real, acesso programático a ImageGen, pesquisa web verificável e um publicador autenticado; nenhum desses mecanismos foi fingido.

## Testes

```bash
python -m unittest discover -s tests -p 'test_srd_draw_enrichment.py' -v
```