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
