"""Mostra como uma busca pode ganhar ou perder informação ao aplicar um filtro."""
import argparse
from study import bm25, compatible, covered, write


def cases():
    return [
        {'id':'filtro-ajuda',
         'question':'Tenho o cartão Alfa. Qual regra de anuidade devo consultar?',
         'query_attributes':{'product':['alfa'],'public':['pf']},
         'chunks':[{'id':'E1','text':'O cartão Alfa para pessoa física cobra R$ 120 de anuidade. A isenção exige fatura mensal de pelo menos R$ 1.000.'},
                   {'id':'E2','text':'O cartão Beta para pessoa física tem anuidade gratuita.'}],
         'metadata':{'E1':{'product':['alfa'],'public':['pf']},'E2':{'product':['beta'],'public':['pf']}},
         'sufficient_sets':[['E1']],
         'lesson':'O filtro retira a regra de outro cartão. A resposta ainda precisa explicar o gasto mínimo para ter isenção.'},
        {'id':'filtro-prejudica',
         'question':'Após cancelar o cartão Alfa, continuam novos lançamentos de anuidade?',
         'query_attributes':{'product':['alfa']},
         'chunks':[{'id':'E3','text':'O cartão Alfa cobra anuidade.'},
                   {'id':'E4','text':'O documento Cartão Beta contém uma nota geral: o cancelamento interrompe novos lançamentos de anuidade em todos os cartões, incluindo Alfa.'}],
         'metadata':{'E3':{'product':['alfa'],'public':['pf']},'E4':{'product':['beta'],'public':['pf']}},
         'sufficient_sets':[['E3','E4']],
         'lesson':'A descrição de E4 erra ao registrar somente Beta. O filtro perde uma regra que também vale para Alfa. Corrigir o alcance para geral conserva essa fonte.'},
    ]


def demonstrate():
    result=[]
    for case in cases():
        ranked=[chunk for _,chunk in bm25(case['question'],case['chunks'])]
        kept=[c for c in ranked if compatible(case['metadata'][c['id']],case['query_attributes'])]
        result.append({'id':case['id'],'question':case['question'],'sources':ranked,
            'kept':[c['id'] for c in kept],'removed':[c['id'] for c in ranked if c not in kept],
            'coverage_before':covered([c['id'] for c in ranked],case['sufficient_sets']),
            'coverage_after':covered([c['id'] for c in kept],case['sufficient_sets']),'lesson':case['lesson']})
    return {'status':'exemplo fictício para aprendizagem',
            'method':'Busca por palavras com BM25 e filtro didático. Não executa E5, Qwen ou julgamentos humanos.','cases':result}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',help='Salvar a demonstração em um novo arquivo JSON')
    a=p.parse_args();report=demonstrate()
    print('RAG Bancário Público: demonstração com regras fictícias.\n')
    print('O programa mostra as fontes. As respostas de IA pertencem à etapa de modelos.\n')
    for case in report['cases']:
        print(case['question'])
        for source in case['sources']:print(f'  [{source["id"]}] {source["text"]}')
        print('  Fontes mantidas:',', '.join(case['kept']))
        print('  Fontes retiradas:',', '.join(case['removed']) or 'nenhuma')
        print('  Há todas as fontes necessárias após o filtro?','Sim' if case['coverage_after'] else 'Não')
        print('  O que observar:',case['lesson'],'\n')
    if a.output:write(a.output,report);print('Demonstração salva em:',a.output)


if __name__=='__main__':main()
