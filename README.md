# RAG Bancário Público

**Como a organização dos documentos ajuda ou prejudica a busca das evidências?** Este estudo explora essa pergunta em páginas públicas de Inter e Bradesco.

RAG é uma técnica que busca informações em documentos antes de produzir uma resposta com inteligência artificial. A entrega principal deste projeto examina a etapa de busca.

## Estado da entrega

| Parte | Estado em 12/10/2026 |
|---|---|
| Documentos e trechos | 27 documentos, divididos em 62 trechos |
| Perguntas | 30 perguntas próprias, em cinco classes |
| Comparações de busca | 150 pares de pergunta e configuração, concluídos |
| Referências | 43 âncoras com origem e posição conferidas por código |
| Geração complementar | 56 respostas salvas de uma execução parcial |
| Correção das respostas | Sem avaliação semântica validada |
| Publicação científica | Manuscrito para revisão autoral; sem submissão |

Os dados e referências foram preparados com apoio de IA. A amostra é pequena, escolhida por conveniência e sem revisão humana independente. O pesquisador trabalha no Inter; este projeto usa apenas fontes públicas e não representa o banco.

## Escolha por onde começar

- **Quero entender:** [explicação do projeto](docs/entenda-o-projeto.md).
- **Quero ver os achados:** [resultados e exemplos](docs/resultados.md).
- **Quero repetir as contas:** [reprodução em poucos comandos](docs/reproducao.md).
- **Quero consultar o artigo:** [manuscrito com resultados](docs/manuscrito.md).
- **Quero saber o método e seus limites:** [método aplicado](docs/metodo.md).
- **Quero coletar outra coleção:** [guia técnico](docs/execucao.md).
- **Quero localizar um arquivo:** [índice da documentação](docs/index.md).

## Repita a análise

Com Python 3.11 ou superior, na pasta do projeto:

```bash
python replay_results.py
```

Esse comando usa os rankings publicados. Não baixa modelos, não acessa os bancos e não precisa de pacotes adicionais. A saída deve indicar `metrics_match: true` e `bootstrap_match: true` nos dois conjuntos.

Para entender os filtros com casos fictícios:

```bash
python demo.py
```

## Cinco configurações de busca

| Código | O que muda |
|---|---|
| A | Busca por sentido no trecho original |
| B | Acrescenta título, seção, tipo, produto e público à representação |
| C | Usa a representação B e filtra por atributos preparados da pergunta |
| Bp | Acrescenta somente produto e público |
| L | Busca por palavras com BM25 |

Os atributos das perguntas incluem inferências assistidas. Seu uso foi registrado e não equivale a uma extração validada de perguntas reais. A configuração S, sem documentos, pertence somente à geração complementar.

## Principal resultado

Nas oito perguntas elegíveis do conjunto final, B, Bp e L encontram todas as âncoras nas primeiras cinco posições. A e C alcançam 87,5%. O filtro ajuda em uma pergunta do piloto e elimina uma referência em outra pergunta do conjunto final. [Veja os denominadores, os intervalos e os limites](docs/resultados.md).

## Dados, direitos e histórico

O GitHub publica código, perguntas próprias, posições das referências, hashes e resultados derivados. Os textos completos das fontes, prompts, pesos e respostas ficam fora do repositório. A conferência operacional das fontes não constitui autorização expressa dos bancos para redistribuição.

O [escopo atual](docs/escopo-atual.md) foi autorizado após o início da geração. O [protocolo original](docs/protocolo.md) permanece preservado como histórico. A geração completa e os testes com leitores podem integrar uma ampliação futura.

Para contribuir, consulte [CONTRIBUTING.md](CONTRIBUTING.md). Para citar, informe o endereço do repositório e o commit usado. A escolha da licença dos materiais autorais e da revista pertence ao pesquisador.
