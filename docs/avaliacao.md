# Como conferir as respostas

[Voltar ao início](../README.md) · [Método ativo](protocolo-individual.md)

A jornada rápida usa verificações automáticas e assistência de Codex. Avaliação humana independente fica como etapa adicional. A integração de julgamento por modelo ainda está pendente.

## Registre quem ou o que avaliou

Cada resultado informa origem, ferramenta ou pessoa, versão disponível, instrução, data, referência e justificativa. Regras determinísticas, julgamento por IA e revisão humana são registrados separadamente. Um escore automático não recebe o rótulo humano.

A referência fica congelada antes das saídas. Registrar quando a mesma pessoa ou ferramenta participa da preparação e do julgamento. Ocultar o nome da configuração ajuda, mas não estabelece independência.

## Critérios de conteúdo

A adequação recebe `1` quando todos os requisitos estão atendidos e não há afirmação incompatível; caso contrário, recebe `0`. Casos sem evidência ou sem decisão permanecem pendentes, com seu motivo.

| Pergunta | O que conferir |
|---|---|
| Direta, condição ou exceção | Regra, condições, valores e exceções necessários |
| Ambiguidade | Pedido de esclarecimento previsto |
| Insuficiência | Reconhecimento da falta de evidência, sem preencher a lacuna |

Aplicabilidade pergunta se a informação vale para a situação da pessoa. Suficiência pergunta se o contexto contém informação bastante. Produto e público ficam separados de elegibilidade, canal e período, porque somente os dois primeiros alimentam o filtro.

## O que pode ser automático

- Encontrar valores, datas e identificadores presentes nas passagens e nas respostas.
- Registrar fontes recuperadas e fontes retiradas pelo filtro ou limite da entrada.
- Calcular cobertura e recall após fixar referências e mapa de evidências.
- Comparar escores completos e produzir intervalos por família.

Uma correspondência textual não prova adequação. A avaliação por IA exige justificativa e conserva suas limitações. O catálogo atual localiza passagens; ele não julga respostas.

## Comparações e intervalos

H1 compara B com A; H2, C com B; H3, B com Bp. H1 e H3 usam condição e exceção. H2 usa perguntas com produto ou público explícito e codificável. Comparações exigem os dois escores da mesma pergunta e regras prévias para falhas e ausências.

O código calcula 5.000 reamostragens de famílias dentro de cada banco. Os intervalos de 95% usam percentis 0,025 e 0,975; os de 98,33%, 0,008333 e 0,991667, da mesma distribuição, com interpolação linear. Registrar também se a diferença estimada atinge dez pontos percentuais.

Com referências ou escores assistidos, os resultados são exploratórios e condicionados a essas anotações. Intervalos não quantificam todos os erros do avaliador automático. Concordância entre ferramentas não equivale a validação humana.

## Fidelidade e publicação

Conferir valores, unidades, datas e IDs antes e depois de qualquer ajuste de repetição. Uma perda de um item antes preservado impede aceitar o ajuste. O teste automático correspondente permanece pendente de integração.

Cada diagnóstico reúne pergunta, resposta, referência, passagens e origem do julgamento. Mudanças na coleção ou no procedimento recebem nova versão. A publicação identifica claramente o que foi executado, o que foi sugerido e o que continua pendente.
