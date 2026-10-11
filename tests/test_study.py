import math
import json
import csv
import tempfile
import unittest
from pathlib import Path

from study import (bm25, compatible, covered, kappa, paired_bootstrap, prefix, quantile,
                   recall, stability_sample, validate_questions, write)
from study import analyze, blind, write_records
from collect import check_url
from audit import degenerate
from study import agreement, combine, write_csv
from demo import demonstrate
from prepare import file_hashes


class StudyChecks(unittest.TestCase):
    def test_demonstration_is_labelled_and_shows_filter_cost(self):
        report=demonstrate()
        self.assertIn('fictício',report['status'])
        self.assertTrue(report['cases'][0]['coverage_after'])
        self.assertTrue(report['cases'][1]['coverage_before'])
        self.assertFalse(report['cases'][1]['coverage_after'])
        self.assertEqual(report['cases'][1]['removed'],['E4'])

    def test_invalid_question_fields_are_rejected(self):
        q={'id':'q','bank':'a','family':'a:f','class':'direta','question':'Pergunta','query_attributes':{}}
        for altered in ({**q,'id':[]},{**q,'question':''},{**q,'query_attributes':[]},
                        {**q,'query_attributes':{'product':['desconhecido']}},
                        {**q,'query_attributes':{'product':[1]}}):
            with self.assertRaises(ValueError):validate_questions([altered])
        with self.assertRaises(ValueError):validate_questions([])

    def test_agreement_normalizes_sets_and_refuses_missing_pair(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            rows=[{'item_id':'i1','attribute':'evidence','annotator':'R1','value':'["E1","E2"]'},
                  {'item_id':'i1','attribute':'evidence','annotator':'R2','value':'["E2","E1","E1"]'},
                  {'item_id':'i2','attribute':'evidence','annotator':'R1','value':'["E3"]'},
                  {'item_id':'i2','attribute':'evidence','annotator':'R2','value':'["E3","E4"]'}]
            write_csv(root/'annotations.csv',rows,list(rows[0]))
            agreement(root/'annotations.csv',root/'agreement.json',['R1','R2'],['evidence'])
            report=json.loads((root/'agreement.json').read_text())['evidence']
            self.assertEqual(report['n'],2)
            self.assertEqual(report['agreement'],.5)
            self.assertEqual(report['mean_jaccard'],.75)
            write_csv(root/'incomplete.csv',rows[:-1],list(rows[0]))
            with self.assertRaises(ValueError):agreement(root/'incomplete.csv',root/'missing.json',['R1','R2'],['evidence'])

    def test_combine_requires_completion_and_main_pairs(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            run={'run_id':'r','question_id':'q','config':'A','seed':None}
            write_records(root/'q-runs.jsonl',[run])
            with self.assertRaises(ValueError):combine(root,root/'incomplete.jsonl')
            write_records(root/'retrieval.jsonl',[{'question_id':'q','config':'A'}])
            combine(root,root/'combined.jsonl')
            self.assertEqual(json.loads((root/'combined.jsonl').read_text()),run)
            write_records(root/'extra-runs.jsonl',[{**run,'run_id':'r2'}])
            with self.assertRaises(ValueError):combine(root,root/'repeated.jsonl')

    def test_file_hashes_refuse_duplicate_names(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'file.txt').write_text('exemplo')
            file_hashes(root/'hashes.json',[f'file={root/"file.txt"}'])
            report=json.loads((root/'hashes.json').read_text())
            self.assertEqual(len(report['file']),64)
            with self.assertRaises(ValueError):file_hashes(root/'bad.json',[f'x={root/"file.txt"}',f'x={root/"file.txt"}'])
    def test_blind_and_analysis_with_fictional_inputs(self):
        qs=[{'id':'q1','bank':'ficticio','family':'ficticio:f1','class':'condicao',
             'question':'Pergunta fictícia','query_attributes':{'product':['alfa']}}]
        rs=[{'run_id':c,'question_id':'q1','config':c,'seed':None,'question':'Pergunta fictícia',
             'answer':'Resposta fictícia','evidence':[]} for c in ('A','B','C','Bp','L','S')]
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            write_records(root/'questions.jsonl',qs)
            write_records(root/'runs.jsonl',rs)
            blind(root/'runs.jsonl',root/'judging',2026)
            self.assertFalse((root/'judging'/'J2.csv').exists())
            blind(root/'runs.jsonl',root/'two-judges',2026,judges=2)
            self.assertTrue((root/'two-judges'/'J2.csv').exists())
            with self.assertRaises(ValueError):blind(root/'runs.jsonl',root/'invalid',2026,judges=0)
            with (root/'judging'/'J1.csv').open() as f:
                reader=csv.DictReader(f);rows=list(reader)
                self.assertNotIn('config',reader.fieldnames)
                self.assertNotIn('seed',reader.fieldnames)
                self.assertEqual(len(rows),6)
            from study import write_csv
            write_csv(root/'judgments.csv',[{'question_id':'q1','config':c,'adequacy':int(c in ('B','C'))}
                     for c in ('A','B','C','Bp','L','S')],['question_id','config','adequacy'])
            analyze(root/'questions.jsonl',root/'judgments.csv',root/'analysis.json')
            result=json.loads((root/'analysis.json').read_text())
            self.assertEqual(result['H1']['estimate'],1)
            self.assertEqual(result['H2']['estimate'],0)
            self.assertEqual(result['H3']['estimate'],1)

    def test_degeneration_boundary(self):
        self.assertIsNotNone(degenerate(list(range(20))*3))
        self.assertIsNone(degenerate(list(range(20))*2))
        self.assertIsNone(degenerate(list(range(19))*3))
    def test_filter_preserves_general_unknown_and_overlap(self):
        q = {'product':['alfa'], 'public':['pf']}
        self.assertTrue(compatible({'product':['geral'], 'public':['pf']}, q))
        self.assertTrue(compatible({'product':['desconhecido'], 'public':['desconhecido']}, q))
        self.assertTrue(compatible({'product':['alfa','beta'], 'public':['pf']}, q))
        self.assertFalse(compatible({'product':['beta'], 'public':['pf']}, q))
        self.assertTrue(compatible({'product':['beta'], 'public':['pf']}, {}))

    def test_quadro5_loss_and_duplicate_evidence(self):
        self.assertTrue(covered(['E3','E4','E4'], [['E3','E4']]))
        self.assertFalse(covered(['E3'], [['E3','E4']]))
        self.assertEqual(recall(['E3','E3'], ['E3','E4']), .5)
        self.assertIsNone(recall([], []))

    def test_bm25_stable_ties_and_accents(self):
        chunks = [{'id':'b','text':'cartão anuidade'}, {'id':'a','text':'cartão anuidade'},
                  {'id':'c','text':'conta saldo'}]
        result = bm25('cartão', chunks)
        self.assertEqual([c['id'] for _,c in result], ['a','b','c'])
        expected = math.log(1 + (3-2+.5)/(2+.5))
        self.assertAlmostEqual(result[0][0], expected)

    def test_pilot_exclusion_and_path_traversal(self):
        q = {'id':'p1','bank':'bank-a','family':'bank-a:f1','class':'condicao',
             'question':'Pergunta', 'query_attributes':{}}
        validate_questions([q])
        with self.assertRaises(ValueError): validate_questions([q], [q['family']])
        with self.assertRaises(ValueError): validate_questions([q,q])
        with self.assertRaises(ValueError): validate_questions([{**q,'id':'../secret'}])

    def test_bootstrap_is_paired_clustered_and_linear(self):
        pairs = [('a','a:f1',1), ('a','a:f1',1), ('b','b:f2',1)]
        result = paired_bootstrap(pairs, repetitions=40)
        self.assertEqual(result['estimate'],1)
        self.assertEqual(result['ci95'],[1,1])
        self.assertEqual(result['families_by_bank'],{'a':1,'b':1})
        self.assertEqual(quantile([0,1,2,3],.25),.75)
        self.assertEqual(kappa(['a','b'],['a','b'])['kappa'],1)
        self.assertIsNone(kappa(['a'],['a'])['kappa'])

    def test_prefix_ablation_and_stability(self):
        chunk = {'title':'Título', 'section':'Seção'}
        m = {'product':['alfa'], 'public':['pf'], 'document_type':'regra'}
        self.assertIn('Título',prefix(chunk,m,'B'))
        self.assertNotIn('Título',prefix(chunk,m,'Bp'))
        qs = [{'id':f'q{i}', 'bank':'a','class':'direta'} for i in range(4)]
        self.assertEqual(stability_sample(qs),stability_sample(list(reversed(qs))))
        self.assertEqual(len(stability_sample(qs)),1)

    def test_collection_boundary_and_immutable_output(self):
        check_url('https://bank.example/doc','bank.example')
        for url in ('http://bank.example/doc','https://other.example/doc','https://u:p@bank.example/doc'):
            with self.assertRaises(ValueError): check_url(url,'bank.example')
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'result.json'
            write(p, {'test':1})
            with self.assertRaises(FileExistsError): write(p, {'test':2})


if __name__ == '__main__': unittest.main()
