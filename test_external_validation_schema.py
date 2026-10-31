import unittest

from external_validation_schema import (
    EvidenceSource,
    ExternalValidationCase,
    ReferenceLabel,
    ReviewerAssessment,
    validate_dataset,
)


def make_case(
    claim_id="SCI-001",
    evidence=None,
    reviewers=None,
    notes="",
):
    if evidence is None:
        evidence = (
            EvidenceSource("E-001", "Source A", "origin-A"),
        )

    if reviewers is None:
        reviewers = (
            ReviewerAssessment(
                "reviewer-1",
                ReferenceLabel.ACCEPT,
                "Evidence supports the claim",
            ),
            ReviewerAssessment(
                "reviewer-2",
                ReferenceLabel.ACCEPT,
                "Independent assessment supports the claim",
            ),
        )

    return ExternalValidationCase(
        claim_id=claim_id,
        domain="Scientific research",
        claim_text="A testable scientific claim",
        evidence_sources=evidence,
        reviewer_assessments=reviewers,
        final_reference_label=ReferenceLabel.ACCEPT,
        adjudication_notes=notes,
    )


class ExternalValidationSchemaTests(unittest.TestCase):

    def test_valid_dataset(self):
        cases = validate_dataset([make_case()])
        self.assertEqual(len(cases), 1)

    def test_duplicate_claims_rejected(self):
        with self.assertRaises(ValueError):
            validate_dataset([
                make_case(),
                make_case(),
            ])

    def test_missing_evidence_rejected(self):
        with self.assertRaises(ValueError):
            validate_dataset([
                make_case(evidence=()),
            ])

    def test_insufficient_reviewers_rejected(self):
        reviewers = (
            ReviewerAssessment(
                "reviewer-1",
                ReferenceLabel.ACCEPT,
                "Supporting evidence",
            ),
        )

        with self.assertRaises(ValueError):
            validate_dataset([
                make_case(reviewers=reviewers),
            ])

    def test_disagreement_requires_notes(self):
        reviewers = (
            ReviewerAssessment(
                "reviewer-1",
                ReferenceLabel.ACCEPT,
                "Supporting evidence",
            ),
            ReviewerAssessment(
                "reviewer-2",
                ReferenceLabel.REJECT,
                "Contradictory evidence",
            ),
        )

        with self.assertRaises(ValueError):
            validate_dataset([
                make_case(reviewers=reviewers),
            ])

    def test_documented_disagreement_allowed(self):
        reviewers = (
            ReviewerAssessment(
                "reviewer-1",
                ReferenceLabel.ACCEPT,
                "Supporting evidence",
            ),
            ReviewerAssessment(
                "reviewer-2",
                ReferenceLabel.REJECT,
                "Contradictory evidence",
            ),
        )

        cases = validate_dataset([
            make_case(
                reviewers=reviewers,
                notes="Adjudication reviewed conflicting evidence",
            ),
        ])

        self.assertEqual(len(cases), 1)

    def test_invalid_reference_label_rejected(self):
        case = make_case()

        invalid_case = ExternalValidationCase(
            claim_id=case.claim_id,
            domain=case.domain,
            claim_text=case.claim_text,
            evidence_sources=case.evidence_sources,
            reviewer_assessments=case.reviewer_assessments,
            final_reference_label="INVALID",
        )

        with self.assertRaises(TypeError):
            validate_dataset([invalid_case])


if __name__ == "__main__":
    unittest.main()
