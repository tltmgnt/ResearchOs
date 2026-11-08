"""SQLite event persistence with optimistic concurrency and corruption detection.

Hashes detect accidental edits; a database owner can rewrite the entire chain.
This is not an externally anchored or authenticated ledger.
"""
import hashlib
import json
import sqlite3


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


class EventStore:
    def __init__(self, path):
        self.connection = sqlite3.connect(path, isolation_level=None, timeout=5)
        self.connection.execute('CREATE TABLE IF NOT EXISTS events (revision INTEGER PRIMARY KEY, body TEXT NOT NULL, previous TEXT NOT NULL, digest TEXT NOT NULL)')

    def close(self):
        self.connection.close()

    def read(self):
        result, previous = [], '0' * 64
        for revision, body, parent, digest in self.connection.execute('SELECT revision,body,previous,digest FROM events ORDER BY revision'):
            expected = hashlib.sha256((previous + body).encode()).hexdigest()
            if revision != len(result) + 1 or parent != previous or expected != digest:
                raise ValueError('event chain corruption')
            result.append(json.loads(body))
            previous = digest
        return result

    def append(self, event, expected_revision):
        if type(expected_revision) is not int or expected_revision < 0 or not isinstance(event, dict):
            raise ValueError('event object and nonnegative integer revision required')
        body = encode(event)
        if len(body.encode()) > 1048576:
            raise ValueError('event limit exceeded')
        self.connection.execute('BEGIN IMMEDIATE')
        try:
            current = self.read()
            if len(current) != expected_revision:
                raise ValueError('stale revision')
            row = self.connection.execute('SELECT digest FROM events ORDER BY revision DESC LIMIT 1').fetchone()
            previous = row[0] if row else '0' * 64
            digest = hashlib.sha256((previous + body).encode()).hexdigest()
            self.connection.execute('INSERT INTO events VALUES (?,?,?,?)', (expected_revision + 1, body, previous, digest))
            self.connection.execute('COMMIT')
        except BaseException:
            self.connection.execute('ROLLBACK')
            raise
        return expected_revision + 1
