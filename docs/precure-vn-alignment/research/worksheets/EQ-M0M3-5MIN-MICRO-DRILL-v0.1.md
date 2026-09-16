# Micro-drill 5′ — EQ-SA01 M0→M3 (ladder early · M4 CLOSED)

**Mã:** EQ-M0M3-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T2** · sau/trước `EQ-5MIN` · kèm `EPI-5MIN` / `IMAGEJ-QA-5MIN` · trước claim AUROC M3  
**Goal:** ACTIVE · \(Y_{D21}\) không đổi · M0→M3 exploratory · M4/L3 **CLOSED** · synthetic ≠ BN · PREP ≠ DONE  
**Spec:** `EQ-SA01-early-warning` · SAP ES M0–M3 · `EPI-SA01-EARLY-WINDOW`

## Một câu

> EQ-M0M3 5′ = nhắc ladder M0 (D0) → M1 (D3) → M2 (delta) → M3 (D0–D7 + clin_event) trên \(Z\) — **không** PCT_D21 làm early · **không** M4/\(X_{\text{PEA}}\) trước G2 · AUROC sandbox ≠ BN.

## Drill (điền)

```text
Y(t*): PRIMARY_OUT D21 ImageJ 100% — xác nhận không đổi? CÓ
t' early ∈ {D0,D3,D7} hôm nay nhấn: ________
M0 (1 dòng Z(D0)+C): ________
M1 thêm: Z(D3) | khác — ghi: ________
M2 thêm: delta/slope D0→D3 | khác — ghi: ________
M3 thêm: Z(D7)/quỹ đạo + clin_event | khác — ghi: ________
PCT_EPITH D21 làm predictor early? KHÔNG
M4 / X_PEA / L3 hôm nay? CLOSED — vì: ________
AUROC sandbox = evidence BN? KHÔNG
Cặp đã đụng: EQ-5MIN | EPI-5MIN | IMAGEJ-QA | SAP-ES | TRIPOD-SYNTH | PB007 | PB001 — ghi: ________
1 việc nhỏ ≤30′ (EQ Drill 10′ / EPI window / H0H1 skim): ________
Đóng Goal / mở G2 vì đã viết M0–M3? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| EQ đầy đủ | `EQ-SA01` · Drill 10′ |
| EQ 5′ chung | `EQ-5MIN` · siblings: **`EQ02-M0M3-5MIN`** (SA-02) · **`EQ05-M0M3-5MIN`** (SA-05) |
| Early window | `EPI-5MIN` · `EPI-SA01-EARLY-WINDOW` · **`IMAGEJ-EPI-5MIN`** |
| ImageJ QA | `IMAGEJ-QA-5MIN` |
| SAP / TRIPOD | `SAP-ES-5MIN` · `TRIPOD-SYNTH-5MIN` |
| PB equation | `PB007-5MIN` · **`PB007-EQ-5MIN`** · `PB001-5MIN` |
| De-ID×EQ | **`DEID-EQ-5MIN`** · `DEID-MISS-5MIN` |
| ISO-SWAB×EQ | **`ISO-SWAB-EQ-5MIN`** · `OMICS-IF-5MIN` |
| PEA×EQ | **`PEA-EQ-5MIN`** · `PEA-PANEL-5MIN` |
| PREANALYTIC×EQ | **`PREANALYTIC-EQ-5MIN`** · `PREANALYTIC-5MIN` |
| PEA-PANEL×EQ | **`PEA-PANEL-EQ-5MIN`** · `PEA-PANEL-5MIN` |
| INTERIM-G2×EQ | **`INTERIM-G2-EQ-5MIN`** · `INTERIM-G2-5MIN` |
| OMICS-IF×EQ | **`OMICS-IF-EQ-5MIN`** · `OMICS-IF-5MIN` |
| G2×EQ | **`G2-EQ-5MIN`** · `G2-5MIN` |
| OMICS-GATES×EQ | **`OMICS-GATES-EQ-5MIN`** · `OMICS-GATES-5MIN` |
| PB009×EQ | **`PB009-EQ-5MIN`** · `PB009-5MIN` |
| L1L2L3×EQ | **`L1L2L3-EQ-5MIN`** · `L1L2L3-5MIN` |
| AI-STACK×EQ | **`AI-STACK-EQ-5MIN`** · `AI-STACK-5MIN` |
| CLIN-BN×EQ | **`CLIN-BN-EQ-5MIN`** · `CLIN-BN-5MIN` |
| YTESO×EQ | **`YTESO-EQ-5MIN`** · `YTESO-5MIN` |
| PB004×EQ | **`PB004-EQ-5MIN`** · `PB004-5MIN` |
| BN-VISIT×EQ | **`BN-VISIT-EQ-5MIN`** · `BN-VISIT-5MIN` |
| PB005×EQ | **`PB005-EQ-5MIN`** · `PB005-5MIN` |
| PB006×EQ | **`PB006-EQ-5MIN`** · `PB006-5MIN` |
| TRANSLATION×EQ | **`TRANSLATION-EQ-5MIN`** · `TRANSLATION-5MIN` |
| SYNTH×EQ | **`SYNTH-EQ-5MIN`** · `SYNTH-5MIN` |
| M4 gate | `G2-5MIN` · `OMICS-IF-5MIN` · PEA bridge |
| PB008×EQ | **`PB008-EQ-5MIN`** · `PB008-5MIN` |
| MEDIA×EQ | **`MEDIA-EQ-5MIN`** · `MEDIA-5MIN` |
| HAWTHORNE×EQ | **`HAWTHORNE-EQ-5MIN`** · `HAWTHORNE-5MIN` |
| PB001×EQ | **`PB001-EQ-5MIN`** · `PB001-5MIN` |
| PB002×EQ | **`PB002-EQ-5MIN`** · `PB002-5MIN` |
| GLOSSARY×EQ | **`GLOSSARY-EQ-5MIN`** · `GLOSSARY-5MIN` |
| EPI×EQ | **`EPI-EQ-5MIN`** · `EPI-5MIN` |
| ALERT×EQ | **`ALERT-EQ-5MIN`** · `ALERT-5MIN` |
| CLIN_EVENT×EQ | **`CLIN_EVENT-EQ-5MIN`** · `CLIN_EVENT-5MIN` |
| LEAKAGE×EQ | **`LEAKAGE-EQ-5MIN`** · `LEAKAGE-5MIN` |
| IMAGEJ×EQ | **`IMAGEJ-EQ-5MIN`** · `IMAGEJ-QA-5MIN` |
| MISSINGNESS×EQ | **`MISSINGNESS-EQ-5MIN`** · `MISSINGNESS-5MIN` |

## Cấm

- Dùng PCT/outcome D21 làm predictor “early”  
- Mở M4/PEA/G2 vì đã điền ladder  
- Claim AUROC M3 sandbox = phát hiện sớm lâm sàng  

## Liên kết

- EQ: `../equations/EQ-SA01-early-warning-v0.1.md` · Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2)  
- Protocol: `../../rituals/daily-protocol.md` · Bridge: `MULTI-OMICS-PEA-SA01-BRIDGE`
