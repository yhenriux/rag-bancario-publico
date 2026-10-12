# Método aplicado

[Início](../README.md) · [Escopo](escopo-atual.md) · [Dados](dados.md)

Este é um estudo documental exploratório, conduzido por um pesquisador com apoio de IA. O foco aplicado é a localização de evidências. A redução do alcance foi autorizada em 12/10/2026, após os rankings e 56 respostas estarem disponíveis.

## Fontes e organização

A coleção contém 27 páginas públicas de Inter e Bradesco, recuperadas em 11 e 12/10/2026. Quatro arquivos mudaram durante a recuperação; [as versões estão registradas](retomada-fontes-20261012.json). Páginas sem extração utilizável e falhas de acesso foram excluídas com justificativa.

Os textos foram divididos em trechos de até 320 tokens, com sobreposição de 48, usando o tokenizador E5. O catálogo associa títulos e expressões a produtos e públicos por regras determinísticas. A mesma âncora pode aparecer em trechos sobrepostos e conta uma única vez por pergunta.

## Perguntas e referências

São 20 perguntas do conjunto piloto e 10 de famílias novas no conjunto final. Os nomes preservam a divisão original; a comparação documental está completa nos dois. As classes são direta, condição, exceção, ambiguidade e insuficiência.

Codex participa da preparação de perguntas, dossiês, metadados e referências. Os campos de produto e público incluem informações explícitas, normalizações e inferências. Consulte o [registro por pergunta](results-20261012/query-attribute-audit.jsonl). Esses campos não foram extraídos por um classificador validado em perguntas reais.

As 43 âncoras são segmentos curtos registrados por posição e hash. O código confere suas posições e vínculos com os trechos. Esse controle verifica integridade, com alcance distinto de uma revisão independente do sentido das referências.

## Busca

A, B, C e Bp usam multilingual-e5-large-instruct em CPU, precisão FP32, revisão `274baa43b0e13e37fafa6428dbc7938e62e5c439`. L usa BM25, com k1=1,2 e b=0,75. Todas as buscas delimitam candidatos ao banco da pergunta. Os prefixos modificam a representação usada para buscar; o texto de origem permanece preservado.

A filtragem C usa os mesmos vetores de B. Compara rótulos literalmente e conserva categorias gerais ou desconhecidas. Os rankings registram até dez posições. A seleção preparada para o gerador tem até cinco trechos, sujeita ao orçamento de entrada. O estudo documental compara essas posições sem precisar concluir a geração.

## Medidas e intervalos

Recall de âncoras é a parcela das referências recuperadas. Cobertura é a presença de pelo menos um conjunto de âncoras definido no dossiê. Perguntas sem referência recebem valor não aplicável. São 16 perguntas elegíveis no piloto e oito no final.

B−A e B−Bp usam condição e exceção. C−B usa perguntas com atributos preparados. Os intervalos percentis de 95% e 98,33% usam as mesmas 5.000 reamostragens de famílias por banco, semente 2026. São exploratórios e condicionados à amostra e às referências. Intervalos sem variação observada não demonstram equivalência geral.

## Geração complementar

Qwen3-8B GGUF Q4_K_M com llama.cpp b11557 produziu 56 respostas salvas. A meta anterior era 180 respostas no piloto e 60 no final. O subconjunto salvo resulta da interrupção e não sustenta comparações de adequação.

Os 36 controles de fidelidade preservaram 144 itens literais. O juiz automático acertou 17 de 20 controles na segunda calibração, abaixo do mínimo de 19. Suas notas ficam excluídas. As saídas brutas das calibrações anteriores não foram recuperadas; seus relatórios públicos permanecem como histórico.

## Limites

Amostra de conveniência pequena, referências assistidas, atributos parcialmente inferidos e preparação compartilhada introduzem dependência e risco de circularidade. Não houve avaliação humana independente, teste com leitores ou validação externa. Uma correção do vocabulário aplicada ao caso BF04 é posterior ao achado e fica separada dos resultados principais.
