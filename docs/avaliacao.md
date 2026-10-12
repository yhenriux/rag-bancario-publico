# O que foi avaliado

[Início](../README.md) · [Resultados](resultados.md) · [Método](metodo.md)

A entrega mede a recuperação das referências preparadas. A correção semântica das respostas ainda não tem uma medida validada.

## Medidas documentais

- **Recall:** parcela das âncoras encontrada nas primeiras posições.
- **Cobertura:** presença de um conjunto de âncoras especificado no dossiê.
- **Perda pelo filtro:** referência que deixa de existir em todos os trechos candidatos restantes.
- **Contexto efetivo:** referências presentes nos trechos selecionados para a entrada do gerador.

As âncoras são curtas e assistidas. Cobertura de âncoras não comprova que todas as condições relevantes foram identificadas.

## Controles técnicos

Os controles de fidelidade verificam itens literais conhecidos. Os diagnósticos das 56 respostas verificam falhas, limite de saída, repetição e identificadores de fonte. Um identificador válido informa que a fonte estava disponível; verificar se a afirmação é sustentada exige análise de conteúdo.

## Por que não publicamos notas de correção

O critério do juiz automático era acertar pelo menos 19 de 20 controles. A segunda rodada acertou 17. A [decisão registrada](evaluation-decision-20261011.json) desativa a adequação automática. Nenhuma dessas notas entra nos achados bancários.

Não houve avaliação por pessoas independentes, concordância entre anotadores ou teste de compreensão com leitores. Os comandos `study.py blind` e `study.py agreement` continuam disponíveis para uma possível ampliação com plano próprio.

## Incerteza

Os contrastes usam reamostragem de famílias por banco. Os intervalos publicados são exploratórios. A amostra pequena e a preparação assistida limitam sua interpretação.

## Posição das referências

A revisão diagnóstica calcula recall@1/3/5/10 e MRR@10, a média do inverso da posição da primeira âncora até dez trechos. Ausência nesse limite vale zero; pergunta sem referências recebe NA. MRR mede acesso inicial, não cobertura ou suficiência semântica. [Matriz](diagnostico-20261012/matrix.md).
