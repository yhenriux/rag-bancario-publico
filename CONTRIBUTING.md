# Como contribuir

[Início](README.md) · [Método](docs/metodo.md)

Você pode propor uma melhoria de linguagem, apontar uma referência incompleta ou relatar um erro de reprodução. Informe arquivo, trecho ou comando e o resultado esperado.

## Antes de alterar

1. Leia o método e confira se o arquivo é atual ou histórico.
2. Preserve o protocolo original e os rankings da execução publicada.
3. Registre origem e justificativa de mudanças nas referências.
4. Use outra versão para novas fontes, perguntas ou modelos.
5. Execute os testes e a reprodução quando alterar cálculos.

```bash
python -m pip install 'beautifulsoup4>=4.12,<5' 'pypdf>=5,<7'
python -m unittest discover -s tests -v
python replay_results.py
```

Uma correção posterior pode explicar um achado, mas deve ficar separada dos resultados originais. Não apresente conteúdo assistido como anotação humana independente.

## Fontes e informações privadas

Não publique textos integrais dos bancos, prompts com esses textos, credenciais ou dados pessoais. As condições de redistribuição das fontes não estão aprovadas. A escolha da licença dos materiais autorais ainda cabe ao pesquisador.
