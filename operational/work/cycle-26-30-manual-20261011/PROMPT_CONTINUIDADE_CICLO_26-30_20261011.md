# Prompt de continuidade — SRD Card Game 607 — ciclo 26–30

Use este documento como handoff operacional completo da execução do ciclo 26–30. Ele descreve o que já foi feito, o que foi comprovado, o que permanece pendente e a ordem obrigatória para concluir o lote sem perder evidências.

## Papel e contrato obrigatório

Você é o próximo agente Codex responsável por continuar esta tarefa. Siga o `D:\Repos\AGENTS.md` e as instruções do repositório. Somente Codex pode entender, planejar, executar, testar, validar, revisar e aprovar. Não invoque Claude, DeepSeek, CodeWhale ou qualquer outro provedor, inclusive como fallback.

`IMPLEMENTADO != CONCLUÍDO`. Só declare `COMPLETED` depois de confirmar implementação, testes, validação, evidência verificável, revisão independente e aprovação final do Codex principal. Um checkbox, relato de worker, processo ativo, teste isolado ou pacote gerado não substitui esses gates.

Preserve alterações existentes, credenciais, histórico Git, worktrees e arquivos superseded. Não use `git reset`, `git clean`, troca de branch, commit, push, publicação, login, instalação ou remoção destrutiva sem autorização explícita. Não reescreva o pacote-base histórico.

## Escopo

- Repositório: `D:\Repos\SRD-Card-Game-607-Supervisor`
- Tarefa: `SRD-Card-Game-607-cycle-26-30-20261011`
- Lote em execução: `26–30` (exatamente os cinco próximos IDs pendentes)
- Próximo lote, ainda não executado: `31–35`
- Não executar, criar ou antecipar artefatos de `31–35` nesta tarefa.
- Não incluir V-Bridge, navegador ChatGPT ou qualquer outro projeto.
- O lote deve preservar os 28 homebrews/IDs 607 excluídos do escopo anterior.

Log operacional canônico:

`D:\Repos\logs\20261011-003209__SRD-Card-Game-607-cycle-26-30-20261011__SRD-Card-Game-607-Ciclo-26-30.md`

Atualize esse mesmo log com `D:\Repos\.agents\scripts\Update-CodexTaskLog.ps1` a cada marco material. Não crie um segundo log para esta tarefa. O estado real deve indicar estado, gate, evidência, próxima ação, responsável e condição de parada.

## Artefatos principais

Pacote-base histórico, imutável:

`D:\Repos\SRD-Card-Game-607-Supervisor\SRD_CYCLES\21-25\SRD_PACOTE_CONTINUIDADE_LOTE25_2026-10-11.zip`

SHA-256 obrigatório do pacote-base:

`04614280e4a25b744b47d111517a105170c1f4ea4e3da4f4865d9ac69e068dbc`

Pacote canônico atual do lote 26–30:

`D:\Repos\SRD-Card-Game-607-Supervisor\SRD_CYCLES\26-30\SRD_PACOTE_CONTINUIDADE_LOTE30_2026-10-11.zip`

SHA-256 confirmado na geração mais recente:

`2f04c5fc9a31215b9a92b5e009bc1d231b042a22c8530551e62fa804543cb218`

Esse SHA foi confirmado pelo audit final corrigido após a disposição do finding de KP-S012. Ele identifica o pacote atual, mas não substitui a nova revisão independente nem o gate visual.

Diretório de trabalho do lote:

`D:\Repos\SRD-Card-Game-607-Supervisor\SRD_CYCLES\26-30\working`

Construtor principal:

`D:\Repos\SRD-Card-Game-607-Supervisor\SRD_CYCLES\26-30\working\03_CONSTRUTOR\build_deliverables.py`

Leia-me do lote:

`D:\Repos\SRD-Card-Game-607-Supervisor\SRD_CYCLES\26-30\working\03_CONSTRUTOR\LEIA-ME.txt`

Helper de empacotamento:

`D:\Repos\SRD-Card-Game-607-Supervisor\New-SRDOperationalContinuationPackage.ps1`

## Estado de origem e preparação já concluída

1. O pacote-base foi extraído no diretório de trabalho e os diretórios `03_CONSTRUTOR` e `04_INSUMOS` foram preparados.
2. A base foi verificada pelo SHA-256 exato acima.
3. O Git do repositório não possui commits; os arquivos existentes aparecem como não rastreados. Esse estado foi preservado. Não fazer commit ou limpeza.
4. Não foram encontrados artefatos de execução dos ciclos `31–35` ou `LOTE35`.
5. O runtime Python bundled usado e validado é:
   `C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
6. O runtime observado foi Python 3.12.14 com `python-docx` 1.2.0. Não instalar dependências nem usar `pip`.
7. Não foi encontrado `soffice.exe` nem `libreoffice` no `PATH`; a verificação observada foi `NO_SOFFICE_COMMAND_FOUND`.

## Cinco IDs do ciclo 26–30

IDs atuais e estado pretendido no pacote:

- `KP-S008` — Arcane Leviathan — completo.
- `KP-S009` — Primordial Surge — completo.
- `KP-S010` — Primordial Matriarch — completo.
- `KP-S011` — Abominable Beauty — parcial, por inconsistência da fonte em `Undead Nature`.
- `KP-S012` — Hvalfiskr — completo.

Fontes estáveis preservadas nos dados atuais:

- [`KP-S008`](https://www.5esrd.com/database/creature/arcane-leviathan/)
- [`KP-S009`](https://www.5esrd.com/database/creature/primordial-surge/)
- [`KP-S010`](https://www.5esrd.com/database/creature/primordial-matriarch/)
- [`KP-S011`](https://www.5esrd.com/database/creature/abominable-beauty/)
- [`KP-S012`](https://kpogl.wikidot.com/monster:hvalfiskr)

Contagens esperadas após a geração:

- IDs totais: `607`.
- Fichas locais: `108`.
- Fichas externas integradas: `104`.
- Fichas completas: `212`.
- Fichas pendentes: `395`.
- Imagens verificadas: `23`.
- Páginas conhecidas: `119`.
- Páginas conhecidas ainda pendentes: `15`.
- A página `380` não deve ser criada.
- URLs antigas retestadas: `7`.

## Alterações já implementadas

No construtor, foram feitas as seguintes alterações:

1. Data do ciclo ajustada para `2026-10-11` e lote para `26-30`.
2. Foram adicionados os cinco registros externos acima.
3. Foram definidos os estados do lote:

   ```text
   CURRENT_BATCH_IDS = ['KP-S008','KP-S009','KP-S010','KP-S011','KP-S012']
   CURRENT_REVIEWED_PENDING_IDS = []
   CURRENT_PARTIAL_IDS = ['KP-S011']
   CURRENT_COMPLETE_IDS = ['KP-S008','KP-S009','KP-S010','KP-S012']
   ```

4. `KP-S011` mantém `Undead Nature` em `tracos`, não em `acoes`; o registro permanece parcial e a inconsistência da fonte está explicitada.
5. `KP-S010` foi corrigido para incluir os efeitos de sucesso de `Storm Blast`, os efeitos de falha, a limpeza de ácido/fogo, a repetição de salvamento de trovão e a economia de covil: iniciativa 20, perdendo empates, sem repetir o mesmo efeito em rodadas consecutivas.
6. A economia de covil também foi inserida na renderização DOCX.
7. `KP-S009` foi corrigido para a duração correta de `Primordial Form`: cegueira/surdez até a criatura iniciar o turno fora do espaço da onda.
8. `KP-S012` foi corrigido para os sentidos suportados: `blindsight 120 ft. (somente forma de baleia)` e `darkvision 120 ft.`; não usar “blind beyond range”.
9. A data de verificação dos 108 registros externos históricos anteriores foi preservada como `2026-10-10`. Somente os cinco registros atuais usam `2026-10-11`.
10. Os marcadores internos de citação do tipo `turn...view...`/`turn...search...` foram removidos dos artefatos atuais distribuídos pelo construtor. As citações atuais mantêm URLs estáveis.
11. Foi corrigido o fallback de citação para garantir que cada `fonte_citacao_web` dos cinco IDs atuais contenha a URL estável correspondente, não apenas um rótulo.
12. O helper de empacotamento foi ajustado para localizar dinamicamente exatamente um ZIP de imagens `SRD_FICHAS_IMAGENS_607_v*.zip`, em vez de depender do nome antigo.
13. O `LEIA-ME.txt` documenta expressamente o escopo do gate de citações: o scan de marcadores aplica-se aos artefatos atuais; o `00_PACOTE_BASE` é um checkpoint histórico preservado byte a byte e não é reescrito nem usado como prova de ausência de marcadores atuais.
14. Após a quarta revisão, `KP-S010` foi corrigido novamente: `Create Elementals` agora registra que a dispensa de um ou mais elementais usa uma ação bônus, e `Consume` agora exige um ponto visível no solo.
15. Após a revisão seguinte, `Erratic Weather` foi corrigido para registrar que os eventos raramente duram mais de uma hora e que os efeitos desaparecem ao longo de 1d10 dias após a morte da matriarca.
16. O CSV `SRD_AUDITORIA_PENDENCIAS_607.csv` foi corrigido para preservar `2026-10-10` nas 108 observações históricas e usar `2026-10-11` somente nos cinco registros atuais.
17. Após a revisão do SHA `dd3fdee`, `KP-S012` foi corrigido: `Chained Anchor` agora descreve o teste de Força CD 19 como `teste_atributo`, registra que destruir a corrente desprende a âncora para espaço desocupado até 5 ft. do alvo e impede `Reel Anchor`.

## Revisões independentes já realizadas e disposição

Os resultados abaixo são históricos e não substituem uma revisão do SHA atual:

1. A revisão do pacote inicial foi interrompida/fechada; não foi aceita como veredicto.
2. A revisão do SHA `44c00a20d0d9d7e9278f3a107642b0beb042cbfe00ed5e67a185f49204c75ed5` retornou `CHANGES_REQUIRED` por efeitos incompletos de `KP-S010`, duração incorreta em `KP-S009`, sentidos incorretos em `KP-S012`, datas históricas sobrescritas, marcadores internos no construtor e gate visual pendente. Todos os achados de conteúdo foram corrigidos.
3. A revisão do SHA `476adedf20880e3dcaba250ba93904eb4875583b5ff187761ee20f96b5b330b9` retornou `CHANGES_REQUIRED` porque a economia de covil não estava no DOCX/ZIP interno. A renderização foi corrigida.
4. A revisão do SHA `1aeb89691f3f592be710429d783004781ac915ea16dba319107bd942129e3436` retornou `CHANGES_REQUIRED` por cinco campos de citação atuais sem URL estável e por uma observação de baixo risco sobre marcadores no pacote-base histórico. As cinco URLs foram corrigidas. O pacote-base não deve ser adulterado; o escopo de scan foi documentado no `LEIA-ME.txt`.
5. A revisão do SHA `f0f94f2269291bb477e6ba84d0c57d81fe5734bb5e4486edefd3b464c844ef2b` retornou `CHANGES_REQUIRED` por duas omissões em `KP-S010`: a ação bônus para dispensar elementais e a exigência de ponto visível em `Consume`. Ambas foram corrigidas no construtor e regeneradas no pacote atual.
6. A revisão do SHA `63fc0050022ed7fa107e2d9ac559246c6dc6d8345f71c1b64602a2708bf055aa` confirmou as correções anteriores, mas retornou `CHANGES_REQUIRED` por `Erratic Weather` excessivamente restritivo e datas históricas incorretas no CSV. Ambos foram corrigidos e regenerados no pacote atual.
7. A revisão do SHA `dd3fdee08510c0390af2201375fc070ea65dfce176d52c3e38b7718fc36a8f3f` confirmou as correções anteriores, mas retornou `CHANGES_REQUIRED` por `Chained Anchor` incompleto em `KP-S012` e pela classificação incorreta do teste de Força. Ambos foram corrigidos e regenerados no pacote atual.

Pacotes superseded preservados, sem exclusão:

- `...\\superseded\\SRD_PACOTE_CONTINUIDADE_LOTE30_2026-10-11.initial.zip` — SHA `b6161c8e2ddcb815bd5397d92c79da9eb40961558cfcc95091e4be02ed523116`.
- `...\\superseded\\SRD_PACOTE_CONTINUIDADE_LOTE30_2026-10-11.pre-findings-correction.zip` — SHA `44c00a20d0d9d7e9278f3a107642b0beb042cbfe00ed5e67a185f49204c75ed5`.
- `...\\superseded\\SRD_PACOTE_CONTINUIDADE_LOTE30_2026-10-11.pre-citation-fallback.zip` — SHA `098300d95e8bede6d613babf5fb6a9f7d93a29099a1d2b90cbf490b2c2849a5e`.
- `...\\superseded\\SRD_PACOTE_CONTINUIDADE_LOTE30_2026-10-11.pre-docx-correction.zip` — SHA `476adedf20880e3dcaba250ba93904eb4875583b5ff187761ee20f96b5b330b9`.
- `...\\superseded\\SRD_PACOTE_CONTINUIDADE_LOTE30_2026-10-11.pre-source-url-correction.zip` — SHA `1aeb89691f3f592be710429d783004781ac915ea16dba319107bd942129e3436`.
- `...\\superseded\\SRD_PACOTE_CONTINUIDADE_LOTE30_2026-10-11.pre-kp-s010-fix.zip` — SHA `f0f94f2269291bb477e6ba84d0c57d81fe5734bb5e4486edefd3b464c844ef2b`.
- `...\\superseded\\SRD_PACOTE_CONTINUIDADE_LOTE30_2026-10-11.pre-erratic-weather-csv-fix.zip` — SHA `63fc0050022ed7fa107e2d9ac559246c6dc6d8345f71c1b64602a2708bf055aa`.
- `...\\superseded\\SRD_PACOTE_CONTINUIDADE_LOTE30_2026-10-11.pre-kp-s012-chained-anchor-fix.zip` — SHA `dd3fdee08510c0390af2201375fc070ea65dfce176d52c3e38b7718fc36a8f3f`.

## Gates já observados

Os seguintes checks já foram executados com sucesso e reconciliados com o pacote canônico atual:

- AST compile do construtor.
- Execução do construtor com o Python bundled.
- Abertura de DOCX com `python-docx`.
- Contagens esperadas de 607 IDs, 212 fichas completas, 395 pendentes e 23 imagens.
- Verificação das cinco URLs atuais.
- Verificação dos estados e correções mecânicas descritas acima.
- Audit final corrigido do pacote atual, com resultado `FINAL_PACKAGE_AUDIT_PASS`.

Gates ainda abertos:

- O audit final do pacote SHA `2f04c5fc9a31215b9a92b5e009bc1d231b042a22c8530551e62fa804543cb218` passou. A tentativa anterior havia falhado por erro de sintaxe no próprio harness de auditoria (`print(json.dumps(...))` sem fechar `)`); o harness foi corrigido e o resultado atual é observável.
- A nova revisão independente Codex do SHA `2f04c5fc9a31215b9a92b5e009bc1d231b042a22c8530551e62fa804543cb218` ainda está pendente.
- O gate visual não foi executado porque não há `soffice.exe`/`libreoffice`. Não converter, instalar ou fingir o gate. Classifique como `NOT_TESTED`/`BLOCKED` com a evidência `NO_SOFFICE_COMMAND_FOUND`.
- O pacote-base histórico contém marcadores que não devem ser usados para declarar falha dos artefatos atuais. O base deve ser verificado somente por byte/hash/CRC e preservado exatamente.

## Próximas ações obrigatórias

Execute nesta ordem, registrando cada marco no log canônico:

### 1. Preservar o audit final local

O audit final já passou sem alterar os artefatos do produto. Se qualquer arquivo que compõe o pacote for alterado daqui em diante, reexecute o harness antes de prosseguir. O resultado confirmado contém:

- SHA-256 do pacote atual igual a `2f04c5fc9a31215b9a92b5e009bc1d231b042a22c8530551e62fa804543cb218`.
- SHA-256 do pacote-base igual a `04614280e4a25b744b47d111517a105170c1f4ea4e3da4f4865d9ac69e068dbc`.
- CRC do ZIP externo íntegro e exatamente 20 entradas únicas.
- Manifesto com exatamente 19 arquivos além do pacote-base e hashes/tamanhos consistentes.
- ZIP interno do pacote-base byte/hash esperado.
- Artefatos textuais atuais sem marcadores internos de citação.
- `LEIA-ME.txt` contendo o escopo explícito do gate atual versus checkpoint histórico.
- JSON com 607 IDs, 212 completos, 395 pendentes e estados exatos do lote.
- `KP-S011` com `Undead Nature` em `tracos`.
- `KP-S009` com o gatilho/duração corrigidos.
- `KP-S010` com efeitos de `Storm Blast`, economia de covil, iniciativa 20, desempate perdido, ação bônus para dispensa em `Create Elementals` e ponto visível em `Consume`.
- `KP-S010` com `Erratic Weather` preservando eventos que raramente duram mais de uma hora e desaparecem ao longo de 1d10 dias após a morte.
- `KP-S012` com os dois sentidos suportados.
- `KP-S012` com `Chained Anchor` completo: teste de Força diferenciado de salvaguarda, desprendimento da âncora após destruição da corrente e bloqueio de `Reel Anchor`.
- As cinco `fonte_citacao_web` atuais contendo suas URLs estáveis.
- As 108 datas externas históricas preservadas em `2026-10-10`.
- As 108 observações históricas do CSV também preservadas em `2026-10-10`; somente os cinco IDs atuais usam `2026-10-11`.
- Os seis CSVs com 607 registros.
- DOCX principal e DOCX interno abrindo, com `Economia de covil.` e iniciativa 20/perdendo empates.
- ZIP de imagens íntegro, com 7 entradas e 23 imagens verificadas.
- Relatório, estado e prompt apontando para o ciclo 26–30 e sem execução de 31–35.

O resultado confirmado do harness é `FINAL_PACKAGE_AUDIT_PASS`, incluindo `current_artifacts_internal_markers: 0`, `current_source_urls: 5`, `base_historical_markers: PRESERVED_IMMUTABLE_NOT_SCANNED_AS_CURRENT` e `visual_gate: NOT_TESTED_NO_SOFFICE`.

### 2. Reconfirmar o gate visual

Faça somente a verificação read-only de `soffice`/`libreoffice`. Se continuar ausente, registre `PARTIAL` ou `BLOCKED` conforme o contrato, com a saída observada. Não instale dependências, não converta por outro meio e não marque o gate como aprovado.

### 3. Solicitar a quarta revisão independente Codex

Despache um novo agente Codex independente, somente leitura, contra o SHA atual completo. Preferência obrigatória: `gpt-6.1-sol`, raciocínio `medium`, sem reutilizar o agente que implementou a mudança e sem editar o repositório. O prompt da revisão deve exigir:

- validação do ZIP e manifesto;
- confirmação do SHA atual e do SHA-base;
- rechecagem das cinco URLs estáveis;
- rechecagem das correções dos cinco IDs;
- confirmação das datas históricas preservadas;
- confirmação de que os artefatos atuais não possuem marcadores internos;
- confirmação de que o base histórico permanece imutável e que o escopo documentado é adequado;
- consideração explícita do gate visual `NOT_TESTED_NO_SOFFICE`;
- veredicto `PASS` ou `CHANGES_REQUIRED`, com findings acionáveis.

Trate a resposta do revisor como não verificada até reconciliar a resposta com o filesystem, os hashes, os testes e o log. Encerre o agente depois do resultado; não o deixe ativo sem necessidade.

### 4. Se houver findings

Persistir um plano de correção delimitado, corrigir somente o escopo autorizado usando Codex, regenerar o pacote, gerar novo SHA, repetir o audit local e solicitar nova revisão do novo SHA. Preserve todos os pacotes superseded e não reutilize uma aprovação de SHA antigo.

### 5. Encerrar o ciclo atual corretamente

- Se a revisão independente aprovar, todos os gates locais passarem e o gate visual continuar indisponível, o estado máximo demonstrável é `PARTIAL`/`BLOCKED`, nunca `COMPLETED`.
- Só use `COMPLETED` se implementação, testes, validação, evidência, review independente e gate visual aplicável estiverem comprovados.
- Atualize o log no resultado da revisão e no estado terminal. Use `Finish` somente com o estado permitido e evidência válida.
- Não declarar “done” apenas porque o ZIP foi criado ou porque o reviewer respondeu.

### 6. Próximo ciclo, somente depois do gate terminal

Quando o ciclo 26–30 estiver realmente aprovado, crie uma nova thread independente Codex para o ciclo 31–35, sem paralelismo e sem retomar a thread pai. Passe o pacote validado, seu SHA, o log e as restrições. Faça preflight e confirme o pacote-base antes de selecionar exatamente os próximos cinco pendentes. Não comece 31–35 durante a resolução deste handoff.

## Critério de parada

Pare somente em uma destas condições:

- `COMPLETED`: todos os gates aplicáveis foram comprovados e aprovados pelo Codex principal; ou
- `PARTIAL`, `BLOCKED` ou `UNKNOWN / INTERRUPTED`: existe impedimento observável documentado, com evidência, dependência ausente, impacto e ação necessária.

Se o audit do pacote passar e a revisão independente ainda estiver pendente, o estado é `SUCCEEDED_PENDING_VALIDATION`, não conclusão. Se a revisão passar mas o visual continuar indisponível, o resultado permanece parcial/bloqueado. Não faça retry cego e não esconda o bloqueio.

## Resumo executivo

O lote 26–30 foi implementado e corrigido, os findings adicionais das revisões independentes foram dispostos, o pacote atual foi regenerado com SHA `2f04c5fc9a31215b9a92b5e009bc1d231b042a22c8530551e62fa804543cb218` e o audit final passou. O próximo agente deve obter a nova revisão independente Codex, registrar o gate visual ausente e encerrar com o estado que a evidência realmente sustentar. O ciclo 31–35 só pode começar em uma nova execução depois disso.
