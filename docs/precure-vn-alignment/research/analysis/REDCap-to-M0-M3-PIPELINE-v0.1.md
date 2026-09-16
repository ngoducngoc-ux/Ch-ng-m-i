# Pipeline REDCap export → M0–M3 (SA-01/02/05)

**Mã:** PIPELINE-ES-v0.1  
**Ngày:** 2026-09-16  
**Phạm vi:** exploratory early-signal; không thay SAP primary endpoints.

## 1. Luồng

```text
REDCap (staging) → export CSV wide/long → QC script → feature matrix M0–M3 → SAP ES metrics
                      ↑
              verify.sh (synthetic only trước khi có export thật)
```

## 2. QC tối thiểu (trước model)

| Bước | Kiểm tra |
|------|----------|
| ID | SUBJ_ID unique; visit không trùng (SA-01 repeating) |
| Thời gian | VISIT_CODE ∈ {D0,D3,D7,…} khớp DESIGN-SA01 |
| Missing | Báo % missing theo biến M0–M3 |
| Leakage | Không dùng biến sau cửa sổ early (vd. D14→D21 OK cho Y, không OK cho X@D14 trong “early”) |

## 3. Map script synthetic → export thật

| SA | Script sandbox | Outcome cột | Predictors chính |
|----|----------------|-------------|------------------|
| 01 | `sa01_early_signal_synthetic_m0_m3.py` | PRIMARY_OUT / PCT D21 | PCT_EPITH, CFU, VAS |
| 02 | `sa02_early_signal_synthetic_m0_m3.py` | RELIEF_D3 | VAS, CFU D0–D3 |
| 05 | `sa05_early_signal_synthetic_m0_m3.py` | IMPROVED_D14 | PUSH, TURN_ADHERE, CFU |

Khi có export: thay `simulate()` bằng `read_csv()` + cùng `feature_sets()` / `eval_models()`.

## 4. Mở rộng M4 (chỉ sau G2)

Chỉ khi `SPEC-SA01-BIO-v0.1-DRAFT.md` G2 pass → thêm cột \(X_{\text{mol}}\) → logistic/GEE M4.

## 5. Việc nhỏ

- [ ] Script `redcap_import_qc.py` — chạy `--demo` sau synthetic; export thật khi có
- [ ] Chạy `bash verify.sh` sau mỗi thay đổi feature_sets

## Chạy sandbox

```bash
bash docs/precure-vn-alignment/research/analysis/verify.sh
python3 docs/precure-vn-alignment/research/analysis/redcap_import_qc.py --demo
```

## Liên kết Q2

Bridge: `../worksheets/Q2-STAGING-DEID-EARLY-SIGNAL-BRIDGE-v0.1.md` · checklist de-ID · thẻ Q2 staging
