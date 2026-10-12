# Organização documental e recuperação de evidências para respostas bancárias

## Resumo

Uma resposta bancária depende da regra encontrada e das condições que delimitam seu uso. Este artigo examina como a descrição de trechos e a filtragem por produto e público afetam a recuperação de evidências em documentação pública de dois bancos brasileiros. A exploração assistida reúne 27 páginas e 62 trechos, compara cinco configurações de busca e usa vinte perguntas no piloto e dez perguntas de famílias novas na etapa final. O foco documental é definido após o início de uma geração complementar, encerrada com 56 respostas salvas. Os controles técnicos preservam 144 itens exigidos em 36 respostas. A calibração insuficiente do avaliador automático restringe os resultados a medidas documentais e diagnósticos de execução. Na etapa final, três configurações recuperam todas as âncoras de referência nas oito perguntas elegíveis; duas alcançam 87,5%. Casos trabalhados mostram o filtro favorecendo uma referência e excluindo outra por falta de relação entre categorias. Uma correção posterior recupera as referências no caso observado. O estudo entrega intervenções auditáveis, com alcance limitado à coleção e à preparação assistida, sem estimativa validada de adequação semântica.

Palavras-chave: organização do conhecimento; recuperação da informação; documentação bancária; inteligência artificial; avaliação documental.

## Document organization and evidence retrieval for banking answers

## Abstract

Banking answers depend on both the retrieved rule and the conditions that determine when it applies. This article examines how passage descriptions and filtering by product and audience affect evidence retrieval in public documentation from two Brazilian banks. The assisted exploration includes 27 pages and 62 passages, compares five retrieval configurations, and uses twenty pilot questions and ten final questions from new rule families. The documentary focus is defined after complementary generation starts, ending with 56 saved responses. Technical controls preserve 144 required items across 36 responses. The automated evaluator fails calibration, so outcomes are restricted to documentary measures and execution diagnostics. In the final phase, three configurations retrieve all reference anchors for the eight eligible questions; two achieve 87.5%. Worked cases show filtering helping one reference and excluding another because a relation between categories is missing. A subsequent correction recovers the references in the observed case. The study provides auditable interventions, with scope limited to this collection and assisted preparation, and without a validated estimate of semantic answer adequacy.

Keywords: knowledge organization; information retrieval; banking documentation; artificial intelligence; documentary evaluation.

## Organización documental y recuperación de evidencias para respuestas bancarias

## Resumen

Una respuesta bancaria depende de la regla recuperada y de las condiciones que delimitan su aplicación. Este artículo examina cómo la descripción de fragmentos y el filtrado por producto y público afectan la recuperación de evidencias en documentación pública de dos bancos brasileños. La exploración asistida reúne 27 páginas y 62 fragmentos, compara cinco configuraciones de búsqueda y utiliza veinte preguntas en el piloto y diez preguntas de familias nuevas en la etapa final. El enfoque documental se define tras iniciar una generación complementaria, cerrada con 56 respuestas guardadas. Los controles técnicos conservan 144 elementos exigidos en 36 respuestas. La calibración insuficiente del evaluador automático limita los resultados a medidas documentales y diagnósticos de ejecución. En la etapa final, tres configuraciones recuperan todas las anclas de referencia en las ocho preguntas elegibles; dos alcanzan el 87,5%. Los casos muestran beneficios y pérdidas del filtro, relacionadas con la representación de categorías. Una corrección posterior recupera las referencias del caso observado. El estudio ofrece intervenciones auditables, con alcance limitado a la colección y a su preparación asistida, sin una estimación validada de adecuación semántica.

Palabras clave: organización del conocimiento; recuperación de información; documentación bancaria; inteligencia artificial; evaluación documental.

## 1 Introdução

Uma pergunta sobre isenção de anuidade pode esconder várias decisões. O usuário pode ter investimentos no banco, mas a regra encontrada pode depender do cartão, do valor investido e das modalidades de investimento. Uma página sobre o assunto oferece evidências para explicar esses critérios. A decisão sobre o caso exige também reconhecer quais atributos foram informados e quais permanecem em aberto. Quando faltam dados, pedir esclarecimento pode preservar melhor a regra do que apresentar uma conclusão geral.

A geração aumentada por recuperação, conhecida pela sigla inglesa RAG, combina busca documental e produção de texto por um modelo de linguagem. Essa combinação amplia o papel da organização do conhecimento na resposta. Selecionar fontes, segmentar documentos, descrever trechos e estabelecer relações entre categorias define quais evidências ficam disponíveis. Uma falha nessa preparação pode se propagar mesmo quando o gerador segue a instrução de usar somente os documentos recebidos.

O problema envolve a interação entre recuperação e aplicabilidade. Um trecho pode estar relacionado ao assunto e conter uma regra restrita a um produto específico. Um filtro pode reduzir fontes incompatíveis e, ao mesmo tempo, excluir uma regra necessária para identificar uma condição ou pedir esclarecimento. A avaliação ganha precisão quando conserva esses mecanismos separados, em vez de resumir todas as etapas em uma única nota para a resposta.

Este artigo examina duas decisões documentais: enriquecer a representação dos trechos e filtrar candidatos por produto e público. A questão é como essas decisões afetam a recuperação de referências em uma pequena coleção de documentos bancários públicos. O objetivo aplicado é converter as ocorrências observadas em intervenções verificáveis na base de conhecimento. O leitor principal é o profissional que organiza fontes e precisa compreender por que uma evidência aparece ou desaparece.

A execução é uma exploração assistida conduzida por um pesquisador individual. A preparação das perguntas e das referências recebe apoio de inteligência artificial. O protocolo original, preservado no projeto, descreve equipes independentes e uma amostra confirmatória. A execução aplicada adota outro alcance: dois bancos, uma amostra de conveniência, referências assistidas e medidas documentais. O alcance assistido é registrado antes do piloto. A concentração da entrega na recuperação documental é autorizada após os rankings e 56 respostas estarem disponíveis. Essa mudança posterior ao início da execução integra a interpretação exploratória.

O estudo produz um catálogo rastreável, entradas publicadas, respostas preservadas e cálculos reproduzíveis. A calibração do juiz automático fica abaixo do critério fixado e a adequação semântica das respostas permanece sem estimativa validada. O artigo concentra a análise nas medidas sustentadas pelos registros: recuperação de âncoras, cobertura, exclusões, contexto efetivo e sinais técnicos. Essa delimitação organiza o que o leitor pode conferir e reaproveitar.

## 2 Relações entre organização documental e resposta

### 2.1 A necessidade de informação e seus atributos

Wilson (1999) relaciona modelos de comportamento informacional, busca e resolução de problemas. Essa perspectiva situa a recuperação dentro de uma necessidade de informação. A referência consultada inclui o resumo e os dados da publicação, sem pressupor leitura integral. No presente estudo, a relação com o problema do usuário orienta perguntas que explicitam produto e público ou exigem reconhecer a ausência dessas informações.

Metadados são informações usadas para descrever e localizar um documento ou trecho. Título, seção, produto e público entram nessa descrição. Os atributos de aplicabilidade delimitam a situação em que uma regra vale, incluindo idade, canal, período, valor e condição de uso. Produto e público participam do filtro experimental. Os demais atributos permanecem nos textos e nos dossiês. Passar pelo filtro, portanto, verifica apenas a compatibilidade prevista por seus campos.

As categorias também dependem de relações. Um cartão específico pertence à categoria geral de cartões, mas seus rótulos podem ser diferentes. Uma comparação por igualdade de nomes deixa essa relação implícita. Ao usar o rótulo como requisito de seleção, o sistema precisa de informação suficiente para reconhecer o vínculo. A mesma descrição que ajuda uma pergunta específica a encontrar seu produto pode dificultar uma pergunta ampla quando a hierarquia está ausente.

A descrição documental expressa escolhas sobre o uso das fontes. Manter o valor desconhecido é uma dessas escolhas. Quando o documento não explicita o público, o protocolo evita completar o campo por suposição. Essa opção conserva candidatos no filtro, com custo possível de ruído. A alternativa de excluir tudo que não tem descrição completa aumenta o risco de perda. O estudo registra esse trade-off e permite observar suas consequências.

### 2.2 Contexto na representação dos trechos

Lewis et al. (2020) apresentam a combinação entre recuperação e geração para tarefas intensivas em conhecimento. Nesta implementação, um recuperador seleciona trechos e o gerador recebe apenas os textos disponíveis no contexto. O modelo não consulta novos sites durante a resposta. O registro das evidências recebidas identifica a fronteira entre a coleção, a busca e a geração.

Ford (2024), na apresentação técnica da Anthropic, descreve o acréscimo de contexto produzido por modelo antes da indexação. A página identifica Daniel Ford como responsável por pesquisa e escrita, e o endereço anterior na seção de notícias redireciona para a página de engenharia. Aqui, os prefixos são determinísticos: título, seção, tipo, produto e público. O resultado observado se refere a essa representação e precisa de outra execução para estimar o efeito de contexto gerado por modelo.

Dadopoulos et al. (2025) relatam ganhos na qualidade das respostas com metadados gerados por modelo, acompanhados de perdas de recuperação em algumas comparações. Também observam redução de recuperação em um contraste que combina seleção de arquivos e reescrita da consulta, discutindo possível restrição excessiva ou efeito da reescrita. Esse antecedente sustenta a separação entre resultados de recuperação e geração. Seus filtros operam por arquivo, enquanto esta execução usa produto e público.

Joren et al. (2025) examinam contexto suficiente. Suficiência pergunta se as evidências contêm informação bastante para responder; aplicabilidade pergunta se essa informação vale para a pessoa e a situação descritas. Um contexto pode explicar os critérios de um cartão específico e ainda exigir o esclarecimento de qual cartão o usuário possui. A pergunta e o documento, considerados em conjunto, determinam a ação informacional esperada.

### 2.3 A tarefa do avaliador

OmniEval, de Wang et al. (2025), apresenta um benchmark financeiro para avaliação de recuperação e geração. A publicação na conferência EMNLP, a autoria e o identificador digital foram conferidos na fonte. Esse trabalho oferece um exemplo de desenho de avaliação automática. A validação de um juiz local continua dependendo de controles próprios, pois modelos, instruções, referências e tarefas diferem entre estudos.

A análise distingue três tarefas. A recuperação de âncoras verifica a presença de segmentos definidos como referência. Os diagnósticos técnicos verificam execução, repetição e identificadores de citação. A adequação semântica exige decidir se a resposta preserva sentido, condições e ação esperada. Essas tarefas podem compartilhar evidências, mas possuem critérios diferentes. O formato correto de uma saída estruturada também pode coexistir com uma decisão incorreta do juiz.

A preparação assistida impõe uma limitação adicional. Perguntas, metadados e referências podem refletir a interpretação da mesma ferramenta, o que reduz a independência entre as etapas. Congelar esses elementos antes das respostas conserva a cronologia e evita ajustes oportunistas. A rastreabilidade ajuda a auditar o processo e não remove o viés de seleção ou substitui validação independente.

## 3 Método executado

### 3.1 Fontes e critérios de seleção

A pesquisa é documental, quantitativa e exploratória. A coleção reúne 27 páginas oficiais de Inter e Bradesco sobre contas, cartões e serviços associados. Os critérios incluem acesso público, pertinência ao domínio, preservação da versão consultada e extração utilizável. Páginas vazias, erros de acesso e redirecionamentos fora do host cadastrado recebem justificativa de exclusão. Não há acesso a contas autenticadas, dados de clientes ou fontes internas.

Banco do Brasil e Caixa integram a seleção inicial de candidatos. Duas rodadas limitadas encerram a conferência para esta execução. As rotas examinadas da Caixa apresentam redirecionamentos circulares. No Banco do Brasil, a página de políticas contém material de privacidade em scripts, mas a trilha comparável de termos e extração não se completa no ciclo reservado. A exclusão é registrada como decisão de escopo, sem atribuir uma proibição geral aos bancos.

A conferência operacional de políticas, termos disponíveis e regras de acesso acompanha a coleta. Esse registro distingue a autorização interna para o lote e a licença de redistribuição. Os arquivos originais e os prompts que reproduzem os textos ficam no pacote privado do pesquisador. O GitHub recebe endereços, hashes, posições, perguntas próprias e indicadores derivados. A disponibilidade pública de uma página não é apresentada como consentimento expresso do banco.

O conjunto inicial conserva dezessete documentos. A ampliação examina treze endereços, com onze downloads e dez extrações aproveitáveis. Duas falhas de coleta e uma extração vazia ficam documentadas. Após a pausa do ambiente, as fontes da ampliação são recuperadas: 23 arquivos coincidem com os hashes anteriores e quatro mudam. A reconstrução das entradas usa a versão recuperada e registra a diferença antes da geração longa.

### 3.2 Extração e catalogação assistidas

O extrator preserva a origem e as posições dos textos. Quando o elemento principal da página está vazio, prioriza o corpo em relação a um artigo parcial de banner. Em páginas com um contêiner de conteúdo principal identificável, a seleção conserva o texto e as notas disponíveis e reduz menus. A conferência é assistida, sem revisão visual independente por pessoas ou uso de reconhecimento óptico de caracteres para suprir lacunas.

Tokens são unidades usadas pelos modelos para processar o texto e podem corresponder a partes de palavras. A segmentação usa 320 tokens e sobreposição de 48, preservando uma região comum entre trechos vizinhos. A coleção recuperada resulta em 62 trechos. Os números da execução anterior permanecem na história do projeto; o presente artigo descreve os segmentos usados nas entradas registradas desta execução.

Regras determinísticas associam expressões do título a produtos e expressões no texto a públicos. As ocorrências de público recebem posições de origem. Categorias desconhecidas permanecem explícitas. Expressões condicionais e de exceção são catalogadas como candidatos documentais, sem equivalência automática com regras semanticamente validadas. O catálogo público inclui rótulos e referências posicionais, sem republicar os textos completos.

As relações entre categorias não são expandidas no filtro principal. Essa opção torna visível o custo de uma comparação literal. Os metadados usados no resultado principal permanecem congelados. Uma intervenção posterior possui registro separado e informa seu caráter de demonstração sobre um caso já conhecido.

### 3.3 Perguntas e referências

Uma família agrupa perguntas que dependem da mesma regra. O piloto usa vinte perguntas de quatorze famílias; a etapa final usa dez perguntas de dez famílias novas. Cada banco contribui com duas perguntas por classe no piloto e uma por classe na etapa final. As classes são direta, condição, exceção, ambiguidade e insuficiência. A amostra fica abaixo da meta inicial porque a preparação evita multiplicar paráfrases apenas para alcançar um número.

Perguntas e dossiês são preparados com apoio de Codex antes das respostas. O dossiê registra a ação esperada, os requisitos e as referências. Cada âncora aponta para documento, posição e hash. As âncoras são segmentos curtos, escolhidos como indicadores documentais. Sua recuperação permite verificar localização e cobertura desse conjunto, com alcance diferente de uma avaliação completa de todas as proposições necessárias à resposta.

As perguntas sem suporte recebem busca lexical na coleção inteira e conferência assistida nas entradas congeladas. A ausência é relativa à coleção. Não se conclui que o banco carece de uma informação ou de um produto a partir dessa busca. Perguntas fictícias sobre produtos não encontrados também ficam identificadas no conjunto, de modo que não sejam interpretadas como serviços reais.

Os atributos de produto e público das perguntas são preparados com apoio de Codex. Incluem termos expressos, normalização e inferências de domínio. Conta You é associada a pessoa física, análise de crédito a cartão e a segunda via de débito a conta e pessoa física, por decisões da preparação. Esses campos não são extraídos por um modelo validado em perguntas reais. A auditoria posterior registra essa origem sem mudar as entradas ou os rankings. A coincidência entre preparação dos atributos e escolha das referências pode favorecer o filtro e limita a independência do contraste.

Todas as famílias do piloto são excluídas da etapa final. A regra de saques em caixa eletrônico usada no teste técnico anterior também é excluída. Benefícios de cartões adicionais e isenção de anuidade do Aeternum formam famílias distintas no mesmo documento. A dependência documental residual acompanha a análise, pois separar regras não torna seus textos de origem independentes.

### 3.4 Configurações e execução local

O Quadro 1 descreve cinco configurações de busca. A configuração S, sem documentos, pertence à geração complementar e tem medidas de recuperação não aplicáveis. O banco informado na pergunta delimita os candidatos em todas as buscas. O enriquecimento modifica a representação usada pelo recuperador. O gerador recebe os textos originais selecionados, com identificador, título, endereço e posição, sem os prefixos experimentais. Modelo, precisão e instruções de resposta permanecem iguais entre as configurações.

Quadro 1 Configurações de busca documental

| Código | Recuperação | Decisão documental |
|---|---|---|
| A | Busca semântica no trecho original | Sem prefixo adicional |
| B | Busca semântica com prefixo completo | Título, seção, tipo, produto e público |
| C | Busca de B com filtro | Produto e público preparados para a pergunta |
| Bp | Busca semântica com prefixo reduzido | Produto e público |
| L | Busca lexical BM25 | Correspondência de termos |

Fonte: elaboração própria, 2026.

O recuperador é multilingual-e5-large-instruct em precisão de 32 bits na unidade central de processamento. O gerador é Qwen3-8B na distribuição GGUF Q4_K_M, executada pelo llama.cpp b11557. A quantização usa uma representação compacta dos pesos. Revisões, hashes e versões efetivamente instaladas estão no registro. Um hash confere a identidade dos bytes e acompanha mudanças de arquivo, sem validar seu conteúdo.

O servidor usa contexto de 8.192 tokens, oito threads, lote de 512 e micro-lote de 128. A reorganização interna dos pesos e o cache global de prompts ficam desativados para respeitar o limite de memória. O cache da sessão conserva entradas consecutivas. Tentativas técnicas anteriores permanecem descritas nos registros públicos; suas respostas parciais indisponíveis após a pausa não integram a análise.

A entrada construída admite até 4.096 tokens, e a resposta até 512. A busca conserva as dez primeiras posições; o contexto começa com até cinco trechos. Se o limite de entrada é excedido, o último trecho é removido e o evento é registrado. A geração principal usa temperatura zero e penalidade de repetição igual a um. Os controles técnicos não motivam penalidade adicional.

O plano de estabilidade usa sementes 43 e 44, temperatura 0,7, top_p 0,8 e top_k 20 nas configurações A, B e C. O arredondamento por banco e classe seleciona dez perguntas, correspondentes a 50% do piloto. O orçamento é de 120 respostas principais e sessenta adicionais, totalizando 180. A etapa final prevista contém sessenta respostas principais, cuja geração não foi executada. O executor salva cada combinação e só reutiliza checkpoints com entrada, parâmetros e identidade de runtime correspondentes.

### 3.5 Fidelidade e decisão sobre o juiz

Doze controles sintéticos verificam valores monetários, percentuais, datas e identificadores de fonte. Cada caso usa a política principal e as duas sementes de estabilidade, totalizando 36 saídas e 144 itens exigidos. A conferência procura equivalentes explícitos e registra limites de saída, truncamento de entrada e blocos de ao menos vinte tokens repetidos três vezes. A preservação literal tem alcance restrito e não estabelece fidelidade semântica geral.

O risco de a penalidade de repetição atingir os tokens de evidência é tratado com penalidade neutra e conferência dos itens nas três políticas de semente. O comportamento de Transformers não é usado para certificar outro backend. Os parâmetros efetivos de llama.cpp, seu executável e seu retorno de tokens acompanham o registro. A fidelidade é repetida na configuração adotada para a execução atual.

A calibração do juiz exige ao menos dezenove acertos em vinte controles e todas as estruturas de saída válidas. O plano admite uma correção de instrução e uma segunda rodada. Os relatórios publicados registram dez acertos na primeira e dezessete na segunda. Os casos incluem erros numéricos, fonte inventada, público incompatível, condição omitida, ambiguidade e ausência de evidência. A decisão encerra a calibração e desativa a adequação automática das respostas bancárias.

Essas calibrações antecedem os ajustes operacionais de memória. A exclusão do juiz é mantida de forma conservadora. As saídas brutas daquela etapa não foram recuperadas após a pausa, limitação registrada junto aos relatórios públicos. Não se reabre a seleção do avaliador usando as respostas bancárias. Não há julgamento humano independente, coeficientes de concordância entre pessoas ou notas semânticas imputadas às falhas técnicas.

### 3.6 Indicadores e incerteza

A recuperação de âncoras é a proporção das referências presentes nos primeiros três, cinco ou dez trechos. A cobertura verifica se um conjunto definido no dossiê está completo. Perguntas sem referência e a configuração sem documentos têm medida não aplicável. O denominador aparece junto a cada média. Os indicadores permanecem ligados à especificação assistida e não são convertidos em taxa de adequação.

A análise do filtro separa trechos excluídos que contêm uma referência e âncoras sem nenhum trecho restante que as contenha. A segunda medida identifica indisponibilidade causada pelo filtro. A análise também verifica as âncoras nas evidências efetivamente enviadas ao gerador, após possíveis retiradas por orçamento. Ranking e contexto entregue podem divergir, razão para conservar os dois registros.

Os diagnósticos das respostas incluem falha, limite de saída, truncamento, repetição e citações entre colchetes. Um identificador é válido nesse diagnóstico quando pertence às evidências recebidas. A validade do identificador não decide se a afirmação correspondente é sustentada pelo texto. A execução parcial conserva saídas com sementes distintas, mas sua composição resulta da interrupção. Não se estima estabilidade geral a partir desse subconjunto.

B menos A e B menos Bp usam perguntas de condição e exceção. C menos B usa perguntas com atributos preparados, incluindo inferências assistidas. Os intervalos percentis de 95% e 98,33% usam as mesmas cinco mil reamostragens de famílias, estratificadas por banco, com semente 2026. A análise informa se a estimativa pontual alcança dez pontos percentuais e se sua magnitude absoluta atinge esse valor. Todos os contrastes são exploratórios.

### 3.7 Dimensionamento e registro

O cálculo confirmatório do protocolo original usa pares discordantes. Com discordância q de 0,25, diferença de interesse Δ de 0,10, poder de 80%, β de 0,20 e nível α* de 0,05 dividido por três, a aproximação resulta em 258,98 pares. O limiar é de 260 famílias elegíveis de condição e exceção. A Equação 1 expressa a aproximação usada para o dimensionamento anterior.

$$
n \approx \frac{[z_{1-\alpha^*/2}\sqrt{q}+z_{1-\beta}\sqrt{q-\Delta^2}]^2}{\Delta^2} \tag{1}
$$

O plano alternativo de precisão, sob independência e discordância de 0,25, exige cerca de 97 pares para meia largura de dez pontos em um intervalo normal de 95%. Simulações ilustrativas com duas mil repetições examinam discordâncias de 0,10, 0,25 e 0,40. A etapa final tem quatro famílias de condição e exceção. Nem o alvo de poder nem o de precisão é alcançado. A apresentação de intervalos não amplia a representatividade da amostra.

Os rankings de ambos os conjuntos são calculados na preparação. As famílias são separadas, sem ocultação dos rankings finais. O método assistido e os hashes entram em commit público antes do piloto. A decisão posterior de concluir a recuperação documental mantém as entradas e registra as 56 gerações como módulo parcial. A análise dos dois conjuntos não constitui validação externa ou pré-registro confirmatório. Não há geração final, depósito com DOI ou liberação presumida dessa etapa. O pacote privado conserva fontes, entradas e respostas salvas.

## 4 Resultados

### 4.1 Execução e controles

A busca documental é concluída nos dois conjuntos: vinte perguntas do piloto e dez do final, comparadas em cinco configurações, totalizando 150 pares. A auditoria verifica as posições e os hashes das 43 âncoras e suas ligações com os 62 trechos. As 56 respostas salvas pertencem a uma geração parcial do piloto, cuja meta anterior era 180; as sessenta respostas finais previstas não foram geradas. O subconjunto disponível decorre da interrupção e não sustenta uma comparação balanceada de qualidade. Nos diagnósticos dessas 56 saídas, não há falha, limite de saída, repetição degenerada ou identificador citado fora das evidências recebidas. Esses sinais técnicos não atribuem correção semântica.

Os 36 controles atuais preservam os 144 itens exigidos, sem truncamento ou repetição degenerada. Os relatórios de calibração anteriores conservam dez e dezessete acertos em vinte casos, apesar da validade estrutural das saídas. A adequação automática permanece desativada e nenhuma resposta bancária recebe uma nota atribuída a avaliador humano. Os testes de código verificam também retomada e rejeição de controles finais divergentes.

### 4.2 Recuperação de referências

Tabela 1 Recuperação e cobertura de âncoras nas primeiras cinco posições

| Configuração | Recall piloto (16) | Cobertura piloto (16) | Recall final (8) | Cobertura final (8) |
|---|---:|---:|---:|---:|
| A | 90,625% | 87,500% | 87,500% | 87,500% |
| B | 90,625% | 87,500% | 100,000% | 100,000% |
| C | 96,875% | 93,750% | 87,500% | 87,500% |
| Bp | 96,875% | 93,750% | 100,000% | 100,000% |
| L | 93,750% | 93,750% | 100,000% | 100,000% |

Fonte: cálculos sobre os rankings e as referências assistidas publicados no projeto. Os números entre parênteses indicam perguntas elegíveis.

A amostra elegível tem dezesseis perguntas no piloto e oito na etapa final. Na etapa final, B, Bp e L recuperam todas as âncoras em cinco posições. A e C alcançam 87,5%, com perdas em perguntas diferentes. O pequeno conjunto e as referências curtas produzem um teto da medida em três configurações. O resultado não fundamenta superioridade geral de modelos ou equivalência entre todas as formas de busca.

No piloto, B menos A e B menos Bp têm diferença de −12,5 pontos no recall nas oito perguntas de condição e exceção. Os intervalos percentis de 95% e 98,33% vão de −42,86 a zero pontos. C menos B tem diferença de 6,25 pontos nas dezesseis perguntas elegíveis; o intervalo de 95% vai de zero a 21,43 pontos, e o de 98,33%, de zero a 25. A cobertura apresenta os mesmos contrastes.

No conjunto final, B menos A e B menos Bp têm diferença zero nas quatro perguntas de condição e exceção e intervalos de zero a zero. A ausência de diferenças nesse conjunto não demonstra equivalência geral. C menos B tem diferença de −12,5 pontos nas oito perguntas elegíveis, com ambos os intervalos de −37,5 a zero pontos. Os contrastes negativos de 12,5 pontos atingem a magnitude de interesse de dez pontos, enquanto o ganho de 6,25 não atinge esse valor. Nenhuma dessas comparações fornece apoio confirmatório.

### 4.3 Casos que mostram benefício e perda do filtro

A pergunta B05 trata da inclusão da segunda via de um cartão de débito perdido nos serviços essenciais gratuitos. O dossiê aponta para uma passagem que delimita a gratuidade e registra perda como exceção. Em cinco posições, B não recupera a âncora, enquanto C a recupera. O filtro usa produto conta e público pessoa física, preparados por inferência assistida. A pergunta menciona cartão de débito e não identifica o público. Essa classificação reduz candidatos e altera a seleção, com risco de favorecer a fonte usada na própria preparação. O benefício é condicionado a esses campos e não demonstra sua extração correta de perguntas reais. O resultado demonstra um benefício documental nesse caso, sem atribuir uma nota semântica à resposta.

A pergunta BF04 indaga se investimentos no Bradesco tornam a anuidade do cartão isenta. O cartão não é identificado. A, B, Bp e L recuperam as duas âncoras da regra do Aeternum em cinco posições. C não recupera nenhuma porque a pergunta usa a categoria geral cartão e a descrição registra o produto específico Aeternum. A igualdade de rótulos deixa ausente a relação entre as categorias e retira os trechos necessários ao esclarecimento previsto no dossiê.

Os dois casos mostram que o filtro depende da representação e da pergunta. Em B05, a redução de candidatos favorece uma referência. Em BF04, a falta de hierarquia torna uma regra inacessível. A descrição específica do Aeternum pode favorecer a busca de seu produto e também exige uma relação mais ampla quando funciona como requisito de exclusão. O efeito da catalogação se articula com a política de seleção.

Uma demonstração posterior acrescenta a relação entre Aeternum e cartão e reaplica a seleção ao ranking congelado de B. As duas âncoras retornam às primeiras cinco posições. O teste é limitado ao caso observado, sem novas respostas ou mudanças nos resultados principais. Trata-se de uma correção verificável do mecanismo identificado; sua generalização depende de perguntas e documentos ainda não usados para definir a intervenção.

## 5 Discussão e ações na base de conhecimento

A primeira implicação para o profissional da informação é a necessidade de distinguir descrição e exclusão. Uma descrição orienta a localização de um trecho e modifica sua posição relativa. Um requisito de filtro também decide se o trecho pode aparecer. O uso da mesma categoria nessas duas funções exige verificar relações, abrangência e valores desconhecidos. A relevância dessa conferência cresce quando as fontes contêm regras gerais e produtos especializados.

O caso BF04 torna essa relação observável. O nome específico identifica corretamente o produto documentado. Sua ligação com a categoria geral é necessária para perguntas amplas. A correção pode preservar a distinção entre cartões e reconhecer a hierarquia ao mesmo tempo. A informação exigida para decidir a isenção continua dependendo do cartão e das condições do usuário; ampliar a recuperação apoia a busca de evidências e o pedido de esclarecimento.

O benefício em B05 também possui alcance definido. O filtro melhora a localização da âncora nesse ranking e não demonstra que toda pergunta com produto e público deva usar exclusão literal. A coexistência dos dois casos ajuda a substituir uma recomendação única por critérios verificáveis: observar quais referências somem, quais permanecem em outro trecho e quais relações de categoria explicam a seleção. A intervenção pode então ser aplicada ao vocabulário e reavaliada.

A comparação dos prefixos tem comportamento dependente da pergunta. O prefixo completo perde uma referência no piloto que o prefixo reduzido conserva. Na etapa final, ambos alcançam o teto da medida. Esse padrão recomenda examinar detalhes de representação antes de atribuir um efeito geral ao enriquecimento. Título, seção e tipo oferecem contexto, mas também podem modificar a competição entre trechos e deslocar uma informação específica.

Os resultados ambíguos relatados por Dadopoulos et al. (2025) reforçam a necessidade de conservar medidas separadas. Nesta execução, o juiz insuficientemente calibrado limita a análise à perda ou recuperação documental e aos sinais técnicos. A consequência semântica de uma mudança no ranking permanece aberta. Cobertura alta, identificador válido e resposta correta são tarefas relacionadas que exigem conferências próprias.

O Quadro 2 organiza ações que o responsável pela base pode executar e testar. As propostas seguem a evidência disponível e não pressupõem uma equipe de anotação. Um pesquisador individual pode preservar versões, modificar uma relação documentada e medir a recuperação novamente. A validação semântica independente exige outro componente de estudo e conserva sua própria declaração de método.

Quadro 2 Ocorrências e intervenções documentais

| Ocorrência | Registro utilizado | Intervenção |
|---|---|---|
| Produto específico perde relação com categoria geral | BF04 e trilha de exclusão | Registrar hierarquia e testar seleção ampliada |
| Redução de candidatos favorece referência | B05 e ranking por configuração | Examinar o uso do filtro por classe de pergunta |
| Referência não aparece nas primeiras posições | Âncoras e ranking completo conservado | Rever descrição, segmentação e competição entre trechos |
| Orçamento retira evidências | Lista efetivamente enviada | Reunir regra e condição ou ajustar prioridade |
| Avaliador erra controles conhecidos | Duas calibrações publicadas | Conservar adequação fora das medidas principais |

Fonte: elaboração própria, 2026. A linha sobre orçamento descreve um mecanismo de controle; a tabela de diagnósticos informa se ele ocorreu nesta execução.

A calibração oferece também um resultado operacional. A estrutura correta de uma saída permite seu processamento e pode coexistir com rótulos incorretos. A política registrada evita que essa facilidade de integração seja confundida com competência de avaliação. Uma ferramenta que não alcança o critério definido pode continuar útil para exploração, mas suas notas não sustentam a conclusão sobre adequação nesta tarefa.

A divulgação dos elementos de referência torna a preparação discutível. Outros pesquisadores podem contestar uma âncora curta, identificar uma condição omitida ou ampliar a coleção. Os cálculos podem ser reproduzidos sem modelos a partir dos rankings públicos. Essa abertura expõe escolhas metodológicas, inclusive seus limites, e permite uma revisão mais concreta do que uma taxa de acerto apresentada sem entradas rastreáveis.

## 6 Limitações e disponibilidade

A coleção é pequena e selecionada por conveniência. Não cobre todos os produtos, canais ou públicos das instituições. Os candidatos excluídos refletem dificuldades técnicas e o limite do ciclo de coleta. Quatro fontes recebem novos arquivos na recuperação, e a execução registra essa versão. Páginas futuras podem mudar novamente; uma nova coleta constitui outra coleção e precisa de novos hashes.

Metadados, perguntas e referências recebem assistência da mesma ferramenta. A preparação pode favorecer regras mais fáceis de reconhecer e produz dependência entre decisões. Não há separação equivalente às equipes independentes do protocolo original. As âncoras curtas medem localização de segmentos, sem assegurar a cobertura de todas as proposições que uma pessoa especialista escolheria. Os intervalos são condicionados a essa referência e à amostra observada.

O gerador quantizado e o recuperador local também delimitam os resultados. Os controles sintéticos preservam itens conhecidos em contextos específicos; seu sucesso não implica fidelidade geral. O módulo parcial inclui duas sementes adicionais em algumas entradas e sinais técnicos, sem leitura independente das respostas. Não houve teste de compreensão com leitores, avaliação humana das respostas ou comparação entre anotações de pessoas distintas.

Os relatórios de calibração anteriores permanecem públicos, mas suas saídas brutas não foram recuperadas após a pausa. A decisão conservadora de excluir o juiz evita usá-los para liberar uma medida semântica na execução atual. Os arquivos novos, incluindo entradas e respostas, são preservados em pacote privado antes e após as fases. Essa limitação de proveniência anterior integra a interpretação e não é completada por dados inventados.

O GitHub contém código, perguntas próprias, referências posicionais, hashes, rankings e relatórios derivados. O pacote privado conserva originais, trechos, índices, prompts e as 56 respostas do módulo parcial. A reprodução dos cálculos usa somente dados públicos e a biblioteca padrão do Python. O código, os dados derivados e as instruções estão em https://github.com/yhenriux/rag-bancario-publico. A reprodução da geração depende da versão das fontes, do modelo e do executável. Alterações nesses elementos recebem novos registros.

ChatGPT/Codex participa da discussão do desenho, pesquisa de fontes, programação, preparação de referências, análise assistida e redação e revisão. Qwen3-8B gera as respostas e participou dos controles de calibração anteriores; E5 produz representações de recuperação. Cálculos e diagnósticos documentais são executados por código publicado. A assistência é declarada e as ferramentas não recebem autoria. O pesquisador trabalha no Inter; a investigação usa apenas fontes públicas e não representa posicionamento institucional. A responsabilidade intelectual e a aprovação de publicação permanecem com o pesquisador.

## 7 Considerações finais

O estudo executa uma comparação documental com fontes públicas de dois bancos, referências posicionais e versões registradas. O filtro favorece uma referência e elimina outra em casos diferentes. A relação entre categorias explica uma das perdas e permite demonstrar uma correção no ranking conhecido. A calibração insuficiente conserva a adequação semântica fora das conclusões, com resultados centrados nas medidas verificáveis.

O leitor pode examinar as perguntas, contestar referências, reaproveitar os controles e repetir os cálculos publicados. Também pode testar relações de produto em outra coleção ou avaliar outro juiz com casos conhecidos. O produto aplicado é uma ligação rastreável entre uma decisão documental, sua ocorrência no sistema e uma intervenção que pode receber nova verificação.

## Referências

DADOPOULOS, Michail; LADAS, Anestis; MOSCHIDIS, Stratos; NEGKAKIS, Ioannis. **Metadata-Driven Retrieval-Augmented Generation for Financial Question Answering**. arXiv, 2025. Preprint arXiv:2510.24402, versão 1. Disponível em: https://arxiv.org/html/2510.24402v1. Acesso em: 11 out. 2026.

FORD, Daniel. **Introducing Contextual Retrieval**. Anthropic, 19 set. 2024. Disponível em: https://www.anthropic.com/engineering/contextual-retrieval. Acesso em: 11 out. 2026.

INTFLOAT. **multilingual-e5-large-instruct**. Hugging Face, [s. d.]. Modelo, revisão 274baa43b0e13e37fafa6428dbc7938e62e5c439. Disponível em: https://huggingface.co/intfloat/multilingual-e5-large-instruct. Acesso em: 12 out. 2026.

JOREN, Hailey; ZHANG, Jianyi; FERNG, Chun-Sung; JUAN, Da-Cheng; TALY, Ankur; RASHTCHIAN, Cyrus. **Sufficient Context: A New Lens on Retrieval Augmented Generation Systems**. In: INTERNATIONAL CONFERENCE ON LEARNING REPRESENTATIONS, 2025. Artigo. Disponível em: https://research.google/pubs/sufficient-context-a-new-lens-on-retrieval-augmented-generation-systems-2/. Acesso em: 11 out. 2026.

LEWIS, Patrick et al. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**. arXiv, 2020. Preprint arXiv:2005.11401. Disponível em: https://arxiv.org/abs/2005.11401. Acesso em: 11 out. 2026.

QWEN TEAM. **Qwen3-8B-GGUF**. Hugging Face, [s. d.]. Modelo, revisão 7c41481f57cb95916b40956ab2f0b139b296d974. Disponível em: https://huggingface.co/Qwen/Qwen3-8B-GGUF. Acesso em: 12 out. 2026.

WANG, Shuting; TAN, Jiejun; DOU, Zhicheng; WEN, Ji-Rong. OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in Financial Domain. In: CONFERENCE ON EMPIRICAL METHODS IN NATURAL LANGUAGE PROCESSING, 2025, Suzhou. **Proceedings [...]**. Association for Computational Linguistics, 2025. p. 5726–5751. DOI: 10.18653/v1/2025.emnlp-main.292. Disponível em: https://aclanthology.org/2025.emnlp-main.292/. Acesso em: 11 out. 2026.

WILSON, T. D. Models in information behaviour research. **Journal of Documentation**, v. 55, n. 3, p. 249–270, 1999. DOI: 10.1108/EUM0000000007145.
