# Micro-drill 5′ — VAS × EQ (SA-02 0–10 · ladder Z · ≠ VAS_D3 early)

**Mã:** VAS-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4** · sau `VAS-5MIN` / `EQ02-M0M3-5MIN` / `VAS-LEAK-5MIN` / `PB002-EQ-5MIN` · trước claim “đã có early-signal SA-02”  
**Goal:** ACTIVE · primary ΔVAS D3 không đổi · eCRF **0–10** · M0–M3 trên \(Z\) D1/CFU · L3 CLOSED · PREP ≠ DONE  
**DOI:** [10.1186/1745-6215-15-263](https://doi.org/10.1186/1745-6215-15-263) (STPIS — chỉ so sánh literature)

## Một câu

> VAS×EQ 5′ = giữ **0–10** + 1 dòng ladder M0–M3 trên \(Z\) D1/CFU — **không** VAS_D3 làm predictor early; không đổi eCRF 0–100 vì STPIS mm.

## Drill (điền)

```text
eCRF thang: 0–10 — ĐÚNG (không 0–100)
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________ (thường EQ02)
t* primary: ΔVAS D3 — ĐÚNG
t' early: D1 | CFU_D0 — chọn (không VAS_D3): ________
1 dòng Z / M0→M3 (không VAS_D3 feature): ________
M1 sandbox có VAS_D3 → leakage? CÓ
Gộp Y với SA-01/05? KHÔNG
Order omics / đóng Goal vì VAS×EQ? KHÔNG
Cặp đã đụng: VAS | VAS-LEAK | VAS-LEAK-EQ | EQ02 | PB002-EQ | SYNTH-EQ | EPI-EQ — ghi: ________
1 việc nhỏ ≤30′ (LEAKAGE/EQ Drill 10′ / SHIFT): ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| VAS alone | `VAS-5MIN` · `VAS-SCALE-HARMONIZE-SA02` |
| VAS-LEAK×EQ | **`VAS-LEAK-EQ-5MIN`** · `VAS-LEAK-5MIN` |
| Leak / synth | `VAS-LEAK-5MIN` · `LEAK-CROSS-5MIN` · `SYNTH-EQ-5MIN` |
| EQ / PB-002 | `EQ02-M0M3-5MIN` · `PB002-EQ-5MIN` · `PB007-EQ-5MIN` |
| EPI sibling | `EPI-EQ-5MIN` · `EPI-5MIN` |
| CROSS | `CROSS-EQ-5MIN` · `CROSS-SA-5MIN` |
| ALERT×EQ | **`ALERT-EQ-5MIN`** · `ALERT-5MIN` |

## Cấm

- Đổi eCRF 0–100 trừ amendment `[CẦN XÁC NHẬN]`  
- VAS_D3 = early predictor · gộp Y · mở L3  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4) · Protocol: `../../rituals/daily-protocol.md`  
- PB-002: `PB002-EQ-5MIN`
