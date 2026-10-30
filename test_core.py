import unittest
from researchos import Claim, Evidence, EpistemicController, Status

class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.os = EpistemicController()
        self.os.register(Claim('c1', 'Every prime is odd'))

    def test_unsupported_promotion_blocked(self):
        self.os.transition('c1', Status.UNVERIFIED)
        with self.assertRaises(ValueError):
            self.os.transition('c1', Status.SUPPORTED)

    def test_independent_verification_required(self):
        self.os.transition('c1', Status.UNVERIFIED)
        self.os.add_evidence('c1', Evidence('e1', 'reviewer', True))
        self.os.transition('c1', Status.SUPPORTED)
        with self.assertRaises(ValueError):
            self.os.transition('c1', Status.VALIDATED)

    def test_challenge_propagates_to_dependents(self):
        self.os.register(Claim('c2', 'Derived claim', dependencies=['c1']))
        self.os.add_evidence('c1', Evidence('counterexample', '2 is prime and even', False, True))
        self.assertEqual(self.os.claims['c1'].status, Status.CONTESTED)
        self.assertEqual(self.os.claims['c2'].status, Status.CONTESTED)

    def test_validated_transition(self):
        self.os.transition('c1', Status.UNVERIFIED)
        self.os.add_evidence('c1', Evidence('e1', 'independent checker', True, True))
        self.os.transition('c1', Status.SUPPORTED)
        self.os.transition('c1', Status.VALIDATED)
        self.assertEqual(self.os.claims['c1'].status, Status.VALIDATED)
    def test_unverified_evidence_blocks_validation(self):
        self.os.transition('c1', Status.UNVERIFIED)

        self.os.add_evidence(
            'c1',
            Evidence('e_unverified', 'reviewer', True, False)
        )

        self.os.transition('c1', Status.SUPPORTED)

        with self.assertRaises(ValueError):
            self.os.transition('c1', Status.VALIDATED)

        self.assertEqual(
            self.os.claims['c1'].status,
            Status.SUPPORTED
        )
    def test_single_origin_cannot_be_assured(self):
        self.os.transition('c1', Status.UNVERIFIED)

        self.os.add_evidence(
            'c1',
            Evidence(
                'e1',
                'independent_checker',
                True,
                True,
                'origin_a'
            )
        )

        self.os.transition('c1', Status.SUPPORTED)
        self.os.transition('c1', Status.VALIDATED)

        with self.assertRaises(ValueError):
            self.os.transition('c1', Status.ASSURED)

        self.assertEqual(
            self.os.claims['c1'].status,
            Status.VALIDATED
        )
    def test_missing_dependency_rejected(self):
        invalid_claim = Claim(
            'c_missing',
            'Claim with nonexistent dependency',
            dependencies=['does_not_exist']
        )

        with self.assertRaisesRegex(
            ValueError,
            'unknown dependency'
        ):
            self.os.register(invalid_claim)

        self.assertNotIn(
            'c_missing',
            self.os.claims
        )
if __name__ == '__main__':
    unittest.main()
