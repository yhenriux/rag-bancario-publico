# Resultados da busca de evidências

[Início](../README.md) · [Método](metodo.md) · [Repita as contas](reproducao.md)

A comparação documental está concluída: 30 perguntas, cinco configurações e 150 pares. Os resultados usam referências preparadas com apoio de IA e não têm validação humana independente.

## Como ler os números

Recall é a parcela das âncoras encontrada. Cobertura é a presença de um conjunto de âncoras indicado no dossiê. As seis perguntas sem referência ficam fora dessas médias, com valor não aplicável. A configuração S não faz busca.

| Configuração | Recall piloto (16) | Cobertura piloto (16) | Recall segundo (8) | Cobertura segundo (8) |
|---|---:|---:|---:|---:|
| A | 90,625% | 87,500% | 87,500% | 87,500% |
| B | 90,625% | 87,500% | 100,000% | 100,000% |
| C | 96,875% | 93,750% | 87,500% | 87,500% |
| Bp | 96,875% | 93,750% | 100,000% | 100,000% |
| L | 93,750% | 93,750% | 100,000% | 100,000% |

As medidas usam as primeiras cinco posições. Há também resultados para três e dez posições nos arquivos públicos. O teto de 100% descreve as âncoras desta amostra; não assegura suficiência da informação ou correção de uma resposta.

## Quando o filtro ajuda: pergunta B05

“Perdi meu cartão de débito Bradesco. A segunda via está incluída nos serviços essenciais gratuitos?”

B não encontra a âncora nas primeiras cinco posições; C encontra. A fonte registra perda como exceção à gratuidade. O filtro usa produto `conta` e público `pf`, ambos preparados por inferência assistida. O benefício é condicionado a essa classificação e não demonstra que o sistema identificaria corretamente os atributos de uma pergunta real.

[Fonte sobre contas e serviços essenciais](https://banco.bradesco/cidadania-financeira/educacao-financeira/produtos-e-servicos-financeiros/contas-bancarias/index.shtm).

## Quando o filtro prejudica: pergunta BF04

“Tenho investimentos no Bradesco. Minha anuidade do cartão está isenta?”

A, B, Bp e L encontram as duas âncoras da regra do Aeternum. C exclui os trechos porque a pergunta usa `cartao` e o catálogo usa `aeternum`. A comparação literal não registra a relação de pertencimento entre as categorias. A pergunta ainda exige esclarecer o cartão e as condições.

[Fonte do Visa Aeternum](https://banco.bradesco/html/principal/cartoes/aeternum/).

Uma correção posterior acrescenta a relação `aeternum → cartao` e reaplica a seleção ao ranking congelado. As duas âncoras retornam às primeiras cinco posições. Essa demonstração usa o caso já observado, sem novas chamadas de modelo e sem alterar os resultados principais. [Registro da intervenção](results-20261012/intervention.json).

## Casos discordantes e sensibilidade

Em recall@5 e cobertura@5, C supera B somente em B05 (1/16 perguntas elegíveis do piloto) e perde somente em BF04 (1/8 do segundo conjunto). No piloto, B perde para A e Bp em B05, entre oito perguntas de condição e exceção; no segundo conjunto, as quatro perguntas dessas classes empatam nos dois contrastes.

A revisão acrescenta [matriz 30 × 5](diagnostico-20261012/matrix.md), recall@1/3/5/10, MRR@10 e posições por âncora. B05 está na posição 6 de B e 4 de C. Retirar os dois campos inferidos torna o caso equivalente a B, eliminando o ganho no corte de cinco posições. Em BF04, cartão é expresso e a falha permanece. Esta sensibilidade é posterior, limitada aos dois casos e não valida um extrator independente.

O catálogo oferece 18 candidatos do Inter e 44 do Bradesco antes do filtro adicional. BM25 é competitivo: no segundo conjunto, B e L recuperam todas as âncoras em três posições. L apresenta recall@1 de 87,5% e MRR@10 de 0,917, contra 62,5% e 0,792 em B. No piloto, L tem recall@3 e @5 de 93,75%, acima de A e B em 90,625%; C e Bp alcançam 96,875% em cinco posições.

B05 e BF04 não esgotam as mudanças de posição: em recall@1, I08 também distingue C e B no piloto. A ordem das listas publicadas muda em 17/20 e 9/10 perguntas. [Cálculos completos](diagnostico-20261012/diagnostics.json) e [decisões críticas](resposta-parecer-20261012.md).

## Intervalos históricos, fora da interpretação principal

| Conjunto | Diferença de recall | Perguntas elegíveis | Estimativa (p.p.) | Intervalo 95% (p.p.) | Intervalo 98,33% (p.p.) |
|---|---|---:|---:|---|---|
| pilot | B-A | 8 | -12.50 | -42.86 a 0.00 | -42.86 a 0.00 |
| pilot | B-Bp | 8 | -12.50 | -42.86 a 0.00 | -42.86 a 0.00 |
| pilot | C-B | 16 | 6.25 | 0.00 a 21.43 | 0.00 a 25.00 |
| final | B-A | 4 | 0.00 | 0.00 a 0.00 | 0.00 a 0.00 |
| final | B-Bp | 4 | 0.00 | 0.00 a 0.00 | 0.00 a 0.00 |
| final | C-B | 8 | -12.50 | -37.50 a 0.00 | -37.50 a 0.00 |

P.p. significa pontos percentuais. B−A e B−Bp usam condição e exceção; C−B usa perguntas com atributos preparados. Os intervalos percentis vêm das mesmas 5.000 reamostragens de famílias por banco, com semente 2026. O critério histórico de dez pontos continua nos relatórios JSON. Em oito perguntas, uma mudança binária já vale 12,5 pontos; esse limiar não define relevância robusta nesta amostra. Os intervalos permanecem como histórico reproduzível, com a interpretação principal baseada nos casos.

Todos os contrastes são exploratórios. O intervalo 0 a 0 no conjunto final decorre de diferenças nulas nas quatro perguntas elegíveis; não demonstra equivalência geral. A divisão de famílias preserva o desenho, mas os rankings dos dois conjuntos já estavam disponíveis antes da mudança de escopo.

## Geração complementar

56 respostas foram salvas, sem falhas de execução, limite de saída, repetição degenerada ou citações fora da entrada nos diagnósticos publicados. O subconjunto resulta da interrupção e não é balanceado. Não há medida validada de sua correção. [Resumo técnico](results-20261012/partial-generation.json).

## Arquivos para conferir

- [Resumo piloto](results-20261012/pilot/summary.json) e [resumo final](results-20261012/final/summary.json).
- [Rankings piloto](results-20261012/pilot/retrieval.jsonl) e [rankings finais](results-20261012/final/retrieval.jsonl).
- [Auditoria das referências](results-20261012/reference-audit.jsonl).
- [Origem dos atributos das perguntas](results-20261012/query-attribute-audit.jsonl).

Amostra pequena, referências curtas e preparação assistida limitam a generalização. Uma comparação com perguntas reais e referências independentes exige outra etapa de pesquisa.

## Resultados separados por banco

As doze perguntas elegíveis do Inter, oito no piloto e quatro no segundo conjunto, têm recall@5 de 100% nas cinco configurações. Todas as diferenças nesse corte estão nas doze elegíveis do Bradesco. O Inter mantém diferenças em acesso inicial: no piloto, recall@1 de C é 100%, de A/B/Bp é 87,5% e de L é 75%; no segundo conjunto, A/Bp/L têm 100% e B/C, 75%.

Os vinte estratos por banco, conjunto e configuração estão em `summary_by_bank` no [relatório diagnóstico](diagnostico-20261012/diagnostics.json). A [matriz](diagnostico-20261012/matrix.md) informa banco, classe e número de âncoras. A preparação compartilhada limita a independência; retirar campos inferidos verifica uma consequência determinística da política de seleção.
