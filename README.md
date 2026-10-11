# RAG Bancário Público

**Como uma inteligência artificial pode consultar documentos bancários e responder sem perder condições importantes?**

Este projeto estuda respostas sobre contas e cartões de bancos brasileiros. Ele compara formas de organizar e buscar documentos públicos. Também verifica se a resposta preserva as regras que valem para a situação da pessoa.

RAG significa *retrieval-augmented generation*, ou geração aumentada por recuperação. Aqui, isso quer dizer: **buscar informações em documentos antes de produzir uma resposta**.

## Um exemplo

Uma página informa que um cartão oferece isenção de anuidade quando a fatura mensal chega a R$ 1.000. A pessoa pergunta se tem isenção com uma fatura de R$ 600.

O sistema precisa encontrar a regra certa e explicar o limite de gasto. Citar a página e omitir esse limite pode levar a uma resposta inadequada.

Os valores e os cartões usados nos exemplos deste repositório são fictícios.

## Comece por aqui

| Você quer… | Abra… |
|---|---|
| Entender a ideia, sem programar | [O estudo em linguagem simples](docs/entenda-o-projeto.md) |
| Ver um exemplo no seu computador | [Primeiros passos](docs/primeiros-passos.md) |
| Preparar e executar a pesquisa | [Guia de execução](docs/execucao.md) |
| Ver o plano em lotes para uma jornada | [Planejamento completo](docs/plano-execucao.md) |
| Entender verificações e avaliações | [Guia de avaliação](docs/avaliacao.md) |
| Entender uma palavra técnica | [Glossário](docs/glossario.md) |
| Acompanhar o que já está pronto | [Plano de trabalho](docs/roadmap.md) |
| Consultar o desenho científico completo | [Adendo individual ativo](docs/protocolo-individual.md) |

## Veja a demonstração

Instale Python 3.11 ou superior e abra um terminal na pasta do projeto. Execute:

```bash
python demo.py
```

A demonstração mostra dois casos: um filtro retira uma regra de outro cartão; outro filtro perde uma regra geral necessária. Ela funciona sem baixar modelos de inteligência artificial e sem acessar sites de bancos.

Para conferir os testes do código:

```bash
python -m unittest discover -s tests -v
```

## O que o estudo compara

| Nome | Como o sistema busca informações |
|---|---|
| A | Busca pelo sentido do texto original. |
| B | Acrescenta título, seção, tipo de documento, produto e público à descrição usada na busca. |
| C | Usa a descrição de B e aplica um filtro de produto e público. |
| Bp | Acrescenta somente produto e público à descrição. |
| L | Busca pela correspondência de palavras, com o método BM25. |
| S | Produz uma resposta sem consultar documentos. |

BM25 é uma forma de ordenar textos pela presença das palavras da pergunta. A busca por sentido usa o modelo E5. O modelo Qwen produz as respostas. [Veja o que esses nomes significam](docs/glossario.md).

As descrições adicionais ajudam a buscar. O modelo que produz a resposta recebe o conteúdo original dos trechos encontrados.

## O que está pronto

- Coleta, extração e catálogo automático em um comando, após resolver as condições de acesso.
- Conferência real de robots.txt para seis candidatos, com data, hash e pendências.
- Registro dos endereços, das datas e dos códigos de conferência dos arquivos.
- Código das seis formas de busca e resposta.
- Demonstração com fontes fictícias.
- Formulários para avaliar respostas sem mostrar qual sistema as produziu.
- Cálculos de cobertura das fontes, concordância entre avaliadores e diferenças entre sistemas.
- Testes automáticos e guias para executar cada etapa.

**O corpus real e o piloto dos modelos ainda não foram executados.** A pré-conferência de acesso já começou. Codex auxilia no trabalho operacional; Yago é o único pesquisador. [Veja as fontes e os bloqueios](docs/fontes-e-acesso.md).

## Execução em lote

A meta é coletar e catalogar as fontes autorizadas em uma jornada. Codex prepara os cadastros, trata pendências e entrega os registros. Não há carga semanal nem catalogação manual obrigatória por Yago.

```bash
python batch.py run private/sources.json data/day-01 --user-agent "RAGBankingStudy/0.3 (email-real@instituicao.edu)"
```

O comando gera textos extraídos, catálogo CSV/JSONL, duplicatas e passagens literais com valores e condições. Requer Beautiful Soup e pypdf, além do cadastro aprovado. [Veja os comandos e seus pré-requisitos](docs/execucao.md).

Descrições semânticas, perguntas, referências e julgamento por IA ainda precisam de integração sobre os dados reais. Os modelos dependem de infraestrutura validada. Avaliações automáticas são identificadas como automáticas; o estudo assistido é exploratório. Validação humana fica como etapa adicional.

O [adendo ativo](docs/protocolo-individual.md) registra essa mudança. A meta de uma jornada não garante executar o experimento completo quando permissões ou equipamento estiverem pendentes.

## Documentação em linguagem simples

Usamos frases diretas, palavras comuns e exemplos próximos do problema. Explicamos os termos técnicos quando aparecem. A [política de linguagem simples](docs/linguagem-simples.md) adota como referência a Lei nº 15.263/2025 e inclui um roteiro para testar os textos com leitores iniciantes.

O [adendo individual](docs/protocolo-individual.md) define o desenho ativo. O [protocolo anterior](docs/protocolo.md) permanece preservado como histórico; seus requisitos de equipe, orçamento manual e julgamento humano foram substituídos pelo adendo nos pontos indicados.

## Contribua

Você pode apontar uma explicação confusa, relatar um problema ou sugerir uma melhoria. [Veja como contribuir](CONTRIBUTING.md).

Arquivos de coleta, dados de avaliação e chaves de identificação ficam fora do Git por padrão. Cada documento de um banco conserva seus próprios direitos de uso. [Veja as regras de publicação](docs/dados-e-publicacao.md).

**Responsável:** [Yago Henrique](https://github.com/yhenriux). Projeto independente de pesquisa. A seleção de bancos e a coleta usam fontes públicas.
