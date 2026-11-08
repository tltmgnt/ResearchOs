"""Versioned dependency direction and conservative source-lineage analysis."""
import hashlib
import json
from pathlib import Path


def dependency(edge, source_system, target_system):
    """Convert depends_on only; TruthAi dependent->prerequisite, TECT reverse."""
    systems = {'truthai', 'tect'}
    if source_system not in systems or target_system not in systems:
        raise ValueError('unknown system')
    if not isinstance(edge, dict) or set(edge) != {'source', 'target', 'relation'}:
        raise ValueError('exact dependency fields required')
    if edge['relation'] != 'depends_on':
        raise ValueError('support and contradiction require separate semantics')
    if any(not isinstance(edge[k], str) or not edge[k].strip() for k in ('source', 'target')) or edge['source'] == edge['target']:
        raise ValueError('distinct nonempty endpoints required')
    result = dict(edge)
    if source_system != target_system:
        result['source'], result['target'] = edge['target'], edge['source']
    return result


def lineage(sources):
    """Cluster declared shared ancestry, never assert statistical independence."""
    if not isinstance(sources, dict) or len(sources) > 256:
        raise ValueError('bounded source map required')
    for key, parents in sources.items():
        if not isinstance(key, str) or not key or not isinstance(parents, list) or any(not isinstance(p, str) or p not in sources for p in parents):
            raise ValueError('known source ancestry required')
    roots, visiting = {}, set()
    def visit(key):
        if key in visiting:
            raise ValueError('ancestry cycle')
        if key not in roots:
            visiting.add(key)
            roots[key] = set().union(*(visit(p) for p in sources[key])) if sources[key] else {key}
            visiting.remove(key)
        return roots[key]
    for key in sources:
        visit(key)
    pairs = [[a, b] for a in sorted(sources) for b in sorted(sources) if a < b and roots[a] & roots[b]]
    return {'roots': {k: sorted(v) for k, v in sorted(roots.items())},
            'shared_ancestry_pairs': pairs, 'statistical_independence_established': False,
            'scope': 'Declared lineage only; distinct roots can still be correlated or falsely declared'}


def check_snapshot(directory, release):
    """Check explicit vendored bytes against an authoritative release manifest."""
    directory = Path(directory)
    if release.get('schema_version') != 1 or not isinstance(release.get('modules'), dict):
        raise ValueError('unsupported release')
    mismatches = []
    for name, expected in release['modules'].items():
        if Path(name).name != name or not name.endswith('.py'):
            raise ValueError('module basename required')
        path = directory / name
        if path.is_symlink() or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            mismatches.append(name)
    return {'conforms': not mismatches, 'mismatches': mismatches,
            'release_version': release['version'], 'authenticity_established': False}
