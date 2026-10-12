# Como escrevemos a documentação

[Voltar ao início](../README.md)

Queremos que uma pessoa consiga encontrar, entender e usar as informações do projeto.

Adotamos como referência os artigos 4º e 5º da [Lei nº 15.263, de 14 de novembro de 2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15263.htm). A lei trata da comunicação da administração pública com a população. O projeto usa suas técnicas como orientação editorial.

## Regras de escrita

1. Começar pela informação de que o leitor precisa.
2. Usar frases curtas e ordem direta.
3. Desenvolver uma ideia por parágrafo.
4. Preferir palavras conhecidas.
5. Explicar um termo técnico quando ele aparecer.
6. Apresentar o nome completo antes de usar uma sigla.
7. Usar títulos que indiquem o conteúdo ou a ação.
8. Dividir instruções em passos.
9. Usar listas e tabelas quando ajudam a comparar ou agir.
10. Escrever quem faz cada ação.
11. Preservar valores, condições, exceções e limites da regra.
12. Usar nomes claros nos links e explicar mensagens de erro.

O protocolo conserva sua versão científica revisada. Os guias explicam o método efetivamente aplicado, e o protocolo original permanece como histórico.

## Exemplo de revisão

| Texto técnico | Texto para quem está começando |
|---|---|
| Verificar a aplicabilidade dos atributos não filtrados. | Confira se a regra vale para o prazo, o canal e as condições da pergunta. |
| Congelar os artefatos e conservar hashes. | Fixe a versão dos arquivos e guarde seus códigos de conferência. |
| Julgamento cego à configuração. | A pessoa avalia a resposta sem saber qual sistema a produziu. |

## Como testar com leitores

Testar a compreensão com pessoas do público-alvo é uma melhoria editorial futura. Esse teste está pendente e não condiciona a execução individual do experimento. A revisão de clareza pelo próprio pesquisador continua prevista, com seus limites registrados.

Convide leitores sem experiência em RAG. Peça que usem a documentação para fazer estas tarefas:

- Explicar, com suas palavras, o objetivo do projeto.
- Encontrar o comando da demonstração.
- Dizer o que já foi executado e o que continua pendente.
- Identificar quem avalia as respostas.
- Encontrar uma explicação para um termo técnico.
- Dizer o que fazer quando o arquivo de saída já existe.

Registre se cada pessoa concluiu a tarefa, onde teve dúvida e quais palavras atrapalharam. Revise o texto e repita as tarefas que tiveram problemas.

Testes automáticos de links e exemplos ajudam a manter os guias. A avaliação com leitores verifica se as explicações funcionam para o público.

## Antes de publicar uma alteração

- A primeira frase informa o que o leitor precisa saber?
- O texto diz quem faz a ação?
- As siglas e os termos foram explicados?
- As condições e os números foram preservados?
- O leitor consegue encontrar o próximo passo?
- Os links levam ao material indicado?
- O texto distingue exemplo fictício, teste técnico e resultado da pesquisa?
