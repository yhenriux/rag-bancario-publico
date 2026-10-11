# Execute o estudo passo a passo

[Voltar ao início](../README.md) · [Consultar palavras técnicas](glossario.md)

Este guia serve à execução individual por Yago. O [adendo individual](protocolo-individual.md) define o desenho ativo. O código está preparado; a seleção dos bancos, o piloto e os julgamentos humanos ainda precisam acontecer.

Antes dos comandos, consulte o [planejamento completo](plano-execucao.md). Ele define os responsáveis, as entregas e as decisões necessárias para cada etapa.

## 1. Prepare o ambiente

Use Python 3.11 ou superior. Crie um ambiente separado para instalar os programas do projeto:

```bash
python -m venv .venv
```

Ative esse ambiente:

| Sistema | Comando |
|---|---|
| Windows, PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows, Prompt de Comando | `.venv\Scripts\activate.bat` |
| macOS ou Linux | `source .venv/bin/activate` |

Se o PowerShell bloquear a ativação, use o Prompt de Comando. Instale as dependências, que são os programas usados pelo código:

```bash
python -m pip install -r requirements.txt
```

PyTorch precisa corresponder ao equipamento. A geração usa precisão FP16 na GPU e FP32 na CPU. Esses nomes indicam a forma de representar números nos cálculos. Yago precisa verificar a memória disponível antes de baixar e executar os modelos.

Uma mudança de precisão ou quantização precisa ser testada e registrada para todas as configurações. Quantização é uma forma de reduzir a memória dos modelos.

## 2. Registre as versões dos modelos

O comando abaixo consulta a versão atual de E5 e Qwen e cria uma configuração local. Ele acessa o Hugging Face, serviço que guarda os modelos. Ele baixa somente informações de versão:

```bash
python prepare.py revisions configs/study.json private/study.json
```

Confira o campo `device` no arquivo criado. Use `cuda:0` para uma GPU compatível ou `cpu` para executar na CPU.

Conserve esse arquivo. O código exige versões identificadas por SHA, um código que aponta para uma revisão dos arquivos. [Veja o glossário](glossario.md).

As instruções de busca e resposta estão nessa configuração. Yago revisa e fixa seu texto antes da etapa final. Registre também as versões instaladas:

```bash
python -m pip freeze > private/dependencias.txt
```

## 3. Escolha as fontes

Selecione três bancos com conta e cartão para pessoa física e documentos oficiais públicos em português.

Registre todos os bancos considerados. Explique por que cada banco entra ou fica fora. Nenhum banco foi escolhido neste repositório.

Copie `configs/sources.example.json` para `private/sources.json`. Preencha os campos indicados em [Como preencher os dados](dados.md).

Revise os termos de uso e registre a decisão de coleta. O valor `approved` significa que uma pessoa revisou a fonte e autorizou sua inclusão no estudo.

## 4. Colete os documentos

Troque o contato de exemplo pelo contato real da pesquisa:

```bash
python collect.py collect private/sources.json data/pilot-snapshot --user-agent "RAGBankingStudy/0.2 (seu-email@instituicao.edu)"
```

O programa usa os endereços cadastrados. Ele verifica as regras de acesso do site, guarda cópias dos documentos e registra os códigos de conferência.

O arquivo `manifest.jsonl` registra as fontes coletadas. O arquivo `errors.jsonl` registra os problemas. Resolva os problemas antes de fixar a coleção do estudo.

O programa aceita páginas HTML, PDFs com texto e texto simples. Ele bloqueia acessos fora do domínio aprovado e arquivos acima de 20 MiB. Cada coleta precisa de uma nova pasta.

## 5. Revise o texto extraído

```bash
python collect.py extract data/pilot-snapshot data/pilot-documents.jsonl
```

Compare o texto extraído com o documento original. Confira valores, datas, títulos, tabelas, notas e exceções.

Guarde a versão revisada em `data/pilot-documents-reviewed.jsonl`. Após a revisão real, use `approved` no campo `extraction_review`.

Organize as seções no arquivo revisado. O código divide o texto dentro dessas seções.

PDFs sem texto precisam de reconhecimento de texto, chamado OCR, e revisão. Páginas que carregam o conteúdo por scripts podem exigir outra forma de captura. Registre qualquer mudança de método.

## 6. Divida os documentos em trechos

```bash
python experiment.py segment data/pilot-documents-reviewed.jsonl private/study.json data/pilot-chunks.jsonl
```

Cada trecho tem até 320 unidades de texto do modelo E5, chamadas tokens. Os trechos consecutivos compartilham até 48 tokens. Essa sobreposição ajuda a conservar o contexto perto de uma divisão.

O registro conserva o documento, a seção, as posições no texto e o código da fonte.

## 7. Prepare as anotações e perguntas

Yago prepara e congela as referências nas fontes originais antes das descrições de busca e das saídas. Depois descreve os documentos em `private/pilot-metadata.json`, preserva a versão inicial e registra a revisão individual.

Perguntas, famílias, dossiês e mapa de evidências ficam fixados antes da geração. A mesma pessoa conhece as fontes e os procedimentos; o estudo declara esse limite de independência.

O piloto tem 60 perguntas: quatro de cada grupo por banco. Use o formato de `examples/questions.jsonl`, mantendo o campo `origin` para indicar a origem real de cada pergunta.

Os exemplos do repositório são fictícios. Eles ensinam o formato e servem aos testes do código.

[Veja os papéis e os critérios de avaliação](avaliacao.md).

## 8. Prepare a busca e execute o piloto

```bash
python experiment.py index data/pilot-chunks.jsonl private/pilot-metadata.json private/study.json data/pilot-index
python experiment.py run private/study.json data/pilot-chunks.jsonl private/pilot-metadata.json private/pilot-questions.jsonl data/pilot-index runs/pilot --phase pilot
```

O primeiro comando prepara os índices, arquivos que permitem comparar a pergunta com os trechos. O segundo busca as fontes e produz respostas nas seis configurações.

E5 representa o sentido dos textos. Qwen recebe a pergunta e o texto original dos trechos encontrados. Os títulos e as descrições adicionais participam da busca.

O gerador recebe até 4.096 tokens e produz até 512 tokens de resposta. Se a entrada exceder o limite, o código retira os últimos trechos inteiros e registra a retirada.

A geração principal usa uma política fixa sem amostragem. O código usa duas sementes adicionais, 43 e 44, para verificar estabilidade em 25% das perguntas de A, B e C. Yago precisa aprovar e registrar a regra de arredondamento antes da etapa final.

## 9. Confira os problemas técnicos

O piloto precisa verificar se contextos idênticos produzem respostas idênticas na comparação principal.

O código registra repetição degenerada: um bloco de pelo menos vinte tokens repetido três vezes seguidas.

Se esse problema exigir ajuste, Yago executa o teste da penalidade e os doze casos de fidelidade:

```bash
python audit.py processor private/processor-check.json
python fidelity.py private/study.json examples/fidelity_cases.json runs/fidelity
```

O segundo comando produz 72 saídas técnicas e um formulário individual J1 com os rótulos ocultos. Yago confere valores, unidades, datas e identificadores. O piloto pode exigir 72 conferências adicionais.

Qualquer perda de um item antes preservado impede aceitar o ajuste. Persistência da repetição, falha de fidelidade ou incompatibilidade da implementação suspende a etapa final até revisão registrada.

O ajuste aceito usa penalidade 1,05 somente nos tokens já gerados. O parâmetro global fica em 1,0. A decisão deve existir antes dos escores de adequação. Ela vale para todas as configurações e para a estabilidade.

## 10. Prepare e avalie as respostas

Depois que a execução terminar, reúna as respostas e prepare os formulários:

```bash
python study.py combine runs/pilot private/pilot-runs.jsonl
python study.py blind private/pilot-runs.jsonl private/pilot-judging --judges 1
```

O primeiro comando verifica a conclusão da execução. O segundo oculta configuração e semente e muda a ordem das respostas para cada avaliador.

Yago usa somente J1 e as referências necessárias. Guarda a chave em arquivo separado e evita consultá-la durante o julgamento. O conhecimento anterior limita o cegamento.

Preserve a primeira avaliação e reavalie 20% após no mínimo 14 dias, sem consultar a primeira marcação. Use a segunda passagem como diagnóstico de consistência. Separe respostas principais e estabilidade.

## 11. Compare as avaliações e calcule os resultados

Para comparar duas passagens da mesma pessoa na amostra revisada:

```bash
python study.py agreement private/metadata-annotations.csv runs/metadata-agreement.json --annotators rodada1 rodada2 --set-attributes product public
```

Use o mesmo comando para descrições, referências ou julgamentos reavaliados. `rodada1` e `rodada2` identificam Yago em dois momentos. Relate consistência intra-avaliador; não são pessoas independentes. Campos que representam conjuntos precisam de listas JSON no CSV.

Para analisar as respostas principais já avaliadas:

```bash
python study.py analyze private/pilot-questions.jsonl private/pilot-judgments.csv runs/pilot-analysis.json
python audit.py retrieval runs/pilot/retrieval.jsonl private/pilot-dossiers.jsonl private/pilot-unit-map.json runs/pilot-retrieval-metrics.jsonl
```

A análise compara perguntas emparelhadas e calcula intervalos com 5.000 reamostragens das famílias dentro de cada banco. A interpretação automática é exploratória.

O mapa de evidências relaciona passagens de referência e trechos. Ele evita contar a mesma evidência várias vezes.

## 12. Prepare a etapa final

Use o piloto para medir esforço, contar famílias elegíveis e planejar a amostra. O dimensionamento por simulação continua pendente. Sua implementação e suas suposições precisam ser revistas com a estrutura encontrada no piloto.

Retire todas as perguntas e famílias do piloto da etapa final, incluindo paráfrases. Registre essas famílias no campo `pilot_families`.

Fixe perguntas, critérios, modelos e orçamento. Deposite o plano público datado antes da coleta final. Preencha `examples/freeze.template.json` com os registros reais.

Calcule os códigos dos arquivos:

```bash
python prepare.py hashes private/input-hashes.json config=private/study.json chunks=data/final-chunks.jsonl metadata=private/final-metadata.json questions=private/final-questions.jsonl index_inputs=data/final-index/inputs.json index_A=data/final-index/A.pt index_B=data/final-index/B.pt index_Bp=data/final-index/Bp.pt
```

Inclua esses códigos no campo `input_hashes` de `private/freeze.json`. O código confere os arquivos. Yago verifica o conteúdo das decisões e a anterioridade do depósito.

Execute a etapa final:

```bash
python experiment.py run private/study.json data/final-chunks.jsonl private/final-metadata.json private/final-questions.jsonl data/final-index runs/final --phase final --gate private/freeze.json
```

Repita os controles de geração, avaliação e análise. A análise permanece exploratória conforme o [adendo individual](protocolo-individual.md).
