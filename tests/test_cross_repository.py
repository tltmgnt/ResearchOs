"""Executed only when real domain packages are installed, never mocked."""
import importlib.util
import unittest
from tect_interop.demo import run

AVAILABLE=all(importlib.util.find_spec(n) is not None for n in ('spatial_topology','formal_topology','truthai_assurance'))

@unittest.skipUnless(AVAILABLE, 'Install pinned integration packages to exercise this test')
class IntegrationTests(unittest.TestCase):
    def test_actual_calls_and_invalidation(self):
        report=run()
        self.assertEqual(report['before']['spatial']['status'],'REQUIREMENTS_SATISFIED')
        self.assertEqual(report['after']['spatial']['status'],'GAPS_FOUND')
        self.assertEqual(report['before']['formal']['status'],'OBLIGATIONS_HOLD')
        self.assertEqual(report['after']['formal']['status'],'GAPS_FOUND')
        self.assertTrue(report['before']['certificates']['certificates_valid'])
        self.assertTrue(report['after']['certificates']['certificates_valid'])
        self.assertTrue(report['before']['same_predicate_agrees'])
        self.assertTrue(report['after']['same_predicate_agrees'])
        self.assertTrue(report['truthai']['snapshot_changed'])
        self.assertEqual(report['truthai']['status']['status'],'NEEDS_REVIEW')
        self.assertEqual(report['tect']['state']['claims']['conclusion']['state'],'UNVERIFIED')
        self.assertIn('CLAIM_REVISED',report['tect']['state']['claims']['conclusion']['reassessment_reasons'])
        self.assertEqual(report['tect']['transition_outcomes']['FAIL'],0)
        self.assertFalse(report['execution_authorized'])
        self.assertFalse(report['independent_reproduction'])
