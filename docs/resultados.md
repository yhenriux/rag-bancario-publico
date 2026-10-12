# Resultados da busca de evidências

[Início](../README.md) · [Método](metodo.md) · [Repita as contas](reproducao.md)

A comparação documental está concluída: 30 perguntas, cinco configurações e 150 pares. Os resultados usam referências preparadas com apoio de IA e não têm validação humana independente.

## Como ler os números

Recall é a parcela das âncoras encontrada. Cobertura é a presença de um conjunto de âncoras indicado no dossiê. As seis perguntas sem referência ficam fora dessas médias, com valor não aplicável. A configuração S não faz busca.

| Configuração | Recall piloto (16) | Cobertura piloto (16) | Recall final (8) | Cobertura final (8) |
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

## Diferenças e incerteza

| Conjunto | Diferença de recall | Perguntas elegíveis | Estimativa (p.p.) | Intervalo 95% (p.p.) | Intervalo 98,33% (p.p.) |
|---|---|---:|---:|---|---|
| pilot | B-A | 8 | -12.50 | -42.86 a 0.00 | -42.86 a 0.00 |
| pilot | B-Bp | 8 | -12.50 | -42.86 a 0.00 | -42.86 a 0.00 |
| pilot | C-B | 16 | 6.25 | 0.00 a 21.43 | 0.00 a 25.00 |
| final | B-A | 4 | 0.00 | 0.00 a 0.00 | 0.00 a 0.00 |
| final | B-Bp | 4 | 0.00 | 0.00 a 0.00 | 0.00 a 0.00 |
| final | C-B | 8 | -12.50 | -37.50 a 0.00 | -37.50 a 0.00 |

P.p. significa pontos percentuais. B−A e B−Bp usam condição e exceção; C−B usa perguntas com atributos preparados. Os intervalos percentis vêm das mesmas 5.000 reamostragens de famílias por banco, com semente 2026. A magnitude de dez pontos também é informada nos relatórios JSON.

Todos os contrastes são exploratórios. O intervalo 0 a 0 no conjunto final decorre de diferenças nulas nas quatro perguntas elegíveis; não demonstra equivalência geral. A divisão de famílias preserva o desenho, mas os rankings dos dois conjuntos já estavam disponíveis antes da mudança de escopo.

## Geração complementar

56 respostas foram salvas, sem falhas de execução, limite de saída, repetição degenerada ou citações fora da entrada nos diagnósticos publicados. O subconjunto resulta da interrupção e não é balanceado. Não há medida validada de sua correção. [Resumo técnico](results-20261012/partial-generation.json).

## Arquivos para conferir

- [Resumo piloto](results-20261012/pilot/summary.json) e [resumo final](results-20261012/final/summary.json).
- [Rankings piloto](results-20261012/pilot/retrieval.jsonl) e [rankings finais](results-20261012/final/retrieval.jsonl).
- [Auditoria das referências](results-20261012/reference-audit.jsonl).
- [Origem dos atributos das perguntas](results-20261012/query-attribute-audit.jsonl).

Amostra pequena, referências curtas e preparação assistida limitam a generalização. Uma comparação com perguntas reais e referências independentes exige outra etapa de pesquisa.
