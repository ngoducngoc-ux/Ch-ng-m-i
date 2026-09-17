# ML / omics predictive — 5 pitfalls (Precure alignment) · refresh v0.1b

**Mã:** ML-PITFALLS-v0.1b · **Ngày:** 2026-09-16  
**Goal:** ACTIVE · STREAK thật vẫn **2 DONE** · EQ bank **CLOSED** · densify ≠ DONE  
**STREAK&lt;3?** Path STREAK3 trước · **`STREAK3-PACK`** · **`STREAK3-EQ`** · NatMed → tick **19/09** · dừng OPENER/stack  
**STREAK≥3?** **`AFTER-STREAK3-OPENER`** → 1×EQ sibling → **`DAILY-STACK`** · bridges #0–14  
**Không:** agent tick DONE · UpdateGoal complete trên PREP/densify · invent EQ mới · biospecimen trước G1–G2 · L3 CLOSED  
**Curriculum:** Ngày 20 · Không thay SAP primary · tip tiếp `YTESO` (`y-te-so-precure-bridge`) · Drive keep `1Vjchf1i…`  

```text
STREAK <3? → STREAK3 (PI-NEXT) · densify ≠ DONE
        ↓ STREAK ≥3
OPENER → EQ sibling → DAILY-STACK · ritual theo Ngày N
```

1. **Leakage thời gian** — dùng biến sau \(t^*\) hoặc outcome proxy để dự báo \(Y(t^*)\).  
2. **Leakage nhóm** — tune trên cùng tập đánh giá AUROC (cần nested CV / hold-out site).  
3. **Multiplicity** — quét hàng trăm protein không FDR → false discovery.  
4. **Batch / site** — omics và site confounded; cần batch correction hoặc stratify.  
5. **Synthetic → lâm sàng** — AUROC sandbox **không** báo cáo như evidence BN · PREP≠DONE.

## Khung báo cáo

- TRIPOD: DOI [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594) (prediction model reporting) · VDHN ≠ DOI  
- Micro-drill 5′: **`PITFALLS-5MIN-MICRO-DRILL`** (T4/T5 · cả 5) · `TRIPOD-5MIN` · **`SYNTH-5MIN`** (#5) · **`LEAKAGE-5MIN`** (#1) · **`PITFALLS-SCIENCE-CARD`** · **`PITFALLS-EQ-SCIENCE-CARD`**  
- Exploratory Smart A: pre-spec M0–M3 trong SAP ES; mọi M4 + omics sau G2 · L3 CLOSED  
- Hub: `MULTI-OMICS-GATES` (refresh v0.1b) · `AI-LONGITUDINAL-STACK` (refresh v0.1b) · `SCIENCE-CARDS-INDEX`

## Việc nhỏ

- [x] Pitfall ↔ kiểm trong repo (Ngày 20 prep):
  - **#5 Synthetic→lâm sàng:** `verify.sh` + sandbox — chỉ QC pipeline · **`SYNTH-5MIN-MICRO-DRILL`**.
  - **#1 Leakage thời gian:** SAP ES §7 · atlas `LEAKAGE-CROSS-SA-ATLAS` · **`LEAKAGE-5MIN-MICRO-DRILL`** (T4).
  - **#3 Multiplicity:** SAP ES FDR / hypothesis-generating; PEA panel hẹp worksheet.
  - **#2/#4:** cần data thật + site hold-out — `[CẦN XÁC NHẬN]` khi có omics.
- densify ≠ DONE · EQ bank CLOSED · không invent EQ · Goal ACTIVE.
