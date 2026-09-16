# Micro-drill 5′ — PITFALLS × EQ (1 pitfall · ladder Z · ≠ AUROC claim)

**Mã:** PITFALLS-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4 / T5** · sau `PITFALLS-5MIN` / `LEAKAGE-EQ-5MIN` / `SYNTH-EQ-5MIN` / `EQ-M0M3-5MIN` · trước claim model sớm  
**Goal:** ACTIVE · 1 pitfall + 1 dòng ladder · sandbox ≠ BN · L3/G2 CLOSED · PREP ≠ DONE  
**DOI:** TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594)

## Một câu

> PITFALLS×EQ 5′ = chọn **1 trong 5** pitfalls **và** 1 dòng ladder M0–M3 trên feature hợp lệ — anti-overclaim; AUROC sandbox ≠ evidence.

## Drill (điền)

```text
Pitfall: #1 time | #2 group | #3 multiplicity | #4 batch/site | #5 synth→BN — chọn: ________
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________
1 feature LEAK / SAI nếu vào M early: ________
1 feature HỢP LỆ cho ladder: ________
1 dòng Z / M0→M3 (chỉ feature hợp lệ): ________
SAP primary đổi vì drill? KHÔNG
verify PASS / AUROC SYN = BN evidence? KHÔNG
Cặp đã đụng: PITFALLS | LEAKAGE-EQ | SYNTH-EQ | TRIPOD-EQ | MISSINGNESS-EQ — ghi: ________
1 việc nhỏ ≤30′ (ML-OMICS skim / EQ Drill 10′): ________
Đóng Goal / mở G2 vì PITFALLS×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| PITFALLS alone | `PITFALLS-5MIN` · `ML-OMICS-PITFALLS` |
| Leak / SYNTH×EQ | `LEAKAGE-EQ-5MIN` · `SYNTH-EQ-5MIN` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| TRIPOD / miss | `TRIPOD-EQ-5MIN` · `MISSINGNESS-EQ-5MIN` |
| STREAK / backlog | `STREAK3-EQ-5MIN` · `BACKLOG-EQ-5MIN` |

## Cấm

- Báo AUROC sandbox như bằng chứng lâm sàng  
- Tune trên cùng tập đánh giá (#2) · quét panel không FDR (#3)  
- Order PEA / mở G2 vì đã ôn pitfalls  

## Liên kết

- Guide: `../guides/ML-OMICS-PITFALLS-v0.1.md`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4/T5) · Protocol: `../../rituals/daily-protocol.md`
