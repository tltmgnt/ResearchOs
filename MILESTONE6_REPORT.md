# ResearchOS — Milestone 6 Evaluation Report

## 1. Overview

Milestone 6 introduces an independent evaluation framework
and a synthetic scientific-claims pilot.

The objective is to measure classification behavior,
identify errors, and verify reproducibility.

## 2. Evaluation Framework

Module: researchos/evaluation.py

The framework supports three outcomes:

- ACCEPT
- REJECT
- UNCERTAIN

It measures:

- Accuracy
- False acceptance rate
- False rejection rate
- Uncertainty rate

Evaluation cases contain reference labels that are
separate from observed system decisions.

A SHA-256 fingerprint supports reproducibility checks.

## 3. Scientific Pilot

Module: pilot_scientific.py

Domain: Scientific research claims

Pilot type: Synthetic demonstration

Four predefined cases are evaluated:

| Case | Expected outcome |
|------|------------------|
| SCI-001 | ACCEPT |
| SCI-002 | REJECT |
| SCI-003 | UNCERTAIN |
| SCI-004 | UNCERTAIN |

The pilot exercises the ResearchOS controller using
supporting, contradictory, unverified, and absent evidence.

## 4. Expected Pilot Metrics

For the four synthetic cases:

| Metric | Expected value |
|--------|----------------|
| Total cases | 4 |
| Correct classifications | 4 |
| Accuracy | 100% |
| False acceptances | 0 |
| False rejections | 0 |
| Uncertain outcomes | 2 |
| False acceptance rate | 0% |
| False rejection rate | 0% |
| Uncertainty rate | 50% |

These values describe the predefined synthetic test
scenario, not performance on real scientific research.

## 5. Automated Verification

Tests include:

- Existing controller regression tests
- Independent evaluation tests
- Scientific pilot regression tests
- Reproducibility checks

GitHub Actions was reported passing after the pilot
regression tests were added.

The exact test count should be confirmed from the
final workflow logs before release.

## 6. Evaluation Methodology

False acceptance rate:

False acceptances divided by reference REJECT cases.

False rejection rate:

False rejections divided by reference ACCEPT cases.

Uncertainty rate:

Observed UNCERTAIN outcomes divided by all cases.

Accuracy:

Exact agreement between observed and reference outcomes
divided by all cases.

When a denominator is zero, the current implementation
returns 0.0. This convention should be considered when
interpreting reports.

## 7. Limitations

- The pilot uses synthetic claims.
- Reference labels are predefined, not independently
  established by external scientific experts.
- The sample contains only four cases.
- The results do not establish real-world accuracy.
- No statistical confidence intervals are calculated.
- No external scientific dataset has been evaluated.
- The framework does not independently establish truth.
- The pilot does not demonstrate production readiness.

## 8. Milestone Completion Criteria

- [x] Evaluation framework implemented
- [x] False acceptance and rejection metrics implemented
- [x] Uncertainty metric implemented
- [x] Reproducibility fingerprint implemented
- [x] Synthetic scientific pilot implemented
- [x] Automated pilot tests implemented
- [x] GitHub Actions reported passing
- [ ] Final workflow test count verified
- [ ] Final code review completed
- [ ] Milestone 6 merged into main

## 9. Conclusion

Milestone 6 demonstrates a reproducible evaluation
workflow for a small synthetic scientific-claims pilot.

The next research phase should use independently labeled
real-world cases, larger datasets, and external review.

ResearchOS remains a research prototype.
