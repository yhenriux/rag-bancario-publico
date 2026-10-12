# Tabelas e quadros editáveis

Este arquivo reúne as sete tabelas e quadros do artigo e dos suplementos. Os números preservam os resultados publicados.

Quadro 1 Configurações de busca documental

| Código | Recuperação | Decisão documental |
|---|---|---|
| A | Busca semântica no trecho original | Sem cabeçalho contextual adicional |
| B | Busca semântica com cabeçalho contextual completo | Título, seção, tipo, produto e público |
| C | Busca de B com filtro | Produto e público preparados para a pergunta |
| Bp | Busca semântica com cabeçalho contextual reduzido | Produto e público |
| L | Busca lexical BM25 | Correspondência de termos |

Fonte: elaboração própria, 2026.

Tabela 1 Posição e recuperação de âncoras por conjunto

| Conjunto / configuração | Recall@1 | Recall@3 | Recall@5 | Recall@10 | MRR@10 |
|---|---:|---:|---:|---:|---:|
| Piloto / A | 71,9% | 90,6% | 90,6% | 90,6% | 0,844 |
| Piloto / B | 65,6% | 90,6% | 90,6% | 100,0% | 0,812 |
| Piloto / C | 71,9% | 90,6% | 96,9% | 100,0% | 0,849 |
| Piloto / Bp | 65,6% | 90,6% | 96,9% | 96,9% | 0,825 |
| Piloto / L | 62,5% | 93,8% | 93,8% | 100,0% | 0,820 |
| Segundo / A | 75,0% | 87,5% | 87,5% | 100,0% | 0,830 |
| Segundo / B | 62,5% | 100,0% | 100,0% | 100,0% | 0,792 |
| Segundo / C | 50,0% | 87,5% | 87,5% | 87,5% | 0,667 |
| Segundo / Bp | 75,0% | 87,5% | 100,0% | 100,0% | 0,844 |
| Segundo / L | 87,5% | 100,0% | 100,0% | 100,0% | 0,917 |

Fonte: rankings e referências assistidas publicados. Denominadores: dezesseis perguntas no piloto e oito no segundo conjunto. MRR@10 é a média do inverso da posição da primeira âncora no limite de dez trechos.

Tabela 1a Recuperação e acesso inicial por banco

| Banco / conjunto / configuração | N | Recall@1 | Recall@3 | Recall@5 | MRR@10 |
|---|---:|---:|---:|---:|---:|
| Inter / piloto / A | 8 | 87,5% | 100,0% | 100,0% | 0,938 |
| Inter / piloto / B | 8 | 87,5% | 100,0% | 100,0% | 0,938 |
| Inter / piloto / C | 8 | 100,0% | 100,0% | 100,0% | 1,000 |
| Inter / piloto / Bp | 8 | 87,5% | 100,0% | 100,0% | 0,938 |
| Inter / piloto / L | 8 | 75,0% | 100,0% | 100,0% | 0,875 |
| Inter / segundo / A | 4 | 100,0% | 100,0% | 100,0% | 1,000 |
| Inter / segundo / B | 4 | 75,0% | 100,0% | 100,0% | 0,875 |
| Inter / segundo / C | 4 | 75,0% | 100,0% | 100,0% | 0,875 |
| Inter / segundo / Bp | 4 | 100,0% | 100,0% | 100,0% | 1,000 |
| Inter / segundo / L | 4 | 100,0% | 100,0% | 100,0% | 1,000 |
| Bradesco / piloto / A | 8 | 56,2% | 81,2% | 81,2% | 0,750 |
| Bradesco / piloto / B | 8 | 43,8% | 81,2% | 81,2% | 0,688 |
| Bradesco / piloto / C | 8 | 43,8% | 81,2% | 93,8% | 0,698 |
| Bradesco / piloto / Bp | 8 | 43,8% | 81,2% | 93,8% | 0,713 |
| Bradesco / piloto / L | 8 | 50,0% | 87,5% | 87,5% | 0,766 |
| Bradesco / segundo / A | 4 | 50,0% | 75,0% | 75,0% | 0,661 |
| Bradesco / segundo / B | 4 | 50,0% | 100,0% | 100,0% | 0,708 |
| Bradesco / segundo / C | 4 | 25,0% | 75,0% | 75,0% | 0,458 |
| Bradesco / segundo / Bp | 4 | 50,0% | 75,0% | 100,0% | 0,688 |
| Bradesco / segundo / L | 4 | 75,0% | 100,0% | 100,0% | 0,833 |

Fonte: cálculos posteriores sobre rankings congelados. N é o número de perguntas elegíveis no estrato. Recall@10 e cobertura por banco constam do relatório público.

Tabela 2 Perguntas discordantes nas primeiras cinco posições

| Conjunto / contraste | Elegíveis | Primeiro supera | Segundo supera | Empates |
|---|---:|---|---|---:|
| Piloto / B × A | 8 | 0 | 1 (B05) | 7 |
| Piloto / B × Bp | 8 | 0 | 1 (B05) | 7 |
| Piloto / C × B | 16 | 1 (B05) | 0 | 15 |
| Segundo / B × A | 4 | 0 | 0 | 4 |
| Segundo / B × Bp | 4 | 0 | 0 | 4 |
| Segundo / C × B | 8 | 0 | 1 (BF04) | 7 |

Fonte: análise posterior dos rankings congelados. As contagens são iguais para recall@5 e cobertura@5. Primeiro e segundo designam a ordem das configurações no contraste.

Quadro 2 Diagnósticos e intervenções documentais

| Ocorrência | Registro utilizado | Intervenção |
|---|---|---|
| Produto específico perde relação com categoria geral | BF04 e trilha de exclusão | Registrar hierarquia e testar seleção ampliada |
| Redução de candidatos favorece referência | B05 e ranking por configuração | Examinar o uso do filtro por classe de pergunta |
| Referência não aparece nas primeiras posições | Âncoras e dez posições publicadas | Rever descrição, segmentação e competição entre trechos |
| Orçamento retira evidências | Lista efetivamente enviada | Reunir regra e condição ou ajustar prioridade |
| Avaliador erra controles conhecidos | Duas calibrações publicadas | Manter adequação fora das medidas principais |

Fonte: elaboração própria, 2026. A linha sobre orçamento descreve um mecanismo de controle; os registros de contexto efetivo informam se ele ocorreu nesta execução.

Tabela A1 Posição inicial, recall e cobertura por pergunta

| ID | Banco | Classe | N | A | B | C | Bp | L |
|---|---|---|---:|---|---|---|---|---|
| I01 | Inter | direta | 1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I02 | Inter | direta | 1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 2/1/1 |
| I03 | Inter | condição | 3 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I04 | Inter | condição | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I05 | Inter | exceção | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I06 | Inter | exceção | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I07 | Inter | ambiguidade | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| I08 | Inter | ambiguidade | 3 | 2/1/1 | 2/1/1 | 1/1/1 | 2/1/1 | 2/1/1 |
| I09 | Inter | insuficiência | 0 | NA | NA | NA | NA | NA |
| I10 | Inter | insuficiência | 0 | NA | NA | NA | NA | NA |
| B01 | Bradesco | direta | 1 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 |
| B02 | Bradesco | direta | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 8/0/0 |
| B03 | Bradesco | condição | 1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 2/1/1 |
| B04 | Bradesco | condição | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| B05 | Bradesco | exceção | 1 | 1/1/1 | 6/0/0 | 4/1/1 | 2/1/1 | 1/1/1 |
| B06 | Bradesco | exceção | 1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| B07 | Bradesco | ambiguidade | 2 | NR/0/0 | 3/1/1 | 3/1/1 | 5/1/1 | 1/1/1 |
| B08 | Bradesco | ambiguidade | 2 | 2/0,5/0 | 2/0,5/0 | 2/0,5/0 | 2/0,5/0 | 1/1/1 |
| B09 | Bradesco | insuficiência | 0 | NA | NA | NA | NA | NA |
| B10 | Bradesco | insuficiência | 0 | NA | NA | NA | NA | NA |
| IF01 | Inter | direta | 4 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| IF02 | Inter | condição | 3 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| IF03 | Inter | exceção | 3 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| IF04 | Inter | ambiguidade | 1 | 1/1/1 | 2/1/1 | 2/1/1 | 1/1/1 | 1/1/1 |
| IF05 | Inter | insuficiência | 0 | NA | NA | NA | NA | NA |
| BF01 | Bradesco | direta | 1 | 7/0/0 | 3/1/1 | 3/1/1 | 4/1/1 | 3/1/1 |
| BF02 | Bradesco | condição | 1 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 | 1/1/1 |
| BF03 | Bradesco | exceção | 2 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 | 1/1/1 |
| BF04 | Bradesco | ambiguidade | 2 | 1/1/1 | 1/1/1 | NR/0/0 | 1/1/1 | 1/1/1 |
| BF05 | Bradesco | insuficiência | 0 | NA | NA | NA | NA | NA |

Fonte: análise posterior dos rankings congelados. As perguntas IF e BF pertencem ao segundo conjunto. Valores não arredondados nas células; referências assistidas.

Tabela B1 Recuperação e cobertura de âncoras nas primeiras cinco posições

| Configuração | Recall piloto (16) | Cobertura piloto (16) | Recall segundo (8) | Cobertura segundo (8) |
|---|---:|---:|---:|---:|
| A | 90,625% | 87,500% | 87,500% | 87,500% |
| B | 90,625% | 87,500% | 100,000% | 100,000% |
| C | 96,875% | 93,750% | 87,500% | 87,500% |
| Bp | 96,875% | 93,750% | 100,000% | 100,000% |
| L | 93,750% | 93,750% | 100,000% | 100,000% |

Fonte: cálculos sobre os rankings e as referências assistidas publicados no projeto. Os números entre parênteses indicam perguntas elegíveis.