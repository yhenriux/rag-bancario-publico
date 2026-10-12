# Fontes e condições de coleta

[Início](../README.md) · [Registro das decisões](source-decisions-20261011.json) · [Auditoria atual](results-20261012/source-audit.json)

A entrega usa documentação pública de Inter e Bradesco. A conferência operacional foi assistida por Codex e registrada por endereço. Ela não equivale a autorização expressa dos bancos nem a licença de redistribuição.

| Candidato | Decisão desta execução | Motivo registrado |
|---|---|---|
| Inter | Incluído | Fontes públicas cadastradas, regras de acesso e políticas examinadas |
| Bradesco | Incluído | Fontes públicas utilizáveis, separadas de serviços autenticados |
| Banco do Brasil | Excluído neste ciclo | Conferência comparável de termos e extração não concluída em duas rodadas |
| Caixa | Excluída neste ciclo | Redirecionamentos circulares nas rotas examinadas em duas rodadas |
| Itaú | Coleta suspensa | Termos examinados restringem acesso automatizado massificado sem autorização |
| Santander | Fora da seleção aplicada | Não integrou a coleção concluída |

A exclusão de Banco do Brasil e Caixa é uma decisão de escopo; os registros não afirmam proibição geral de coleta. Os [candidatos iniciais](../configs/candidates.json) e a [pré-conferência](access-preflight.json) ficam preservados.

## O que foi guardado

Cada fonte tem URL, data, arquivo original, hash, regra de acesso consultada e decisão operacional. As 27 fontes usadas têm registro de origem e hash de robots.txt. Quatro arquivos mudaram na recuperação de 12/10; [confira a lista](retomada-fontes-20261012.json).

## Limites da coleta

O coletor verifica domínio, redirecionamentos, robots.txt e intervalo entre acessos. As regras permitem um lote limitado de páginas públicas cadastradas. Não usamos login, informações de clientes, documentos internos ou caminhos bloqueados.

O material integral fica em pacote privado. O GitHub recebe catálogo derivado, posições, hashes e resultados. Uma nova coleta precisa de nova conferência dos termos e regras na data da execução.

## Relação institucional

Yago trabalha no Inter. A pesquisa usa apenas fontes públicas e não representa posicionamento ou aprovação da instituição.
