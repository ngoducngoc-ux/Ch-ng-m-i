# Micro-drill 5′ — LEAKAGE × EQ (timestamp · ladder Z · ≠ AUROC claim)

**Mã:** LEAKAGE-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4** (T2/T6) · sau `LEAKAGE-5MIN` / `LEAK-CROSS-5MIN` / `EQ-M0M3-5MIN` / `VAS-EQ-5MIN` · trước claim AUROC “đẹp”  
**Goal:** ACTIVE · feature \(t' < t^*\) · không trùng \(Y\) · sandbox ≠ BN · G2/L3 CLOSED · PREP ≠ DONE  
**Pitfall:** ML-OMICS #1 · DOI TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594)

## Một câu

> LEAKAGE×EQ 5′ = 1 feature leakage + 1 feature hợp lệ **và** 1 dòng ladder M0–M3 chỉ trên feature hợp lệ — M1+VAS_D3 = QC leakage, ≠ evidence.

## Drill (điền — 1 SA)

```text
Thứ: T2|T4|T6 · SA: 01|02|05 — chọn: ________
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________
t* / Y: ________
1 feature LEAKAGE nếu vào M early: ________
1 feature HỢP LỆ cho t': ________
1 dòng Z / M0→M3 (chỉ feature hợp lệ): ________
Sandbox AUROC đẹp → claim BN? KHÔNG
Cặp đã đụng: LEAKAGE | LEAK-CROSS | VAS-LEAK | VAS-EQ | SYNTH-EQ | TRIPOD-EQ — ghi: ________
Order omics / đóng Goal vì LEAKAGE×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| LEAKAGE alone | `LEAKAGE-5MIN` · `LEAKAGE-CROSS-SA-ATLAS` |
| LEAK×CROSS / VAS | `LEAK-CROSS-5MIN` · `VAS-LEAK-5MIN` · `VAS-EQ-5MIN` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| TRIPOD / SYNTH | `TRIPOD-EQ-5MIN` · `SYNTH-EQ-5MIN` |
| IMAGEJ / miss | `IMAGEJ-EQ-5MIN` · `MISSINGNESS-EQ-5MIN` |

## Cấm

- Báo M1 sandbox AUROC như ES lâm sàng  
- Mở G2 vì “phát hiện” leakage trên SYN · 1 câu cho cả 3 SA  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4 · EQ days) · Protocol: `../../rituals/daily-protocol.md`  
- Pitfalls: `../guides/ML-OMICS-PITFALLS-v0.1.md`
