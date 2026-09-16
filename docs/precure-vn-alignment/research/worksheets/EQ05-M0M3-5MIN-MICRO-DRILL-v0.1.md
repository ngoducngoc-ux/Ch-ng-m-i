# Micro-drill 5′ — EQ-SA05 M0→M3 (ladder · PUSH_D14 = leakage · ≠ auto-treat)

**Mã:** EQ05-M0M3-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T6** · sau/trước `EQ-5MIN` · kèm `PUSH-ALERT-5MIN` · trước claim AUROC M1/M3 SA-05  
**Goal:** ACTIVE · primary ΔPUSH D14 không đổi · M0→M3 exploratory · M4/L3 **CLOSED** · PREP ≠ DONE  
**Spec:** `EQ-SA05-early-warning` · `PUSH-SA05-COMPONENTS` · SAP ES M0–M3

## Một câu

> EQ05-M0M3 5′ = ladder M0 (PUSH_D0+C) → M1 (PUSH_D3/D7) → M2 (+CFU) → M3 (+TURN_ADHERE) — **PUSH_D14 làm early = leakage QC**, không phải evidence; **không** đổi primary · **không** auto-treat ICU / L3.

## Drill (điền)

```text
Y_prim: ΔPUSH D14−D0 — xác nhận không đổi? CÓ
Y_improved: 1{ΔPUSH≤−2} — exploratory? CÓ
M0 (1 dòng PUSH_D0+AGE+STAGE+GROUP): ________
M1 thêm: PUSH_D3 | PUSH_D7 | cả hai — ghi: ________
M2 thêm: CFU_D0/D3 — ghi: ________
M3 thêm: TURN_ADHERE — ghi: ________
PUSH_D14 làm predictor early? KHÔNG — leakage vì: ________
Component = co-primary / thay ΔPUSH D14? KHÔNG
Gộp Y với SA-01/02? KHÔNG
AUROC M3 sandbox = claim ICU? KHÔNG
X / omics ICU / L3 hôm nay? CLOSED
Cặp đã đụng: EQ-5MIN | EQ-M0M3 | EQ02-M0M3 | PUSH-ALERT | PUSH-5MIN | ALERT | LEAKAGE | PB003 — ghi: ________
1 việc nhỏ ≤30′ (EQ-SA05 Drill 10′ / PUSH-ALERT / EH-SA05): ________
Đóng Goal / mở L3 vì EQ05-M0M3? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| EQ đầy đủ | `EQ-SA05` · Drill 10′ |
| EQ 5′ chung | `EQ-5MIN` |
| SA-01 / SA-02 siblings | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` |
| PUSH × ALERT | `PUSH-ALERT-5MIN` · `PUSH-5MIN` · `PUSH-SA05-COMPONENTS` |
| Leakage | `LEAKAGE-5MIN` (không PUSH_D14 early) |
| Primary SA-05 | `PB003-5MIN` |
| PB×EQ | **`PB007-EQ-5MIN`** · `PB007-5MIN` |
| CROSS×EQ | **`CROSS-EQ-5MIN`** · `CROSS-SA-5MIN` |
| PB003×EQ | **`PB003-EQ-5MIN`** · `PB003-5MIN` |

## Cấm

- Báo AUROC M1/M3 sandbox như early-signal ICU lâm sàng  
- Dùng PUSH_D14 / outcome D14 làm predictor “early”  
- Component = co-primary · auto-treat · mở X/L3 vì đã viết ladder  

## Liên kết

- EQ: `../equations/EQ-SA05-early-warning-v0.1.md` · Daily stack: `DAILY-STACK-AFTER-STREAK3` (T6)  
- Protocol: `../../rituals/daily-protocol.md` · Gap: `EQ-EH-SA05-GAP`
