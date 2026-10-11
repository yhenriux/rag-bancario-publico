"""Relatório de recuperação e diagnósticos das respostas sem juiz semântico."""
import argparse
import json
import re
from collections import Counter,defaultdict
from pathlib import Path
from statistics import mean,median
from study import records,load,write,write_records,paired_bootstrap,digest
from audit import degenerate


def diagnostics(item,answer):
    evidence={e['id'] for e in item['evidence']}
    citations=re.findall(r'\[([A-Za-z0-9_-]+)\]',answer['answer'] or '')
    engine=answer.get('engine_response') or {}
    # Estes diagnósticos apontam sinais técnicos; não determinam adequação semântica.
    return {'run_id':item['id'],'question_id':item['question_id'],'config':item['config'],
       'seed':item['seed'],'status':answer['status'],'citation_count':len(citations),
       'invalid_citations':sorted(set(citations)-evidence),
       'valid_citations':sorted(set(citations)&evidence),
       'evidence_present':bool(evidence),'missing_citation_with_evidence':bool(evidence) and not citations,
       'truncated':engine.get('truncated',False),'stop_type':engine.get('stop_type'),
       'output_tokens':engine.get('tokens_predicted'),'degenerate':degenerate(engine.get('tokens',[])),
       'elapsed_seconds':answer['elapsed_seconds'],'answer_sha256':digest(answer['answer'] or ''),
       'human_validated':False}


def run(root,phase,output):
    from audit import retrieval_metrics
    root=Path(root);out=Path(output);out.mkdir(parents=True,exist_ok=False)
    prompts=records(root/(phase+'-inputs')/'prompts.jsonl')
    answers=records(root/phase/'answers.jsonl');by={a['id']:a for a in answers}
    if len(by)!=len(prompts) or {p['id'] for p in prompts}!=set(by):raise ValueError('Execução incompleta ou duplicada')
    ds=root/'dataset-v2'/(phase+'-dossiers.jsonl');qs=records(root/'dataset-v2'/(phase+'-questions.jsonl'))
    qmap={q['id']:q for q in qs}
    retrieval_metrics(root/(phase+'-inputs')/'retrieval.jsonl',ds,root/'dataset-v2/unit-map.json',out/'retrieval-metrics.jsonl')
    metrics=records(out/'retrieval-metrics.jsonl')
    unit_map=load(root/'dataset-v2/unit-map.json')
    dmap={d['question_id']:d for d in records(ds)}
    chunks=records(root/'chunks.jsonl')
    effective=[]
    for row in records(root/(phase+'-inputs')/'retrieval.jsonl'):
        if row['config']=='S':continue
        q=qmap[row['question_id']];d=dmap[q['id']]
        refs=set(d['reference_units']);excluded={c['chunk_id'] for c in row['excluded']}
        bank_chunks={c['id'] for c in chunks if c['bank']==q['bank']}
        available={u for c in bank_chunks-excluded for u in unit_map.get(c,[])}
        selected={u for c in row['prompt_evidence_ids'] for u in unit_map.get(c,[])}
        effective.append({'question_id':q['id'],'config':row['config'],
            'reference_anchors_unavailable_after_filter':sorted(refs-available),
            'prompt_anchor_recall':len(refs&selected)/len(refs) if refs else None,
            'budget_removed_ids':row['budget_removed_ids'],
            'prompt_evidence_ids':row['prompt_evidence_ids']})
    write_records(out/'effective-context.jsonl',effective)
    diag=[diagnostics(p,by[p['id']]) for p in prompts];write_records(out/'diagnostics.jsonl',diag)
    means=[]
    for mode in ('A','B','C','Bp','L'):
        for k in (3,5,10):
            rows=[r for r in metrics if r['config']==mode and r.get('k')==k and r.get('recall') is not None]
            means.append({'config':mode,'k':k,'eligible_questions':len(rows),
               'mean_anchor_recall':mean(r['recall'] for r in rows) if rows else None,
               'all_anchors_covered':mean(r['coverage'] for r in rows) if rows else None})
    lookup={(r['question_id'],r['config'],r.get('k')):r for r in metrics}; contrasts=[]
    for label,left,right,classes in [('B-A','B','A',{'condicao','excecao'}),('B-Bp','B','Bp',{'condicao','excecao'}),('C-B','C','B',set(q['class'] for q in qs))]:
        for metric in ('recall','coverage'):
            pairs=[]
            for q in qs:
                if q['class'] not in classes or (label=='C-B' and not q['query_attributes']):continue
                a=lookup[(q['id'],left,5)].get(metric);b=lookup[(q['id'],right,5)].get(metric)
                if a is not None and b is not None:pairs.append((q['bank'],q['family'],float(a)-float(b)))
            contrasts.append({'contrast':label,'metric':metric,'k':5,
                      'result':paired_bootstrap(pairs) if pairs else None})
    summary=[]
    for mode in ('A','B','C','Bp','L','S'):
        d=[r for r in diag if r['config']==mode and r['seed'] is None]
        summary.append({'config':mode,'main_generations':len(d),'failed':sum(r['status']=='failed' for r in d),
           'truncated':sum(r['truncated'] for r in d),'degenerate':sum(bool(r['degenerate']) for r in d),
           'answers_with_invalid_citations':sum(bool(r['invalid_citations']) for r in d),
           'answers_without_citation_when_evidence_present':sum(r['missing_citation_with_evidence'] for r in d)})
    stable=[]
    pmap={p['id']:p for p in prompts}
    for q in qs:
        for mode in ('A','B','C'):
            group=[r for r in diag if r['question_id']==q['id'] and r['config']==mode]
            if len(group)>1:
                main=next(r for r in group if r['seed'] is None)
                for s in group:
                    if s['seed'] is not None:stable.append({'question_id':q['id'],'config':mode,'seed':s['seed'],
                       'identical_text':s['answer_sha256']==main['answer_sha256'],
                       'same_valid_citations':s['valid_citations']==main['valid_citations'],
                       'same_technical_flags':(s['truncated'],bool(s['degenerate']),bool(s['invalid_citations']))==(main['truncated'],bool(main['degenerate']),bool(main['invalid_citations']))})
    filtered=[r for r in effective if r['config']=='C' and r['reference_anchors_unavailable_after_filter']]
    report={'phase':phase,'completed':True,'questions':len(qs),'families':len({q['family'] for q in qs}),
       'banks':dict(Counter(q['bank'] for q in qs)),'classes':dict(Counter(q['class'] for q in qs)),
       'generations':len(prompts),'main_generations':sum(p['seed'] is None for p in prompts),
       'stability_generations':sum(p['seed'] is not None for p in prompts),
       'elapsed_generation_seconds':sum(a['elapsed_seconds'] for a in answers),
       'median_seconds_per_generation':median(a['elapsed_seconds'] for a in answers),
       'retrieval_summary':means,'paired_exploratory_contrasts':contrasts,
       'technical_summary':summary,'filter_excluded_reference_questions':[r['question_id'] for r in filtered],
       'evidence_budget':{'pairs_with_removed_evidence':sum(bool(r['budget_removed_ids']) for r in effective)},
       'automatic_adequacy_enabled':False,'human_validated':False,
       'limitations':['Amostra de conveniência pequena','Referências e metadados assistidos, sem validação humana independente',
          'Âncoras curtas medem recuperação documental, não todas as proposições','Sem avaliação semântica validada das respostas',
          'Intervalos exploratórios condicionados às famílias e referências preparadas; não corrigem seleção de fontes'],
       'input_sha256':{'prompts':digest((root/(phase+'-inputs')/'prompts.jsonl').read_text()),
                     'answers':digest((root/phase/'answers.jsonl').read_text())}}
    write(out/'summary.json',report);write_records(out/'stability.jsonl',stable)
    return report

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('root');p.add_argument('phase');p.add_argument('output');a=p.parse_args()
 r=run(a.root,a.phase,a.output);print(json.dumps({'completed':r['completed'],'generations':r['generations'],'questions':r['questions']}))
