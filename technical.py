"""Teste técnico local com E5 e um servidor llama.cpp. Não substitui o piloto."""
import argparse
import json
import time
import subprocess
import urllib.request
from urllib.parse import urlsplit
from pathlib import Path

from experiment import encode, tokenizer, metadata_valid, file_sha
from study import CONFIGS, records, load, prefix, compatible, bm25, digest, write, write_records


def prepare(config_path, chunks_path, metadata_path, reference_path, output):
    import torch
    from transformers import AutoModel
    torch.set_num_threads(2)
    config, chunks, metadata, ref = load(config_path), records(chunks_path), load(metadata_path), load(reference_path)
    metadata_valid(chunks, metadata)
    tok = tokenizer(config, 'e5')
    model = AutoModel.from_pretrained(config['e5_model'], revision=config['e5_revision']).to('cpu')
    query = encode(['Instruct: ' + config['query_instruction'] + '\nQuery: ' + ref['question']], tok, model, 'cpu')[0]
    vectors = {}
    for mode in ('A', 'B', 'Bp'):
        texts = []
        for c in chunks:
            original = prefix(c, metadata[c['id']], mode)
            ids = tok.encode(original, add_special_tokens=False)
            texts.append((tok.decode(ids[:128]) if len(ids) > 128 else original) + c['text'])
        vectors[mode] = encode(texts, tok, model, 'cpu')
    qtok = tokenizer(config, 'qwen')
    outputs = []
    candidates = [i for i, c in enumerate(chunks) if c['bank'] == ref['bank']]
    for mode in CONFIGS:
        excluded = []
        if mode == 'S': ranking = []
        elif mode == 'L': ranking = bm25(ref['question'], [chunks[i] for i in candidates])
        else:
            allowed = []
            for i in candidates:
                if mode == 'C' and not compatible(metadata[chunks[i]['id']], ref['query_attributes']):
                    excluded.append(chunks[i]['id'])
                else: allowed.append(i)
            vec = vectors['B' if mode == 'C' else mode]
            ranking = sorted([(float(vec[i] @ query), chunks[i]) for i in allowed], key=lambda p: (-p[0], p[1]['id']))
        selected = [c for _, c in ranking[:5]]
        removed = []
        while True:
            evidence = [{k: c[k] for k in ('id', 'title', 'url', 'location', 'text')} for c in selected]
            user = 'Pergunta: ' + ref['question'] + '\nEvidências:\n' + json.dumps(evidence, ensure_ascii=False)
            prompt = qtok.apply_chat_template([{'role':'system', 'content':config['answer_instruction']},
                {'role':'user', 'content':user}], tokenize=False, add_generation_prompt=True, enable_thinking=False)
            tokens = len(qtok.encode(prompt))
            if tokens <= 4096: break
            if not selected: raise ValueError('Instrução e pergunta ultrapassam o orçamento')
            removed.append(selected.pop()['id'])
        outputs.append({'config':mode, 'prompt':prompt, 'prompt_sha256':digest(prompt),
            'prompt_tokens':tokens, 'evidence':evidence, 'excluded':excluded, 'removed':removed,
            'ranking':[{'chunk_id':c['id'], 'score':score} for score, c in ranking[:10]]})
    write_records(output, outputs)
    write(str(output) + '.inputs.json', {'phase':'technical_smoke', 'human_validated':False,
        'excluded_from_final':True, 'config':config,
        'input_hashes':{str(p):file_sha(p) for p in (config_path, chunks_path, metadata_path, reference_path)}})


def generate(prompts_path, endpoint, output, max_tokens=512):
    address = urlsplit(endpoint)
    if address.scheme != 'http' or address.hostname != '127.0.0.1' or not address.port or address.username or address.password or address.path or address.query or address.fragment:
        raise ValueError('Este teste usa somente servidor local')
    inputs = records(prompts_path)
    if not inputs or not 1 <= max_tokens <= 512:
        raise ValueError('Forneça entradas e um limite de saída entre 1 e 512')
    if Path(output).exists():
        raise ValueError('Escolha um novo caminho para esta execução')
    results = []
    # A última chamada repete A para verificar a geração no mesmo ambiente.
    for item in inputs + [inputs[0]]:
        payload = {'prompt':item['prompt'], 'temperature':0, 'n_predict':max_tokens,
                   'seed':42, 'repeat_penalty':1.0, 'presence_penalty':0.0,
                   'frequency_penalty':0.0, 'cache_prompt':False, 'stream':False}
        request = urllib.request.Request(endpoint + '/completion', data=json.dumps(payload).encode(),
                                         headers={'Content-Type':'application/json'})
        start = time.monotonic()
        with urllib.request.urlopen(request, timeout=600) as response: result = json.load(response)
        results.append({'config':item['config'], 'repeat':len(results) == len(inputs),
            'prompt_sha256':item['prompt_sha256'], 'answer':result['content'],
            'elapsed_seconds':time.monotonic()-start, 'engine_response':result,
            'request_parameters':{k:v for k,v in payload.items() if k != 'prompt'},
            'human_validated':False, 'phase':'technical_smoke'})
        write(str(output) + '.' + str(len(results)) + '.json', results[-1])
        print(json.dumps({'config':item['config'], 'completed':len(results),
                          'seconds':round(results[-1]['elapsed_seconds'], 2)}), flush=True)
    write_records(output, results)
    write(str(output)+'.summary.json', {'configurations':len(inputs), 'generations':len(results),
        'repeat_identical':results[0]['answer'] == results[-1]['answer'],
        'human_validated':False, 'pilot_completed':False, 'max_output_tokens':max_tokens,
        'backend':'llama.cpp', 'precision':'Q4_K_M', 'prompts_sha256':file_sha(prompts_path)})


def local(prompts_path, executable, model_file, output):
    """Inicia e encerra o servidor na mesma execução, sem serviço externo."""
    endpoint = 'http://127.0.0.1:18771'
    args = [executable, '-m', model_file, '-c', '8192', '-t', '2', '-tb', '2',
            '-np', '1', '-ngl', '0', '--host', '127.0.0.1', '--port', '18771',
            '--no-webui', '--no-warmup']
    with Path(str(output)+'.server.log').open('x') as log:
        server = subprocess.Popen(args, stdout=log, stderr=log)
        try:
            for _ in range(90):
                if server.poll() is not None:
                    raise RuntimeError('Servidor encerrou; consultar o log')
                try:
                    with urllib.request.urlopen(endpoint+'/health', timeout=1) as response:
                        if response.status == 200: break
                except Exception: time.sleep(1)
            else: raise RuntimeError('Servidor não ficou pronto')
            generate(prompts_path, endpoint, output)
        finally:
            server.terminate()
            try: server.wait(timeout=10)
            except subprocess.TimeoutExpired: server.kill(); server.wait()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    p = commands.add_parser('prepare')
    for key in ('config', 'chunks', 'metadata', 'reference', 'output'): p.add_argument(key)
    p = commands.add_parser('generate')
    for key in ('prompts', 'endpoint', 'output'): p.add_argument(key)
    p.add_argument('--max-tokens', type=int, default=512)
    p = commands.add_parser('local')
    for key in ('prompts', 'executable', 'model_file', 'output'): p.add_argument(key)
    args = parser.parse_args()
    if args.command == 'prepare': prepare(args.config, args.chunks, args.metadata, args.reference, args.output)
    elif args.command == 'generate': generate(args.prompts, args.endpoint, args.output, args.max_tokens)
    else: local(args.prompts, args.executable, args.model_file, args.output)
