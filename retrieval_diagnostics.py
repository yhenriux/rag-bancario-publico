"""Diagnóstico posterior dos rankings publicados, sem executar modelos."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from study import covered, load, records, recall

MODES = ('A', 'B', 'C', 'Bp', 'L')
KS = (1, 3, 5, 10)


def measure(ranking, dossier, unit_map):
    references = set(dossier['reference_units'])
    positions = {u: next((i for i, c in enumerate(ranking[:10], 1)
                         if u in unit_map.get(c['chunk_id'], [])), None)
                 for u in sorted(references)}
    first = min((p for p in positions.values() if p is not None), default=None)
    result = {'anchor_positions_top10': positions, 'first_anchor_rank_top10': first,
              'reciprocal_rank_at10': (1 / first if first else 0) if references else None}
    for k in KS:
        units = {u for c in ranking[:k] for u in unit_map.get(c['chunk_id'], [])}
        result['recall_at' + str(k)] = recall(units, references)
        result['coverage_at' + str(k)] = covered(units, dossier['sufficient_sets']) if dossier['sufficient_sets'] else None
    return result


def diagnose(root):
    root = Path(root)
    cfg = root / 'configs/execution-20261012'
    base = root / 'docs/results-20261012'
    unit_map = load(cfg / 'unit-map.json')
    rows, summaries, discordants, filter_differences, matrix = [], [], [], [], []
    sources = [cfg / n for n in ('catalog.jsonl', 'unit-map.json')]
    phases = {}
    for phase in ('pilot', 'final'):
        questions = records(cfg / (phase + '-questions.jsonl'))
        dossiers = {d['question_id']: d for d in records(cfg / (phase + '-dossiers.jsonl'))}
        rankings = {(r['question_id'], r['config']): r for r in records(base / phase / 'retrieval.jsonl')}
        sources += [cfg / (phase + '-questions.jsonl'), cfg / (phase + '-dossiers.jsonl'), base / phase / 'retrieval.jsonl']
        measurements = {}
        for q in questions:
            cells = {}
            for mode in MODES:
                m = measure(rankings[q['id'], mode]['ranked'], dossiers[q['id']], unit_map)
                row = {'phase': phase, 'question_id': q['id'], 'bank': q['bank'], 'class': q['class'], 'config': mode, **m}
                rows.append(row); measurements[q['id'], mode] = row
                cells[mode] = m
            matrix.append({'phase': phase, 'question_id': q['id'], 'cells': cells})
        phases[phase] = (questions, rankings, dossiers, measurements)
        for mode in MODES:
            selected = [r for r in rows if r['phase'] == phase and r['config'] == mode and r['recall_at5'] is not None]
            summary = {'phase': phase, 'config': mode, 'eligible_questions': len(selected)}
            for field in [*(f'recall_at{k}' for k in KS), *(f'coverage_at{k}' for k in KS), 'reciprocal_rank_at10']:
                summary[field] = sum(r[field] for r in selected) / len(selected) if selected else None
            summaries.append(summary)
        for left, right in (('B', 'A'), ('B', 'Bp'), ('C', 'B')):
            eligible = [q for q in questions if dossiers[q['id']]['reference_units'] and
                        (left == 'C' or q['class'] in ('condicao', 'excecao'))]
            for field in ('recall_at5', 'coverage_at5'):
                wins, losses, ties = [], [], []
                for q in eligible:
                    delta = measurements[q['id'], left][field] - measurements[q['id'], right][field]
                    (wins if delta > 0 else losses if delta < 0 else ties).append(q['id'])
                discordants.append({'phase': phase, 'contrast': left + '-' + right, 'metric': field,
                                    'eligible_questions': len(eligible), 'left_better': wins,
                                    'right_better': losses, 'ties': ties})
        for k in KS:
            changed = [q['id'] for q in questions if measurements[q['id'], 'C']['recall_at' + str(k)] != measurements[q['id'], 'B']['recall_at' + str(k)]]
            filter_differences.append({'phase': phase, 'k': k, 'recall_differs': changed})
        filter_differences.append({'phase': phase, 'ranked_order_differs': [q['id'] for q in questions
                                  if [c['chunk_id'] for c in rankings[q['id'], 'C']['ranked']] !=
                                     [c['chunk_id'] for c in rankings[q['id'], 'B']['ranked']]]})
    # Sensibilidade limitada a dois casos: a auditoria já classificava os campos.
    # Sem campos inferidos, B05 fica sem filtro; BF04 mantém a mesma seleção.
    audit_path = base / 'query-attribute-audit.jsonl'
    audit = records(audit_path); sources.append(audit_path)
    sensitivity = []
    for phase, qid in (('pilot', 'B05'), ('final', 'BF04')):
        questions, rankings, dossiers, measurements = phases[phase]
        q = next(q for q in questions if q['id'] == qid)
        removed = {a['field'] for a in audit if a['question_id'] == qid and a['preparation'] == 'inferencia_assistida'}
        attrs = {f: v for f, v in q['query_attributes'].items() if f not in removed}
        # Nenhuma nova ordenação estimada a partir de uma lista truncada.
        if attrs == q['query_attributes']:
            mode = 'C'
        elif not attrs:
            mode = 'B'
        else:
            raise ValueError('Sensibilidade exige reordenar todos os candidatos: ' + qid)
        sensitivity.append({'question_id': qid, 'removed_inferred_fields': sorted(removed),
                            'retained_attributes': attrs, 'equivalent_frozen_config': mode,
                            'original_C_recall_at5': measurements[qid, 'C']['recall_at5'],
                            'without_inferred_fields_recall_at5': measurements[qid, mode]['recall_at5']})
    result = {'analysis_timing': 'posthoc_after_review', 'scope': 'frozen_rankings_and_assisted_references',
              'candidate_chunks_by_bank': dict(sorted(Counter(c['bank'] for c in records(cfg / 'catalog.jsonl')).items())),
              'input_sha256': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
              'summary': summaries, 'discordant_pairs': discordants,
              'C_vs_B_differences': filter_differences, 'two_case_sensitivity': sensitivity, 'measurements': rows}
    return result, matrix


def markdown_matrix(matrix):
    text = ['# Matriz diagnóstica posterior', '',
            'Cada célula contém posição da primeira âncora no top 10 / recall@5 / cobertura@5. ',
            'NR: nenhuma âncora nas dez posições publicadas; NA: pergunta sem referência. ',
            'As posições não medem suficiência semântica. IDs `final` identificam o segundo conjunto histórico.', '',
            '| Pergunta | A | B | C | Bp | L |', '|---|---|---|---|---|---|']
    for row in matrix:
        cells = []
        for mode in MODES:
            m = row['cells'][mode]
            if m['recall_at5'] is None:
                cells.append('NA')
            else:
                position = m['first_anchor_rank_top10'] or 'NR'
                cells.append(f"{position} / {m['recall_at5']:g} / {m['coverage_at5']:g}")
        text.append('| ' + ' | '.join([row['question_id'], *cells]) + ' |')
    return '\n'.join(text) + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', default='.')
    parser.add_argument('--output', help='Diretório novo; omita para conferir o relatório publicado.')
    args = parser.parse_args()
    result, matrix = diagnose(args.root)
    if args.output:
        folder = Path(args.output); folder.mkdir(parents=True, exist_ok=False)
        (folder / 'diagnostics.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
        (folder / 'matrix.md').write_text(markdown_matrix(matrix))
        print(json.dumps({'output': str(folder), 'pairs': len(result['measurements'])}))
    else:
        folder = Path(args.root) / 'docs/diagnostico-20261012'
        if result != load(folder / 'diagnostics.json') or markdown_matrix(matrix) != (folder / 'matrix.md').read_text():
            raise ValueError('Diagnóstico publicado diverge')
        print(json.dumps({'diagnostics_match': True, 'pairs': len(result['measurements'])}))
