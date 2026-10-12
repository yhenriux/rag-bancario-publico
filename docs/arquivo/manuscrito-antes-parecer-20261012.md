> Registro histórico anterior ao parecer de 12 de outubro de 2026. O texto vigente está em `../manuscrito.md`.

# Organização do conhecimento em RAG bancário: recuperação de evidências em documentos públicos brasileiros

## Resumo

Este estudo examina como metadados e filtros de produto e público afetam a recuperação de evidências bancárias. A análise exploratória reúne 27 páginas públicas de dois bancos brasileiros, 62 trechos e cinco configurações de busca, com vinte perguntas no piloto e dez de famílias novas no conjunto final. Perguntas, atributos e referências recebem preparação assistida por inteligência artificial. O alcance documental é definido após o início da geração complementar, interrompida com 56 respostas salvas. Os controles preservam 144 itens em 36 saídas; a calibração insuficiente do avaliador impede estimar adequação semântica. Nas oito perguntas finais elegíveis, três configurações recuperam todas as âncoras nas primeiras cinco posições; duas alcançam 87,5%. Os casos mostram benefício da filtragem e perda por ausência de relação entre categorias. Uma intervenção posterior recupera as referências no caso observado. A contribuição associa decisões documentais, ocorrências de recuperação e intervenções auditáveis, com conclusões restritas à coleção, às referências assistidas e ao desenho exploratório.

Palavras-chave: organização do conhecimento; recuperação da informação; documentação bancária; inteligência artificial; avaliação documental.

## Knowledge organization in banking RAG: evidence retrieval from Brazilian public documents

## Abstract

This study examines how metadata and product and audience filters affect banking evidence retrieval. The exploratory analysis comprises 27 public pages from two Brazilian banks, 62 passages, and five retrieval configurations, with twenty pilot questions and ten final questions from new rule families. Questions, attributes, and references are prepared with artificial intelligence assistance. The documentary scope is defined after complementary generation begins, which stops with 56 saved responses. Controls preserve 144 items across 36 outputs; insufficient evaluator calibration prevents estimating semantic answer adequacy. For the eight eligible final questions, three configurations retrieve all anchors within the first five positions, while two achieve 87.5%. The cases show a filtering benefit and a loss caused by a missing category relation. A subsequent intervention restores the references in the observed case. The contribution links documentary decisions, retrieval occurrences, and auditable interventions. Conclusions remain limited to the collection, assisted references, and exploratory design, without extending these retrieval findings to validated answer correctness.

Keywords: knowledge organization; information retrieval; banking documentation; artificial intelligence; documentary evaluation.

## Organización del conocimiento en RAG bancario: recuperación de evidencias en documentos públicos brasileños

## Resumen

Este estudio examina cómo los metadatos y los filtros de producto y público afectan la recuperación de evidencias bancarias. El análisis exploratorio reúne 27 páginas públicas de dos bancos brasileños, 62 fragmentos y cinco configuraciones de búsqueda, con veinte preguntas en el piloto y diez de familias nuevas en el conjunto final. Preguntas, atributos y referencias reciben preparación asistida por inteligencia artificial. El alcance documental se define tras iniciar la generación complementaria, interrumpida con 56 respuestas guardadas. Los controles conservan 144 elementos en 36 salidas; la calibración insuficiente del evaluador impide estimar adecuación semántica. En las ocho preguntas finales elegibles, tres configuraciones recuperan todas las anclas en las primeras cinco posiciones; dos alcanzan el 87,5%. Los casos muestran un beneficio del filtrado y una pérdida por ausencia de relación entre categorías. Una intervención posterior recupera las referencias del caso observado. La contribución vincula decisiones documentales, resultados de recuperación e intervenciones auditables, con conclusiones circunscritas a la colección, las referencias asistidas y el diseño exploratorio.

Palabras clave: organización del conocimiento; recuperación de información; documentación bancaria; inteligencia artificial; evaluación documental.

## 1 Introdução

A recuperação de uma regra bancária depende de como o documento descreve o produto, o público e as condições de uso. Uma pergunta sobre isenção de anuidade, por exemplo, pode exigir identificar o cartão, o valor investido e as modalidades de investimento. A página encontrada pode explicar esses critérios, embora a pergunta ainda omita informações necessárias à decisão. Nessa situação, localizar a regra também sustenta o pedido de esclarecimento ao usuário.

A geração aumentada por recuperação, conhecida pela sigla inglesa RAG, combina busca em documentos e produção de texto por um modelo de linguagem. A organização do conhecimento participa dessa operação por meio da seleção das fontes, da segmentação, da descrição dos trechos e das relações entre categorias. Essas escolhas delimitam as evidências disponíveis para o gerador. Uma informação excluída durante a busca permanece indisponível mesmo quando o modelo segue a instrução de responder com base nas fontes recebidas.

Metadados e filtros exercem funções relacionadas nesse processo. A descrição de um trecho modifica sua representação e sua posição na busca. O filtro determina quais candidatos permanecem acessíveis. Assim, um atributo pode favorecer a localização de uma regra e também restringir uma evidência necessária para reconhecer uma condição ou uma exceção. A interpretação desses efeitos exige medidas específicas para recuperação, disponibilidade e adequação da resposta.

Este artigo investiga como o enriquecimento dos trechos e a filtragem por produto e público afetam a recuperação de referências em documentação pública bancária brasileira. O estudo compara cinco configurações em uma coleção de Inter e Bradesco e acompanha as ocorrências que explicam ganhos e perdas na busca. Sua contribuição aplicada é ligar decisões de organização documental a registros verificáveis e a intervenções na base de conhecimento. O leitor principal é o profissional responsável por organizar fontes e investigar por que uma evidência aparece ou desaparece.

A pesquisa é conduzida por um pesquisador individual, com apoio de inteligência artificial na preparação e na análise. O protocolo original, preservado no repositório, previa equipes independentes e uma amostra confirmatória. A execução assistida, registrada antes do piloto, adota dois bancos, amostra de conveniência e referências preparadas com apoio de IA. A decisão de concentrar a entrega na recuperação documental ocorre depois de os rankings e 56 respostas estarem disponíveis. Essa cronologia situa a análise no alcance exploratório e integra seus limites de interpretação.

A entrega reúne catálogo rastreável, entradas publicadas, respostas preservadas e cálculos reproduzíveis. A calibração insuficiente do avaliador automático mantém a adequação semântica sem estimativa validada. Os resultados apresentados abrangem recuperação de âncoras, cobertura dos conjuntos de referência, exclusões, contexto efetivo e diagnósticos técnicos. Cada medida corresponde a uma tarefa definida e conserva as restrições da preparação assistida.

## 2 Organização documental e recuperação de evidências

### 2.1 Necessidades de informação e atributos de aplicabilidade

Wilson (1999) relaciona modelos de comportamento informacional, busca e resolução de problemas. Essa perspectiva situa a recuperação no contexto de uma necessidade de informação. A consulta utilizada neste artigo abrange o resumo e os dados bibliográficos da publicação, sem pressupor leitura integral. No estudo aplicado, a necessidade do usuário orienta perguntas que informam produto e público ou exigem reconhecer quais atributos ainda precisam de esclarecimento.

Metadados são informações que descrevem e ajudam a localizar documentos ou trechos. Título, seção, tipo, produto e público compõem a descrição usada nesta pesquisa. Os atributos de aplicabilidade delimitam a situação em que uma regra vale: idade, canal, período, valor e condições de uso, entre outros. Produto e público participam da filtragem; os demais atributos permanecem nos textos e nos dossiês. A aprovação de um trecho pelo filtro verifica, portanto, a compatibilidade prevista nesses campos, com alcance parcial sobre a aplicabilidade da regra.

As relações entre categorias também afetam essa compatibilidade. Um cartão específico pertence à categoria geral de cartões, embora seu nome e o rótulo da categoria sejam diferentes. A comparação literal entre nomes deixa essa relação sem representação. Quando o rótulo funciona como requisito de seleção, a ausência do vínculo pode excluir uma regra pertinente a uma pergunta ampla. A descrição específica do produto e sua relação com a categoria geral precisam operar em conjunto.

Conservar valores desconhecidos é outra decisão de organização documental. Quando a fonte não explicita o público, o protocolo mantém o campo sem completar seu conteúdo por suposição. O filtro preserva esse candidato, com possível aumento de ruído. A exclusão de registros incompletos amplia o risco de perda de evidências. Esse compromisso entre acesso e restrição depende da cobertura e da qualidade da descrição e recebe registro no desenho aplicado.

### 2.2 Enriquecimento contextual e suficiência

Lewis et al. (2020) apresentam a combinação de recuperação e geração em tarefas intensivas em conhecimento. Na implementação deste estudo, o recuperador seleciona trechos e o gerador trabalha com os textos inseridos na entrada. A resposta não envolve consulta a novos sites. O registro das evidências recebidas conserva a passagem entre coleção, recuperação e geração e delimita o material disponível em cada execução.

Ford (2024), na apresentação técnica da Anthropic, descreve a inclusão de contexto produzido por modelo antes da indexação. A página atribui pesquisa e escrita a Daniel Ford; o endereço anterior na seção de notícias redireciona para a página de engenharia. Nesta pesquisa, os prefixos são produzidos por regras determinísticas e reúnem título, seção, tipo, produto e público. Os achados descrevem essa forma de enriquecimento. Estimar o efeito de contexto gerado por modelo exige outra configuração e outra execução.

Dadopoulos et al. (2025) relatam melhora na qualidade das respostas com metadados gerados por modelo, acompanhada de perdas de recuperação em algumas comparações. Em um contraste que combina seleção de arquivos e reescrita da consulta, a recuperação também diminui. Os autores discutem restrição excessiva e efeitos da reescrita como explicações possíveis. Essa evidência fundamenta o acompanhamento separado de recuperação e geração. A comparação entre os estudos considera que seus filtros operam por arquivo, enquanto o desenho aqui aplicado utiliza produto e público.

Joren et al. (2025) examinam a suficiência do contexto. Suficiência verifica se as evidências contêm informação bastante para responder; aplicabilidade verifica se essa informação vale para a pessoa e a situação descritas. Uma fonte pode apresentar os critérios de um cartão e ainda exigir identificar qual cartão o usuário possui. Essas dimensões coexistem na avaliação e orientam ações como responder, esclarecer ou reconhecer a limitação documental.

### 2.3 Referências de avaliação e independência

OmniEval, de Wang et al. (2025), apresenta um conjunto de referência financeiro para avaliar recuperação e geração. Sua publicação na conferência EMNLP, autoria e identificador digital foram conferidos na fonte. O trabalho fornece um antecedente de avaliação automática em domínio financeiro. O uso de um avaliador local exige, adicionalmente, calibração para os modelos, instruções, referências e tarefas efetivamente empregados.

O desenho distingue três tarefas de avaliação. A recuperação de âncoras confere a presença de segmentos preparados como referência. Os diagnósticos técnicos verificam execução, repetição e identificadores de citação. A adequação semântica requer avaliar a preservação do sentido, das condições e da ação esperada. Essas tarefas compartilham materiais, mas seus critérios e seus limites de validade são próprios. Uma saída estruturada pode ser processável e conter uma decisão incorreta do avaliador.

A independência entre preparação e avaliação ganha relevância quando a mesma ferramenta apoia perguntas, metadados e referências. Suas interpretações podem se repetir entre etapas e favorecer determinados registros. Fixar os arquivos antes das respostas conserva a cronologia e impede ajustes oportunistas desses elementos. A rastreabilidade torna essa preparação auditável, enquanto a validação independente continua necessária para examinar seus vieses de seleção e interpretação.

## 3 Método executado

### 3.1 Fontes e critérios de seleção

O estudo é documental, quantitativo e exploratório. A coleção contém 27 páginas oficiais de Inter e Bradesco sobre contas, cartões e serviços associados. A inclusão exige acesso público, pertinência ao domínio, preservação da versão consultada e extração utilizável. Páginas vazias, erros de acesso e redirecionamentos fora do domínio cadastrado recebem justificativa de exclusão. A coleta abrange fontes públicas, sem acesso a contas autenticadas, dados de clientes ou documentos internos.

Banco do Brasil e Caixa também integram a seleção inicial. A conferência termina após duas rodadas limitadas para cada candidato. Nas rotas examinadas da Caixa, ocorrem redirecionamentos circulares. No Banco do Brasil, a página de políticas contém informações de privacidade em scripts, mas a trilha comparável de termos e extração não se completa no ciclo reservado. As exclusões expressam decisões de escopo dessa execução e não estabelecem uma proibição geral de coleta nessas instituições.

A conferência operacional de políticas, termos disponíveis e regras de acesso acompanha cada lote. O registro distingue liberação interna do projeto e licença de redistribuição. Originais e prompts que reproduzem os textos permanecem no pacote privado do pesquisador. O GitHub publica endereços, hashes, posições, perguntas próprias e indicadores derivados. O acesso público às páginas não constitui consentimento expresso dos bancos para reproduzir seu conteúdo.

A coleção inicial contém dezessete documentos. A ampliação examina treze endereços, produz onze downloads e aproveita dez extrações. Duas falhas de coleta e uma extração vazia ficam registradas. Após a pausa do ambiente, a recuperação das fontes conserva 23 arquivos com os hashes anteriores e identifica mudança em quatro. As entradas são reconstruídas sobre essa versão recuperada, cuja diferença é registrada antes da geração longa.

### 3.2 Extração e catalogação assistidas

A extração preserva origem e posições dos textos. Quando o elemento principal da página está vazio, o extrator utiliza o corpo em lugar de um artigo parcial de banner. Quando existe um contêiner principal identificável, seleciona seu conteúdo, conserva texto e notas disponíveis e reduz menus. A conferência é assistida por IA. Não houve revisão visual independente por pessoas nem uso de reconhecimento óptico de caracteres para preencher lacunas.

A segmentação utiliza até 320 tokens por trecho e sobreposição de 48 tokens. Tokens são unidades de processamento que podem corresponder a partes de palavras. A sobreposição conserva uma região comum entre trechos vizinhos. A coleção recuperada resulta em 62 trechos. Os registros anteriores permanecem no histórico; os resultados deste artigo utilizam os segmentos das entradas fixadas para a execução atual.

Regras determinísticas associam expressões dos títulos a produtos e expressões do texto a públicos. As ocorrências de público recebem posições de origem. Valores desconhecidos continuam explícitos. Expressões de condição e exceção são catalogadas como candidatos documentais, sujeitos à interpretação de conteúdo. O catálogo público contém rótulos e referências posicionais, com os textos completos preservados no pacote privado.

O filtro principal compara categorias literalmente, sem expandir suas relações hierárquicas. Os metadados dos resultados principais permanecem fixados. A demonstração posterior de uma relação entre categorias recebe registro separado e utiliza um caso já observado. Essa separação conserva a comparação original e torna a intervenção identificável como análise posterior.

### 3.3 Perguntas e referências

Uma família reúne perguntas que dependem da mesma regra. O conjunto piloto contém vinte perguntas de quatorze famílias; o conjunto final contém dez perguntas de dez famílias novas. Cada banco contribui com duas perguntas por classe no piloto e uma por classe no final. As cinco classes são direta, condição, exceção, ambiguidade e insuficiência. A amostra fica abaixo da meta inicial porque a preparação evita multiplicar paráfrases para completar uma quantidade sem ampliar a diversidade das regras.

Codex apoia a preparação das perguntas e dos dossiês antes da geração. Cada dossiê registra ação esperada, requisitos e referências. As âncoras são segmentos curtos identificados por documento, posição e hash. Sua presença mede localização e cobertura do conjunto preparado. Uma avaliação completa das proposições necessárias à resposta depende de examinar a abrangência e a qualidade dessas referências.

Perguntas sem suporte recebem busca lexical em toda a coleção e conferência assistida nas entradas fixadas. A ausência registrada é relativa a essa coleção. Ela não estabelece ausência da informação ou do produto no banco. Perguntas sobre produtos fictícios não encontrados também recebem identificação própria, evitando que o material de avaliação seja interpretado como descrição de serviços reais.

Os campos de produto e público das perguntas incluem termos expressos, normalizações e inferências de domínio preparadas com apoio de Codex. Conta You é associada a pessoa física; análise de crédito, a cartão; segunda via de débito, a conta e pessoa física. A execução não utiliza um extrator de atributos validado em perguntas reais. A auditoria posterior informa essas decisões sem alterar entradas ou rankings. Como a preparação dos campos e a escolha das referências compartilham assistência, o filtro pode ser favorecido por essa dependência.

Todas as famílias do piloto são excluídas do conjunto final. A regra de saques em caixa eletrônico utilizada no teste técnico anterior também é excluída. Benefícios de cartões adicionais e isenção de anuidade do Aeternum constituem famílias distintas no mesmo documento. A separação das regras conserva, portanto, dependência documental residual, considerada na interpretação da amostra e dos intervalos.

### 3.4 Configurações e execução local

O Quadro 1 apresenta as cinco configurações de busca. Todas delimitam os candidatos ao banco informado na pergunta. O enriquecimento modifica a representação usada pelo recuperador. A configuração S, sem documentos, pertence somente à geração complementar e recebe medidas de recuperação não aplicáveis. No módulo de geração, o modelo recebe os textos originais selecionados, identificador, título, endereço e posição, sem os prefixos experimentais. Modelo, precisão e instruções de resposta permanecem iguais entre configurações.

Quadro 1 Configurações de busca documental

| Código | Recuperação | Decisão documental |
|---|---|---|
| A | Busca semântica no trecho original | Sem prefixo adicional |
| B | Busca semântica com prefixo completo | Título, seção, tipo, produto e público |
| C | Busca de B com filtro | Produto e público preparados para a pergunta |
| Bp | Busca semântica com prefixo reduzido | Produto e público |
| L | Busca lexical BM25 | Correspondência de termos |

Fonte: elaboração própria, 2026.

O recuperador é multilingual-e5-large-instruct, executado na unidade central de processamento em precisão de 32 bits. O gerador é Qwen3-8B, na distribuição GGUF Q4_K_M, executada pelo llama.cpp b11557. A quantização compacta a representação dos pesos. Revisões, hashes e versões instaladas integram o registro da execução. O hash identifica os bytes do arquivo e permite conferir alterações, enquanto a validade do conteúdo depende de avaliação específica.

O servidor utiliza contexto de 8.192 tokens, oito threads, lote de 512 e micro-lote de 128. A reorganização interna dos pesos e o cache global de prompts permanecem desativados para o limite de memória do ambiente. O cache da sessão conserva entradas consecutivas. Os registros públicos descrevem as tentativas técnicas anteriores. Respostas parciais dessas tentativas, indisponíveis após a pausa, ficam fora da análise atual.

A entrada admite até 4.096 tokens e a resposta, até 512. A busca registra as dez primeiras posições; o contexto preparado começa com até cinco trechos. Quando a entrada excede seu limite, o executor retira o último trecho e registra a retirada. A geração principal utiliza temperatura zero e penalidade de repetição igual a um. Os controles técnicos não indicam necessidade de penalidade adicional.

O plano de estabilidade utiliza sementes 43 e 44, temperatura 0,7, top_p 0,8 e top_k 20 nas configurações A, B e C. O arredondamento por banco e classe seleciona dez perguntas, correspondentes a 50% do piloto. O orçamento previsto reúne 120 respostas principais e sessenta adicionais, totalizando 180. O conjunto final prevê sessenta respostas principais, cuja geração não foi executada. O executor salva cada combinação e reutiliza registros parciais somente quando entrada, parâmetros e identidade do ambiente de execução correspondem aos anteriores.

### 3.5 Fidelidade e calibração do avaliador

Doze controles sintéticos verificam valores monetários, percentuais, datas e identificadores de fonte. Cada caso utiliza a política principal e as duas sementes de estabilidade, totalizando 36 saídas e 144 itens exigidos. A conferência procura equivalentes explícitos, registra limites de saída e truncamento de entrada e detecta blocos de ao menos vinte tokens repetidos três vezes. Essa verificação avalia a preservação literal dos itens conhecidos em condições delimitadas.

A penalidade de repetição pode alcançar os tokens das evidências. A execução utiliza penalidade neutra e confere os itens nas três políticas de semente. O comportamento da biblioteca Transformers não certifica o comportamento de outro mecanismo de execução. Por essa razão, o registro conserva os parâmetros efetivos do llama.cpp, seu executável e os tokens retornados. Os controles de fidelidade são repetidos na configuração adotada para a execução atual.

A calibração exige pelo menos dezenove acertos em vinte controles e validade estrutural de todas as saídas. O plano admite uma correção de instrução e uma segunda rodada. Os relatórios publicados registram dez acertos na primeira e dezessete na segunda. Os controles abrangem erro numérico, fonte inventada, público incompatível, condição omitida, ambiguidade e falta de evidência. O desempenho da segunda rodada permanece abaixo do limiar e encerra a calibração, com adequação automática desativada nas respostas bancárias.

As calibrações antecedem os ajustes operacionais de memória. A decisão de excluir o avaliador continua válida para a execução atual. As saídas brutas anteriores não foram recuperadas depois da pausa; essa lacuna acompanha os relatórios públicos. O estudo não reabre a escolha do avaliador com base nas respostas bancárias. Também não houve julgamento humano independente, cálculo de concordância entre pessoas ou atribuição de notas semânticas às falhas técnicas.

### 3.6 Medidas de recuperação e incerteza

O recall de âncoras corresponde à proporção de referências presentes nos primeiros três, cinco ou dez trechos. A cobertura indica se pelo menos um conjunto de âncoras definido no dossiê está completo. Perguntas sem referência e a configuração sem documentos recebem valor não aplicável. Cada média apresenta seu denominador. As duas medidas ficam condicionadas à especificação assistida e não são interpretadas como taxa de adequação das respostas.

A análise do filtro registra duas ocorrências: exclusão de trechos que contêm uma referência e ausência de qualquer trecho restante que contenha determinada âncora. A segunda identifica indisponibilidade após a filtragem. O estudo também confere quais âncoras estão nas evidências efetivamente selecionadas para o gerador, depois de eventuais retiradas por orçamento. O ranking e o contexto entregue são preservados separadamente, pois essa retirada pode modificar a disponibilidade final.

Os diagnósticos das respostas registram falha, limite de saída, truncamento, repetição e citações entre colchetes. Um identificador é válido quando pertence às evidências recebidas na entrada. A sustentação da afirmação pelo texto citado exige uma conferência de conteúdo adicional. O módulo parcial contém saídas com sementes distintas, mas sua composição decorre da interrupção; esse subconjunto não sustenta uma estimativa geral de estabilidade.

Os contrastes B menos A e B menos Bp utilizam perguntas de condição e exceção. C menos B utiliza perguntas com atributos preparados, incluindo inferências assistidas. Os intervalos percentis de 95% e 98,33% são obtidos das mesmas cinco mil reamostragens de famílias, estratificadas por banco, com semente 2026. O relatório informa se a estimativa pontual alcança dez pontos percentuais e se sua magnitude absoluta atinge esse valor. Todos os contrastes permanecem exploratórios.

### 3.7 Dimensionamento e registro da execução

O dimensionamento confirmatório do protocolo original utiliza pares discordantes. Os parâmetros são discordância q de 0,25, diferença de interesse Δ de 0,10, poder de 80%, β de 0,20 e nível α* de 0,05 dividido por três. A aproximação da Equação 1 resulta em 258,98 pares e estabelece o limiar de 260 famílias elegíveis de condição e exceção. Esse cálculo pertence ao planejamento anterior e contextualiza a distância entre seu alvo e a amostra aplicada.

$$
n \approx \frac{[z_{1-\alpha^*/2}\sqrt{q}+z_{1-\beta}\sqrt{q-\Delta^2}]^2}{\Delta^2} \tag{1}
$$

O plano alternativo de precisão exige cerca de 97 pares para meia largura de dez pontos em um intervalo normal de 95%, sob independência e discordância de 0,25. Simulações ilustrativas com duas mil repetições examinam discordâncias de 0,10, 0,25 e 0,40. O conjunto final contém quatro famílias de condição e exceção, abaixo dos alvos de poder e de precisão. Os intervalos apresentados descrevem a variabilidade na amostra e não ampliam sua representatividade.

Os rankings dos dois conjuntos são calculados na preparação. As famílias são separadas, com os rankings finais disponíveis desde essa etapa. O método assistido e os hashes são publicados em commit antes do piloto. A decisão posterior de concluir o estudo documental preserva as entradas e registra as 56 gerações como módulo parcial. Essa cronologia impede apresentar a análise como validação externa ou pré-registro confirmatório. Não houve geração final, depósito com DOI ou liberação presumida dessa etapa. Fontes, entradas e respostas salvas permanecem no pacote privado.

## 4 Resultados

### 4.1 Execução e controles

A comparação documental abrange vinte perguntas do piloto e dez do conjunto final, em cinco configurações, totalizando 150 pares. A auditoria confere posições, hashes e vínculos das 43 âncoras com os 62 trechos. A geração complementar conserva 56 respostas do piloto, de uma meta anterior de 180. As sessenta respostas finais previstas não foram geradas. A interrupção determina a composição do subconjunto disponível, que permanece sem uma comparação balanceada de qualidade.

Nos diagnósticos das 56 respostas salvas, não há falha de execução, limite de saída, repetição degenerada ou identificador citado fora das evidências recebidas. Nos 36 controles atuais, os 144 itens exigidos são preservados, sem truncamento ou repetição degenerada. Esses resultados descrevem integridade técnica e preservação literal; a correção semântica das respostas continua sem avaliação validada.

Os relatórios de calibração anteriores registram dez e dezessete acertos em vinte controles, com saídas estruturalmente válidas. O desempenho permanece abaixo do critério de dezenove acertos e mantém a adequação automática desativada. Nenhuma resposta bancária recebe nota atribuída a avaliação humana. Os testes do código verificam também a retomada e a rejeição de controles finais divergentes.

### 4.2 Recuperação das referências

Tabela 1 Recuperação e cobertura de âncoras nas primeiras cinco posições

| Configuração | Recall piloto (16) | Cobertura piloto (16) | Recall final (8) | Cobertura final (8) |
|---|---:|---:|---:|---:|
| A | 90,625% | 87,500% | 87,500% | 87,500% |
| B | 90,625% | 87,500% | 100,000% | 100,000% |
| C | 96,875% | 93,750% | 87,500% | 87,500% |
| Bp | 96,875% | 93,750% | 100,000% | 100,000% |
| L | 93,750% | 93,750% | 100,000% | 100,000% |

Fonte: cálculos sobre os rankings e as referências assistidas publicados no projeto. Os números entre parênteses indicam perguntas elegíveis.

As médias da Tabela 1 incluem dezesseis perguntas elegíveis no piloto e oito no conjunto final. Neste último, B, Bp e L recuperam todas as âncoras nas primeiras cinco posições, enquanto A e C alcançam 87,5%, com perdas em perguntas distintas. A amostra pequena e as referências curtas produzem um teto da medida em três configurações. A interpretação permanece circunscrita a essas referências, sem estabelecer superioridade geral dos modelos ou equivalência entre estratégias de busca.

No piloto, B menos A e B menos Bp apresentam diferença de −12,5 pontos percentuais no recall das oito perguntas de condição e exceção. Os intervalos percentis de 95% e 98,33% variam de −42,86 a zero pontos. C menos B apresenta diferença de 6,25 pontos nas dezesseis perguntas elegíveis. Seu intervalo de 95% vai de zero a 21,43 pontos; o de 98,33%, de zero a 25. Os contrastes de cobertura têm as mesmas estimativas e intervalos.

No conjunto final, B menos A e B menos Bp apresentam diferença zero nas quatro perguntas de condição e exceção e intervalos de zero a zero. Esse resultado decorre da ausência de diferenças observadas nessas perguntas e não demonstra equivalência geral. C menos B apresenta diferença de −12,5 pontos nas oito perguntas elegíveis, com ambos os intervalos entre −37,5 e zero pontos. As diferenças negativas de 12,5 pontos atingem a magnitude de interesse de dez pontos; o ganho de 6,25 permanece abaixo dela. Nenhum contraste fornece apoio confirmatório.

### 4.3 Benefício e perda associados à filtragem

A pergunta B05 examina se a segunda via de um cartão de débito Bradesco perdido integra os serviços essenciais gratuitos. A referência delimita a gratuidade e registra perda como exceção. Nas primeiras cinco posições, B não recupera a âncora e C a recupera. A filtragem utiliza produto conta e público pessoa física, ambos preparados por inferência assistida. Como a pergunta menciona cartão de débito e omite o público, o ganho depende dessa classificação. A preparação dos campos pode favorecer a fonte escolhida no próprio dossiê, o que limita a independência do contraste e impede concluir que os atributos seriam extraídos corretamente de perguntas reais. O caso registra recuperação documental, sem nota semântica para a resposta.

A pergunta BF04 examina se investimentos no Bradesco tornam a anuidade do cartão isenta, sem identificar qual cartão. A, B, Bp e L recuperam as duas âncoras da regra do Aeternum nas primeiras cinco posições. C não recupera nenhuma: a pergunta utiliza a categoria geral cartão e o catálogo registra o produto específico Aeternum. A comparação literal omite a relação entre essas categorias e exclui os trechos previstos no dossiê para apoiar o esclarecimento.

Os casos mostram que o efeito do filtro depende da representação e dos atributos preparados da pergunta. Em B05, a redução de candidatos favorece uma referência. Em BF04, a ausência de hierarquia torna a regra inacessível. A descrição específica do Aeternum pode favorecer a busca por seu produto e requer também a relação com a categoria geral quando participa de um requisito de exclusão. Catalogação e política de seleção, portanto, contribuem conjuntamente para o resultado.

A intervenção posterior acrescenta a relação entre Aeternum e cartão e reaplica a seleção ao ranking congelado de B. As duas âncoras retornam às primeiras cinco posições. Não há geração de novas respostas nem alteração dos resultados principais. A demonstração verifica uma correção no mecanismo identificado para esse caso já observado. Sua generalização exige perguntas e documentos independentes daqueles usados para definir a intervenção.

## 5 Discussão e intervenções na base de conhecimento

Os achados evidenciam duas funções da organização documental que precisam ser avaliadas conjuntamente. A descrição modifica a representação e a posição relativa dos trechos; a filtragem modifica sua disponibilidade. Uma mesma categoria participa dessas funções, com consequências dependentes das relações de pertencimento, do alcance da regra e dos valores desconhecidos. Essa conferência ganha relevância em coleções que combinam regras gerais e produtos especializados.

O caso BF04 identifica um mecanismo específico de perda. O nome Aeternum descreve corretamente o produto, mas sua relação com cartão permanece ausente no requisito de seleção. A intervenção conserva a distinção entre produtos e representa a hierarquia necessária para uma pergunta ampla. O retorno das âncoras demonstra a correção documental nesse ranking. A decisão sobre isenção continua dependendo do cartão e das condições do usuário, de modo que ampliar o acesso às fontes apoia também o pedido de esclarecimento.

O ganho observado em B05 exige outra consideração. O filtro recupera uma referência após utilizar atributos preparados por inferência assistida. Parte do benefício pode depender da correspondência entre esses atributos e a fonte selecionada para o dossiê. O caso sustenta uma análise do mecanismo nessa preparação, com generalização condicionada à validação da classificação em perguntas reais. Examinar referências excluídas, ocorrências preservadas em outros trechos e relações entre categorias oferece critérios verificáveis para decidir quando e como aplicar o filtro.

Os prefixos também apresentam efeitos dependentes da pergunta. No piloto, o prefixo completo perde uma referência que o prefixo reduzido conserva; no conjunto final, ambos atingem o teto da medida. Esse padrão recomenda investigar os componentes da representação e a competição entre trechos. Título, seção e tipo acrescentam contexto, mas podem também deslocar uma informação específica na ordenação. A observação localizada não identifica um efeito geral favorável ou desfavorável do enriquecimento.

Dadopoulos et al. (2025) relatam efeitos de recuperação e geração que variam entre configurações. A leitura desses antecedentes reforça o acompanhamento separado das etapas. Nesta pesquisa, a calibração insuficiente limita a análise à recuperação documental e aos diagnósticos técnicos. A consequência semântica das mudanças de ranking permanece em aberto. Cobertura de âncoras, validade dos identificadores e correção da resposta são dimensões relacionadas, cuja validação exige procedimentos próprios.

O Quadro 2 associa ocorrências a registros e intervenções que o responsável pela base pode examinar. Essas ações cabem à condução individual com assistência técnica: preservar versões, registrar uma relação de categoria e medir novamente a recuperação. A avaliação semântica independente exige outro componente de pesquisa, com método e origem dos julgamentos declarados. A distinção entre correção de um caso conhecido e validação em dados novos acompanha a interpretação de cada intervenção.

Quadro 2 Ocorrências e intervenções documentais

| Ocorrência | Registro utilizado | Intervenção |
|---|---|---|
| Produto específico perde relação com categoria geral | BF04 e trilha de exclusão | Registrar hierarquia e testar seleção ampliada |
| Redução de candidatos favorece referência | B05 e ranking por configuração | Examinar o uso do filtro por classe de pergunta |
| Referência não aparece nas primeiras posições | Âncoras e ranking completo conservado | Rever descrição, segmentação e competição entre trechos |
| Orçamento retira evidências | Lista efetivamente enviada | Reunir regra e condição ou ajustar prioridade |
| Avaliador erra controles conhecidos | Duas calibrações publicadas | Conservar adequação fora das medidas principais |

Fonte: elaboração própria, 2026. A linha sobre orçamento descreve um mecanismo de controle; os registros de contexto efetivo informam se ele ocorreu nesta execução.

A calibração produz uma decisão operacional relevante. Saídas estruturalmente válidas tornam a avaliação processável, embora possam conter rótulos incorretos. O critério registrado mantém a facilidade de processamento e a competência para julgar como aspectos que precisam de conferências próprias. Uma ferramenta abaixo do limiar pode apoiar exploração, com suas notas excluídas das conclusões sobre adequação nessa tarefa.

A disponibilidade das referências permite revisar a preparação. Outros pesquisadores podem contestar uma âncora curta, identificar condições omitidas ou ampliar a coleção. Os rankings públicos permitem repetir os cálculos sem executar modelos. Essa abertura conserva as escolhas metodológicas junto às medidas e oferece uma base concreta para examinar vieses, limites e intervenções, com taxas de acerto vinculadas às entradas que as sustentam.

## 6 Limitações e disponibilidade dos materiais

A amostra é pequena e selecionada por conveniência. Sua cobertura de produtos, canais e públicos das instituições é parcial. As exclusões refletem dificuldades técnicas e o ciclo limitado de coleta. Quatro fontes mudam durante a recuperação, e a execução conserva essa versão. Alterações posteriores nos sites podem produzir outra coleção, cuja coleta exige novos hashes e registro próprio.

Metadados, perguntas e referências compartilham assistência da mesma ferramenta. Essa preparação pode favorecer regras mais fáceis de reconhecer e introduzir dependência entre decisões. O desenho aplicado não estabelece a separação entre equipes independentes prevista no protocolo original. As âncoras curtas medem a localização dos segmentos escolhidos, com cobertura incerta sobre todas as proposições que uma pessoa especialista poderia exigir. Os intervalos ficam condicionados à referência preparada e à amostra observada.

O recuperador local e o gerador quantizado delimitam a implementação examinada. Os controles sintéticos preservam itens conhecidos em contextos específicos, com validade restrita a essas condições. O módulo parcial inclui duas sementes adicionais em algumas entradas e diagnósticos técnicos, sem leitura independente das respostas. Não houve teste de compreensão com leitores, avaliação humana das respostas ou comparação entre anotações de pessoas distintas.

Os relatórios das calibrações anteriores permanecem públicos, mas suas saídas brutas não foram recuperadas após a pausa. Essa lacuna de proveniência acompanha a decisão de manter o avaliador excluído das medidas semânticas atuais. Os arquivos novos, incluindo entradas e respostas, são preservados em pacote privado antes e após as fases. O relato conserva a indisponibilidade dos registros anteriores, sem preencher essa ausência com resultados presumidos.

O GitHub disponibiliza código, perguntas próprias, referências posicionais, hashes, rankings e relatórios derivados. Originais, trechos, índices, prompts e as 56 respostas do módulo parcial permanecem no pacote privado. Os cálculos são reproduzíveis com dados públicos e a biblioteca padrão do Python. Código, dados derivados e instruções estão em https://github.com/yhenriux/rag-bancario-publico. A reprodução da geração depende da versão das fontes, do modelo e do executável; mudanças nesses componentes recebem novos registros.

ChatGPT/Codex apoia a discussão do desenho, pesquisa de fontes, programação, preparação de referências, análise assistida, redação e revisão. Qwen3-8B produz as respostas e participou dos controles de calibração anteriores. E5 gera as representações usadas na recuperação. Código publicado executa os cálculos e os diagnósticos documentais. As ferramentas não assumem autoria. O pesquisador trabalha no Inter; a investigação utiliza apenas fontes públicas e não representa posicionamento institucional. A responsabilidade intelectual e a aprovação de publicação permanecem com o pesquisador.

## 7 Considerações finais

A pesquisa examina como decisões de organização do conhecimento alteram a recuperação de referências em documentação pública de dois bancos brasileiros. A comparação identifica um benefício do filtro condicionado aos atributos preparados e uma perda associada à ausência de relação entre categorias. A intervenção posterior recupera as âncoras no ranking conhecido, com os resultados principais preservados. A contribuição demonstrada é a associação rastreável entre descrição documental, seleção de evidências e uma correção verificável.

Os resultados permanecem restritos à coleção e à preparação assistida. A calibração insuficiente conserva a adequação semântica sem estimativa validada. Os materiais publicados permitem examinar perguntas, contestar referências, reaproveitar controles e repetir os cálculos. Replicar o desenho em outra coleção, testar relações de produto em perguntas novas e calibrar outro avaliador com casos conhecidos são extensões justificadas pelos mecanismos observados.

## Referências

DADOPOULOS, Michail; LADAS, Anestis; MOSCHIDIS, Stratos; NEGKAKIS, Ioannis. **Metadata-Driven Retrieval-Augmented Generation for Financial Question Answering**. arXiv, 2025. Preprint arXiv:2510.24402, versão 1. Disponível em: https://arxiv.org/html/2510.24402v1. Acesso em: 11 out. 2026.

FORD, Daniel. **Introducing Contextual Retrieval**. Anthropic, 19 set. 2024. Disponível em: https://www.anthropic.com/engineering/contextual-retrieval. Acesso em: 11 out. 2026.

INTFLOAT. **multilingual-e5-large-instruct**. Hugging Face, [s. d.]. Modelo, revisão 274baa43b0e13e37fafa6428dbc7938e62e5c439. Disponível em: https://huggingface.co/intfloat/multilingual-e5-large-instruct. Acesso em: 12 out. 2026.

JOREN, Hailey; ZHANG, Jianyi; FERNG, Chun-Sung; JUAN, Da-Cheng; TALY, Ankur; RASHTCHIAN, Cyrus. **Sufficient Context: A New Lens on Retrieval Augmented Generation Systems**. In: INTERNATIONAL CONFERENCE ON LEARNING REPRESENTATIONS, 2025. Artigo. Disponível em: https://research.google/pubs/sufficient-context-a-new-lens-on-retrieval-augmented-generation-systems-2/. Acesso em: 11 out. 2026.

LEWIS, Patrick et al. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**. arXiv, 2020. Preprint arXiv:2005.11401. Disponível em: https://arxiv.org/abs/2005.11401. Acesso em: 11 out. 2026.

QWEN TEAM. **Qwen3-8B-GGUF**. Hugging Face, [s. d.]. Modelo, revisão 7c41481f57cb95916b40956ab2f0b139b296d974. Disponível em: https://huggingface.co/Qwen/Qwen3-8B-GGUF. Acesso em: 12 out. 2026.

WANG, Shuting; TAN, Jiejun; DOU, Zhicheng; WEN, Ji-Rong. OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in Financial Domain. In: CONFERENCE ON EMPIRICAL METHODS IN NATURAL LANGUAGE PROCESSING, 2025, Suzhou. **Proceedings [...]**. Association for Computational Linguistics, 2025. p. 5726–5751. DOI: 10.18653/v1/2025.emnlp-main.292. Disponível em: https://aclanthology.org/2025.emnlp-main.292/. Acesso em: 11 out. 2026.

WILSON, T. D. Models in information behaviour research. **Journal of Documentation**, v. 55, n. 3, p. 249–270, 1999. DOI: 10.1108/EUM0000000007145.
