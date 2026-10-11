"""Refaz a análise documental pública; não baixa modelos ou textos bancários."""
import argparse
import tempfile
from pathlib import Path
from audit import retrieval_metrics
from analysis_run import summarize_retrieval
from study import load,records


def replay(root):
    root=Path(root);output=[]
    for phase in ('pilot','final'):
        result=root/'docs/results-20261011'/phase
        config=root/'configs/execution-20261011'
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp)/'metrics.jsonl'
            retrieval_metrics(result/'retrieval.jsonl',config/(phase+'-dossiers.jsonl'),config/'unit-map.json',target)
            metrics=records(target)
            if metrics!=records(result/'retrieval-metrics.jsonl'):
                raise ValueError('Métricas documentais divergem: '+phase)
            means,contrasts=summarize_retrieval(metrics,records(config/(phase+'-questions.jsonl')))
            summary=load(result/'summary.json')
            if means!=summary['retrieval_summary'] or contrasts!=summary['paired_exploratory_contrasts']:
                raise ValueError('Resumo ou reamostragem diverge: '+phase)
            output.append({'phase':phase,'metrics_match':True,'bootstrap_match':True})
    return output

if __name__=='__main__':
    import json
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',nargs='?',default='.')
    print(json.dumps(replay(p.parse_args().root),ensure_ascii=False))
