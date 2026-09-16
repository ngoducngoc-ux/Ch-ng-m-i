#!/usr/bin/env python3
"""Minimal QC for SA-01 wide CSV before M0–M3 modeling.

Usage:
  python3 redcap_import_qc.py --demo          # uses synthetic_sa01_early_signal.csv
  python3 redcap_import_qc.py path/to/export.csv
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

REQUIRED = [
    "SUBJ_ID",
    "AGE",
    "WOUND_TYPE",
    "GROUP",
    "PCT_EPITH_D0",
    "PCT_EPITH_D3",
    "PCT_EPITH_D7",
    "PRIMARY_OUT_D21",
]


def qc(path: Path) -> list[str]:
    errors: list[str] = []
    df = pd.read_csv(path)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        errors.append(f"missing columns: {missing}")
    if "SUBJ_ID" in df.columns and df["SUBJ_ID"].duplicated().any():
        errors.append("duplicate SUBJ_ID")
    if "PRIMARY_OUT_D21" in df.columns:
        rate = df["PRIMARY_OUT_D21"].mean()
        if rate <= 0 or rate >= 1:
            errors.append(f"PRIMARY_OUT_D21 event rate out of (0,1): {rate}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", nargs="?", help="REDCap export (wide)")
    parser.add_argument("--demo", action="store_true", help="QC synthetic SA-01 output")
    args = parser.parse_args()
    if args.demo:
        path = Path(__file__).resolve().parent / "outputs" / "synthetic_sa01_early_signal.csv"
    elif args.csv:
        path = Path(args.csv)
    else:
        parser.error("provide csv path or --demo")
    if not path.is_file():
        print(f"QC FAIL: file not found {path}", file=sys.stderr)
        sys.exit(1)
    errors = qc(path)
    if errors:
        print("QC FAIL:", "; ".join(errors))
        sys.exit(1)
    print(f"QC PASS: {path} ({len(pd.read_csv(path))} rows)")


if __name__ == "__main__":
    main()
