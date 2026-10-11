# Entenda o projeto

[Voltar ao início](../README.md)

## O problema

Uma resposta pode citar a página certa e perder a condição que define quando uma regra vale. Um cartão pode oferecer isenção somente acima de um gasto mínimo. Queremos estudar como a organização dos documentos ajuda a preservar essas condições e quando um filtro perde uma fonte necessária.

## Como funciona

O sistema consulta documentos públicos, encontra passagens e produz uma resposta. Cada passagem conserva sua origem. Comparamos seis formas de busca e resposta, descritas no [início do projeto](../README.md#o-que-o-estudo-compara).

Descrições dos documentos, chamadas metadados, funcionam como etiquetas. Elas podem informar produto, público e tipo de documento. Uma etiqueta errada pode prejudicar a busca. O alcance geral de uma regra precisa de suporte na fonte.

## Quem trabalha

Yago é o único pesquisador. Codex auxilia no trabalho operacional: localizar fontes, conferir condições, coletar, catalogar, preparar propostas e analisar registros. O plano usa lotes, com meta de coleta e catálogo em uma jornada. Não exige fichas manuais por documento nem disponibilidade semanal.

O código já encadeia coleta aprovada, extração e catálogo. Descrições semânticas, perguntas e avaliações assistidas ainda precisam ser preparadas sobre a coleção real. Os modelos também precisam de ambiente validado.

## Como conferir respostas

Uma referência reúne a regra, suas condições, as passagens e o comportamento esperado. Perguntas e referências são fixadas antes das respostas.

- **Suficiência:** há informação bastante para responder?
- **Aplicabilidade:** essa informação vale para a situação descrita?

Regras automáticas ajudam a localizar perdas de valores e fontes. Julgamento por IA, quando utilizado, fica identificado como automático. Validação humana independente é uma etapa adicional. Não há avaliações humanas fictícias.

## O piloto

O piloto é um teste inicial com meta de 60 perguntas, em três bancos e cinco classes: direta, condição, exceção, ambiguidade e falta de informação. Produz 360 saídas principais e 90 de estabilidade.

Essas saídas não exigem 450 marcações humanas na jornada rápida. Uma execução menor serve como teste técnico e registra seu tamanho real. O estudo assistido permanece exploratório.

## O que fica registrado

Fontes, termos, endereços, datas, hashes, passagens, descrições, perguntas, famílias, versões dos modelos, respostas, falhas e origem de cada anotação. Uma família reúne perguntas apoiadas na mesma regra; muitas paráfrases não criam famílias independentes.

[Veja o plano de execução](plano-execucao.md) e a [situação das entregas](roadmap.md).
