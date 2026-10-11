# SRD-607 — revisão independente do ciclo 21–25

Data: 2026-10-11  
Pacote revisado: `SRD_CYCLES/21-25/SRD_PACOTE_CONTINUIDADE_LOTE25_2026-10-11.zip`  
SHA-256 observado: `04614280e4a25b744b47d111517a105170c1f4ea4e3da4f4865d9ac69e068dbc`

## Resultado

**BLOQUEADA — sem veredito independente Codex.**

O Codex secundário foi iniciado duas vezes, sempre em modo não interativo e sem autorização para alterar arquivos:

1. `codex exec --ephemeral --sandbox read-only --model gpt-5.6-luna ...` — `exit 1`.
2. `codex exec --ephemeral --sandbox workspace-write --ignore-user-config --model gpt-5.6-luna ...` — `exit 1`.

Nos dois casos o runtime retornou `failed to initialize in-process app-server client: Acesso negado (os error 5)`, após avisos de falha de manutenção do banco de logs. Nenhum dos processos produziu um relatório de revisão e nenhum arquivo do workspace foi alterado por eles. O resultado não é convertido em aprovação.

## Evidência local independente disponível

- O ZIP final tem 20 entradas, zero nomes duplicados e contém `00_PACOTE_BASE`, `01_CONTINUIDADE`, `02_SAIDA_v2.1.0`, `03_CONSTRUTOR` e `04_INSUMOS`.
- O manifesto tem 19 entradas e foi recalculado contra os bytes do ZIP: zero divergências.
- O pacote-base aninhado tem SHA-256 `7046aebdbd75db46d1be2da1bd8e478070e7bbe4076207e80099311f3a901bca`.
- Os artefatos locais preservam 607 IDs únicos: 208 completos, 399 incompletos e 23 imagens diretas verificadas; os cinco IDs do ciclo são `KP-A006`, `KP-A020`, `KP-S003`, `KP-S006` e `KP-S007`.
- Os dois DOCX têm estrutura ZIP válida e `python-docx 1.2.0` abriu ambos. Isso não prova inspeção visual.
- O prompt do próximo processo contém exatamente as posições 26, 27, 28, 29 e 30; não foram encontrados padrões de credenciais nos artefatos auditados.
- `soffice.exe` não está disponível; o relatório marca o gate visual como bloqueado.

## Condição para aceite

Um agente Codex independente precisa executar a revisão e emitir veredito após o runtime/app-server deixar de retornar `Acesso negado`. Até lá, o pacote é um artefato parcial validado localmente, não uma execução aprovada/concluída.
