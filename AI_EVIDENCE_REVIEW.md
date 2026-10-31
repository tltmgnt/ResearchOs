ResearchOS | TECT v0.6

AI Evidence Review

Version: 0.1
Status: Evidence collection — Independent review pending
Branch: develop/tect-v0.6-external-validation
Protocol: EXTERNAL_VALIDATION_PROTOCOL.md
Candidate dataset: AI_CANDIDATE_CLAIMS.md

⸻

1. Purpose

This document records evidence gathered for AI research claims before independent reference labels are assigned.

It distinguishes:

1. Results reported by the original researchers.
2. Evidence confirmed through source inspection.
3. Independent reviewer assessments.
4. Final adjudicated reference labels.
5. ResearchOS predictions.

These stages must remain separate to prevent circular validation.

⸻

2. Evidence Record: AI-001

2.1 Claim Identification

Claim ID: AI-001

Category: Benchmark performance

Research area: Neural machine translation

Candidate claim:

The Transformer model achieved a reported BLEU score of 28.4 on WMT 2014 English-to-German translation.

Claim type: Historical reporting of an experimental result.

Important distinction: Confirming that a paper reports a score does not independently establish that the experimental result is correct or reproducible.

2.2 Original Publication

Title: Attention Is All You Need

Authors: Ashish Vaswani et al.

Publication year: 2017

Publication identifier: arXiv:1706.03762

Publication venue: Advances in Neural Information Processing Systems (NeurIPS 2017)

Source type: Original research publication

Evidence identifier: AI-001-SOURCE-01

Origin ID: vaswani-2017-transformer

Evidence status: Source identified; detailed verification pending.

2.3 Reported Experimental Result

### 2.3 Reported Experimental Result

| Field | Recorded information |
|---|---|
| Task | English-to-German machine translation |
| Benchmark | WMT 2014 |
| Test set | newstest2014 |
| Model | Transformer (big) |
| Reported metric | BLEU |
| Reported score | 28.4 |
| Comparison model | Transformer (base): 27.3 BLEU |
| Training hardware | 8 NVIDIA P100 GPUs |
| Reported training time | 3.5 days |
| Primary evidence location | Table 2 and Section 6.1 |
| Source verification | Original publication confirms reported score |
| Independent replication | Not yet assessed |

**Source verification finding:** The original NeurIPS 2017
publication reports 28.4 BLEU for Transformer (big) on
WMT 2014 English-to-German translation.

**Evidence limitation:** This verifies what the authors
reported. It does not independently reproduce the result.

**Reference label:** UNASSIGNED
2.4 Evidence Provenance

### 2.4 Evidence Provenance

**Primary publication:** Vaswani et al. (2017),
*Attention Is All You Need*.

**Publication identifier:** arXiv:1706.03762

**Evidence identifier:** AI-001-SOURCE-01

**Origin ID:** vaswani-2017-transformer

**Evidence locations:**
- Section 5.1: Training data and tokenization
- Section 5.2: Hardware and training schedule
- Table 2: Reported translation benchmark results
- Section 6.1: Model results and inference settings

**Confirmed source details:**
- Approximately 4.5 million training sentence pairs
- Byte-pair encoding with approximately 37,000 tokens
- Transformer (big) model
- 300,000 training steps
- Eight NVIDIA P100 GPUs
- Beam size 4
- Length penalty 0.6
- Averaging of the final 20 checkpoints
- Reported WMT 2014 English-German score: 28.4 BLEU

**Source verification status:** PRIMARY SOURCE INSPECTED

**Independent replication status:** NOT ASSESSED

**Independent reviewer status:** PENDING

**Final reference label:** UNASSIGNED

**Scientific limitation:**
The publication confirms what the original authors reported.
It does not independently establish reproducibility or
validate the reported performance.
2.5 Verification Checklist

* [ ]	Original publication accessed.
* [ ]	Exact result located in the publication.
* [ ]	Model variant confirmed.
* [ ]	Benchmark and test split confirmed.
* [ ]	BLEU calculation method examined.
* [ ]	Experimental conditions recorded.
* [ ]	Independent replication evidence searched.
* [ ]	Supporting evidence documented.
* [ ]	Contradictory evidence documented.
* [ ]	Evidence limitations summarized.

2.6 Known Evaluation Risks

### 2.6 Evidence Limitations and Evaluation Risks

**1. Original-source dependence**

The original publication is primary evidence of what its
authors reported, not independent confirmation of the result.

**2. BLEU scoring sensitivity**

BLEU scores depend on tokenization, preprocessing,
reference translations, and scoring implementation.

An independent reproduction must document these settings.

**3. Model configuration**

The reported 28.4 BLEU result applies to Transformer (big).

Results from Transformer (base) must not be substituted.

**4. Dataset consistency**

An independent evaluation must identify the WMT 2014
English-to-German test set and verify that its evaluation
data are comparable to those used in the original study.

**5. Training reproducibility**

Relevant factors include:
- Training data and preprocessing
- Model architecture and hyperparameters
- Training duration
- Hardware and software environment
- Random seeds
- Checkpoint selection and averaging

**6. Independent evidence**

Additional publications repeating the original score
do not constitute independent replication.

A replication should document a separately executed
experiment and its relationship to the original work.

**7. Claim interpretation**

AI-001 states that the original authors reported
28.4 BLEU.

Verification of that historical reporting statement
is distinct from verification that the model reliably
achieves 28.4 BLEU under reproducible conditions.

**8. Reference-label integrity**

Independent reviewers must assess the precise claim
defined in the dataset.

They must not silently reinterpret a reporting claim
as a reproducibility claim.

**Current assessment:**
Primary-source reporting documented.
Independent replication not assessed.
Reviewer labels unassigned.

2.7 Independent Reviewer Assessment

Reviewer 1

* Reviewer ID: Pending
* Qualifications: Pending
* Conflict-of-interest declaration: Pending
* Evidence reviewed: Pending
* Label: Pending
* Rationale: Pending

Reviewer 2

* Reviewer ID: Pending
* Qualifications: Pending
* Conflict-of-interest declaration: Pending
* Evidence reviewed: Pending
* Label: Pending
* Rationale: Pending

Permitted labels: ACCEPT, REJECT, UNCERTAIN.

No reviewer label may be assigned without an actual independent assessment.

2.8 Adjudication

Reviewer agreement: Not assessed

Disagreement: Not assessed

Adjudication notes: Pending

Final reference label: UNASSIGNED

Important: UNASSIGNED is a documentation placeholder, not a value of the ReferenceLabel enum.

2.9 ResearchOS Prediction

Prediction: NOT RUN

ResearchOS commit SHA: Pending

Input evidence version: Pending

Prediction timestamp: Pending

Evaluation status: NOT EVALUATED

ResearchOS predictions must be generated without access to finalized reference labels.

⸻

3. Review Workflow

For each candidate claim:

1. Identify the original publication.
2. Locate the exact reported result.
3. Record relevant experimental conditions.
4. Collect additional supporting or contradictory evidence.
5. Document evidence provenance and shared origins.
6. Obtain independent reviewer assessments.
7. Adjudicate disagreements.
8. Freeze the reference dataset.
9. Generate ResearchOS predictions separately.
10. Compare predictions with reference labels.

4. Dataset Review Status

Claim ID	Evidence review	Independent reviewers	Reference label
AI-001	In progress	Pending	Unassigned
AI-002	Not started	Pending	Unassigned
AI-003	Not started	Pending	Unassigned
AI-004	Not started	Pending	Unassigned
AI-005	Not started	Pending	Unassigned
AI-006	Not started	Pending	Unassigned
AI-007	Not started	Pending	Unassigned
AI-008	Not started	Pending	Unassigned
AI-009	Not started	Pending	Unassigned
AI-010	Not started	Pending	Unassigned

⸻

5. Scientific Integrity Statement

The candidate dataset contains published research claims, not independently established scientific truths.

Original publications provide primary evidence of what their authors reported.

Independent validation requires additional evidence assessment, qualified reviewers, and separation between reference labels and ResearchOS predictions.

No external validation accuracy or reliability claims are justified at this stage.

⸻

Current status: AI-001 evidence-review structure established. Detailed source verification and independent review remain pending.
