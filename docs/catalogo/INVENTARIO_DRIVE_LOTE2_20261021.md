# Inventário e integração do Drive — lote 2 (21/10/2026)

## Lote integrado neste PR

- **9 fichas SRD 5.2.1 adicionais** trazidas da pasta `Fichas/Completas`: `AT-003` Aboleth; `AT-024` Pegasus; `AT-025` Unicorn; `AT-026` Deva; `AT-027` Guardian Naga; `AT-028` Sphinx of Lore; `AT-030` Planetar; `AT-031` Sphinx of Valor; `AT-032` Solar. Com as 3 do lote anterior, o manifesto passa a apontar para **12 fichas complementares**. Os arquivos originais são mantidos íntegros em `data/drive-fichas-srd-20261021/`. Não sobrescrever `fichas-607.json`, ND, raridade, CA, PV ou habilidades do catálogo-base; a condição de homologação administrativa segue a do documento original.
- **1 imagem autoral de `Imagens/Novas`**: `AT-023` Giant Owl (`AT-023-giant-owl.png`), com origem `candidata-nao-homologada`. Disponível **apenas no painel de detalhes**, não na grade, sem substituir ilustração existente. Total cumulativo do manifesto: **15 imagens** (14 WebP do lote anterior e 1 PNG) e **12 fichas**.
- O código aceita esquemas de identidade de ficha `identificacao.id_catalogo`, `identificacao.ID_CATALOGO` ou `ID_CATALOGO` no nível superior, sempre exigindo identidade idêntica ao ID do catálogo para apresentar o JSON.

## Inventário verificável de Imagens/Novas

Consultado o Google Drive com paginação de metadados, **6 páginas / 567 arquivos**. Contagem sem carregar ou promover as imagens:

| Classificação por nome de arquivo | Arquivos | Observação |
| --- | ---: | --- |
| Arquivos com ID canônico reconhecido da megalista | 180 | Correspondem a **67 IDs distintos**, com diversas alternativas/versões para a mesma criatura |
| Arquivos com prefixo de identificação não reconhecido como ID canônico | 157 | Não atribuir um ID de criatura automaticamente |
| Arquivos sem identificador canônico parseável | 230 | Fotos/ilustrações genéricas, nomes de cenas ou formatos diferentes |
| **Total** | **567** | Preserva todos no Drive; não apaga ou move nenhum |

Os rótulos dos arquivos representam condições **não mutuamente exclusivas**: **306** contêm `candidata`; **14** contêm `rejeitada`; **42** contêm `revisar` ou `em-revisao`. Nem todo arquivo com ID canônico reconhecido é uma imagem adequada à criatura. As imagens explicitamente rejeitadas **não são promovidas**. A triagem deve escolher a alternativa correta quando há três ou mais arquivos para o mesmo ID.

## Fichas/Completas

O conector apresentou **a primeira lista de 100 arquivos**, dos quais 97 tinham extensão `.json` e 3 eram textos Markdown. Desses, 12 nomes começam com `AT-`, incluindo as 3 fichas SRD já incorporadas no primeiro lote. **Não é correto afirmar que toda a pasta foi inventariada**: essa visualização tem um limite de 100 resultados; podem existir mais arquivos.

Os nove JSONs adicionados têm `AT-` reconhecido e identificações compatíveis com a megalista. O status `FICHA_MECANICA_DA_FONTE_COMPLETA_NAO_HOMOLOGADA` permanece, onde presente. Não foram republicadas fichas de fontes editoriais não SRD (TF/KP/EXT) sem avaliação de direitos.

## Restrições importantes

- A autorização do usuário, criador das imagens, para publicá-las no Catálogo SRD permanece registrada no manifesto. Não é homologação automática de adequação visual, de atribuição editorial ou de mecânica.
- Algumas transferências de PNG de cerca de 3 MB falharam durante a cópia para o GitHub. Só `AT-023` entrou **com integridade validada**. Os demais PNGs permanecem no Drive para o próximo lote; não escrever referências para arquivos que não chegaram ao GitHub.
- Nenhuma mão, ordem de monte, token do Google Drive, ID privado de arquivo ou estado oficial de partida foi inserido no catálogo público.
- O Catálogo SRD continua como repositório externo de dados; isso **não altera** a configuração de pin do motor Ascend Card Game automaticamente.

## Próxima execução

1. Validar visualmente uma arte de cada criatura com ID canônico, rejeitando variantes marcadas `rejeitada` e duplicatas para o mesmo ID.
2. Converter PNGs aprovados de grande porte para WebP com compressão adequada antes de subir, conservando original e proveniência no Drive.
3. Conciliar os arquivos de `Fichas/Completas` além dos 100 primeiros. Para fontes SRD, só adicionar a ficha original ligada ao ID; para editoras terceiras, publicar apenas metadados e referências permitidos, não o texto integral sem autorização.
4. Criar/reexecutar testes de curadoria, imagens, esquema de ficha e alinhamento com os 1.320 registros antes de novos merges.

**Nenhuma partida oficial foi iniciada ou modificada.**
