# Micro-drill 5′ — CROSS-SA early-signal map (không gộp Y)

**Mã:** CROSS-SA-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4**/ **T6**/ **CN** · STREAK3 · bridge #2 · Ngày 33–36 · trước claim “một model Smart A chung”  
**Goal:** ACTIVE · cờ đầu SA-01 · mỗi SA một \(Y(t^*)\) · L3 **CLOSED** · synthetic ≠ BN · PREP ≠ DONE  

## Một câu

> CROSS-SA 5′ = so sánh **schema** \(t^*\)/\(Z\) sớm giữa SA — học khung, **không** train chung một model / gộp endpoint / chọn cờ theo AUROC sandbox.

## Drill (điền)

```text
SA đang ôn (không gộp): 01 | 02 | 05 | 03 | 04 — chọn: ________
t* primary đúng: D21 | VAS_D3 | PUSH_D14 | ATCC | ISO — ghi: ________
1 Z sớm (không dùng Y(t*) làm predictor): ________
Gộp Y SA-01+02+05? KHÔNG — vì: ________
Chọn cờ đầu theo AUROC synthetic? KHÔNG
verify.sh PASS = evidence BN? KHÔNG
Omics vì “đã so sánh schema”? KHÔNG
1 việc nhỏ ≤30′ (EQ / ENDPOINTS / OMICS-GATES / PB001): ________
Cặp đã đụng: EQ-5MIN | VAS/PUSH/EPI | OMICS-GATES | SHIFT | PB001 — ghi: ________
Đóng Goal vì CROSS-SA? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Map đầy đủ | `CROSS-SA-EARLY-SIGNAL-MAP` |
| Bridge | `ENDPOINTS-CROSS-SA-BRIDGE` |
| EQ | `EQ-5MIN` · `EQ-SA01|02|05` · **`PB007-EQ-5MIN`** · **`CROSS-EQ-5MIN`** |
| LEAK×CROSS | **`LEAK-CROSS-5MIN`** · `LEAKAGE-5MIN` |
| Cổng | `OMICS-GATES-5MIN` · `G2-5MIN` |
| Cờ đầu | `PB001-5MIN` · DECISION-FLAGSHIP |

## Cấm

- Một model / một \(Y\) cho nhiều SA  
- Chọn cờ đầu hoặc power theo AUROC sandbox  
- Order L3 vì schema “đã khớp”  

## Liên kết

- Worksheet: `CROSS-SA-EARLY-SIGNAL-MAP-v0.1.md`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4/T6/CN) · Protocol: `../../rituals/daily-protocol.md`
