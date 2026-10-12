# Repita os cálculos publicados

[Início](../README.md) · [Dados](dados.md) · [Guia técnico](execucao.md)

A reprodução da análise funciona com Python 3.11 ou superior e os arquivos públicos. Não exige modelos, textos bancários ou pacotes adicionais.

## 1. Obtenha os arquivos

Use **Code → Download ZIP** no GitHub e extraia o arquivo. Ou execute:

```bash
git clone https://github.com/yhenriux/rag-bancario-publico.git
cd rag-bancario-publico
```

Abra o terminal na pasta que contém `replay_results.py`.

## 2. Recalcule as medidas e os intervalos

```bash
python replay_results.py
```

Resultado esperado: dois registros, `pilot` e `final`, ambos com `metrics_match: true`, `bootstrap_match: true` e `intervention_match: true`. O programa compara as novas contas com os relatórios publicados e interrompe se houver divergência.

Ele usa os rankings em `docs/results-20261012/` e as referências em `configs/execution-20261012/`. Recalcula recall, cobertura, diferenças pareadas e 5.000 reamostragens. Também reproduz a intervenção posterior no caso BF04.

## 3. Confira os códigos dos arquivos

```bash
python -c "import json,hashlib,pathlib; m=json.load(open('SHA256SUMS.json')); assert all(hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()==h for p,h in m.items()); print('Integridade conferida')"
```

O manifesto cobre arquivos registrados do projeto. Ele confere os bytes; o conteúdo e as escolhas científicas continuam sujeitos a revisão.

## 4. Execute os testes do código

```bash
python -m pip install 'beautifulsoup4>=4.12,<5' 'pypdf>=5,<7'
python -m unittest discover -s tests -v
python demo.py
```

## O que cada reprodução comprova

| Reprodução | O que você consegue verificar |
|---|---|
| Contas públicas | Medidas calculadas sobre rankings e referências publicados |
| Originais privados | Extração, posições e conteúdo da coleção usada |
| Nova coleta | Outra versão dos sites, com novos hashes e possíveis diferenças |
| Nova busca por modelos | Exige fontes, dependências e revisões fixadas; pode depender do equipamento |
| Geração | Módulo parcial; retomada exige entradas e checkpoints correspondentes |

Uma nova coleta não recupera necessariamente os mesmos bytes. Os textos completos ficam privados porque sua redistribuição não está aprovada.
