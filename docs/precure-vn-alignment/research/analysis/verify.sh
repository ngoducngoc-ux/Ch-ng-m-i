#!/usr/bin/env bash
# Verify Precure analysis sandboxes still run.
set -euo pipefail
ANA="$(cd "$(dirname "$0")" && pwd)"
cd "$ANA"
python3 sa01_early_signal_synthetic_m0_m3.py >/tmp/precure_sa01_verify.out
python3 sa05_early_signal_synthetic_m0_m3.py >/tmp/precure_sa05_verify.out
python3 sa02_early_signal_synthetic_m0_m3.py >/tmp/precure_sa02_verify.out
python3 redcap_import_qc.py --demo
test -f outputs/synthetic_m0_m3_metrics.json
test -f outputs/synthetic_sa05_m0_m3_metrics.json
test -f outputs/synthetic_sa02_m0_m3_metrics.json
python3 -c 'import json; from pathlib import Path
paths=["outputs/synthetic_m0_m3_metrics.json","outputs/synthetic_sa05_m0_m3_metrics.json","outputs/synthetic_sa02_m0_m3_metrics.json"]
for p in paths:
 d=json.loads(Path(p).read_text()); assert d.get("note","").startswith("SYNTHETIC"); assert len(d["metrics"])==4; print(p,"OK",[m["model"] for m in d["metrics"]])'
echo "PRECURE verify: PASS"
