"""72 saídas técnicas, contexto fixo; conferência individual separada da adequação."""
import argparse
import os
import json
import random
from pathlib import Path
from study import digest, load, write, write_csv, write_records


def main(config_path,cases_path,output,judges=1):
    if judges not in (1,2):raise ValueError('Escolha um ou dois julgadores reais')
    os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
    import torch
    from transformers import AutoModelForCausalLM,LogitsProcessorList,RepetitionPenaltyLogitsProcessor
    from experiment import tokenizer,environment,revisions
    from audit import degenerate,verify_processor
    config,cases=load(config_path),load(cases_path)
    revisions(config)
    if len(cases)!=12 or len({c['id'] for c in cases})!=12:raise ValueError('Exigir doze casos únicos congelados')
    out=Path(output);out.mkdir(parents=True,exist_ok=False)
    write(out/'processor-test.json',verify_processor())
    write(out/'environment.json',environment(config,{'config':config_path,'cases':cases_path}))
    torch.use_deterministic_algorithms(True)
    torch.manual_seed(2026)
    tok=tokenizer(config,'qwen')
    dtype=torch.float16 if config['device'].startswith('cuda') else torch.float32
    model=AutoModelForCausalLM.from_pretrained(config['qwen_model'],revision=config['qwen_revision'],torch_dtype=dtype).to(config['device']).eval()
    results=[]
    for case in cases:
        user='Pergunta: '+case['question']+'\nEvidências:\n'+json.dumps(case['evidence'],ensure_ascii=False)
        prompt=tok.apply_chat_template([{'role':'system','content':config['answer_instruction']},{'role':'user','content':user}],
                                      tokenize=False,add_generation_prompt=True,enable_thinking=False)
        inputs=tok(prompt,return_tensors='pt').to(config['device'])
        if inputs['input_ids'].shape[-1]>4096:raise ValueError('Caso excede contexto')
        for penalty in (1.0,1.05):
            for seed in (None,43,44):
                torch.manual_seed(2026 if seed is None else seed)
                kwargs={'do_sample':seed is not None,'num_beams':1,'max_new_tokens':512,'repetition_penalty':1.0}
                if seed is not None:kwargs.update(temperature=.7,top_p=.8,top_k=20,min_p=0.0)
                if penalty==1.05:kwargs['logits_processor']=LogitsProcessorList([RepetitionPenaltyLogitsProcessor(1.05,prompt_ignore_length=inputs['input_ids'].shape[-1])])
                with torch.inference_mode():generated=model.generate(**inputs,**kwargs)
                tokens=generated[0,inputs['input_ids'].shape[-1]:].tolist()
                results.append({'case_id':case['id'],'seed':seed,'penalty':penalty,'prompt':prompt,'prompt_sha256':digest(prompt),
                    'answer':tok.decode(tokens,skip_special_tokens=True),'degeneration':degenerate(tokens),'required_items':case['required_items']})
    write_records(out/'private-results.jsonl',results)
    rng=random.Random(2026);rng.shuffle(results)
    key,rows=[],[]
    for i,r in enumerate(results):
        blind_id=f'tecnico-{i+1:03d}'
        key.append({'blind_id':blind_id,'case_id':r['case_id'],'seed':r['seed'],'penalty':r['penalty']})
        rows.append({'blind_id':blind_id,'answer':r['answer'],'required_items':json.dumps(r['required_items'],ensure_ascii=False),
                     'preserved_items':'','omissions':'','alterations':'','invented_identifiers':'','notes':''})
    write_records(out/'private_key.jsonl',key)
    for judge in ('J1','J2')[:judges]:
        ordered=list(rows);rng.shuffle(ordered)
        write_csv(out/(judge+'.csv'),ordered,list(rows[0]))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('config','cases','output'):p.add_argument(name)
    p.add_argument('--judges',type=int,choices=(1,2),default=1)
    a=p.parse_args();main(a.config,a.cases,a.output,a.judges)
