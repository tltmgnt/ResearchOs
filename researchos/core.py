"""Minimal deterministic TECT-inspired claim assurance controller.

Demonstration software, not a mathematical truth oracle.
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List

class Status(str, Enum):
    GENERATED = 'GENERATED'
    UNVERIFIED = 'UNVERIFIED'
    SUPPORTED = 'SUPPORTED'
    CONTESTED = 'CONTESTED'
    VALIDATED = 'VALIDATED'
    ASSURED = 'ASSURED'

@dataclass
class Evidence:
    identifier: str
    source: str
    supports: bool
    independently_verified: bool = False
    origin_id: str = ""

@dataclass
class Claim:
    identifier: str
    statement: str
    status: Status = Status.GENERATED
    dependencies: List[str] = field(default_factory=list)
    evidence: List[Evidence] = field(default_factory=list)

class EpistemicController:
    def __init__(self):
        self.claims: Dict[str, Claim] = {}
        self.audit: List[dict] = []

    def register(self, claim: Claim):
        if claim.identifier in self.claims:
            raise ValueError('duplicate claim identifier')

        for dependency_id in claim.dependencies:
            if dependency_id not in self.claims:
                raise ValueError(
                    f'unknown dependency: {dependency_id}'
                )

        self.claims[claim.identifier] = claim
        self.audit.append({
            'claim': claim.identifier,
            'event': 'registered'
        })

    def add_evidence(self, claim_id: str, evidence: Evidence):
        claim = self.claims[claim_id]
        if any(e.identifier == evidence.identifier for e in claim.evidence):
            raise ValueError('duplicate evidence identifier')
        claim.evidence.append(evidence)
        self.audit.append({'claim': claim_id, 'event': 'evidence_added', 'evidence': evidence.identifier})
        if not evidence.supports:
            self._contest_with_dependents(claim_id)

    def _contest_with_dependents(self, claim_id: str):
        queue = [claim_id]
        visited = set()
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            claim = self.claims[current]
            old = claim.status
            claim.status = Status.CONTESTED
            self.audit.append({'claim': current, 'event': 'contested', 'previous': old.value})
            queue.extend(c.identifier for c in self.claims.values() if current in c.dependencies)
    def _has_dependency_cycle(self, claim_id: str) -> bool:
        visiting = set()
        visited = set()

        def visit(current_id: str) -> bool:
            if current_id in visiting:
                return True

            if current_id in visited:
                return False

            visiting.add(current_id)

            for dependency_id in self.claims[current_id].dependencies:
                if visit(dependency_id):
                    return True

            visiting.remove(current_id)
            visited.add(current_id)
            return False

        return visit(claim_id)


    def transition(self, claim_id: str, target: Status):
        claim = self.claims[claim_id]
        allowed = {
            Status.GENERATED: {Status.UNVERIFIED},
            Status.UNVERIFIED: {Status.SUPPORTED},
            Status.SUPPORTED: {Status.VALIDATED},
            Status.VALIDATED: {Status.ASSURED},
            Status.CONTESTED: {Status.UNVERIFIED},
            Status.ASSURED: set(),
        }

                if target not in allowed[claim.status]:
            raise ValueError(
                f'invalid transition: {claim.status.value} -> {target.value}'
            )

        if target in {
            Status.SUPPORTED,
            Status.VALIDATED,
            Status.ASSURED
        }:
            if self._has_dependency_cycle(claim_id):
                raise ValueError('circular dependency detected')

        if target in {Status.SUPPORTED, Status.VALIDATED, Status.ASSURED}:
            if not claim.evidence or any(not e.supports for e in claim.evidence):
                raise ValueError(
                    'supporting evidence required; unresolved challenge blocks promotion'
                )

            if any(
                self.claims[d].status not in {Status.VALIDATED, Status.ASSURED}
                for d in claim.dependencies
            ):
                raise ValueError('unvalidated dependency blocks promotion')

        if target in {Status.VALIDATED, Status.ASSURED}:
            from .verification import verify_evidence

            if not verify_evidence(claim):
                raise ValueError('independent verification required')

        if target == Status.ASSURED:
            from .verification import verify_independent_origins

            if not verify_independent_origins(claim):
                raise ValueError(
                    'two independent verified origins required'
                )
        previous = claim.status
        claim.status = target
        self.audit.append({'claim': claim_id, 'event': 'transition', 'from': previous.value, 'to': target.value})
