import copy
import json
from pathlib import Path
import tempfile
import unittest
from tect_interop.contracts import dependency, lineage, check_snapshot
from tect_interop.store import EventStore
from tect_interop.evaluation import CONDITIONS, score


class InteropTests(unittest.TestCase):
    def test_direction_roundtrip(self):
        edge = {'source': 'conclusion', 'target': 'evidence', 'relation': 'depends_on'}
        converted = dependency(edge, 'truthai', 'tect')
        self.assertEqual(converted['source'], 'evidence')
        self.assertEqual(dependency(converted, 'tect', 'truthai'), edge)
        with self.assertRaises(ValueError):
            dependency(dict(edge, relation='supports'), 'tect', 'truthai')

    def test_correlated_evidence(self):
        result = lineage({'origin': [], 'copy1': ['origin'], 'copy2': ['origin'], 'other': []})
        self.assertIn(['copy1', 'copy2'], result['shared_ancestry_pairs'])
        self.assertFalse(result['statistical_independence_established'])
        for bad in ({'a': ['missing']}, {'a': ['b'], 'b': ['a']}):
            with self.assertRaises(ValueError): lineage(bad)

    def test_vendored_conformance(self):
        root = Path(__file__).resolve().parents[1]
        manifest = json.loads((root/'core_release.json').read_text())
        self.assertTrue(check_snapshot(root/'tect_runtime', manifest)['conforms'])
        with tempfile.TemporaryDirectory() as tmp:
            self.assertFalse(check_snapshot(tmp, manifest)['conforms'])

    def test_restart_concurrency_and_corruption(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'events.db'
            a = EventStore(path); b = EventStore(path)
            a.append({'claim': 'x', 'state': 'SUPPORTED'}, 0)
            with self.assertRaises(ValueError): b.append({'claim': 'bad'}, 0)
            a.close()
            self.assertEqual(b.read(), [{'claim': 'x', 'state': 'SUPPORTED'}])
            b.append({'claim': 'x', 'state': 'CONTESTED', 'reason': 'changed input'}, 1)
            b.close(); c = EventStore(path)
            self.assertEqual(c.read()[-1]['state'], 'CONTESTED')
            c.connection.execute("UPDATE events SET body='{}' WHERE revision=1")
            with self.assertRaises(ValueError): c.read()
            c.close()

    def test_matched_study_and_denominators(self):
        rows = [{'task': 't1', 'condition': condition, 'correct': True, 'accepted': False,
                 'seconds': 0, 'reviewer_seconds': 0} for condition in CONDITIONS]
        result = score(rows)
        self.assertIsNone(result['metrics']['tect']['false_acceptance_rate'])
        self.assertIsNone(result['metrics']['tect']['validated_results_per_hour'])
        with self.assertRaises(ValueError): score(rows[:-1])
        with self.assertRaises(ValueError): score(rows+rows[:1])
        changed = copy.deepcopy(rows); changed[0]['seconds'] = float('nan')
        with self.assertRaises(ValueError): score(changed)
        changed = copy.deepcopy(rows); changed[-1].update(accepted=True, correct=False, seconds=60)
        self.assertEqual(score(changed)['metrics']['tect']['false_acceptance_rate'], 1)
