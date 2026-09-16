#!/usr/bin/env python3
"""Synthetic SA-02 throat/VAS data + M0–M3 AUROC demo for early-signal.

Primary clinical endpoint in protocol: ΔVAS D3 vs D0. This sandbox predicts
binary 'meaningful relief' at D3 from D0–D3 signals. SYNTHETIC ONLY.
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
N = 100
OUT_DIR = Path(__file__).resolve().parent / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def simulate(n: int = N, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    age = rng.integers(18, 71, size=n)
    dx = rng.integers(1, 4, size=n)
    group = rng.integers(1, 3, size=n)
    adhere = rng.integers(0, 3, size=n)
    latent = (
        -0.02 * (age - 40)
        - 0.25 * (dx - 1)
        + 0.3 * (group == 1)
        + 0.25 * adhere
        + rng.normal(0, 1, n)
    )
    vas_d0 = np.clip(7 - 0.5 * latent + rng.normal(0, 1.0, n), 2, 10)
    cfu_d0 = np.clip(5.5 - 0.5 * latent + rng.normal(0, 0.6, n), 1.0, 8.0)
    cfu_d1 = np.clip(cfu_d0 - 0.4 - 0.35 * latent + rng.normal(0, 0.5, n), 0.5, 8.0)
    vas_d3 = np.clip(vas_d0 - 2.0 - 0.6 * latent + rng.normal(0, 0.9, n), 0, 10)
    cfu_d3 = np.clip(cfu_d1 - 0.5 - 0.3 * latent + rng.normal(0, 0.5, n), 0.5, 8.0)
    delta = vas_d3 - vas_d0
    y = (delta <= -2).astype(int)
    return pd.DataFrame(
        {
            "SUBJ_ID": [f"SA-02-{i:03d}" for i in range(1, n + 1)],
            "AGE": age,
            "DX_CAT": dx,
            "GROUP": group,
            "ADHERE": adhere,
            "VAS_D0": vas_d0.round(1),
            "VAS_D3": vas_d3.round(1),
            "DELTA_VAS_D3": delta.round(1),
            "CULTURE_CFU_D0": cfu_d0.round(2),
            "CULTURE_CFU_D1": cfu_d1.round(2),
            "CULTURE_CFU_D3": cfu_d3.round(2),
            "RELIEF_D3": y,
        }
    )


def feature_sets(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    base = ["AGE", "DX_CAT", "GROUP", "VAS_D0"]
    return {
        "M0": df[base],
        "M1": df[base + ["VAS_D3"]],
        "M2": df[base + ["VAS_D3", "CULTURE_CFU_D0", "CULTURE_CFU_D3"]],
        "M3": df[
            base
            + [
                "VAS_D3",
                "CULTURE_CFU_D0",
                "CULTURE_CFU_D1",
                "CULTURE_CFU_D3",
                "ADHERE",
            ]
        ],
    }


def eval_models(df: pd.DataFrame) -> pd.DataFrame:
    y = df["RELIEF_D3"].to_numpy()
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
    data_path = OUT_DIR / "synthetic_sa02_early_signal.csv"
    metrics_path = OUT_DIR / "synthetic_sa02_m0_m3_metrics.json"
    df.to_csv(data_path, index=False)
    payload = {
        "note": "SYNTHETIC ONLY — not clinical evidence",
        "seed": SEED,
        "endpoint": "RELIEF_D3 := (VAS_D3 - VAS_D0) <= -2",
        "metrics": metrics.to_dict(orient="records"),
    }
    metrics_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(metrics.to_string(index=False))
    print(f"wrote {data_path}")
    print(f"wrote {metrics_path}")


if __name__ == "__main__":
    main()
