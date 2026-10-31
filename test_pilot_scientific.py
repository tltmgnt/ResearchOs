import unittest

from pilot_scientific import run_pilot


class ScientificPilotTests(unittest.TestCase):

    def test_pilot_results(self):
        report = run_pilot()

        self.assertEqual(report.total, 4)
        self.assertEqual(report.correct, 4)
        self.assertEqual(report.accuracy, 1.0)

        self.assertEqual(report.false_acceptances, 0)
        self.assertEqual(report.false_rejections, 0)
        self.assertEqual(report.uncertain, 2)

        self.assertEqual(report.false_acceptance_rate, 0.0)
        self.assertEqual(report.false_rejection_rate, 0.0)
        self.assertEqual(report.uncertainty_rate, 0.5)

    def test_pilot_reproducibility(self):
        first = run_pilot()
        second = run_pilot()

        self.assertEqual(
            first.fingerprint,
            second.fingerprint,
        )


if __name__ == "__main__":
    unittest.main()
