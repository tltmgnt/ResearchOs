ResearchOS | TECT v0.6

AI Candidate Research Claims — Dataset v0.1

Domain: Artificial Intelligence
Status: Candidate collection — Not independently validated
Target: 10 claims
Collection date: 2026-10-30
Protocol: EXTERNAL_VALIDATION_PROTOCOL.md
Selection criteria: AI_EVALUATION_CRITERIA.md

1. Purpose

This document records 10 candidate claims from identifiable AI research publications.

Each claim describes a result reported by its original authors. Inclusion does not mean ResearchOS has verified the result.

All reference labels, reviewer assessments, and ResearchOS predictions remain unassigned.

2. Benchmark Performance Claims

AI-001 — Transformer Translation Performance

Source: Attention Is All You Need
Authors: Vaswani et al. (2017)
Identifier: arXiv:1706.03762
Category: Benchmark performance

Candidate claim: The Transformer model achieved a reported BLEU score of 28.4 on WMT 2014 English-to-German translation.

Metric: BLEU
Benchmark: WMT 2014 English-to-German
Reported result: 28.4 BLEU

Verification requirements: Confirm the evaluation configuration, tokenization, scoring procedure, and model variant.

Reference label: Pending independent review.

AI-002 — BERT GLUE Performance

Source: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
Authors: Devlin et al. (2019)
Identifier: arXiv:1810.04805
Category: Benchmark performance

Candidate claim: BERT achieved a reported GLUE score of 80.5.

Metric: GLUE aggregate score
Benchmark: GLUE
Reported result: 80.5

Verification requirements: Confirm the benchmark version, evaluation split, model configuration, and score aggregation.

Reference label: Pending independent review.

AI-003 — BERT Question Answering Performance

Source: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
Identifier: arXiv:1810.04805
Category: Benchmark performance

Candidate claim: BERT achieved a reported F1 score of 93.2 on SQuAD v1.1.

Metric: F1
Benchmark: SQuAD v1.1
Reported result: 93.2

Verification requirements: Confirm the model variant, evaluation split, preprocessing, and scoring procedure.

Reference label: Pending independent review.

AI-004 — FlashAttention Training Speed

Source: FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness
Authors: Dao et al. (2022)
Identifier: arXiv:2205.14135
Category: Benchmark performance

Candidate claim: FlashAttention produced a reported threefold training speedup on GPT-2 at sequence length 1,024 under the paper’s experimental conditions.

Metric: Training speedup
Benchmark: GPT-2 training experiment
Reported result: 3× speedup

Verification requirements: Confirm hardware, baseline implementation, sequence length, and measurement method.

Reference label: Pending independent review.

3. Model Comparison Claims

AI-005 — LoRA Parameter Efficiency

Source: LoRA: Low-Rank Adaptation of Large Language Models
Authors: Hu et al. (2021)
Identifier: arXiv:2106.09685
Category: Model comparison

Candidate claim: The authors reported that LoRA could reduce trainable parameters by a factor of 10,000 relative to full GPT-3 175B fine-tuning under the reported comparison.

Metric: Trainable parameter count
Reported result: Up to 10,000× reduction

Verification requirements: Confirm the compared configurations, parameter accounting, and experimental conditions.

Reference label: Pending independent review.

AI-006 — LoRA GPU Memory Comparison

Source: LoRA: Low-Rank Adaptation of Large Language Models
Identifier: arXiv:2106.09685
Category: Model comparison

Candidate claim: The authors reported that LoRA could reduce GPU memory requirements by approximately threefold compared with full GPT-3 175B fine-tuning under their stated conditions.

Metric: GPU memory requirements
Reported result: Approximately 3× reduction

Verification requirements: Confirm optimizer, precision, hardware, batch size, and baseline configuration.

Reference label: Pending independent review.

AI-007 — QLoRA Benchmark Comparison

Source: QLoRA: Efficient Finetuning of Quantized LLMs
Authors: Dettmers et al. (2023)
Identifier: arXiv:2305.14314
Category: Model comparison

Candidate claim: The authors reported that their Guanaco model reached 99.3% of ChatGPT’s performance level on the Vicuna benchmark under their evaluation methodology.

Metric: Relative benchmark performance
Benchmark: Vicuna
Reported result: 99.3% relative performance

Verification requirements: Examine evaluation methodology, judge reliability, model versions, and benchmark limitations.

Reference label: Pending independent review.

4. Reproducibility and Resource Claims

AI-008 — QLoRA Memory Feasibility

Source: QLoRA: Efficient Finetuning of Quantized LLMs
Identifier: arXiv:2305.14314
Category: Reproducibility

Candidate claim: The authors reported fine-tuning a 65-billion-parameter language model using a single 48 GB GPU.

Metric: Hardware memory feasibility
Reported configuration: 65B parameters; one 48 GB GPU

Verification requirements: Confirm quantization, optimizer, training configuration, hardware specifications, and independently reproducible implementation details.

Reference label: Pending independent review.

AI-009 — FlashAttention BERT Training Reproduction

Source: FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness
Identifier: arXiv:2205.14135
Category: Reproducibility

Candidate claim: The authors reported a 15% end-to-end wall-clock speedup on BERT-large training at sequence length 512 relative to their stated MLPerf 1.1 comparison.

Metric: End-to-end training time
Reported result: 15% speedup

Verification requirements: Examine baseline comparability, hardware, training configuration, and whether the result can be independently reproduced.

Reference label: Pending independent review.

AI-010 — GPT-3 Few-Shot Evaluation

Source: Language Models are Few-Shot Learners
Authors: Brown et al. (2020)
Identifier: arXiv:2005.14165
Category: Reproducibility

Candidate claim: The authors reported evaluating GPT-3 on few-shot tasks without task-specific gradient updates or fine-tuning, using text prompts containing instructions and demonstrations.

Evaluation property: Absence of task-specific gradient updates during few-shot evaluation

Verification requirements: Examine the paper’s evaluation procedures, prompt construction, model access limitations, and evidence needed to reproduce the experimental setup.

Reference label: Pending independent review.

5. Dataset Summary

Category	Claims
Benchmark performance	4
Model comparisons	3
Reproducibility	3
Total	10

Claims with completed independent review: 0

Claims with finalized reference labels: 0

ResearchOS predictions recorded: 0

External evaluation completed: No

6. Primary Publications

1. Vaswani et al. (2017). Attention Is All You Need. arXiv:1706.03762.
2. Devlin et al. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv:1810.04805.
3. Dao et al. (2022). FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. arXiv:2205.14135.
4. Hu et al. (2021). LoRA: Low-Rank Adaptation of Large Language Models. arXiv:2106.09685.
5. Dettmers et al. (2023). QLoRA: Efficient Finetuning of Quantized LLMs. arXiv:2305.14314.
6. Brown et al. (2020). Language Models are Few-Shot Learners. arXiv:2005.14165.

7. Required Independent Review

Before evaluating ResearchOS:

* [ ]	Check each claim against the identified paper version.
* [ ]	Confirm benchmark versions and experimental settings.
* [ ]	Record source locations and evidence provenance.
* [ ]	Apply inclusion and exclusion criteria.
* [ ]	Document reviewer qualifications and conflicts.
* [ ]	Obtain two independent assessments per claim.
* [ ]	Preserve reviewer disagreements.
* [ ]	Finalize reference labels through documented adjudication.
* [ ]	Generate ResearchOS predictions without reference-label access.
* [ ]	Calculate metrics and analyze errors.

8. Limitations

These claims were selected as candidates from original research publications. The reported figures and descriptions have not been independently reproduced.

Several claims come from the same publications and therefore should not be treated as statistically independent observations.

The reproducibility category contains claims suitable for reproduction-oriented assessment; it does not imply that independent replications have been completed.

A dataset of 10 claims cannot establish general reliability across AI research.

Current status: Candidate dataset assembled; independent external validation pending.
