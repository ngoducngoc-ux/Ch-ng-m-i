# Micro-drill 5′ — L1→L2→L3 daily gate (AI trước omics)

**Mã:** L1L2L3-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T3** (bắt buộc trước PEA/G2) · T6 ICU · CN PB-009 · mọi lúc muốn nói “AI / omics” · cặp `PB009-5MIN`/`G2-5MIN`/`PEA-5MIN`  
**Goal:** ACTIVE · L3 **CLOSED** mặc định · SYN ≠ N thật · PREP ≠ DONE  

## Một câu

> L1L2L3 5′ = khoanh **L1 / L2 / L3 hôm nay** · L3 luôn **CLOSED** trừ G2+ethics trên N thật — `verify.sh` PASS **không** mở omics.

## Drill (điền)

```text
SA neo: 01 | 02 | 05 — chọn: ________
L1 hôm nay: CHƯA | SYN | N thật — thiếu: ________
L2 hôm nay: CHƯA | SYN QC | N thật — leakage? CÓ|CHƯA
L3: CLOSED vì ________ (G2 / chưa N / ethics / …)
1 rủi ro nếu đảo L3 trước L1/L2:
1 câu PB-009 (AI dọc không cần omics hôm nay):
Cặp đã đụng: PB009 | G2 | PEA | EQ | SHIFT | DEID — ghi: ________
Order PEA/omics hôm nay? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Tầng | Đủ khi | Cặp 5′ | Cấm nổi |
|------|--------|--------|---------|
| **L1** | ID–visit–time–event–\(Z\) | `CLIN_EVENT-5MIN` · `BN-VISIT-5MIN` · `PB004-5MIN` | PHI public |
| **L2** | M0–M3 + de-ID QC; N thật = L2.4 | `EQ-5MIN` · `LEAKAGE-5MIN` · `TRIPOD-5MIN` · `SYNTH-5MIN` | AUROC sandbox = L2.4 |
| **L3** | G2 + G1 + \(X\) thêm giá trị | `G2-5MIN` · `PEA-5MIN` · `PB009-5MIN` | verify PASS = mở G2 |

Card đầy đủ: `L1L2L3-DAILY-GATE-CARD`.

## Cấm

- Tick L2.4 vì `verify.sh` / AUROC synthetic  
- Order PEA / mở G2 vì đã điền đủ ô  
- Coi drill PREP = STREAK DONE / đóng Goal  

## Liên kết

- OMICS-GATES 5′: **`OMICS-GATES-5MIN-MICRO-DRILL`**

- Gate card: `L1L2L3-DAILY-GATE-CARD` · Checklist: `PB-009-AI-BEFORE-OMICS`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T3) · Protocol: `../../rituals/daily-protocol.md`
