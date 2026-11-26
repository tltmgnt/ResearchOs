"""Controlled synthetic comparison of fixed vs gated seven-stage review.
Both arms perform identical stage functions on matched records. No model calls,
real researcher comparison, operational optimization or scientific validation.
"""
import argparse
import json
import statistics
import time
from copy import deepcopy
from mra_x_tga import evaluate, example, digest


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False)


def cases():
    expected = {'valid': 'REVIEW_CANDIDATE', 'tampered': 'STOP', 'duplicate': 'STOP',
                'budget': 'STOP', 'missing_obligation': 'DECOMPOSE', 'refuted': 'RETIRE',
                'reopening': 'STOP', 'missing_evidence': 'DECOMPOSE'}
    for i in range(20):
        for name, disposition in expected.items():
            r = example()
            r['claim'] = f'synthetic {i} {name}'
            if name == 'tampered':
                r['evidence'][0]['sha256'] = '0' * 64
            elif name == 'duplicate':
                r['prior_claim_hashes'] = [digest(r['claim'])]
            elif name == 'budget':
                r['reserve']['calls'] = 5
            elif name == 'missing_obligation':
                r['obligations'] = []
            elif name == 'refuted':
                r['refuted'] = True
            elif name == 'reopening':
                r['new_hypothesis'] = False
            elif name == 'missing_evidence':
                r['evidence'] = []
            yield name, r, disposition


def run(record, gated):
    """Run real deterministic stages and count executed stages, not model calls."""
    stages = 0
    def stage(operation):
        nonlocal stages
        stages += 1
        return operation()
    record_hash = stage(lambda: digest(canonical(record)))
    evidence = stage(lambda: [digest(e['content']) for e in record['evidence']])
    resources = stage(lambda: {k: record['used'][k] + record['reserve'][k] for k in record['budget']})
    decision = stage(lambda: evaluate(record))
    if gated and decision['status'] != 'REVIEW_CANDIDATE':
        return decision, None, stages
    obligations = stage(lambda: [digest(x) for x in record['obligations']])
    proof_packet = stage(lambda: {'claim_hash': digest(record['claim']), 'record_hash': record_hash,
                                   'evidence_hashes': evidence, 'resource_plan': resources,
                                   'obligation_hashes': obligations})
    packet_hash = stage(lambda: digest(canonical(proof_packet)))
    return decision, packet_hash if decision['status'] == 'REVIEW_CANDIDATE' else None, stages


def benchmark(repeats=21):
    fixtures = list(cases())
    arms = {False: [], True: []}
    totals = {}
    results = {}
    for trial in range(repeats):
        for gated in ((False, True) if trial % 2 == 0 else (True, False)):
            start = time.perf_counter_ns()
            outputs = [run(r, gated) for _, r, _ in fixtures]
            arms[gated].append(time.perf_counter_ns() - start)
            decisions = [(a, b) for a, b, _ in outputs]
            if gated in results and results[gated] != decisions:
                raise AssertionError('nondeterministic output')
            results[gated] = decisions
            totals[gated] = sum(c for _, _, c in outputs)
    if results[False] != results[True]:
        raise AssertionError('review outcomes or candidate packets differ')
    for (_, _, expected), (decision, _) in zip(fixtures, results[True]):
        if decision['status'] != expected or decision['authorizes_execution'] or decision['theorem_promoted']:
            raise AssertionError('unexpected disposition or authority')
    return {'fixture_count': len(fixtures), 'categories': 8, 'repetitions': repeats,
            'exact_disposition_and_candidate_packet_matches': len(fixtures),
            'baseline_executed_stages_per_trial': totals[False],
            'gated_executed_stages_per_trial': totals[True],
            'executed_stage_reduction_fraction': 1 - totals[True] / totals[False],
            'baseline_median_ns_per_trial': statistics.median(arms[False]),
            'gated_median_ns_per_trial': statistics.median(arms[True]),
            'raw_baseline_ns': arms[False], 'raw_gated_ns': arms[True],
            'scope': 'matched synthetic deterministic software review only; not independent research or live model benchmarking'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repeats', type=int, default=21)
    args = parser.parse_args()
    if not 1 <= args.repeats <= 1000:
        parser.error('repeats must be between 1 and 1000')
    print(json.dumps(benchmark(args.repeats), indent=2))
