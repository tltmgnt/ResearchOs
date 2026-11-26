import json
import subprocess
import sys
import unittest
from pathlib import Path


class MraBenchmarkTest(unittest.TestCase):
    def test_matched_synthetic_stage_accounting(self):
        script = Path(__file__).resolve().parents[1] / "tools/mra_x_controlled_benchmark.py"
        result = subprocess.run([sys.executable, str(script), "--repeats", "2"],
                                check=True, capture_output=True, text=True, timeout=30)
        report = json.loads(result.stdout)
        self.assertEqual(report["fixture_count"], 160)
        self.assertEqual(report["exact_disposition_and_candidate_packet_matches"], 160)
        self.assertEqual(report["baseline_executed_stages_per_trial"], 1120)
        self.assertEqual(report["gated_executed_stages_per_trial"], 700)
        self.assertEqual(report["executed_stage_reduction_fraction"], 0.375)
