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
| M4 gate | `G2-5MIN` · `OMICS-IF-5MIN` · PEA bridge |

## Cấm

- Dùng PCT/outcome D21 làm predictor “early”  
- Mở M4/PEA/G2 vì đã điền ladder  
- Claim AUROC M3 sandbox = phát hiện sớm lâm sàng  

## Liên kết

- EQ: `../equations/EQ-SA01-early-warning-v0.1.md` · Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2)  
- Protocol: `../../rituals/daily-protocol.md` · Bridge: `MULTI-OMICS-PEA-SA01-BRIDGE`
