"""ResearchOS v0.6 — External validation dataset schema."""

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Tuple


class ReferenceLabel(str, Enum):
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"
    UNCERTAIN = "UNCERTAIN"


@dataclass(frozen=True)
class EvidenceSource:
    identifier: str
    citation: str
    origin_id: str


@dataclass(frozen=True)
class ReviewerAssessment:
    reviewer_id: str
    label: ReferenceLabel
    rationale: str


@dataclass(frozen=True)
class ExternalValidationCase:
    claim_id: str
    domain: str
    claim_text: str
    evidence_sources: Tuple[EvidenceSource, ...]
    reviewer_assessments: Tuple[ReviewerAssessment, ...]
    final_reference_label: ReferenceLabel
    adjudication_notes: str = ""


def validate_dataset(
    cases: Iterable[ExternalValidationCase],
) -> Tuple[ExternalValidationCase, ...]:
    """Validate cases without modifying the original dataset."""

    cases = tuple(cases)
    seen_claims = set()

    for case in cases:
        if not isinstance(case, ExternalValidationCase):
            raise TypeError("Invalid evaluation case")

        if not case.claim_id.strip():
            raise ValueError("Claim ID cannot be empty")

        if case.claim_id in seen_claims:
            raise ValueError(
                f"Duplicate claim ID: {case.claim_id}"
            )

        seen_claims.add(case.claim_id)

        if not case.domain.strip():
            raise ValueError("Scientific domain is required")

        if not case.claim_text.strip():
            raise ValueError("Claim text is required")

        if not isinstance(
            case.final_reference_label,
            ReferenceLabel,
        ):
            raise TypeError("Invalid reference label")

        if not case.evidence_sources:
            raise ValueError(
                f"Evidence sources required: {case.claim_id}"
            )

        source_ids = set()

        for source in case.evidence_sources:
            if not isinstance(source, EvidenceSource):
                raise TypeError("Invalid evidence source")

            if not all((
                source.identifier.strip(),
                source.citation.strip(),
                source.origin_id.strip(),
            )):
                raise ValueError(
                    "Evidence source fields cannot be empty"
                )

            if source.identifier in source_ids:
                raise ValueError("Duplicate evidence source ID")

            source_ids.add(source.identifier)

        if len(case.reviewer_assessments) < 2:
            raise ValueError(
                "At least two reviewer assessments required"
            )

        reviewer_ids = set()
        reviewer_labels = set()

        for assessment in case.reviewer_assessments:
            if not isinstance(
                assessment,
                ReviewerAssessment,
            ):
                raise TypeError("Invalid reviewer assessment")

            if not assessment.reviewer_id.strip():
                raise ValueError("Reviewer ID required")

            if not assessment.rationale.strip():
                raise ValueError("Reviewer rationale required")

            if not isinstance(
                assessment.label,
                ReferenceLabel,
            ):
                raise TypeError("Invalid reviewer label")

            if assessment.reviewer_id in reviewer_ids:
                raise ValueError("Duplicate reviewer ID")

            reviewer_ids.add(assessment.reviewer_id)
            reviewer_labels.add(assessment.label)

        if len(reviewer_labels) > 1:
            if not case.adjudication_notes.strip():
                raise ValueError(
                    "Reviewer disagreement requires "
                    "adjudication notes"
                )

    return cases
