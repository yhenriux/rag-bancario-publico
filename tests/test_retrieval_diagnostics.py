import unittest
from pathlib import Path
from retrieval_diagnostics import diagnose, measure
from study import load


class DiagnosticChecks(unittest.TestCase):
    def test_anchor_positions_deduplicate_overlap_and_handle_absence(self):
        ranking = [{'chunk_id': c} for c in ('x', 'y', 'z')]
        dossier = {'reference_units': ['a', 'b'], 'sufficient_sets': [['a', 'b']]}
        m = measure(ranking, dossier, {'x': ['a'], 'y': ['a'], 'z': []})
        self.assertEqual(m['anchor_positions_top10'], {'a': 1, 'b': None})
        self.assertEqual(m['recall_at3'], .5)
        self.assertEqual(m['coverage_at3'], 0)
        self.assertEqual(m['reciprocal_rank_at10'], 1)
        empty = measure(ranking, {'reference_units': [], 'sufficient_sets': []}, {})
        self.assertIsNone(empty['reciprocal_rank_at10'])

    def test_published_diagnostic_and_original_means_match(self):
        root = Path(__file__).resolve().parents[1]
        result, matrix = diagnose(root)
        self.assertEqual(result, load(root / 'docs/diagnostico-20261012/diagnostics.json'))
        self.assertEqual(len(matrix), 30)
        self.assertEqual(sum(r['anchor_count'] == 0 for r in matrix), 6)
        self.assertEqual({r['bank'] for r in matrix}, {'inter', 'bradesco'})
        for row in result['summary']:
            original = load(root / f"docs/results-20261012/{row['phase']}/summary.json")['retrieval_summary']
            matched = next(x for x in original if x['config'] == row['config'] and x['k'] == 5)
            self.assertEqual(row['recall_at5'], matched['mean_anchor_recall'])
            self.assertEqual(row['coverage_at5'], matched['all_anchors_covered'])
            strata = [s for s in result['summary_by_bank'] if s['phase'] == row['phase'] and s['config'] == row['config']]
            self.assertEqual(sum(s['eligible_questions'] for s in strata), row['eligible_questions'])
            for field in ('recall_at5', 'coverage_at5', 'reciprocal_rank_at10'):
                reconstructed = sum(s[field] * s['eligible_questions'] for s in strata) / row['eligible_questions']
                self.assertAlmostEqual(reconstructed, row[field], places=14)
        self.assertTrue(all(s['recall_at5'] == 1 for s in result['summary_by_bank'] if s['bank'] == 'inter'))
        cases = {r['question_id']: r for r in result['two_case_sensitivity']}
        self.assertEqual(cases['B05']['without_inferred_fields_recall_at5'], 0)
        self.assertEqual(cases['BF04']['without_inferred_fields_recall_at5'], 0)


if __name__ == '__main__': unittest.main()
