# Plano de execução em uma jornada

[Voltar ao início](../README.md) · [Método ativo](protocolo-individual.md) · [Comandos](execucao.md)

**Meta:** executar seleção, conferência, coleta e catálogo em lote, com assistência de Codex. Yago recebe o resultado e uma lista curta de decisões. O plano dispensa horas semanais e uma equipe de anotadores.

## Entregas na ordem de execução

| Lote | O que Codex faz | Entrega verificável |
|---|---|---|
| 1. Fontes | Localiza páginas oficiais de contas e cartões; examina termos e robots.txt | Bancos candidatos, URLs, permissões e motivos de exclusão |
| 2. Coleta | Baixa as URLs aprovadas, respeita limites de acesso e registra falhas | Arquivos originais, data, endereço e hash de cada arquivo |
| 3. Catálogo | Extrai texto, identifica cópias iguais e localiza passagens com valores e condições | Catálogo CSV/JSONL, passagens literais e pendências |
| 4. Preparação | Sugere descrições, famílias de regras, perguntas e referências nas fontes | Arquivos com origem das anotações; versões congeladas |
| 5. Modelos | Verifica ambiente, versões, memória e uma execução pequena | Relatório técnico; tempo observado e bloqueios |
| 6. Piloto | Executa as seis configurações quando os pré-requisitos estiverem resolvidos | Saídas, fontes usadas, falhas e diagnóstico exploratório |
| 7. Publicação | Resume o que terminou e atualiza o GitHub | Código, relatório e decisões reproduzíveis, sem divulgar cópias sem direito de publicação |

Coleta e catalogação são a prioridade da jornada. PDFs digitalizados, páginas sem texto acessível, restrições de uso e falta de equipamento podem deixar uma fonte ou etapa pendente. A lista final indica exatamente o que foi feito e o que impediu o restante. Um bloqueio de acesso leva à análise de outra fonte, conservando o motivo da exclusão.

## O que já começou

A [pré-conferência técnica](access-preflight.json) registra consultas reais a robots.txt, sem baixar o corpus ou aprovar permissões. A [situação das fontes](fontes-e-acesso.md) registra decisões e limites de acesso. A [primeira execução](execucao-20261011.md) já produziu 17 documentos reais de dois bancos.

Inter e Bradesco já fornecem documentos ao lote limitado. Banco do Brasil e Caixa continuam em análise; Itaú, Santander e C6 estão suspensos pelas restrições encontradas. Nubank depende de uma definição compatível do escopo institucional e da modalidade da conta. A combinação final de três bancos ainda não está definida.

## Coleta e catálogo em um comando

Após resolver e registrar as condições das fontes em `private/sources.json`:

```bash
python batch.py run private/sources.json data/day-01 --user-agent "RAGBankingStudy/0.3 (email-real@instituicao.edu)"
```

Esse comando encadeia coleta, extração e catálogo. O cadastro precisa conter somente URLs oficiais aprovadas. O programa mantém o intervalo entre acessos; não acelera por meio de acessos massivos. Por padrão, erros interrompem o lote e deixam o registro de falhas. A opção `--allow-partial` conserva documentos utilizáveis e registra pendências, sem congelar uma coleção final.

O catálogo entrega:

- Título, banco, URL, data, tipo de arquivo e hash.
- Contagem de seções e caracteres.
- Cópias idênticas identificadas dentro de cada banco.
- Assuntos candidatos: conta e cartão.
- Passagens literais com valores, prazos e condições, com posição no texto.
- Alertas de texto curto e caracteres problemáticos.
- Origem automática das propostas e ausência de validação humana.

O código não deduz nomes exatos de produtos nem o público por essas regras. Esses campos ficam desconhecidos até preparação ancorada nas fontes. PDFs sem texto e problemas de extração exigem tratamento próprio.

## Preparação assistida e julgamento

Codex prepara propostas com evidência; Yago não precisa preencher fichas documento por documento. Um caso técnico real já foi preparado; a preparação do piloto completo continua pendente. Conservar as instruções, a ferramenta usada, a data e as passagens de suporte.

Perguntas e referências são congeladas antes das saídas. A origem sintética ou assistida das perguntas fica explícita. Criar paráfrases não aumenta o número de famílias independentes. A alegação de falta de evidência exige busca na coleção completa; não pode resultar de uma passagem isolada.

Avaliações por IA ficam identificadas como automáticas e exploratórias. Verificações de números e identificadores auxiliam o diagnóstico, mas não substituem uma avaliação de conteúdo. Validação humana independente, se realizada depois, tem registro e procedimento próprios.

## Validação dos modelos

1. Conferir Python, dependências, hardware e espaço disponível antes de baixar arquivos grandes.
2. Fixar as revisões do [E5](https://huggingface.co/intfloat/multilingual-e5-large-instruct) e [Qwen](https://huggingface.co/Qwen/Qwen3-8B), com licenças e parâmetros.
3. Executar um caso técnico nas seis configurações, identificar a origem dos dados e medir tempo e memória.
4. Verificar limites de entrada, IDs de fontes, repetição e fidelidade de números.
5. Projetar a duração do piloto com base no tempo medido. Se houver impedimento, registrar a execução pendente e a infraestrutura necessária.

PyTorch e Transformers estão instalados. O E5 foi executado com pesos reais. O ambiente tem 8 GiB e nenhuma GPU exposta; o Qwen completo excede essa memória. A alternativa oficial GGUF Q4_K_M concluiu sete gerações técnicas em llama.cpp, separada do piloto completo. Não há contratação de infraestrutura ou uso de API paga previsto sem decisão específica.

Se houver repetição degenerada, o teste mantém a penalidade global em 1,0 e examina a penalidade 1,05 apenas sobre tokens gerados. Conferir valores e identificadores antes e depois. A implementação precisa ser validada na [versão 4.57.1 de Transformers](https://huggingface.co/docs/transformers/v4.57.1/en/internal/generation_utils). Uma perda de fidelidade impede aceitar o ajuste.

## Piloto e passagem à etapa final

A meta do piloto é 60 perguntas em cinco classes e três bancos, com 450 saídas incluindo estabilidade. O lote rápido não impõe marcações humanas nem reavaliação depois de 14 dias. Uma execução menor recebe o nome de teste técnico e registra sua composição.

O relatório identifica cobertura documental, famílias, tempos medidos, falhas, origem das referências e origem das avaliações. A etapa final exclui perguntas e famílias do piloto e depende de registro prévio do método atualizado. Simulação de precisão, registro final, validação humana e testes de compreensão com leitores continuam pendentes.

## O que depende de Yago

- Confirmar escolhas que mudem o escopo ou o método quando houver uma proposta concreta.
- Fornecer o ambiente de execução se os modelos excederem a infraestrutura disponível.
- Revisar e assumir as conclusões e declarações do manuscrito.

Codex executa o trabalho operacional e prepara os registros. Não há tarefa obrigatória de catalogação manual por Yago.
