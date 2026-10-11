import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from collect import extract
from experiment import segment
from study import write_records, records
from technical import generate


class ExecutionChecks(unittest.TestCase):
    def snapshot(self, root, bodies):
        entries = []
        for i, body in enumerate(bodies):
            name = str(i) + '.html'
            (root / name).write_bytes(body)
            entries.append({'document_id':str(i), 'url':'https://bank.example/'+name,
                'raw_path':name, 'sha256':hashlib.sha256(body).hexdigest(), 'mime':'text/html'})
        write_records(root/'manifest.jsonl', entries)

    def test_empty_main_fallback_and_partial_extraction(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.snapshot(root, [b'<body><main></main><article>Value 6.40 and condition.</article></body>', b'<html></html>'])
            extract(root, root/'out.jsonl', allow_partial=True)
            self.assertIn('6.40', records(root/'out.jsonl')[0]['sections'][0]['text'])
            self.assertEqual(len(records(root/'out.jsonl.errors.jsonl')), 1)

    def test_partial_extraction_never_accepts_tampered_snapshot(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.snapshot(root, [b'<main>Original</main>'])
            (root/'0.html').write_text('Changed')
            with self.assertRaisesRegex(ValueError, 'alterado'):
                extract(root, root/'out.jsonl', allow_partial=True)

    def test_assisted_segmentation_requires_explicit_flag_and_record(self):
        config = {'e5_revision':'a'*40, 'qwen_revision':'b'*40}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            doc = {'extraction_review':'assisted_checked', 'review_origin':'Codex', 'sections':[]}
            write_records(root/'input.jsonl', [doc])
            with patch('experiment.tokenizer'):
                with self.assertRaises(ValueError): segment(root/'input.jsonl', config, root/'out.jsonl')
                with self.assertRaises(ValueError): segment(root/'input.jsonl', config, root/'out.jsonl', True)
                doc['review_record'] = 'decision.json'
                write_records(root/'registered.jsonl', [doc])
                segment(root/'registered.jsonl', config, root/'out.jsonl', True)
                self.assertEqual(records(root/'out.jsonl'), [])

    def test_generation_checkpoints_and_repeat_do_not_overwrite(self):
        import io
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_records(root/'prompts.jsonl', [{'config':'A', 'prompt':'test', 'prompt_sha256':'abc'}])
            with patch('technical.urllib.request.urlopen', side_effect=lambda *a, **k: io.BytesIO(b'{"content":"same"}')):
                generate(root/'prompts.jsonl', 'http://127.0.0.1:18771', root/'answers.jsonl')
            self.assertEqual(len(records(root/'answers.jsonl')), 2)
            self.assertTrue(json.loads((root/'answers.jsonl.summary.json').read_text())['repeat_identical'])
            with self.assertRaises(ValueError): generate(root/'prompts.jsonl', 'http://127.0.0.1:18771', root/'answers.jsonl')
            with self.assertRaises(ValueError): generate(root/'prompts.jsonl', 'http://127.0.0.1:18771@external.example', root/'other.jsonl')


if __name__ == '__main__': unittest.main()
