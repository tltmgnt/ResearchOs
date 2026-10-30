from .core import Claim


def verify_evidence(claim: Claim) -> bool:
    """Check for independently verified supporting evidence."""
    return any(
        evidence.supports and evidence.independently_verified
        for evidence in claim.evidence
    )