# Como avaliar as respostas

[Voltar ao início](../README.md) · [Consultar palavras técnicas](glossario.md)

Yago avalia se cada resposta preserva o que a pergunta exige. Os modelos produzem respostas; as pessoas fazem os julgamentos de adequação.

## Separe as etapas

O [adendo individual](protocolo-individual.md) define a execução ativa. Yago prepara referências nos documentos originais, congela os requisitos antes das saídas e faz descrições e julgamentos em arquivos e momentos separados.

O formulário J1 oculta configuração e semente. Yago mantém a chave separada e evita consultá-la durante as marcações. Isso limita a identificação explícita do sistema, enquanto a familiaridade com as fontes e procedimentos limita o cegamento. Não há avaliação humana independente.

## Confira a adequação

A adequação recebe `1` quando todos os requisitos da referência são atendidos e a resposta não traz afirmação incompatível. Caso contrário, recebe `0`.

| Tipo de pergunta | O que verificar |
|---|---|
| Direta, condição ou exceção | A resposta preserva a regra e todos os requisitos necessários? |
| Ambiguidade | A resposta pede o esclarecimento previsto? |
| Insuficiência | A resposta informa a falta de evidência e evita preencher a lacuna? |

Uma resposta pode citar a fonte certa e perder uma condição. Os avaliadores verificam o conteúdo e a relação com a situação descrita.

## Registre também os atributos

Para cada atributo necessário, marque compatível, incompatível ou indeterminado.

Produto e público são os atributos usados pelo filtro. Elegibilidade, canal e período ficam em outro grupo. A separação mostra se o ganho do filtro alcança condições que ele não usa.

Um atributo que não é necessário à pergunta fica fora do seu denominador. Denominador é a quantidade de casos que entram no cálculo.

## Confira o uso das fontes

- **Completude:** quantos requisitos obrigatórios a resposta preservou.
- **Sustentação:** se cada afirmação está sustentada, parcialmente sustentada, contradita ou sem suporte.
- **Cobertura:** se a busca encontrou todas as passagens de ao menos um conjunto suficiente.
- **Recall:** qual parcela das passagens de referência a busca encontrou.

Passagens repetidas contam uma vez. Quando não há passagens de referência, recall não se aplica. A configuração S recebe avaliação de conteúdo; recuperação e sustentação por fontes fornecidas não se aplicam.

## Registre os problemas

Uma resposta pode ter mais de um problema:

- Busca insuficiente.
- Fonte necessária retirada pelo filtro.
- Uso incompleto ou incorreto da fonte.
- Informação incompatível com a situação.
- Referência inadequada.

Registre também fontes retiradas por limite de tamanho da entrada do modelo. Esse é um evento técnico separado.

## Preserve a primeira passagem e reavalie a amostra

Yago avalia todas as respostas uma vez. Depois de no mínimo 14 dias, reavalia a amostra previamente fixada de 20%, em outra ordem e sem consultar as primeiras marcações. As duas passagens ficam preservadas.

A primeira avaliação é a principal. A segunda é diagnóstico de consistência. Erros materiais comprovados recebem justificativa e análise de sensibilidade. Evitar escolher uma rodada pelo resultado favorável a uma hipótese.

O comando `study.py agreement` compara `rodada1` e `rodada2` do mesmo pesquisador. Reportar acordo e eventual kappa como intra-avaliador, com tamanho, categorias e limite de memória. Conjuntos também recebem Jaccard. [Veja o comando](execucao.md#11-compare-as-avaliações-e-calcule-os-resultados).

## Compare as configurações

| Hipótese | Diferença calculada | Perguntas que entram |
|---|---|---|
| H1 | B menos A | Condição e exceção |
| H2 | C menos B | Produto ou público explícito e codificável |
| H3 | B menos Bp | Condição e exceção |

As diferenças mantêm a mesma pergunta nos dois sistemas. A análise exige pares completos. Falhas e avaliações ausentes precisam de regra registrada previamente.

## Leia os intervalos com cuidado

O programa calcula intervalos com 5.000 reamostragens das famílias dentro de cada banco. Cada família conserva suas perguntas e pares.

Os intervalos de 95% usam os percentis 0,025 e 0,975. Os intervalos de 98,33% usam 0,008333 e 0,991667. Ambos vêm da mesma distribuição de reamostragens, com interpolação linear.

O relatório separa a direção do efeito e sua magnitude. Informa se a estimativa chega à diferença de interesse de dez pontos percentuais.

O desenho individual é exploratório. Os intervalos descrevem variação entre famílias condicionada às avaliações de Yago; não incluem variabilidade entre julgadores independentes. [Veja o adendo](protocolo-individual.md).

## Verifique a fidelidade técnica

Se o piloto exigir ajuste contra repetição, Yago confere os doze casos técnicos. O programa produz 72 saídas e um formulário individual J1.

Verifique valores, unidades, datas e identificadores antes e depois do ajuste. Qualquer item antes preservado que se perde impede aceitar a mudança.

Essas conferências são adicionais às avaliações do piloto.

## Transforme o diagnóstico em uma ação

Para cada ganho ou perda, reúna pergunta, fontes, adequação, atributos e problema encontrado.

A ação pode ser corrigir a descrição, conservar o alcance geral, reunir regra e exceção ou testar uma instrução mais clara. A mudança precisa de uma nova avaliação.
