# Organização do conhecimento em RAG bancário: recuperação de evidências em documentos públicos brasileiros

## Resumo

Este estudo de caso diagnóstico examina como cabeçalhos contextuais e filtros de produto e público alteram a recuperação de evidências bancárias. A coleção reúne 27 páginas públicas de dois bancos brasileiros e 62 trechos, comparados em cinco configurações de busca. Vinte perguntas do piloto e dez de famílias novas no segundo conjunto utilizam âncoras, passagens curtas preparadas como referência com assistência de inteligência artificial. Nas primeiras cinco posições, o filtro recupera a referência em uma das dezesseis perguntas elegíveis do piloto que a busca sem filtro deixa de fora. Em uma das oito perguntas elegíveis do segundo conjunto, exclui as duas âncoras por ausência da relação entre Aeternum e cartão no catálogo. Uma sensibilidade posterior mostra que o ganho depende de campos inferidos. No segundo conjunto, a busca lexical recupera todas as âncoras em três posições. A amostra pequena e a preparação compartilhada limitam a generalização. Os dados permitem diagnosticar ordenação e exclusão de referências, com adequação semântica das respostas fora do alcance avaliado.

Palavras-chave: organização do conhecimento; recuperação da informação; documentação bancária; inteligência artificial; avaliação documental.

## Knowledge organization in banking RAG: evidence retrieval from Brazilian public documents

## Abstract

This diagnostic case study examines how contextual headers and product and audience filters change banking evidence retrieval. The collection contains 27 public pages from two Brazilian banks and 62 passages, compared across five retrieval configurations. Twenty pilot questions and ten questions from new rule families in a second set use anchors, short reference passages prepared with artificial intelligence assistance. Within the first five positions, filtering retrieves the reference for one of sixteen eligible pilot questions where unfiltered retrieval leaves it out. For one of eight eligible questions in the second set, filtering excludes both anchors because the catalogue lacks the relation between Aeternum and the card category. A subsequent sensitivity analysis shows that the gain depends on inferred attributes. In the second set, lexical retrieval finds all anchors within three positions. The small sample and shared preparation limit generalization. The published data support diagnosis of ranking and reference exclusion, while semantic answer adequacy remains outside the evaluated scope.

Keywords: knowledge organization; information retrieval; banking documentation; artificial intelligence; documentary evaluation.

## Organización del conocimiento en RAG bancario: recuperación de evidencias en documentos públicos brasileños

## Resumen

Este estudio de caso diagnóstico examina cómo los encabezados contextuales y los filtros de producto y público modifican la recuperación de evidencias bancarias. La colección reúne 27 páginas públicas de dos bancos brasileños y 62 fragmentos, comparados en cinco configuraciones de búsqueda. Veinte preguntas del piloto y diez de familias nuevas en un segundo conjunto utilizan anclas, pasajes breves de referencia preparados con asistencia de inteligencia artificial. En las primeras cinco posiciones, el filtro recupera la referencia en una de las dieciséis preguntas elegibles del piloto que la búsqueda sin filtro deja fuera. En una de las ocho preguntas elegibles del segundo conjunto, excluye ambas anclas porque el catálogo omite la relación entre Aeternum y tarjeta. Un análisis posterior de sensibilidad muestra que la ganancia depende de atributos inferidos. En el segundo conjunto, la búsqueda léxica recupera todas las anclas en tres posiciones. La muestra pequeña y la preparación compartida limitan la generalización. Los datos permiten diagnosticar ordenación y exclusión de referencias; la adecuación semántica de las respuestas queda fuera del alcance evaluado.

Palabras clave: organización del conocimiento; recuperación de información; documentación bancaria; inteligencia artificial; evaluación documental.

## 1 Introdução

Uma regra bancária pode estar publicada e ainda ser difícil de localizar na situação em que o cliente precisa dela. A documentação combina regras gerais, produtos específicos, condições e exceções. Na geração aumentada por recuperação, conhecida pela sigla RAG, a busca seleciona as evidências que o modelo recebe para elaborar uma resposta. Organizar essa documentação determina tanto a posição dos trechos quanto sua inclusão no conjunto de candidatos. O presente artigo examina essa etapa de recuperação.

A literatura de RAG descreve enriquecimento contextual, busca lexical e semântica, filtragem e avaliação das respostas. A organização do conhecimento oferece conceitos para examinar as relações entre as categorias usadas nessas operações. Um produto específico, como o cartão Aeternum, pode receber seu nome próprio no catálogo e precisar também de um vínculo com a categoria cartão. Quando o catálogo serve de filtro, essa relação interfere diretamente no acesso à evidência. O problema das relações hierárquicas é conhecido; interessa aqui diagnosticar sua manifestação numa implementação de recuperação e documentar como verificar o mecanismo.

A pergunta de pesquisa é: como cabeçalhos contextuais e filtros de produto e público alteram a posição e a cobertura das evidências de referência em uma coleção de documentos bancários públicos brasileiros? A lacuna delimitada pelos trabalhos consultados é a articulação, nesse recorte, entre descrição documental, exclusão de candidatos e diagnóstico por pergunta. O estudo oferece uma análise rastreável desses mecanismos, com referências curtas ligadas às passagens de origem. A seleção bibliográfica é dirigida ao problema, sem pretensão de revisão sistemática ou de demonstrar ausência de estudos sobre o tema.

O desenho aplicado é um estudo de caso diagnóstico, quantitativo e exploratório. Reúne 27 páginas de Inter e Bradesco, 62 trechos, vinte perguntas no piloto e dez em um segundo conjunto de famílias novas. Cinco configurações permitem examinar busca semântica, enriquecimento contextual, filtragem e busca lexical. Perguntas, atributos e referências compartilham preparação assistida por inteligência artificial. Essa dependência delimita a interpretação dos contrastes e motiva uma análise posterior de sensibilidade em dois casos.

O protocolo inicial previa avaliar também respostas geradas. O avaliador automático ficou abaixo do critério de calibração e a geração permaneceu parcial. A decisão de concluir a análise documental ocorreu depois de os rankings dos dois conjuntos e 56 respostas estarem disponíveis. O artigo relata os resultados observados e seus limites; o Apêndice B mantém o planejamento anterior e os registros desse módulo. O público inclui pesquisadores de Ciência da Informação e recuperação da informação, além de profissionais que organizam bases documentais. A contribuição consiste em tornar examinável o caminho entre rótulo, seleção, posição e evidência localizada nesta coleção.

## 2 Organização do conhecimento e avaliação da recuperação

### 2.1 Descrição, categorias e relações

Metadados descrevem documentos ou trechos e ajudam a localizá-los. Título, seção, tipo, produto e público compõem a descrição utilizada no estudo. Os atributos de aplicabilidade delimitam a situação em que uma regra vale, incluindo idade, canal, período, valor e condições de uso. Produto e público integram o filtro; os demais atributos permanecem no texto e nos dossiês de referência. A compatibilidade nesses dois campos cobre, portanto, uma parte da aplicabilidade.

A ISO 25964-1 apresenta recomendações para desenvolver e manter tesauros destinados à recuperação da informação (International Organization for Standardization, 2011). O Simple Knowledge Organization System (SKOS) distingue rótulos de conceitos e permite representar relações entre conceitos mais amplos e mais específicos (Miles; Bechhofer, 2009). Essas referências ajudam a separar o nome de um produto, a categoria à qual pertence e a relação necessária à consulta. O estudo implementa uma seleção literal por rótulos, sem um tesauro formal. A relação Aeternum–cartão recebe uma demonstração posterior no caso em que sua ausência exclui referências.

A política de seleção também precisa lidar com valores desconhecidos. Aqui, um campo não especificado na fonte mantém o candidato, com possível aumento de ruído. Excluir todo registro incompleto poderia retirar regras pertinentes. A escolha expressa uma política de acesso à evidência que deve acompanhar a qualidade do catálogo. Wilson (1999) situa a busca no contexto da necessidade de informação; nesse recorte, perguntas amplas podem exigir identificar o produto antes de decidir se uma condição se aplica. O alcance da consulta a Wilson é informado no Apêndice C.

### 2.2 Recuperação, enriquecimento e domínio financeiro

Lewis et al. (2020) combinam recuperação e geração em tarefas intensivas em conhecimento. A implementação aqui examinada seleciona trechos da coleção fixada; o gerador recebe esses textos e não consulta novos sites. O modelo multilingual-e5-large-instruct pertence à família de representações multilíngues descrita por Wang et al. (2024). BM25 ordena por correspondência de termos, frequência e comprimento dos documentos (Robertson; Zaragoza, 2009). O desempenho relativo depende das consultas e da coleção, o que justifica manter a busca lexical como referência de comparação.

Ford (2024) descreve a inclusão de contexto produzido por modelo antes da indexação e a combinação de busca semântica com BM25. Nesta pesquisa, cabeçalho contextual designa o texto descritivo acrescentado por regras determinísticas ao trecho. Esse cabeçalho se distingue da instrução de consulta exigida pelo recuperador E5. As estratégias semântica e lexical são comparadas separadamente; sua fusão numa busca híbrida permanece uma extensão do desenho.

Dadopoulos et al. (2025) relatam melhora na qualidade das respostas com metadados gerados por modelo, acompanhada de perdas de recuperação em algumas comparações. Também observam queda de recuperação num contraste que combina seleção de arquivos e reescrita da consulta, discutindo restrição excessiva e efeitos da reescrita. Seu filtro opera por arquivo e integra outras alterações. Esse antecedente motiva separar recuperação e geração e examinar perdas por seleção, com cautela para atribuir o efeito a uma única operação.

FinanceBench reúne perguntas sobre empresas com respostas e evidências, permitindo avaliar sistemas de perguntas e respostas financeiras (Islam et al., 2023). Seu domínio difere das páginas de ajuda e de produtos para clientes estudadas aqui. OmniEval combina geração de casos com GPT-4, anotação humana, métricas por regras e avaliadores ajustados para examinar recuperação e geração em finanças (Wang et al., 2025). A existência desses recursos mostra o papel de referências e validação na avaliação financeira; seus resultados não certificam o avaliador local ou as referências desta coleção.

### 2.3 Referências, posição e julgamento

A avaliação em recuperação da informação relaciona coleção, consultas e referências de relevância. Medidas em diferentes cortes do ranking distinguem localizar evidências cedo e recuperá-las em posições posteriores (Manning; Raghavan; Schütze, 2008). Aqui, âncoras são passagens curtas preparadas como referência e identificadas por documento, posição e hash. O recall mede a proporção dessas âncoras localizada; a cobertura verifica se um conjunto previsto no dossiê está completo. A posição da primeira âncora descreve acesso inicial e pode coexistir com outras referências ausentes.

Joren et al. (2025) examinam suficiência do contexto. Suficiência pergunta se há informação bastante para responder; aplicabilidade pergunta se essa informação vale para a pessoa e a situação descritas. A cobertura das âncoras escolhidas neste estudo representa um critério documental do dossiê, cuja suficiência semântica permanece dependente da abrangência dessas referências.

Zheng et al. (2023) descrevem vieses de posição, extensão e favorecimento das próprias respostas em avaliadores baseados em modelos de linguagem. Usar Qwen3-8B para gerar e julgar introduz um risco adicional a examinar; este estudo não estima sua magnitude. A calibração foi executada e ficou abaixo do limiar estabelecido, por isso as notas semânticas foram excluídas. Os diagnósticos técnicos conferem execução e identificadores; julgar preservação de sentido, condições e ação esperada exige outra validação.

A preparação compartilhada de perguntas, atributos e dossiês pode repetir interpretações e favorecer a fonte selecionada como referência. Fixar os arquivos antes da geração protege a cronologia, enquanto uma avaliação independente é necessária para examinar a validade dessas interpretações. A análise posterior de atributos inferidos torna parte dessa dependência visível, sem estabelecer independência retrospectiva.

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

Uma família reúne perguntas que dependem da mesma regra. O conjunto piloto contém vinte perguntas de quatorze famílias; o segundo conjunto contém dez perguntas de dez famílias novas. Cada banco contribui com duas perguntas por classe no piloto e uma por classe no segundo conjunto. As cinco classes são direta, condição, exceção, ambiguidade e insuficiência. A amostra fica abaixo da meta inicial porque a preparação evita multiplicar paráfrases para completar uma quantidade sem ampliar a diversidade das regras.

ChatGPT/Codex apoia a preparação das perguntas e dos dossiês antes da geração. Cada dossiê registra ação esperada, requisitos e referências. As âncoras são segmentos curtos identificados por documento, posição e hash. Sua presença mede localização e cobertura do conjunto preparado. Uma avaliação completa das proposições necessárias à resposta depende de examinar a abrangência e a qualidade dessas referências.

Perguntas sem suporte recebem busca lexical em toda a coleção e conferência assistida nas entradas fixadas. A ausência registrada é relativa a essa coleção. Ela não estabelece ausência da informação ou do produto no banco. Perguntas sobre produtos fictícios não encontrados também recebem identificação própria, evitando que o material de avaliação seja interpretado como descrição de serviços reais.

Os campos de produto e público das perguntas incluem termos expressos, normalizações e inferências de domínio preparadas com apoio de ChatGPT/Codex. Conta You é associada a pessoa física; análise de crédito, a cartão; segunda via de débito, a conta e pessoa física. A execução não utiliza um extrator de atributos validado em perguntas reais. A auditoria posterior informa essas decisões sem alterar entradas ou rankings. Como a preparação dos campos e a escolha das referências compartilham assistência, o filtro pode ser favorecido por essa dependência.

Todas as famílias do piloto são excluídas do segundo conjunto. A regra de saques em caixa eletrônico utilizada no teste técnico anterior também é excluída. Benefícios de cartões adicionais e isenção de anuidade do Aeternum constituem famílias distintas no mesmo documento. A separação das regras conserva, portanto, dependência documental residual, considerada na interpretação da amostra e dos intervalos.

### 3.4 Configurações de recuperação

Todas as configurações restringem os candidatos ao banco indicado na pergunta: dezoito trechos do Inter ou 44 do Bradesco, antes do filtro de produto e público. O Quadro 1 resume as operações. A configuração sem documentos, S, pertence apenas ao módulo complementar de geração e recebe recuperação não aplicável. O cabeçalho altera a representação usada na indexação; os textos originais selecionados, identificadores, títulos, endereços e posições compõem a entrada do gerador, sem o cabeçalho experimental.

Quadro 1 Configurações de busca documental

| Código | Recuperação | Decisão documental |
|---|---|---|
| A | Busca semântica no trecho original | Sem cabeçalho contextual adicional |
| B | Busca semântica com cabeçalho contextual completo | Título, seção, tipo, produto e público |
| C | Busca de B com filtro | Produto e público preparados para a pergunta |
| Bp | Busca semântica com cabeçalho contextual reduzido | Produto e público |
| L | Busca lexical BM25 | Correspondência de termos |

Fonte: elaboração própria, 2026.

O recuperador multilingual-e5-large-instruct é executado na unidade central de processamento em precisão de 32 bits. BM25 utiliza os parâmetros k1 de 1,2 e b de 0,75. A configuração Bp, com descrição reduzida a produto e público, já integra o protocolo original e as entradas fixadas antes da geração do piloto. Ela examina o conjunto adicional de título, seção e tipo presente em B. Suas diferenças não isolam o efeito de cada atributo.

### 3.5 Medidas e análise diagnóstica

O recall de âncoras em um corte k é a quantidade de âncoras distintas localizada nos primeiros k trechos dividida pelo total do dossiê. Âncoras repetidas em trechos sobrepostos contam uma vez. As médias dão o mesmo peso a cada pergunta elegível. A cobertura vale um quando pelo menos um conjunto de âncoras previsto no dossiê está completo e zero nos demais casos. Perguntas sem referência e a configuração S recebem valor não aplicável. A matriz do Apêndice A inclui as trinta perguntas; as médias utilizam dezesseis no piloto e oito no segundo conjunto.

A análise diagnóstica utiliza recall nas posições 1, 3, 5 e 10, a posição de cada âncora nas dez posições publicadas e a média do inverso da posição da primeira âncora, denominada MRR@10. Uma pergunta sem qualquer âncora nesse limite recebe inverso zero; uma pergunta sem referências recebe valor não aplicável. MRR@10 mede o acesso à primeira referência, enquanto recall e cobertura examinam o conjunto. Essa análise é posterior à fixação dos rankings e utiliza os arquivos congelados, com os resultados originais mantidos.

Os contrastes B menos A e B menos Bp abrangem perguntas de condição e exceção. C menos B abrange as perguntas elegíveis com atributos preparados. As contagens indicam em quantas perguntas cada configuração supera a outra e quantas empatam. A apresentação principal usa casos discordantes e medidas descritivas. Os intervalos bootstrap anteriores e o critério de dez pontos percentuais ficam no Apêndice B como histórico analítico, pois a amostra oferece pouca discriminação para inferência.

O diagnóstico distingue excluir um trecho com referência e deixar uma âncora sem qualquer trecho que a contenha. Também confere as evidências selecionadas após eventuais retiradas por orçamento de entrada. O ranking conserva dez posições e o contexto começa com até cinco trechos. Ranking e contexto efetivo são arquivos distintos, permitindo localizar efeitos da seleção e do limite técnico.

A sensibilidade posterior abrange B05 e BF04. Retira somente campos que a auditoria existente classificou como inferência assistida. Em B05, ambos os campos saem e a seleção equivale exatamente a B, sem filtro adicional; em BF04, o campo expresso cartão permanece e a seleção equivale ao C original. Essa regra não exige novo ranking nem extração oportunista a partir das âncoras. Seu alcance é examinar a dependência de dois casos conhecidos, sem substituir os resultados principais ou validar um extrator automático.

### 3.6 Cronologia e módulo complementar

Os rankings dos dois conjuntos são calculados na preparação e ficam disponíveis desde essa etapa. As famílias do piloto são excluídas do segundo conjunto, com dependência documental residual explicitada. O método assistido e os hashes são publicados em commit antes da geração do piloto. O segundo conjunto recebe esse nome no artigo para explicitar seu papel complementar; os arquivos conservam o identificador histórico final. Ele não constitui validação externa ou conjunto cego.

A decisão posterior de concluir o estudo documental mantém 56 respostas como módulo parcial. O avaliador acertou dez e dezessete de vinte controles nas duas rodadas, abaixo do critério de dezenove, e a adequação automática ficou desativada. Não houve julgamento humano independente. O Apêndice B apresenta orçamento, parâmetros, controles, diagnósticos e lacunas de proveniência da geração. As ferramentas de IA utilizadas no método e no texto são declaradas na seção 8.

## 4 Resultados

### 4.1 Recuperação e posição das referências

A comparação reúne trinta perguntas em cinco configurações, totalizando 150 pares. A auditoria confere posições, hashes e vínculos das 43 âncoras com os 62 trechos. As seis perguntas da classe insuficiência ficam na matriz com medidas não aplicáveis. A Tabela 1 acrescenta cortes mais restritos e posição inicial aos resultados em cinco posições.

Tabela 1 Posição e recuperação de âncoras por conjunto

| Conjunto / configuração | Recall@1 | Recall@3 | Recall@5 | Recall@10 | MRR@10 |
|---|---:|---:|---:|---:|---:|
| Piloto / A | 71,9% | 90,6% | 90,6% | 90,6% | 0,844 |
| Piloto / B | 65,6% | 90,6% | 90,6% | 100,0% | 0,812 |
| Piloto / C | 71,9% | 90,6% | 96,9% | 100,0% | 0,849 |
| Piloto / Bp | 65,6% | 90,6% | 96,9% | 96,9% | 0,825 |
| Piloto / L | 62,5% | 93,8% | 93,8% | 100,0% | 0,820 |
| Segundo / A | 75,0% | 87,5% | 87,5% | 100,0% | 0,830 |
| Segundo / B | 62,5% | 100,0% | 100,0% | 100,0% | 0,792 |
| Segundo / C | 50,0% | 87,5% | 87,5% | 87,5% | 0,667 |
| Segundo / Bp | 75,0% | 87,5% | 100,0% | 100,0% | 0,844 |
| Segundo / L | 87,5% | 100,0% | 100,0% | 100,0% | 0,917 |

Fonte: rankings e referências assistidas publicados. Denominadores: dezesseis perguntas no piloto e oito no segundo conjunto. MRR@10 é a média do inverso da posição da primeira âncora no limite de dez trechos.

No piloto, C e Bp alcançam recall@5 de 96,9%; BM25, 93,8%; A e B, 90,6%. Nas dez posições, B, C e L recuperam todas as âncoras, enquanto A mantém 90,6% e Bp alcança 96,9%. No segundo conjunto, B, Bp e L chegam a 100% em cinco posições; A e C ficam em 87,5%. O corte de uma posição distingue as configurações: L obtém 87,5%, A e Bp 75%, B 62,5% e C 50%. L também apresenta a maior MRR@10 nesse conjunto, de 0,917.

A cobertura@5 no piloto é 87,5% para A e B e 93,8% para C, Bp e L; no segundo conjunto coincide com o recall@5 de cada configuração. O Apêndice B mantém a tabela original com valores exatos. Recall é uma média das proporções por pergunta: 90,625%, por exemplo, não deve ser convertido em uma fração de âncoras somadas sem verificar os diferentes denominadores dos dossiês. As casas decimais da Tabela 1 servem à leitura, com valores integrais nos arquivos de cálculo.

### 4.2 Contrastes e casos discordantes

Tabela 2 Perguntas discordantes nas primeiras cinco posições

| Conjunto / contraste | Elegíveis | Primeiro supera | Segundo supera | Empates |
|---|---:|---|---|---:|
| Piloto / B × A | 8 | 0 | 1 (B05) | 7 |
| Piloto / B × Bp | 8 | 0 | 1 (B05) | 7 |
| Piloto / C × B | 16 | 1 (B05) | 0 | 15 |
| Segundo / B × A | 4 | 0 | 0 | 4 |
| Segundo / B × Bp | 4 | 0 | 0 | 4 |
| Segundo / C × B | 8 | 0 | 1 (BF04) | 7 |

Fonte: análise posterior dos rankings congelados. As contagens são iguais para recall@5 e cobertura@5. Primeiro e segundo designam a ordem das configurações no contraste.

B05 e BF04 são os únicos casos em que C e B diferem em recall@5 e cobertura@5 nos respectivos conjuntos. Essa afirmação cobre o corte de cinco posições. No piloto, I08 apresenta ganho de C em recall@1, os recalls de C e B empatam nas posições 3 e 10 e a ordem das listas publicadas difere em dezessete das vinte perguntas. No segundo conjunto, BF04 distingue o recall nos quatro cortes e a ordem difere em nove das dez perguntas. Assim, os dois casos esgotam as diferenças do desfecho em cinco posições, enquanto mudanças de ordenação ocorrem em outras perguntas, inclusive sem referência.

No piloto, B perde para A e Bp em B05 nas oito perguntas de condição e exceção; as demais sete empatam. No segundo conjunto, os quatro pares dessas classes empatam em cada contraste. A contagem de casos informa a base empírica das diferenças. Com oito perguntas, um desfecho binário alterado muda a média em 12,5 pontos percentuais; o critério anterior de dez pontos não distingue um efeito robusto de uma única pergunta.

### 4.3 Filtro, atributos inferidos e relação entre categorias

B05 pergunta: “Perdi meu cartão de débito Bradesco. A segunda via está incluída nos serviços essenciais gratuitos?”. O dossiê utiliza a passagem que delimita a gratuidade e inclui perda entre as exceções. A Resolução nº 3.919, art. 2º, I, b, contextualiza essa distinção para conta de depósitos à vista (Brasil, 2010). A consulta normativa é posterior e serve à discussão; não altera a coleção, as âncoras ou o julgamento do caso. O experimento localiza a referência bancária, sem estimar uma tarifa ou julgar a resposta gerada.

A âncora de B05 aparece na sexta posição de B e na quarta de C. O ganho em cinco posições consiste em trazê-la para o corte de seleção. O filtro utiliza conta e pessoa física, ambos inferidos na preparação da pergunta, que menciona cartão de débito e omite o público. Na sensibilidade que retira esses campos, a seleção volta exatamente ao ranking B e o recall@5 retorna de um a zero. A vantagem depende, portanto, dessa preparação assistida. O caso não sustenta a precisão de extração de atributos em consultas reais.

BF04 pergunta: “Tenho investimentos no Bradesco. Minha anuidade do cartão está isenta?”. A pergunta omite o cartão e exige esclarecimento. A, B, Bp e L localizam as duas âncoras escolhidas sobre Aeternum em cinco posições. C exclui ambas: a pergunta usa cartão e o catálogo usa Aeternum, sem vínculo com a categoria geral. Retirar inferências não modifica esse caso, pois cartão é um termo expresso da pergunta. A falha permanece e identifica uma perda associada à relação ausente na seleção literal.

A intervenção posterior acrescenta Aeternum à categoria cartão e reaplica a seleção ao ranking congelado de B. As duas âncoras retornam às cinco primeiras posições. Esse procedimento verifica o mecanismo num caso conhecido, sem medir ganho em dados independentes. O resultado principal de C permanece intacto; a demonstração aparece separadamente nos arquivos e na discussão.

## 5 Discussão

### 5.1 Alcance dos cabeçalhos e dos filtros

A descrição contextual e o filtro operam em pontos distintos. O cabeçalho altera a representação que ordena trechos; o filtro pode impedir que uma referência entre na lista. B05 localiza uma mudança de posição condicionada a atributos inferidos. BF04 localiza uma exclusão que permanece quando somente os atributos expressos da pergunta são usados. Ambos permitem explicar uma operação concreta, com alcance limitado às referências preparadas e aos casos observados.

A perda em BF04 reencontra um problema conhecido da organização do conhecimento: relacionar uma descrição específica à categoria mais ampla usada na consulta. SKOS e tesauros oferecem meios de explicitar relações de conceitos, enquanto a demonstração executada apenas acrescenta um pertencimento entre produto e categoria. Ela não constitui implantação ou validação de um vocabulário controlado completo. O interesse empírico é tornar visível a consequência de usar um catálogo sem essa relação como requisito de exclusão. O cabeçalho de B também contém Aeternum; em C, o mesmo catálogo participa adicionalmente de uma decisão que exclui o trecho.

Os cabeçalhos apresentam efeitos dependentes da pergunta. Em B05, B perde em cinco posições uma referência que Bp mantém. Nos dez primeiros resultados de B, a referência existe, de modo que sua posição e o corte explicam a perda observada. O contraste B–Bp reúne título, seção e tipo numa ablação conjunta e não identifica qual componente produz o deslocamento. No segundo conjunto, ambos alcançam o teto em cinco posições, mas diferem na primeira e na terceira. Examinar cortes e âncoras por pergunta evita tratar esse teto como equivalência de ordenação.

### 5.2 O que o desempenho do BM25 indica

BM25 é competitivo nessa coleção. No piloto, supera A e B em recall@3 e recall@5, enquanto C e Bp apresentam recall@5 maior. No segundo conjunto, L recupera todas as âncoras já em três posições e apresenta a melhor medida de acesso inicial entre as configurações examinadas. Esses resultados mantêm a busca lexical como alternativa relevante antes de se assumir a necessidade de enriquecimento ou busca semântica.

A coleção oferece dezoito ou 44 candidatos por banco, contém documentação curta de produtos e utiliza perguntas próximas das regras que serviram à sua preparação. A correspondência lexical pode bastar em parte dessas condições. As âncoras curtas e o número pequeno de candidatos também favorecem o teto observado. A análise não mede custo de latência entre estratégias nem permite extrapolar para coleções maiores, termos distantes da fonte ou consultas de clientes coletadas em uso real. A busca híbrida é uma hipótese para outra avaliação, não uma melhoria demonstrada neste estudo.

### 5.3 Intervenções e validade das referências

O Quadro 2 reúne ações que derivam dos diagnósticos ou dos mecanismos de controle. Uma ação corretiva num caso conhecido precisa ser testada depois em novas perguntas e fontes para avaliar sua abrangência. A matriz e as posições individuais permitem também contestar as próprias referências: um trecho pode conter a âncora e ainda omitir informação necessária a uma interpretação completa.

Quadro 2 Diagnósticos e intervenções documentais

| Ocorrência | Registro utilizado | Intervenção |
|---|---|---|
| Produto específico perde relação com categoria geral | BF04 e trilha de exclusão | Registrar hierarquia e testar seleção ampliada |
| Redução de candidatos favorece referência | B05 e ranking por configuração | Examinar o uso do filtro por classe de pergunta |
| Referência não aparece nas primeiras posições | Âncoras e dez posições publicadas | Rever descrição, segmentação e competição entre trechos |
| Orçamento retira evidências | Lista efetivamente enviada | Reunir regra e condição ou ajustar prioridade |
| Avaliador erra controles conhecidos | Duas calibrações publicadas | Manter adequação fora das medidas principais |

Fonte: elaboração própria, 2026. A linha sobre orçamento descreve um mecanismo de controle; os registros de contexto efetivo informam se ele ocorreu nesta execução.



A sensibilidade de B05 explicita a influência dos campos inferidos e oferece uma análise crítica do benefício observado. Ela não resolve a dependência entre perguntas, catálogo e dossiês. Uma extensão justificável é testar uma regra de extração definida antes de novos casos ou acrescentar anotação independente. O uso compartilhado de Qwen3-8B como gerador e avaliador, a calibração abaixo do limiar e a indisponibilidade das saídas brutas anteriores reforçam a necessidade de validação específica da avaliação semântica. Sua exclusão das conclusões impede converter validade estrutural em competência para julgar respostas.

## 6 Limitações e disponibilidade

A coleção foi selecionada por conveniência e cobre parcialmente produtos, canais e públicos de dois bancos. As exclusões expressam dificuldades técnicas e um ciclo limitado de coleta. Quatro das 27 páginas mudaram durante a recuperação; os hashes e os instantâneos privados identificam a versão usada. Uma nova coleta pode produzir outros textos e resultados.

Perguntas, metadados e referências compartilham assistência de ChatGPT/Codex. O desenho aplicado não estabelece a separação entre equipes independentes prevista inicialmente. As âncoras curtas representam as passagens escolhidas, com cobertura incerta sobre todas as proposições que um especialista exigiria. Famílias diferentes podem compartilhar um documento. Os resultados e a sensibilidade permanecem condicionados a essa preparação, à amostra pequena e às dez posições publicadas.

O módulo de geração foi interrompido e não oferece uma comparação balanceada de qualidade. Não houve avaliação humana independente, concordância entre anotadores ou teste de compreensão com leitores. Os controles sintéticos conferem preservação literal em situações delimitadas. A lacuna das saídas brutas anteriores é descrita no Apêndice B, sem preenchimento por dados presumidos.

O GitHub publica código, perguntas próprias, referências posicionais, hashes, rankings e relatórios derivados. Com esses arquivos e a biblioteca padrão do Python, terceiros repetem as métricas a partir dos rankings congelados, inclusive o diagnóstico acrescentado na revisão. Reexecutar a busca original exige os textos, índices, modelos e versões do ambiente. Originais, trechos, índices, prompts e 56 respostas ficam no pacote privado do pesquisador porque a redistribuição não está licenciada. Não houve depósito com DOI. Os materiais públicos estão em https://github.com/yhenriux/rag-bancario-publico.

## 7 Considerações finais

O estudo diagnóstico associa representação documental, seleção de candidatos e localização de referências em uma coleção pública de dois bancos brasileiros. Em cinco posições, o filtro supera a busca sem filtro numa pergunta do piloto e perde numa pergunta do segundo conjunto. A sensibilidade mostra a dependência do ganho em relação aos campos inferidos; a demonstração hierárquica explica a exclusão no caso conhecido. Os cortes mais restritos destacam a competitividade do BM25 e diferenças ocultas pelo teto da medida em cinco posições.

A contribuição é uma análise auditável de mecanismos e referências, com alcance documental. O leitor pode examinar a matriz, contestar âncoras e atributos, repetir os cálculos e reaproveitar o procedimento de diagnóstico em outra coleção. Novas perguntas com preparação independente são necessárias para avaliar generalização das intervenções e correção das respostas geradas.

## 8 Declarações

### 8.1 Conflito de interesses

O pesquisador trabalha no Inter, uma das instituições da coleção. A seleção utiliza os critérios de acesso público, pertinência, versão preservada e extração utilizável da seção 3.1 e inclui Bradesco para comparação documental. O trabalho utiliza apenas fontes públicas, sem documentos internos, dados de clientes ou acesso autenticado, e não representa posicionamento institucional. Essa declaração informa o vínculo e o procedimento de seleção; não estabelece independência externa da preparação.

### 8.2 Uso de inteligência artificial e responsabilidade

ChatGPT/Codex apoia discussão do desenho, pesquisa de fontes, programação, preparação de perguntas e referências, análise assistida, redação e revisão. Qwen3-8B produz as respostas e participou dos controles de calibração anteriores; E5 produz as representações da recuperação. Código publicado calcula as medidas e os diagnósticos. As ferramentas não assumem autoria. A responsabilidade intelectual, a revisão autoral e a aprovação de publicação cabem ao pesquisador. A extensão desse uso é declarada também para a verificação da política editorial do periódico escolhido.

## Referências

BRASIL. Conselho Monetário Nacional. **Resolução nº 3.919, de 25 de novembro de 2010**. Altera e consolida as normas sobre cobrança de tarifas pela prestação de serviços. Texto disponibilizado pelo Banco Central do Brasil. Disponível em: https://www.bcb.gov.br/pre/normativos/res/2010/pdf/res_3919_v4_p.pdf. Acesso em: 12 out. 2026.

DADOPOULOS, Michail; LADAS, Anestis; MOSCHIDIS, Stratos; NEGKAKIS, Ioannis. **Metadata-Driven Retrieval-Augmented Generation for Financial Question Answering**. arXiv, 2025. Preprint arXiv:2510.24402, versão 1. Disponível em: https://arxiv.org/html/2510.24402v1. Acesso em: 11 out. 2026.

FORD, Daniel. **Introducing Contextual Retrieval**. Anthropic, 19 set. 2024. Disponível em: https://www.anthropic.com/engineering/contextual-retrieval. Acesso em: 11 out. 2026.

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO 25964-1:2011: Information and documentation: Thesauri and interoperability with other vocabularies: Part 1: Thesauri for information retrieval**. Geneva: ISO, 2011. Descrição pública do escopo. Disponível em: https://www.iso.org/standard/53657.html. Acesso em: 12 out. 2026.

INTFLOAT. **multilingual-e5-large-instruct**. Hugging Face, [s. d.]. Modelo, revisão 274baa43b0e13e37fafa6428dbc7938e62e5c439. Disponível em: https://huggingface.co/intfloat/multilingual-e5-large-instruct. Acesso em: 12 out. 2026.

ISLAM, Pranab et al. **FinanceBench: A New Benchmark for Financial Question Answering**. arXiv, 2023. Preprint arXiv:2311.11944. Disponível em: https://arxiv.org/abs/2311.11944. Acesso em: 12 out. 2026.

JOREN, Hailey; ZHANG, Jianyi; FERNG, Chun-Sung; JUAN, Da-Cheng; TALY, Ankur; RASHTCHIAN, Cyrus. **Sufficient Context: A New Lens on Retrieval Augmented Generation Systems**. In: INTERNATIONAL CONFERENCE ON LEARNING REPRESENTATIONS, 2025. **Anais [...]**. OpenReview, 2025. Disponível em: https://openreview.net/forum?id=Jjr2Odj8DJ. Acesso em: 12 out. 2026.

LEWIS, Patrick et al. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**. In: **Advances in Neural Information Processing Systems**, v. 33, 2020. Disponível em: https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html. Acesso em: 12 out. 2026.

MANNING, Christopher D.; RAGHAVAN, Prabhakar; SCHÜTZE, Hinrich. **Introduction to Information Retrieval**. Cambridge: Cambridge University Press, 2008. Disponível em: https://nlp.stanford.edu/IR-book/. Acesso em: 12 out. 2026.

MILES, Alistair; BECHHOFER, Sean (ed.). **SKOS Simple Knowledge Organization System Reference**. W3C Recommendation, 18 ago. 2009. Disponível em: https://www.w3.org/TR/skos-reference/. Acesso em: 12 out. 2026.

QWEN TEAM. **Qwen3-8B-GGUF**. Hugging Face, [s. d.]. Modelo, revisão 7c41481f57cb95916b40956ab2f0b139b296d974. Disponível em: https://huggingface.co/Qwen/Qwen3-8B-GGUF. Acesso em: 12 out. 2026.

ROBERTSON, Stephen; ZARAGOZA, Hugo. The Probabilistic Relevance Framework: BM25 and Beyond. **Foundations and Trends in Information Retrieval**, v. 3, n. 4, p. 333–389, 2009. DOI: 10.1561/1500000019. Disponível em: https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf. Acesso em: 12 out. 2026.

WANG, Liang et al. **Multilingual E5 Text Embeddings: A Technical Report**. arXiv, 2024. Preprint arXiv:2402.05672. Disponível em: https://arxiv.org/abs/2402.05672. Acesso em: 12 out. 2026.

WANG, Shuting; TAN, Jiejun; DOU, Zhicheng; WEN, Ji-Rong. OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in Financial Domain. In: CONFERENCE ON EMPIRICAL METHODS IN NATURAL LANGUAGE PROCESSING, 2025, Suzhou. **Proceedings [...]**. Association for Computational Linguistics, 2025. p. 5726–5751. DOI: 10.18653/v1/2025.emnlp-main.292. Disponível em: https://aclanthology.org/2025.emnlp-main.292/. Acesso em: 11 out. 2026.

WILSON, T. D. Models in information behaviour research. **Journal of Documentation**, v. 55, n. 3, p. 249–270, 1999. DOI: 10.1108/EUM0000000007145.

ZHENG, Lianmin et al. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In: **Advances in Neural Information Processing Systems**, v. 36, 2023. Datasets and Benchmarks Track. Disponível em: https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html. Acesso em: 12 out. 2026.

## Apêndice A Matriz pergunta × configuração

A matriz abrange trinta perguntas e cinco configurações. Cada célula contém posição da primeira âncora nas dez posições publicadas, recall@5 e cobertura@5, nessa ordem. NR significa nenhuma âncora recuperada no limite; NA significa pergunta sem referência. Uma âncora pode aparecer na sexta posição e receber recall@5 zero. A posição inicial não certifica suficiência semântica. Os arquivos JSON incluem as posições de cada âncora e os resultados nos quatro cortes.

Tabela A1 Posição inicial, recall e cobertura por pergunta

| Pergunta | A | B | C | Bp | L |
|---|---|---|---|---|---|
| I01 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I02 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 2/1/1 |
| I03 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I04 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I05 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I06 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I07 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I08 | 2/1/1 | 2/1/1 | 1/1/1 | 2/1/1 | 2/1/1 |
| I09 | NA | NA | NA | NA | NA |
| I10 | NA | NA | NA | NA | NA |
| B01 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 |
| B02 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 8/0/0 |
| B03 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 2/1/1 |
| B04 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| B05 | 1/1/1 | 6/0/0 | 4/1/1 | 2/1/1 | 1/1/1 |
| B06 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| B07 | NR/0/0 | 3/1/1 | 3/1/1 | 5/1/1 | 1/1/1 |
| B08 | 2/0,5/0 | 2/0,5/0 | 2/0,5/0 | 2/0,5/0 | 1/1/1 |
| B09 | NA | NA | NA | NA | NA |
| B10 | NA | NA | NA | NA | NA |
| IF01 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| IF02 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| IF03 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| IF04 | 1/1/1 | 2/1/1 | 2/1/1 | 1/1/1 | 1/1/1 |
| IF05 | NA | NA | NA | NA | NA |
| BF01 | 7/0/0 | 3/1/1 | 3/1/1 | 4/1/1 | 3/1/1 |
| BF02 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 | 1/1/1 |
| BF03 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| BF04 | 1/1/1 | 1/1/1 | NR/0/0 | 1/1/1 | 1/1/1 |
| BF05 | NA | NA | NA | NA | NA |

Fonte: análise posterior dos rankings congelados. As perguntas IF e BF pertencem ao segundo conjunto. Valores não arredondados nas células; referências assistidas.

## Apêndice B Método complementar e histórico analítico

Este apêndice mantém o planejamento e os dados que acompanharam a geração parcial e a análise estatística anterior. Esses procedimentos contextualizam o desvio de escopo e não constituem resultados confirmatórios do estudo documental.

### B.1 Ambiente, orçamento e retomada

O recuperador é multilingual-e5-large-instruct, executado na unidade central de processamento em precisão de 32 bits. O gerador é Qwen3-8B, na distribuição GGUF Q4_K_M, executada pelo llama.cpp b11557. A quantização compacta a representação dos pesos. Revisões, hashes e versões instaladas integram o registro da execução. O hash identifica os bytes do arquivo e permite conferir alterações, enquanto a validade do conteúdo depende de avaliação específica.

O servidor utiliza contexto de 8.192 tokens, oito threads, lote de 512 e micro-lote de 128. A reorganização interna dos pesos e o cache global de prompts permanecem desativados para o limite de memória do ambiente. O cache da sessão conserva entradas consecutivas. Os registros públicos descrevem as tentativas técnicas anteriores. Respostas parciais dessas tentativas, indisponíveis após a pausa, ficam fora da análise atual.

A entrada admite até 4.096 tokens e a resposta, até 512. A busca registra as dez primeiras posições; o contexto preparado começa com até cinco trechos. Quando a entrada excede seu limite, o executor retira o último trecho e registra a retirada. A geração principal utiliza temperatura zero e penalidade de repetição igual a um. Os controles técnicos não indicam necessidade de penalidade adicional.

O plano de estabilidade utiliza sementes 43 e 44, temperatura 0,7, top_p 0,8 e top_k 20 nas configurações A, B e C. O arredondamento por banco e classe seleciona dez perguntas, correspondentes a 50% do piloto. O orçamento previsto reúne 120 respostas principais e sessenta adicionais, totalizando 180. O segundo conjunto prevê sessenta respostas principais, cuja geração não foi executada. O executor salva cada combinação e reutiliza registros parciais somente quando entrada, parâmetros e identidade do ambiente de execução correspondem aos anteriores.

### B.2 Fidelidade, calibração e proveniência

Doze controles sintéticos verificam valores monetários, percentuais, datas e identificadores de fonte. Cada caso utiliza a política principal e as duas sementes de estabilidade, totalizando 36 saídas e 144 itens exigidos. A conferência procura equivalentes explícitos, registra limites de saída e truncamento de entrada e detecta blocos de ao menos vinte tokens repetidos três vezes. Essa verificação avalia a preservação literal dos itens conhecidos em condições delimitadas.

A penalidade de repetição pode alcançar os tokens das evidências. A execução utiliza penalidade neutra e confere os itens nas três políticas de semente. O comportamento da biblioteca Transformers não certifica o comportamento de outro mecanismo de execução. Por essa razão, o registro conserva os parâmetros efetivos do llama.cpp, seu executável e os tokens retornados. Os controles de fidelidade são repetidos na configuração adotada para a execução atual.

A calibração exige pelo menos dezenove acertos em vinte controles e validade estrutural de todas as saídas. O plano admite uma correção de instrução e uma segunda rodada. Os relatórios publicados registram dez acertos na primeira e dezessete na segunda. Os controles abrangem erro numérico, fonte inventada, público incompatível, condição omitida, ambiguidade e falta de evidência. O desempenho da segunda rodada permanece abaixo do limiar e encerra a calibração, com adequação automática desativada nas respostas bancárias.

As calibrações antecedem os ajustes operacionais de memória. A decisão de excluir o avaliador continua válida para a execução atual. As saídas brutas anteriores não foram recuperadas depois da pausa; essa lacuna acompanha os relatórios públicos. O estudo não reabre a escolha do avaliador com base nas respostas bancárias. Também não houve julgamento humano independente, cálculo de concordância entre pessoas ou atribuição de notas semânticas às falhas técnicas.

A geração conserva 56 respostas do piloto, de uma meta de 180; as sessenta previstas para o segundo conjunto não foram geradas. A interrupção determina a composição do subconjunto.

Nos diagnósticos das 56 respostas salvas, não há falha de execução, limite de saída, repetição degenerada ou identificador citado fora das evidências recebidas. Nos 36 controles atuais, os 144 itens exigidos são preservados, sem truncamento ou repetição degenerada. Esses resultados descrevem integridade técnica e preservação literal; a correção semântica das respostas continua sem avaliação validada.

Os testes do código verificam a retomada e a rejeição de controles finais divergentes. Os relatórios de calibração e os registros técnicos permanecem públicos.

Os diagnósticos das respostas conferem falha, limite de saída, truncamento, repetição e citações entre colchetes. Um identificador válido pertence às evidências da entrada; sua validade não demonstra sustentação da afirmação. O subconjunto interrompido inclui sementes distintas em algumas entradas, sem composição que sustente uma estimativa geral de estabilidade. Respostas bancárias não recebem notas atribuídas a julgamento humano.

### B.3 Dimensionamento e intervalos anteriores

O dimensionamento confirmatório do protocolo original utiliza pares discordantes. Os parâmetros são discordância q de 0,25, diferença de interesse Δ de 0,10, poder de 80%, β de 0,20 e nível α* de 0,05 dividido por três. A aproximação da Equação 1 resulta em 258,98 pares e estabelece o limiar de 260 famílias elegíveis de condição e exceção. Esse cálculo pertence ao planejamento anterior e contextualiza a distância entre seu alvo e a amostra aplicada.

$$
n \approx \frac{[z_{1-\alpha^*/2}\sqrt{q}+z_{1-\beta}\sqrt{q-\Delta^2}]^2}{\Delta^2} \tag{1}
$$

O plano alternativo de precisão exige cerca de 97 pares para meia largura de dez pontos em um intervalo normal de 95%, sob independência e discordância de 0,25. Simulações ilustrativas com duas mil repetições examinam discordâncias de 0,10, 0,25 e 0,40. O segundo conjunto contém quatro famílias de condição e exceção, abaixo dos alvos de poder e de precisão. Os intervalos apresentados descrevem a variabilidade na amostra e não ampliam sua representatividade.

Os contrastes B menos A e B menos Bp utilizam perguntas de condição e exceção. C menos B utiliza perguntas com atributos preparados, incluindo inferências assistidas. Os intervalos percentis de 95% e 98,33% são obtidos das mesmas cinco mil reamostragens de famílias, estratificadas por banco, com semente 2026. O relatório informa se a estimativa pontual alcança dez pontos percentuais e se sua magnitude absoluta atinge esse valor. Todos os contrastes permanecem exploratórios.

Tabela B1 Recuperação e cobertura de âncoras nas primeiras cinco posições

| Configuração | Recall piloto (16) | Cobertura piloto (16) | Recall segundo (8) | Cobertura segundo (8) |
|---|---:|---:|---:|---:|
| A | 90,625% | 87,500% | 87,500% | 87,500% |
| B | 90,625% | 87,500% | 100,000% | 100,000% |
| C | 96,875% | 93,750% | 87,500% | 87,500% |
| Bp | 96,875% | 93,750% | 100,000% | 100,000% |
| L | 93,750% | 93,750% | 100,000% | 100,000% |

Fonte: cálculos sobre os rankings e as referências assistidas publicados no projeto. Os números entre parênteses indicam perguntas elegíveis.



No piloto, B menos A e B menos Bp apresentam diferença de −12,5 pontos percentuais no recall das oito perguntas de condição e exceção. Os intervalos percentis de 95% e 98,33% variam de −42,86 a zero pontos. C menos B apresenta diferença de 6,25 pontos nas dezesseis perguntas elegíveis. Seu intervalo de 95% vai de zero a 21,43 pontos; o de 98,33%, de zero a 25. Os contrastes de cobertura têm as mesmas estimativas e intervalos.

No segundo conjunto, B menos A e B menos Bp apresentam diferença zero nas quatro perguntas de condição e exceção e intervalos de zero a zero. Esse resultado decorre da ausência de diferenças observadas nessas perguntas e não demonstra equivalência geral. C menos B apresenta diferença de −12,5 pontos nas oito perguntas elegíveis, com ambos os intervalos entre −37,5 e zero pontos. O critério histórico de dez pontos identifica mecanicamente as diferenças negativas de 12,5 e deixa o ganho de 6,25 abaixo do limiar. Nesta amostra, essa classificação não define relevância empírica ou apoio confirmatório.

Os intervalos são percentis das reamostragens das famílias observadas. Na amostra pequena, uma única família discordante pode ficar ausente de uma repetição e produzir limite zero. Intervalos de zero a zero surgem quando os pares observados empatam; não demonstram equivalência populacional. O artigo prioriza contagens e diagnóstico por pergunta. As cinco mil reamostragens, com semente 2026 e estratificação por banco, permanecem nos relatórios públicos para reproduzir a análise histórica.

## Apêndice C Alcance da verificação bibliográfica

A consulta limitada ao resumo e aos dados bibliográficos refere-se especificamente a Wilson (1999). Dadopoulos et al. (2025) foi consultado em texto completo, com atenção ao método e às comparações de recuperação e geração. A referência à ISO 25964-1 utiliza a descrição pública do escopo da norma; o texto integral da norma não foi acessado. SKOS é usado como referência conceitual, sem declaração de conformidade da implementação.

As versões publicadas de Lewis et al. (2020) e Joren et al. (2025) são identificadas como anais. O endereço de OpenReview de Joren foi identificado, mas seu acesso direto encontrou verificação de navegador; a versão dos autores no arXiv informa, na primeira página, publicação na ICLR 2025. A página definitiva de OmniEval informa 5726–5751, mantidos nesta versão. A página de Contextual Retrieval atribui pesquisa e escrita a Daniel Ford; o endereço de engenharia é o adotado. Fontes bibliográficas e decisões de conferência constam da resposta ao parecer no repositório.
