# Phương trình early warning — SA-02 (PB-002)

**Mã:** EQ-SA02-v0.1  
**Cập nhật:** 2026-09-16 · **Cập nhật:** M0–M3 + leakage note · bridge endpoints · **Drill 10′**  
**Curriculum:** Ngày 12 (2026-09-28) · Q2 staging · **Primary không đổi:** VAS D3

## Primary (không đổi)

\[
Y_{\text{prim}} = \mathrm{VAS}(D3)
\quad\text{hoặc }\Delta\mathrm{VAS}_{D0\to D3}\text{ theo SAP primary synopsis}
\]

## Exploratory early-signal (binary ES — sandbox / SAP ES)

\[
Y_{\text{relief}} = \mathbb{1}\{(\mathrm{VAS}_{D3}-\mathrm{VAS}_{D0})\le -2\}
\]

\[
P(Y_{\text{relief}}=1)=\sigma\big(\beta_0 + \boldsymbol{\beta}_Z^\top Z(t') + \beta_g GROUP + \boldsymbol{\beta}_C^\top C\big)
\]

| Khối | Biến (eCRF SA-02 v0.1) | Ghi chú |
|------|------------------------|---------|
| \(Z\) | VAS_D0 · (VAS_D1 `[CẦN XÁC NHẬN]`) · CULTURE_CFU_D0/D1/D3 | Cửa sổ \(t'\le D3\) |
| \(C\) | AGE, DX_CAT, ADHERE | Baseline severity / adherence |
| Nhóm | GROUP | RCT arm |
| \(X\) | Marker niêm mạc | **gated** — không thay primary |

### M0–M3 (SAP ES — exploratory · khớp sandbox QC)

| Model | Predictors (ý) | Mục đích |
|-------|----------------|----------|
| **M0** | VAS_D0 + AGE + DX_CAT + GROUP | Baseline only |
| **M1** | + VAS_D3 *(sandbox QC — xem leakage)* | Demo pipeline; **không** dùng làm claim early |
| **M1\*** (khoa học) | + VAS_D1 nếu thu · hoặc chỉ CFU_D0 | True early trước / không trùng \(Y\) |
| **M2** | + CULTURE_CFU_D0, CFU_D3 | Vi sinh vs triệu chứng |
| **M3** | + CFU_D1 + ADHERE | Full early window + adherence |

**Leakage note:** sandbox `sa02_…_m0_m3.py` M1 gồm `VAS_D3` gần định nghĩa \(Y_{\text{relief}}\) → AUROC cao = **QC cấu trúc**, ≠ evidence. Ritual Ngày 12 ưu tiên câu hỏi D1/`CFU` dẫn trước \(\Delta\)VAS.

**H0/H1 (exploratory):** chuỗi \(Z(t')\) với \(t'<D3\) cải thiện vs chỉ VAS_D0 — `EH-SA02-early-signal` · không đổi primary.

**Precure shift:** tồn tại \(t'\le D3\) (ưu tiên D1/CFU) sao cho tín hiệu **dẫn trước** hoặc bổ sung \(\Delta\)VAS — không claim Dx sớm.

### Drill 10′ (điền — leakage / không gộp SA)

```text
t* SA-02: ________     t' ưu tiên (D1/CFU): ________
Y_relief định nghĩa: ________
M1 sandbox gồm VAS_D3 → leakage? CÓ — vì: ________
M1* khoa học dùng gì thay: ________
X mucosa / L3: CLOSED vì ________
1 câu KHÔNG gộp với SA-01/05:
```

## M4 / \(X_{\text{mucosa}}\) — L3 (gated)

\[
P(Y_{\text{relief}}=1)=\sigma\big(\ldots + \boldsymbol{\beta}_X^\top X_{\text{mucosa}}(t')\big)
\quad\text{chỉ sau G1–G2 / ISO liên quan}
\]

Mặc định **CLOSED** · SA-02 = support, không mở omics vì đã đọc VAS.

## ALERT (không phải model)

Ngưỡng nội bộ trên VAS series / AE — `ALERT-SA02`. ALERT ≠ thay \(\beta\) SAP; ≠ đổi nhánh RCT.

## Cấm

- Dùng biến sau / trùng \(Y\) (vd. chính VAS_D3 làm “early predictor”) rồi claim early lâm sàng  
- Marker = primary  
- AUROC synthetic = evidence BN  
- Gộp model với SA-01/05

## Liên kết

- `eCRF-SA02-early-signal-dictionary-v0.1.md` · `SAP-SA02-ES-v0.1-DRAFT.md` · `VAS-SCALE-HARMONIZE-SA02-v0.1.md`  
- Bridge: `ENDPOINTS-CROSS-SA-BRIDGE-v0.1.md` · thẻ `ENDPOINTS-EARLY-SIGNAL-RITUAL-CARD`  
- Drill hàng ngày: `../study-sheets/STUDY-SHEET-MULTI-OMICS-ES-DRILL-v0.1.md` (§ SA-02)  
- `CROSS-SA-EARLY-SIGNAL-MAP` · `EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01` (timestamp triệu chứng)
