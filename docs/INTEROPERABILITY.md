# TECT interoperability contract v0.1

## Authority and migration

`tect_runtime` in ResearchOs is the authoritative source for six shared Python modules listed in `core_release.json`. Domain repositories retain pinned vendored snapshots, verified by their conformance workflow. This prevents silent drift without silently changing existing `researchos` imports. `domain.py` remains repository-specific. Updates require an explicit release hash and commit change, local tests and CI. Use separate virtual environments because several domain packages expose the same legacy `researchos` import name.

The older ResearchOs `researchos.EpistemicController` API and the richer `tect_runtime.Controller` API are distinct. This release preserves both. It does not pretend a common import name makes their claim schemas interchangeable.

## Direction, units and meanings

| System / domain | Mathematical object | Dependency or quantity semantics | Boundary |
|---|---|---|---|
| TruthAi Registry | Typed dependency DAG | source depends on target | Local snapshot-bound review declarations |
| TECT runtime | Claim / evidence graph | source prerequisite, target dependent | Declared-policy epistemic state, no truth oracle |
| Geometry / TDA | Finite complex / Rips filtration | GF(2) homology; TDA coordinates supplied by caller | No arbitrary-space classification or population inference |
| Spatial / networks | Explicit undirected geographic / directed communication graph | Spatial approximate meters; networks synchronous rounds | Geometric crossings do not create edges; no async guarantee |
| Dynamics | Exact rational 2x2 discrete linear map | Per-step Schur/Jury criteria | No nonlinear or continuous-system theorem |
| Molecular | Explicit neutral atom/bond graph | Declared bond orders, valence ceilings, within-component distance | No implicit hydrogen, aromaticity, stereochemistry or energy |
| Physics / robotics / biology | Idealized SSH chain / 2D grid routes / context-scoped signed network | Each repository defines its units, conditions and approximation | No experiment, certified motion or clinical finding implied |

`tect_interop.contracts.dependency` reverses `depends_on` edges at the TruthAi boundary. It rejects `supports` and `contradicts`, which cannot be losslessly mapped by changing endpoint order. Other claim and evidence schemas require explicit versioned adapters; none is silently inferred.

## Source, identity and storage

`lineage` detects shared declared ancestors. Different ancestry roots do not prove independence. Content digests and byte-replay establish integrity, not source identity. Optional `attestation.verify` checks Ed25519 signatures against a caller-supplied, scoped, revocable trust map and binds claim version, policy version, evidence digest and validity interval. Key-owner identity remains an out-of-band responsibility. No self-supplied public key grants trust.

`EventStore` supports persistent append, restart, optimistic concurrency, transactional rollback and hash-chain consistency. It does not provide an externally anchored ledger, append-only enforcement against the database owner, encryption or multi-tenant authorization.

## Cross-repository execution

`tect_interop.demo` calls actual Spatial and Formal functions, checks formal certificates, records the byte digests in the actual TruthAi Registry, translates a dependency into the actual canonical TECT controller and demonstrates changed-input invalidation. Its deterministic graph is synthetic. Formal scenario labels come from the spatial analyzer: this is correlated evidence. All possible single static edge removals in this supplied graph are enumerated; arbitrary future outages, path lengths after failure, node failures and geographic truth are outside the checked claim.

`integration-lock.json` records the input revisions. TruthAi is private: public ResearchOs CI does not assume access to it. The integration job runs in TruthAi, checking out its own source and explicitly pinned public domain/core repositories. External users need authorized TruthAi source access to reproduce that full path.

## Evaluation and scientific limits

Existing `researchos.r3b` supports matched runners and paired statistics. `tect_interop.evaluation.score` adds a small exact observation schema requiring all four conditions for every task; zero-denominator metrics remain null. Synthetic tests validate software behavior only. Independent observers, blinded ground truth, frozen protocols, power analysis and real tasks are still needed before performance claims.

The concept paper's compact-state convergence statement needs qualification: strict decrease of a bounded potential alone does not imply finite-time arrival (for example, potential 1/n approaches zero without reaching it). Finite discrete states with strict descent support finite termination. Continuous/compact versions require additional progress and continuity assumptions and generally establish weaker limits. Robustness implies accepted-region preservation only when the metric, margin and perturbation bounds are compatible. Graph stability does not prove truth, and encoded governance invariants do not prove completeness or legal compliance.

## Outstanding external acceptance

Do not mark these completed using synthetic fixtures: independently recruited reproduction, measured four-condition domain study, real cloud/provider verification, externally established key custody and reviewer identity, clinical/facility/robot deployment authorization. Existing healthcare provider/security adapters are implementation assets; live-provider validation needs the authorized provider, environment, custody records and actual observations. No new spending or scheduled trigger is introduced here.
