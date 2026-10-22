# Importação local pelo CMD

No Prompt de Comando, executar:

```cmd
D:\Repos\Catalogo-SRD\Importar-SRD-Local.cmd --aplicar
```

Sem `--aplicar`, apenas analisa e gera `logs/importacao-local.json`.
Para outro Drive: acrescentar `--drive-root "G:\Meu Drive\SRD Card Game"`.
O launcher usa o Python do PATH e instala Pillow 13.0.0 no perfil do usuário
se necessário no modo aplicar. Nenhum comando Git de commit/push é executado.

O importador lê Fichas/Completas e Imagens/Novas. Para imagens, somente nomes
contendo `rejeitada` (sem distinguir maiúsculas) impedem importação. Falhas reais
de leitura/conversão são relatadas como erro e produzem código de saída 1.
Arquivos iguais são reconhecidos por SHA-256. As imagens novas são convertidas
para WebP no acervo complementar `artes_locais`, sem substituir a arte principal.
Todas aparecem no acervo da página; variantes com identidade comprovada também
aparecem nos detalhes da criatura. Imagens sem vínculo confirmado são importadas
com essa pendência, sem criar IDs ou associar uma espécie por aproximação.

As fichas JSON são preservadas em envelopes complementares contendo identidade,
hash SHA-256 da origem e dados originais; Markdown associado fica no mesmo envelope.
Não altera a fonte no Drive. O site exibe o envelope na ficha complementar.
IDs e nomes internos precisam confirmar a identidade do catálogo. Registros sem ID
canônico são associados exclusivamente por nome inequívoco; nenhum ID é inventado.
Versões diferentes da mesma ficha são relatadas para conciliação, sem sobrescrita.
Repetir a execução reconhece os conteúdos já integrados.

Os dados mantêm edição e procedência declaradas na origem, sem homologação de
mecânicas ou de direitos de publicação. A importação é local; publicar é outra operação.
