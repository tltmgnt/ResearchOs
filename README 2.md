# ResearchOS — Topological Epistemic Control Theory (TECT)

**Status: research prototype / pre-alpha. Not certified for high-stakes use.**

ResearchOS explores an auditable control layer between AI-generated claims and accepted knowledge. TECT represents claims, evidence, dependencies, provenance, challenges, and governance as a versioned epistemic state. The initial prototype demonstrates a small, deterministic state-transition controller; it does **not** establish truth or prove the full TECT theory.

> **AI generation ≠ knowledge acceptance.**

## What works in v0.1

- Register claims and supporting/contradictory evidence.
- Enforce a limited claim state machine.
- Block unsupported promotions and require independently verified evidence for validation.
- Mark challenged claims and their dependents as contested.
- Record a simple in-memory audit log.

**Not yet implemented:** real theorem proving, automated adversarial agents, persistent graph storage, cryptographic provenance, source-independence estimation, governance policy engine, assurance scoring, benchmark comparisons, or production security.

## Quick start

Requires Python 3.10+; no runtime dependencies.

```bash
python -m pip install -e .
python examples/demo.py
python -m unittest discover -s tests -v
```

Expected demonstration: the false claim “Every prime number is odd” becomes `CONTESTED` after receiving the counterexample 2.

## Architecture

`Generator → Claim Registry → Evidence/Dependency Graph → Validation/Challenge → TECT Controller → Audit Record`

The current prototype implements only the registry, simplified evidence/dependency handling, controller, and in-memory audit record.

## Research agenda

1. Specify TECT state semantics and mathematically sound transition invariants.
2. Add external proof checking and independent reproduction adapters.
3. Build a labeled benchmark with correct, incorrect, and incomplete proofs.
4. Compare single-model, multi-agent, and TECT-controlled verification under matched budgets.
5. Measure false acceptance, false rejection, cost, and audit reconstruction time.
6. Run ablations on dependency tracking, adversarial testing, and transition guards.

See [research specification](docs/TECT_SPEC.md), [evaluation plan](docs/EVALUATION.md), and [roadmap](docs/ROADMAP.md).

## Important limitations

Evidence marked `independently_verified=True` is a **caller-provided assertion**, not proof of actual independent verification. The prototype is vulnerable to untrusted input and must not be used for scientific, safety, or operational certification. TECT stability is not equivalent to truth.

## Licensing and intellectual property

**No open-source license has been granted yet.** All rights reserved pending an explicit licensing decision. Do not publish proprietary details, confidential data, patent-sensitive disclosures, or government-restricted information without appropriate review.

## Contributions

See [CONTRIBUTING.md](CONTRIBUTING.md). External contributions are not currently accepted pending licensing decisions.
