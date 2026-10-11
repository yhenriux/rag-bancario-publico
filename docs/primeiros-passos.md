# Veja a demonstração no seu computador

[Voltar ao início](../README.md)

A demonstração funciona sem acessar bancos e sem baixar modelos de inteligência artificial. Ela usa quatro regras fictícias para mostrar como um filtro pode ajudar ou prejudicar a busca.

## 1. Baixe os arquivos

No [repositório do GitHub](https://github.com/yhenriux/rag-bancario-publico), clique em **Code** e depois em **Download ZIP**.

Extraia o arquivo. Abra a pasta que contém `README.md` e `demo.py`.

Se você já usa Git, pode baixar com:

```bash
git clone https://github.com/yhenriux/rag-bancario-publico.git
cd rag-bancario-publico
```

## 2. Confira o Python

Python é o programa que executa os scripts deste projeto. Use a versão 3.11 ou superior.

Abra um terminal nessa pasta e digite:

```bash
python --version
```

No Windows, você também pode usar `py --version`. No macOS ou Linux, tente `python3 --version`.

Se o comando não existir, instale o Python pelo [site oficial](https://www.python.org/downloads/). No Windows, marque a opção que permite usar Python no terminal.

## 3. Execute a demonstração

```bash
python demo.py
```

Se seu computador usa `py` ou `python3`, use esse nome no lugar de `python` em todos os comandos.

Você verá dois casos:

1. O filtro mantém a regra do cartão Alfa e retira a regra do cartão Beta.
2. Uma descrição incorreta faz o filtro retirar uma regra geral necessária.

A demonstração mostra as fontes e explica o que observar. Ela não produz respostas com E5 ou Qwen.

## 4. Salve o exemplo, se quiser

```bash
python demo.py --output runs/demonstracao.json
```

O programa cria um arquivo de resultados da demonstração. Ele conserva o arquivo existente: para repetir e salvar, escolha outro nome.

## 5. Confira os testes

```bash
python -m unittest discover -s tests -v
```

Se tudo estiver certo, o terminal mostra `OK`. Os testes verificam partes do código com exemplos fictícios.

Os testes também rodam no GitHub. Abra a aba **Actions** para ver o resultado após cada alteração.

## O que fazer depois?

Para entender os papéis da equipe, leia [Entenda o projeto](entenda-o-projeto.md).

Para preparar uma pesquisa com documentos reais, siga o [guia de execução](execucao.md). Essa etapa exige revisão das fontes, instalação dos modelos e participação de avaliadores.

## Problemas comuns

| Mensagem ou situação | O que fazer |
|---|---|
| Python não foi encontrado | Confira a instalação e tente `py` ou `python3`. |
| O arquivo `demo.py` não foi encontrado | Abra o terminal na pasta que contém esse arquivo. |
| O arquivo de saída já existe | Escolha um novo nome em `--output`. |
| Aparece um erro durante o teste | Copie o erro, informe o comando usado e [abra um relato](https://github.com/yhenriux/rag-bancario-publico/issues). |

Antes de publicar um erro, confira se o texto contém dados pessoais ou informações de acesso.
