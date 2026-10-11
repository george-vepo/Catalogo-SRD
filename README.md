# Supervisor local do SRD Card Game 607

Este diretório contém o supervisor local em PowerShell para iniciar uma nova
execução independente de `codex exec` a cada janela de cinco lotes. Ele não
usa `codex exec resume`, não cria conversas do ChatGPT e não usa opções de
bypass de sandbox, aprovação ou confiança.

O par solicitado foi fixado nos prompts e na linha de comando como
`gpt-5.6-luna` com `model_reasoning_effort=max`. O supervisor só passa essa
configuração depois de confirmar, pelo `codex --version` e por
`codex exec --help`, que a instalação expõe as opções necessárias (`-C`, `-s`,
`--json` e `-o`).

## Modos

```powershell
pwsh -NoProfile -File .\Start-SRDCampaignSupervisor.ps1 -Mode SelfTest
pwsh -NoProfile -File .\Start-SRDCampaignSupervisor.ps1 -Mode Simulate -SimulationScenario normal
pwsh -NoProfile -File .\Start-SRDCampaignSupervisor.ps1 -Mode Prepare -PackagePath <LOTE20.zip>
pwsh -NoProfile -File .\Start-SRDCampaignSupervisor.ps1 -Mode Run -PackagePath <LOTE20.zip> -Workdir <repositorio-git>
pwsh -NoProfile -File .\Start-SRDCampaignSupervisor.ps1 -Mode Resume -Workdir <repositorio-git>
pwsh -NoProfile -File .\Start-SRDCampaignSupervisor.ps1 -Mode Cancel
```

`Prepare` valida o pacote sem iniciar pesquisa. Para a retomada atual, a
validação exige que o pacote contenha um pacote-base interno identificado
como LOTE20; um ZIP que apenas tenha LOTE20 no nome externo, mas contenha
LOTE16 como base, é bloqueado.

`Run` exige um repositório Git confiável e só despacha depois da validação do
pacote. Cada execução recebe um prompt próprio, um diretório de saída próprio,
uma chave de idempotência derivada de campanha/intervalo/SHA-256 e arquivos de
stdout, stderr e última mensagem. O estado durável fica em `state/campaign.json`
e o histórico sem segredos em `state/history.jsonl`.

Falha de preflight, credential broker, execução, auditoria, empacotamento ou
ZIP mantém o checkpoint e coloca a campanha em `BLOCKED`; não há avanço
silencioso. O supervisor encerra em `COMPLETED` quando as duas contagens
atingem a meta e não agenda outra janela.
