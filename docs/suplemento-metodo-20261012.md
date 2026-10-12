# Suplemento de método e proveniência

[Manuscrito](manuscrito.md) · [Reprodução](reproducao.md)

Este material mantém os parâmetros e registros técnicos que complementam o artigo. A coleção, as perguntas, as âncoras e os rankings originais permanecem fixados. As saídas anteriores de calibração indisponíveis continuam identificadas como lacuna.

## Ambiente e histórico técnico


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


## Alcance da consulta bibliográfica anterior


A consulta limitada ao resumo e aos dados bibliográficos refere-se especificamente a Wilson (1999). Dadopoulos et al. (2025) foi consultado em texto completo, com atenção ao método e às comparações de recuperação e geração. A referência à ISO 25964-1 utiliza a descrição pública do escopo da norma; o texto integral da norma não foi acessado. SKOS é usado como referência conceitual, sem declaração de conformidade da implementação.

As versões publicadas de Lewis et al. (2020) e Joren et al. (2025) são identificadas como anais. O endereço de OpenReview de Joren foi identificado, mas seu acesso direto encontrou verificação de navegador; a versão dos autores no arXiv informa, na primeira página, publicação na ICLR 2025. A página definitiva de OmniEval informa 5726–5751, mantidos nesta versão. A página de Contextual Retrieval atribui pesquisa e escrita a Daniel Ford; o endereço de engenharia é o adotado. Fontes bibliográficas e decisões de conferência constam da resposta ao parecer no repositório.

## Fontes adicionais consultadas

Os artigos de Hjørland sobre organização do conhecimento e tesauros e a discussão de Tudhope e Binding foram consultados nos PDFs da editora, com atenção aos conceitos e às posições sobre relações semânticas. RAGAS e ARES foram consultados nos PDFs da ACL. Sua citação situa a separação entre avaliação de contexto e de respostas; essas ferramentas não foram executadas no experimento.

A Resolução CMN nº 3.919 foi conferida na [versão v7 publicada pelo Banco Central](https://normativos.bcb.gov.br/Lists/Normativos/Attachments/49514/Res_3919_v7_P.pdf), consultada em 12/10/2026. O art. 2º, I, b mantém a exceção de perda. A referência à versão v7 documenta o texto consolidado consultado; o número do arquivo não é usado isoladamente como certificado de vigência de todos os dispositivos na data. A consulta normativa complementa a discussão e não altera o corpus bancário.

A descrição pública da ISO sustenta a afirmação limitada sobre o propósito da norma; seu texto integral pago não foi consultado. A leitura restrita de Wilson permanece declarada. A referência de OmniEval continua nas páginas 5726–5751 da fonte definitiva. O Word conserva a equação em objeto nativo, com duas raízes e uma fração, conferidas na renderização.
