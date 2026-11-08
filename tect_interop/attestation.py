"""Optional Ed25519 receipt verification against an explicitly supplied trust map.

Key ownership and real-world reviewer identity must be established out of band.
Never infer a trusted identity from an embedded key or self-signed declaration.
"""
import base64
from datetime import datetime, timezone
import hashlib
import json


def instant(value):
    if not isinstance(value, str):
        raise ValueError('UTC timestamp required')
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None or result.utcoffset().total_seconds() != 0:
        raise ValueError('UTC timestamp required')
    return result.astimezone(timezone.utc)


def signing_bytes(receipt):
    fields = {'schema_version', 'key_id', 'claim', 'claim_version', 'policy_version',
              'scope', 'evidence_sha256', 'issued_at', 'expires_at'}
    if not isinstance(receipt, dict) or set(receipt) != fields:
        raise ValueError('exact signed receipt fields required')
    if type(receipt['schema_version']) is not int or receipt['schema_version'] != 1 or type(receipt['claim_version']) is not int or receipt['claim_version'] < 1:
        raise ValueError('unsupported version')
    if any(not isinstance(receipt[k], str) or not receipt[k] for k in fields-{'schema_version', 'claim_version'}):
        raise ValueError('nonempty signed strings required')
    return json.dumps(receipt, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def verify(receipt, signature_base64, trust, evidence, *, claim, claim_version, policy_version, scope, now):
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    from cryptography.exceptions import InvalidSignature
    body = signing_bytes(receipt)
    if len(body) > 16384 or not isinstance(evidence, bytes):
        raise ValueError('bounded receipt and evidence bytes required')
    key = trust.get(receipt['key_id'])
    if not isinstance(key, dict) or set(key) != {'public_key_base64', 'revoked', 'scopes'} or key['revoked'] is not False or scope not in key['scopes']:
        raise ValueError('untrusted, revoked or out-of-scope key')
    if (receipt['claim'], receipt['claim_version'], receipt['policy_version'], receipt['scope']) != (claim, claim_version, policy_version, scope):
        raise ValueError('stale or mismatched subject/policy/scope')
    if not instant(receipt['issued_at']) <= instant(now) < instant(receipt['expires_at']):
        raise ValueError('receipt not current')
    if hashlib.sha256(evidence).hexdigest() != receipt['evidence_sha256']:
        raise ValueError('evidence digest mismatch')
    try:
        public = Ed25519PublicKey.from_public_bytes(base64.b64decode(key['public_key_base64'], validate=True))
        public.verify(base64.b64decode(signature_base64, validate=True), body)
    except (InvalidSignature, ValueError, TypeError) as exc:
        raise ValueError('invalid signature') from exc
    return {'signature_valid': True, 'trusted_key_id': receipt['key_id'],
            'real_world_identity_verified_by_this_function': False,
            'scientific_correctness_established': False}
