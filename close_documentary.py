"""Fecha a análise documental usando rankings congelados; não executa modelos."""
import argparse
from collections import Counter
from pathlib import Path
from statistics import mean
from audit import retrieval_metrics
from analysis_run import summarize_retrieval, diagnostics
from study import load, records, write, write_records, digest, validate_questions


def close(root, output):
    root, output = Path(root), Path(output)
    output.mkdir(parents=True, exist_ok=False)
    docs = records(root/'documents.jsonl')
    chunks = records(root/'chunks.jsonl')
    units = records(root/'dataset-v2/reference-units.jsonl')
    unit_map = load(root/'dataset-v2/unit-map.json')
    by_doc = {d['document_id']: d for d in docs}
    by_chunk = {c['id']: c for c in chunks}
    by_unit = {u['id']: u for u in units}
    assert len(by_doc) == len(docs) and len(by_chunk) == len(chunks)
    assert len(by_unit) == len(units)
    import hashlib
    originals = list((root.resolve().parents[1]/'data').rglob('raw/*'))
    for d in docs:
        if not any(p.is_file() and p.stem==d['document_id'] and
                   hashlib.sha256(p.read_bytes()).hexdigest()==d['sha256'] for p in originals):
            raise ValueError('Original ausente ou divergente: '+d['document_id'])
    checks = []
    for u in units:
        d = by_doc[u['document_id']]
        section = next(s for s in d['sections'] if s['location'] == u['location'])
        assert 0 <= u['char_start'] < u['char_end'] <= len(section['text'])
        assert d['sha256'] == u['source_sha256']
        checks.append({'unit_id':u['id'], 'document_id':d['document_id'],
                       'url':d['url'], 'positions_valid':True, 'source_hash_matches':True})
    for cid, ids in unit_map.items():
        c = by_chunk[cid]
        for uid in ids:
            u = by_unit[uid]
            assert u['document_id'] == c['document_id'] and u['location'] == c['location']
            assert c['char_start'] <= u['char_start'] < u['char_end'] <= c['char_end']
    write_records(output/'reference-audit.jsonl', checks)
    write(output/'source-audit.json', {
        'documents':len(docs), 'chunks':len(chunks), 'reference_anchors':len(units),
        'snapshot_bytes_verified':len(docs), 'verification':'sha256 de todos os originais usados',
        'banks':dict(Counter(d['bank'] for d in docs)),
        'all_registry_records_present':all(bool(d.get('source_registry')) for d in docs),
        'all_robots_hashes_present':all(bool(d.get('robots_sha256')) for d in docs),
        'express_permission_from_banks':False, 'source_redistribution_approved':False,
        'review_kind':'registro operacional assistido; não constitui parecer jurídico',
        'human_independent_review':False})
    families = set()
    for phase in ('pilot','final'):
        qs = records(root/'dataset-v2'/f'{phase}-questions.jsonl')
        validate_questions(qs, families if phase=='final' else ())
        if phase=='pilot': families = {q['family'] for q in qs}
        folder = output/phase
        folder.mkdir()
        ranking = records(root/f'{phase}-inputs/retrieval.jsonl')
        expected = {(q['id'],c) for q in qs for c in ('A','B','C','Bp','L','S')}
        assert len(ranking) == len(expected)
        assert {(r['question_id'],r['config']) for r in ranking} == expected
        for r in ranking:
            assert len({c['chunk_id'] for c in r['ranked']}) == len(r['ranked'])
            q = next(q for q in qs if q['id']==r['question_id'])
            assert all(by_chunk[c['chunk_id']]['bank']==q['bank'] for c in r['ranked'])
        write_records(folder/'retrieval.jsonl', ranking)
        retrieval_metrics(folder/'retrieval.jsonl', root/'dataset-v2'/f'{phase}-dossiers.jsonl',
                          root/'dataset-v2/unit-map.json', folder/'retrieval-metrics.jsonl')
        metrics = records(folder/'retrieval-metrics.jsonl')
        means, contrasts = summarize_retrieval(metrics, qs)
        dmap = {d['question_id']:d for d in records(root/'dataset-v2'/f'{phase}-dossiers.jsonl')}
        effective=[]
        for r in ranking:
            if r['config']=='S':continue
            q=next(q for q in qs if q['id']==r['question_id'])
            refs=set(dmap[q['id']]['reference_units'])
            excluded={c['chunk_id'] for c in r['excluded']}
            bank_ids={c['id'] for c in chunks if c['bank']==q['bank']}
            available={u for cid in bank_ids-excluded for u in unit_map.get(cid,[])}
            selected={u for cid in r['prompt_evidence_ids'] for u in unit_map.get(cid,[])}
            effective.append({'question_id':q['id'],'config':r['config'],
                'reference_anchors_unavailable_after_filter':sorted(refs-available),
                'prompt_anchor_recall':len(refs&selected)/len(refs) if refs else None,
                'budget_removed_ids':r['budget_removed_ids']})
        write_records(folder/'effective-context.jsonl',effective)
        write(folder/'summary.json', {'phase':phase,'scope':'documentary_retrieval',
            'retrieval_completed':True,'questions':len(qs),'families':len({q['family'] for q in qs}),
            'classes':dict(Counter(q['class'] for q in qs)), 'retrieval_pairs':5*len(qs),
            'retrieval_summary':means,'paired_exploratory_contrasts':contrasts,
            'automatic_adequacy_enabled':False,'human_validated':False,
            'filter_excluded_reference_questions':[r['question_id'] for r in effective
                if r['config']=='C' and r['reference_anchors_unavailable_after_filter']],
            'input_sha256':{'retrieval':digest((folder/'retrieval.jsonl').read_text())},
            'limitations':['amostra de conveniência','referências assistidas e sem avaliação independente',
                'atributos preparados incluem inferências','mudança de escopo posterior ao início da execução',
                'âncoras curtas não demonstram suficiência semântica','conjuntos não constituem validação externa']})
    prompts={p['id']:p for p in records(root/'pilot-inputs/prompts.jsonl')}
    answers=[load(p) for p in sorted((root/'pilot').glob('*.json')) if len(p.stem)==64]
    assert len({a['id'] for a in answers}) == len(answers)
    assert all(a['id'] in prompts for a in answers)
    diag=[diagnostics(prompts[a['id']],a) for a in answers]
    write_records(output/'partial-generation-diagnostics.jsonl',diag)
    write(output/'partial-generation.json', {'status':'partial_saved','saved':len(answers),
        'original_pilot_target':len(prompts),'original_final_target':60,
        'failed':sum(a['status']=='failed' for a in answers),
        'output_limited':sum(d['output_limited'] for d in diag),
        'invalid_citations':sum(bool(d['invalid_citations']) for d in diag),
        'missing_citations_with_evidence':sum(d['missing_citation_with_evidence'] for d in diag),
        'degenerate':sum(bool(d['degenerate']) for d in diag),
        'automatic_adequacy_enabled':False,'semantic_correctness_evaluated':False,
        'completed_ids':[a['id'] for a in answers],
        'interpretation':'subconjunto determinado pela interrupção, sem amostragem balanceada ou comparação válida de adequação'})
    return {'documents':len(docs),'chunks':len(chunks),'anchors':len(units),
            'retrieval_questions':30,'retrieval_pairs':150,'saved_generations':len(answers)}


if __name__=='__main__':
    import json
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('root');p.add_argument('output');a=p.parse_args()
    print(json.dumps(close(a.root,a.output),ensure_ascii=False))
