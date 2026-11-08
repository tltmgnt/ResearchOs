# Additional repository opportunities

Build after the shared core and one externally evaluated use case are stable. These are proposed names, not repositories created by this implementation. Check naming availability before creation; a new repository does not establish a new scientific contribution.

| Priority | Proposed repository | Concrete first release | Why it adds coverage |
|---|---|---|---|
| 1 | TruthAI-Causal-Inference-and-Intervention | Small structural causal models, interventions, confounding counterexamples, identification assumptions and reproducible synthetic benchmarks | Connectivity, correlation and claim support currently do not identify causal effects |
| 2 | TruthAI-Uncertainty-and-Calibration | Proper scoring rules, reliability diagrams, abstention, conformal coverage under explicit exchangeability assumptions, shift diagnostics | Current confidence/independence weights are policy inputs, not demonstrated calibrated probabilities |
| 3 | TruthAI-Independent-Benchmark-Lab | Frozen task datasets, ground-truth adjudication protocol, paired four-condition runs, reproducible result submissions | Existing runners need actual independently labeled observations and third-party replication |
| 4 | Topology-for-Time-Series-and-Change-Detection | Delay embeddings, persistence summaries, drift alerts and false-alarm evaluations on versioned signals | Static graph analyses do not characterize changing processes |
| 5 | Topology-for-Supply-Chains-and-Resource-Resilience | Multi-layer dependency graphs, constrained flow and bounded disruption scenarios | Adds capacities, inventory and recovery timing beyond unweighted connectivity |
| 6 | Topology-for-Climate-Water-and-Energy-Systems | One scoped watershed or microgrid simulation with units, conservation checks and uncertainty | Adds coupled physical infrastructure and climate stresses; needs domain expertise |
| 7 | Topology-for-Software-Dependencies-and-Security | SBOM import, transitive exposure, change impact and signed build provenance | Adds software supply-chain assurance distinct from scientific claim graphs |
| 8 | TruthAI-Human-Review-and-Collaboration | Reviewer assignment, disagreement resolution, conflict-of-interest records and measured review burden | Adds human workflow and independent adjudication rather than more generative agents |

## Keep inside existing repositories initially

Interoperability, the canonical state controller, evidence-lineage utilities and the platform index now belong in ResearchOs/TruthAi. Another generic OS or duplicated TECT core would increase maintenance without adding a separate experiment. Keep a new domain adapter in its existing domain repository until it has its own data, tests and acceptance criteria.

## Scientific and software integration references

Use established primary project interfaces rather than silently reimplementing their full scope: [DoWhy](https://www.pywhy.org/dowhy/), [GUDHI](https://gudhi.inria.fr/), [RDKit](https://www.rdkit.org/docs/), [NetworkX](https://networkx.org/documentation/stable/), and [RO-Crate](https://www.researchobject.org/ro-crate/). These are reference integration targets, not installed dependencies or claimed collaborators.

For every proposed repository, require one bounded question, a typed input/output contract, an independent oracle or benchmark, units and assumptions, a replayable evidence record, a license decision, and a clearly labeled external-validation gap before expanding scope.
