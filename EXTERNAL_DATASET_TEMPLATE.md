ResearchOS | TECT v0.6

External Evaluation Dataset Template

Version: 0.1
Status: Template — No External Evaluation Performed
Protocol: EXTERNAL_VALIDATION_PROTOCOL.md
Schema: external_validation_schema.py

⸻

1. Purpose

This template defines the information required to evaluate ResearchOS against independently established scientific reference labels.

The dataset must preserve a clear separation between:

1. Scientific claims and evidence
2. Independent reviewer assessments
3. Adjudicated reference labels
4. ResearchOS predictions
5. Evaluation results

Important: This document is a template, not a completed dataset. No real-world validation results are claimed.

2. Dataset Metadata

Field	Value
Dataset identifier	TBD
Dataset version	TBD
Scientific domain	TBD
Dataset curator	TBD
Collection start date	TBD
Collection end date	TBD
Evaluation protocol version	0.1
ResearchOS version	TBD
ResearchOS commit SHA	TBD
Dataset license or usage permission	TBD
Dataset fingerprint	TBD
Number of claims	TBD

3. Claim Record

Each claim must contain the following information.

Field	Description
claim_id	Unique claim identifier
domain	Scientific research domain
claim_text	Exact scientific claim
source_document	Original publication or source
source_identifier	DOI or another persistent identifier, if available
publication_date	Publication date, if known
collection_date	Date the claim was collected
inclusion_reason	Reason for including the claim
exclusion_flags	Potential quality or eligibility concerns

Blank Claim Record

Claim ID: TBD

Scientific domain: TBD

Claim text: TBD

Original source: TBD

Persistent identifier: TBD

Publication date: TBD

Collection date: TBD

Inclusion reason: TBD

Exclusion flags: None recorded / TBD

4. Evidence Records

Every evidence record must identify its source and provenance.

Field	Description
evidence_id	Unique evidence identifier
claim_id	Associated scientific claim
citation	Complete source citation
origin_id	Identifier for the underlying evidence origin
evidence_type	Supporting, contradictory, or inconclusive
source_location	Page, section, figure, or other location
verification_status	Verification status
verification_method	Method used to verify the evidence
verification_date	Date of verification
notes	Relevant limitations

Blank Evidence Record

Evidence ID: TBD

Claim ID: TBD

Citation: TBD

Origin ID: TBD

Evidence type: TBD

Source location: TBD

Verification status: Not yet verified

Verification method: TBD

Verification date: TBD

Notes: TBD

Evidence Independence

Two citations do not necessarily represent two independent evidence origins.

Multiple publications may depend on the same underlying dataset, experiment, or source.

Evidence independence must be assessed and documented rather than inferred from citation counts alone.

5. Independent Reviewer Assessments

Each claim should receive assessments from at least two distinct qualified reviewers.

Reviewer 1

Reviewer ID: TBD

Relevant expertise: TBD

Conflict-of-interest declaration: TBD

Assessment date: TBD

Reference label: TBD

Rationale: TBD

Evidence reviewed: TBD

Uncertainty notes: TBD

Reviewer 2

Reviewer ID: TBD

Relevant expertise: TBD

Conflict-of-interest declaration: TBD

Assessment date: TBD

Reference label: TBD

Rationale: TBD

Evidence reviewed: TBD

Uncertainty notes: TBD

Reviewer Independence

Reviewers must submit their initial assessments without access to ResearchOS predictions.

The review process must document whether reviewers were also blinded to one another’s assessments.

Distinct reviewer identifiers alone do not prove reviewer independence.

6. Reference Labels

The permitted reference labels are:

Label	Meaning
ACCEPT	Evidence adequately supports the claim under the protocol.
REJECT	Evidence contradicts the claim under the protocol.
UNCERTAIN	Evidence is insufficient, conflicting, or inconclusive.

Reference labels must be established independently of ResearchOS predictions.

These labels are evidence-based judgments, not declarations of absolute scientific truth.

7. Disagreement and Adjudication

Claim ID: TBD

Reviewer 1 label: TBD

Reviewer 2 label: TBD

Agreement: TBD

Adjudication required: TBD

Adjudicator ID: TBD

Adjudication date: TBD

Evidence considered: TBD

Final reference label: TBD

Adjudication rationale: TBD

Unresolved concerns: TBD

Original reviewer assessments must be preserved.

If a disagreement cannot be resolved, the case must remain explicitly documented as unresolved or receive an UNCERTAIN reference label when justified by the protocol.

8. ResearchOS Prediction Record

ResearchOS predictions must be generated separately from reviewer reference labels.

Claim ID: TBD

ResearchOS version: TBD

Commit SHA: TBD

Execution timestamp: TBD

Input evidence identifiers: TBD

Configuration: TBD

Predicted outcome: TBD

Controller status: TBD

Execution notes: TBD

Prediction Isolation

Reference labels, reviewer rationales, and adjudication outcomes must not be supplied to ResearchOS when generating predictions.

Predictions should be saved before the evaluation framework compares them with reference labels.

Any exceptions must be documented.

9. Evaluation Record

After predictions and reference labels are finalized, evaluation metrics may be calculated.

Dataset identifier: TBD

Dataset version: TBD

Evaluation timestamp: TBD

Number of cases: TBD

Correct classifications: TBD

Accuracy: TBD

False acceptances: TBD

False acceptance rate: TBD

False rejections: TBD

False rejection rate: TBD

Uncertain predictions: TBD

Uncertainty rate: TBD

Evaluation fingerprint: TBD

Evaluator version: TBD

Metric Interpretation

A reported zero error count does not establish that the true error rate is zero.

Rates with zero denominators must be identified as undefined in external reports, even if the current software implementation returns 0.0.

Dataset size, class distribution, uncertainty, and selection methods must accompany reported metrics.

10. Dataset Quality Checklist

Before an evaluation begins:

* [ ]	Claims have unique identifiers.
* [ ]	Scientific domains are documented.
* [ ]	Original claim sources are recorded.
* [ ]	Evidence citations are traceable.
* [ ]	Evidence origins are documented.
* [ ]	Dataset inclusion criteria are recorded.
* [ ]	Reviewer qualifications are documented.
* [ ]	Conflicts of interest are documented.
* [ ]	At least two independent assessments exist per claim.
* [ ]	Reviewer disagreements are preserved.
* [ ]	Final reference labels are documented.
* [ ]	ResearchOS predictions are generated independently.
* [ ]	Dataset and software versions are recorded.
* [ ]	Evaluation inputs are reproducible.
* [ ]	Exclusions and missing data are documented.

11. Data Handling

Use only data that may lawfully and ethically be collected and evaluated.

Respect publication licenses, database terms, and applicable privacy requirements.

Do not include confidential reviewer identities, sensitive personal information, or restricted research data in a public repository without appropriate authorization.

Use pseudonymous reviewer identifiers where suitable.

12. Known Limitations

This template does not itself:

* Collect scientific evidence
* Verify scientific claims
* Recruit qualified reviewers
* Establish reviewer independence
* Resolve scientific disagreements
* Generate ResearchOS predictions
* Demonstrate real-world accuracy

The Python dataset schema validates selected structural requirements. Additional methodological checks remain necessary.

13. Next Steps

1. Select a specific scientific domain.
2. Define inclusion and exclusion criteria.
3. Identify suitable published research sources.
4. Assemble an initial candidate claim dataset.
5. Arrange independent expert review.
6. Preserve reference labels separately from predictions.
7. Run ResearchOS against the approved dataset.
8. Evaluate and report results transparently.

⸻

Current status: Dataset template established. No external scientific claims have yet been independently evaluated under this protocol.
