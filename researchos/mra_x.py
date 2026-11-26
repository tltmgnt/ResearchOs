"""Explicit MRA-X -> ResearchOS candidate bridge; no status promotion."""
from .core import Claim, Status
from .mra_x_policy import digest
from .mra_x_runtime import submit


def propose(record, ledger):
    """Return a ledger decision and an unverified native Claim or None.

    The caller can register the returned Claim using EpistemicController.
    No evidence is promoted and no native controller is mutated automatically.
    A ledger enrollment is durable even if a later host registration fails.
    """
    decision = submit(ledger, record)
    if decision["status"] != "REVIEW_CANDIDATE":
        return decision, None
    claim = Claim(identifier="mra-x:" + digest(record["claim"]),
                  statement=record["claim"], status=Status.UNVERIFIED)
    return decision, claim
