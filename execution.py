"""Preparação assistida, recuperação e controle prospectivo da execução GGUF."""
import argparse
import json
import re
from pathlib import Path
from study import (CONFIGS, load, records, write, write_records, prefix, compatible,
                   bm25, digest, validate_questions, stability_sample)
from experiment import tokenizer, encode, file_sha, metadata_valid


def metadata(chunks_path, output):
    rows={}
    for c in records(chunks_path):
        text=c['text']; title=c['title'].lower()
        products=[]
        for word,label in [('conta','conta'),('cartão','cartao'),('pix','pix'),
                           ('saque de limite','saque_limite'),('crédito flex','credito_flex'),
                           ('aeternum','aeternum'),('cdb mais limite','mais_limite'),
                           ('poupança mais','mais_limite'),('loop','loop')]:
            if word in title: products.append(label)
        if not products: products=['desconhecido']
        public=[]; anchors=[]
        patterns=[(r'\bPF\b|pessoa física|pessoas físicas','pf'),
                  (r'\bMEI\b','mei'),(r'\bPJ\b|pessoa jurídica','pj'),
                  (r'\bOne\b','one'),(r'\bPrime\b','prime'),(r'\bWin\b','win')]
        for pattern,label in patterns:
            m=re.search(pattern,text,re.I)
            if m: public.append(label);anchors.append({'field':'public','value':label,
                               'char_start':c['char_start']+m.start(),'char_end':c['char_start']+m.end()})
        if not public:public=['desconhecido']
        rows[c['id']]={'product':products,'public':public,'document_type':'pagina_publica',
           'evidence':{'document_id':c['document_id'],'location':c['location'],
                       'title_product_rules':True,'public_anchors':anchors},
           'adjudication_id':'automatic-rules-20261011-'+c['id'],
           'origin':'deterministic_v2_assisted','human_validated':False,
           'conditions':[m.group() for m in re.finditer(r'[^\n]*(?:desde que|somente|apenas|se |mediante)[^\n]*',text,re.I)],
           'exceptions':[m.group() for m in re.finditer(r'[^\n]*(?:exceto|salvo|não podem|não é possível)[^\n]*',text,re.I)]}
    metadata_valid(records(chunks_path),rows)
    write(output,rows)


def prepare(config_path,chunks_path,metadata_path,questions_path,dossiers_path,indices,output,phase):
    import torch
    from transformers import AutoModel
    torch.set_num_threads(8)
    config=load(config_path); chunks=records(chunks_path);meta=load(metadata_path)
    qs=records(questions_path); dossiers={d['question_id']:d for d in records(dossiers_path)}
    validate_questions(qs,config.get('pilot_families',[]) if phase=='final' else ())
    metadata_valid(chunks,meta)
    idx=load(Path(indices)/'inputs.json')
    if idx['config']!=config or idx['chunks_sha256']!=file_sha(chunks_path) or idx['metadata_sha256']!=file_sha(metadata_path):
        raise ValueError('Índices divergentes')
    out=Path(output);out.mkdir(parents=True,exist_ok=False)
    tok=tokenizer(config,'e5'); model=AutoModel.from_pretrained(config['e5_model'],revision=config['e5_revision']).to('cpu')
    queries=encode(['Instruct: '+config['query_instruction']+'\nQuery: '+q['question'] for q in qs],tok,model,'cpu')
    del model
    vectors={k:torch.load(Path(indices)/(k+'.pt'),weights_only=True) for k in ('A','B','Bp')}
    qtok=tokenizer(config,'qwen'); prompts=[]; retrieval=[]
    stable=set(stability_sample(qs)) if phase=='pilot' else set()
    for qi,q in enumerate(qs):
        candidates=[i for i,c in enumerate(chunks) if c['bank']==q['bank']]
        for mode in CONFIGS:
            excluded=[]
            if mode=='S':rank=[]
            elif mode=='L':rank=bm25(q['question'],[chunks[i] for i in candidates])
            else:
                allowed=[]
                for i in candidates:
                    if mode=='C' and not compatible(meta[chunks[i]['id']],q['query_attributes']):
                        excluded.append({'chunk_id':chunks[i]['id']})
                    else:allowed.append(i)
                v=vectors['B' if mode=='C' else mode]
                rank=sorted([(float(v[i]@queries[qi]),chunks[i]) for i in allowed],key=lambda p:(-p[0],p[1]['id']))
            selected=[c for _,c in rank[:5]]; removed=[]
            while True:
                ev=[{k:c[k] for k in ('id','title','url','location','text')} for c in selected]
                text='Pergunta: '+q['question']+'\nEvidências:\n'+json.dumps(ev,ensure_ascii=False)
                prompt=qtok.apply_chat_template([{'role':'system','content':config['answer_instruction']},
                    {'role':'user','content':text}],tokenize=False,add_generation_prompt=True,enable_thinking=False)
                count=len(qtok.encode(prompt))
                if count<=4096:break
                if not selected:raise ValueError('Pergunta excede orçamento')
                removed.append(selected.pop()['id'])
            retrieval.append({'question_id':q['id'],'config':mode,'excluded':excluded,
               'ranked':[{'chunk_id':c['id'],'score':s} for s,c in rank[:10]],
               'prompt_evidence_ids':[e['id'] for e in ev],'budget_removed_ids':removed})
            for seed in ([None,43,44] if q['id'] in stable and mode in ('A','B','C') else [None]):
                prompts.append({'id':phase+'-'+q['id']+'-'+mode+'-'+str(seed),
                   'question_id':q['id'],'family':q['family'],'config':mode,'seed':seed,'phase':phase,'prompt':prompt,
                   'prompt_tokens':count,'evidence':ev})
    write_records(out/'prompts.jsonl',prompts);write_records(out/'retrieval.jsonl',retrieval)
    hashes={k:file_sha(v) for k,v in {'config':config_path,'chunks':chunks_path,'metadata':metadata_path,
                  'questions':questions_path,'dossiers':dossiers_path,'index_inputs':Path(indices)/'inputs.json',
                  'prompts':out/'prompts.jsonl','retrieval':out/'retrieval.jsonl'}.items()}
    write(out/'freeze.json',{'phase':phase,'input_hashes':hashes,'questions':len(qs),
          'families':sorted({q['family'] for q in qs}),'stability_questions':sorted(stable),
          'expected_generations':len(prompts),'human_validated':False})


def judge_inputs(config_path,questions_path,dossiers_path,prompts_path,answers_path,output):
    from evaluate import prompt,SCHEMA
    tok=tokenizer(load(config_path),'qwen')
    qs={q['id']:q for q in records(questions_path)};ds={d['question_id']:d for d in records(dossiers_path)}
    answers={a['id']:a for a in records(answers_path)};inputs=[]
    for p in records(prompts_path):
        a=answers[p['id']]
        if a['status']!='completed':continue
        q=qs[p['question_id']]; ref=ds[q['id']]
        # O juiz recebe o conteúdo e os IDs, sem configuração, semente ou prefixos.
        rendered=prompt(tok,q['question'],{'expected':ref['expected'],'requirements':ref['requirements'],
                 'class':q['class']},p['evidence'],a['answer'])
        if len(tok.encode(rendered))>7168:raise ValueError('Julgamento excede orçamento')
        inputs.append({'id':'judge-'+p['id'],'answer_id':p['id'],'prompt':rendered,'json_schema':SCHEMA})
    write_records(output,inputs)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest='command',required=True)
    c=s.add_parser('metadata');c.add_argument('chunks');c.add_argument('output')
    c=s.add_parser('prepare')
    for f in ('config','chunks','metadata','questions','dossiers','indices','output','phase'):c.add_argument(f)
    c=s.add_parser('judge')
    for f in ('config','questions','dossiers','prompts','answers','output'):c.add_argument(f)
    a=p.parse_args()
    if a.command=='metadata':metadata(a.chunks,a.output)
    elif a.command=='prepare':prepare(a.config,a.chunks,a.metadata,a.questions,a.dossiers,a.indices,a.output,a.phase)
    else:judge_inputs(a.config,a.questions,a.dossiers,a.prompts,a.answers,a.output)
