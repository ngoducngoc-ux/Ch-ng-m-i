# Micro-drill 5′ — ML/omics pitfalls (5 cổng anti-overclaim)

**Mã:** PITFALLS-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4**/ **T5** · STREAK3 · Ngày 20 · trước claim model sớm / AUROC  
**Goal:** ACTIVE · không thay SAP primary · L3 **CLOSED** · synthetic ≠ BN · PREP ≠ DONE  
**DOI:** TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594)

## Một câu

> PITFALLS 5′ = chọn **1 trong 5** pitfalls (leakage thời gian · leakage nhóm · multiplicity · batch/site · synthetic→BN) và viết 1 hàng kiểm trong repo — không báo cáo sandbox như evidence.

## Drill (điền)

```text
Pitfall hôm nay: #1 time | #2 group | #3 multiplicity | #4 batch/site | #5 synth→BN — chọn: ________
1 câu “đúng kiểm” trong repo (file/atlas): ________
1 câu SAI hôm nay: ________
SAP primary đổi vì pitfall drill? KHÔNG
verify.sh PASS = BN evidence? KHÔNG (#5)
M4/X mở vì đã ôn pitfalls? KHÔNG
Cặp đã đụng: LEAKAGE-5MIN | SYNTH-5MIN | TRIPOD-5MIN | EQ-5MIN | GLOSSARY — ghi: ________
1 việc nhỏ ≤30′: ________
Đóng Goal vì PITFALLS? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| # | File cặp |
|---|----------|
| 1 | `LEAKAGE-5MIN` · `LEAKAGE-CROSS-SA-ATLAS` |
| 2/4 | hold-out site — `[CẦN XÁC NHẬN]` khi có data thật |
| 3 | SAP ES FDR · PEA panel hẹp |
| 5 | `SYNTH-5MIN` · `verify.sh` |
| Guide | `ML-OMICS-PITFALLS` · `TRIPOD-5MIN` |
| SYNTH×EQ | **`SYNTH-EQ-5MIN`** · `SYNTH-5MIN` |
| PITFALLS×EQ | **`PITFALLS-EQ-5MIN`** · EQ ladders |

## Cấm

- Báo cáo AUROC sandbox như bằng chứng lâm sàng  
- Tune trên cùng tập đánh giá (#2)  
- Quét hàng trăm protein không FDR (#3)  

## Liên kết

- Guide: `../guides/ML-OMICS-PITFALLS-v0.1.md`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4/T5) · Protocol: `../../rituals/daily-protocol.md`
- Thẻ khoa học: `PITFALLS-SCIENCE-CARD-v0.1.md`
