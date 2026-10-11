# Adendo ativo: execução em lote com assistência de IA

[Voltar ao início](../README.md) · [Plano de um dia](plano-execucao.md) · [Protocolo original](protocolo.md)

**Atualizado em 11/10/2026, antes da coleta do corpus.** Yago é o único pesquisador. Codex auxilia na seleção de fontes, programação, catalogação, preparação de perguntas e análise. O plano operacional usa entregas em lote. Não exige equipe, carga semanal, centenas de marcações manuais ou espera de 14 dias.

Este adendo substitui o planejamento individual anterior nos pontos abaixo. O protocolo original conserva seu arquivo e hash. A mudança de método precisa entrar no manuscrito: os resultados de avaliação automática têm origem e interpretação próprias.

## Divisão do trabalho

| Trabalho | Execução |
|---|---|
| Examinar fontes, termos e acesso | Codex reúne evidências e registra permissões e bloqueios |
| Coletar, extrair, deduplicar e catalogar | Código em lote; Codex trata as exceções |
| Sugerir descrições, perguntas e referências | Regras automáticas e assistência de IA, com origem registrada |
| Validar e executar E5 e Qwen | Código no equipamento disponível, com registros de versão, tempo e memória |
| Conferir respostas e preparar análises | Verificações automáticas; eventual julgamento por IA identificado separadamente |
| Decisões autorais e mudanças de escopo | Yago recebe uma lista curta de decisões concretas |

Os scripts já implementam coleta dirigida, extração e catálogo determinístico. Preparação semântica completa, julgamento por modelo e execução integrada do piloto permanecem pendentes. Catalogar por regras não equivale a gerar metadados semânticos por IA.

## Objetivo da etapa rápida

Completar, em uma jornada, a seleção possível, a conferência das fontes, a coleta autorizada e seu catálogo. Validar o ambiente e iniciar o piloto técnico quando acesso, dependências e memória permitirem. A jornada é uma meta operacional; cada entrega termina com contagens e bloqueios reais.

A etapa produz uma coleção identificada e um diagnóstico técnico exploratório. Adequação julgada por IA recebe o rótulo **avaliação automática**. Esse resultado não constitui validação humana independente.

## Origem e controle dos registros

Cada anotação informa origem: regra determinística, assistência de IA ou revisão humana. Para IA, registrar ferramenta/modelo, versão disponível, instrução, data, evidência literal e eventual correção. Não preencher `approved` para fingir uma revisão humana. Valores desconhecidos continuam desconhecidos; alcance geral exige suporte na fonte.

Referências e perguntas são preparadas a partir dos documentos e congeladas antes das respostas. Descrições da busca ficam em arquivo separado. Registrar o compartilhamento de pesquisador ou ferramenta entre preparação e avaliação: separar arquivos não produz independência.

Uma checagem automática pode detectar ausência de valores, IDs ou termos, mas não estabelece sozinha se uma resposta é adequada. Avaliações de conteúdo por IA exigem justificativa ancorada e conservam o rótulo automático. Discordâncias e casos sem evidência ficam pendentes.

## Piloto e análise

O piloto técnico mantém a meta de 60 perguntas, quatro por banco e classe, se houver três bancos e cobertura suficiente. São 360 saídas principais e 90 de estabilidade. As 450 saídas não exigem 450 avaliações humanas na etapa rápida. Uma amostra menor pode servir à validação técnica, com seu tamanho e distribuição registrados; não recebe o nome de piloto completo.

As seis configurações A/B/C/Bp/L/S, os controles de fontes, a fidelidade técnica e a exclusão das famílias do piloto permanecem. H1/H2/H3 continuam como perguntas de pesquisa. Estimativas dependentes de referências ou julgamentos automáticos são exploratórias e condicionadas a essas referências e julgamentos. Não reportar apoio confirmatório ou concordância humana inexistente.

O estudo agora examina descrições assistidas quando usadas. O argumento de que metadados manuais representam um teto não descreve automaticamente essa execução. Conservar diferenças de origem ao interpretar cada contraste.

## Etapa final e manuscrito

O tamanho final depende do número real de famílias, dos resultados técnicos e da infraestrutura. Não há obrigação operacional de 120 ou 660 perguntas, nem promessa de precisão com uma amostra arbitrária. Fixar amostra e registrar o desenho modificado antes da etapa final.

Uma validação humana futura requer procedimento e amostra próprios. Ela fica separada da jornada rápida. A revisão temporal após 14 dias e o orçamento manual do planejamento anterior deixam de ser requisitos ativos.

O código de segmentação ainda exige extração humana aprovada. Para um piloto inteiramente automático, esse controle precisa de uma extensão explícita, com origem e limitações registradas, antes de executar a cadeia completa. Não contornar o controle alterando rótulos. O registro público final e as decisões metodológicas continuam pendentes.
