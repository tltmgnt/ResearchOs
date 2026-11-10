# Topology compatibility and curriculum v2 — ResearchOs

Version 2 adapts the explicit-molecular-graph teaching pattern to this repository's actual role. This is documentation and a learning/decision framework; it introduces no mathematical engine, runtime dependency or operational permission.

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

## Source-linked reading laboratory

The table is a guided selection of source lines, not an assertion that the whole repository is covered. Line numbers refer to the inspected source blob `6eeb933cfcd4ebb547a8cb87006a6307ee307499` in [tect_runtime/core.py](../../tect_runtime/core.py). Recheck anchors after source changes.

| Line | Statement | Learning check |
| --- | --- | --- |
| [16](../../tect_runtime/core.py#L16) | `def canonical(value):` | State the input/output contract and trace one normal and one failing case. |
| [17](../../tect_runtime/core.py#L17) | `return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False)+'\n'` | Predict the returned value and distinguish a computed result from authorization. |
| [20](../../tect_runtime/core.py#L20) | `def digest(value): return hashlib.sha256(canonical(value).encode()).hexdigest()` | State the input/output contract and trace one normal and one failing case. |
| [23](../../tect_runtime/core.py#L23) | `def text(value):` | State the input/output contract and trace one normal and one failing case. |
| [25](../../tect_runtime/core.py#L25) | `raise ValueError('Expected a trimmed nonempty string of at most 4096 characters')` | Construct the triggering input and explain why rejection preserves the contract. |
| [26](../../tect_runtime/core.py#L26) | `return value` | Predict the returned value and distinguish a computed result from authorization. |
| [29](../../tect_runtime/core.py#L29) | `def unit(value):` | State the input/output contract and trace one normal and one failing case. |
| [31](../../tect_runtime/core.py#L31) | `raise ValueError('Expected a finite number in [0,1]')` | Construct the triggering input and explain why rejection preserves the contract. |
| [32](../../tect_runtime/core.py#L32) | `return float(value)` | Predict the returned value and distinguish a computed result from authorization. |
| [35](../../tect_runtime/core.py#L35) | `def date(value):` | State the input/output contract and trace one normal and one failing case. |
| [38](../../tect_runtime/core.py#L38) | `if result.tzinfo is None: raise ValueError('Timestamps require a timezone')` | Construct the triggering input and explain why rejection preserves the contract. |
| [39](../../tect_runtime/core.py#L39) | `return result` | Predict the returned value and distinguish a computed result from authorization. |
| [42](../../tect_runtime/core.py#L42) | `def fields(obj,required,optional=()):` | State the input/output contract and trace one normal and one failing case. |
| [44](../../tect_runtime/core.py#L44) | `raise ValueError('Missing or unknown fields')` | Construct the triggering input and explain why rejection preserves the contract. |
| [47](../../tect_runtime/core.py#L47) | `def policy_default():` | State the input/output contract and trace one normal and one failing case. |
| [48](../../tect_runtime/core.py#L48) | `return {'actors':{'author':['author'],'validator':['validator'],'adversary':['adversary'],` | Predict the returned value and distinguish a computed result from authorization. |
| [54](../../tect_runtime/core.py#L54) | `class Controller:` | State the input/output contract and trace one normal and one failing case. |
| [60](../../tect_runtime/core.py#L60) | `def __init__(self, policy, as_of):` | State the input/output contract and trace one normal and one failing case. |
| [62](../../tect_runtime/core.py#L62) | `if not isinstance(policy['actors'],dict) or not policy['actors']: raise ValueError('Actors required')` | Construct the triggering input and explain why rejection preserves the contract. |
| [67](../../tect_runtime/core.py#L67) | `raise ValueError('Unknown actor role')` | Construct the triggering input and explain why rejection preserves the contract. |
| [69](../../tect_runtime/core.py#L69) | `if policy['minimum_density']<=0 or policy['epsilon']<=0: raise ValueError('Positive thresholds required')` | Construct the triggering input and explain why rejection preserves the contract. |
| [70](../../tect_runtime/core.py#L70) | `if type(policy['minimum_groups']) is not int or not 1<=policy['minimum_groups']<=16: raise ValueError('Invalid minimum_groups')` | Construct the triggering input and explain why rejection preserves the contract. |
| [72](../../tect_runtime/core.py#L72) | `raise ValueError('Nonempty unique registered attack classes required')` | Construct the triggering input and explain why rejection preserves the contract. |
| [73](../../tect_runtime/core.py#L73) | `if not isinstance(policy['required_validations'],list) or not policy['required_validations'] or len(set(policy['required_validations']))!=len(policy['required_validations']): raise ValueError('Unique required validation methods required')` | Construct the triggering input and explain why rejection preserves the contract. |
## Assessment and verification

A learner must explain the model, trace the capstone, identify a counterexample and state the scope boundary. Assess these four competencies equally; a numerical score cannot compensate for an unsupported scientific or operational claim.

Relevant existing checks:

- [tests/test_attestation.py](../../tests/test_attestation.py)
- [tests/test_cross_repository.py](../../tests/test_cross_repository.py)
- [tests/test_interop.py](../../tests/test_interop.py)

Follow [README](../../README.md) for environment and installed-package instructions. Read scripts before execution; source-reading exercises do not authorize provider calls, model downloads, live orders, hardware actions or messages. Synthetic fixtures establish software behavior only. This documentation change does not report those exercises as already executed.

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
