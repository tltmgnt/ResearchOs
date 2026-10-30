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
def verify_independent_origins(claim: Claim) -> bool:
    """Require two distinct verified origins and no verified contradictions."""

    verified_contradiction = any(
        not evidence.supports and evidence.independently_verified
        for evidence in claim.evidence
    )

    if verified_contradiction:
        return False

    verified_origins = {
        evidence.origin_id.strip()
        for evidence in claim.evidence
        if (
            evidence.supports
            and evidence.independently_verified
            and evidence.origin_id.strip()
        )
    }

    return len(verified_origins) >= 2
    
