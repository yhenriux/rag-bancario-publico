import json
import re
import unittest
from pathlib import Path
from hashlib import sha256


class DocumentationChecks(unittest.TestCase):
    def test_local_document_links_exist(self):
        root=Path(__file__).resolve().parents[1]
        for page in [root/'README.md',root/'CONTRIBUTING.md',*root.glob('docs/*.md')]:
            for link in re.findall(r'\]\(([^)]+)\)',page.read_text(encoding='utf-8')):
                if '://' in link or link.startswith('#'):continue
                path=link.split('#')[0]
                self.assertTrue((page.parent/path).exists(),f'{page.name}: {link}')

    def test_protocol_integrity(self):
        root=Path(__file__).resolve().parents[1]
        data=(root/'docs/protocolo.md').read_bytes()
        cut=data.rfind('\n## Verificação de integridade desta minuta'.encode())
        expected=re.search(rb'`([a-f0-9]{64})`\.\n$',data).group(1).decode()
        self.assertEqual(sha256(data[:cut]).hexdigest(),expected)

    def test_example_json_files_parse(self):
        root=Path(__file__).resolve().parents[1]
        for path in [*root.glob('examples/*.json'),*root.glob('configs/*.json')]:json.loads(path.read_text())
        for path in root.glob('examples/*.jsonl'):
            for line in path.read_text().splitlines():
                if line.strip():json.loads(line)


if __name__=='__main__':unittest.main()
