ResearchOS | TECT v0.6

Independent AI Research Reviewer Assessment Template

Version: 0.1
Status: Blank template — No assessments collected
Domain: Artificial Intelligence

Related documents:

* EXTERNAL_VALIDATION_PROTOCOL.md
* AI_REVIEWER_GUIDELINES.md
* AI_CANDIDATE_CLAIMS.md
* AI_EVIDENCE_REVIEW.md

⸻

1. Purpose

This template provides a standardized record for independent assessments of AI research claims.

Each claim must receive assessments from at least two qualified reviewers.

Reviewers must submit their initial assessments independently and without access to ResearchOS predictions or other reviewers’ initial decisions.

Important: This file is a blank template, not evidence that any review has occurred.

Completed assessments should be stored in separate, appropriately access-controlled records until initial reviews are finalized.

2. Claim Information

Claim ID: AI-001

Claim version: Pending confirmation

Research category: Benchmark performance

Claim text:

The Transformer model achieved a reported BLEU score of 28.4 on WMT 2014 English-to-German translation.

Original publication: Vaswani et al. (2017), Attention Is All You Need

Publication identifier: arXiv:1706.03762

Primary evidence: Original publication, Table 2 and Section 6.1

Evidence package version: Pending

Evidence package fingerprint: Pending

Assessment deadline: To be assigned

Claim Interpretation

The candidate claim concerns a result reported in the original publication.

Reviewers must distinguish:

* Whether the publication reports the stated result.
* Whether the underlying experiment was independently reproduced.

These are different evaluation questions.

If the claim wording is ambiguous, flag it before assigning a label.

⸻

3. Reviewer 1 — Independent Assessment

3.1 Reviewer Information

Reviewer ID: Pending

Relevant qualifications: Pending

Area of expertise: Pending

Conflict-of-interest declaration: Pending

Conflict reviewed by coordinator: Pending

Assessment date: Pending

3.2 Independence Confirmation

* [ ]	I assessed the evidence independently.
* [ ]	I did not view ResearchOS predictions.
* [ ]	I did not view another reviewer’s initial assessment.
* [ ]	I disclosed relevant conflicts of interest.
* [ ]	I assessed the specified claim version.

3.3 Evidence Examined

Evidence identifiers: Pending

Original publication examined: Pending

Additional publications examined: Pending

Benchmark documentation examined: Pending

Evidence provenance concerns: Pending

3.4 Assessment

Selected label: UNASSIGNED

Select exactly one when completing the review:

* [ ]	ACCEPT
* [ ]	REJECT
* [ ]	UNCERTAIN

Evidence supporting the decision:

Pending independent reviewer assessment.

Evidence contradicting the claim:

Pending independent reviewer assessment.

Methodological limitations:

Pending independent reviewer assessment.

Assessment rationale:

Pending independent reviewer assessment.

Additional evidence needed, if any:

Pending independent reviewer assessment.

⸻

4. Reviewer 2 — Independent Assessment

4.1 Reviewer Information

Reviewer ID: Pending

Relevant qualifications: Pending

Area of expertise: Pending

Conflict-of-interest declaration: Pending

Conflict reviewed by coordinator: Pending

Assessment date: Pending

4.2 Independence Confirmation

* [ ]	I assessed the evidence independently.
* [ ]	I did not view ResearchOS predictions.
* [ ]	I did not view another reviewer’s initial assessment.
* [ ]	I disclosed relevant conflicts of interest.
* [ ]	I assessed the specified claim version.

4.3 Evidence Examined

Evidence identifiers: Pending

Original publication examined: Pending

Additional publications examined: Pending

Benchmark documentation examined: Pending

Evidence provenance concerns: Pending

4.4 Assessment

Selected label: UNASSIGNED

Select exactly one when completing the review:

* [ ]	ACCEPT
* [ ]	REJECT
* [ ]	UNCERTAIN

Evidence supporting the decision:

Pending independent reviewer assessment.

Evidence contradicting the claim:

Pending independent reviewer assessment.

Methodological limitations:

Pending independent reviewer assessment.

Assessment rationale:

Pending independent reviewer assessment.

Additional evidence needed, if any:

Pending independent reviewer assessment.

⸻

5. Reviewer Agreement

Complete this section only after both initial assessments have been submitted and preserved.

Reviewer 1 label: UNASSIGNED

Reviewer 2 label: UNASSIGNED

Agreement status: NOT ASSESSED

Points of agreement: Pending

Points of disagreement: Pending

Additional evidence required: Pending

Important: Do not change either reviewer’s original assessment during adjudication.

⸻

6. Adjudication Record

Complete this section only after the independent assessments are finalized.

Adjudication required: NOT DETERMINED

Adjudicator ID: Pending

Adjudicator qualifications: Pending

Conflict-of-interest declaration: Pending

Prediction blinding confirmed: Pending

Adjudication date: Pending

Evidence considered: Pending

Disagreement resolution: Pending

Final reference label: UNASSIGNED

Final rationale: Pending

Outstanding uncertainty: Pending

If disagreement cannot be resolved from available evidence, UNCERTAIN may be the appropriate final label.

⸻

7. Reference Dataset Integrity

Before releasing the finalized reference record:

* [ ]	Both reviewer assessments are complete.
* [ ]	Reviewer qualifications are documented.
* [ ]	Conflicts of interest are assessed.
* [ ]	Prediction blinding is confirmed.
* [ ]	Original reviewer labels are preserved.
* [ ]	Adjudication is documented where required.
* [ ]	Final reference label is justified.
* [ ]	Claim version is recorded.
* [ ]	Evidence package version is recorded.
* [ ]	Reference dataset version is recorded.
* [ ]	Reference dataset fingerprint is recorded.

Reference dataset status: NOT FROZEN

⸻

8. ResearchOS Prediction Isolation

This reviewer template must not contain ResearchOS predictions during independent assessment.

After the reference dataset is frozen, predictions must be recorded separately with:

* ResearchOS commit SHA
* Claim identifier and version
* Input evidence version
* Evaluation configuration
* Prediction
* Prediction timestamp
* Reproducibility information

Do not revise reference labels merely because ResearchOS predictions disagree.

⸻

9. Privacy and Record Management

Reviewer identities and contact information must not be published without appropriate permission.

Use stable, non-sensitive reviewer identifiers in public records.

Store completed assessments in a location that prevents reviewers from seeing each other’s initial decisions.

A public GitHub repository is suitable for publishing this blank template, but it should not be used to collect confidential initial assessments.

After review completion, publish an appropriately redacted audit record when permissions allow.

⸻

10. Software Schema Compatibility

The current ReviewerAssessment dataclass contains:

* reviewer_id
* label
* rationale

Additional assessment metadata in this template must be preserved separately until the software schema supports those fields.

The placeholder UNASSIGNED is not a valid ReferenceLabel enum value.

Do not construct a finalized ExternalValidationCase using incomplete reviewer records or placeholder labels.

⸻

11. Current Status

Requirement	Status
Assessment template created	Ready
Reviewer 1 recruited	Pending
Reviewer 2 recruited	Pending
Reviewer qualifications verified	Pending
Independent assessments received	0
Adjudication completed	No
Final reference label assigned	No
Reference dataset frozen	No
ResearchOS prediction generated	No

Scientific status: Independent review has not yet occurred. No external validation result is claimed.

⸻

End of template
