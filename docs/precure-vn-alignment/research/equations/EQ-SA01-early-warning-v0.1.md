# Phương trình early warning — SA-01 (PB-001 / cờ đầu)

**Mã:** EQ-SA01-v0.1  
**Ngày:** 2026-09-16 · **Cập nhật:** bridge PEA / M0–M3 rõ lớp  
**Curriculum:** Ngày 10 (2026-09-26) · ôn PEA 05–07 · Q3 L2

## Primary (không đổi)

\[
Y_{D21} = \mathbb{1}\{\text{biểu mô hóa 100\% tại D21 (ImageJ)}\}
\]

## Exploratory early-signal (logistic) — L1/L2

\[
P(Y_{D21}=1) = \sigma\big(\beta_0 + \boldsymbol{\beta}_Z^\top Z(D0,D3,D7) + \beta_g GROUP + \boldsymbol{\beta}_C^\top C \big)
\]

| Khối | Biến (eCRF v0.2) | Ghi chú |
|------|------------------|---------|
| \(Z\) | PCT_EPITH, CULTURE_CFU, VAS_DRESS | Cửa sổ early \(t'\) |
| Sự kiện | CLIN_EVENT (0–4) | Sensitivity / Zhou — không leakage từ \(Y\) |
| \(C\) | AGE, WOUND_TYPE, ADHERENCE, AE_LOCAL | PB-008 adherence |
| Nhóm | GROUP | RCT arm |

### M0–M3 (SAP ES — exploratory)

| Model | Predictors (ý) | Mục đích |
|-------|----------------|----------|
| **M0** | \(Z(D0)\) + \(C\) | Baseline only |
| **M1** | + \(Z(D3)\) | Early mid |
| **M2** | + deltas / slopes D0→D3 | Động học ngắn |
| **M3** | + \(Z(D7)\) / quỹ đạo D0–D7 + `clin_event` | Full early window |

**H0/H1:** M3 vs M0 AUROC/Brier — `HYP-SA01-H0H1-v0.1.md` (exploratory, không đổi primary).

**Precure shift:** tồn tại \(t' \in \{D0,D3,D7\}\) sao cho chuỗi \(Z\) cải thiện dự báo vs chỉ \(Z(D0)\) — **không** claim chẩn đoán sớm lâm sàng.

## M4 / \(X_{\text{PEA}}\) — L3 (gated)

\[
P(Y_{D21}=1)=\sigma\big(\ldots + \boldsymbol{\beta}_X^\top X_{\text{PEA}}(t')\big)
\quad\text{chỉ sau G2 trên data thật}
\]

| Điều kiện | Artifact |
|-----------|----------|
| G1 nested + ICF | `SPIRIT-NESTED-G1-CHECKLIST` |
| G2 PI/DSMB + N thật | `G2-READINESS` · `OMICS-IF-G2` |
| Pre-analytic R1–R3 | `PRE-ANALYTIC-PEA-SA01` |
| Panel hẹp (không 96 mù) | `PEA-PANEL-FEASIBILITY` |
| H0_mol | `HYP-SA01-H0H1` |

**Bridge 1 trang:** `worksheets/MULTI-OMICS-PEA-SA01-BRIDGE-v0.1.md` · thẻ `PEA-L1L2L3-DECISION-CARD`

### Drill 10′ (điền rồi đối chiếu bridge #1 / #8)

```text
M0 predictors: ________
M3 thêm gì so M0: ________
clin_event có leakage từ Y_D21? KHÔNG vì: ________
M4/X_PEA: CLOSED | điều kiện mở: ________
1 câu Precure shift (t' cải thiện vs Z(D0) only):
Bank đối chiếu: `PRECURE-SHIFT-CROSS-SA-BANK` (hàng SA-01)
```

## ALERT (không phải model)

A1–A4 nội bộ trên \(Z\)/`clin_event` — `ALERT-SA01` · map Nat Med `NATMED-ACTIONABLE-ALERT-MAP` · atlas `ALERT-CROSS-SA-ATLAS`.  
ALERT ≠ thay \(\beta\) trong SAP; ≠ đổi nhánh RCT.

## Cấm

- Dùng biến sau \(t^*\) (vd. PCT D21) làm predictor “early”  
- AUROC synthetic = evidence BN  
- Thêm \(X\) trước G2

## Liên kết

- `EH-SA01-early-signal-v0.1.md` · `DESIGN-SA01-minimal-longitudinal-v0.1.md` · `ALERT-SA01-v0.1.md`  
- `EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01` · `MULTI-OMICS-PEA-SA01-BRIDGE`  
- Drill hàng ngày: `../study-sheets/STUDY-SHEET-MULTI-OMICS-ES-DRILL-v0.1.md`  
- Leakage atlas: `../worksheets/LEAKAGE-CROSS-SA-ATLAS-v0.1.md`  
- ALERT atlas: `../worksheets/ALERT-CROSS-SA-ATLAS-v0.1.md`  
- clin_event atlas: `../worksheets/CLIN_EVENT-CROSS-SA-ATLAS-v0.1.md`  
- Precure shift bank: `../worksheets/PRECURE-SHIFT-CROSS-SA-BANK-v0.1.md`  
- `guides/AI-LONGITUDINAL-STACK-v0.1.md` · `MULTI-OMICS-GATES-SMART-A-v0.1.md`
