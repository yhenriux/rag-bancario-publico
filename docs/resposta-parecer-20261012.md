# Resposta crítica ao parecer de 12 de outubro de 2026

[Manuscrito vigente](manuscrito.md) · [Matriz](diagnostico-20261012/matrix.md) · [Cálculos](diagnostico-20261012/diagnostics.json) · [Versão anterior](arquivo/manuscrito-antes-parecer-20261012.md)

O parecer foi confrontado com os rankings, as referências e as fontes bibliográficas. As revisões mantêm o título escolhido pelo autor e o estudo de recuperação. Nenhuma coleta, pergunta, âncora, metadado ou ranking original foi alterado. A análise adicional é posterior ao parecer, com hashes das entradas. A versão anterior fica arquivada para conservar informações e decisões.

## Decisões e evidências

| Recomendação ou afirmação | Decisão | Aplicação e fundamento |
|---|---|---|
| Reenquadrar como caso diagnóstico | Acolhida | Introdução, pergunta de pesquisa, resumo, discussão e conclusão delimitam estudo de caso diagnóstico e exploratório da recuperação. |
| Substituir o título | Adaptada | Mantido o título escolhido pelo autor, que já explicita recuperação de evidências. O texto delimita a etapa de RAG efetivamente medida e não reivindica correção de respostas. |
| Formular pergunta e lacuna | Acolhida | Pergunta literal e lacuna circunscrita aos trabalhos consultados; seleção dirigida, sem alegar revisão sistemática ou inexistência de literatura. |
| B05 e BF04 são as únicas diferenças C–B | Acolhida com correção | São as únicas diferenças de recall@5 e cobertura@5. Em recall@1 também há I08 no piloto. As listas ordenadas diferem em 17/20 e 9/10 perguntas, inclusive perguntas sem referência. |
| Candidatos por banco seriam cerca de metade dos 62 trechos | Corrigida | Catálogo contém 18 trechos do Inter e 44 do Bradesco. A análise informa os valores exatos. |
| Tratar a circularidade com regra congelada ou segundo anotador | Adaptada | Sensibilidade posterior retira os campos previamente classificados como inferidos em B05 e BF04. B05 equivale a B e perde a vantagem; BF04 mantém C e a falha. Não se inventa anotador, kappa ou independência retrospectiva. Novos casos independentes continuam necessários. |
| Demonstrar regra antes de olhar referências | Não reivindicada | Os resultados já eram conhecidos. A regra de sensibilidade usa a auditoria existente, mas é pós-hoc e não equivale a extração independente congelada antes do experimento. |
| Intervenção Aeternum não mede generalização | Acolhida | Retirada do resumo; explicada como verificação de mecanismo no caso conhecido, separada dos resultados originais. |
| Acrescentar recall@1/3 e MRR | Acolhida | Incluídos cortes 1, 3, 5 e 10, posições de cada âncora e MRR@10. NR significa ausência nas dez posições publicadas; não ausência em toda a coleção. MRR não certifica cobertura ou suficiência. |
| Discutir BM25 | Acolhida | Discussão própria: competitivo no piloto e melhor acesso inicial no segundo conjunto. Não se assume necessidade de busca semântica ou benefício de busca híbrida não executada. |
| Chamar final de segundo conjunto e esclarecer Bp | Acolhida | Texto usa segundo conjunto. IDs de arquivos permanecem `final` por rastreabilidade. Bp consta do protocolo original e das entradas anteriores à geração do piloto. |
| Trocar intervalos por casos discordantes | Acolhida com preservação | Corpo principal usa contagens e matriz 30 × 5. Bootstrap, fórmula, simulações e valores exatos ficam no Apêndice B e nos relatórios históricos. Não se apagam cálculos para favorecer a narrativa. |
| Usar fração 29/32 em lugar de 90,625% | Não aplicada | Recall é média das proporções por pergunta, com denominadores diferentes. A fração sugerida poderia mudar a definição. Corpo usa uma casa decimal; valores exatos continuam disponíveis. |
| Critério de dez pontos sugere relevância com amostra mínima | Acolhida | Retirado da interpretação principal. Apêndice explica que um caso binário em oito perguntas vale 12,5 pontos. |
| Mover geração e poder para suplemento; reduzir método a 60% | Adaptada | Parâmetros, orçamento, fidelidade, calibração, 56 respostas e dimensionamento ficam no Apêndice B. O percentual arbitrário não orienta cortes; informação necessária ao método de busca permanece no corpo. |
| Incluir organização do conhecimento e avaliação clássica | Acolhida | SKOS, escopo público da ISO 25964-1, Manning et al., BM25, E5, FinanceBench e vieses de avaliadores foram acrescentados. A implementação não é declarada conforme SKOS ou ISO. |
| Aumentar para 25–35 referências | Adaptada | A bibliografia passa de oito a dezesseis referências pertinentes e verificadas quanto ao alcance utilizado. Não se acrescentam fontes apenas para atingir uma contagem. |
| Leitura limitada poderia abranger Dadopoulos | Esclarecida | A limitação refere-se somente a Wilson. Dadopoulos foi consultado em texto completo. ISO é citada apenas pelo escopo público; a norma integral não foi consultada. |
| Citar anais de Lewis e Joren | Acolhida | Lewis usa NeurIPS 2020; Joren usa ICLR 2025. O PDF dos autores de Joren confirma publicação na ICLR na primeira página; acesso direto a OpenReview encontrou verificação de navegador. |
| Corrigir OmniEval para 5737–5762 | Não aplicada | Página definitiva e BibTeX da ACL informam 5726–5751, já corretos. A versão de preview mencionada pelo parecer não substitui a fonte definitiva. |
| Avaliador local sem calibração | Corrigida | Calibração foi realizada: 10/20 e 17/20, abaixo de 19/20. Trata-se de calibração insuficiente, com adequação desativada; não de ausência do procedimento. |
| Associar B05 à norma do Banco Central | Acolhida com limite | Resolução CMN nº 3.919, art. 2º, I, b, contextualiza a exceção de perda. Consulta posterior não altera coleção ou âncoras e não estima tarifa específica. |
| Reescrever resumos e reduzir repetições | Acolhida | Três resumos centram resultados com denominadores, definem âncoras e omitem a demonstração pós-hoc como resultado principal. Informação técnica repetida fica nos apêndices. |
| Trocar prefixo por cabeçalho contextual | Acolhida | Terminologia distingue descrição experimental e instrução da consulta E5. Os nomes técnicos históricos dos arquivos não mudam. |
| COI e IA em seção própria | Acolhida | Vínculo com Inter, critérios de seleção, ferramentas e responsabilidade ficam na seção 8; o método remete à declaração. |
| Delimitar reprodutibilidade | Acolhida | Reprodução pública de métricas sobre rankings congelados. Reexecutar busca exige textos, índices, modelos e versões privados. |
| DOI e instantâneos | Parcial | Instantâneos e hashes já são preservados em pacote privado. DOI não foi emitido; não se inventa depósito ou licença. Publicação externa permanece decisão autoral. |
| Política da revista | Conferida, sem declaração de conformidade | Múltiplos Olhares restringe IA em interpretação e redação. O uso real foi declarado, com incompatibilidade explicitada na documentação editorial. Formatação no template não significa elegibilidade editorial. |

## Fontes verificadas e alcance

- [SKOS, W3C](https://www.w3.org/TR/skos-reference/): conceitos, rótulos e relações hierárquicas; consulta à especificação pública.
- [ISO 25964-1:2011](https://www.iso.org/standard/53657.html): consulta à descrição pública, sem acesso ao texto integral pago.
- [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/): dados bibliográficos dos autores e capítulo de avaliação de rankings.
- [Robertson e Zaragoza, PDF dos autores](https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf): título, autoria, volume 3, número 4, páginas 333–389 e DOI no próprio PDF. Alguns catálogos atuais indicam paginação diferente; a referência acompanha o documento efetivamente consultado.
- [Relatório E5](https://arxiv.org/abs/2402.05672): treinamento e modelos de representações multilíngues; [modelo usado](https://huggingface.co/intfloat/multilingual-e5-large-instruct).
- [FinanceBench](https://arxiv.org/abs/2311.11944): domínio, perguntas e evidências no resumo dos autores.
- [LLM-as-a-Judge, NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html): vieses relatados e dados bibliográficos; sem atribuir ao Qwen um viés medido que este estudo não estimou.
- [Lewis, NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html): versão de anais e resumo.
- [Joren, ICLR 2025](https://openreview.net/forum?id=Jjr2Odj8DJ): endereço de anais; [PDF dos autores](https://arxiv.org/pdf/2411.06037) confirma publicação e permite consultar a definição de suficiência.
- [OmniEval, ACL definitiva](https://aclanthology.org/2025.emnlp-main.292/): 5726–5751, autoria, DOI e combinação de anotação humana e avaliadores ajustados.
- [Dadopoulos, versão 1](https://arxiv.org/html/2510.24402v1): método e comparações completos; contraste de seleção de arquivos inclui reescrita.
- [Contextual Retrieval, Anthropic](https://www.anthropic.com/engineering/contextual-retrieval): autoria de Daniel Ford nos agradecimentos, enriquecimento e combinação lexical/semântica.
- [Resolução CMN nº 3.919](https://www.bcb.gov.br/pre/normativos/res/2010/pdf/res_3919_v4_p.pdf): art. 2º, I, b; consulta contextual posterior.
- [Política de Múltiplos Olhares](https://periodicos.ufmg.br/index.php/moci/about/submissions): extensão, resumos, template e limites declarados de IA.

Conferência em 12 de outubro de 2026. Wilson e a identidade dos modelos continuam documentados nas referências anteriores; nenhum grau de leitura integral é presumido.

## Como repetir o diagnóstico acrescentado

```bash
python retrieval_diagnostics.py
```

Resultado esperado: `diagnostics_match: true` e `pairs: 150`. O cálculo usa apenas arquivos públicos e a biblioteca padrão do Python. Não gera novas respostas, não modifica entradas e não baixa modelos.
