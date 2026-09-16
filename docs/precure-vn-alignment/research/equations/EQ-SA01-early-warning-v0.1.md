# Phương trình early warning — SA-01 (PB-001 / cờ đầu)

**Mã:** EQ-SA01-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 10 (2026-09-26)

## Primary (không đổi)

\[
Y_{D21} = \mathbb{1}\{\text{biểu mô hóa 100\% tại D21 (ImageJ)}\}
\]

## Exploratory early-signal (logistic)

\[
P(Y_{D21}=1) = \sigma\big(\beta_0 + \boldsymbol{\beta}_Z^\top Z(D0,D3,D7) + \beta_g GROUP + \boldsymbol{\beta}_C^\top C \big)
\]

| Khối | Biến (eCRF v0.2) |
|------|------------------|
| \(Z\) | PCT_EPITH, CULTURE_CFU, VAS_DRESS, CLIN_EVENT (sensitivity) |
| \(C\) | AGE, WOUND_TYPE, ADHERENCE, AE_LOCAL |
| M0–M3 | như `SAP-SA01-ES-v0.1-DRAFT.md` / sandbox |

**Precure shift:** tồn tại \(t' \in \{D0,D3,D7\}\) sao cho mô hình có chuỗi \(Z\) cải thiện AUROC/Brier vs chỉ \(Z(D0)\) — **không** claim chẩn đoán sớm lâm sàng.

## Liên kết

- `EH-SA01-early-signal-v0.1.md` · `DESIGN-SA01-minimal-longitudinal-v0.1.md` · `ALERT-SA01-v0.1.md`
