"""Executor local retomável. GGUF é uma extensão registrada do desenho original."""
import argparse
import hashlib
import json
import re
import subprocess
import time
import urllib.request
import fcntl
from pathlib import Path

from study import records, digest, load


def atomic(path, value):
    path = Path(path)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(path)


def parameters(seed=None):
    return {'temperature': 0 if seed is None else .7, 'top_p': .8, 'top_k': 20,
            'min_p': 0, 'seed': 42 if seed is None else seed, 'n_predict': 512,
            'repeat_penalty': 1.0, 'presence_penalty': 0.0, 'frequency_penalty': 0.0,
            'cache_prompt': True, 'stream': False, 'return_tokens': True}


def execute(inputs, endpoint, output, call=None, identity=None):
    out=Path(output);out.mkdir(parents=True,exist_ok=True)
    with (out/'.execution.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        return _execute(inputs,endpoint,output,call,identity)


def _execute(inputs, endpoint, output, call=None, identity=None):
    """Cada resposta só é reutilizada com a mesma entrada e parâmetros."""
    if endpoint != 'http://127.0.0.1:18771':
        raise ValueError('Somente servidor local cadastrado')
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    if len({r['id'] for r in inputs}) != len(inputs):
        raise ValueError('Identificadores de execução duplicados')
    if call is None:
        def call(payload):
            request = urllib.request.Request(endpoint + '/completion',
                data=json.dumps(payload).encode(), headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(request, timeout=900) as response:
                return json.load(response)
    results = []
    for item in inputs:
        params = parameters(item.get('seed'))
        if item.get('json_schema'):
            params['json_schema'] = item['json_schema']
        fingerprint = digest(json.dumps({'input':item, 'parameters':params, 'runtime':identity}, sort_keys=True))
        path = out / (hashlib.sha256(item['id'].encode()).hexdigest() + '.json')
        if path.exists():
            row = load(path)
            if row.get('fingerprint') != fingerprint:
                raise ValueError('Checkpoint divergente; escolha outro diretório')
        else:
            start = time.monotonic()
            errors = []
            response = None
            for attempt in range(2):
                try:
                    response = call(dict(params, prompt=item['prompt']))
                    if not isinstance(response.get('content'), str):
                        raise ValueError('Resposta sem conteúdo textual')
                    break
                except Exception as error:
                    errors.append(type(error).__name__ + ': ' + str(error))
            row = {'id':item['id'], 'fingerprint':fingerprint,
                'prompt_sha256':digest(item['prompt']), 'parameters':params,
                'elapsed_seconds':time.monotonic()-start, 'errors':errors,
                'status':'completed' if response is not None else 'failed',
                'answer':response['content'] if response else None,
                'engine_response':response, 'human_validated':False}
            atomic(path, row)
        results.append(row)
        atomic(out / 'progress.json', {'completed':len(results), 'expected':len(inputs),
               'failed':sum(r['status']=='failed' for r in results)})
        print(json.dumps({'id':item['id'], 'completed':len(results), 'expected':len(inputs),
              'status':row['status'], 'seconds':round(row['elapsed_seconds'],1)}), flush=True)
    tmp = out / 'answers.jsonl.tmp'
    tmp.write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in results))
    tmp.replace(out / 'answers.jsonl')
    return results


def check_final(inputs, gate_path):
    finals=[r for r in inputs if r.get('phase')=='final']
    if not finals: return
    if not gate_path: raise ValueError('Etapa final exige registro público e controle assistido')
    gate=load(gate_path)
    if gate.get('method')!='assisted_exploratory_final' or gate.get('human_validated') is not False:
        raise ValueError('Declaração de método inválida')
    url=gate.get('public_registration_url','')
    if not re.fullmatch(r'https://github\.com/yhenriux/rag-bancario-publico/commit/[a-f0-9]{40}',url):
        raise ValueError('Registro exige commit público identificado')
    if any(r.get('family') in gate.get('pilot_families',[]) for r in finals):
        raise ValueError('Família do piloto presente na etapa final')
    if gate.get('inputs_sha256')!=digest(json.dumps(inputs,sort_keys=True)):
        raise ValueError('Entradas divergem do registro')
    for field in ('fidelity','pilot','sources'):
        check=gate['checks'][field]
        data=Path(check['path']).read_bytes()
        if hashlib.sha256(data).hexdigest()!=check['sha256']:
            raise ValueError('Controle divergente: '+field)
    if not load(gate['checks']['fidelity']['path']).get('passed'):
        raise ValueError('Fidelidade não aprovada')
    if not load(gate['checks']['pilot']['path']).get('completed'):
        raise ValueError('Piloto incompleto')
    if any(r['degenerate'] or r['failed'] for r in load(gate['checks']['pilot']['path'])['technical_summary']):
        raise ValueError('Piloto exige tratamento de falha ou repetição antes da etapa final')


def local(inputs, executable, model_file, output, threads=8, gate_path=None):
    check_final(inputs,gate_path)
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    args = [executable, '-m', model_file, '-c', '8192', '-b', '512', '-ub', '128', '--no-repack', '--cache-ram', '0', '-t', str(threads),
            '-tb', str(threads), '-np', '1', '-ngl', '0', '--host', '127.0.0.1',
            '--port', '18771', '--no-webui', '--no-warmup']
    sha=hashlib.sha256()
    with Path(model_file).open('rb') as stream:
        for block in iter(lambda:stream.read(8*1024*1024),b''):sha.update(block)
    identity={'backend':'llama.cpp b11557','precision':'Q4_K_M','threads':threads,
              'model_sha256':sha.hexdigest(),'executable_sha256':hashlib.sha256(Path(executable).read_bytes()).hexdigest(),
              'context_tokens':8192,'gpu_layers':0,'batch_tokens':512,'microbatch_tokens':128,
              'weight_repacking':False,'global_prompt_cache_mib':0}
    atomic(out / 'runtime.json', dict(identity,server_command=args,inputs_sha256=digest(json.dumps(inputs,sort_keys=True))))
    with (out / 'server.log').open('a') as log:
        server = subprocess.Popen(args, stdout=log, stderr=log)
        try:
            for _ in range(60):
                if server.poll() is not None: raise RuntimeError('Servidor encerrou; veja server.log')
                try:
                    with urllib.request.urlopen('http://127.0.0.1:18771/health',timeout=1) as r:
                        if r.status==200: break
                except Exception: time.sleep(1)
            else: raise RuntimeError('Servidor não ficou pronto')
            return execute(inputs, 'http://127.0.0.1:18771', out,identity=identity)
        finally:
            server.terminate()
            try: server.wait(timeout=10)
            except subprocess.TimeoutExpired: server.kill(); server.wait()


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('inputs','executable','model_file','output'): p.add_argument(k)
    p.add_argument('--threads',type=int,default=8)
    p.add_argument('--gate')
    a=p.parse_args()
    local(records(a.inputs),a.executable,a.model_file,a.output,a.threads,a.gate)
