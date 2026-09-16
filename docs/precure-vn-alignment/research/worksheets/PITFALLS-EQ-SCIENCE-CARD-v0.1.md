# PITFALLS-EQ — thẻ khoa học 1 trang (#1+#5 × ladder · ≠ AUROC claim)

**Mã:** PITFALLS-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `PITFALLS-EQ-5MIN-MICRO-DRILL` · PITFALLS-SCIENCE-CARD · LEAKAGE-EQ · SYNTH-EQ · TRIPOD-SYNTH-EQ · EQ-M0M3  
**Căn cứ:** `ML-OMICS-PITFALLS` · TRIPOD DOI 10.1136/bmj.g7594 · G2 CLOSED · L3 CLOSED  
**Dùng khi:** STREAK≥3 · Daily stack **T4/T5** · trước claim model sớm · cặp PITFALLS×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · 1 pitfall + 1 dòng ladder · sandbox ≠ BN · L3/G2 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp PITFALLS×EQ**: chọn **1 trong 5** pitfalls **và** 1 dòng ladder M0–M3 trên feature hợp lệ — anti-overclaim; AUROC sandbox ≠ evidence. Khác `PITFALLS-SCIENCE-CARD` (5 pitfalls alone) / `LEAKAGE-EQ` (timestamp×ladder) / `SYNTH-EQ` (demo×ladder) — thẻ này neo **pitfall × ladder**.

**Mở song song:** thẻ này · `PITFALLS-EQ-5MIN` · `PITFALLS-SCIENCE-CARD` · `LEAKAGE-EQ-5MIN` · `SYNTH-EQ-SCIENCE-CARD` · `TRIPOD-SYNTH-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD`

## Giữ / bỏ (PITFALLS × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên feature hợp lệ / \(Z\) | Feature leak / peek sau AUROC |
| **#1 time** | Timestamp trước \(t^*\) | Outcome leak vào M early |
| **#2 group** | Split độc lập | Tune trên cùng tập đánh giá |
| **#3 mult.** | Pre-spec / FDR | Quét panel không kiểm soát |
| **#4 batch** | Site/batch trong QC | Bỏ qua site effect |
| **#5 synth** | Label pipeline | AUROC SYN = BN evidence |
| **Order / Goal** | KHÔNG từ densify | Mở G2 / đóng Goal vì đã ôn |

## Phương trình ranh giới

```text
1 pitfall (#1–#5)  +  EQ ladder M0–M3 trên feature hợp lệ
  =  bước anti-overclaim hợp lệ hôm nay
Feature hợp lệ  ≠  evidence BN  ≠  AUROC lâm sàng
verify PASS / AUROC_SYN  ≠  early-signal trên BN
Ôn pitfalls  ≠  order PEA / mở G2 / UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T4|T5 · Pitfall: #1|#2|#3|#4|#5 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
1 feature LEAK / SAI nếu vào M early: ________
1 feature HỢP LỆ cho ladder: ________
1 dòng Z / M0→M3 (chỉ feature hợp lệ): ________
SAP primary đổi vì drill? KHÔNG
verify PASS / AUROC SYN = BN evidence? KHÔNG
Cặp LEAK-CROSS-EQ / SYNTH-EQ / TRIPOD-SYNTH-EQ / MISSINGNESS-EQ hôm nay? ________
1 việc ≤30′ (ML-OMICS skim / EQ Drill 10′): ________
Đóng Goal / mở G2 vì PITFALLS×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở PITFALLS + EQ sibling thẻ riêng trước cặp? ________
Pitfall+ladder = lý do AUROC lâm sàng / G2? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | PITFALLS×EQ bridge 1 trang |
| `PITFALLS-EQ-5MIN` | Drill điền |
| `PITFALLS-SCIENCE-CARD` | 5 pitfalls alone |
| `LEAKAGE-EQ` / `LEAK-CROSS-EQ` | Timestamp / cross × ladder |
| `SYNTH-EQ` / `TRIPOD-SYNTH-EQ` | Demo / AI claim × ladder |
| `EQ-M0M3` | Ladder sibling |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Báo AUROC sandbox như bằng chứng lâm sàng  
- Tune trên cùng tập đánh giá (#2) · quét panel không FDR (#3)  
- Order PEA / mở G2 vì đã ôn pitfalls · UpdateGoal trên PREP  

## Liên kết

`PITFALLS-EQ-5MIN-MICRO-DRILL` · `PITFALLS-SCIENCE-CARD` · `../guides/ML-OMICS-PITFALLS-v0.1.md` · `LEAKAGE-SCIENCE-CARD` · `SYNTH-EQ-SCIENCE-CARD` · `TRIPOD-SYNTH-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
