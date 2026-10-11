import tempfile
import json
import hashlib
from pathlib import Path
import unittest
from gguf import execute,check_final
from study import digest


class Resume(unittest.TestCase):
    def test_resume_and_changed_prompt(self):
        calls=[]
        def call(payload):
            calls.append(payload)
            return {'content':'R$ 120,00 [F001]', 'tokens_predicted':8}
        with tempfile.TemporaryDirectory() as d:
            inputs=[{'id':'f-1','prompt':'fonte F001'}]
            execute(inputs,'http://127.0.0.1:18771',d,call)
            execute(inputs,'http://127.0.0.1:18771',d,call)
            self.assertEqual(len(calls),1)
            with self.assertRaises(ValueError):
                execute([{'id':'f-1','prompt':'outra fonte'}],'http://127.0.0.1:18771',d,call)
            with self.assertRaises(ValueError):
                execute(inputs,'http://127.0.0.1:18771',d,call,identity={'model_sha256':'outra-versao'})

    def test_failure_is_not_adequacy_zero(self):
        with tempfile.TemporaryDirectory() as d:
            def fail(payload): raise TimeoutError('indisponível')
            rows=execute([{'id':'f','prompt':'p'}],'http://127.0.0.1:18771',d,fail)
            self.assertEqual(rows[0]['status'],'failed')
            self.assertIsNone(rows[0]['answer'])
            self.assertEqual(len(rows[0]['errors']),2)

    def test_final_requires_matching_controls_and_new_families(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);checks={}
            data={'fidelity':{'passed':True},'pilot':{'completed':True,'technical_summary':[{'failed':0,'degenerate':0}]},'sources':{'banks':['inter','bradesco']}}
            for name,value in data.items():
                p=root/(name+'.json');p.write_text(json.dumps(value))
                checks[name]={'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
            inputs=[{'phase':'final','family':'new','id':'F1','prompt':'p'}]
            gate={'method':'assisted_exploratory_final','human_validated':False,
                'public_registration_url':'https://github.com/yhenriux/rag-bancario-publico/commit/'+'a'*40,
                'pilot_families':['old'],'inputs_sha256':digest(json.dumps(inputs,sort_keys=True)),'checks':checks}
            path=root/'gate.json';path.write_text(json.dumps(gate))
            check_final(inputs,path)
            checks_file=root/'pilot.json';checks_file.write_text('{}')
            with self.assertRaises(ValueError):check_final(inputs,path)
            checks_file.write_text(json.dumps(data['pilot']))
            inputs[0]['family']='old'
            with self.assertRaises(ValueError):check_final(inputs,path)
