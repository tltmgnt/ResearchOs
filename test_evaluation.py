import unittest

from researchos.evaluation import (
    EvaluationCase,
    Outcome,
    evaluate,
)


class EvaluationTests(unittest.TestCase):

    def test_correct_decisions(self):
        cases = [
            EvaluationCase("1", Outcome.ACCEPT, Outcome.ACCEPT),
            EvaluationCase("2", Outcome.REJECT, Outcome.REJECT),
        ]

        report = evaluate(cases)

        self.assertEqual(report.total, 2)
        self.assertEqual(report.correct, 2)
        self.assertEqual(report.accuracy, 1.0)

    def test_false_acceptance(self):
        report = evaluate([
            EvaluationCase("1", Outcome.REJECT, Outcome.ACCEPT)
        ])

        self.assertEqual(report.false_acceptances, 1)
        self.assertEqual(report.false_acceptance_rate, 1.0)

    def test_false_rejection(self):
        report = evaluate([
            EvaluationCase("1", Outcome.ACCEPT, Outcome.REJECT)
        ])

        self.assertEqual(report.false_rejections, 1)
        self.assertEqual(report.false_rejection_rate, 1.0)

    def test_uncertainty(self):
        report = evaluate([
            EvaluationCase("1", Outcome.ACCEPT, Outcome.UNCERTAIN)
        ])

        self.assertEqual(report.uncertain, 1)
        self.assertEqual(report.uncertainty_rate, 1.0)

    def test_reproducibility(self):
        cases = [
            EvaluationCase("1", Outcome.ACCEPT, Outcome.ACCEPT),
            EvaluationCase("2", Outcome.REJECT, Outcome.REJECT),
        ]

        first = evaluate(cases)
        second = evaluate(list(reversed(cases)))

        self.assertEqual(
            first.fingerprint,
            second.fingerprint,
        )

    def test_duplicate_identifiers(self):
        cases = [
            EvaluationCase("1", Outcome.ACCEPT, Outcome.ACCEPT),
            EvaluationCase("1", Outcome.REJECT, Outcome.REJECT),
        ]

        with self.assertRaises(ValueError):
            evaluate(cases)


if __name__ == "__main__":
    unittest.main()
