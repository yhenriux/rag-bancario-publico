# Resposta à reavaliação do manuscrito

[Manuscrito](manuscrito.md) · [Matriz](diagnostico-20261012/matrix.md) · [Suplemento](suplemento-metodo-20261012.md) · [Versão anterior](arquivo/manuscrito-antes-estratos-20261012.md)

A reavaliação foi confrontada com a versão vigente e os rankings congelados. As revisões abaixo preservam o título escolhido pelo autor, a coleção, as perguntas, os atributos, as âncoras, os rankings e as métricas anteriores. A estratificação é uma análise posterior, explicitada como tal. A nota editorial não é utilizada como critério para alterar dados ou escolher resultados.

| Ponto | Decisão e aplicação |
|---|---|
| Concentração do sinal no Bradesco | Acolhido. Acrescentados vinte estratos por banco, conjunto e configuração, com denominadores. Nas doze perguntas elegíveis do Inter, recall@5 é 100% em todas as configurações; diferenças de posição inicial permanecem. |
| Dependência dos rótulos de B05 | Acolhido. Texto explicita que conta diverge da palavra cartão da pergunta e coincide com a categoria da página-alvo, com plausibilidade no domínio e independência não verificada. |
| Sensibilidade determinística | Esclarecido. A remoção de campos verifica a consequência da política de seleção por construção. O texto a apresenta como verificação de dependência e não como validação independente da classificação. |
| Segundo anotador ou regra anterior às referências | Não simulados. Nenhum novo julgamento é apresentado como humano, independente ou definido antes de resultados já conhecidos. Essas extensões requerem outro desenho ou novos casos. |
| Intervenção ainda no resumo | Afirmação corrigida. A intervenção já havia saído do resumo. O resumo atual mantém a exclusão observada e delimita a verificação determinística. |
| BM25 como único sistema com recall@3 de 100% | Redação corrigida. B e L chegam a 100% no segundo conjunto. A vantagem de L aparece em recall@1 e MRR@10, com os valores de B explicitados. |
| Vazamento de processo editorial | Acolhido. Removidas as frases sobre diagnóstico acrescentado na revisão e verificação da política editorial. O Apêndice C foi realocado para o suplemento de proveniência. |
| Referência normativa | Atualizada para a versão v7 efetivamente consultada em 12/10/2026, publicada pelo Banco Central. Art. 2º, I, b confere. O número do arquivo não certifica isoladamente a vigência de toda a norma. A consulta não modifica o corpus. |
| OmniEval | Mantida paginação 5726–5751, conferida na fonte definitiva e já correta. |
| Norma lida apenas no escopo público | Alcance mantido explícito. A afirmação sobre ISO limita-se ao propósito que consta da descrição pública; o texto integral não foi consultado. |
| Literatura acadêmica de organização do conhecimento | Acrescentados Hjørland (2016a, 2016b) e Tudhope e Binding (2016), consultados em PDFs da editora. O debate sobre utilidade e domínio de uso das relações semânticas acompanha a interpretação do caso. |
| RAGAS e ARES | Acrescentados e consultados nos PDFs da ACL. Citados para separar avaliação do contexto e das respostas; não foram executados nem usados como certificação do avaliador local. |
| Contagem de referências | A versão anterior continha dezesseis. A atual contém 21 referências pertinentes. |
| Título sugerido | Mantido o título escolhido pelo autor, que explicita recuperação de evidências. O corpo delimita a etapa de RAG examinada. |
| Matriz autoexplicativa | Acrescentados banco, classe e número de âncoras distintas por pergunta. Os 150 desfechos permanecem iguais. |
| Equação sem raízes na extração | A equação Word contém duas raízes e uma fração como objeto nativo. A renderização confere; a extração textual perde o objeto. |
| Acrescentar distratores | Não inseridos retrospectivamente. Uma expansão requer critérios de seleção e resultados separados; os dados atuais não são ampliados para reduzir um teto já observado. |
| DOI | Nenhum depósito ou DOI é presumido. Instantâneos privados e materiais derivados estão preservados; licença e depósito externo continuam decisões autorais. |
| Score 6,4 | A média ponderada é 6,425. O score e sua margem expressam julgamento editorial, com incerteza não estatística. Não são estimativa de probabilidade de aceite. |

## Novas fontes primárias consultadas

- Hjørland, **Knowledge Organization (KO)**, 2016, p. 475–484: [PDF da editora](https://article.imrpress.com/journal/KO/43/6/10.5771/0943-7444-2016-6-475/cc0dfa4d10f580d91c58ef128585ac90.pdf).
- Hjørland, **Does the Traditional Thesaurus Have a Place in Modern Information Retrieval?**, 2016, p. 145–159: [PDF da editora](https://storage.imrpress.com/imr/journal/KO/article/505035/1752845959575.pdf).
- Tudhope e Binding, **Still Quite Popular After all Those Years**, 2016, p. 174–179: [PDF da editora](https://storage.imrpress.com/imr/journal/KO/article/505037/1752845965495.pdf).
- **RAGAS**, EACL 2024, p. 150–158: [PDF da ACL](https://aclanthology.org/2024.eacl-demo.16.pdf).
- **ARES**, NAACL 2024, p. 338–354: [PDF da ACL](https://aclanthology.org/2024.naacl-long.20.pdf).
- Resolução CMN nº 3.919: [versão v7 publicada pelo Banco Central](https://normativos.bcb.gov.br/Lists/Normativos/Attachments/49514/Res_3919_v7_P.pdf).
- **OmniEval**: [página definitiva da ACL](https://aclanthology.org/2025.emnlp-main.292/).

## Verificação dos cálculos

```bash
python replay_results.py
python retrieval_diagnostics.py
```

A primeira execução reproduz as métricas originais, reamostragens e intervenção posterior. A segunda confere o diagnóstico ampliado, incluindo os estratos e a matriz. O teste recompõe as médias agregadas a partir dos estratos e verifica o teto do Inter. Nenhuma chamada de modelo ou nova coleta é necessária.
