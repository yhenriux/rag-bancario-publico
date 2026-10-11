import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from collect import collect,RedirectPolicy
from study import write


class CollectionChecks(unittest.TestCase):
    def source(self):
        return {'bank':'ficticio','host':'bank.example','urls':['https://bank.example/card'],
                'terms_url':'https://bank.example/terms','terms_checked_at':'2026-10-11',
                'collection_permission':'approved','reviewer':'Pessoa fictícia',
                'permission_evidence':'Revisão fictícia para testar código','redistribution':'pending'}

    def test_permissions_and_robots_are_checked_before_documents(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);write(root/'sources.json',[{**self.source(),'collection_permission':'pending'}])
            with patch('collect.fetch') as fetch:
                with self.assertRaises(ValueError):collect(root/'sources.json',root/'blocked','Study (research@example.org)')
                fetch.assert_not_called()
            write(root/'approved.json',[self.source()])
            with patch('collect.fetch',return_value=(b'User-agent: *\nDisallow: /', 'https://bank.example/robots.txt',{},200)) as fetch:
                with self.assertRaises(SystemExit):collect(root/'approved.json',root/'robots-blocked','Study (research@example.org)')
                self.assertEqual(fetch.call_count,1)
                self.assertTrue((root/'robots-blocked'/'errors.jsonl').read_text().strip())

    def test_snapshot_records_raw_hash_and_url(self):
        body=b'<html><main>Fictional card rule.</main></html>'
        def fake_fetch(url,*args):
            if url.endswith('robots.txt'):return b'User-agent: *\nAllow: /',url,{},200
            return body,url,{'Content-Type':'text/html'},200
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);write(root/'sources.json',[self.source()])
            with patch('collect.fetch',side_effect=fake_fetch),patch('collect.time.sleep'):
                collect(root/'sources.json',root/'snapshot','Study (research@example.org)')
            entry=json.loads((root/'snapshot'/'manifest.jsonl').read_text())
            self.assertEqual(entry['sha256'],hashlib.sha256(body).hexdigest())
            self.assertEqual((root/'snapshot'/entry['raw_path']).read_bytes(),body)
            self.assertEqual(entry['final_url'],'https://bank.example/card')

    def test_redirect_cannot_leave_approved_domain(self):
        with self.assertRaises(ValueError):
            RedirectPolicy('bank.example').redirect_request(None,None,302,'',{},'https://other.example/doc')


if __name__=='__main__':unittest.main()
