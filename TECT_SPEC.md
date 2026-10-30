# TECT formal specification — research draft

## Epistemic state

\(\mathcal{E}_t=(K_t,R_t,E_t,S_t,P_t,\Gamma_t)\): artifacts, dependencies, evidence, claim states, provenance, and governance constraints.

Proposed transition: \(\mathcal{E}_{t+1}=G(\mathcal{E}_t,T,\Gamma,A,V)\).

A transition to a stronger assurance state must meet explicit, versioned predicates. Evidence may be correlated; numerical confidence does not establish correctness. Challenges can demote claims and invalidate dependent conclusions.

## Research hypotheses, not established results

- Epistemic potential: \(\Phi=\alpha U+\beta C+\gamma P+\delta G+\eta A\).
- Stability must be defined relative to a metric and bounded attack class.
- Strict descent on a **finite** state space implies finite termination; compactness and strict descent alone do **not** imply finite termination in continuous spaces.
- A margin-based resilience theorem requires a stated bound linking perturbation distance to changes in validation score (e.g., Lipschitz continuity).
- Governance preservation is an invariant only if the transition relation explicitly enforces it.

## Prototype semantics

States: GENERATED, UNVERIFIED, SUPPORTED, CONTESTED, VALIDATED, ASSURED. This is a deliberately reduced subset of the proposed full state machine. Independent verification is currently represented by an untrusted Boolean supplied by the caller. No claim of formal correctness is made.
