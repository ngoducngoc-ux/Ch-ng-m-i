# Micro-drill 5′ — SAP-ES × EQ (leakage §7 · ladder Z · ≠ primary)

**Mã:** SAP-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5** · sau `SAP-ES-5MIN` · kèm `EQ-M0M3` / `EQ02-M0M3` / `EQ05-M0M3` · trước claim interim / adaptive / “đã có ES trong SAP”  
**Goal:** ACTIVE · primary không đổi · M0–M3 exploratory trên \(Z\) · §7 leakage · L3 **CLOSED** · PREP ≠ DONE  

## Một câu

> SAP×EQ 5′ = neo 1 SA → ladder M0–M3 trên \(Z\) **khớp** SAP-ES (không đảo primary) — nhắc **§7 leakage** + 7.1 — **không** adaptive · **không** dùng \(Y(t^*)\) làm early feature.

## Drill (điền)

```text
SA neo: 01 | 02 | 05 — chọn: ________
EQ sibling: EQ-M0M3 | EQ02-M0M3 | EQ05-M0M3 — chọn: ________
Y(t*) primary (không đổi): ________
1 dòng Z / M0→M3 trong SAP-ES: ________
§7 leakage check (Y(t*) làm early?): KHÔNG — vì: ________
7.1 / interim / adaptive hôm nay? KHÔNG — ghi: ________
X / PEA / L3 vì đã viết SAP×EQ? CLOSED
Cặp đã đụng: SAP-ES | EQ-5MIN | EQ ladders | AMENDMENT-ES | TRIPOD-EQ | LEAK-CROSS | PB007-EQ — ghi: ________
1 việc nhỏ ≤30′ (SAP-SA01-ES skim / EQ Drill 10′ / LEAK-CROSS): ________
Đóng Goal / đổi primary vì SAP×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| SAP alone | `SAP-ES-5MIN` · `SAP-SA01-ES` (và SA-02/05 draft) |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| Amendment | `AMENDMENT-ES-5MIN` · **`AMENDMENT-EQ-5MIN`** · `TT43-AMEND-5MIN` |
| Leakage | `LEAK-CROSS-5MIN` · `LEAKAGE-5MIN` |
| AI | `TRIPOD-EQ-5MIN` |

## Cấm

- Đổi primary / adaptive / interim vì đã điền ladder  
- Outcome \(t^*\) làm predictor early trong SAP-ES  
- Mở G2/L3 vì “SAP đã có ES”  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5) · Protocol: `../../rituals/daily-protocol.md`  
- EQ: `EQ-SA01` · `EQ-SA02` · `EQ-SA05`
