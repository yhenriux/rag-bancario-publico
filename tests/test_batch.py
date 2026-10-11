import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from batch import catalog, preflight, run_batch
from collect import RobotsRules
from study import write, write_records


class BatchChecks(unittest.TestCase):
    def test_robots_wildcards_comments_specificity_and_groups(self):
        robots = RobotsRules('User-agent: *\nAllow: / # público\nDisallow: /*.pdf$\nDisallow: /docs/\nAllow: /docs/open\nUser-agent: Special\nAllow: /\nCrawl-delay: 10\n')
        agent = 'RAGBankingStudy/0.3'
        self.assertFalse(robots.can_fetch(agent, 'https://bank.example/file.pdf'))
        self.assertTrue(robots.can_fetch(agent, 'https://bank.example/file.pdf?download=1'))
        self.assertFalse(robots.can_fetch(agent, 'https://bank.example/docs/secret'))
        self.assertTrue(robots.can_fetch(agent, 'https://bank.example/docs/open'))
        self.assertTrue(robots.can_fetch('Special/1', 'https://bank.example/file.pdf'))
        self.assertEqual(robots.crawl_delay(agent), 0)
        self.assertEqual(robots.crawl_delay('Special/1'), 10)
        tied = RobotsRules('User-agent: *\nDisallow: /a\nAllow: /a\nUser-agent: *\nDisallow: /b')
        self.assertTrue(tied.can_fetch(agent, 'https://bank.example/a'))
        self.assertFalse(tied.can_fetch(agent, 'https://bank.example/b'))
        self.assertFalse(tied.can_fetch(agent, 'https://bank.example/%62'))

    def test_preflight_does_not_collect_or_approve(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write(root/'sources.json', [{'bank': 'ficticio', 'host': 'bank.example',
                'urls': ['https://bank.example/a.pdf'], 'collection_permission': 'pending'}])
            with patch('batch.fetch', return_value=(b'User-agent: *\nDisallow: /*.pdf$',
                    'https://bank.example/robots.txt', {}, 200)) as fetch:
                result = preflight(root/'sources.json', root/'report.json', 'Study/1')
                self.assertEqual(fetch.call_count, 1)
            self.assertFalse(result[0]['urls'][0]['robots_allowed'])
            self.assertEqual(result[0]['collection_permission'], 'pending')
            self.assertFalse(result[0]['corpus_downloaded'])
            with patch('collect.fetch') as fetch:
                with self.assertRaises(ValueError): run_batch(root/'sources.json', root/'batch', 'Study (research@example.org)')
                fetch.assert_not_called()

    def test_full_batch_extracts_html_and_catalogs_without_human_approval(self):
        body = b'<html><title>Fictional rules</title><main>Conta ficticia. Isencao R$ 1000.</main><script>ignore me</script></html>'
        def fake_fetch(url, *args):
            if url.endswith('robots.txt'): return b'User-agent: *\nAllow: /', url, {}, 200
            return body, url, {'Content-Type': 'text/html'}, 200
        source = {'bank': 'ficticio', 'host': 'bank.example', 'urls': ['https://bank.example/card'],
            'terms_url': 'https://bank.example/terms', 'terms_checked_at': '2026-10-11',
            'collection_permission': 'approved', 'reviewer': 'Fictional test reviewer',
            'permission_evidence': 'Fictional fixture', 'redistribution': 'pending'}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write(root/'sources.json', [source])
            with patch('collect.fetch', side_effect=fake_fetch), patch('collect.time.sleep'):
                result = run_batch(root/'sources.json', root/'batch', 'Study (research@example.org)')
            self.assertEqual(result['documents'], 1)
            self.assertEqual(result['human_validated'], 0)
            doc = json.loads((root/'batch/documents.jsonl').read_text())
            self.assertEqual(doc['title'], 'Fictional rules')
            self.assertNotIn('ignore me', doc['sections'][0]['text'])
            self.assertEqual(doc['extraction_review'], 'pending')
            self.assertEqual(doc['sha256'], hashlib.sha256(body).hexdigest())

    def test_catalog_preserves_literal_offsets_provenance_and_duplicates(self):
        text = 'Cartão fictício. Isenção somente se a fatura atingir R$ 1.000.\nConta fictícia para testes.'
        source = {'document_id': 'd1', 'bank': 'ficticio', 'title': '=NAO_EXECUTAR()',
            'final_url': 'https://bank.example/card', 'collected_at': '2026-10-11',
            'sha256': hashlib.sha256(text.encode()).hexdigest(), 'mime': 'text/html',
            'extraction_review': 'pending', 'sections': [{'location': 'html:body', 'text': text}]}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_records(root/'docs.jsonl', [source, {**source, 'document_id': 'd2'}])
            result = catalog(root/'docs.jsonl', root/'catalog')
            self.assertEqual(result['unique_per_bank'], 1)
            self.assertEqual(result['human_validated'], 0)
            entries = [json.loads(line) for line in (root/'catalog/catalog.jsonl').read_text().splitlines()]
            self.assertEqual(entries[1]['duplicate_of'], 'd1')
            self.assertEqual(entries[0]['product'], 'desconhecido')
            self.assertEqual(entries[0]['topic_candidates'], ['cartao', 'conta'])
            for line in (root/'catalog/critical-passages.jsonl').read_text().splitlines():
                passage = json.loads(line)
                self.assertEqual(passage['text'], text[passage['char_start']:passage['char_end']])
            self.assertIn("'=NAO_EXECUTAR()", (root/'catalog/catalog.csv').read_text(encoding='utf-8-sig'))


if __name__ == '__main__': unittest.main()
