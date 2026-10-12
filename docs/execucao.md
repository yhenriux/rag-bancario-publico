# Execute uma nova coleção ou retome os registros

[Início](../README.md) · [Reprodução sem modelos](reproducao.md) · [Formato dos dados](dados.md)

Para repetir somente as contas publicadas, use `python replay_results.py`. Os passos abaixo são para uma nova coleta ou para trabalhar com o pacote privado correspondente à execução.

## Nova coleta

Python 3.11 ou superior. Instale as dependências leves:

```bash
python -m pip install 'beautifulsoup4>=4.12,<5' 'pypdf>=5,<7'
```

Preencha um cadastro próprio a partir de [sources.example.json](../configs/sources.example.json). Registre as condições de uso antes de liberar um endereço. `approved` significa liberação operacional registrada do projeto.

```bash
python batch.py preflight configs/candidates.json private/access-check.json --user-agent "RAGBankingStudy/0.3 (+https://github.com/yhenriux/rag-bancario-publico)"
python batch.py run private/sources.json data/nova-coleta --user-agent "RAGBankingStudy/0.3 (email-real@instituicao.edu)"
```

Use uma pasta nova. Falhas são registradas. `--allow-partial` conserva as extrações utilizáveis e registra as exclusões; não aprova automaticamente a coleção.

## Preparação assistida

O catálogo do lote localiza passagens candidatas. A preparação de metadados e dossiês continua declarando sua origem. Na execução aplicada, `dataset.py` prepara os conjuntos e aceita `--id-map` para fontes que mudaram na recuperação.

A segmentação e os índices estão em `experiment.py`; as entradas reais de busca e geração estão em `execution.py`. Consulte `python arquivo.py --help` para os argumentos. Esses passos exigem dependências e pesos indicados em `requirements.txt` e revisões fixadas.

## Fechamento com rankings já calculados

Após restaurar o pacote privado dentro do repositório:

```bash
python close_documentary.py private/resume-20261012 private/analise-recalculada
```

O comando verifica referências e separação de famílias, recalcula as medidas de busca e registra a geração parcial. Não chama modelos nem altera rankings. A pasta de saída precisa ser nova.

## Geração opcional

`gguf.py local` inicia e encerra o servidor llama.cpp, preservando cada resposta. O módulo usado tem contexto de 8.192 tokens, oito threads, lote 512, micro-lote 128, reorganização de pesos desativada e cache global zero. Os parâmetros e hashes estão nos registros do pacote.

A retomada reutiliza somente respostas com entradas, parâmetros e runtime correspondentes. Alterações exigem uma pasta nova. A geração final mantém controles próprios e não está liberada pela conclusão da análise documental. A entrega atual não exige terminar esse módulo.

## Erros comuns

| Situação | Ação |
|---|---|
| Pasta de saída existente | Escolha outro destino para preservar resultados anteriores |
| Checkpoint divergente | Confira entradas e runtime; não force sua reutilização |
| Falta de pacote Python | Instale as dependências da etapa que está executando |
| Fonte bloqueada ou inacessível | Registre a exclusão e respeite a condição de acesso |
| Nova coleta produz resultados diferentes | Registre novos hashes e trate como outra versão da coleção |
