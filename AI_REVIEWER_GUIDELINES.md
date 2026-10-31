ResearchOS | TECT v0.6

Independent AI Research Reviewer Guidelines

Version: 0.1
Status: Draft — Reviewer Recruitment Pending
Domain: Artificial Intelligence
Development branch: develop/tect-v0.6-external-validation

Related documents:

* EXTERNAL_VALIDATION_PROTOCOL.md
* AI_EVALUATION_CRITERIA.md
* AI_CANDIDATE_CLAIMS.md
* AI_EVIDENCE_REVIEW.md
* external_validation_schema.py

⸻

1. Purpose

These guidelines establish procedures for independently evaluating AI research claims in the ResearchOS external validation pilot.

The initial dataset contains 10 candidate claims.

Each claim must receive assessments from at least two qualified reviewers before a final reference label is established.

Reviewers must evaluate the available scientific evidence, not the anticipated performance of ResearchOS.

2. Reviewer Qualifications

Reviewers should demonstrate relevant expertise through one or more of the following:

* Research experience in machine learning or artificial intelligence.
* Peer-reviewed publications in a relevant field.
* Professional experience evaluating AI systems.
* Experience reproducing machine learning experiments.
* Expertise in relevant benchmarks or evaluation methodologies.

Qualifications must be documented before assignments begin.

Expertise should match the specific claim. For example, a neural machine translation claim should preferably be reviewed by someone familiar with translation evaluation.

A reviewer must not be treated as qualified solely because they use AI tools.

3. Reviewer Independence

Each reviewer must:

1. Submit an individual assessment.
2. Evaluate the evidence without seeing ResearchOS predictions.
3. Avoid discussing their initial label with other assigned reviewers.
4. Disclose relevant conflicts of interest.
5. Document the evidence supporting their decision.
6. Identify important limitations or uncertainty.

Reviewers must not receive instructions to produce a particular distribution of ACCEPT, REJECT, or UNCERTAIN labels.

4. Conflicts of Interest

Reviewers must disclose whether they:

* Authored or contributed to the research being assessed.
* Collaborated with the original research team.
* Have a financial interest related to the claim.
* Participated in developing or evaluating ResearchOS.
* Have another relationship that could materially affect impartiality.

A disclosed conflict does not automatically invalidate an assessment.

The project coordinator must determine whether the conflict requires reassignment, additional review, or explicit qualification of the findings.

Reviewers directly involved in generating ResearchOS predictions must not establish reference labels for the same claims.

5. Reviewer Blinding

Before submitting an initial assessment, reviewers must not have access to:

* ResearchOS predictions for the assigned claims.
* ResearchOS classification rationales.
* Other reviewers’ initial labels or rationales.
* Aggregate ResearchOS evaluation results.

Reviewers may access original publications, benchmark documentation, independent studies, and the evidence package prepared for the claim.

The coordinator must record any blinding failures.

6. Claim Interpretation

Reviewers must assess the precise wording of each candidate claim.

A claim that states:

“The original authors reported a score of 28.4 BLEU”

is different from a claim that states:

“The model independently reproduces a score of 28.4 BLEU.”

The first concerns the accuracy of a historical reporting statement.

The second concerns experimental reproducibility.

Reviewers must not silently change a claim’s meaning.

If the wording is ambiguous, reviewers should flag it before assessment.

Any subsequent claim revision must be versioned and documented.

7. Evidence Assessment

Reviewers should consider:

* Source authenticity and provenance.
* Whether the evidence directly addresses the claim.
* Experimental methodology.
* Benchmark and dataset versions.
* Model configuration.
* Evaluation metrics.
* Statistical uncertainty, when available.
* Supporting findings.
* Contradictory findings.
* Evidence independence.
* Reproducibility limitations.

A source that repeats another publication’s result does not automatically constitute independent confirmation.

Absence of independent replication does not, by itself, establish that an original reporting statement is false.

8. Reference Labels

Reviewers must select exactly one initial label.

ACCEPT

Use ACCEPT when the available evidence adequately supports the precise claim under the established protocol.

A supporting rationale must identify the relevant evidence.

REJECT

Use REJECT when reliable evidence adequately contradicts the precise claim.

A supporting rationale must identify the contradiction.

UNCERTAIN

Use UNCERTAIN when available evidence is insufficient, conflicting, inaccessible, or otherwise inconclusive.

UNCERTAIN is a legitimate scientific outcome.

Reviewers must not force ACCEPT or REJECT merely to avoid uncertainty.

9. Reviewer Assessment Record

Each assessment must include:

Field	Requirement
claim_id	Assigned claim identifier
reviewer_id	Stable, non-sensitive reviewer identifier
reviewer_qualification	Relevant expertise
conflict_disclosure	Declared conflicts or none reported
claim_version	Version of the claim assessed
evidence_identifiers	Sources examined
label	ACCEPT, REJECT, or UNCERTAIN
rationale	Evidence-based explanation
limitations	Important uncertainties
assessment_date	Date assessment was completed
blinding_confirmation	Confirmation that predictions were not viewed

The current ReviewerAssessment dataclass stores reviewer ID, label, and rationale.

Additional review metadata must be retained in an auditable companion record until the software schema is extended.

Do not place personal contact details or sensitive information in a public repository.

10. Independent Review Procedure

For each claim:

1. The coordinator prepares a versioned evidence package.
2. The coordinator assigns two qualified reviewers.
3. Reviewers declare relevant conflicts.
4. Reviewers independently inspect the evidence.
5. Each reviewer submits a label and rationale.
6. Both initial assessments are preserved.
7. The coordinator checks for disagreement.
8. Any disagreement is adjudicated and documented.
9. The final reference label is recorded.
10. The reference dataset is frozen before evaluation.

A coordinator must not change a reviewer’s original label to create agreement.

11. Disagreement Resolution

When reviewers disagree:

1. Preserve both initial assessments.
2. Identify the precise points of disagreement.
3. Examine whether the claim wording is ambiguous.
4. Review relevant evidence and methodological differences.
5. Seek an additional qualified assessment when appropriate.
6. Document the adjudication process.
7. Record the final reference label and justification.

If disagreement cannot be resolved using available evidence, UNCERTAIN may be the appropriate final label.

The adjudication record must identify who made the final decision and whether they had access to ResearchOS predictions.

12. Special Requirements for AI-001

Claim: The original Transformer paper reported 28.4 BLEU on WMT 2014 English-to-German.

Reviewers should examine:

* Vaswani et al. (2017), Attention Is All You Need.
* The original reported benchmark table.
* The Transformer (big) model configuration.
* WMT 2014 English-to-German evaluation details.
* Evidence provenance recorded in AI_EVIDENCE_REVIEW.md.

Additional contextual sources include:

* The Annotated Transformer — separate implementation evidence.
* Ott et al. (2018), Scaling Neural Machine Translation — related benchmark evidence.

Reviewers must distinguish confirmation of the original reporting statement from independent reproduction of the reported score.

Current reviewer status: No assessments collected.

Current reference label: UNASSIGNED.

13. Quality Assurance

Before finalizing a reference label:

* [ ]	Claim wording and version confirmed.
* [ ]	Evidence package version recorded.
* [ ]	Two qualified reviewers assigned.
* [ ]	Reviewer qualifications documented.
* [ ]	Conflicts of interest assessed.
* [ ]	Prediction blinding confirmed.
* [ ]	Independent assessments completed.
* [ ]	Initial labels preserved.
* [ ]	Disagreements documented.
* [ ]	Adjudication completed where required.
* [ ]	Final reference label justified.
* [ ]	Review record retained for audit.

14. ResearchOS Evaluation Separation

Reference labels must be established without using ResearchOS predictions.

ResearchOS predictions must be recorded separately, with the software commit SHA and evaluation configuration.

The evaluation process may compare predictions and reference labels only after both have been frozen.

Reviewers must not revise reference labels merely because ResearchOS disagrees with them.

15. Limitations

Independent reviewers can disagree even when acting in good faith.

Reviewer expertise does not guarantee correctness.

A reference label represents a documented assessment of available evidence, not absolute scientific truth.

Ten candidate claims provide an exploratory pilot and do not establish general reliability across AI research.

16. Completion Criteria

The reviewer phase is complete when:

* [ ]	Reviewers have been recruited.
* [ ]	Qualifications and conflicts are documented.
* [ ]	Evidence packages are prepared.
* [ ]	Independent assessments are collected.
* [ ]	Disagreements are adjudicated.
* [ ]	Final reference labels are recorded.
* [ ]	Review provenance is preserved.
* [ ]	The reference dataset is frozen.

⸻

Current status: Reviewer guidelines established. No independent reviewer assessments or final reference labels have been collected.
