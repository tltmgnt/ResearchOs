import tempfile
import unittest
from pathlib import Path
from researchos import EpistemicController, Status
from researchos.mra_x import propose
from researchos.mra_x_policy import example


class NativeMraTests(unittest.TestCase):
    def test_native_candidate_no_promotion(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp) / "mra-x.sqlite"
            record = example()
            decision, claim = propose(record, ledger)
            self.assertEqual(decision["status"], "REVIEW_CANDIDATE")
            controller = EpistemicController()
            controller.register(claim)
            self.assertEqual(controller.claims[claim.identifier].status, Status.UNVERIFIED)
            self.assertEqual(claim.evidence, [])
            with self.assertRaises(ValueError):
                controller.transition(claim.identifier, Status.SUPPORTED)
            decision, claim = propose(record, ledger)
            self.assertEqual(decision["status"], "STOP")
            self.assertIsNone(claim)
