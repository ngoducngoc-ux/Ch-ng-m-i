# Micro-drill 5′ — PUSH × ALERT (SA-05 · components trước D14 · ≠ app ICU)

**Mã:** PUSH-ALERT-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T6** · EQ-SA05 · sau/trước `PUSH-5MIN` + `ALERT-5MIN` · trước claim “ES SA-05” / deploy ICU  
**Goal:** ACTIVE · primary ΔPUSH D14 không đổi · ALERT B nội bộ · L3 CLOSED · PREP ≠ DONE  
**DOI:** Stotts 2001 [10.1093/gerona/56.12.m795](https://doi.org/10.1093/gerona/56.12.m795)

## Một câu

> PUSH×ALERT 5′ = early ICU trên **exudate / TURN_ADHERE** (ALERT B có cột làm/không làm) **trước D14** — **không** co-primary · **không** PUSH_D14 làm early · **không** deploy app ICU / auto-treat.

## Drill (điền)

```text
t* primary: ΔPUSH D14 — xác nhận? CÓ
t' early: exudate | TURN_ADHERE | tissue | area | PUSH_D14 — chọn (không D14): ________
ALERT B hôm nay (1 hàng atlas): ________
Component = co-primary / thay ΔPUSH D14? KHÔNG
Deploy ALERT ra app ICU / auto-treat? KHÔNG
PUSH_D14 làm predictor early? KHÔNG
Order omics ICU vì PUSH-ALERT? KHÔNG
Cặp đã đụng: PUSH-5MIN | ALERT-5MIN | ALERT-HAWTHORNE | EQ-5MIN | LEAKAGE | PB003 | L1L2L3 — ghi: ________
1 việc nhỏ ≤30′ (components sheet / ALERT B / EQ-SA05 / rater QA): ________
Đóng Goal / mở L3 vì PUSH-ALERT? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| PUSH alone | `PUSH-5MIN` · `PUSH-SA05-COMPONENTS` |
| ALERT alone | `ALERT-5MIN` · atlas SA-05 |
| ALERT×Hawthorne | `ALERT-HAWTHORNE-5MIN` |
| EQ T6 | `EQ-5MIN` · `EQ-SA05` |
| Leakage | `LEAKAGE-5MIN` (không PUSH_D14 early) |
| Primary SA-05 | `PB003-5MIN` |

## Cấm

- Component = co-primary / thay ΔPUSH D14  
- Deploy ALERT B ra app ICU  
- PUSH_D14 = early feature / order omics vì drill  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T6) · Protocol: `../../rituals/daily-protocol.md`  
- Components: `PUSH-SA05-COMPONENTS-v0.1.md`
