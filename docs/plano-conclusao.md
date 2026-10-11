# Plano completo para concluir a pesquisa

[Início](../README.md) · [Execução já realizada](execucao-20261011.md) · [Decisões em formato estruturado](../configs/closure-plan.json)

**Versão de planejamento: 11/10/2026.** Yago é o único pesquisador. Codex conduz o trabalho técnico, prepara os registros e trata exceções. O plano usa execução em lote, sem equipe de anotadores ou catalogação manual obrigatória.

Esta versão define decisões, entregas, alternativas e critérios de conclusão. A publicação deste plano registra o planejamento; a conclusão das etapas depende dos arquivos e testes produzidos na execução. O relatório anterior conserva os resultados efetivamente obtidos.

## 1. Resultado que queremos entregar

Um estudo exploratório reproduzível sobre organização documental e recuperação de evidências bancárias: fontes identificadas, perguntas e referências ancoradas, seis configurações executadas, avaliação automática explicitamente identificada, análise das falhas e recomendações para organizar uma base de conhecimento.

O pacote final inclui código, catálogo com links, decisões de acesso, entradas congeladas, resultados, matriz de falhas, relatório técnico e material de manuscrito. A abrangência cobre os bancos e documentos selecionados. Afirmações sobre todos os bancos brasileiros ou sobre compreensão de leitores exigem evidência adicional.

**Conclusão do núcleo:** as etapas abaixo têm uma entrega verificável ou uma decisão de escopo aplicada. Uma fonte excluída recebe motivo e alternativa; uma avaliação inconclusiva recebe tratamento analítico próprio. Falhas de execução permanecem identificadas como falhas até serem corrigidas.

## 2. Fechar a seleção e as condições das fontes

**Ação:** ampliar Inter e Bradesco e examinar Banco do Brasil, seguido de Caixa, para uma terceira instituição. A busca inicial fica limitada a 40 URLs candidatas por instituição, em até duas rodadas. Começa por contas e cartões para pessoa física; documentos gerais necessários também entram. MEI e PJ, quando presentes em uma fonte, são registrados para distinguir públicos e evitar aplicação indevida.

Para cada candidato: confirmar identidade institucional, modalidade da conta, domínio oficial, acesso sem login, termos aplicáveis, robots.txt, data e possibilidade de preservar o material para pesquisa. Registrar separadamente decisão operacional, autorização expressa e redistribuição. A avaliação assistida de políticas fica identificada como tal. A ausência de uma restrição encontrada não produz uma licença do banco.

Endereços com restrição ou redirecionamento fora do cadastro recebem exclusão motivada. Um destino oficial diferente exige revisão e cadastro próprios. Itaú, Santander e C6 continuam suspensos nas condições já registradas. A descoberta pode consultar menus e mapas de páginas; downloads seguem os limites do domínio.

**Alternativa decidida:** se BB e Caixa não fornecerem uma terceira fonte compatível após essas rodadas, o estudo passa a Inter e Bradesco. O título, método, amostra e limites passam a declarar duas instituições. Essa mudança é fixada antes da preparação definitiva e da geração do piloto ampliado. Nubank fica fora desta rota, evitando alterar silenciosamente a definição institucional de banco.

**Concluído quando:** existir `source-decisions.jsonl` com todos os candidatos, evidências, inclusões e exclusões; o cadastro final contiver somente URLs liberadas operacionalmente; e `scope-decision.json` registrar dois ou três bancos. Nenhuma fonte aguarda indefinidamente uma resposta externa.

## 3. Completar a coleção e a qualidade da extração

**Ação:** coletar as fontes selecionadas em lotes novos, preservando originais, horário, URL final, tipo e SHA-256. Reusar os 17 documentos já coletados quando continuarem dentro do escopo. Eliminar cópias idênticas e registrar versões divergentes. Não usar quantidade de páginas como indicador de suficiência.

Comparar texto extraído com os originais, dando prioridade a tabelas, notas, valores, unidades, datas, condições e exceções. Remover menus repetidos em uma camada derivada, com registro da transformação e posições rastreáveis. Páginas vazias, incompletas ou PDFs sem texto recebem tentativa de fonte alternativa; OCR só entra com ferramenta, versão e verificações registradas. Material que continue ilegível é excluído, preservando o motivo.

**Concluído quando:** cada documento incluído tiver texto utilizável, origem e hash conferidos; cada falha tiver resolução ou exclusão motivada; e a cobertura de contas, cartões, regras gerais, condições e exceções estiver descrita por banco. Zero alertas do catálogo, isoladamente, não comprova qualidade.

**Entrega:** `corpus-manifest.json`, catálogo atualizado e relatório de extração. Cópias sem licença de redistribuição permanecem no pacote privado de pesquisa.

## 4. Preparar metadados, famílias e referências automaticamente

**Ação:** integrar a preparação assistida à coleção inteira. Cada trecho recebe título, seção, tipo, produto, público e evidência literal. Canal, período, elegibilidade e exceções ficam registrados como atributos adicionais. Somente produto e público alimentam o filtro de C; atributos desconhecidos ou gerais seguem a regra conservadora do projeto.

Uma família reúne perguntas ligadas à mesma regra ou ao mesmo conjunto de evidências. Condição, exceção, paráfrase e versão temporal relacionadas ficam na mesma família. Perguntas sem evidência são agrupadas pelo assunto e pela lacuna documental. A contagem de passagens ou paráfrases não aumenta automaticamente o número de famílias independentes.

Cada referência conserva unidades de evidência, conjunto suficiente, requisitos da resposta, limites de aplicabilidade e suporte para esclarecer ou declarar insuficiência. Uma alegação de ausência de evidência exige pesquisa lexical e semântica na coleção congelada, com registro dos candidatos examinados. Dúvidas não resolvidas tornam a pergunta inelegível para a amostra principal.

**Controle:** a proposta de metadados não recebe acesso às respostas geradas; a referência examina o texto original, sem usar o prefixo da busca como prova. Registrar o compartilhamento de ferramenta entre preparação e julgamento e a ausência de independência humana. Checagens verificam se passagens e posições realmente existem, se fontes pertencem ao banco certo e se requisitos possuem suporte.

**Concluído quando:** todos os itens incluídos tiverem origem, evidência e estrutura válidas, e a separação entre piloto e etapa final estiver definida por família, antes da geração. O caso técnico já observado fica fora da etapa final.

**Entrega:** `metadata.json`, `families.jsonl`, `questions.jsonl`, `dossiers.jsonl` e `unit-map.json`, com instruções, versões e hashes.

## 5. Fixar a implementação que cabe no ambiente

**Decisão para a próxima implementação:** E5 em FP32 na CPU e Qwen3-8B oficial GGUF Q4_K_M em llama.cpp, nas revisões e hashes usados no teste real. A escolha entra no adendo e no manuscrito antes das comparações. Quantização e implementação delimitam o resultado do estudo.

O código `technical.py` já cobre um caso. A próxima entrega integra essa implementação ao executor de várias perguntas. Não basta apontar `experiment.py` para um arquivo GGUF: seu gerador atual usa Transformers e precisa de adaptação explícita.

Conservar as seis configurações, escopo por banco, segmentação de 320 tokens com sobreposição de 48, prefixo limitado a 128 tokens, busca dos dez primeiros e uso de até cinco trechos originais na resposta. E5 continua com seu limite de entrada de 512 tokens. Registrar cortes e trechos retirados. Qwen usa até 4.096 tokens de entrada, saída de até 512 e reserva de servidor de 8.192 posições.

Construir os índices e liberar E5 antes de carregar Qwen. O servidor fica local. Usar a mesma versão, precisão, instruções e política de geração em todas as configurações. O principal começa com geração gulosa e penalidade 1,0; a estabilidade usa sementes 43 e 44 e parâmetros fixados no arquivo de execução.

**Concluído quando:** o executor gerar e registrar um lote com múltiplas perguntas, retomar uma interrupção sem duplicar saídas e comprovar que índices, metadados, modelos e perguntas correspondem aos hashes congelados. A adaptação precisa de testes de pares completos, retomada e exclusão de famílias do piloto.

## 6. Fechar fidelidade e repetição antes do estudo final

**Ação:** executar 12 casos técnicos com respostas de referência conhecidas, cobrindo moeda, percentuais, escala, datas, identificadores e condições. Cada caso roda em geração principal e nas duas sementes de estabilidade: 36 saídas na política inicial.

Registrar itens preservados, alterados, omitidos e identificadores inventados. Examinar também repetição degenerada, definida no código por um bloco de pelo menos 20 tokens repetido três vezes seguidas. Parar em 512 tokens não corrige uma repetição; o incidente conserva seu registro.

**Regra decidida:** a penalidade 1,05 só pode entrar se houver comprovação, na implementação fixada, de que os tokens do prompt ficam excluídos e nenhum item antes preservado se perde nos casos pareados. O teste realizado com Transformers não comprova esse comportamento em llama.cpp. Sem essa comprovação, a penalidade permanece 1,0.

Se houver repetição degenerada na política principal, testar uma única alternativa previamente definida: amostragem com temperatura 0,7, top-p 0,8, top-k 20, min-p 0, penalidades adicionais zeradas e semente principal 42. Aplicar a alternativa a todas as configurações e repetir os 36 casos. Se persistirem falhas nos controles críticos, corrigir a implementação e repetir a calibração antes de prosseguir. O tempo gasto entra no orçamento.

**Concluído quando:** o registro definir uma política única, listar a fidelidade alcançada e justificar os incidentes. Perdas críticas dos controles impedem liberar a etapa final. Casos técnicos e suas famílias ficam fora da etapa final.

## 7. Executar o piloto e fechar seu diagnóstico

**Meta principal:** 60 perguntas em cinco classes: direta, condição, exceção, ambiguidade e insuficiência na coleção.

| Escopo fixado | Perguntas por banco e classe | Principais | Perguntas de estabilidade | Saídas adicionais | Total |
|---|---:|---:|---:|---:|---:|
| Três bancos | 4 | 360 | 15 | 90 | 450 |
| Dois bancos | 6 | 360 | 20 | 120 | 480 |

A estabilidade mantém a seleção por hash e o arredondamento por banco e classe do código: `floor(n × 0,25 + 0,5)`. Com seis perguntas por grupo, seleciona duas. Portanto, o cenário de dois bancos tem 480 saídas, e a proporção efetiva de estabilidade é 33,3%. O relatório apresenta esse valor.

Reservar famílias para a etapa final antes de montar o piloto. No piloto, cada família fornece no máximo três perguntas, com a dependência declarada. Se a coleção não sustentar as 60 perguntas elegíveis e a reserva final, ampliar uma rodada dirigida de até 40 URLs por banco ativo. Persistindo cobertura insuficiente, fixar um piloto menor com distribuição e lacunas explícitas, sem completar células com perguntas sem suporte.

**Execução:** checkpoints por pergunta e identificação por fase, pergunta, configuração e semente. Uma falha técnica recebe uma repetição com os mesmos parâmetros. Falha persistente é registrada como incidente, sem trocar o modelo daquela configuração.

**Concluído quando:** todas as chamadas previstas na amostra realmente fixada tiverem resultado ou falha registrada; estabilidade, cortes, fontes excluídas, tempos e memória estiverem reportados; e uma decisão de avanço definir correções, método e disponibilidade de famílias finais.

## 8. Implementar avaliação automática com casos inconclusivos tratados

**Ação:** integrar checagens de valores, unidades, datas, fontes, cobertura e exclusões do filtro. Integrar um julgamento local por modelo com rubrica congelada, referência e passagens originais. Ocultar configuração, semente e prefixo de busca; conservar IDs das fontes. Fixar versão, instrução, ordem e política de geração.

A saída estruturada informa adequação automática `1`, `0` ou `inconclusiva`, requisitos atendidos e ausentes, afirmações incompatíveis, aplicabilidade em atributos filtrados e não filtrados e justificativa ancorada. Um resultado inconclusivo conserva seu motivo. Falha técnica persistente recebe zero somente no indicador operacional de sucesso de execução; seu conteúdo fica sem nota.

Antes das respostas reais, testar o avaliador em 20 casos sintéticos de resultado conhecido, incluindo omissão, inversão de condição, valor errado, fonte inventada, esclarecimento e abstinência pertinente. Critério funcional: pelo menos 19 decisões corretas e todas as saídas estruturalmente válidas. Corrigir uma vez e executar um segundo conjunto congelado de 20 casos. Essa checagem não estima validade do julgamento em documentos reais.

**Alternativa:** se o critério continuar não atendido, a adequação por IA sai do desfecho principal; o estudo concluído reporta recuperação, cobertura, exclusões, fidelidade literal e funcionamento. H1/H2/H3 recebem interpretação limitada aos diagnósticos disponíveis, sem alegar adequação medida. Essa decisão ocorre antes da etapa final.

Quando o avaliador passar, realizar uma segunda leitura automática em 20% das saídas, estratificadas por banco, classe e configuração, mais as saídas inconclusivas ou inválidas. Compartilhamento de modelo fica declarado; concordância é consistência automática, sem atribuição de independência humana. Divergências sem resolução permanecem inconclusivas.

**Concluído quando:** todas as saídas tiverem diagnóstico, nota automática ou motivo de inconclusão e tratamento analítico definido. A execução não depende de fichas manuais de Yago.

## 9. Fixar amostra, registro e controle da etapa final

**Decisão:** estudo final exploratório, com alvo de até 60 perguntas novas, uma por família e separação de todas as famílias observadas no piloto e nos testes. Selecionar a maior amostra equilibrada que a reserva sustentar, com até 60 perguntas. Procurar pelo menos quatro perguntas por banco e classe; células insuficientes ficam explícitas. A amostra menor pode concluir um estudo exploratório com cobertura delimitada.

Simular a precisão antes de gerar respostas finais, usando a composição disponível por banco e classe e discordância estimada no piloto, com cenários de 0,10, 0,25 e 0,40. Usar 2.000 repetições e semente registrada. Apresentar a largura esperada dos intervalos e a disponibilidade por contraste; não prometer meia largura de dez pontos com uma amostra que não a sustenta. Amostra e orçamento são fixados sem ampliação após conhecer o efeito final.

Publicar uma versão prospectiva do método e do manifesto, ancorada em commit e release datada no GitHub, antes das respostas finais. Esse registro próprio conserva o histórico de mudanças e a evidência de que o teste técnico e o piloto já eram conhecidos. Preparar também o pacote de depósito externo. OSF ou Zenodo e DOI entram no relato quando houver depósito efetivo e acesso disponível; o núcleo usa a versão pública verificável do projeto e descreve seu tipo de registro.

Adaptar o controle final: aceitar revisão assistida registrada, exigir a versão pública do adendo, hashes de todas as entradas, exclusões de famílias e decisões de fontes, amostra, fidelidade e avaliação. Preservar os controles de integridade e a distinção entre origem humana e automática.

**Concluído quando:** a release prospectiva existir e a verificação automática de todos os requisitos passar. A etapa final só começa depois desse resultado.

## 10. Executar a etapa final e analisar o conjunto completo

Gerar seis respostas principais por pergunta e estabilidade no subconjunto definido pela mesma regra do piloto. Calcular o número de chamadas a partir da amostra efetiva, antes de executar. Reusar índices congelados e avaliar com a política fixada.

**Análises:** H1, B × A, e H3, B × Bp, nas classes condição e exceção; H2, C × B, em perguntas com filtro explícito codificável. Reportar denominadores próprios por banco, classe e família, cobertura em 3/5/10, evidências necessárias excluídas, aplicabilidade e limites do contexto.

Escores automáticos completos permitem diferenças pareadas e intervalos de 95% com 5.000 reamostragens de famílias dentro de banco e semente fixada. Reportar a estimativa em pontos percentuais e sua relação com a magnitude de interesse de dez pontos, sempre como análise exploratória.

**Inconclusivos:** estender o analisador para conservar todos os denominadores e apresentar limites de pior e melhor caso, atribuindo possibilidades 0/1 aos escores desconhecidos. Pares inteiramente resolvidos podem ter uma análise descritiva adicional, com o viés de seleção explicitado. Não converter dúvida semântica em zero nem descartar silenciosamente pares. Falhas operacionais são analisadas em indicador separado.

**Concluído quando:** resultados, denominadores, incerteza, sensibilidade e falhas puderem ser reproduzidos a partir dos arquivos, e a matriz associar cada falha observada a uma intervenção documental com evidência. Exemplos de benefício e dano da filtragem usam casos efetivamente observados quando disponíveis.

## 11. Concluir publicação, linguagem e material de artigo

Atualizar README, catálogo, relatório, exemplos e `CITATION.cff`; publicar uma release de resultados com manifesto e testes. Código e arquivos derivados próprios têm direitos separados dos documentos coletados. Preparar propostas de licença para aprovação autoral; direitos ainda não definidos ficam explicitados, sem atribuir uma licença aberta às fontes bancárias.

Usar frases curtas, glossário, exemplo completo e comandos copiáveis. Aplicar revisão automática de termos sem explicação, siglas, links, passos incompletos e consistência. Rodar o percurso de instalação em ambiente limpo, gerar um exemplo e comparar seu resultado esperado. Testes reais de compreensão com leitores e validação humana independente ficam fora do núcleo automatizado e são declarados como não realizados.

**Rota editorial:** conferir política de IA antes de escolher o periódico. As diretrizes da Múltiplos Olhares consultadas em 11/10/2026 restringem IA para leitura e interpretação textual e limitam sua utilização declarada. O estudo assistido exige exame de compatibilidade; o uso de IA na própria redação também precisa ser declarado. Preparar consulta editorial, sem envio automático, e verificar duas alternativas com política compatível. A pesquisa, os registros e o pacote de artigo prosseguem sem aguardar uma resposta editorial. A submissão fica limitada a um destino com compatibilidade demonstrada.

Para Múltiplos Olhares, conferir o template oficial, anonimização e propriedades do arquivo, elementos iniciais em português/inglês/espanhol, resumos de 150–250 palavras e declarações suplementares. As regras atuais têm prioridade sobre a sugestão anterior de resumo com aproximadamente 140 palavras. A declaração de IA abrange Codex, ChatGPT e ferramentas realmente utilizadas; a revisão exata indisponível é informada como indisponível. Declarar o vínculo profissional de Yago com o Inter, uso exclusivo de fontes públicas e pesquisa independente.

Conferir cada referência diretamente na fonte, inclusive Dadopoulos, OmniEval e a autoria institucional da página de recuperação contextual. A revisão de manuscrito preserva equações editáveis, orçamento coerente com a amostra executada, tempos verbais consistentes e conclusão útil ao leitor. Submissão e aceite editorial conservam seus próprios estados externos.

**Concluído quando:** o pacote científico tiver versão identificada, dados publicáveis separados, reprodução conferida e material de artigo coerente com o método realmente executado. A rota de submissão tem sua decisão documentada, sem alegação automática de aderência ou aceite.

Fontes oficiais para essa verificação: [diretrizes da revista](https://periodicos.ufmg.br/index.php/moci/about/submissions) e [documentação do Qwen na revisão usada](https://huggingface.co/Qwen/Qwen3-8B-GGUF/blob/7c41481f57cb95916b40956ab2f0b139b296d974/README.md).

## 12. Tempo, retomada e sua participação

**Ordem operacional:** fontes → coleção → famílias e referências → integração e calibração → piloto → decisão e registro → etapa final → análise e publicação. Geração e avaliação usam processos retomáveis; os arquivos sobrevivem a uma interrupção mediante checkpoints e pacotes persistidos. Não há promessa de execução em segundo plano após encerrar uma sessão sem infraestrutura apropriada.

No teste já executado, a mediana principal foi 84,3 segundos por resposta. Uma extrapolação simples fornece aproximadamente 10,5 horas para 450 gerações ou 11,2 horas para 480, antes de preparação, avaliação e incidentes. Uma etapa final de igual tamanho acrescenta tempo semelhante. O julgamento e a preparação assistida precisam de medição própria; dois lotes de 450 somam cerca de 21 horas somente de geração nesse cenário. Tamanho dos contextos e uso do equipamento mudam esses números.

A meta de uma jornada permanece para coleta e preparação possível. O processamento completo é organizado em lotes automáticos, com duração medida, sem impor horas de anotação semanais a Yago. Usar GPU somente se já disponível e validada, mantendo precisão e parâmetros congelados; uma mudança de implementação exige nova calibração. Nenhuma despesa é pressuposta.

**Codex:** pesquisa, programação, operação dos lotes, arquivos, diagnóstico, correções e publicação no escopo autorizado. **Yago:** decisões autorais, aprovação de licenças, assinatura das declarações e aprovação final do artigo. Acesso a uma conta externa pode exigir uma ação pontual; o plano mantém alternativas que preservam o avanço técnico.

## Critério global de encerramento

O projeto é encerrado na versão entregue quando há escopo decidido, fontes resolvidas, coleção auditável, entradas congeladas, execução completa da amostra fixada, calibração documentada, avaliação com inconclusivos tratados, análise reproduzível, release de resultados e material de artigo consistente. Cada item informa estado e arquivo comprobatório. Redução de amostra, exclusão de fonte e limitação de desfecho são mudanças de método declaradas. Etapas experimentais que falharam continuam com estado de falha até a correção.
