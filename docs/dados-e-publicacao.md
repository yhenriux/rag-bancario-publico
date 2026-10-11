# Como guardar e publicar os dados

[Voltar ao início](../README.md)

Cada arquivo precisa ter uma origem e uma versão identificadas. A publicação também depende dos direitos de uso da fonte e da etapa da avaliação.

## O que fica em cada lugar?

| Pasta | Conteúdo | Como usar |
|---|---|---|
| `configs/` | Exemplos de configuração do estudo | Os exemplos podem ficar no GitHub. |
| `examples/` | Perguntas, fontes e formulários fictícios | Servem para aprender e testar o código. |
| `docs/` | Explicações e protocolo | Servem para entender e executar o estudo. |
| `data/` | Cópias das fontes, textos e índices reais | Ficam fora do Git por padrão. |
| `private/` | Anotações, referências, decisões e chaves | A coordenação define quem pode acessar. |
| `runs/` | Resultados e registros das execuções | Ficam fora do Git por padrão. |

O arquivo `.gitignore` evita a inclusão automática dessas pastas no Git. Ele não controla o acesso das pessoas no computador ou no armazenamento da equipe.

## O que o registro de uma fonte contém?

- Banco e tipo de documento.
- Endereço usado na coleta e endereço final.
- Data e horário da coleta.
- Código SHA-256 do conteúdo original.
- Local do arquivo guardado.
- Termos de uso, data de revisão e responsável.
- Decisão sobre coleta e redistribuição.

Conserve o arquivo original. Gere o texto revisado em outro arquivo. Registre o que foi corrigido e por quê.

## O que publicar primeiro?

Código, guias, exemplos fictícios e regras do estudo. Quando a equipe revisar as fontes, poderá publicar o cadastro de endereços e os códigos de conferência permitidos.

Documentos coletados e respostas de avaliação precisam de revisão específica antes da publicação. Uma página disponível para leitura pode ter limites para redistribuição.

A chave que mostra qual configuração produziu cada resposta fica restrita enquanto houver avaliação cega.

## Como fixar uma versão?

Registre a versão do código, as versões dos modelos e os códigos dos arquivos. Deposite o plano em um serviço público datado, como OSF ou Zenodo, antes da etapa final.

O identificador público só entra na documentação depois de existir. O projeto ainda não tem DOI nem estudo final executado.

## Como citar?

Enquanto não houver uma versão com identificador persistente, informe o nome do projeto, o endereço do repositório e o commit usado.

O arquivo `CITATION.cff` contém a identificação básica. Atualize a versão e o identificador quando a publicação ocorrer.

## Quais direitos valem?

Os documentos dos bancos conservam seus direitos e termos de uso. A licença do código ainda precisa ser definida pelo responsável. A publicação do protocolo acompanha a aprovação autoral e o registro da versão.

[Veja o cadastro dos campos](dados.md).
