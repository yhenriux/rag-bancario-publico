# Encontre o código de cada etapa

[Início](../README.md) · [Método](metodo.md) · [Reprodução](reproducao.md)

| Etapa | Arquivo | Estado aplicado |
|---|---|---|
| Acesso e originais | `collect.py`, `batch.py` | Coleta limitada concluída e exclusões registradas |
| Extração e trechos | `collect.py`, `experiment.py` | 27 documentos e 62 trechos |
| Perguntas e dossiês | `dataset.py` | 20 perguntas piloto e 10 finais, sem famílias compartilhadas |
| Entradas dos modelos | `execution.py` | Rankings e prompts fixados antes da geração |
| Geração retomável | `gguf.py` | 56 respostas salvas; módulo parcial |
| Fidelidade | `audit.py` | 36 controles, 144 itens preservados |
| Calibração do juiz | `evaluate.py` | Qualidade insuficiente; adequação desativada |
| Medidas documentais | `audit.py`, `analysis_run.py` | Cálculos concluídos nos dois conjuntos |
| Fechamento documental | `close_documentary.py` | Auditoria e relatórios sem chamar modelos |
| Reprodução pública | `replay_results.py` | Recalcula medidas e intervalos com biblioteca padrão |
| Intervenção posterior | `intervention.py` | Demonstração BF04 separada dos resultados principais |
| Incerteza | `study.py` | 5.000 reamostragens exploratórias por família e banco |
| Integridade e links | `tests/`, `SHA256SUMS.json` | Verificações locais e no GitHub |

O protocolo original inclui procedimentos que não foram realizados. Sua existência no código ou no plano não implica execução. Avaliação humana, testes com leitores e geração completa ficam fora da entrega aplicada.
