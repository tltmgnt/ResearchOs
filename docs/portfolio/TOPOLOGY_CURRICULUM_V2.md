# Topology compatibility and curriculum v2 — ResearchOs

The verified edition of version 2 adapts the explicit-molecular-graph teaching pattern to this repository's actual role. This edition adds executable learning checks and reviewed answer keys. It does not introduce a new topology engine or grant operational permission.

## Repository decision

| Question | Repository-specific answer |
| --- | --- |
| Architectural role | foundational controller |
| Minimum useful mathematics | Directed dependency graphs and finite-state transition systems |
| Relationships to preserve | Claim states, evidence dependencies and conservative invalidation |
| Concrete operation / capstone | Trace a supported claim, add a challenge and follow dependent reopening through the canonical controller |
| Necessity and scope boundary | Epistemic states are policy semantics; they are not automatically a mathematical topology or truth proof |

The decision is a source-based recommendation, not measured proof that a new specialty improves this repository. Start with the existing implementation and compare any proposed abstraction against a simpler alternative.

## Six-criterion compatibility scorecard

Complete one scorecard per proposed candidate and per concrete operation. Leave unmeasured entries unknown. Scores are human judgments from 0 (no fit) to 5 (strong evidenced fit); unknown is not zero. Do not sum an incomplete card. A total out of 30 is a heuristic, not adoption approval, and feasibility or necessity can veto a high total.

| Criterion | Score | Required evidence |
| --- | --- | --- |
| Structural compatibility | Not yet scored | Map the repository objects and the relationships above without losing direction, labels, units or missingness. |
| Transformation support | Not yet scored | Demonstrate the capstone operation on accepted and rejected inputs. |
| Invariant preservation | Not yet scored | State the property preserved and supply a counterexample or perturbation. |
| Computational feasibility | Not yet scored | Measure size, time and memory on bounded fixtures; record limits. |
| Integration compatibility | Not yet scored | Verify existing schemas, APIs and neighboring contracts remain compatible. |
| Mathematical necessity | Not yet scored | Compare with directed dependency graphs and finite-state transition systems and explain the additional capability, if any. |

## Curriculum

Prerequisites: basic programming, sets, functions and graph vocabulary. Work in six competency-gated sessions, approximately 60–90 minutes each; empirical evaluation is a separate research activity.

| Session | Learning objective | Exercise | Completion evidence |
| --- | --- | --- | --- |
| 1. Model | Identify claim states, evidence dependencies and conservative invalidation. | Draw a minimal valid example and one excluded relationship. | Annotated object/relation inventory with explicit assumptions. |
| 2. Contract | Distinguish schema validity from substantive correctness. | Trace validation and propose malformed, missing and boundary inputs. | Input-to-rejection table grounded in current source. |
| 3. Operation | Explain directed dependency graphs and finite-state transition systems. | Trace a supported claim, add a challenge and follow dependent reopening through the canonical controller. | Hand trace compared with existing software, or a clearly labeled specification when no runtime exists. |
| 4. Preservation | State what a transformation must preserve. | Rename identifiers, reorder records, then alter one meaningful relation; predict each effect under the actual contract. | Separate invariant, expected change and unsupported transformation. |
| 5. Comparison | Justify mathematical necessity and cost. | Complete the six-criterion card for the existing approach and one proposed alternative; record unknowns honestly. | Evidence-backed recommendation with baseline and explicit veto conditions. |
| 6. Reproduction | Communicate the bounded result. | Reproduce the capstone using existing offline fixtures and record software version, inputs, outputs and limitations. | Reviewable notebook or report distinguishing computation, replay, independent evaluation and authorization. |

## Worked reasoning and source explanation

Controller.apply() snapshots state before an operation and appends a ledger entry whether the operation passes or fails. A nonadjacent GENERATED→ASSURED request fails without changing the snapshot, but remains in the ledger. GENERATED→UNVERIFIED is adjacent and passes; UNVERIFIED→SUPPORTED without required validation is UNCERTAIN. That third outcome is a preserved evidence gap, not malformed input or scientific falsification. The state_distance projection also ignores statement changes: two different statements can have distance zero. It is not a metric on the complete claim state.

Read the [inspected source](https://github.com/tltmgnt/ResearchOs/blob/049ded90f6c1f3493115684e5fedb0729e3b85a2/tect_runtime/core.py) alongside the [executable answer key](../../curriculum/lab.py). The source link is pinned to the inspected revision; the lab and any explicitly described fix are in this change.

## Run the worked laboratory

From the repository root, with Python 3.12 (the recorded local version is 3.12.14):

```sh
python curriculum/lab.py --verify
```

The lab checks **9 explicit expectations** against existing repository functions. It prints a JSON case report and exits nonzero on a wrong result. `--verify` additionally compares the entire case report with [expected.json](../../curriculum/expected.json). Read the input and predict each result before opening the answer key. No API account, credentials, model download, trading action or equipment connection is needed.

| Checkpoint | Expected answer |
| --- | --- |
| registration | `"PASS"` |
| generated state | `"GENERATED"` |
| cannot skip lifecycle stages | `"FAIL"` |
| rejection leaves state unchanged | `{"claims": {"c": {"assurance_scope": "", "challenges": [], "confidence": 0.5, "id": "c", "last_validation_at": null, "provenance": ["fictional:source"], "reassessment_reasons": [], "state": "GENERATED", "statement": "Synthetic claim", "version": 1}}, "evidence": {}, "relations": [], "version": 1}` |
| rejected operation stays in ledger | `2` |
| adjacent initial transition | `"PASS"` |
| support without validation remains uncertain | `"UNCERTAIN"` |
| projection omits statement changes: not a full-state metric | `0.0` |
| report grants no execution | `false` |

The comparisons above encode independently specified small examples and contract expectations; a passing answer key is not evidence of complete domain correctness. The original functions and their existing test suites remain the authority for broader supported contracts.

## Learner tasks and assessment rubric

1. Before running the lab, predict every expected answer and derive one numeric result or state transition by hand.
2. Explain the worked reasoning above using the referenced source, including the rejected or counterexample case.
3. Add a new valid example and a nearby failing example. Explain which assumption changes, then compare against the existing implementation. For concept/static labs, keep the result explicitly at that level.
4. Complete the scorecard for a proposed extension and a simpler baseline. Leave measurements unknown until collected; a task that the baseline already solves is not evidence for additional topology.

| Competency | Points | Full-credit evidence |
| --- | --- | --- |
| Model and contract | 0–3 | Correct objects, relation direction, labels/units, input bounds and missingness. |
| Derivation and trace | 0–3 | Hand derivation agrees with the specified fixture; source steps explain why. |
| Counterexample | 0–3 | New failing/boundary case has a justified expected result; rejection is not suppressed. |
| Scope and necessity | 0–3 | Distinguishes software behavior from validation and compares an explicit simpler alternative. |

Completion requires at least 10/12 and no zero in scope/necessity. A runnable answer key alone is not evidence that a learner achieved this competency. No learner-outcome study has been performed.

## Verification evidence and maintenance

[VALIDATION.json](../../curriculum/VALIDATION.json) records the inspected base revision, local Python version, source/fixture hashes, lab/answer hashes, case count and exit codes. All cases were executed locally. An in-memory copy with a deliberately wrong comparison was also executed and returned nonzero, checking that the grading failure path is active. Those injected failures are harness checks, not scientific adversarial evaluations.

The dedicated [curriculum workflow](../../.github/workflows/curriculum.yml) runs the same `--verify` command on relevant pull-request changes. CI status is reported by GitHub; the local record does not assert that remote CI passed. Existing full-suite and installed-package requirements still apply to runtime changes. When source or fixture semantics change, inspect the diff and rederive answers before updating expected.json. Never regenerate expected answers solely to silence a failure. Refresh the local validation record after an actual run; do not rewrite its recorded base revision as if a new run occurred.

## Interoperability and adoption gate

Retain explicit domain contracts. Shared assurance records should refer to domain evidence and its assumptions rather than relabeling graph reachability, homology, statistical calibration and epistemic acceptance as interchangeable quantities. The canonical ResearchOs controller remains owned by ResearchOs; this curriculum does not create another controller fork.

Adopt additional mathematics only after a versioned experiment demonstrates a useful operation, the scorecard has evidence, the simpler baseline is inadequate and existing conformance checks remain satisfied. Epistemic states are policy semantics; they are not automatically a mathematical topology or truth proof.

## Portfolio curriculum index

Each repository carries its own decision, source reading and capstone. Links target the review branches for this coordinated documentation revision; after merge, use each repository's README link.

| Repository | Role | Minimum mathematics |
| --- | --- | --- |
| [Turn-Pro-trailblazer-agentic-system-](https://github.com/tltmgnt/Turn-Pro-trailblazer-agentic-system-/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application concept | Directed task graphs; defer topology libraries |
| [Next-Level-AI](https://github.com/tltmgnt/Next-Level-AI/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application concept | Ordinary dependency graphs; defer TDA |
| [TruthAi](https://github.com/tltmgnt/TruthAi/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | foundational platform | Typed directed graphs and explicit state transitions |
| [UTGA-DEFENSE-ENGINEER](https://github.com/tltmgnt/UTGA-DEFENSE-ENGINEER/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application concept | Typed dependency graphs; defer advanced topology |
| [hedgeops-dti-omega](https://github.com/tltmgnt/hedgeops-dti-omega/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application | Typed assessment/dependency graphs |
| [HospitalOS-TECT](https://github.com/tltmgnt/HospitalOS-TECT/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application | Typed evidence graphs and finite-state review logic |
| [Ai-debuting-project](https://github.com/tltmgnt/Ai-debuting-project/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application interface | Ordinary route and component dependency graphs |
| [Grok-HedgeOps-DTI](https://github.com/tltmgnt/Grok-HedgeOps-DTI/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application | Directed evidence/workflow graphs; bounded H0 shadow analysis where already implemented |
| [Healthcare-researchOS-Tect](https://github.com/tltmgnt/Healthcare-researchOS-Tect/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application infrastructure | Typed evidence graphs and versioned event histories |
| [dti-omega-hedgeops-omega](https://github.com/tltmgnt/dti-omega-hedgeops-omega/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application concept | Directed temporal dependency graphs; defer differential topology |
| [-Topological-Data-Analysis-for-Machine-Learning](https://github.com/tltmgnt/-Topological-Data-Analysis-for-Machine-Learning/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized mathematical tool | Computational algebraic topology: bounded Vietoris–Rips persistence |
| [-Topology-for-Networks-and-Distributed-Systems](https://github.com/tltmgnt/-Topology-for-Networks-and-Distributed-Systems/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized graph tool | Directed graph reachability; combinatorial topology only when an invariant is needed |
| [-Topology-in-Physics-and-Materials-Science](https://github.com/tltmgnt/-Topology-in-Physics-and-Materials-Science/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized physical model | Winding of the SSH Bloch loop plus finite-chain linear algebra |
| [ManufacturingOS](https://github.com/tltmgnt/ManufacturingOS/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application | Directed process/dependency graphs and finite-state failure models |
| [ResearchOs](https://github.com/tltmgnt/ResearchOs/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | foundational controller | Directed dependency graphs and finite-state transition systems |
| [QuantumOS](https://github.com/tltmgnt/QuantumOS/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application research | Typed claim graphs and stage transitions; defer new physical topology |
| [-Topology-for-Molecular-Structures-and-Chemistry](https://github.com/tltmgnt/-Topology-for-Molecular-Structures-and-Chemistry/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized graph tool | Labeled graph theory and cycle-space rank |
| [MathOS](https://github.com/tltmgnt/MathOS/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | foundational research workspace | Dependency graphs; TDA only for an explicitly defined representation study |
| [TruthAI-Benchmark-Lab](https://github.com/tltmgnt/TruthAI-Benchmark-Lab/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized evaluation | Directed graph reachability and matched benchmark design |
| [we-the-people-omega-layer-a](https://github.com/tltmgnt/we-the-people-omega-layer-a/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application research | Typed institutional dependency and event graphs |
| [-Topology-for-Geographic-and-Spatial-System](https://github.com/tltmgnt/-Topology-for-Geographic-and-Spatial-System/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized spatial tool | Graph connectivity/routing and explicit polygon predicates |
| [-Topology-for-Robotic-Motion-Planning](https://github.com/tltmgnt/-Topology-for-Robotic-Motion-Planning/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized planning tool | Configuration-space connectivity and bounded branch-cut route signatures |
| [ResearchOS-AI-Assisted-Biological-Research-Verification-Reproducibility-infrastructure](https://github.com/tltmgnt/ResearchOS-AI-Assisted-Biological-Research-Verification-Reproducibility-infrastructure/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application research | Typed provenance/dependency graphs |
| [TruthAI-Human-Review](https://github.com/tltmgnt/TruthAI-Human-Review/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized workflow | Directed assignment/review dependencies and explicit adjudication |
| [ResearchOS-Fusion](https://github.com/tltmgnt/ResearchOS-Fusion/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application research | Typed evidence graphs and finite-state assurance logic |
| [-United-Therapeutics-ResearchOS-Concept-](https://github.com/tltmgnt/-United-Therapeutics-ResearchOS-Concept-/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | application research | Acyclic claim dependencies and version-bound evidence graphs |
| [-Topology-for-Dynamical-Systems-and-Stability-Analysis](https://github.com/tltmgnt/-Topology-for-Dynamical-Systems-and-Stability-Analysis/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized dynamical tool | Exact rational linear algebra and discrete-time stability; no new differential topology required |
| [-Topology-for-Computation-and-Formal-Verification](https://github.com/tltmgnt/-Topology-for-Computation-and-Formal-Verification/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized verification tool | Directed finite-state graphs and temporal property checking |
| [UTGA-Omega-FT](https://github.com/tltmgnt/UTGA-Omega-FT/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | multi-domain research workspace | Separate per-domain graphs and explicit proposal contracts |
| [TruthAI-Uncertainty-and-Calibration](https://github.com/tltmgnt/TruthAI-Uncertainty-and-Calibration/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized evaluation | Probability/statistics first; no additional topology required |
| [-Topology-for-Geometry-and-Mathematical-Space-Classification](https://github.com/tltmgnt/-Topology-for-Geometry-and-Mathematical-Space-Classification/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized mathematical tool | Finite simplicial homology over GF(2) and combinatorial surface recognition |
| [-Topology-in-Biology-and-Medicine](https://github.com/tltmgnt/-Topology-in-Biology-and-Medicine/blob/curriculum/topology-compatibility-v2/docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) | specialized network tool | Directed signed graphs with scoped evidence qualification |

See the [executable portfolio lab index](CURRICULUM_LABS.md) for all pull requests, case counts and local validation records.
