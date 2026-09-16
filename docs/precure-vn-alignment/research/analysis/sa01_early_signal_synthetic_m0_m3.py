#!/usr/bin/env python3
"""Synthetic longitudinal wound data + M0–M3 AUROC demo for SA-01 early-signal.

NOT clinical evidence. Seeds a reproducible sandbox so the exploratory SAP
can be exercised before real REDCap exports exist.
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
N = 120
OUT_DIR = Path(__file__).resolve().parent / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def simulate(n: int = N, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    age = rng.integers(18, 71, size=n)
    wound_type = rng.integers(1, 5, size=n)
    group = rng.integers(1, 3, size=n)
    # Latent healing capacity
    latent = (
        -0.03 * (age - 45)
        - 0.35 * (wound_type >= 3)
        + 0.25 * (group == 1)
        + rng.normal(0, 1, n)
    )
    pct_d0 = np.clip(35 + 8 * latent + rng.normal(0, 8, n), 0, 95)
    pct_d3 = np.clip(pct_d0 + 12 + 4 * latent + rng.normal(0, 6, n), 0, 98)
    pct_d7 = np.clip(pct_d3 + 15 + 5 * latent + rng.normal(0, 6, n), 0, 99)
    culture_d0 = np.clip(5.5 - 0.6 * latent + rng.normal(0, 0.7, n), 1.0, 8.0)
    culture_d7 = np.clip(culture_d0 - 0.8 - 0.4 * latent + rng.normal(0, 0.5, n), 0.5, 8.0)
    vas_d0 = np.clip(6 - 0.4 * latent + rng.normal(0, 1.2, n), 0, 10)
    vas_d7 = np.clip(vas_d0 - 1.5 - 0.3 * latent + rng.normal(0, 1.0, n), 0, 10)
    # Outcome: complete re-epithelialization at D21
    logit = (
        -1.2
        + 0.045 * pct_d7
        - 0.35 * culture_d7
        - 0.12 * vas_d7
        + 0.35 * (group == 1)
        + rng.normal(0, 0.5, n)
    )
    prob = 1 / (1 + np.exp(-logit))
    y = (rng.random(n) < prob).astype(int)
    return pd.DataFrame(
        {
            "SUBJ_ID": [f"SA-01-{i:03d}" for i in range(1, n + 1)],
            "AGE": age,
            "WOUND_TYPE": wound_type,
            "GROUP": group,
            "PCT_EPITH_D0": pct_d0.round(1),
            "PCT_EPITH_D3": pct_d3.round(1),
            "PCT_EPITH_D7": pct_d7.round(1),
            "CULTURE_CFU_D0": culture_d0.round(2),
            "CULTURE_CFU_D7": culture_d7.round(2),
            "VAS_DRESS_D0": vas_d0.round(1),
            "VAS_DRESS_D7": vas_d7.round(1),
            "PRIMARY_OUT_D21": y,
        }
    )


def feature_sets(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    base = ["AGE", "WOUND_TYPE", "GROUP", "PCT_EPITH_D0"]
    return {
        "M0": df[base],
        "M1": df[base + ["PCT_EPITH_D3", "PCT_EPITH_D7"]],
        "M2": df[base + ["PCT_EPITH_D3", "PCT_EPITH_D7", "CULTURE_CFU_D0", "CULTURE_CFU_D7"]],
        "M3": df[
            base
            + [
                "PCT_EPITH_D3",
                "PCT_EPITH_D7",
                "CULTURE_CFU_D0",
                "CULTURE_CFU_D7",
                "VAS_DRESS_D0",
                "VAS_DRESS_D7",
            ]
        ],
    }


def eval_models(df: pd.DataFrame) -> pd.DataFrame:
    y = df["PRIMARY_OUT_D21"].to_numpy()
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
    data_path = OUT_DIR / "synthetic_sa01_early_signal.csv"
    metrics_path = OUT_DIR / "synthetic_m0_m3_metrics.json"
    df.to_csv(data_path, index=False)
    payload = {
        "note": "SYNTHETIC ONLY — not clinical evidence",
        "seed": SEED,
        "metrics": metrics.to_dict(orient="records"),
    }
    metrics_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(metrics.to_string(index=False))
    print(f"wrote {data_path}")
    print(f"wrote {metrics_path}")


if __name__ == "__main__":
    main()
