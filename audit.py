"""Diagnósticos documentais e verificações técnicas; nenhuma adequação automática."""
import argparse
from pathlib import Path
from study import load, records, write_records, covered, recall


def degenerate(tokens):
    # Saídas de até 512 tokens; procura qualquer bloco >=20 repetido três vezes consecutivas.
    for length in range(20, len(tokens)//3+1):
        for start in range(len(tokens)-3*length+1):
            a=tokens[start:start+length]
            if a == tokens[start+length:start+2*length] == tokens[start+2*length:start+3*length]:
                return {'start':start,'length':length,'copies':3}
    return None


def retrieval_metrics(retrieval_path, dossier_path, unit_map_path, output):
    dossiers = {d['question_id']:d for d in records(dossier_path)}
    unit_map = load(unit_map_path)
    metrics=[]
    for row in records(retrieval_path):
        if row['config']=='S':
            metrics.append({'question_id':row['question_id'],'config':'S','recall':None,'coverage':None})
            continue
        d=dossiers[row['question_id']]
        excluded={u for c in row['excluded'] for u in unit_map.get(c['chunk_id'],[])}
        for k in (3,5,10):
            units={u for c in row['ranked'][:k] for u in unit_map.get(c['chunk_id'],[])}
            metrics.append({'question_id':row['question_id'],'config':row['config'],'k':k,
                'recall':recall(units,d['reference_units']), 'coverage':covered(units,d['sufficient_sets']) if d['sufficient_sets'] else None,
                'reference_units_excluded':sorted(excluded.intersection(d['reference_units'])),
                'retrieved_reference_units':sorted(units.intersection(d['reference_units']))})
    write_records(output,metrics)


def verify_processor():
    import importlib.metadata
    import torch
    from transformers import RepetitionPenaltyLogitsProcessor
    if importlib.metadata.version('transformers')!='4.57.1': raise ValueError('Versão inesperada')
    ids=torch.tensor([[1,2,3]])
    scores=torch.ones((1,8))*2
    usual=RepetitionPenaltyLogitsProcessor(1.05)(ids,scores.clone())
    excluded=RepetitionPenaltyLogitsProcessor(1.05,prompt_ignore_length=3)(ids,scores.clone())
    assert usual[0,1]<scores[0,1]
    assert torch.equal(excluded,scores)
    generated=RepetitionPenaltyLogitsProcessor(1.05,prompt_ignore_length=2)(ids,scores.clone())
    assert generated[0,1]==scores[0,1] and generated[0,3]<scores[0,3]
    return {'version':'4.57.1','default_prompt_penalized':True,'prompt_exclusion_verified':True,
            'generated_tokens_still_penalized':True}


def fidelity_report(answers_path,cases_path,runtime_path,output):
    from study import write,digest
    cases=load(cases_path);answers=records(answers_path);runtime=load(runtime_path)
    expected={f'probe-{i+1}-{s}' for i in range(len(cases)) for s in (None,43,44)}
    if len(cases)!=12 or {a['id'] for a in answers}!=expected or len(answers)!=36:
        raise ValueError('Exigir doze controles completos nas três políticas de semente')
    missing=[];bad=[];trunc=[];count=0
    for answer in answers:
        case=cases[int(answer['id'].split('-')[1])-1]
        for item in case['required_items']:
            count+=1
            if not any(x in (answer['answer'] or '') for x in item['equivalents']):
                missing.append({'run_id':answer['id'],'item_id':item['id']})
        engine=answer.get('engine_response') or {}
        if degenerate(engine.get('tokens',[])):bad.append(answer['id'])
        if engine.get('truncated') or engine.get('stop_type')=='limit':trunc.append(answer['id'])
    result={'generations':len(answers),'required_item_checks':count,'missing_items':missing,
        'degenerate_outputs':bad,'truncated_outputs':trunc,'human_validated':False,
        'passed':not(missing or bad or trunc) and all(a['status']=='completed' for a in answers),
        'elapsed_seconds':sum(a['elapsed_seconds'] for a in answers),
        'runtime':{k:v for k,v in runtime.items() if k not in ('server_command',)},
        'cases_sha256':digest(Path(cases_path).read_text()),'answers_sha256':digest(Path(answers_path).read_text())}
    write(output,result);return result


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    s=p.add_subparsers(dest='command',required=True)
    c=s.add_parser('retrieval')
    for name in ('retrieval','dossiers','unit_map','output'):c.add_argument(name)
    c=s.add_parser('processor');c.add_argument('output')
    a=p.parse_args()
    if a.command=='retrieval':retrieval_metrics(a.retrieval,a.dossiers,a.unit_map,a.output)
    else:
        from study import write
        write(a.output,verify_processor())
