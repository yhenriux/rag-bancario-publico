import tempfile
import unittest
from gguf import execute


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
