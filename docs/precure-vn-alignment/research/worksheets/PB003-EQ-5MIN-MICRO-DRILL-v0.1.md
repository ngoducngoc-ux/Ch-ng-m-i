# Micro-drill 5′ — PB-003 × EQ (SA-05 alert · ladder Z · ≠ deploy ICU)

**Mã:** PB003-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T6 / CN** · sau `PB003-5MIN` / `EQ05-M0M3-5MIN` / `PUSH-ALERT-5MIN` / `PB001-EQ-5MIN` · trước claim “đã có early-signal SA-05”  
**Goal:** ACTIVE · support SA-05 · primary ΔPUSH D14 không đổi · M0–M3 trên \(Z\) sớm · \(X\) **CLOSED** · không auto-treat ICU · PREP ≠ DONE  

## Một câu

> PB003×EQ 5′ = 1 \(Z\) cảnh báo (exudate/TURN/`clin_event`) **và** 1 dòng ladder M0–M3 — exploratory trước PUSH tăng hạng; không đổi primary; không deploy ALERT ICU.

## Drill (điền)

```text
Support SA-05 (không cờ đầu)? ĐÚNG
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________ (thường EQ05)
Y(t*): ΔPUSH D14 — ĐÚNG
t' ôn: D0 | D3 | D7 · exudate | TURN — chọn (không PUSH_D14): ________
1 Z ứng viên: ________
1 dòng Z / M0→M3 (X CLOSED): ________
Component / ALERT = co-primary hoặc app ICU? KHÔNG
Gộp Y với SA-01/02? KHÔNG
Order omics / đóng Goal vì PB003×EQ? KHÔNG
Cặp đã đụng: PB003 | PUSH-ALERT | EQ05 | PB007-EQ | L1L2L3-EQ | PB001-EQ — ghi: ________
1 việc nhỏ ≤30′ (PUSH/EQ Drill 10′ / ALERT): ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Thẻ khoa học | **`PB003-EQ-SCIENCE-CARD`** · **`PB007-EQ-SCIENCE-CARD`** · `PB003-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` |
| PB-003 alone | `PB003-5MIN` · EH-SA05 |
| PUSH / ALERT | `PUSH-5MIN` · `PUSH-ALERT-5MIN` · `ALERT-CROSS-5MIN` |
| EQ ladders | `EQ05-M0M3-5MIN` · `PB007-EQ-5MIN` |
| Flagship siblings | `PB001-EQ-5MIN` · `PB002-EQ-5MIN` · `CROSS-EQ-5MIN` |
| Gate | `L1L2L3-EQ-5MIN` · `G2-EQ-5MIN` |
| PUSH×EQ | **`PUSH-EQ-5MIN`** · `PUSH-5MIN` |

## Cấm

- PUSH_D14 = early predictor · ALERT deploy ICU  
- AUROC sandbox = BN · gộp Y · order \(X\)  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T6/CN) · Protocol: `../../rituals/daily-protocol.md`  
- Problem bank: `../problem-bank.md` (PB-003) · **`PB003-EQ-SCIENCE-CARD`** · **`PB003-SCIENCE-CARD`**
