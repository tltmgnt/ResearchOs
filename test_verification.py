from researchos.core import Claim, Evidence
from researchos.verification import verify_evidence


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
