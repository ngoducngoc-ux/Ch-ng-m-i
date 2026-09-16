# Micro-drill 5′ — EPI × EQ (SA-01 window · ladder Z · ≠ PCT_D21)

**Mã:** EPI-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T2** · sau `EPI-5MIN` / `EQ-M0M3-5MIN` / `IMAGEJ-EPI-5MIN` / `PB001-EQ-5MIN` · trước claim “đã có early-signal SA-01”  
**Goal:** ACTIVE · primary D21 không đổi · M0–M3 trên \(Z\) D0–D7 · L3 CLOSED · PREP ≠ DONE · synthetic ≠ BN  

## Một câu

> EPI×EQ 5′ = 1 \(Z\) early-window (PCT_EPITH/CFU/VAS_DRESS/`clin_event`) **và** 1 dòng ladder M0–M3 — **không** PCT_D21 làm predictor early; ImageJ QA trước claim AI trên PCT.

## Drill (điền)

```text
t* primary: D21 biểu mô ImageJ — ĐÚNG
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________ (thường EQ-M0M3)
t' window: D0 | D3 | D7 — chọn (không D21): ________
Z đang ôn: PCT_EPITH | CFU | VAS_DRESS | clin_event — chọn: ________
1 dòng Z / M0→M3 (không PCT_D21): ________
PCT_D21 làm feature early? KHÔNG
Order PEA / AUROC sandbox = BN? KHÔNG
Cặp đã đụng: EPI | IMAGEJ-EPI | EQ-M0M3 | PB001-EQ | PB007-EQ | ALERT — ghi: ________
1 việc nhỏ ≤30′ (IMAGEJ/EQ Drill 10′ / ALERT): ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| EPI alone | `EPI-5MIN` · `EPI-SA01-EARLY-WINDOW` |
| ImageJ | `IMAGEJ-EPI-5MIN` · `IMAGEJ-QA-5MIN` |
| EQ / PB-001 | `EQ-M0M3-5MIN` · `PB001-EQ-5MIN` · `PB007-EQ-5MIN` |
| VAS / PUSH siblings | **`VAS-EQ-5MIN`** · `VAS-5MIN` · `PUSH-5MIN` |
| ALERT / leak | `ALERT-5MIN` · `LEAKAGE-5MIN` |
| IMAGEJ×EQ | **`IMAGEJ-EQ-5MIN`** · `IMAGEJ-QA-5MIN` |
| IMAGEJ-EPI×EQ | **`IMAGEJ-EPI-EQ-5MIN`** · `IMAGEJ-EPI-5MIN` |

## Cấm

- PCT/CFU D21 = early-signal  
- AUROC sandbox = BN · mở PEA vì đã ôn EPI×EQ  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2) · Protocol: `../../rituals/daily-protocol.md`  
- Cờ đầu: `PB001-EQ-5MIN`
- Thẻ khoa học: `EPI-SCIENCE-CARD-v0.1.md`
