"""Demonstração posterior em BF04; não altera configurações nem resultados principais."""
from pathlib import Path
from study import load,records,write,compatible,recall


def demonstrate(root,output,public=False):
    root=Path(root)
    config=root/'configs/execution-20261012' if public else Path('configs/execution-20261012')
    data=config if public else root/'dataset-v2'
    ranking=root/'docs/results-20261012/final/retrieval.jsonl' if public else root/'final-inputs/retrieval.jsonl'
    catalog={c['id']:c for c in records(config/'catalog.jsonl')}
    q=next(q for q in records(data/'final-questions.jsonl') if q['id']=='BF04')
    d=next(d for d in records(data/'final-dossiers.jsonl') if d['question_id']=='BF04')
    rows=records(ranking);rank=next(r for r in rows if r['question_id']=='BF04' and r['config']=='B')['ranked']
    selected=[]
    for candidate in rank:
        c=catalog[candidate['chunk_id']];metadata={k:list(c[k]) for k in ('product','public')}
        if 'aeternum' in metadata['product']:metadata['product'].append('cartao')
        if compatible(metadata,q['query_attributes']):selected.append(candidate['chunk_id'])
    # Os candidatos fora do top 10 vêm depois destes. Âncoras nos primeiros cinco
    # candidatos compatíveis permanecem no top 5 mesmo se sua lista for completada.
    um=load(data/'unit-map.json')
    restored={u for c in selected[:5] for u in um.get(c,[])}
    original=next(r for r in rows if r['question_id']=='BF04' and r['config']=='C')
    old={u for c in original['ranked'][:5] for u in um.get(c['chunk_id'],[])}
    report={'question_id':'BF04','post_hoc':True,'human_validated':False,'parent_relation':{'aeternum':'cartao'},
        'relation_source_url':d['source_urls'][0],'k':5,'baseline_filtered_anchor_recall':recall(old,d['reference_units']),
        'corrected_anchor_recall':recall(restored,d['reference_units']),
        'corrected_known_selected_ids':selected[:5],'reference_units':d['reference_units'],
        'full_context_reconstructed':len(selected)>=5,
        'all_reference_anchors_guaranteed_in_top5':set(d['reference_units']).issubset(restored),
        'new_generation_or_embedding_calls':0,
        'main_results_unchanged':True,'interpretation':'Correção demonstrada no caso já observado, sem validação externa ou estimativa de ganho geral.'}
    write(output,report);return report

if __name__=='__main__':
    import argparse,json
    p=argparse.ArgumentParser();p.add_argument('root');p.add_argument('output');a=p.parse_args()
    print(json.dumps(demonstrate(a.root,a.output),ensure_ascii=False))
