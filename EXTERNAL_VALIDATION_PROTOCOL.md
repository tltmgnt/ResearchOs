ResearchOS | TECT v0.6

External Validation Protocol

Version: 0.1
Status: Draft — Not Yet Executed
Project: ResearchOS | TECT
Development Branch: develop/tect-v0.6-external-validation

⸻

1. Objective

The objective of v0.6 is to evaluate ResearchOS using independently labeled scientific research claims.

Unlike the synthetic pilot introduced in v0.5, external validation must use reference labels established independently of ResearchOS predictions.

The evaluation will measure classification accuracy, false acceptance, false rejection, uncertainty, and reproducibility.

This protocol defines the methodology before external evaluation begins.

2. Scope

The initial evaluation will focus on scientific claims that can be assessed against documented evidence.

Each case must include:

* A unique claim identifier
* A clearly stated scientific claim
* The scientific domain
* Evidence sources
* An independently established reference label
* A ResearchOS prediction
* A documented evaluation outcome

The initial study will use a manageable pilot dataset before expanding to larger evaluations.

3. Reference Labels

Three reference labels will be used:

Label	Definition
ACCEPT	Available evidence adequately supports the claim under the predefined evaluation criteria.
REJECT	Available evidence contradicts the claim under the predefined evaluation criteria.
UNCERTAIN	Available evidence is insufficient, conflicting, or inconclusive.

Reference labels must not be derived from ResearchOS outputs.

These labels describe evidence-based assessments, not absolute scientific truth.

4. Independent Review

Each claim should be evaluated by at least two qualified reviewers working independently.

Reviewers must:

1. Examine the claim and relevant evidence.
2. Assign a reference label.
3. Record their reasoning.
4. Identify supporting and contradictory sources.
5. Document uncertainty.

Reviewers should not see ResearchOS predictions before submitting their initial assessments.

Reviewer qualifications and potential conflicts of interest must be documented.

5. Disagreement Resolution

When reviewers disagree:

1. Preserve both original labels.
2. Record the disagreement.
3. Conduct a documented adjudication.
4. Assign a final reference label only when justified.
5. Retain unresolved cases as UNCERTAIN or report them separately.

Disagreements must not be silently overwritten.

Inter-reviewer agreement should be reported when sufficient data are available.

6. Dataset Requirements

Each evaluation case must contain:

Field	Description
claim_id	Unique identifier
domain	Scientific field
claim_text	Claim being evaluated
evidence_sources	Documented supporting or contradictory sources
reviewer_1_label	First independent assessment
reviewer_2_label	Second independent assessment
final_reference_label	Adjudicated reference label
researchos_prediction	System-generated classification
notes	Review and adjudication details

Source provenance must be preserved.

Personal or sensitive information should be excluded unless its use is authorized and appropriately protected.

7. Dataset Selection

The evaluation dataset should include:

* Supported claims
* Contradicted claims
* Claims with insufficient evidence
* Claims with conflicting evidence
* Cases involving multiple evidence sources
* Cases requiring dependency reasoning

Selection criteria must be documented before running the evaluation.

Cases must not be chosen solely because ResearchOS is expected to classify them correctly.

8. Evaluation Metrics

8.1 Accuracy

The proportion of evaluated cases where ResearchOS predictions match the final reference labels.

8.2 False Acceptance Rate

The number of reference REJECT cases classified as ACCEPT, divided by the total number of reference REJECT cases.

8.3 False Rejection Rate

The number of reference ACCEPT cases classified as REJECT, divided by the total number of reference ACCEPT cases.

8.4 Uncertainty Rate

The number of cases classified as UNCERTAIN by ResearchOS, divided by the total number of evaluated cases.

8.5 Additional Reporting

Results should also include:

* Confusion matrix
* Per-class performance
* Dataset class distribution
* Reviewer agreement
* Error analysis
* Confidence intervals when appropriate

Undefined rates caused by zero denominators must be explicitly identified in external reports rather than interpreted as demonstrated zero error.

9. Reproducibility

Each evaluation run must record:

* ResearchOS version and commit identifier
* Dataset version
* Evaluation protocol version
* Relevant configuration
* Execution environment
* Evaluation timestamp
* Dataset fingerprint
* Evaluation output fingerprint

Repeated evaluation of identical inputs under identical conditions should produce identical classifications and metrics.

10. Separation of Responsibilities

Three components must remain logically separate:

Reference evaluation: Independent reviewers establish evidence-based reference labels.

ResearchOS classification: The system processes claims and produces predictions without access to reference labels.

Metrics calculation: The evaluation framework compares predictions with reference labels.

This separation reduces the risk of circular evaluation.

11. Quality Controls

Before reporting results:

* Verify unique case identifiers.
* Validate required dataset fields.
* Check source provenance.
* Confirm independent labeling.
* Check for duplicate or overlapping cases.
* Review missing data.
* Confirm that reference labels were not used to generate predictions.
* Verify evaluation reproducibility.
* Preserve all classification errors.

Any exclusions must be documented with reasons.

12. Initial Evaluation Plan

The initial external pilot will proceed in five stages:

1. Define the scientific domain and inclusion criteria.
2. Assemble a small dataset of real scientific claims.
3. Obtain independent reference labels.
4. Run ResearchOS without exposing reference labels.
5. Calculate metrics and publish an evaluation report.

Dataset size will be selected based on available qualified reviewers, evidence quality, and study objectives.

No real-world accuracy claims will be made before the evaluation is completed.

13. Success Criteria

The initial v0.6 pilot will be considered methodologically complete when:

* [ ]	A documented external dataset exists.
* [ ]	Dataset inclusion criteria are recorded.
* [ ]	Independent reviewer assessments are available.
* [ ]	Reviewer disagreements are documented.
* [ ]	ResearchOS predictions are generated separately.
* [ ]	Evaluation metrics are calculated.
* [ ]	Classification errors are reviewed.
* [ ]	Reproducibility is demonstrated.
* [ ]	Results and limitations are documented.

Passing automated software tests alone does not satisfy these criteria.

14. Limitations

External reference labels may contain errors or reflect scientific uncertainty.

A small pilot may not generalize to other scientific domains.

Performance depends on dataset composition, evidence quality, reviewer expertise, and evaluation criteria.

This protocol does not establish clinical, regulatory, or production suitability.

15. Conclusion

ResearchOS | TECT v0.6 will investigate whether its evidence-based classification framework produces reliable results when compared against independently established reference labels.

The protocol prioritizes transparent methodology, reproducibility, documented uncertainty, and honest reporting of errors.

Current status: Protocol drafted; external validation not yet performed.
