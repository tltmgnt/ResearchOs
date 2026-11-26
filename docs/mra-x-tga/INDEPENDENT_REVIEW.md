# MRA-X 2.0 independent validation handoff

Status: **NOT CERTIFIED**. This is a review protocol and bounded software evidence, not independent research validation.

## Reproducible evidence

- Shared policy and SQLite runtime: `python tools/mra_x_tga.py --self-test`, `python tools/mra_x_runtime.py --self-test`.
- Matched synthetic software benchmark: `python tools/mra_x_controlled_benchmark.py --repeats 21`.
- Native ResearchOS bridge: `python -m unittest discover -s tests -p 'test_mra_x_native.py'`.
- Scope-projection lemmas: MathOS PR https://github.com/tltmgnt/MathOS/pull/247 and scoped Lean CI https://github.com/tltmgnt/MathOS/actions/runs/45857988378.
- Read-only HedgeOps native bridge: https://github.com/tltmgnt/Grok-HedgeOps-DTI/pull/101.

Local controlled benchmark: 160 synthetic records, eight categories, 21 repetitions, 160 matching dispositions and retained candidate packets per trial; 1,120 fixed-stage vs 700 gated-stage executions (37.5% reduction). These are actual deterministic software stage counts. The fixture mix is deliberately balanced across rejection categories and is not a representative research distribution. Wall-clock results are environment-dependent. No live provider calls or researcher comparisons took place. The original F038 pilot and general SAT recovery remain unverified.

## Proposed prospective independent trial

Before enrollment, independent investigators should register a fixed protocol, task set, baseline, budgets, acceptance thresholds and analysis plan. The following is a proposed starting design, not an approved study.

1. Select at least 30 held-out, non-sensitive mathematical research tasks with clear proof obligations and a mixture of feasible, obstructed and refuted pathways. Keep test solutions and reviewer judgments out of the development data.
2. Compare conventional research with the same tools and resource ceiling against MRA-X-assisted research; randomize assignment, balance expertise and difficulty, prevent cross-arm leakage, and match access to models, references and formal tools.
3. Record actual human time, calls, tokens, monetary cost, compute, preprocessing, failed attempts, valid negative results and proof-replay outcomes. Never substitute modeled stages for actual resource use.
4. Use at least two independent blinded mathematical reviewers; adjudicate disagreement with a third. Review complete proofs, assumptions, reproducibility, scope and novelty, not just output fluency. Do not treat hash consistency as authenticity.
5. Primary outcome: independently accepted substantive contributions (constructive or negative) per researcher-hour at a fixed cost cap. Secondary outcomes: false exclusions, unsupported acceptance, resource costs, completion rates and inter-reviewer agreement. Require no false theorem promotion in the observed sample and report uncertainty; finite zero counts do not prove universal safety.
6. Analyze paired or blocked outcomes with confidence intervals, disclose exclusions and failed runs, publish deidentified evidence with permission, and stop at the predeclared boundary. Report adverse results regardless of direction.
7. External reviewers must sign a scope-specific attestation tied to exact commits, test artifacts, limitations and declared conflicts. Neither software CI nor the authors can award independent certification to themselves.

Do not run clinical, military, broker or other operational actions as part of this validation. Keep all evidence private unless explicitly approved for publication. Any change to authority, permissions, budget execution or accepted proof status requires the host's existing approval process.

## Acceptance boundary

A passing Lean kernel replay verifies only the enrolled formal statements. Independent statement fidelity, novelty, broad scientific benefit, deployment readiness, real-world safety and external certification remain separate. P versus NP remains open. Architecture target 10/10 is not a performance or certification score.
