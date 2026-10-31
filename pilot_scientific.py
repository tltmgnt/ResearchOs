"""ResearchOS Milestone 6: Synthetic scientific-claims pilot."""

from researchos import Claim, Evidence, EpistemicController, Status
from researchos.evaluation import EvaluationCase, Outcome, evaluate


def run_case(identifier, statement, expected, evidence_items):
    controller = EpistemicController()
    controller.register(Claim(identifier, statement))

    controller.transition(identifier, Status.UNVERIFIED)

    for evidence in evidence_items:
        controller.add_evidence(identifier, evidence)

    claim = controller.claims[identifier]

    if claim.status == Status.CONTESTED:
        observed = Outcome.REJECT
    else:
        try:
            controller.transition(identifier, Status.SUPPORTED)
            controller.transition(identifier, Status.VALIDATED)
            observed = Outcome.ACCEPT
        except ValueError:
            observed = Outcome.UNCERTAIN

    return EvaluationCase(identifier, expected, observed)


def run_pilot():
    cases = [
        run_case(
            "SCI-001",
            "A synthetic claim with verified supporting evidence.",
            Outcome.ACCEPT,
            [
                Evidence(
                    "E-001", "Independent reviewer A",
                    True, True, "origin-A"
                )
            ],
        ),
        run_case(
            "SCI-002",
            "A synthetic claim contradicted by verified evidence.",
            Outcome.REJECT,
            [
                Evidence(
                    "E-002", "Independent reviewer B",
                    False, True, "origin-B"
                )
            ],
        ),
        run_case(
            "SCI-003",
            "A synthetic claim with unverified evidence.",
            Outcome.UNCERTAIN,
            [
                Evidence(
                    "E-003", "Unverified source",
                    True, False, "origin-C"
                )
            ],
        ),
        run_case(
            "SCI-004",
            "A synthetic claim without evidence.",
            Outcome.UNCERTAIN,
            [],
        ),
    ]

    report = evaluate(cases)

    for case in cases:
        print(
            f"{case.identifier}: "
            f"expected={case.expected.value}, "
            f"observed={case.observed.value}"
        )

    print(f"Total cases: {report.total}")
    print(f"Accuracy: {report.accuracy:.2%}")
    print(
        f"False acceptance rate: "
        f"{report.false_acceptance_rate:.2%}"
    )
    print(
        f"False rejection rate: "
        f"{report.false_rejection_rate:.2%}"
    )
    print(
        f"Uncertainty rate: "
        f"{report.uncertainty_rate:.2%}"
    )
    print(f"Fingerprint: {report.fingerprint}")

    return report


if __name__ == "__main__":
    run_pilot()
