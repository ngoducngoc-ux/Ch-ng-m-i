#!/usr/bin/env python3
"""Synthetic ICU pressure-ulcer data + M0–M3 AUROC demo for SA-05 early-signal.

Primary clinical endpoint in protocol: ΔPUSH D14 vs D0 (lower PUSH = better).
This sandbox predicts binary 'clinically meaningful improvement' at D14 from
D0–D7 signals. SYNTHETIC ONLY — not clinical evidence.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict

SEED = 20260916
N = 80
OUT_DIR = Path(__file__).resolve().parent / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def simulate(n: int = N, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    age = rng.integers(40, 85, size=n)
    stage = rng.integers(2, 5, size=n)
    group = rng.integers(1, 3, size=n)
    turn_adh = rng.integers(0, 3, size=n)  # 0 poor .. 2 full
    latent = (
        -0.02 * (age - 60)
        - 0.4 * (stage - 2)
        + 0.35 * (group == 1)
        + 0.3 * turn_adh
        + rng.normal(0, 1, n)
    )
    push_d0 = np.clip(10 - 1.2 * latent + rng.normal(0, 1.5, n), 3, 17)
    push_d3 = np.clip(push_d0 - 0.8 - 0.6 * latent + rng.normal(0, 1.0, n), 2, 17)
    push_d7 = np.clip(push_d3 - 1.0 - 0.7 * latent + rng.normal(0, 1.0, n), 1, 17)
    culture_d0 = np.clip(5.0 - 0.4 * latent + rng.normal(0, 0.6, n), 1.0, 8.0)
    culture_d3 = np.clip(culture_d0 - 0.5 - 0.3 * latent + rng.normal(0, 0.5, n), 0.5, 8.0)
    push_d14 = np.clip(push_d7 - 1.2 - 0.8 * latent + rng.normal(0, 1.1, n), 0, 17)
    delta = push_d14 - push_d0
    # Meaningful improvement: PUSH drops by >= 2 points
    y = (delta <= -2).astype(int)
    return pd.DataFrame(
        {
            "SUBJ_ID": [f"SA-05-{i:03d}" for i in range(1, n + 1)],
            "AGE": age,
            "STAGE_NPUAP": stage,
            "GROUP": group,
            "TURN_ADHERE": turn_adh,
            "PUSH_D0": push_d0.round(1),
            "PUSH_D3": push_d3.round(1),
            "PUSH_D7": push_d7.round(1),
            "PUSH_D14": push_d14.round(1),
            "DELTA_PUSH_D14": delta.round(1),
            "CULTURE_CFU_D0": culture_d0.round(2),
            "CULTURE_CFU_D3": culture_d3.round(2),
            "IMPROVED_D14": y,
        }
    )


def feature_sets(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    base = ["AGE", "STAGE_NPUAP", "GROUP", "PUSH_D0"]
    return {
        "M0": df[base],
        "M1": df[base + ["PUSH_D3", "PUSH_D7"]],
        "M2": df[base + ["PUSH_D3", "PUSH_D7", "CULTURE_CFU_D0", "CULTURE_CFU_D3"]],
        "M3": df[
            base
            + [
                "PUSH_D3",
                "PUSH_D7",
                "CULTURE_CFU_D0",
                "CULTURE_CFU_D3",
                "TURN_ADHERE",
            ]
        ],
    }


def eval_models(df: pd.DataFrame) -> pd.DataFrame:
    y = df["IMPROVED_D14"].to_numpy()
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    rows = []
    for name, X in feature_sets(df).items():
        clf = LogisticRegression(max_iter=2000)
        proba = cross_val_predict(clf, X, y, cv=cv, method="predict_proba")[:, 1]
        rows.append(
            {
                "model": name,
                "auroc": float(roc_auc_score(y, proba)),
                "brier": float(brier_score_loss(y, proba)),
                "n": int(len(df)),
                "event_rate": float(y.mean()),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    df = simulate()
    metrics = eval_models(df)
    data_path = OUT_DIR / "synthetic_sa05_early_signal.csv"
    metrics_path = OUT_DIR / "synthetic_sa05_m0_m3_metrics.json"
    df.to_csv(data_path, index=False)
    payload = {
        "note": "SYNTHETIC ONLY — not clinical evidence",
        "seed": SEED,
        "endpoint": "IMPROVED_D14 := (PUSH_D14 - PUSH_D0) <= -2",
        "metrics": metrics.to_dict(orient="records"),
    }
    metrics_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(metrics.to_string(index=False))
    print(f"wrote {data_path}")
    print(f"wrote {metrics_path}")


if __name__ == "__main__":
    main()
