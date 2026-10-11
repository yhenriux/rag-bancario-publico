# Como avaliar as respostas

[Voltar ao início](../README.md) · [Consultar palavras técnicas](glossario.md)

A equipe avalia se cada resposta preserva o que a pergunta exige. Os modelos produzem respostas; as pessoas fazem os julgamentos de adequação.

## Separe os papéis

| Pessoas | Recebem | Produzem | Trabalham sem acesso a |
|---|---|---|---|
| M1 e M2 | Fontes e trechos | Descrições dos documentos | Respostas e julgamentos de J |
| R1 e R2 | Perguntas e fontes originais | Referências e famílias de regras | Descrições de M e respostas dos sistemas |
| J1 e J2 | Perguntas, respostas sem identificação do sistema e referências | Avaliações individuais | Configuração e semente |
| Coordenação | Registros completos | Arquivos, decisões e relatório | Controla o acesso e guarda a chave de identificação |

O protocolo exige seis pessoas distintas nos papéis M/R/J.

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

## Preserve as avaliações individuais

J1 e J2 avaliam de forma independente. A coordenação conserva os formulários originais, a decisão conjunta e sua justificativa.

Faça o mesmo com M1/M2 e R1/R2. Compare as pessoas antes da decisão conjunta.

O comando `study.py agreement` calcula acordo exato e kappa por atributo. Para campos que representam conjuntos, também calcula Jaccard. [Veja o comando no guia](execucao.md#11-compare-as-avaliações-e-calcule-os-resultados).

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

A interpretação automática é exploratória. Uma interpretação confirmatória exige dimensionamento por simulação e pré-registro. Esses requisitos estão no [protocolo](protocolo.md).

## Verifique a fidelidade técnica

Se o piloto exigir um ajuste contra repetição, J1/J2 também conferem os doze casos técnicos. O programa produz 72 saídas e dois formulários.

Verifique valores, unidades, datas e identificadores antes e depois do ajuste. Qualquer item antes preservado que se perde impede aceitar a mudança.

Essas conferências são adicionais às avaliações do piloto.

## Transforme o diagnóstico em uma ação

Para cada ganho ou perda, reúna pergunta, fontes, adequação, atributos e problema encontrado.

A ação pode ser corrigir a descrição, conservar o alcance geral, reunir regra e exceção ou testar uma instrução mais clara. A mudança precisa de uma nova avaliação.
