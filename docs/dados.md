# Como preencher os dados

[Voltar ao início](../README.md) · [Consultar palavras técnicas](glossario.md)

Os nomes dos campos do código estão em inglês. As tabelas abaixo explicam o que cada um guarda.

## Fonte a coletar

Modelo: [sources.example.json](../configs/sources.example.json).

| Campo | O que preencher |
|---|---|
| `bank` | Identificador do banco. Use o mesmo nome em todos os arquivos desse banco. |
| `host` | Domínio oficial aprovado, como `www.example.org`. |
| `urls` | Lista dos endereços dos documentos selecionados. |
| `terms_url` | Endereço dos termos de uso revisados. |
| `terms_checked_at` | Data da revisão. |
| `collection_permission` | `pending` enquanto a revisão estiver pendente; `approved` após decisão documentada. |
| `reviewer` | Responsável pela revisão da fonte. |
| `permission_evidence` | Evidência e justificativa da decisão. |
| `redistribution` | Decisão específica sobre publicar cópias dos documentos. |

Registre bancos candidatos e excluídos em uma tabela separada, com as justificativas.

## Pergunta

Modelo: [questions.jsonl](../examples/questions.jsonl).

| Campo | O que guarda |
|---|---|
| `id` | Código único da pergunta. Use letras sem acento, números, hífen ou sublinhado. |
| `bank` | Banco ao qual a pergunta se refere. |
| `family` | Família da regra, com identificação do banco. |
| `class` | Grupo principal da pergunta. |
| `question` | Texto da pergunta. |
| `query_attributes` | Produto e público explícitos na pergunta, já codificados pelo pesquisador. |
| `origin` | Origem da pergunta: canal oficial ou elaboração do pesquisador. |

Os grupos aceitos pelo código são `direta`, `condicao`, `excecao`, `ambiguidade` e `insuficiencia`.

Se produto e público não estiverem explícitos, use `{}` em `query_attributes`. O código não tenta adivinhar esses valores.

## Descrição do trecho

Modelo: [metadata.json](../examples/metadata.json).

O arquivo usa o ID de cada trecho como chave. Cada descrição contém listas de produto e público, tipo de documento, evidência textual e registro da decisão documentada.

Use `geral` quando a fonte comprovar alcance geral. Use `desconhecido` quando o valor não puder ser determinado. Essas categorias ficam sozinhas na lista do atributo.

A fonte precisa justificar os valores. Yago conserva a versão inicial e as revisões individuais. `adjudication_id` mantém o nome técnico do campo e identifica uma decisão registrada, sem implicar consenso entre pessoas.

## Referência de avaliação

Modelo: [dossiers.jsonl](../examples/dossiers.jsonl).

| Campo | O que guarda |
|---|---|
| `question_id` | Pergunta avaliada. |
| `answerable` | Se a coleção permite responder. |
| `required_attributes` | Características que a informação precisa atender. |
| `mandatory_requirements` | O que uma resposta adequada precisa preservar. |
| `reference_units` | Códigos das passagens de referência. |
| `sufficient_sets` | Conjuntos alternativos de passagens que bastam para responder. |
| `expected_action` | Resposta, esclarecimento ou reconhecimento da falta de evidência. |
| `adjudication_id` | Registro da decisão individual sobre a referência. |

O arquivo [unit_map.json](../examples/unit_map.json) liga os IDs dos trechos às passagens de referência. Passagens repetidas em trechos sobrepostos usam o mesmo código de evidência.

## Anotação individual

Modelo: [annotations.template.csv](../examples/annotations.template.csv).

Cada linha registra item, atributo, pessoa ou rodada, valor, evidência e tempo. No estudo individual, `rodada1` e `rodada2` correspondem ao mesmo pesquisador. Para campos que são conjuntos, escreva uma lista JSON na célula. Exemplos: `["alfa", "beta"]` ou `["E1", "E2"]`.

O comando `study.py agreement` exige duas anotações por item e atributo. Ele interrompe o cálculo se faltar um par.

## Julgamento principal individual

Modelo: [judgments.template.csv](../examples/judgments.template.csv).

Cada linha contém `question_id`, `config`, `adequacy`, `adjudication_id` e `reason`.

Use `0` ou `1` para adequação. Inclua somente a resposta principal de cada pergunta e configuração. Guarde as respostas de estabilidade em outra tabela.

Esse arquivo registra a primeira avaliação individual. O formulário J1 e a segunda passagem da amostra permanecem preservados. A chave privada relaciona IDs com configurações somente após os julgamentos.

## Liberação da etapa final

Modelo: [freeze.template.json](../examples/freeze.template.json).

Registre o endereço público do plano, a data e os documentos das decisões. Preencha os códigos dos dados e índices em `input_hashes`.

O modelo de arquivo começa com valores vazios. Eles não indicam aprovação. A execução final exige registros reais e arquivos correspondentes.

## Cuidados com os exemplos

Cada arquivo em `examples/` mostra um formato ou um caso fictício. Os arquivos de pergunta, dossiê e metadados não formam uma coleção completa para rodar E5/Qwen. A demonstração `demo.py` oferece dois casos completos para aprendizagem.
