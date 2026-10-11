# Plano de pré-registro para avaliação da informação bancária recuperada

Data de preparação: 10 de outubro de 2026.
Status: coleta experimental, piloto, experimento e julgamentos ainda não executados. Depósito público pendente; não há DOI, registro público ou aprovação autoral definitiva. O texto integral abaixo fixa as regras prospectivas desta versão do protocolo.

## Objetivo e contrastes

Avaliar efeitos do enriquecimento contextual dos trechos e da filtragem por produto e público sobre recuperação de evidências e adequação de respostas sobre contas e cartões de três bancos brasileiros. H1 compara B com A e H3 compara B com Bp nas classes condição e exceção. H2 compara C com B nas perguntas com atributo de filtragem explícito e codificável. Adequação binária é o desfecho principal por contraste. Aplicabilidade em atributos filtrados e não filtrados, cobertura e exclusão indevida descrevem os mecanismos. Comparações com L e S, estabilidade e sensibilidade são exploratórias. As seis configurações e parâmetros constam dos Quadros 2 e 3.

## Regras que antecedem a execução

- Seleção dos bancos: operações no Brasil, conta e cartão para pessoa física e documentação oficial pública em português, buscando variedade entre atendimento físico e digital e organização documental. Exclusões, todos os candidatos e justificativas são registrados. Permissões e termos de uso são conferidos no início da coleta; autorizações necessárias indeterminadas mantêm fontes pendentes (seção 4.1).
- Famílias documentais: perguntas com regra e evidência indispensável compartilhadas são agrupadas antes da execução. Perguntas e famílias do piloto, inclusive paráfrases e dependências das mesmas regras, ficam fora do estudo final (seções 4.1 e 4.3).
- Seis pessoas, ainda a recrutar, ocupam papéis distintos: M1 e M2 anotam metadados; R1 e R2 constroem dossiês nas fontes originais sem acesso às anotações de M ou às saídas do sistema; J1 e J2 julgam em ordem aleatória, cegos à configuração e à semente. Nenhum modelo de linguagem atua como juiz (seções 4.2 e 5.2).
- Concordância antes da conciliação: acordo exato e kappa nominal sem ponderação em M por atributo, em R para classe, respondibilidade e atributos indispensáveis e em J para categorias nominais da rubrica. Valores múltiplos de M são conjuntos normalizados; R inclui Jaccard entre conjuntos de unidades de evidência identificadas por documento e localização. Denominadores, frequências e julgamentos originais são preservados (seções 4.2 e 5.2).
- O filtro aceita correspondências explícitas, conjuntos compatíveis, alcance geral documentado e metadados desconhecidos. Ausência de atributo de filtragem expresso conserva a seleção de B. Os dois casos trabalhados são inteiramente fictícios (seções 4.4 e 5.2).
- Repetição degenerada: sequência de pelo menos vinte tokens repetida três vezes consecutivas em qualquer saída do piloto aciona RepetitionPenaltyLogitsProcessor com penalidade 1,05 e prompt_ignore_length igual ao comprimento completo da entrada tokenizada. O parâmetro global repetition_penalty permanece 1,0. Transformers 4.57.1 é a implementação inicial, com comportamento confirmado na documentação e novamente verificado no ambiente do piloto. O ajuste vale uniformemente para as seis configurações e a estabilidade. Doze casos fictícios congelados com valores, unidades, datas e identificadores geram 72 saídas antes e depois do ajuste, considerando geração sem amostragem e duas sementes. J1/J2 fazem até 144 conferências técnicas adicionais, cegos à política e à semente. Qualquer perda de item anteriormente preservado, persistência da degeneração ou incompatibilidade da implementação impede aceitar o ajuste e suspende a execução final até revisão registrada, antes dos escores de adequação (seção 4.5).

## Dimensionamento e orçamento

O piloto prevê sessenta perguntas, cinco classes e três bancos, com 720 julgamentos principais e 180 de estabilidade: total de 900, além de 120 anotações iniciais de dossiês e trabalho de metadados, preparação e conciliação. No cenário ilustrativo de 660 perguntas, são 44 por banco e classe e 264 nas classes condição e exceção. Estas ultrapassam o limiar somente se representarem famílias distintas elegíveis, após excluir o piloto. São 7.920 julgamentos principais e 1.980 adicionais, total de 9.900 e 495 horas a três minutos por julgamento, além de verificações técnicas, preparação, metadados e conciliação. Quantidade e duração são hipóteses de planejamento; o piloto informa o orçamento definitivo (seção 4.5).

Para pares independentes, a fórmula da seção 5.3 fornece n≈258,98 com q=0,25, Δ=0,10, α*=0,05/3 e poder de 80%. O limiar conservador é 260 famílias elegíveis por contraste. A equivalência exige uma pergunta por família. H1 e H3 precisam dessa quantidade nas classes condição e exceção em conjunto, após excluir o piloto.

Menos de 260 famílias elegíveis por contraste determina análise exploratória. Atingir o limiar também exige simulação de poder que preserve dependência intrafamília e composição por banco e classe; o piloto pode elevar o mínimo. Na inviabilidade, o alvo passa à precisão: intervalo de 95% da diferença de adequação com meia largura até dez pontos percentuais, como objetivo de planejamento. A aproximação conservadora sob diferença nula exige 97 pares independentes com q=0,25 e meia largura h=0,10; a dependência entre perguntas exige simulação. Amostra, orçamento, famílias e decisão são fixados antes de gerar resultados finais, sem extensão após conhecer o efeito.

Análises exploratórias usam intervalos percentis com 5.000 reamostragens de famílias dentro de cada banco, preservando perguntas e pares e os bancos como estratos fixos. Os intervalos de 95% usam quantis 0,025 e 0,975 da distribuição reamostrada; os de 98,33% usam 0,008333 e 0,991667, com interpolação linear. Eventual confirmação utiliza Bonferroni nos três contrastes; apoio exige limite inferior ajustado maior que zero. O relato informa separadamente se a estimativa pontual alcança dez pontos percentuais. Intervalos de 95% são descritivos. Estratos pequenos, famílias disponíveis e incerteza são reportados (seção 5.3).

## Congelamento e depósito pendentes

- Confirmar autoria, contribuições, aprovação e enquadramento institucional da avaliação humana.
- Identificar os bancos e inventariar fontes, permissões, produtos, período e candidatos excluídos.
- Selecionar as seis pessoas, treinar equipes e executar o piloto.
- Congelar famílias reservadas, perguntas, denominadores elegíveis, amostra, orçamento e decisão por contraste.
- Congelar instruções completas, revisões dos modelos, bibliotecas, segmentadores, ambiente, arredondamento da estabilidade e tratamento de falhas técnicas ou avaliações incompletas antes da geração final.
- Registrar mudanças do piloto e depositar o plano antes da coleta final, com identificação persistente; incorporar endereço ou DOI ao manuscrito e às Notas da Obra somente após depósito real.
- Definir licença e materiais compartilháveis segundo os direitos das fontes.

Uma comparação posterior com prefixos gerados por modelo constitui extensão com protocolo e orçamento próprios. Metadados manuais fornecem referência sob curadoria intensiva; sua interpretação como teto prático exige comparação direta (seção 6).

O hash identifica o conteúdo preparado. Data local e hash, isoladamente, não certificam anterioridade pública; esta depende do depósito datado em repositório, como OSF ou Zenodo.

## Identificação dos arquivos desta versão

- Manuscrito_RAG_Bancario_Protocolo.docx: 803472 bytes; SHA-256 `99867b9ef4505ba76c030ed67b374bf18db8387a70b07726ac68eaae9cc96195`.
- Notas_da_Obra_MOCI_Minuta.docx: 110451 bytes; SHA-256 `ed9373536be6e18ed938a84f08982cc097338e6c5d06f487e231be40701172a7`.
- Manuscrito_RAG_Bancario_Protocolo.pdf: 340467 bytes; SHA-256 `ab1981215e61213b53fd64890bcc6faec687b159295d1b9182940eea9f2945bb`.

## Texto integral do protocolo para preservação da versão

# Quando a informação recuperada se aplica? Protocolo para serviços bancários brasileiros

## 1 Introdução

Uma resposta sobre anuidade pode apontar para a página correta de um cartão e omitir o gasto mínimo que concede a isenção. Para quem mantém uma base de conhecimento, o problema envolve duas decisões: selecionar uma evidência que corresponda à situação descrita e preservar os requisitos da regra ao redigir a resposta. Produto, público, elegibilidade, canal e período podem modificar o que uma informação permite afirmar. A qualidade do serviço depende desse encadeamento entre representação documental, recuperação e uso da evidência.

A geração aumentada por recuperação, conhecida pela expressão inglesa retrieval-augmented generation (RAG), combina busca em uma coleção com produção de respostas por um modelo de linguagem (Lewis et al., 2020). O acesso a documentos permite localizar a origem das afirmações, mas a presença de uma citação, isoladamente, informa pouco sobre a adequação da resposta à pergunta. Este protocolo aproxima a avaliação técnica de uma tarefa familiar à Ciência da Informação: decidir quando a informação recuperada serve à necessidade expressa pelo usuário.

O objetivo é avaliar como o enriquecimento contextual dos trechos e a filtragem por produto e público afetam a recuperação de evidências e a adequação das respostas sobre contas e cartões de três bancos brasileiros. A aplicabilidade é medida contra a situação descrita na pergunta, representada em um dossiê: registro de referência que reúne os atributos necessários, os requisitos da resposta e as evidências documentais suficientes. Uma resposta adequada deve preservar esses requisitos ou realizar o esclarecimento ou a abstenção previstos para a pergunta.

O artigo apresenta um protocolo prospectivo, com piloto e estudo final ainda pendentes. A análise é exploratória em contrastes com menos de 260 famílias elegíveis, conforme o dimensionamento da seção 5.3; eventual confirmação exige também dimensionamento por simulação e recursos para a avaliação humana. Publicar o desenho antes dos resultados torna verificáveis as decisões sobre tarefas, comparações e critérios de avaliação, além de permitir sua discussão antes de uma coleta custosa. O protocolo prevê registro público do plano, com data e resumo criptográfico, antes da coleta final.

A contribuição é medir, na mesma comparação, se a evidência serve à pergunta, se a resposta preserva as condições da regra e o que a seleção documental perdeu no caminho. O produto previsto é uma matriz de interpretação para profissionais que organizam e mantêm bases de conhecimento. Ela relaciona mudanças na representação documental a ganhos, perdas e falhas que exigem intervenções diferentes.

## 2 Relevância, organização do conhecimento e recuperação

### 2.1 Da relevância à aplicabilidade

A relevância possui uma história conceitual extensa na Ciência da Informação (Mizzaro, 1997). Wilson (1973) formula a relevância situacional; Schamber, Eisenberg e Nilan (1990) enfatizam seu caráter dinâmico e situado. Cosijn e Ingwersen (2000) distinguem dimensões de relevância, e Saracevic (2007) relaciona suas manifestações a diferentes níveis da interação informacional. Essas contribuições permitem examinar a relação entre um documento e a situação para a qual ele será utilizado, além da proximidade temática entre texto e pergunta.

A perspectiva sociocognitiva associa necessidades e critérios de relevância às práticas e aos pressupostos dos domínios (Hjørland, 2002). Em serviços bancários, a expressão “isenção de anuidade” pode remeter a regras distintas conforme modalidade e elegibilidade. O estudo traduz essa relação em requisitos verificáveis no dossiê. A avaliação considera tanto a presença de evidência compatível quanto o tratamento das condições que delimitam sua aplicação.

Aplicabilidade designa a compatibilidade da evidência ou da afirmação com os atributos indispensáveis à pergunta. Adequação designa o atendimento integral aos requisitos do dossiê pela resposta. Uma evidência pode corresponder ao produto consultado e conter uma exceção que a resposta omitiu. Essa distinção permite localizar a falha na seleção ou no uso da informação, com implicações diferentes para a manutenção da base.

### 2.2 Representação documental orientada ao domínio

A análise de domínio oferece meios para relacionar a organização documental às práticas e às necessidades de uma comunidade (Hjørland, 2017). A classificação facetada permite combinar dimensões de representação conforme a busca (Broughton, 2006). No protocolo, essa fundamentação orienta a escolha de dimensões descritivas, como produto, público, elegibilidade, canal e vigência, a partir das regras encontradas nos documentos.

O vocabulário operacional distingue metadados, que são a descrição estruturada de documentos e trechos, de atributos, que são as características representadas nessa descrição ou exigidas pela pergunta. A organização facetada constitui a fundamentação para combinar dimensões; sua implementação corresponde a um esquema explícito de metadados. Valores desconhecidos e documentos de alcance geral recebem categorias próprias, acompanhadas de evidência e justificativa, para evitar inferências silenciosas de compatibilidade.

Essa representação serve a dois usos experimentais. O enriquecimento contextual acrescenta uma descrição ao texto indexado. A filtragem restringe candidatos por atributos expressos na pergunta. O primeiro uso altera a representação para busca; o segundo altera o conjunto elegível. Compará-los separadamente examina se aproximar o assunto da pergunta preserva as regras necessárias para respondê-la.

### 2.3 Enriquecimento e suficiência da evidência

O enriquecimento contextual já integra propostas de recuperação. Ford (2024), em documentação técnica da Anthropic, descreve a técnica Contextual Retrieval: um modelo produz um contexto breve para cada trecho antes da indexação semântica e lexical, com opções de combinação e reordenação dos resultados. O presente protocolo utiliza descrições manuais estruturadas. Assim, a técnica industrial fornece um antecedente relevante, enquanto a comparação aqui proposta examina um procedimento documental específico e auditável.

Dadopoulos et al. (2025, seção 3.4.2) investigam seleção de arquivos por um modelo, reescrita da consulta e busca restrita aos arquivos selecionados, além de enriquecimento e reordenação em perguntas financeiras. O trabalho encontra-se em preprint e constitui antecedente direto do desenho. Wang et al. (2025) apresentam o OmniEval, com diversidade de tarefas financeiras e avaliação de etapas do processo. Es et al. (2024) propõem o Retrieval Augmented Generation Assessment (RAGAs) para avaliar componentes de sistemas de geração aumentada por recuperação. Esses trabalhos apoiam a decomposição da avaliação em recuperação, evidência e resposta.

Em comparações entre trechos originais e contextualizados, Dadopoulos et al. (2025, seção 4.2.2) relatam aumento do F1 das respostas em todos os pares avaliados, acompanhado de queda na recuperação de afirmações em algumas configurações. A combinação de seleção de arquivos e reescrita também reduz essa recuperação; os autores apontam reformulação inadequada e restrição excessiva como explicações possíveis (seção 4.2.3). Esses achados fundamentam a expectativa de H1 e o exame conjunto de benefícios e perdas em H2. O antecedente usa metadados gerados por modelo e filtragem por arquivo, combinada com reescrita, enquanto o presente protocolo isola a filtragem por produto e público sob curadoria manual. A diferença de tarefas e intervenções delimita a comparação entre os estudos.

Joren et al. (2025) examinam a suficiência do contexto para responder e distinguem limitações da informação disponível de falhas no seu uso pelo modelo. A suficiência considera se o contexto contém informação bastante para responder; a aplicabilidade examina se essa informação vale para a situação de quem perguntou, tal como descrita no enunciado. Liu et al. (2024) demonstram que a posição da informação no contexto também afeta sua utilização. Essas contribuições orientam a distinção entre ausência de evidência na coleção, recuperação incompleta e resposta inadequada apesar de evidência suficiente.

Permanece por testar, nas tarefas bancárias brasileiras selecionadas, se a compatibilidade obtida pela filtragem de produto e público se estende à elegibilidade, ao canal e ao período exigidos pela pergunta. Essa é a questão empírica do protocolo. A avaliação separada dos atributos filtrados e não filtrados, com referências produzidas por uma equipe independente, torna observável o alcance dos ganhos documentais.

## 3 Hipóteses e critérios de interpretação

O Quadro 1 fixa os contrastes e as perguntas elegíveis para cada hipótese. A adequação binária é o desfecho principal de cada contraste, calculado na população de perguntas à qual a hipótese se refere. As outras medidas ajudam a interpretar o mecanismo. A média global das tarefas constitui um resultado secundário, dependente da composição intencional da amostra.

| Hipótese | Contraste | Perguntas elegíveis | Desfecho | Interpretação prevista |
|---|---|---|---|---|
| H1 | B × A | Classes condição e exceção | Adequação | Ganho de B favorece H1. Recuperação melhor com adequação estável sugere limite no uso da evidência. |
| H2 | C × B | Perguntas com produto ou público explícito e codificável | Adequação; exclusão indevida e cobertura como diagnósticos | Ganho de adequação em C favorece H2. Exclusões e cobertura indicam seu custo documental. Compatibilidade maior com cobertura menor caracteriza uma troca. |
| H3 | B × Bp | Classes condição e exceção | Adequação | Ganho de B favorece H3 e indica utilidade do conjunto adicional de descrição. |

Quadro 1. Hipóteses, contrastes e populações de análise.

Fonte: elaboração própria.

Diferenças nulas ou negativas não oferecem apoio direcional às hipóteses. Intervalos amplos são interpretados como inconclusivos; ausência de significância, por si só, não demonstra igualdade. A análise confirmatória, se dimensionada e registrada, utiliza os critérios da seção 5.3. O contraste B × Bp examina um conjunto de atributos adicionais e sua interação, com interpretação conjunta.

## 4 Desenho e procedimentos

### 4.1 Coleção e unidade de dependência

A seleção intencional inclui três bancos com operações no Brasil, oferta de conta e cartão para pessoa física e documentação oficial pública em português. A seleção busca variedade entre atendimento físico e digital e formas de organização documental. São excluídos candidatos sem documentação identificável dos dois produtos, com acesso dependente de autenticação ou com restrições incompatíveis com a coleta prevista. Um inventário registra todos os candidatos, a decisão de inclusão ou exclusão e sua justificativa. A escolha ocorre antes de avaliar as configurações.

A coleta começa pela conferência das permissões e dos termos de uso de cada fonte. O registro conserva endereço dos termos, data da consulta, condições de coleta e uso e decisão sobre inclusão. Fontes cuja autorização necessária permaneça indeterminada ficam pendentes até esclarecimento. A coleção é organizada por banco, de modo que todas as configurações compartilhem o mesmo conjunto de candidatos nas perguntas sobre cada instituição.

Um instantâneo é uma cópia datada da coleção utilizada no experimento. Seu inventário conserva endereço eletrônico, identificação documental, data da coleta, data de publicação quando disponível, vigência declarada e resumo criptográfico do arquivo. Data de coleta e vigência são registradas separadamente. Documentos conflitantes, descontinuados ou sem indicação temporal recebem marcação explícita; a respondibilidade depende da evidência que o instantâneo efetivamente contém.

Uma família documental reúne perguntas que dependem da mesma regra e de evidências compartilhadas, ainda que essas evidências estejam distribuídas em vários documentos. Essa unidade representa dependência informacional, sem se reduzir ao endereço de uma página. As famílias são definidas e congeladas antes das execuções, conservando justificativas e vínculos entre perguntas, regras e documentos. Perguntas que compartilham evidência indispensável pertencem à mesma família; dúvidas de agrupamento são resolvidas antes da análise.

### 4.2 Metadados e independência das equipes

A segmentação preserva título, seção, cabeçalhos de tabelas, notas e vínculos entre regra e exceção. Dois anotadores da equipe de metadados, M1 e M2, descrevem os trechos independentemente. O esquema inclui tipo documental, produto, público, elegibilidade, canal e informação temporal, com evidência textual para cada valor. As divergências são conciliadas após a conservação dos julgamentos originais.

Uma equipe distinta, R1 e R2, constrói os dossiês diretamente a partir das perguntas e dos documentos originais, sem acesso às anotações de metadados nem às saídas do sistema. Dois outros avaliadores, J1 e J2, julgam as respostas após o congelamento dos dossiês. O desenho prevê seis pessoas com papéis distintos, ainda a recrutar para a execução.

A concordância de M1 e M2 é reportada antes da conciliação, por atributo, com acordo exato e kappa sem ponderação para valores nominais. Valores múltiplos são tratados como conjuntos normalizados, com acordo por igualdade do conjunto e categorias desconhecida e geral explícitas. Para R1 e R2, são reportados acordo e kappa para classe, respondibilidade e atributos indispensáveis, além do índice de Jaccard para os conjuntos de unidades de evidência identificadas por documento e localização. Os resultados incluem denominadores e frequências das categorias, para contextualizar a concordância.

A separação das equipes reduz a influência de quem desenha a representação sobre o padrão de avaliação. Os grupos compartilham as fontes originais. A análise explicita esse vínculo e distingue os atributos empregados pelo filtro dos demais atributos requeridos pela pergunta. R1 e R2 também identificam os atributos expressos no enunciado para orientar a codificação de consultas, conservando a trilha dessa decisão.

### 4.3 Perguntas e dossiês

O piloto prevê aproximadamente sessenta perguntas: quatro por classe e por banco. As classes são resposta direta, condição, exceção, ambiguidade e insuficiência documental. A classe principal determina a análise prevista, e marcadores secundários conservam características sobrepostas. Aproximadamente metade das perguntas parte de dúvidas publicadas nos canais oficiais; as demais são elaboradas pelos pesquisadores para representar dependências e lacunas presentes na coleção. O registro identifica a origem de cada enunciado.

O dossiê registra atributos indispensáveis, requisitos obrigatórios da resposta, unidades de evidência e conjuntos suficientes alternativos. Uma unidade de evidência é uma passagem que fundamenta um requisito; trechos sobrepostos que expressam a mesma passagem são contabilizados uma vez. R1 e R2 examinam a respondibilidade independentemente e conciliam as referências antes de produzir as respostas experimentais.

Nas perguntas ambíguas, o dossiê especifica o atributo que exige esclarecimento e as respostas que dependem dele. Nas perguntas de insuficiência, registra o requisito sem suporte, a inspeção da coleção e a abstenção esperada. Essa construção distingue uma pergunta que exige informação adicional do usuário de outra para a qual falta documentação no instantâneo.

As perguntas e as famílias utilizadas no piloto ficam fora do conjunto final, incluindo paráfrases e outras perguntas dependentes das mesmas regras. O inventário de famílias registra essa exclusão antes da seleção final. O piloto orienta a calibração do procedimento, e a avaliação final utiliza perguntas e famílias reservadas.

### 4.4 Configurações comparadas

O Quadro 2 apresenta seis configurações. As quatro primeiras constituem o núcleo experimental; as demais oferecem referências de interpretação. A ordenação lexical usa o BM25, modelo clássico de recuperação probabilística (Robertson; Zaragoza, 2009).

| Configuração | Representação para recuperação | Finalidade |
|---|---|---|
| A | Conteúdo original do trecho, com representação semântica | Referência sem enriquecimento |
| B | Conteúdo com título, seção, tipo documental, produto e público no prefixo | Enriquecimento contextual completo do protocolo |
| C | Representação de B, com filtragem por produto e público explícitos na pergunta | Efeito adicional da filtragem |
| Bp | Conteúdo com prefixo restrito a produto e público | Ablação do conjunto adicional de descrição |
| L | Conteúdo original, com recuperação lexical BM25 | Referência lexical |
| S | Pergunta e instrução, sem documentos recuperados | Referência sem recuperação |

Quadro 2. Configurações e funções analíticas.

Fonte: elaboração própria.

O filtro de C aceita correspondência explícita, valores múltiplos compatíveis, documentos de alcance geral documentado e metadados desconhecidos. A compatibilidade geral é justificada na fonte. Quando nenhum atributo de filtragem estiver expresso na pergunta, C compartilha a seleção de B. O registro conserva candidatos excluídos, valores comparados e justificativas, permitindo identificar evidências suficientes eliminadas indevidamente.

As configurações com recuperação entregam ao gerador o mesmo formato: identificador, título, fonte, localização e conteúdo original dos trechos selecionados. Os prefixos de enriquecimento são usados na indexação. As instruções de resposta permanecem iguais, exigindo uso das evidências, preservação de condições, referência aos identificadores e esclarecimento ou abstenção quando cabíveis. S recebe a mesma pergunta e instrução, com seção documental vazia.

### 4.5 Execução, sensibilidade e esforço humano

A comparação principal produz uma resposta por pergunta e configuração, com geração sem amostragem. O Quadro 3 reúne os parâmetros previstos. Com a política de geração fixa, o contraste B × C examina diferenças decorrentes da seleção documental. Contextos efetivos idênticos devem produzir saídas idênticas no ambiente congelado; o piloto inclui uma verificação dessa propriedade e registra eventuais fontes técnicas de divergência.

A configuração inicial prevê um modelo multilíngue de representação e um gerador de oito bilhões de parâmetros, cujas versões serão congeladas antes do estudo final (INTFLOAT, [2024]; QWEN, [2025]). A decodificação sem amostragem constitui uma escolha metodológica de comparabilidade. A implementação inicial adota Transformers 4.57.1: sua documentação confirma que a penalidade usual de repetição inclui os tokens do prompt em modelos de geração apenas decodificadores (Hugging Face, [s. d.]). O piloto verifica esse comportamento na versão instalada e conserva versão, código e registro do teste técnico.

Uma verificação técnica anterior aos julgamentos detecta repetição degenerada quando uma sequência de pelo menos vinte tokens aparece três vezes consecutivas na saída. Se o evento ocorrer em qualquer configuração do piloto, o ajuste utiliza RepetitionPenaltyLogitsProcessor com penalidade 1,05 e prompt_ignore_length igual ao comprimento completo da entrada tokenizada, por geração. O parâmetro global repetition_penalty permanece em 1,0, para evitar uma segunda penalidade sobre o prompt. O ajuste vale uniformemente para as seis configurações e a estabilidade, com os demais parâmetros fixos. A exclusão do prompt reduz a interferência direta nas evidências; valores já emitidos na resposta continuam sujeitos à penalidade.

Antes e depois do ajuste, doze casos fictícios de verificação, congelados antes da geração, exigem reprodução de valores monetários, percentuais, datas e identificadores de fonte fornecidos no contexto. O mesmo caso e contexto são executados sem amostragem e com as duas sementes da estabilidade, nas duas políticas: 72 saídas no total. J1 e J2 conferem de forma independente, cegos à política e à semente, a fidelidade de cada item obrigatório. Valores são comparados com moeda, unidade e escala preservadas, aceitando equivalências de formato previamente listadas; identificadores exigem correspondência exata. Omissões, alterações e identificadores inexistentes são registrados por caso e política. Qualquer perda de um item preservado na saída correspondente sem penalidade impede aceitar o ajuste. São até 144 conferências técnicas adicionais, separadas dos julgamentos de adequação. O teste de repetição é repetido uma vez; persistência, falha de fidelidade ou incompatibilidade da implementação suspendem a execução final e exigem revisão registrada da política. A decisão antecede os escores de adequação do experimento.

A análise de sensibilidade a três, cinco e dez trechos examina a recuperação e a cobertura dos conjuntos suficientes, especialmente quando regra e exceção estejam separadas. Ela reutiliza os dossiês e dispensa nova geração. O desempenho das respostas é avaliado no número principal de cinco trechos. Com esse limite e o tamanho previsto dos trechos, a perda por orçamento de contexto deve ser infrequente; ocorrências são conservadas como eventos técnicos com identificação da evidência retirada.

A análise de estabilidade utiliza uma subamostra de 25% das perguntas, estratificada por banco e classe e selecionada antes da geração. No piloto, são quinze perguntas, uma por combinação de banco e classe. As duas respostas adicionais de A, B e C também recebem julgamento humano, com a mesma rubrica. O relato descreve a variação de adequação e a concordância entre repetições por pergunta, separadamente da comparação principal.

O orçamento do piloto é de 720 julgamentos de respostas na comparação principal, calculados como seis configurações, sessenta perguntas e dois avaliadores. A estabilidade acrescenta 180 julgamentos, calculados como três configurações, quinze perguntas, duas sementes e dois avaliadores. O total é de 900 julgamentos de respostas, além de 120 anotações iniciais de dossiês e do trabalho de metadados, conciliação e preparação. Como ilustração de orçamento, 660 perguntas equilibradas entre cinco classes e três bancos correspondem a 44 por combinação e 264 nas classes condição e exceção. Essa quantidade ultrapassa o limiar de 260 somente se as 264 perguntas representarem famílias distintas elegíveis, após excluir o piloto; sua disponibilidade ainda exige verificação. São 7.920 julgamentos principais. A três minutos por julgamento, somam-se 396 horas entre os dois avaliadores. A estabilidade em 165 perguntas acrescenta 1.980 julgamentos e 99 horas: o conjunto chega a 9.900 julgamentos e 495 horas, além das equipes de metadados e referências, conciliação e verificações técnicas. Quantidade de perguntas e duração são hipóteses de planejamento; o piloto informa o orçamento final.

| Componente | Especificação inicial a congelar após o piloto |
|---|---|
| Segmentação | Até 320 tokens do segmentador E5 por trecho; sobreposição máxima de 48; preservação de cabeçalhos e notas |
| Prefixo e entrada E5 | Prefixo de até 128 tokens; entrada total de até 512; registrar truncamento efetivo |
| Representação | intfloat/multilingual-e5-large-instruct; instrução de busca em português constante; vetores normalizados; similaridade por cosseno; busca exata |
| Recuperação principal | Cinco trechos, com desempate por identificador estável; sem reordenação adicional |
| Gerador | Qwen/Qwen3-8B; enable_thinking=False; do_sample=False; num_beams=1; até 512 tokens de saída; repetition_penalty=1,0; ajuste técnico por processador de penalidade 1,05 com prompt excluído (seção 4.5) |
| Contexto | Entrada de até 4.096 tokens do segmentador Qwen; incluir pergunta, instrução e evidências; conservar trechos inteiros em ordem de recuperação; retirar os últimos se exceder o limite |
| Estabilidade | A, B e C em 25% das perguntas; do_sample=True; temperatura 0,7; top_p=0,8; top_k=20; min_p=0; sementes 43 e 44 |
| Sensibilidade da recuperação | Recalcular seleção e cobertura para três, cinco e dez trechos nas cinco configurações com recuperação |
| Referência lexical | BM25; k1=1,2; b=0,75; palavras Unicode em minúsculas; acentos preservados; sem remoção de palavras ou redução a radicais |
| Auditabilidade | Transformers 4.57.1 como versão inicial; revisões dos modelos, segmentadores, bibliotecas, instruções, hardware, política de penalidade, identificadores, contextos e respostas no registro |

Quadro 3. Parâmetros e registros de execução.

Fonte: elaboração própria, com especificações iniciais baseadas em INTFLOAT ([2024]) e QWEN ([2025]).

### 4.6 Assistência na elaboração

A elaboração contou com assistência de ChatGPT e Codex, da OpenAI, na redação e revisão textual, formulação do protocolo, busca de referências, rodadas assistidas de parecer e adequação ao template. Essa assistência inclui as conversas de revisão que orientam os ajustes do texto. Os modelos de representação e geração especificados para o experimento ainda não foram executados. A declaração detalhada de uso e os campos para aprovação autoral constam das Notas da Obra.

## 5 Avaliação e análise

### 5.1 Adequação e aplicabilidade por grupo de atributos

A adequação é binária, segundo a classe e os requisitos do dossiê. Nas respostas diretas, condicionais e de exceção, todos os requisitos indispensáveis devem ser satisfeitos, sem afirmação incompatível com a situação descrita. Na ambiguidade, é necessário solicitar o esclarecimento previsto. Na insuficiência, a resposta deve indicar a limitação documental e evitar preencher a lacuna com uma afirmação sem suporte.

A aplicabilidade é reportada em dois grupos: atributos filtrados, produto e público; e atributos não filtrados, incluindo elegibilidade, canal e período. Para cada atributo indispensável, os avaliadores marcam compatibilidade, incompatibilidade ou informação indeterminada. O relato informa contagens e denominadores, com a informação indeterminada apresentada separadamente. Uma pergunta sem requisito de canal, por exemplo, fica fora do denominador desse atributo. A análise dos atributos não filtrados é restrita às perguntas em que ao menos um deles seja necessário.

O primeiro grupo examina se o filtro cumpre sua função operacional. O segundo examina se a informação selecionada e a resposta preservam requisitos que o filtro não utiliza. Os julgamentos partem dos dossiês independentes, e os avaliadores recebem os documentos originais pertinentes, sem os metadados experimentais ou os nomes das configurações. A adequação é apresentada junto dessa decomposição, para distinguir compatibilidade parcial de atendimento completo.

A cobertura indica se os resultados contêm ao menos um conjunto suficiente alternativo do dossiê. A completude corresponde à fração de requisitos obrigatórios atendidos na resposta. A sustentação das afirmações documentais tem quatro categorias nominais: sustentada, parcialmente sustentada, contradita e sem suporte. A exclusão indevida de evidência registra unidades do dossiê eliminadas pelo filtro, e as perdas de cobertura identificam perguntas com um conjunto suficiente em B que deixa de estar presente em C. O relato apresenta também os ganhos no sentido inverso e a diferença líquida de cobertura entre as configurações.

Recall@5 utiliza as unidades de evidência do dossiê como referência, com deduplicação de passagens sobrepostas. A medida é interpretada em relação a esse conjunto anotado, nas perguntas com ao menos uma unidade de evidência de referência. A posição da primeira evidência é descrita apenas nas perguntas diretas respondíveis com uma unidade. Abstenção indevida em pergunta respondível e esclarecimento desnecessário são reportados separadamente. Na configuração S, a adequação de conteúdo é analisada à parte; cobertura documental, recuperação e sustentação por fonte fornecida têm classificação de não aplicáveis.

### 5.2 Julgamento e exemplo trabalhado

J1 e J2 julgam as respostas de forma independente, em ordem aleatória e sem acesso à configuração nem à semente. Nenhum modelo de linguagem atua como juiz; as métricas documentais automáticas comparam identificadores às referências humanas. A rubrica será calibrada no piloto e congelada para a etapa final. A concordância é descrita por proporção de acordo e coeficiente kappa sem ponderação para categorias nominais. A conciliação conserva o julgamento inicial de cada avaliador, a decisão final e sua justificativa documental.

A taxonomia admite falhas cumulativas: recuperação insuficiente, exclusão indevida pelo filtro, uso incompleto ou incorreto da evidência, incompatibilidade de atributos e referência inadequada. O registro técnico conserva eventos de retirada de evidência do contexto. Ausência de informação na coleção caracteriza a respondibilidade da pergunta, conforme o dossiê. O Quadro 4 ilustra como os conceitos se aplicam a um único caso.

| Elemento | Registro ilustrativo |
|---|---|
| Pergunta | “Tenho o cartão Alfa, sou pessoa física e minha fatura é de R$ 600. Tenho isenção de anuidade?” |
| Evidência E1 | Documento fictício: cartão Alfa para pessoa física; anuidade de R$ 120; isenção para fatura mensal igual ou superior a R$ 1.000 |
| Evidência E2 | Documento fictício: cartão Beta, de outra modalidade, com anuidade gratuita |
| Dossiê | Classe condição; atributos indispensáveis: Alfa, pessoa física e valor da fatura; evidência suficiente: E1; resposta esperada: o valor informado não atinge o requisito de isenção |
| Seleção ilustrativa de C | E1 permanece; E2 é excluída por produto incompatível |
| Resposta ilustrativa inadequada | “Sim, você tem isenção de anuidade [E1].” |
| Classificação | Produto e público compatíveis; elegibilidade incompatível; afirmação contradita por E1; adequação igual a zero; falha de uso da evidência |
| Resposta ilustrativa adequada | “Com fatura de R$ 600, você não atinge o requisito de R$ 1.000 para a isenção do cartão Alfa [E1].” |

Quadro 4. Exemplo trabalhado, inteiramente fictício, de pergunta, evidências e julgamento.

Fonte: elaboração própria. Produtos, documentos, valores e respostas foram criados para explicar o protocolo; o quadro não apresenta saída experimental.

O caso mostra o papel da decomposição: a filtragem seleciona o produto solicitado, enquanto a resposta ainda pode falhar no requisito de elegibilidade. Um resultado agregado que privilegiasse apenas produto e público esconderia essa diferença. A referência à E1 também pode estar formalmente correta e sustentar uma afirmação contrária à regra documentada.

O Quadro 5 apresenta o risco simétrico: uma regra geral necessária é excluída quando sua abrangência recebe uma codificação restrita incorreta. A regra prevista de C preserva documentos corretamente identificados como gerais ou desconhecidos. O erro de produto também contamina o prefixo de B e pode prejudicar sua ordenação. Na seleção fictícia mostrada, B ainda recupera E3 e E4; C acrescenta a exclusão de E4. A falha de representação atua nas duas configurações, e o contraste distingue a perda adicional associada ao filtro.

| Elemento | Registro ilustrativo |
|---|---|
| Pergunta | “O cartão Alfa tem anuidade. Após o protocolo de cancelamento, continuam novos lançamentos?” |
| Evidências fictícias | E3: o cartão Alfa cobra anuidade. E4: documento intitulado “Cartão Beta”, cuja nota declara que o cancelamento interrompe novos lançamentos de anuidade em todos os cartões, incluindo Alfa |
| Dossiê | Classe exceção; conjunto suficiente: E3 e E4; resposta esperada: novos lançamentos cessam após o protocolo de cancelamento |
| Erro de metadados | A descrição de E4 registra somente Beta, por seguir o título e omitir o alcance geral declarado na nota |
| Seleção e custo | B recupera E3 e E4; C exclui E4 por produto. A cobertura do conjunto suficiente passa de um para zero; há exclusão indevida de evidência necessária |
| Diagnóstico e ação | Corrigir o alcance de E4 para geral e testar novamente cobertura e adequação; uma resposta que afirme continuidade dos novos lançamentos contraria o dossiê |

Quadro 5. Exemplo fictício de perda de evidência por erro de abrangência nos metadados.

Fonte: elaboração própria. Produtos, regras e seleções são fictícios; não houve execução experimental.

### 5.3 Dimensionamento e inferência

O piloto verifica a segmentação, calibra a rubrica, estima esforço humano, caracteriza discordâncias e conta as famílias elegíveis reservadas para o estudo final. H1 e H3 abrangem as classes condição e exceção; H2 abrange perguntas com atributo de filtragem explícito e codificável. Cada contraste tem seu próprio denominador de famílias, após a exclusão do piloto.

Para pares independentes, o dimensionamento usa a aproximação normal apresentada na Equação (1), que distingue a variância sob a hipótese nula da variância sob a alternativa:

$$
n \approx \frac{\left[z_{1-\alpha^*/2}\sqrt{q}+z_{1-\beta}\sqrt{q-\Delta^2}\right]^2}{\Delta^2}\tag{1}
$$

Nessa expressão, n é o número de pares independentes, q é a probabilidade de discordância entre configurações, Δ é a diferença de adequação a detectar, α*=0,05/3, 1−β é o poder e z representa o quantil da distribuição normal padrão. Com q=0,25, Δ=0,10, poder de 80% e teste bilateral, obtém-se n≈258,98, arredondado para 259 pares; o planejamento adota o limiar conservador de 260. Esse valor equivale a famílias somente quando cada família contribui com uma pergunta. H1 e H3 exigem essa quantidade nas classes condição e exceção, em conjunto, dentro das tarefas selecionadas.

A decisão é fixada por contraste: menos de 260 famílias elegíveis mantém a análise exploratória. Atingir esse limiar também exige confirmação de poder por simulação, reproduzindo a dependência entre perguntas e a composição por banco e classe. O piloto pode elevar o mínimo requerido pela simulação; a contagem, o tamanho final e a decisão são registrados antes de gerar as respostas finais. Se o orçamento ou a quantidade de famílias impedir esse requisito, o alvo passa a ser precisão: intervalo de 95% da diferença de adequação com meia largura de até dez pontos percentuais, tratado como objetivo de planejamento. Para uma meia largura h=0,10 e discordância q=0,25, a aproximação conservadora sob diferença nula, apresentada na Equação (2), indica 97 pares independentes. Esse mínimo é ilustrativo, ignora dependência intrafamília e se aplica à população elegível de cada contraste.

$$
n_{\mathrm{prec}} \approx \frac{z_{0,975}^{2}\,q}{h^{2}} \approx 96,04\tag{2}
$$

A amostra é fixada previamente pela simulação de precisão e pela disponibilidade; eventual intervalo mais amplo é reportado com sua incerteza, sem ampliar a amostra após conhecer o efeito.

Uma etapa confirmatória exige amostra, contrastes, famílias, critérios e orçamento fixados previamente. Os três contrastes usam Bonferroni, com intervalos de 98,33% para a interpretação confirmatória e intervalos de 95% descritivos. Apoio confirmatório exige limite inferior do intervalo ajustado da diferença de adequação maior que zero. O relato também informa se a estimativa pontual alcança a diferença de interesse de dez pontos percentuais. Apoio direcional e magnitude de interesse são critérios apresentados separadamente; limite inferior positivo com estimativa inferior a dez pontos indica efeito positivo abaixo da magnitude planejada. A estimativa mantém a mesma pergunta nas configurações comparadas.

Os intervalos percentis de 95% e 98,33% usam a mesma distribuição de 5.000 reamostragens de famílias dentro de cada banco: quantis 0,025 e 0,975 para o primeiro; quantis α*/2=0,008333 e 1−α*/2=0,991667 para o segundo, com interpolação linear entre estatísticas ordenadas. A análise exploratória interpreta os intervalos de 95%; os intervalos ajustados fundamentam somente os contrastes previamente dimensionados e registrados. Cada família reamostrada conserva suas perguntas e pares; os três bancos permanecem estratos fixos. O relato apresenta famílias por contraste e banco, tamanhos dos agrupamentos e estratos pequenos. Poucas famílias exigem descrição e explicitação da instabilidade dos intervalos.

As comparações com L e S, a estabilidade, a sensibilidade ao número de trechos e os recortes adicionais são exploratórios. O relato separa as classes previstas nas hipóteses da média global. A aplicabilidade identifica os atributos relacionados a cada ganho, e a cobertura caracteriza o custo documental da filtragem.

## 6 Matriz de interpretação para manutenção da base

A matriz prevista reúne configuração e pergunta, diferenças nos desfechos, evidências preservadas ou perdidas, falhas classificadas e ação documental a testar. Sua finalidade é orientar o diagnóstico: revisar a descrição, corrigir o filtro, reunir regra e exceção ou melhorar a instrução de uso da evidência. O Quadro 6 fornece uma linha-modelo vinculada ao exemplo fictício.

| Decisão documental | Padrão ilustrativo | Diagnóstico | Ação a testar após o experimento |
|---|---|---|---|
| Filtrar produto e público em C | Produto correto; elegibilidade omitida na resposta | Compatibilidade dos atributos filtrados, com falha no uso de requisito não filtrado | Preservar a regra de isenção junto ao trecho e testar instrução que exija verificar seu requisito; reavaliar adequação e cobertura |

Quadro 6. Linha-modelo da matriz de interpretação, sem resultados empíricos.

Fonte: elaboração própria, com base no caso fictício do Quadro 4.

Na execução, cada linha remete aos identificadores dos registros de evidência e avaliação. Ganhos de recuperação com adequação estável apontam uma etapa diferente daquela indicada por perda de cobertura após filtragem. O contraste B × Bp orienta a decisão sobre o conjunto adicional de descrição; a identificação do efeito de cada atributo exige outros contrastes.

A manutenção é examinada pelo esforço observado para descrever documentos, atualizar valores e conciliar divergências. Esse registro relaciona a utilidade do ganho ao custo de manter os metadados. As ações propostas pela matriz constituem intervenções futuras a verificar, com critérios explícitos para a nova avaliação.

A descrição manual conciliada fornece uma referência de desempenho sob curadoria intensiva para profissionais que consideram automatizar a contextualização, como na técnica de Ford (2024). A interpretação como teto prático depende de comparar os dois procedimentos: prefixos automáticos podem representar relações que a descrição manual omitiu. Uma etapa posterior com prefixos gerados por modelo é uma extensão prevista para avaliar essa transferência, sujeita a orçamento e protocolo próprio.

## 7 Limites, registro e transparência

O protocolo utiliza documentação pública e perguntas construídas ou adaptadas para o experimento. Sua população de inferência corresponde à situação descrita nos enunciados, dentro do instantâneo coletado. O desenho deixa fora documentos internos, dados de clientes e atendimentos reais. A escolha intencional de três bancos compara tarefas selecionadas, com generalização limitada para o setor bancário e para outros domínios.

Metadados manuais conciliados representam uma descrição controlada; resultados poderão mudar com anotação automática, documentação incompleta e manutenção operacional. A separação das equipes reduz circularidade, mas as referências e os metadados permanecem baseados nas mesmas fontes públicas. A avaliação separada dos atributos não filtrados é essencial para distinguir cumprimento do filtro de preservação mais ampla da aplicabilidade.

O gerador de oito bilhões de parâmetros favorece reprodução com recursos delimitados. O comportamento poderá diferir do de modelos maiores usados em serviços reais, inclusive na interpretação de regras, abstenção e aproveitamento de evidências. A decodificação fixa, a representação escolhida e o tamanho dos trechos também delimitam os resultados. A sensibilidade de recuperação a três e dez trechos descreve mudanças nas evidências recuperadas; a geração com esses tamanhos de contexto exige outra avaliação.

Documentos públicos e perguntas frequentes podem ter participado do treinamento do gerador. A configuração S oferece uma referência de conteúdo, sem identificação causal da contribuição da memória prévia. As fontes datadas identificam o conteúdo da coleção experimental, enquanto os dados de treinamento do modelo permanecem desconhecidos. As inferências estatísticas dependem das famílias elegíveis e da precisão disponível para cada hipótese.

Antes da coleta final, o plano deverá ser depositado em repositório público com data, identificação persistente e resumo criptográfico. Atualizações decorrentes do piloto integram uma nova versão registrada antes da execução final, com descrição e justificativa das alterações. Serão divulgados inventário, esquema de metadados, perguntas, rubricas, instruções, versões técnicas, registros de execução e decisões de avaliação, respeitando os direitos de uso das fontes. O registro de alterações posteriores exige histórico e justificativa.

O protocolo prevê fontes públicas, sem dados pessoais de clientes. O enquadramento ético da avaliação humana deverá ser definido institucionalmente antes de recrutar avaliadores. Coleta, experimentos e julgamentos ainda não foram realizados. A responsabilidade pelo conteúdo, pela conferência das fontes e pela aprovação final cabe aos autores, com declarações detalhadas nas Notas da Obra.

## 8 Considerações finais

O protocolo oferece instrumentos que o leitor pode examinar antes da execução: contrastes com populações elegíveis, critérios de aplicabilidade e adequação, regras de independência entre equipes e exemplos de ganhos e perdas documentais. A rubrica pode ser reaproveitada em outras coleções, desde que atributos e conjuntos suficientes sejam reconstruídos para as tarefas locais.

Pesquisadores e profissionais podem criticar as hipóteses, testar a clareza dos dossiês e replicar o desenho em outra instituição ou domínio, conservando a distinção entre evidência suficiente e informação aplicável. O registro das adaptações torna essas replicações comparáveis. A matriz de interpretação orienta o diagnóstico e a escolha de intervenções na base de conhecimento; sua utilidade empírica depende da execução e dos resultados do estudo.

## Referências

BROUGHTON, Vanda. The need for a faceted classification as the basis of all methods of information retrieval. **Aslib Proceedings**, v. 58, n. 1-2, p. 49-72, 2006. DOI: 10.1108/00012530610648671. Disponível em: https://doi.org/10.1108/00012530610648671. Acesso em: 10 out. 2026.

COSIJN, Erica; INGWERSEN, Peter. Dimensions of relevance. **Information Processing & Management**, v. 36, n. 4, p. 533-550, 2000. DOI: 10.1016/S0306-4573(99)00072-2. Disponível em: https://doi.org/10.1016/S0306-4573(99)00072-2. Acesso em: 10 out. 2026.

DADOPOULOS, Michail; LADAS, Anestis; MOSCHIDIS, Stratos; NEGKAKIS, Ioannis. **Metadata-Driven Retrieval-Augmented Generation for Financial Question Answering**. [S. l.]: arXiv, 2025. Preprint. DOI: 10.48550/arXiv.2510.24402. Disponível em: https://arxiv.org/abs/2510.24402. Acesso em: 10 out. 2026.

ES, Shahul; JAMES, Jithin; ESPINOSA ANKE, Luis; SCHOCKAERT, Steven. RAGAs: Automated Evaluation of Retrieval Augmented Generation. In: CONFERENCE OF THE EUROPEAN CHAPTER OF THE ASSOCIATION FOR COMPUTATIONAL LINGUISTICS, 18., 2024, St. Julians. **Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations**. St. Julians: Association for Computational Linguistics, 2024. p. 150-158. DOI: 10.18653/v1/2024.eacl-demo.16. Disponível em: https://aclanthology.org/2024.eacl-demo.16/. Acesso em: 10 out. 2026.

FORD, Daniel. **Introducing contextual retrieval**. [S. l.]: Anthropic, 19 set. 2024. Disponível em: https://www.anthropic.com/engineering/contextual-retrieval. Acesso em: 10 out. 2026.

HJØRLAND, Birger. Epistemology and the socio-cognitive perspective in information science. **Journal of the American Society for Information Science and Technology**, v. 53, n. 4, p. 257-270, 2002. DOI: 10.1002/asi.10042. Disponível em: https://doi.org/10.1002/asi.10042. Acesso em: 10 out. 2026.

HJØRLAND, Birger. Domain analysis. **Knowledge Organization**, v. 44, n. 6, p. 436-464, 2017. DOI: 10.5771/0943-7444-2017-6-436. Disponível em: https://doi.org/10.5771/0943-7444-2017-6-436. Acesso em: 10 out. 2026.

HUGGING FACE. **Utilities for Generation**. Versão 4.57.1. [S. l.]: Hugging Face, [s. d.]. Disponível em: https://huggingface.co/docs/transformers/v4.57.1/en/internal/generation_utils#transformers.RepetitionPenaltyLogitsProcessor. Acesso em: 10 out. 2026.

INTFLOAT. **Multilingual-E5-large-instruct**: model card. [S. l.]: Hugging Face, [2024]. Disponível em: https://huggingface.co/intfloat/multilingual-e5-large-instruct. Acesso em: 10 out. 2026.

JOREN, Hailey; ZHANG, Jianyi; FERNG, Chun-Sung; JUAN, Da-Cheng; TALY, Ankur; RASHTCHIAN, Cyrus. Sufficient Context: A New Lens on Retrieval Augmented Generation Systems. In: INTERNATIONAL CONFERENCE ON LEARNING REPRESENTATIONS, 13., 2025, Singapore. **Proceedings of the International Conference on Learning Representations**. [S. l.]: ICLR, 2025. Disponível em: https://proceedings.iclr.cc/paper_files/paper/2025/hash/33dffa2e3d2ab74a783d1a8c292f66d9-Abstract-Conference.html. Acesso em: 10 out. 2026.

LEWIS, Patrick; PEREZ, Ethan; PIKTUS, Aleksandra; PETRONI, Fabio; KARPUKHIN, Vladimir; GOYAL, Naman; KÜTTLER, Heinrich; LEWIS, Mike; YIH, Wen-tau; ROCKTÄSCHEL, Tim; RIEDEL, Sebastian; KIELA, Douwe. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. In: CONFERENCE ON NEURAL INFORMATION PROCESSING SYSTEMS, 34., 2020, [S. l.]. **Advances in Neural Information Processing Systems**. [S. l.]: Curran Associates, 2020. v. 33. Disponível em: https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html. Acesso em: 10 out. 2026.

LIU, Nelson F.; LIN, Kevin; HEWITT, John; PARANJAPE, Ashwin; BEVILACQUA, Michele; PETRONI, Fabio; LIANG, Percy. Lost in the Middle: How Language Models Use Long Contexts. **Transactions of the Association for Computational Linguistics**, v. 12, p. 157-173, 2024. DOI: 10.1162/tacl_a_00638. Disponível em: https://aclanthology.org/2024.tacl-1.9/. Acesso em: 10 out. 2026.

MIZZARO, Stefano. Relevance: the whole history. **Journal of the American Society for Information Science**, v. 48, n. 9, p. 810-832, 1997. DOI: 10.1002/(SICI)1097-4571(199709)48:9<810::AID-ASI6>3.0.CO;2-U. Disponível em: https://doi.org/10.1002/(SICI)1097-4571(199709)48:9%3C810::AID-ASI6%3E3.0.CO;2-U. Acesso em: 10 out. 2026.

QWEN. **Qwen3-8B**: model card. [S. l.]: Hugging Face, [2025]. Disponível em: https://huggingface.co/Qwen/Qwen3-8B. Acesso em: 10 out. 2026.

ROBERTSON, Stephen; ZARAGOZA, Hugo. The probabilistic relevance framework: BM25 and beyond. **Foundations and Trends in Information Retrieval**, v. 3, n. 4, p. 333-389, 2009. DOI: 10.1561/1500000019. Disponível em: https://doi.org/10.1561/1500000019. Acesso em: 10 out. 2026.

SARACEVIC, Tefko. Relevance: a review of the literature and a framework for thinking on the notion in information science. Part II: nature and manifestations of relevance. **Journal of the American Society for Information Science and Technology**, v. 58, n. 13, p. 1915-1933, 2007. DOI: 10.1002/asi.20682. Disponível em: https://doi.org/10.1002/asi.20682. Acesso em: 10 out. 2026.

SCHAMBER, Linda; EISENBERG, Michael B.; NILAN, Michael S. A re-examination of relevance: toward a dynamic, situational definition. **Information Processing & Management**, v. 26, n. 6, p. 755-776, 1990. DOI: 10.1016/0306-4573(90)90050-C. Disponível em: https://doi.org/10.1016/0306-4573(90)90050-C. Acesso em: 10 out. 2026.

WANG, Shuting; TAN, Jiejun; DOU, Zhicheng; WEN, Ji-Rong. OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in Financial Domain. In: CONFERENCE ON EMPIRICAL METHODS IN NATURAL LANGUAGE PROCESSING, 2025, Suzhou. **Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing**. Suzhou: Association for Computational Linguistics, 2025. p. 5726-5751. DOI: 10.18653/v1/2025.emnlp-main.292. Disponível em: https://aclanthology.org/2025.emnlp-main.292/. Acesso em: 10 out. 2026.

WILSON, Patrick. Situational relevance. **Information Storage and Retrieval**, v. 9, p. 457-471, 1973. DOI: 10.1016/0020-0271(73)90096-X. Disponível em: https://doi.org/10.1016/0020-0271(73)90096-X. Acesso em: 10 out. 2026.

## Apêndice A Registro e reprodução

O registro por pergunta inclui identificador, banco, produto, origem do enunciado, classe principal, marcadores secundários e família documental. O dossiê conserva respondibilidade, atributos indispensáveis, requisitos obrigatórios, unidades de evidência e conjuntos suficientes alternativos. Os atributos de produto e público expressos na consulta são codificados antes da execução, com justificativa e histórico de conciliação.

Cada execução conserva configuração, política de geração, semente quando houver amostragem, revisões técnicas, pergunta, instrução, candidatos, exclusões, resultados ordenados, contexto efetivo e resposta. Cada avaliação conserva julgamentos independentes, adequação, aplicabilidade por grupo de atributos, completude, sustentação e falhas cumulativas. As decisões conciliadas remetem às evidências e mantêm histórico de alterações.

No BM25, a frequência documental inversa é calculada como ln[1 + (N − n + 0,5)/(n + 0,5)], com N igual ao número de trechos candidatos e n ao número de trechos que contêm o termo. A frequência do termo é normalizada pelo comprimento do trecho, com k1=1,2 e b=0,75. O registro técnico conserva a implementação e a convenção adotada para reprodução.

A subamostra de estabilidade é selecionada por ordenação do resumo criptográfico SHA-256 do identificador de cada pergunta concatenado à expressão fixa “estabilidade-2026”, dentro de cada combinação de banco e classe. A regra de arredondamento será fixada no plano final. O pacote de reprodução conserva a lista selecionada e os denominadores das análises. As versões dos modelos, a instrução exata de busca e a amostra final serão completadas após o piloto e congeladas antes da execução final.

## Verificação de integridade desta minuta

SHA-256 do conteúdo anterior a esta seção, em UTF-8 com quebras LF e sem alterações de espaços: `ca0b0b79290789c359cbd53428007d93bfe7b1ce753ef22168456ce313b203ea`.
