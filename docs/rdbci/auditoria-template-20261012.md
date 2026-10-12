# Auditoria do manuscrito em português contra o template anexado

Auditoria de 12/10/2026. Objeto: o manuscrito corrigido em português, com quinze páginas. O template anexado `Template_Atualizado-OTH-2.docx` tem o mesmo SHA-256 do modelo oficial usado anteriormente: `e16dd44b901df87876f9a7aed833bc5f2027bf176a0c97e2360616818119b72d`. O manuscrito examinado tem SHA-256 `3e2f8c4be2cd24dcd698469d9605e541f3b74b418244d121e31c3824b4fd8117`.

A adequação completa **não está demonstrada**. O arquivo está íntegro, seu conteúdo científico foi preservado e sua estrutura atende a vários requisitos, mas ainda há diferenças de formatação e itens obrigatórios ausentes. A conferência anterior não examinou suficientemente as instruções guardadas nos comentários do template.

## O que está conforme

- Word íntegro: pacote ZIP com CRC válido e XML bem formado; conversão no LibreOffice concluída.
- Papel A4; texto principal Times New Roman 12, justificado, com espaçamento simples e sem espaço adicional entre parágrafos.
- Recuo de primeira linha de 1,25 cm e margens correspondentes ao item principal das diretrizes públicas da revista. Esses valores não coincidem integralmente com a configuração interna do arquivo de template, conforme detalhado adiante.
- Títulos em português e inglês. A fonte Teko 16 coincide com a fonte efetivamente gravada nos títulos do modelo.
- Resumos estruturados com os cinco rótulos, 197 palavras em português e 186 em inglês; ambos ficam entre 100 e 250 palavras.
- Cinco palavras-chave em cada idioma. A confirmação terminológica do ERIC pertence à preparação anterior; esta auditoria confere quantidade, presença e apresentação, sem repetir uma validação lexical completa.
- Introdução, discussão teórica, método, resultados, discussão, limites e conclusão presentes. O fechamento usa Conclusão.
- Cabeçalhos principais Calibri Light 14 em negrito e vermelho; subseções Calibri Light 12 em itálico e vermelho.
- Cinco tabelas e quadros nativos e editáveis, com título acima, fonte abaixo e cabeçalho repetido nas continuações. Todas as células conservam os valores da cópia íntegra anterior.
- Vinte e uma referências, com nomes próprios restaurados e um hiperlink em cada referência. A existência do vínculo no Word não certifica que os 21 destinos estejam disponíveis na rede.
- Texto visível e campos centrais de propriedades sem o nome, ORCID ou endereço pessoal do repositório do pesquisador. Esse resultado não equivale a uma limpeza completa dos resíduos internos do template.
- Apêndices separados do texto principal; ausência de agradecimentos no manuscrito.

## Pendências comprovadas

| Prioridade | Item | Evidência | Ação necessária |
|---|---|---|---|
| Alta | Autodescrição dos objetos | O template tem instruções nos comentários 23 a 26 e o texto da revista pede Descrição após Fonte. Nenhum dos cinco objetos do manuscrito tem esse parágrafo. | Acrescentar uma descrição acessível a cada tabela e quadro, imediatamente após a fonte. |
| Alta | Comentários residuais | O pacote conserva 21 comentários do modelo em `word/comments.xml`, além de partes de pessoas e comentários auxiliares. Não há âncoras de comentário no novo texto. | Remover comentários e metadados auxiliares que não pertençam ao manuscrito final. Não tratar esses nomes residuais como autores do estudo. |
| Alta | Referências de eventos | Entradas de anais não seguem uniformemente a estrutura de nome do evento, edição, ano, local e publicação prescrita no template. Alguns dados requerem conferência na fonte. | Padronizar cada tipo documental e completar somente metadados verificáveis. A cidade do Journal of Documentation permanece em [S. l.]; o registro público ISSN consultado não fornece a cidade. |
| Alta para a conclusão do envio | Depósito dos complementos | O template exige depósito em repositório de dados e indicação do link no CRediT. O manuscrito informa que não houve depósito com DOI. | Realizar o depósito adequado e informar a localização, sem confundir presença no GitHub com conclusão dessa exigência. DOI não é, sozinho, a exigência literal do template. |
| Média | Seção da revista | A orientação Inclua a seção aqui e o comentário 2 não têm correspondente preenchido no manuscrito. | Inserir Artigo de Pesquisa na posição destinada à seção. |
| Média | Cores dos resumos e rótulos | RESUMO, ABSTRACT, PALAVRAS-CHAVE e KEYWORDS estão pretos. Os cinco rótulos internos também estão pretos. O modelo e o comentário 4 prescrevem vermelho. | Aplicar a cor correspondente aos rótulos, preservando o preto no restante do texto dos resumos. |
| Média | Legendas e fontes | As legendas estão centralizadas e sem o destaque específico da expressão Tabela ou Quadro e do número. O modelo as apresenta à esquerda, com esse trecho destacado; o rótulo Fonte também tem cor diferente. | Reproduzir alinhamento e destaque do modelo, mantendo fonte, tamanho e conteúdo científico. |
| Média | Termos estrangeiros | hash, hashes, ranking, rankings, prompts e downloads permanecem sem itálico em trechos do corpo do artigo. recall e bootstrap já estão em itálico. | Uniformizar o itálico ou empregar tradução adequada, preservando os nomes próprios de modelos e ferramentas. |
| Média | Primeira apresentação das siglas | RAG aparece nos resumos sem expansão; RAGAS e ARES são apresentados sem o nome completo. MRR tem explicação da medida, mas a apresentação formal da sigla pode ser normalizada. | Explicar as siglas no primeiro uso pertinente e distinguir siglas de nomes de produtos ou modelos. |
| Baixa | Fidelidade gráfica das tabelas | O modelo usa rosa claro nos corpos e linhas vermelhas; o manuscrito alterna rosa e branco e usa grade cinza. | Replicar o tratamento do modelo, mantendo tabelas editáveis e legíveis. |
| Baixa / interpretação editorial | Conclusão | A seção relata resultados, contribuição e limites, mas não retoma explicitamente todos os elementos de objetivo e método citados na orientação do template. | Tornar essa retomada explícita e concisa. Não criar automaticamente cinco subtítulos: a instrução admite interpretação. |

## Divergências do próprio material editorial

- **Margem direita:** o arquivo tem 3 cm; o item principal das diretrizes públicas pede 2,5 cm. O manuscrito utiliza 2,5 cm. Trata-se de diferença entre duas fontes editoriais, e não de falha inequívoca contra as diretrizes públicas.
- **Recuo:** parágrafos do modelo usam aproximadamente 1,48 cm. O item principal das diretrizes pede 1,25 cm e outro item da mesma página menciona 1,1 cm. O manuscrito usa 1,25 cm.
- **Fonte do título:** a instrução escrita indica Agency FB; os próprios títulos do Word estão em Teko 16. O manuscrito segue a fonte efetivamente gravada.
- **Nomes nas referências:** a instrução destacada exige nomes por extenso e o lembrete final menciona abreviação. A opção por nomes por extenso segue a orientação explícita associada ao princípio DEIA.
- **Cabeçalho e rodapé:** a posição de campos do template não coincide integralmente com a indicação de numeração superior direita das diretrizes. O manuscrito segue essa indicação e remove exemplos de volume, data e elocation não atribuídos. Essas diferenças devem ser reconhecidas antes de exigir cópia literal do arquivo.

## Alcance da auditoria

Foram examinados o texto e os comentários do template, estilos, propriedades de seção, tabelas, relações de hiperlink, pacote interno do Word e renderização. A integridade e a preservação das células foram verificadas. O template foi convertido e inspecionado nas doze páginas; a renderização mais recente do manuscrito de quinze páginas foi usada como referência visual.

Esta etapa não alterou o manuscrito, não reexecutou o experimento, não refez toda a verificação bibliográfica e não certificou compreensão por leitores. A declaração de conformidade completa fica pendente das correções apontadas. Assinaturas, revisão autoral, formulário unificado e outras condições da submissão permanecem fora do resultado de conformidade do Word.

## Fontes editoriais

- Template anexado pelo autor, conferido contra a cópia oficial anterior por SHA-256; instruções principais e comentários internos.
- Diretrizes públicas consultadas em 12/10/2026: https://periodicos.sbu.unicamp.br/ojs/index.php/rdbci/about/submissions.
- Registro público ISSN consultado: https://portal.issn.org/resource/ISSN/0022-0418. O registro confirma o periódico e o país, mas não fornece a cidade na consulta pública realizada.
