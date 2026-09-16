# Micro-drill 5′ — PUSH SA-05 early-signal (components trước D14)

**Mã:** PUSH-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T6** · EQ-SA05 · bridge #4/#8 · sau `ALERT-5MIN` · trước claim “đã có early-signal SA-05”  
**Goal:** ACTIVE · primary ΔPUSH D14 không đổi · L3 CLOSED · PREP ≠ DONE · không auto-treat ICU  
**DOI:** Stotts 2001 [10.1093/gerona/56.12.m795](https://doi.org/10.1093/gerona/56.12.m795)

## Một câu

> Early-signal ICU nhìn **exudate / TURN_ADHERE** (và QA ảnh) **trước D14** — **không** thay primary ΔPUSH D14; **không** coi component = co-primary; **không** deploy ALERT ra app ICU.

## Drill (điền)

```text
t* primary: ΔPUSH D14 — ĐÚNG | SAI
t' early hôm nay: exudate | TURN_ADHERE | tissue | area | PUSH_D14 — chọn (không D14): ________
Component = co-primary? KHÔNG — vì N=80 / confounder ICU: ________
ALERT B deploy app ICU? KHÔNG — vì: ________
Order omics ICU vì Stotts/EQ? KHÔNG — L3 CLOSED
1 việc nhỏ ≤30′ (EQ / ALERT / rater QA / shift): ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Components đầy đủ | `PUSH-SA05-COMPONENTS` |
| ALERT | `ALERT-5MIN` · atlas SA-05 |
| Leakage | atlas SA-05 · không PUSH_D14 làm early |
| Cặp SA-01/02 | `EPI-5MIN` · `VAS-5MIN` |
| EQ 5′ | `EQ-5MIN-MICRO-DRILL` (T6) |
| Omics gate | `PB009-5MIN` · L1L2L3 gate |

## Cấm

- Component thay \(\Delta\)PUSH D14 / co-primary  
- Deploy ALERT B ra app ICU  
- Order omics ICU vì đã ôn PUSH/EQ  
- Synthetic SA-05 chốt ngưỡng lâm sàng  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T6)  
- Shift: `PRECURE-SHIFT-CROSS-SA-BANK` · Protocol: `../../rituals/daily-protocol.md`
