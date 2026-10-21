# Ausências de fichas no Excel v2.1 (auditoria somente leitura)

Foi localizada no Drive a planilha `SRD_Card_Game_Catalogo_Ativo_v2_1_Fichas_Integradas.xlsx` (modificada em 20/10/2026). A aba Resumo informa **139 criaturas com JSON e 146 documentos integrais**, sendo **68 JSON associados ao conjunto de 635 IDs ativos**. O mesmo resumo alerta que somente 9 fichas foram auditadas nessa execução: a existência do JSON não é homologação.

Todos os **29 IDs ausentes do arquivo web**, já registrados na auditoria de v2.0, aparecem na aba do catálogo com a indicação literal `SEM JSON NESTE ACERVO` e **não aparecem no índice de documentos integrais da v2.1**. Destes, **28 são homebrew do jogo e preservados na v2.0**; o restante é o `KP-S007`, de terceiros, com referência externa e ficha local pendente.

A expressão `FICHA COMPLETA ORIGINAL` em v2.0 registra uma declaração herdada: **não foram recuperados CA, PV, iniciativa, habilidades e ataques desses 28 registros pelo material v2.1**. Não presumir que possam participar de um combate ainda sem uma ficha integral verificada.

Os dados originais não foram alterados. Nenhuma criatura foi removida, substituída, homologada, nem teve estatística inventada. A planilha v2.1 é insumo para auditoria, **não a fonte substituta aprovada**.

Veja `auditoria/fichas-v21-29-ids-ausentes-20261021.json` para os 29 registros e a evidência de suas ausências.

Próxima pendência: localizar a **ficha de criação original dos 28 homebrew** em fontes anteriores ao Excel v2.1, validar sua integridade/versão contra as regras do jogo e documentar a decisão do administrador. A posição do KP-S007 deve ser tratada isoladamente.
