ResearchOS | TECT v0.6

AI Evidence Review

Version: 0.2
Status: Evidence collection — Independent review pending
Research domain: Artificial Intelligence
Development branch: develop/tect-v0.6-external-validation

Related documents:

* EXTERNAL_VALIDATION_PROTOCOL.md
* AI_EVALUATION_CRITERIA.md
* AI_CANDIDATE_CLAIMS.md
* AI_REVIEWER_GUIDELINES.md
* AI_REVIEWER_ASSESSMENT_TEMPLATE.md
* AI_REVIEWER_RECRUITMENT.md
* external_validation_schema.py

⸻

1. Purpose

This document records evidence gathered for real-world artificial intelligence research claims before independent reference labels are established.

The objective is to create a transparent, auditable evidence record that supports external evaluation of ResearchOS.

The review process distinguishes five separate activities:

1. Recording results reported by original researchers.
2. Verifying statements against identifiable publications.
3. Examining supporting, contradictory, and independent evidence.
4. Obtaining independent reviewer assessments and reference labels.
5. Comparing frozen reference labels with separately generated ResearchOS predictions.

These activities must remain separate to prevent circular validation.

Scientific integrity principle: A published claim is not automatically a validated scientific conclusion.

⸻

2. Evidence Record: AI-001

2.1 Claim Identification

Claim ID: AI-001

Category: Benchmark performance

Research area: Neural machine translation

Candidate claim:

The Transformer model achieved a reported BLEU score of 28.4 on WMT 2014 English-to-German translation.

Claim type: Historical reporting of an experimental result.

Claim interpretation: The candidate claim concerns the score reported by the original publication.

It does not assert that an independent research team has reproduced the exact result.

Claim wording clarification: The reported score corresponds to the Transformer (big) configuration.

A future claim revision may explicitly identify Transformer (big), provided the change is versioned and applied consistently before independent review.

Current claim version: Original candidate wording retained.

Reference label: UNASSIGNED

ResearchOS prediction: NOT RUN

⸻

2.2 Original Publication

Title: Attention Is All You Need

Authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin.

Publication year: 2017

Publication venue: Advances in Neural Information Processing Systems (NeurIPS 2017)

Publication identifier: arXiv:1706.03762

Evidence identifier: AI-001-SOURCE-01

Origin ID: vaswani-2017-transformer

Source type: Original research publication

Primary evidence locations:

* Section 5.1 — Training Data and Batching
* Section 5.2 — Hardware and Schedule
* Table 2 — Translation benchmark results
* Section 6.1 — Machine Translation

Source verification status: PRIMARY SOURCE REPORTING VERIFIED

Independent replication status: NOT ESTABLISHED

Source Verification Finding

The original publication reports a BLEU score of 28.4 for Transformer (big) on WMT 2014 English-to-German translation.

This confirms the historical reporting statement.

It does not independently establish the reproducibility or general reliability of the result.

⸻

2.3 Reported Experimental Result

Field	Recorded information
Research task	Neural machine translation
Translation direction	English-to-German
Benchmark	WMT 2014
Evaluation test set	newstest2014
Model architecture	Transformer
Model configuration	Transformer (big)
Evaluation metric	BLEU
Reported result	28.4 BLEU
Comparison configuration	Transformer (base)
Comparison result	27.3 BLEU
Training hardware	Eight NVIDIA P100 GPUs
Reported training duration	Approximately 3.5 days
Training steps	300,000
Evidence location	Table 2 and Section 6.1
Independent reproduction	Not established

Verification Finding

The reported 28.4 BLEU result is attributable to Transformer (big), not Transformer (base).

The original publication provides the experimental context for this result.

Evidence Limitation

The result has been verified as a statement appearing in the original publication.

This is not equivalent to independently rerunning the experiment.

⸻

2.4 Experimental Conditions and Evidence Provenance

2.4.1 Training Data

Dataset: WMT 2014 English-to-German

Approximate training size: 4.5 million sentence pairs

Tokenization: Byte-pair encoding

Shared vocabulary: Approximately 37,000 tokens

Evidence location: Section 5.1

2.4.2 Model Training

Model: Transformer (big)

Training hardware: Eight NVIDIA P100 GPUs

Training steps: 300,000

Reported training duration: Approximately 3.5 days

Evidence location: Section 5.2

2.4.3 Evaluation Configuration

Translation direction: English-to-German

Evaluation benchmark: WMT 2014

Test set: newstest2014

Reported metric: BLEU

Reported result: 28.4

Beam size: 4

Length penalty: 0.6

Checkpoint averaging: Final 20 checkpoints for the big model

Evidence location: Section 6.1

2.4.4 Provenance Assessment

Evidence identifier: AI-001-SOURCE-01

Origin ID: vaswani-2017-transformer

Evidence classification: ORIGINAL PUBLICATION

Source relationship: Original authors reporting their own experiment.

Evidence independence: Not independent of the original experiment.

2.4.5 Outstanding Technical Details

The following details require further examination before attempting a controlled reproduction:

* Exact BLEU scoring implementation and signature.
* Complete preprocessing and tokenization configuration.
* Software framework and dependency versions.
* Random seeds and run-to-run variability.
* Availability and identity of trained checkpoints.
* Differences between original and modern benchmark evaluation procedures.

Technical reproducibility status: INCOMPLETE

⸻

2.5 Verification Checklist

A. Original Publication

* [x]	Original publication identified.
* [x]	Publication identifier recorded.
* [x]	Reported 28.4 BLEU result located.
* [x]	Transformer (big) model identified.
* [x]	WMT 2014 English-to-German benchmark identified.
* [x]	Primary evidence locations documented.

B. Experimental Conditions

* [x]	Training dataset documented.
* [x]	Approximate training dataset size documented.
* [x]	Tokenization approach documented.
* [x]	Model configuration identified.
* [x]	Training hardware documented.
* [x]	Training duration documented.
* [x]	Training steps documented.
* [x]	Beam size documented.
* [x]	Length penalty documented.
* [x]	Checkpoint averaging documented.
* [ ]	Exact BLEU scoring implementation verified.
* [ ]	Complete software environment verified.
* [ ]	Random seeds and run variability verified.

C. External Evidence

* [x]	Separate Transformer implementation identified.
* [x]	Related external benchmark experiment identified.
* [x]	External benchmark result documented.
* [x]	Major comparability limitations identified.
* [ ]	Full implementation independence assessed.
* [ ]	Comparable exact-result replication established.
* [ ]	Additional supporting evidence systematically reviewed.
* [ ]	Contradictory evidence systematically reviewed.

D. Independent Review

* [ ]	Reviewer 1 recruited.
* [ ]	Reviewer 2 recruited.
* [ ]	Reviewer qualifications verified.
* [ ]	Conflicts of interest assessed.
* [ ]	Independent assessments completed.
* [ ]	Reviewer agreement assessed.
* [ ]	Disagreements adjudicated if necessary.
* [ ]	Final reference label established.

E. ResearchOS Evaluation

* [ ]	Reference dataset frozen.
* [ ]	ResearchOS prediction generated separately.
* [ ]	ResearchOS commit SHA recorded.
* [ ]	Prediction configuration documented.
* [ ]	Evaluation metrics calculated.
* [ ]	Evaluation results independently audited.

Primary-source verification: COMPLETED

External evidence review: PARTIAL

Independent validation: NOT COMPLETED

⸻

2.6 Evidence Limitations and Evaluation Risks

2.6.1 Original-Source Dependence

The original publication provides direct evidence of what its authors reported.

It does not independently confirm its own experimental result.

2.6.2 BLEU Scoring Sensitivity

BLEU scores can depend on:

* Tokenization.
* Text normalization.
* Reference translations.
* Scoring implementation.
* Dataset preparation.
* Evaluation configuration.

Comparisons must account for these differences.

2.6.3 Model Configuration

The 28.4 BLEU result applies to Transformer (big).

The Transformer (base) result must not be substituted.

2.6.4 Dataset Comparability

Independent evaluations must document the training and evaluation datasets.

Using the same test set does not necessarily mean two experiments used identical training conditions.

2.6.5 Training Reproducibility

Potential sources of variation include:

* Training data.
* Model hyperparameters.
* Random seeds.
* Hardware.
* Software dependencies.
* Optimizer configuration.
* Checkpoint selection.
* Decoding parameters.

2.6.6 Evidence Independence

Multiple publications repeating the same reported score do not automatically provide multiple independent confirmations.

Evidence must be traced to its underlying experimental origin.

2.6.7 Claim Interpretation

The historical statement:

“The original paper reported 28.4 BLEU”

is distinct from:

“Independent researchers reproduced 28.4 BLEU.”

A reviewer must assess the exact claim wording.

Independent replication is not a prerequisite for confirming that the original paper reported a particular result.

2.6.8 Reviewer Independence

Independent reviewers must not see ResearchOS predictions before completing their initial assessments.

Their original decisions must be preserved.

2.6.9 Statistical Limitations

A single reported benchmark score does not establish the variability of results across training runs.

Any uncertainty estimates must be supported by documented experiments.

2.6.10 Scientific Conclusion

The original reporting statement has been checked against the primary publication.

The broader experimental reproducibility question remains open.

No independent reviewer reference label has been assigned.

⸻

2.6A Independent Replication Evidence

A. Objective

This section evaluates whether external sources provide evidence relevant to reproducing or independently assessing the original Transformer translation result.

Evidence must be classified according to its actual contribution.

A separate implementation is not automatically an exact replication.

A related benchmark result is not automatically an exact replication.

B. Evidence Classification

Evidence category	Definition	Establishes exact replication?
Original publication	Reports the original experiment	No
Secondary citation	Repeats the original finding	No
Separate implementation	Implements the architecture independently	Not necessarily
Separate benchmark experiment	Reports an independently executed evaluation	Not necessarily
Comparable replication	Repeats sufficiently comparable conditions and evaluates the result	Potentially

C. Comparability Requirements

Candidate replication evidence should be assessed across:

1. Model configuration.
2. Training dataset.
3. Training preprocessing.
4. Evaluation dataset.
5. BLEU scoring procedure.
6. Decoding configuration.
7. Checkpoint selection.
8. Hardware and software environment.
9. Reported results.
10. Independence from the original experimental execution.

Material differences must be documented.

⸻

D. Current Evidence Inventory

AI-001-SOURCE-01 — Original Publication

Source: Vaswani et al. (2017), Attention Is All You Need

Identifier: arXiv:1706.03762

Evidence type: Original research publication

Origin ID: vaswani-2017-transformer

Model: Transformer (big)

Benchmark: WMT 2014 English-to-German

Reported result: 28.4 BLEU

Evidence location: Table 2 and Section 6.1

Assessment:

The original publication documents the reported benchmark result and associated experimental conditions.

It establishes what the authors reported but does not independently reproduce the experiment.

Classification: ORIGINAL SOURCE EVIDENCE

Exact independent replication: NO

⸻

AI-001-IMPLEMENTATION-01 — The Annotated Transformer

Source: The Annotated Transformer

Original author: Alexander “Sasha” Rush

Original publication year: 2018

Source: Harvard NLP

Evidence type: Separate Transformer implementation

Origin ID: harvardnlp-annotated-transformer-2018

Implementation framework: PyTorch

Demonstration task: IWSLT German-to-English translation

Assessment:

The Annotated Transformer provides a separately written, educational implementation of the Transformer architecture.

The resource contains explanations and code corresponding to the original Transformer paper.

Its demonstration does not establish that the original Transformer (big) model achieved 28.4 BLEU in an independently reproduced WMT 2014 English-to-German experiment.

Text describing the original paper’s experimental results must not be mistaken for newly executed experimental evidence.

Classification: SEPARATE IMPLEMENTATION EVIDENCE

Benchmark comparability: LIMITED

Exact independent replication: NOT ESTABLISHED

⸻

AI-001-BENCHMARK-01 — Scaling Neural Machine Translation

Source: Ott et al. (2018), Scaling Neural Machine Translation

Authors: Myle Ott, Sergey Edunov, David Grangier, and Michael Auli

Publication venue: Proceedings of the Third Conference on Machine Translation (WMT 2018)

DOI: 10.18653/v1/W18-6301

arXiv identifier: 1806.00187

Evidence type: Separate benchmark experiment

Origin ID: ott-2018-scaling-nmt

Model family: Transformer

Evaluation benchmark: WMT 2014 English-to-German

Training dataset: WMT 2016 English-to-German

Reported result: 29.3 BLEU

Reported hardware: 128 GPUs

Reported training duration: Approximately 85 minutes

Additional reported finding: The authors report matching the accuracy of Vaswani et al. using an accelerated training configuration.

Assessment:

Ott et al. describe a separately conducted Transformer training and evaluation study.

Their reported 29.3 BLEU result provides relevant external evidence that Transformer-based models can achieve strong performance on the WMT 2014 English-to-German benchmark.

However, their training procedures, optimization methods, and experimental conditions differ from the original study.

Their result should not be interpreted as an exact reproduction of the original 28.4 BLEU experiment.

Classification: RELATED EXTERNAL BENCHMARK EVIDENCE

Benchmark comparability: PARTIAL

Exact independent replication: NOT ESTABLISHED

Full independence assessment: PENDING

⸻

AI-001-REPLICATION-01 — Comparable Independent Replication

Source: Not yet established

Evidence type: Comparable independent replication

Origin ID: Pending

Model configuration: Pending

Training dataset: Pending

Evaluation dataset: Pending

BLEU scoring procedure: Pending

Reported result: Pending

Experimental independence: Pending

Comparability assessment: Pending

Status: NOT ESTABLISHED

This entry is a placeholder for a future source that satisfies the project’s replication criteria.

It must not be counted as completed evidence.

⸻

E. Evidence Inventory Summary

Evidence ID	Source	Classification	Exact replication
AI-001-SOURCE-01	Vaswani et al.	Original publication	No
AI-001-IMPLEMENTATION-01	Harvard NLP	Separate implementation	Not established
AI-001-BENCHMARK-01	Ott et al.	Related benchmark experiment	Not established
AI-001-REPLICATION-01	Pending	Comparable replication	Not established

Confirmed source records: 3

Placeholder replication records: 1

Exact independent replications established: 0

Independent reviewer assessments: 0

Final reference label: UNASSIGNED

ResearchOS prediction: NOT RUN

⸻

F. Outstanding Replication Tasks

* [x]	Identify a separate Transformer implementation.
* [x]	Identify a related external benchmark experiment.
* [x]	Document reported external benchmark performance.
* [x]	Record differences between original and external experiments.
* [ ]	Verify complete methodological comparability.
* [ ]	Establish independent reproduction of the exact original configuration.
* [ ]	Assess additional supporting evidence.
* [ ]	Assess contradictory evidence.
* [ ]	Submit the completed evidence package for independent review.

Replication Conclusion

The original 28.4 BLEU reporting statement is supported by the original publication.

A separate implementation and a related external benchmark experiment have been documented.

Exact independent replication has not been established.

No reviewer reference label has been assigned.

⸻

2.7 Independent Reviewer Assessment

Independent assessments must follow AI_REVIEWER_GUIDELINES.md.

At least two qualified reviewers are required.

Completed initial assessments must be submitted separately and preserved without alteration.

Reviewer 1

Reviewer ID: Pending

Qualifications: Pending

Relevant expertise: Pending

Conflict-of-interest declaration: Pending

Evidence reviewed: Pending

Claim version: Pending

Prediction blinding confirmed: Pending

Selected label: UNASSIGNED

Assessment rationale: Pending

Assessment date: Pending

Reviewer 2

Reviewer ID: Pending

Qualifications: Pending

Relevant expertise: Pending

Conflict-of-interest declaration: Pending

Evidence reviewed: Pending

Claim version: Pending

Prediction blinding confirmed: Pending

Selected label: UNASSIGNED

Assessment rationale: Pending

Assessment date: Pending

Permitted Labels

* ACCEPT
* REJECT
* UNCERTAIN

No reviewer label may be assigned without an actual independent assessment.

Current reviewer status: NOT COMPLETED

⸻

2.8 Adjudication

Reviewer 1 label: UNASSIGNED

Reviewer 2 label: UNASSIGNED

Reviewer agreement: NOT ASSESSED

Disagreement: NOT ASSESSED

Adjudicator ID: Pending

Adjudication evidence: Pending

Adjudication notes: Pending

Final reference label: UNASSIGNED

Reference dataset status: NOT FROZEN

Adjudication Requirements

If reviewers disagree:

1. Preserve their initial assessments.
2. Document the disagreement.
3. Examine relevant evidence and methodological differences.
4. Obtain additional independent review if necessary.
5. Record the adjudication decision and rationale.
6. Preserve unresolved uncertainty.

A final reference label must not be influenced by ResearchOS predictions.

Important: UNASSIGNED is a documentation placeholder, not a valid value of the ReferenceLabel enum.

⸻

2.9 ResearchOS Prediction

Claim ID: AI-001

Prediction status: NOT RUN

ResearchOS commit SHA: Pending

Input evidence version: Pending

Prediction configuration: Pending

Prediction timestamp: Pending

Observed outcome: UNASSIGNED

Evaluation status: NOT EVALUATED

Prediction Isolation

ResearchOS predictions must be generated without access to finalized reference labels or reviewer conclusions.

The evaluation process must preserve separate records for:

1. Claim and evidence inputs.
2. Independent reference assessments.
3. ResearchOS predictions.
4. Final evaluation results.

Reference labels and predictions must be frozen before they are compared.

Implementation note: The existing ResearchOS evaluation module compares supplied expected and observed outcomes. A separate, auditable procedure is still required to generate and freeze actual ResearchOS predictions.

No prediction should be fabricated or inferred from the expected label.

⸻

3. Independent Review Workflow

The following workflow applies to each candidate claim.

Stage 1 — Claim Registration

* Record the claim identifier.
* Record the exact claim wording.
* Assign a claim version.
* Record the original publication.

Stage 2 — Source Verification

* Examine the original publication.
* Locate the reported result.
* Document experimental conditions.
* Record evidence provenance.

Stage 3 — External Evidence Collection

* Identify independent implementations.
* Identify related benchmark experiments.
* Search for comparable replications.
* Document supporting and contradictory evidence.
* Assess source independence.

Stage 4 — Independent Reviewer Assessment

* Recruit qualified reviewers.
* Verify qualifications and conflicts.
* Provide a versioned evidence package.
* Obtain independent assessments.
* Preserve original reviewer labels and rationales.

Stage 5 — Adjudication

* Compare independent assessments.
* Document disagreements.
* Resolve disagreements when justified.
* Establish the final reference label.

Stage 6 — Reference Dataset Freeze

* Freeze claim wording and evidence versions.
* Freeze finalized reference labels.
* Record the dataset version and fingerprint.

Stage 7 — ResearchOS Classification

* Generate ResearchOS predictions separately.
* Record the software commit SHA.
* Record the input evidence version.
* Preserve the prediction output.

Stage 8 — Evaluation

* Compare frozen predictions with reference labels.
* Calculate evaluation metrics.
* Analyze classification errors.
* Document uncertainty and limitations.

⸻

4. Dataset Review Status

Claim ID	Evidence review	Independent reviewers	Reference label	ResearchOS prediction
AI-001	Primary-source verification completed; external evidence partial	Pending	Unassigned	Not run
AI-002	Not started	Pending	Unassigned	Not run
AI-003	Not started	Pending	Unassigned	Not run
AI-004	Not started	Pending	Unassigned	Not run
AI-005	Not started	Pending	Unassigned	Not run
AI-006	Not started	Pending	Unassigned	Not run
AI-007	Not started	Pending	Unassigned	Not run
AI-008	Not started	Pending	Unassigned	Not run
AI-009	Not started	Pending	Unassigned	Not run
AI-010	Not started	Pending	Unassigned	Not run

Dataset Summary

Candidate AI claims: 10

Claims with primary-source verification documented: 1

Claims with completed independent reviewer assessments: 0

Claims with finalized reference labels: 0

ResearchOS predictions generated: 0

Completed external evaluations: 0

⸻

5. Evidence Quality Requirements

Before a claim is submitted for final reference labeling, its evidence record should include:

* [ ]	Exact claim wording.
* [ ]	Claim version.
* [ ]	Original publication identifier.
* [ ]	Relevant source locations.
* [ ]	Experimental conditions.
* [ ]	Evidence provenance.
* [ ]	Independent-source classification.
* [ ]	Supporting evidence.
* [ ]	Contradictory evidence, or a documented search finding.
* [ ]	Known limitations.
* [ ]	Reviewer qualification records.
* [ ]	Independent reviewer assessments.
* [ ]	Adjudication record, if required.

Missing evidence must be recorded as missing.

Absence of evidence must not be presented as evidence of absence.

⸻

6. Reproducibility and Audit Requirements

The external validation process should preserve:

Item	Requirement
ResearchOS version	Commit SHA
Dataset version	Recorded
Claim version	Recorded
Evidence package version	Recorded
Source identifiers	Recorded
Reviewer assessments	Preserved
Reference labels	Frozen before comparison
Predictions	Generated separately
Evaluation configuration	Recorded
Dataset fingerprint	Recorded
Evaluation fingerprint	Recorded

Changes to claim wording, evidence selection, reference labels, or predictions must be documented.

Evaluation results must be reproducible from the frozen inputs.

⸻

7. Scientific Integrity Statement

The candidate dataset contains published AI research claims, not independently established scientific truths.

Original publications provide primary evidence of what their authors reported.

Separate implementations and related benchmark experiments can provide useful context without necessarily reproducing the original experimental result.

Independent validation requires qualified reviewers, documented reference labels, prediction isolation, and reproducible evaluation.

No external validation accuracy, false acceptance rate, false rejection rate, or reliability claim is justified before the evaluation has been completed.

The initial dataset of 10 claims is exploratory and cannot establish broad generalization across AI research.

⸻

8. Current Conclusions

AI-001

Original reported result: DOCUMENTED

Original publication: IDENTIFIED AND CHECKED

Experimental conditions: PARTIALLY DOCUMENTED

Separate implementation evidence: IDENTIFIED

Related external benchmark evidence: IDENTIFIED

Exact independent replication: NOT ESTABLISHED

Independent reviewers: PENDING

Final reference label: UNASSIGNED

ResearchOS prediction: NOT RUN

External validation: NOT COMPLETED

Overall ResearchOS v0.6 Status

The project has established an initial evidence-review framework and documented primary-source and contextual evidence for AI-001.

Independent scientific review and external performance evaluation remain outstanding.

Current status: AI-001 primary-source verification documented; external evidence review partial; independent validation pending.

⸻

9. Source References

Source 1 — Original Transformer Publication

Vaswani, A., et al. (2017).

Attention Is All You Need.

Advances in Neural Information Processing Systems.

arXiv:1706.03762

Primary evidence: Table 2 and Sections 5–6.

Source 2 — Separate Transformer Implementation

Rush, A. (2018).

The Annotated Transformer.

Harvard NLP.

Evidence category: Separate implementation and educational demonstration.

Source 3 — Related External Benchmark Experiment

Ott, M., Edunov, S., Grangier, D., and Auli, M. (2018).

Scaling Neural Machine Translation.

Proceedings of the Third Conference on Machine Translation.

DOI: 10.18653/v1/W18-6301

arXiv:1806.00187

Evidence category: Related external benchmark experiment.

⸻

End of AI Evidence Review — Version 0.2
