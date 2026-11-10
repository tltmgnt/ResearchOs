"""Offline curriculum answer key. Synthetic checks, never operational approval."""
import ast
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
for base in (ROOT, ROOT / "src", ROOT / "layer-b"):
    sys.path.insert(0, str(base))
CASES = []

def check(name, actual, expected):
    passed = actual == expected
    CASES.append({"case": name, "actual": actual, "expected": expected, "passed": passed})
    if not passed:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")

def rejects(name, call, error=ValueError):
    try:
        call()
    except error:
        check(name, error.__name__, error.__name__)
    else:
        raise AssertionError(f"{name}: expected {error.__name__}")




def run():
    from tect_runtime.core import Controller, policy_default, state_distance
    c = Controller(policy_default(), "2026-11-08T12:00:00Z")
    op = {"op":"register","actor":"author","data":{"id":"c","statement":"Synthetic claim",
          "provenance":["fictional:source"],"confidence":.5,"assurance_scope":""}}
    check("registration", c.apply(op)["outcome"], "PASS")
    check("generated state", c.snapshot()["claims"]["c"]["state"], "GENERATED")
    before = c.snapshot()
    entry = c.apply({"op":"transition","actor":"validator","data":{"claim":"c","target":"ASSURED"}})
    check("cannot skip lifecycle stages", entry["outcome"], "FAIL")
    check("rejection leaves state unchanged", c.snapshot(), before)
    check("rejected operation stays in ledger", len(c.ledger), 2)
    check("adjacent initial transition", c.apply({"op":"transition","actor":"validator","data":{"claim":"c","target":"UNVERIFIED"}})["outcome"], "PASS")
    check("support without validation remains uncertain", c.apply({"op":"transition","actor":"validator","data":{"claim":"c","target":"SUPPORTED"}})["outcome"], "UNCERTAIN")
    altered = c.snapshot(); altered["claims"]["c"]["statement"] = "Different statement"
    check("projection omits statement changes: not a full-state metric", state_distance(c.snapshot(),altered), 0.0)
    check("report grants no execution", c.report()["execution_authorized"], False)

if __name__ == "__main__":
    if sys.argv[1:] not in ([], ["--verify"]):
        raise SystemExit("Usage: python curriculum/lab.py [--verify]")
    run()
    report = {"schema_version": 1, "status": "PASS", "case_count": len(CASES),
              "cases": CASES, "scope": "Synthetic curriculum checks only"}
    if sys.argv[1:] == ["--verify"]:
        expected = json.loads((Path(__file__).parent / "expected.json").read_text())
        if report != expected:
            raise AssertionError("Observed answers differ from curriculum/expected.json")
    print(json.dumps(report, sort_keys=True, indent=2, allow_nan=False))
