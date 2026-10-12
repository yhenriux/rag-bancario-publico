# Método aplicado nesta execução

> **Documento histórico.** Preserve este registro para acompanhar o planejamento e as decisões da época. A entrega atual está no [método aplicado](metodo.md), nos [resultados](resultados.md) e no [escopo atual](escopo-atual.md).


Este adendo define uma exploração assistida por IA, conduzida por um pesquisador individual. O protocolo original continua preservado em `protocolo.md`. As conclusões desta execução usam o método aqui descrito.

## Escopo e fontes

A coleção selecionada reúne 27 páginas públicas de Inter e Bradesco. O cadastro registra 13 URLs na ampliação, 11 downloads e 10 extrações aproveitáveis. Duas falhas de coleta e uma extração vazia são excluídas, com justificativas. Originais, hashes e cabeçalhos ficam no pacote privado. A liberação operacional limitada do projeto não corresponde a autorização dos bancos nem a licença para republicar textos.

Caixa e Banco do Brasil passam por duas rodadas limitadas de verificação. A Caixa apresenta redirecionamentos circulares. No BB, a página de políticas contém material de privacidade em scripts; a trilha comparável de termos e extração não foi concluída no limite do ciclo. O escopo desta execução fica fechado em dois bancos. Não se afirma que o BB proíbe pesquisa ou coleta.

O pesquisador trabalha no Inter. A investigação usa apenas documentos públicos, sem posicionamento institucional.

## Preparação e amostra

A extração assistida conserva os originais. Em páginas Bradesco com `main` vazio, o corpo é escolhido antes de um `article` parcial. O contêiner `section.mainContent`, quando disponível, conserva conteúdo e notas e reduz menus. Não houve revisão visual humana, OCR ou revisão independente.

O E5 segmenta textos em 320 tokens, com sobreposição de 48. A coleção tem 58 trechos. Metadados seguem regras determinísticas ligadas ao título e a posições no texto. Produto e público desconhecidos permanecem explícitos. Condições e exceções são candidatos documentais; não representam uma interpretação humana validada.

A amostra de conveniência contém **20 perguntas no piloto** e **10 na etapa final**. Cada banco contribui com duas perguntas por classe no piloto e uma por classe na etapa final. As cinco classes são: direta, condição, exceção, ambiguidade e insuficiência. A redução em relação à meta de 60 é registrada antes da geração; não se multiplicam paráfrases para completar a meta. Isso limita a precisão e a generalização.

As famílias do piloto ficam fora da etapa final. Cada família recebe no máximo três perguntas no piloto e uma na etapa final. A regra técnica de saques em caixa eletrônico do Inter é excluída. Benefícios de cartões adicionais e anuidade do Aeternum são regras distintas no mesmo documento; a dependência documental residual permanece uma limitação.

Perguntas, dossiês e âncoras são preparados por Codex antes das respostas. As referências para insuficiência são verificadas por busca lexical na coleção inteira e pela recuperação semântica congelada. Ausência na coleção não significa inexistência no banco. A recuperação das âncoras é um indicador documental restrito; não prova compreensão semântica de todas as condições.

## Modelos e execução

O gerador é `Qwen/Qwen3-8B-GGUF`, revisão `7c41481f57cb95916b40956ab2f0b139b296d974`, arquivo `Qwen3-8B-Q4_K_M.gguf`, SHA-256 `d98cdcbd03e17ce47681435b5150e34c1417f50b5c0019dd560e4882c5745785`. O backend é llama.cpp b11557, commit `5c8854fd8`, CPU, oito threads, uma sessão e contexto de 8.192 tokens. O lote interno é fixado em 512 tokens e o micro-lote em 128; as duas tentativas iniciais são preservadas e excluídas, com reinício integral do piloto e repetição dos 36 controles técnicos após cada ajuste. A reorganização interna dos pesos é desativada para evitar a pressão de memória observada. A quantização Q4_K_M é uma mudança em relação ao executor original em Transformers e precisa constar no artigo.

O recuperador é E5 multilingual large instruct, revisão `274baa43b0e13e37fafa6428dbc7938e62e5c439`, CPU FP32. As três representações dos índices são A, B e Bp. C filtra o índice B por produto/público; desconhecido ou geral passa. L usa BM25 e S não recebe documentos. Prefixos servem à recuperação. O gerador recebe o texto original com IDs, título, URL e posição, sem os prefixos experimentais.

Todas as seis configurações usam as mesmas instruções, modelo e precisão. O orçamento de entrada é de 4.096 tokens e o de saída é de 512. Se necessário, a evidência de menor posição é removida, com registro. A geração principal usa temperatura zero e `repeat_penalty=1`. Não é aplicado ajuste anti-repetição, pois os 36 controles não apresentam repetição degenerada ou perda de itens exigidos. A documentação oficial do backend confirma os parâmetros e o retorno de IDs dos tokens; o teste do processador Transformers não é tratado como prova sobre llama.cpp.

Na estabilidade, A/B/C usam sementes 43 e 44, temperatura 0,7, top_p 0,8, top_k 20 e min_p zero. Com duas perguntas por estrato banco/classe, o arredondamento seleciona uma: 10 perguntas, 50% da amostra. O piloto gera **120 respostas principais + 60 de estabilidade = 180**. A etapa final gera **60 respostas principais**. O percentual real de estabilidade é informado.

O executor salva uma resposta por combinação de fase, pergunta, configuração e semente. A retomada verifica o hash da entrada, os parâmetros e a identidade do modelo. Uma falha recebe uma repetição com os mesmos parâmetros; falhas permanentes são registradas, sem nota de adequação inventada.

## Avaliação e análise

A fidelidade usa 12 controles sintéticos e três políticas de semente, totalizando 36 respostas. Verifica valores, datas, percentuais, IDs, truncamento e blocos repetidos de 20 tokens ou mais. A calibração do avaliador usa 20 controles, com mínimo de 19 acertos e todos os JSONs válidos. Uma correção de instrução e outros 20 controles são permitidos. Se a segunda rodada falhar, a adequação automática deixa de ser desfecho principal. Não há terceira tentativa ou seleção de juiz pelo resultado bancário.

Nenhum resultado é apresentado como julgamento humano. Gerador e eventual juiz compartilham a família Qwen; a preparação por IA também impede afirmar independência equivalente às equipes do protocolo original.

A análise principal mede recuperação de âncoras em k=3/5/10, cobertura do conjunto de âncoras, exclusões de referências pelo filtro, evidências removidas pelo orçamento, IDs de citação inválidos, repetição, truncamento e falhas de execução. Cobertura documental não equivale à adequação de uma resposta. Se a calibração passar, a rubrica automática entra como análise secundária, com inconclusivos e limites pessimista/otimista. Se falhar, avaliações bancárias não são usadas para estimar adequação.

Diferenças pareadas B−A e B−Bp em condição/exceção e C−B em perguntas com atributos explícitos são exploratórias. Os intervalos percentis de 95% e 98,33% usam as mesmas 5.000 reamostragens de famílias, estratificadas por banco, semente 2026. O limiar confirmatório do protocolo original não é atingido. Não se declara confirmação de H1/H2/H3. Quando aplicável, informa-se se a diferença pontual alcança dez pontos percentuais.

## Registro e publicação

O método, as perguntas e os hashes são publicados em commit GitHub antes do piloto. Antes da etapa final, o resultado do piloto, a decisão sobre o avaliador e os hashes finais entram em novo commit. Este é um registro público próprio, sem DOI e sem alegar depósito OSF ou Zenodo.

Textos bancários completos e prompts com esses textos ficam no pacote privado. O GitHub recebe código, perguntas autorais, referências derivadas, URLs, posições, hashes e relatórios. A reprodução exata depende das versões das fontes; alterações de conteúdo exigem registrar uma nova coleção, sem substituir hashes silenciosamente.

Teste com leitores humanos, concordância entre humanos e avaliação independente não integram esta execução. A documentação passa por verificações automáticas de links e exemplos, que não substituem esses testes. A escolha de revista depende de política editorial compatível com o uso efetivo de IA; a Múltiplos Olhares exige conferência específica. Licença autoral e submissão editorial dependem da decisão do pesquisador.
