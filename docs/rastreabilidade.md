# O que cada parte do código executa

[Voltar ao início](../README.md) · [Consultar palavras técnicas](glossario.md)

Esta tabela liga o [adendo individual ativo](protocolo-individual.md) e os procedimentos preservados aos arquivos do projeto. Ela também mostra o que continua pendente.

| Decisão da pesquisa | Arquivo ou comando | Situação |
|---|---|---|
| Preservar o plano científico | `docs/protocolo.md` | Cópia e código de integridade conferidos |
| Selecionar três bancos e justificar exclusões | Cadastro de fontes e guia de execução | Codex auxilia; decisão final pendente |
| Revisar termos de uso antes da coleta | `collect.py` | Bloqueio testado com dados fictícios |
| Guardar fonte, endereço, data e código | `collect.py` | Instantâneos testados; pré-conferência real de acesso registrada |
| Extrair páginas e PDFs | `collect.py extract` | Extração HTML testada em lote fictício; PDF real pendente |
| Revisar tabelas, valores e notas | Guia de execução | Alertas e assistência; validação humana adicional |
| Separar preparação e julgamento por etapas | Adendo individual e guia de avaliação | Um pesquisador com assistência; origem de cada anotação explícita |
| Retirar famílias do piloto da etapa final | `study.py check` e `experiment.py` | Validação testada |
| Dividir texto em trechos E5 | `experiment.py segment` | Código preparado; validação do modelo pendente |
| Comparar A, B, C, Bp, L e S | `experiment.py` | Código preparado; execução integrada dos modelos pendente |
| Conservar geral e desconhecido no filtro | `study.compatible` | Testado |
| Verificar perda de fonte pelo filtro | `demo.py`, `audit.py` | Demonstração e cálculos centrais testados |
| Usar o texto original na geração | `experiment.py run` | Código preparado; validação do modelo pendente |
| Registrar limite de entrada e retirada de fontes | `experiment.py` | Código preparado; execução pendente |
| Medir estabilidade em 25% das perguntas | `study.stability_sample` | Seleção testada; regra de arredondamento a aprovar |
| Conferir repetição e fidelidade | `audit.py`, `fidelity.py` | Detector testado; geração e conferências pendentes |
| Verificar penalidade na versão instalada | `audit.py processor` | Teste preparado; execução com Transformers pendente |
| Reunir respostas de uma execução completa | `study.py combine` | Testado |
| Ocultar o sistema e mudar a ordem das respostas | `study.py blind` | Exportação testada com exemplos fictícios |
| Comparar avaliações individuais | `study.py agreement` | Kappa, conjuntos e Jaccard testados; uso intra-avaliador entre rodadas |
| Avaliar adequação e aplicabilidade | Formulários e referências | Avaliação automática ainda sem integração; validação humana adicional |
| Calcular cobertura e recall | `audit.py retrieval` | Funções centrais testadas; referências reais pendentes |
| Comparar H1, H2 e H3 | `study.py analyze` | Testado com julgamentos fictícios |
| Calcular intervalos por família e banco | `study.paired_bootstrap` | Testado com dados fictícios |
| Planejar poder e precisão | Conta em `study.py budget` | Conta conferida; simulação da estrutura real pendente |
| Verificar dados fixados antes da etapa final | `prepare.py hashes`, `experiment.final_gate` | Códigos testados; decisões metodológicas humanas |
| Explicar termos e conferir links | Guias, glossário e testes | Links e exemplos conferidos; teste com leitores pendente |

## Limites da implementação atual

Os testes locais verificam o código com dados fictícios. A execução de E5 e Qwen precisa de validação no ambiente completo. A extração HTML integrada ao catálogo foi testada com uma fonte fictícia; a extração de PDFs reais continua pendente.

A análise de amostra por simulação ainda precisa ser implementada e revisada com dados do piloto. O código atual trata os resultados estatísticos como exploratórios.

Os arquivos de decisão conservam registros. Codex prepara os registros e Yago assume as decisões autorais. O depósito anterior à etapa final continua pendente.

## Automação da jornada

`batch.py preflight` verifica caminhos sem baixar documentos. `batch.py run` encadeia coleta aprovada, extração e catálogo. O catálogo localiza passagens literais por regras e mantém campos semânticos desconhecidos. Preparação semântica, julgamento por IA e piloto E5/Qwen ainda precisam de execução e validação.
