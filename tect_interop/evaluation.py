"""Matched four-condition study scoring; consumes observations, invents none."""
CONDITIONS = ('human', 'single_model', 'unstructured_agents', 'tect')


def score(rows):
    if not isinstance(rows, list) or not rows or len(rows) > 40000:
        raise ValueError('nonempty bounded observations required')
    tasks = {}
    for row in rows:
        if not isinstance(row, dict) or set(row) != {'task', 'condition', 'correct', 'accepted', 'seconds', 'reviewer_seconds'}:
            raise ValueError('exact observation fields required')
        if not isinstance(row['task'], str) or not row['task'] or row['condition'] not in CONDITIONS:
            raise ValueError('task and known condition required')
        if type(row['correct']) is not bool or type(row['accepted']) is not bool:
            raise ValueError('externally labeled correctness and acceptance booleans required')
        for field in ('seconds', 'reviewer_seconds'):
            import math
            value = row[field]
            if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
                raise ValueError('finite nonnegative measured durations required')
        group = tasks.setdefault(row['task'], {})
        if row['condition'] in group:
            raise ValueError('duplicate task-condition pair')
        group[row['condition']] = row
    if any(set(group) != set(CONDITIONS) for group in tasks.values()):
        raise ValueError('all four conditions required for every matched task')
    metrics = {}
    for condition in CONDITIONS:
        values = [group[condition] for group in tasks.values()]
        accepted = sum(r['accepted'] for r in values)
        valid = sum(r['accepted'] and r['correct'] for r in values)
        seconds = sum(r['seconds'] for r in values)
        metrics[condition] = {'tasks': len(values), 'accepted': accepted,
                              'false_acceptance_rate': (accepted-valid)/accepted if accepted else None,
                              'acceptance_coverage': accepted/len(values),
                              'validated_results_per_hour': valid*3600/seconds if seconds else None,
                              'reviewer_seconds_per_valid_result': sum(r['reviewer_seconds'] for r in values)/valid if valid else None}
    return {'schema_version': 1, 'metrics': metrics, 'independent_labels_authenticated': False,
            'statistical_significance_established': False,
            'scope': 'Descriptive matched observations; protocol, ground truth and reviewer identities require external validation'}
