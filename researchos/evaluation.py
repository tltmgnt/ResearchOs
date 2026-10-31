"""Independent evaluation metrics for ResearchOS."""

from dataclasses import dataclass
from enum import Enum
from typing import Iterable
import hashlib
import json


class Outcome(str, Enum):
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"
    UNCERTAIN = "UNCERTAIN"


@dataclass(frozen=True)
class EvaluationCase:
    identifier: str
    expected: Outcome
    observed: Outcome


@dataclass(frozen=True)
class EvaluationReport:
    total: int
    correct: int
    false_acceptances: int
    false_rejections: int
    uncertain: int
    accuracy: float
    false_acceptance_rate: float
    false_rejection_rate: float
    uncertainty_rate: float
    fingerprint: str


def evaluate(cases: Iterable[EvaluationCase]) -> EvaluationReport:
    cases = list(cases)

    identifiers = [case.identifier for case in cases]

    if len(identifiers) != len(set(identifiers)):
        raise ValueError("Duplicate evaluation identifiers")

    if any(not identifier.strip() for identifier in identifiers):
        raise ValueError("Empty evaluation identifier")

    for case in cases:
        if not isinstance(case.expected, Outcome):
            raise TypeError("Expected outcome must be Outcome")
        if not isinstance(case.observed, Outcome):
            raise TypeError("Observed outcome must be Outcome")

    total = len(cases)

    correct = sum(
        case.expected == case.observed
        for case in cases
    )

    false_acceptances = sum(
        case.expected == Outcome.REJECT
        and case.observed == Outcome.ACCEPT
        for case in cases
    )

    false_rejections = sum(
        case.expected == Outcome.ACCEPT
        and case.observed == Outcome.REJECT
        for case in cases
    )

    uncertain = sum(
        case.observed == Outcome.UNCERTAIN
        for case in cases
    )

    expected_rejections = sum(
        case.expected == Outcome.REJECT
        for case in cases
    )

    expected_acceptances = sum(
        case.expected == Outcome.ACCEPT
        for case in cases
    )

    def rate(numerator, denominator):
        return numerator / denominator if denominator else 0.0

    canonical = [
        {
            "identifier": case.identifier,
            "expected": case.expected.value,
            "observed": case.observed.value,
        }
        for case in sorted(cases, key=lambda c: c.identifier)
    ]

    payload = json.dumps(
        canonical,
        sort_keys=True,
        separators=(",", ":"),
    )

    fingerprint = hashlib.sha256(
        payload.encode("utf-8")
    ).hexdigest()

    return EvaluationReport(
        total=total,
        correct=correct,
        false_acceptances=false_acceptances,
        false_rejections=false_rejections,
        uncertain=uncertain,
        accuracy=rate(correct, total),
        false_acceptance_rate=rate(
            false_acceptances,
            expected_rejections,
        ),
        false_rejection_rate=rate(
            false_rejections,
            expected_acceptances,
        ),
        uncertainty_rate=rate(uncertain, total),
        fingerprint=fingerprint,
    )
