# Comandos para execução em lote

[Voltar ao início](../README.md) · [Plano de uma jornada](plano-execucao.md) · [Adendo ativo](protocolo-individual.md)

Codex conduz o trabalho operacional e registra os resultados. Os comandos abaixo descrevem o que existe no código. Coleta e catálogo estão encadeados; a preparação semântica e o piloto completo ainda precisam de integração e validação no ambiente disponível.

## Prepare somente o necessário

Python 3.11 ou superior. Para coleta, extração e catálogo, instalar apenas as duas dependências leves:

```bash
python -m pip install 'beautifulsoup4>=4.12,<5' 'pypdf>=5,<7'
```

PyTorch e Transformers são necessários na etapa dos modelos. A instalação completa está em `requirements.txt`; verificar equipamento e memória antes de baixar modelos grandes.

## Confira caminhos sem baixar documentos

```bash
python batch.py preflight configs/candidates.json private/access-check.json --user-agent "RAGBankingStudy/0.3 (+https://github.com/yhenriux/rag-bancario-publico)"
```

O comando consulta robots.txt e registra resultados ou erros. Ele não aprova permissões. O [relatório publicado](access-preflight.json) contém uma conferência real dos seis candidatos.

## Colete, extraia e catalogue

Codex prepara o cadastro completo com as fontes e decisões documentadas. O modelo está em [sources.example.json](../configs/sources.example.json). O cadastro de candidatos não serve diretamente à coleta.

```bash
python batch.py run private/sources.json data/day-01 --user-agent "RAGBankingStudy/0.3 (email-real@instituicao.edu)"
```

Cada execução usa uma pasta nova. Somente fontes aprovadas entram no lote. O programa mantém os controles de domínio, redirecionamento, robots.txt e intervalo de acesso. Por padrão, falhas de coleta interrompem a sequência e ficam em `snapshot/errors.jsonl`. Com `--allow-partial`, o lote conserva documentos utilizáveis e registra erros de coleta e extração. Esse modo não congela a coleção final.

Arquivos entregues:

| Arquivo | Conteúdo |
|---|---|
| `snapshot/manifest.jsonl` | Origem, data, tipo de arquivo e hash |
| `snapshot/raw/` | Cópias da coleta, fora do Git |
| `documents.jsonl` | Texto extraído, com revisão pendente |
| `catalog/catalog.csv` | Catálogo legível em uma planilha |
| `catalog/catalog.jsonl` | Catálogo para processamento |
| `catalog/critical-passages.jsonl` | Passagens literais com posição no texto |
| `catalog/summary.json` | Contagens de documentos, duplicatas e alertas |

Para catalogar uma extração já existente:

```bash
python batch.py catalog data/documents.jsonl data/catalog
```

Valores exatos de produto e público ficam desconhecidos nesse catálogo determinístico. Codex prepara propostas semânticas com evidência em uma etapa separada. Anotações automáticas conservam sua origem e não recebem aprovação humana fictícia.

## Prepare a execução dos modelos

O código existente fixa revisões, divide textos, cria índices e compara seis configurações:

```bash
python prepare.py revisions configs/study.json private/study.json
python experiment.py segment data/pilot-documents-reviewed.jsonl private/study.json data/pilot-chunks.jsonl
python experiment.py index data/pilot-chunks.jsonl private/pilot-metadata.json private/study.json data/pilot-index
python experiment.py run private/study.json data/pilot-chunks.jsonl private/pilot-metadata.json private/pilot-questions.jsonl data/pilot-index runs/pilot --phase pilot
```

Esses comandos exigem dependências, modelos e arquivos reais já preparados. `segment` aceita revisão humana aprovada ou, com `--allow-assisted`, revisão `assisted_checked` que informe origem e registro. O rótulo assistido não representa revisão humana. O controle da etapa final ainda exige uma extensão registrada para aceitá-lo. Os exemplos fictícios não são uma coleção pronta para rodar esse piloto.

O [teste técnico de 11/10/2026](execucao-20261011.md) usa `technical.py prepare` e `technical.py generate`, com E5 e servidor local llama.cpp. O comando `technical.py local` inicia e encerra o servidor em uma só execução, recebendo o caminho do executável e dos pesos. Ele registra a alternativa GGUF e fica separado do piloto. Os caminhos das entradas são informados na linha de comando; pesos e bibliotecas são pré-requisitos.

A meta é 60 perguntas, quatro por banco e classe. A geração principal produz 360 saídas e a estabilidade acrescenta 90. Uma execução menor é registrada como teste técnico.

## Confira fidelidade e resultados

```bash
python audit.py processor private/processor-check.json
python fidelity.py private/study.json examples/fidelity_cases.json runs/fidelity
python study.py combine runs/pilot private/pilot-runs.jsonl
```

O teste de fidelidade produz 72 saídas quando necessário. Seu formulário humano permanece disponível como opção; não é uma tarefa obrigatória da jornada rápida. Um controle de fidelidade automático precisa de implementação e validação específicas.

Cobertura e diferenças podem ser calculadas após preparar referências, mapa de evidências e escores completos:

```bash
python audit.py retrieval runs/pilot/retrieval.jsonl private/pilot-dossiers.jsonl private/pilot-unit-map.json runs/pilot-retrieval-metrics.jsonl
python study.py analyze private/pilot-questions.jsonl private/pilot-judgments.csv runs/pilot-analysis.json
```

O programa estatístico recebe números e não determina sozinho se são humanos ou automáticos. O relatório e o registro associado identificam a origem de cada escore. Resultados com referências ou julgamentos automáticos permanecem exploratórios.

## Opção futura: avaliação humana

`study.py blind` e `study.py agreement` continuam disponíveis. Não há obrigação de preencher centenas de fichas ou esperar 14 dias na etapa rápida. Uma avaliação humana posterior exige plano próprio e relato do procedimento realmente executado.

## Etapa final

Excluir todas as perguntas e famílias do piloto, definir a amostra e registrar o desenho atualizado antes da etapa final. Os controles de hashes e liberação permanecem. O depósito público, a simulação de precisão e a etapa final ainda não foram executados.
