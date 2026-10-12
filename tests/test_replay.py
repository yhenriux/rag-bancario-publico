"""A reprodução precisa rejeitar dados publicados adulterados."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from replay_results import replay


class ReplayChecks(unittest.TestCase):
    def test_public_results_reproduce(self):
        root=Path(__file__).resolve().parents[1]
        self.assertTrue(all(r['metrics_match'] and r['bootstrap_match'] for r in replay(root)))

    def test_tampered_reference_map_is_rejected(self):
        root=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            dest=Path(tmp)
            for folder in ('configs/execution-20261012','docs/results-20261012'):
                shutil.copytree(root/folder,dest/folder)
            path=dest/'configs/execution-20261012/unit-map.json'
            values=json.loads(path.read_text())
            for key in values:values[key]=[]
            path.write_text(json.dumps(values))
            with self.assertRaisesRegex(ValueError,'Métricas documentais divergem'):
                replay(dest)


if __name__=='__main__':unittest.main()
