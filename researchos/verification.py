from .core import Claim


def verify_evidence(claim: Claim) -> bool:
    """Verify support without ignoring verified contradictions."""

    verified_support = any(
        evidence.supports and evidence.independently_verified
        for evidence in claim.evidence
    )

    verified_contradiction = any(
        not evidence.supports and evidence.independently_verified
        for evidence in claim.evidence
    )

    return verified_support and not verified_contradiction
def test_verified_contradiction_blocks_verification():
    claim = Claim("test5", "Contradictory claim")

    claim.evidence.append(
        Evidence("support", "source_a", True, True)
    )

    claim.evidence.append(
        Evidence("contradiction", "source_b", False, True)
    )

    assert verify_evidence(claim) is False
