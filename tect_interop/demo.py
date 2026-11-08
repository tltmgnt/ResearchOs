"""Real installed Spatial -> Formal -> TruthAi/TECT software integration.

Single static edge removal, undirected triangle, declared geographic coordinates.
The two analyzers check the same connectivity predicate by different algorithms.
This is correlated synthetic evidence, not independent real-world reproduction.
"""
import argparse
from dataclasses import replace
import hashlib
import json
from pathlib import Path
from .contracts import dependency
from .store import EventStore


NOW = '2026-11-08T12:00:00Z'
END = '2026-11-09T12:00:00Z'


def inputs(remove_direct=False):
    points = {'A': [0, 0], 'B': [0.01, 0], 'C': [0, 0.01]}
    features = [{'type': 'Feature', 'id': key, 'properties': {'kind': 'node'},
                 'geometry': {'type': 'Point', 'coordinates': point}} for key, point in points.items()]
    for source, target in [('A', 'B'), ('B', 'C')] + ([] if remove_direct else [('A', 'C')]):
        features.append({'type': 'Feature', 'id': source+target,
                         'properties': {'kind': 'edge', 'source': source, 'target': target},
                         'geometry': {'type': 'LineString', 'coordinates': [points[source], points[target]]}})
    policy = {'schema_version': 1, 'required_nodes': list(points), 'disabled_nodes': [],
              'disabled_edges': [], 'required_paths': [{'id': 'resilience', 'source': 'A', 'target': 'C',
               'max_distance_m': 100000, 'require_redundancy': True}]}
    return {'type': 'FeatureCollection', 'features': features}, policy


def analyze(data, policy):
    from spatial_topology.analysis import build_report as spatial
    from formal_topology.analysis import build_report as formal
    from formal_topology.certificates import check_certificates
    spatial_report = spatial(data, policy)
    edges = [f['id'] for f in data['features'] if f['properties']['kind'] == 'edge']
    # Each reachable state is either no outage or exactly one static edge outage.
    # Compute labels through actual spatial route analysis; formal checks exhaustively
    # quantify over this explicitly enumerated scenario set, not arbitrary failures.
    states = []
    for identifier, disabled in [('normal', [])] + [('loss-'+e, [e]) for e in edges]:
        result = spatial(data, dict(policy, disabled_edges=disabled,
                         required_paths=[dict(policy['required_paths'][0], require_redundancy=False)]))
        states.append({'id': identifier, 'labels': ['connected'] if result['status'] == 'REQUIREMENTS_SATISFIED' else []})
    model = {'schema_version': 1, 'initial': 'normal', 'propositions': ['connected'],
             'states': states, 'transitions': [{'id': 'choose-'+s['id'], 'source': 'normal', 'target': s['id']} for s in states]}
    requirements = {'schema_version': 1, 'required_states': [s['id'] for s in states],
                    'disabled_transitions': [], 'properties': [{'id': 'all-single-edge-outages', 'kind': 'invariant',
                    'predicate': {'atom': 'connected'}}]}
    formal_report = formal(model, requirements)
    certificates = check_certificates(model, requirements, formal_report['property_results'])
    return {'spatial': spatial_report, 'formal': formal_report, 'certificates': certificates,
            'model': model, 'requirements': requirements,
            'same_predicate_agrees': (spatial_report['status'] == 'REQUIREMENTS_SATISFIED') == (formal_report['status'] == 'OBLIGATIONS_HOLD')}


def run():
    from truthai_assurance import Artifact, Claim, Dependency, Registry
    from tect_runtime import Controller, policy_default
    from tect_runtime.pilot import receipt
    from tect_runtime.core import canonical
    before, after = analyze(*inputs()), analyze(*inputs(True))
    payload = canonical(before).encode()
    registry = Registry()
    artifact = Artifact('domain-results', hashlib.sha256(payload).hexdigest(), 'synthetic:actual-installed-analyzers',
                        'single static undirected edge failure', NOW, END)
    registry.add(artifact)
    registry.verify_artifact(artifact.id, payload, NOW)
    registry.add(Claim('resilience', 'spatial-formal', 'All enumerated single-edge outages preserve A-C connectivity',
                       artifact.scope, 'synthetic-author'))
    registry.link(Dependency('resilience', artifact.id))
    # This is deliberately a local declaration; the Registry reports identity unauthenticated.
    registry.review('resilience', 'synthetic-review-declaration', NOW, END)
    old_snapshot = registry.snapshot('resilience')
    affected = registry.replace(replace(artifact, sha256=hashlib.sha256(canonical(after).encode()).hexdigest()))
    registry.verify_artifact(artifact.id, canonical(after).encode(), NOW)
    status = registry.status('resilience', NOW)
    controller = Controller(policy_default(), NOW)
    for cid in ('source', 'conclusion'):
        controller.apply({'op': 'register', 'actor': 'author', 'data': {
            'id': cid, 'statement': 'Synthetic '+cid, 'provenance': ['local:installed-integration'],
            'confidence': 0.5, 'assurance_scope': artifact.scope}})
    translated = dependency({'source': 'conclusion', 'target': 'source', 'relation': 'depends_on'}, 'truthai', 'tect')
    controller.apply({'op': 'relation', 'actor': 'validator', 'data': translated})
    controller.apply({'op': 'evidence', 'actor': 'validator', 'data': receipt('source', 'real-function-results', before, independence=0.0)})
    controller.apply({'op': 'revise', 'actor': 'author', 'data': {'claim': 'source',
        'statement': 'Input changed: direct edge removed', 'provenance': ['local:changed-network'],
        'confidence': 0.5, 'assurance_scope': artifact.scope}})
    return {'schema_version': 1, 'before': before, 'after': after,
            'truthai': {'affected': affected, 'snapshot_changed': old_snapshot != registry.snapshot('resilience'), 'status': status},
            'tect': controller.report(), 'execution_authorized': False,
            'independent_reproduction': False, 'reviewer_identity_authenticated': False,
            'scope': 'Actual installed software calls on synthetic correlated inputs; no physical, scientific or production assurance'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--ledger', required=True)
    args = parser.parse_args()
    result = run()
    store = EventStore(args.ledger)
    try:
        revision = len(store.read())
        store.append({'operation': 'integration_run', 'report': result}, revision)
    finally:
        store.close()
    with Path(args.output).open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
    print(json.dumps({'report': args.output, 'execution_authorized': False}))


if __name__ == '__main__':
    main()
