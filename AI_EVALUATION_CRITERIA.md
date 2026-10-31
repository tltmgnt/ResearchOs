ResearchOS | TECT v0.6

AI Research Evaluation Criteria

Version: 0.1
Status: Draft — Candidate Selection Protocol
Domain: Artificial Intelligence
Development Branch: develop/tect-v0.6-external-validation

⸻

1. Objective

This document establishes objective criteria for selecting artificial intelligence research claims for external evaluation of ResearchOS.

The initial pilot will target 10 real-world AI research claims.

The objective is to evaluate whether ResearchOS classifications agree with independently established reference labels.

Claims must be selected before ResearchOS predictions are generated.

No real-world performance claims will be made until independent review and evaluation are completed.

2. Research Scope

The initial evaluation will focus on three categories.

2.1 Benchmark Performance

Claims reporting measurable AI model performance on established benchmarks.

Examples include:

* Classification accuracy
* Reasoning benchmark scores
* Code-generation benchmark performance
* Language-model evaluation results

2.2 Model Comparisons

Claims comparing the performance of two or more AI systems under documented evaluation conditions.

2.3 Reproducibility

Claims concerning whether reported experimental results can be reproduced using documented methods, datasets, and evaluation settings.

3. Eligible Sources

Candidate claims may originate from:

* Peer-reviewed AI research publications
* Publicly accessible research preprints
* Official benchmark publications
* Research institution technical reports
* Publicly documented experimental evaluations

Each source must have sufficient methodological detail to support independent assessment.

Preprint status and peer-review status must be recorded.

Publication status alone must not determine whether a claim is accepted or rejected.

4. Inclusion Criteria

A candidate claim must satisfy all of the following:

1. It makes a specific, testable statement.
2. It concerns AI model performance, comparison, or reproducibility.
3. It originates from an identifiable research source.
4. The original publication or technical report is accessible.
5. Relevant evaluation methods are documented.
6. The claim can be assessed using available evidence.
7. The claim has a unique identifier.
8. The source and publication date can be recorded.
9. Relevant benchmark or dataset versions can be identified where applicable.
10. The claim can be evaluated without relying on ResearchOS predictions.

5. Exclusion Criteria

Exclude claims that:

* Are purely promotional or subjective
* Lack identifiable original sources
* Cannot be stated precisely
* Depend on inaccessible evidence essential to evaluation
* Require unauthorized access to proprietary data
* Lack sufficient methodological information for meaningful assessment
* Duplicate another selected claim without adding a distinct evaluation question
* Require handling sensitive or restricted information without authorization

Every exclusion must be documented with a reason.

Claims must not be excluded merely because ResearchOS is likely to classify them incorrectly.

6. Claim Representation

Each selected claim must contain:

Field	Requirement
claim_id	Unique identifier
claim_text	Exact, testable claim
domain	Artificial Intelligence
category	Performance, Comparison, or Reproducibility
source_title	Original publication title
source_identifier	DOI, arXiv ID, or equivalent
publication_date	Date or year
benchmark	Relevant benchmark, if applicable
benchmark_version	Version or documented release
evaluation_metric	Metric used in the claim
reported_result	Result reported by the source
evaluation_conditions	Relevant experimental settings
evidence_sources	Supporting or contradictory sources
inclusion_reason	Explanation of eligibility

If a field is not applicable, record that explicitly rather than inventing a value.

7. Initial Dataset Composition

The pilot will target 10 candidate claims.

Proposed selection:

Category	Target claims
Benchmark performance	4
Model comparisons	3
Reproducibility	3
Total	10

These targets may be adjusted if eligible evidence is insufficient.

Changes must be documented before evaluation.

The dataset must not be artificially balanced using knowledge of ResearchOS predictions.

8. Evidence Requirements

Each candidate claim should have:

* An identifiable original publication
* Traceable evidence citations
* Documented experimental methods
* Relevant benchmark or dataset information
* Available supporting or contradictory findings
* Recorded limitations and uncertainties

Multiple citations must not automatically be treated as independent evidence.

Evidence independence requires examining whether sources share underlying experiments, datasets, or reported results.

9. Benchmark Comparability

Performance claims must be evaluated in context.

Reviewers should examine:

* Benchmark version
* Dataset split
* Evaluation metric
* Model version
* Prompting or inference settings
* Number of evaluation trials
* Statistical uncertainty, when reported
* Potential benchmark contamination
* Differences in experimental conditions

Scores obtained under materially different conditions must not be treated as directly comparable without justification.

10. Independent Reference Review

Each claim should receive assessments from at least two qualified reviewers.

Reviewers must not see ResearchOS predictions before submitting their initial assessments.

Permitted labels:

Label	Interpretation
ACCEPT	Available evidence adequately supports the claim under the protocol.
REJECT	Available evidence contradicts the claim under the protocol.
UNCERTAIN	Available evidence is insufficient, conflicting, or inconclusive.

Reviewers must document their reasoning and relevant evidence.

Disagreements must be preserved and adjudicated according to EXTERNAL_VALIDATION_PROTOCOL.md.

11. Prediction Isolation

The evaluation process must maintain three separate stages:

Stage A — Reference assessment

Independent reviewers examine the evidence and establish reference labels.

Stage B — ResearchOS classification

ResearchOS processes claims and permitted evidence inputs without access to reference labels or reviewer conclusions.

Stage C — Evaluation

The evaluation framework compares ResearchOS predictions with finalized reference labels.

Reference labels must not influence system predictions.

12. Evaluation Metrics

The external evaluation will report:

* Total evaluated claims
* Class distribution
* Accuracy
* False acceptance count and rate
* False rejection count and rate
* Uncertainty count and rate
* Confusion matrix
* Per-class results
* Reviewer agreement
* Reproducibility information

Metrics with zero denominators must be identified as undefined.

Results must include dataset size and limitations.

13. Reproducibility Requirements

Record:

* ResearchOS commit SHA
* Dataset version
* Evaluation protocol version
* Claim-selection criteria version
* Source identifiers
* Benchmark versions
* Evaluation configuration
* Execution environment
* Dataset fingerprint
* Evaluation fingerprint

All modifications to the dataset after initial selection must be documented.

14. Quality Controls

Before evaluation:

* [ ]	Ten eligible candidate claims have been identified, or a documented smaller sample has been approved.
* [ ]	Each claim has a traceable original source.
* [ ]	Inclusion and exclusion criteria have been applied.
* [ ]	Duplicate claims have been checked.
* [ ]	Benchmark conditions have been recorded.
* [ ]	Evidence provenance has been documented.
* [ ]	Independent reviewer assessments are available.
* [ ]	Reviewer disagreements are preserved.
* [ ]	Reference labels are finalized separately.
* [ ]	ResearchOS predictions are generated without label leakage.
* [ ]	Evaluation inputs and software versions are recorded.

15. Interpretation and Limitations

The initial pilot is exploratory.

Ten claims are insufficient to establish broad generalization across AI research.

Published benchmark results may contain reporting errors, methodological limitations, or dataset contamination.

Independent reviewer labels are evidence-based judgments rather than absolute truth.

A successful pilot will demonstrate that the evaluation process can be executed transparently and reproducibly. It will not establish production readiness.

16. Completion Criteria

This phase is complete when:

* [ ]	Candidate claims are collected.
* [ ]	Sources and evidence are documented.
* [ ]	Eligibility decisions are recorded.
* [ ]	Independent reference reviews are completed.
* [ ]	ResearchOS predictions are recorded separately.
* [ ]	Evaluation metrics are calculated.
* [ ]	Classification errors are analyzed.
* [ ]	Reproducibility is verified.
* [ ]	Findings and limitations are published.

⸻

Current status: Selection criteria defined. No external AI claims have yet been evaluated.
