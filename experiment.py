"""Segmentação, recuperação E5/BM25 e geração Qwen conforme seis configurações."""
import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
from pathlib import Path

from study import (CONFIGS, compatible, digest, load, prefix, records, stability_sample,
                   validate_questions, bm25, write, write_records)


def revisions(config):
    for field in ('e5_revision', 'qwen_revision'):
        value = config.get(field, '')
        if len(value) != 40 or any(ch not in '0123456789abcdef' for ch in value):
            raise ValueError(f'Congelar SHA de revisão do modelo: {field}')


def tokenizer(config, model):
    from transformers import AutoTokenizer
    return AutoTokenizer.from_pretrained(config[model + '_model'], revision=config[model + '_revision'])


def segment(documents, config, output, allow_assisted=False):
    revisions(config)
    tok = tokenizer(config, 'e5')
    chunks = []
    for doc in records(documents):
        assisted = doc.get('extraction_review') == 'assisted_checked' and doc.get('review_origin') and doc.get('review_record')
        if doc['extraction_review'] != 'approved' and not (allow_assisted and assisted):
            raise ValueError('Extração requer revisão registrada; a opção assistida exige origem e registro explícitos')
        for section in doc['sections']:
            text = section['text']
            encoded = tok(text, add_special_tokens=False, return_offsets_mapping=True)
            offsets = encoded['offset_mapping']
            start = 0
            while start < len(offsets):
                end = min(start + 320, len(offsets))
                first, last = offsets[start][0], offsets[end-1][1]
                identity = f'{doc["document_id"]}:{section["location"]}:{start}:{end}'
                chunks.append({'id': digest(identity), 'document_id': doc['document_id'],
                    'bank': doc['bank'], 'title': doc['title'], 'section': section['section'],
                    'url': doc['final_url'], 'location': section['location'],
                    'token_start': start, 'token_end': end, 'char_start': first, 'char_end': last,
                    'text': text[first:last], 'source_sha256': doc['sha256'],
                    'extraction_review': doc['extraction_review'], 'review_origin': doc.get('review_origin')})
                if end == len(offsets): break
                start = end - 48
    write_records(output, chunks)


def metadata_valid(chunks, metadata):
    for chunk in chunks:
        m = metadata[chunk['id']]
        for field in ('product', 'public'):
            values = m[field]
            if not isinstance(values, list) or not values or any(not isinstance(v,str) or not v.strip() for v in values):
                raise ValueError('Metadado sem categoria explícita')
            if any(v in ('geral', 'desconhecido') for v in values) and len(values) != 1:
                raise ValueError('Geral/desconhecido devem ser categorias isoladas, com justificativa')
        if not m.get('evidence') or not m.get('document_type') or not m.get('adjudication_id'):
            raise ValueError('Metadados conciliados exigem evidência, tipo e trilha da decisão')


def encode(texts, tok, model, device):
    import torch
    import torch.nn.functional as F
    result = []
    model.eval()
    for i in range(0, len(texts), 8):
        batch = tok(texts[i:i+8], max_length=512, truncation=True, padding=True, return_tensors='pt').to(device)
        with torch.inference_mode():
            hidden = model(**batch).last_hidden_state
            hidden = hidden.masked_fill(~batch['attention_mask'][..., None].bool(), 0.0)
            pooled = hidden.sum(dim=1) / batch['attention_mask'].sum(dim=1)[..., None]
            result.append(F.normalize(pooled, p=2, dim=1).cpu())
    if not result:
        raise ValueError('Coleção vazia')
    return torch.cat(result)


def index(chunks_path, metadata_path, config, output):
    import torch
    from transformers import AutoModel
    revisions(config)
    chunks, metadata = records(chunks_path), load(metadata_path)
    metadata_valid(chunks, metadata)
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    tok = tokenizer(config, 'e5')
    model = AutoModel.from_pretrained(config['e5_model'], revision=config['e5_revision']).to(config['device'])
    audit = []
    for mode in ('A', 'B', 'Bp'):
        texts = []
        for c in chunks:
            original = prefix(c, metadata[c['id']], mode)
            ids = tok.encode(original, add_special_tokens=False)
            limited = tok.decode(ids[:128]) if len(ids) > 128 else original
            text = limited + c['text']
            audit.append({'chunk_id': c['id'], 'config': mode, 'prefix_token_count': len(ids),
                          'prefix_truncated': len(ids) > 128,
                          'input_truncated': len(tok.encode(text)) > 512})
            texts.append(text)
        torch.save(encode(texts, tok, model, config['device']), out / (mode + '.pt'))
    write_records(out / 'audit.jsonl', audit)
    write(out / 'inputs.json', {'config': config, 'chunks_sha256': file_sha(chunks_path),
                               'metadata_sha256': file_sha(metadata_path)})


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def final_gate(path, inputs):
    gate = load(path)
    for key in ('public_registration_url', 'registered_at', 'ethics_review_record', 'roles_record',
                'pilot_decision_record', 'sample_decision_record', 'fidelity_decision_record'):
        if not gate.get(key): raise ValueError(f'Etapa final bloqueada: {key}')
    if not gate['public_registration_url'].startswith('https://'):
        raise ValueError('Depósito público requer URL HTTPS real')
    for key, path in inputs.items():
        if gate['input_hashes'].get(key) != file_sha(path):
            raise ValueError(f'Arquivo divergente do congelamento: {key}')


def environment(config, inputs):
    packages = {}
    for name in ('torch', 'transformers', 'numpy', 'beautifulsoup4', 'pypdf'):
        try: packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError: packages[name] = None
    return {'python': platform.python_version(), 'platform': platform.platform(),
            'packages': packages, 'config': config, 'input_hashes': {k: file_sha(p) for k,p in inputs.items()},
            'code_hashes': {p: file_sha(Path(__file__).parent / p) for p in ('experiment.py','study.py','collect.py','audit.py','fidelity.py')}}


def run(config_path, chunks_path, metadata_path, questions_path, indices, output, phase, gate_path=None):
    os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
    import torch
    from transformers import AutoModel, AutoModelForCausalLM, LogitsProcessorList, RepetitionPenaltyLogitsProcessor
    config = load(config_path)
    revisions(config)
    if importlib.metadata.version('transformers') != '4.57.1':
        raise ValueError('Esta implementação exige Transformers 4.57.1')
    torch.use_deterministic_algorithms(True)
    torch.manual_seed(2026)
    chunks, metadata, questions = records(chunks_path), load(metadata_path), records(questions_path)
    validate_questions(questions, config.get('pilot_families', []) if phase == 'final' else ())
    metadata_valid(chunks, metadata)
    if not questions or len({c['id'] for c in chunks}) != len(chunks):
        raise ValueError('Perguntas vazias ou trechos duplicados')
    indices = Path(indices)
    inputs = {'config': config_path, 'chunks': chunks_path, 'metadata': metadata_path, 'questions': questions_path,
              'index_inputs': indices / 'inputs.json', 'index_A': indices / 'A.pt',
              'index_B': indices / 'B.pt', 'index_Bp': indices / 'Bp.pt'}
    indexed = load(indices / 'inputs.json')
    if indexed['chunks_sha256'] != file_sha(chunks_path) or indexed['metadata_sha256'] != file_sha(metadata_path):
        raise ValueError('Índice divergente da coleção ou dos metadados')
    if indexed['config'] != config:
        raise ValueError('Reconstruir índices com a mesma configuração')
    if phase == 'final':
        if any(c.get('extraction_review') != 'approved' for c in chunks):
            raise ValueError('Trechos com revisão assistida exigem extensão registrada do controle da etapa final; disponíveis somente para teste/piloto')
        if not gate_path: raise ValueError('Etapa final exige congelamento documentado')
        if not config.get('pilot_families'):
            raise ValueError('Registre as famílias do piloto que devem ficar fora da etapa final')
        final_gate(gate_path, inputs)
    if config['generation_penalty'] not in (1.0, 1.05):
        raise ValueError('Política de repetição fora do protocolo')
    if config['generation_penalty'] == 1.05 and not config.get('fidelity_pass_record'):
        raise ValueError('Penalidade ajustada exige registro de fidelidade aceito')
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    write(out / 'environment.json', environment(config, inputs))
    e5_tok = tokenizer(config, 'e5')
    e5 = AutoModel.from_pretrained(config['e5_model'], revision=config['e5_revision']).to(config['device'])
    queries = encode(['Instruct: ' + config['query_instruction'] + '\nQuery: ' + q['question'] for q in questions],
                     e5_tok, e5, config['device'])
    del e5
    if torch.cuda.is_available(): torch.cuda.empty_cache()
    vectors = {mode: torch.load(indices / (mode + '.pt'), weights_only=True) for mode in ('A','B','Bp')}
    if any(v.shape[0] != len(chunks) for v in vectors.values()): raise ValueError('Índice incompleto')
    qwen_tok = tokenizer(config, 'qwen')
    dtype = torch.float16 if config['device'].startswith('cuda') else torch.float32
    generator = AutoModelForCausalLM.from_pretrained(config['qwen_model'], revision=config['qwen_revision'],
                                                     torch_dtype=dtype).to(config['device']).eval()
    stable = set(stability_sample(questions))
    results, retrieval = [], []
    for qi, q in enumerate(questions):
        candidates = [i for i,c in enumerate(chunks) if c['bank'] == q['bank']]
        if not candidates: raise ValueError(f'Banco sem coleção: {q["bank"]}')
        for mode in CONFIGS:
            excluded = []
            if mode == 'S': ranking = []
            elif mode == 'L': ranking = bm25(q['question'], [chunks[i] for i in candidates])
            else:
                allowed = []
                for i in candidates:
                    if mode == 'C' and not compatible(metadata[chunks[i]['id']], q['query_attributes']):
                        excluded.append({'chunk_id': chunks[i]['id'], 'query_attributes': q['query_attributes'],
                                         'metadata': metadata[chunks[i]['id']]})
                    else: allowed.append(i)
                vec = vectors['B' if mode == 'C' else mode]
                ranking = sorted([(float(vec[i] @ queries[qi]), chunks[i]) for i in allowed],
                                 key=lambda item: (-item[0], item[1]['id']))
            retrieval.append({'question_id': q['id'], 'config': mode, 'excluded': excluded,
                'ranked': [{'chunk_id': c['id'], 'score': s} for s,c in ranking[:10]],
                'candidate_count': len(candidates)})
            selected = [c for _, c in ranking[:5]]
            removed = []
            while True:
                evidence = [{'id': c['id'], 'title': c['title'], 'url': c['url'],
                             'location': c['location'], 'text': c['text']} for c in selected]
                user = 'Pergunta: ' + q['question'] + '\nEvidências:\n' + json.dumps(evidence, ensure_ascii=False)
                prompt = qwen_tok.apply_chat_template([{'role':'system','content':config['answer_instruction']},
                    {'role':'user','content':user}], tokenize=False, add_generation_prompt=True, enable_thinking=False)
                input_ids = qwen_tok(prompt, return_tensors='pt').to(config['device'])
                if input_ids['input_ids'].shape[-1] <= 4096: break
                if not selected: raise ValueError('Pergunta/instrução ultrapassa orçamento de entrada')
                removed.append(selected.pop()['id'])
            seeds = [None] + ([43,44] if mode in ('A','B','C') and q['id'] in stable else [])
            for seed in seeds:
                kwargs = {'do_sample': seed is not None, 'num_beams':1, 'max_new_tokens':512,
                          'repetition_penalty':1.0}
                if seed is not None:
                    torch.manual_seed(seed)
                    kwargs.update(temperature=.7, top_p=.8, top_k=20, min_p=0.0)
                if config['generation_penalty'] == 1.05:
                    kwargs['logits_processor'] = LogitsProcessorList([RepetitionPenaltyLogitsProcessor(
                        1.05, prompt_ignore_length=input_ids['input_ids'].shape[-1])])
                with torch.inference_mode(): generated = generator.generate(**input_ids, **kwargs)
                output_tokens = generated[0,input_ids['input_ids'].shape[-1]:].tolist()
                answer = qwen_tok.decode(output_tokens, skip_special_tokens=True)
                from audit import degenerate
                identity = f'{phase}:{q["id"]}:{mode}:{seed}'
                results.append({'run_id': digest(identity), 'question_id': q['id'], 'question':q['question'],
                    'bank':q['bank'], 'family':q['family'], 'phase':phase, 'config':mode, 'seed':seed,
                    'prompt':prompt, 'prompt_sha256':digest(prompt), 'evidence':evidence, 'answer':answer,
                    'removed_for_context':removed, 'generation_kwargs':{k:v for k,v in kwargs.items() if k!='logits_processor'}})
                results[-1]['degeneration'] = degenerate(output_tokens)
                results[-1]['generation_penalty'] = config['generation_penalty']
        # Checkpoints por pergunta limitam perda se uma execução pesada falhar.
        write_records(out / (q['id'] + '-runs.jsonl'), results)
        results = []
    write_records(out / 'retrieval.jsonl', retrieval)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    s = p.add_subparsers(dest='command', required=True)
    c = s.add_parser('segment'); c.add_argument('documents'); c.add_argument('config'); c.add_argument('output')
    c.add_argument('--allow-assisted', action='store_true')
    c = s.add_parser('index'); c.add_argument('chunks'); c.add_argument('metadata'); c.add_argument('config'); c.add_argument('output')
    c = s.add_parser('run')
    for name in ('config','chunks','metadata','questions','indices','output'): c.add_argument(name)
    c.add_argument('--phase', choices=('pilot','final'), default='pilot'); c.add_argument('--gate')
    a = p.parse_args()
    if a.command == 'segment': segment(a.documents, load(a.config), a.output, a.allow_assisted)
    elif a.command == 'index': index(a.chunks, a.metadata, load(a.config), a.output)
    else: run(a.config, a.chunks, a.metadata, a.questions, a.indices, a.output, a.phase, a.gate)
