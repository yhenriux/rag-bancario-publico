"""Registra as versões dos modelos e os arquivos usados em uma execução."""
import argparse
import json
from urllib.request import Request,urlopen
from urllib.parse import quote
from study import load,write
from experiment import file_sha


def model_revisions(config_path,output):
    config=load(config_path)
    for model in ('e5','qwen'):
        url='https://huggingface.co/api/models/'+quote(config[model+'_model'],safe='/')
        with urlopen(Request(url,headers={'User-Agent':'RAGBankingStudy/0.2'}),timeout=30) as response:
            payload=json.load(response)
        sha=payload['sha']
        if len(sha)!=40 or any(c not in '0123456789abcdef' for c in sha):
            raise ValueError('O serviço não retornou uma versão válida do modelo')
        config[model+'_revision']=sha
    write(output,config)


def file_hashes(output,names):
    paths={}
    for entry in names:
        name,separator,path=entry.partition('=')
        if not separator or not name or not path or name in paths:raise ValueError('Use nome=caminho, sem repetir nomes')
        paths[name]=file_sha(path)
    if not paths:raise ValueError('Informe pelo menos um arquivo')
    write(output,paths)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    subs=p.add_subparsers(dest='command',required=True)
    c=subs.add_parser('revisions',help='Registrar a versão atual de cada modelo, sem baixar os pesos')
    c.add_argument('config');c.add_argument('output')
    c=subs.add_parser('hashes',help='Calcular códigos que permitem conferir se os arquivos mudaram')
    c.add_argument('output');c.add_argument('files',nargs='+')
    a=p.parse_args()
    if a.command=='revisions':model_revisions(a.config,a.output)
    else:file_hashes(a.output,a.files)
