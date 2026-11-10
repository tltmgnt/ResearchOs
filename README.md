# ResearchOS / TECT

Research prototype for controlled, revisable acceptance of claims. Software checks and declared policy acceptance do not establish scientific truth or production authorization.

## Install and check

```sh
python -m pip install .
python -m unittest discover -s . -p 'test_*.py'
python -m unittest discover -s tests
```

`researchos` preserves the original small controller API. `tect_runtime` is the authoritative v0.1 source for the richer domain controllers; these APIs are distinct and are not silently substituted. `core_release.json` fingerprints its six shared modules. Domain repositories retain explicit, pinned snapshots plus their own domain adapters. See [interoperability](docs/INTEROPERABILITY.md), [portfolio](docs/portfolio/INDEX.md), and [new repository opportunities](docs/portfolio/NEW_REPOSITORIES.md).

`tect_interop` adds dependency-direction conversion, declared-source lineage, an optimistic-concurrency SQLite event store, descriptive matched-study scoring, and an actual installed cross-repository demonstration. It does not authenticate source identities or perform independent research evaluations.

The canonical pilot checks only declared source-lineage software. Select a domain repository for a scientific-domain adapter. `tect-runtime evaluate INPUT --output DIRECTORY` evaluates a supplied scenario; `tect-runtime verify DIRECTORY` replays it. A completed report can contain blocked gates and return a nonzero acceptance exit code.

## Cross-repository demonstration

Install the exact Spatial, Formal and TruthAi revisions in `integration-lock.json` into a separate virtual environment, then install this repository. Run:

```sh
python -m tect_interop.demo --output report.json --ledger events.sqlite
```

The test calls the real spatial and finite-state analyzers on one synthetic undirected graph. Removing an edge changes the finite verification result and reopens the TruthAi review and TECT dependent claim. Formal labels are computed by the spatial analyzer, so this is correlated software evidence, not independent reproduction. The ledger survives restart and rejects stale concurrent writes; its hashes do not prevent an owner rewriting the database.

[Legacy overview](README%202.md) records the original prototype. [TECT scope](docs/INTEROPERABILITY.md) explains mathematical and operational limits. No schedules, paid providers, broker execution or external messages are enabled by this change.

**∞**

## Topology compatibility and curriculum

See the [repository-specific v2 curriculum](docs/portfolio/TOPOLOGY_CURRICULUM_V2.md) for topology choices, worked explanations, a graded laboratory and adoption boundaries. Run the offline answer key from this repository root:\n\n```sh\npython curriculum/lab.py --verify\n```\n\n[Expected answers](curriculum/expected.json) · [Recorded local validation](curriculum/VALIDATION.json). The guide states any existing dependency needed for the lab.
