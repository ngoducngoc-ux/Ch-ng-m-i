# Micro-drill 5′ — CROSS-SA × EQ (schema t*/Z · không gộp Y · ladder)

**Mã:** CROSS-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4**/ **T6**/ **CN** · sau `CROSS-SA-5MIN` · kèm `EQ-M0M3` / `EQ02-M0M3` / `EQ05-M0M3` · trước claim “một model Smart A chung”  
**Goal:** ACTIVE · cờ đầu SA-01 · mỗi SA một \(Y(t^*)\) · L3 **CLOSED** · synthetic ≠ BN · PREP ≠ DONE  

## Một câu

> CROSS×EQ 5′ = so sánh **schema** \(t^*\)/\(Z\) sớm + ladder M0–M3 giữa SA — học khung EQ, **không** train chung / gộp endpoint / chọn cờ theo AUROC sandbox.

## Drill (điền)

```text
SA đang ôn (không gộp): 01 | 02 | 05 — chọn: ________
EQ sibling: EQ-M0M3 | EQ02-M0M3 | EQ05-M0M3 — chọn: ________
t* primary đúng: D21 | VAS_D3 | PUSH_D14 — ghi: ________
1 Z sớm (không dùng Y(t*) làm predictor): ________
1 dòng ladder M0→M3 (Z only): ________
Gộp Y SA-01+02+05? KHÔNG — vì: ________
Chọn cờ đầu theo AUROC synthetic? KHÔNG
verify.sh PASS = evidence BN? KHÔNG
Omics / L3 vì “schema đã khớp”? KHÔNG
Cặp đã đụng: CROSS-SA | EQ-5MIN | EQ-M0M3 | EQ02 | EQ05 | PB007-EQ | SHIFT | OMICS-GATES — ghi: ________
1 việc nhỏ ≤30′ (CROSS map / EQ Drill 10′ / PB007-EQ): ________
Đóng Goal vì CROSS×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Thẻ khoa học | **`CROSS-EQ-SCIENCE-CARD`** · `CROSS-SA-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` |
| CROSS alone | `CROSS-SA-5MIN` · `CROSS-SA-EARLY-SIGNAL-MAP` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| PB×EQ | `PB007-EQ-5MIN` · `PB007-5MIN` |
| TRIPOD×EQ | **`TRIPOD-EQ-5MIN`** · `TRIPOD-SYNTH-5MIN` |
| LEAK×CROSS | **`LEAK-CROSS-5MIN`** · `LEAKAGE-5MIN` |
| LEAK-CROSS×EQ | **`LEAK-CROSS-EQ-5MIN`** · `LEAK-CROSS-5MIN` |
| ALERT×CROSS | **`ALERT-CROSS-5MIN`** · `ALERT-5MIN` |
| ALERT-CROSS×EQ | **`ALERT-CROSS-EQ-5MIN`** · `ALERT-CROSS-5MIN` |
| Bridge | `ENDPOINTS-CROSS-SA-BRIDGE` |
| Cờ đầu | `PB001-5MIN` · DECISION-FLAGSHIP |
| SHIFT×EQ | **`SHIFT-EQ-5MIN`** · `SHIFT-5MIN` |

## Cấm

- Một model / một \(Y\) cho nhiều SA  
- Chọn cờ đầu hoặc power theo AUROC sandbox  
- Order L3 vì schema “đã khớp” / ladder “đã đủ”  

## Liên kết

- Worksheet: `CROSS-SA-EARLY-SIGNAL-MAP-v0.1.md`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4/T6/CN) · Protocol: `../../rituals/daily-protocol.md`
- Thẻ khoa học: **`CROSS-EQ-SCIENCE-CARD-v0.1.md`** · `CROSS-SA-SCIENCE-CARD-v0.1.md`
