import base64
import hashlib
import importlib.util
import unittest
from tect_interop.attestation import signing_bytes, verify


@unittest.skipUnless(importlib.util.find_spec('cryptography'), 'Install the signatures extra')
class SignatureTests(unittest.TestCase):
    def test_signature_binding_revocation_and_staleness(self):
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
        key = Ed25519PrivateKey.generate()
        receipt = {'schema_version': 1, 'key_id': 'test-only', 'claim': 'c', 'claim_version': 1,
                   'policy_version': '1', 'scope': 'fixture', 'evidence_sha256': hashlib.sha256(b'data').hexdigest(),
                   'issued_at': '2026-11-08T00:00:00Z', 'expires_at': '2026-11-09T00:00:00Z'}
        signature = base64.b64encode(key.sign(signing_bytes(receipt))).decode()
        trust = {'test-only': {'public_key_base64': base64.b64encode(key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)).decode(),
                               'revoked': False, 'scopes': ['fixture']}}
        options = dict(claim='c', claim_version=1, policy_version='1', scope='fixture', now='2026-11-08T12:00:00Z')
        self.assertTrue(verify(receipt, signature, trust, b'data', **options)['signature_valid'])
        for override in ({'claim_version': 2}, {'policy_version': '2'}, {'now': '2026-11-10T00:00:00Z'}):
            with self.assertRaises(ValueError): verify(receipt, signature, trust, b'data', **dict(options, **override))
        with self.assertRaises(ValueError): verify(receipt, signature, trust, b'changed', **options)
        changed = dict(receipt, claim='different')
        with self.assertRaises(ValueError): verify(changed, signature, trust, b'data', **dict(options, claim='different'))
        trust['test-only']['revoked'] = True
        with self.assertRaises(ValueError): verify(receipt, signature, trust, b'data', **options)
