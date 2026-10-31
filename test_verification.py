from researchos.core import Claim, Evidence
from researchos.verification import (
    verify_evidence,
    verify_independent_origins,
)

def test_unsupported_claim_rejected():
    claim = Claim("test1", "AI-generated claim")
    assert verify_evidence(claim) is False


def test_verified_evidence_accepted():
    claim = Claim("test2", "Test claim")
    claim.evidence.append(
        Evidence("e1", "reviewer", True, True)
    )
    assert verify_evidence(claim) is True


def test_unverified_evidence_rejected():
    claim = Claim("test3", "Test claim")
    claim.evidence.append(
        Evidence("e2", "reviewer", True, False)
    )
    assert verify_evidence(claim) is False
def test_non_supporting_evidence_rejected():
    claim = Claim("test4", "Test claim")
    claim.evidence.append(
        Evidence("e3", "reviewer", False, True)
    )
    assert verify_evidence(claim) is False
def test_verified_contradiction_blocks_verification():
    claim = Claim("test5", "Contradictory claim")

    claim.evidence.append(
        Evidence("support", "source_a", True, True)
    )

    claim.evidence.append(
        Evidence("contradiction", "source_b", False, True)
    )

    assert verify_evidence(claim) is False

def test_distinct_verified_origins_accepted():
    claim = Claim("test6", "Distinct origins")

    claim.evidence.append(
        Evidence("e1", "source_a", True, True, "origin_a")
    )
    claim.evidence.append(
        Evidence("e2", "source_b", True, True, "origin_b")
    )

    assert verify_independent_origins(claim) is True


def test_duplicate_origins_rejected():
    claim = Claim("test7", "Duplicate origins")

    claim.evidence.append(
        Evidence("e1", "source_a", True, True, "origin_a")
    )
    claim.evidence.append(
        Evidence("e2", "source_b", True, True, "origin_a")
    )

    assert verify_independent_origins(claim) is False


def test_missing_origins_rejected():
    claim = Claim("test8", "Missing origins")

    claim.evidence.append(
        Evidence("e1", "source_a", True, True)
    )
    claim.evidence.append(
        Evidence("e2", "source_b", True, True)
    )

    assert verify_independent_origins(claim) is False


def test_verified_contradiction_rejected():
    claim = Claim("test9", "Contradictory evidence")

    claim.evidence.append(
        Evidence("e1", "source_a", True, True, "origin_a")
    )
    claim.evidence.append(
        Evidence("e2", "source_b", True, True, "origin_b")
    )
    claim.evidence.append(
        Evidence("e3", "source_c", False, True, "origin_c")
    )

    assert verify_independent_origins(claim) is False


def test_single_verified_origin_rejected():
    claim = Claim("test10", "Single origin")

    claim.evidence.append(
        Evidence("e1", "source_a", True, True, "origin_a")
    )

    assert verify_independent_origins(claim) is False
def test_whitespace_does_not_create_independent_origin():
    from researchos.core import Claim, Evidence
    from researchos.verification import verify_independent_origins

    claim = Claim(
        identifier="M5-001",
        statement="Test evidence provenance"
    )

    claim.evidence = [
        Evidence(
            identifier="E1",
            source="Source A",
            supports=True,
            independently_verified=True,
            origin_id="source-A"
        ),
        Evidence(
            identifier="E2",
            source="Source A duplicate",
            supports=True,
            independently_verified=True,
            origin_id=" source-A "
        )
    ]

    assert verify_independent_origins(claim) is False

 def test_duplicate_evidence_identifier_across_claims():
    import pytest
    from researchos.core import Claim, Evidence, EpistemicController

    controller = EpistemicController()

    first = Claim(identifier="claim-1", statement="First claim")
    second = Claim(identifier="claim-2", statement="Second claim")

    controller.register(first)
    controller.register(second)

    controller.add_evidence(
        "claim-1",
        Evidence("shared-evidence", "source-a", True, True)
    )

    with pytest.raises(ValueError, match="duplicate evidence identifier"):
        controller.add_evidence(
            "claim-2",
            Evidence("shared-evidence", "source-b", True, True)
        )
