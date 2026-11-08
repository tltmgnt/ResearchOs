"""Synthetic software self-check adapter, not a scientific domain validator."""
from tect_interop.contracts import lineage


def check():
    configuration = {'origin': [], 'copy-a': ['origin'], 'copy-b': ['origin']}
    result = lineage(configuration)
    passed = ['copy-a', 'copy-b'] in result['shared_ancestry_pairs']
    return {'domain': 'declared-provenance-software',
            'statement': 'Two declared copies share their explicitly declared origin',
            'passed': passed, 'configuration': configuration, 'observed': result,
            'scope': 'Synthetic source-lineage self-check only; no source identity or scientific independence established'}
