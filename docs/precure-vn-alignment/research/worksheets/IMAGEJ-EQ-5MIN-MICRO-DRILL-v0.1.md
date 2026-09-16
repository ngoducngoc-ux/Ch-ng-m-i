# Micro-drill 5′ — IMAGEJ × EQ (PCT QA · ladder Z · ≠ PCT_D21)

**Mã:** IMAGEJ-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T2** · sau `IMAGEJ-QA-5MIN` / `IMAGEJ-EPI-5MIN` / `EQ-M0M3-5MIN` / `EPI-EQ-5MIN` · trước claim AI trên % biểu mô  
**Goal:** ACTIVE · primary D21 ImageJ không đổi · QA trước AUROC · M0–M3 trên \(Z\) D0–D7 · L3 CLOSED · PREP ≠ DONE  

## Một câu

> IMAGEJ×EQ 5′ = SOP ảnh/rater **và** 1 dòng ladder M0–M3 trên PCT_EPITH ≤D7 — không PCT_D21 làm early feature; QA trước mọi claim AI.

## Drill (điền)

```text
t* = D21 · Y = biểu mô 100% ImageJ — ĐÚNG
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________ (thường EQ-M0M3)
t' ôn: D0 | D3 | D7 — chọn: ________
SOP ảnh đủ (khoảng cách/ánh sáng/góc)? CÓ | CHƯA — thiếu: ________
Blinded / 2nd rater subset? CÓ | CHƯA | N/A
1 dòng Z PCT / M0→M3 (không D21 feature): ________
PCT_D21 = predictor early? KHÔNG
AUROC khi ảnh chưa SOP / order PEA vì QA giấy? KHÔNG
Cặp đã đụng: IMAGEJ-QA | IMAGEJ-EPI | EPI-EQ | EQ-M0M3 | LEAKAGE-EQ | PB001-EQ — ghi: ________
1 việc nhỏ ≤30′ (SOP skim / EQ Drill 10′ / EPI): ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| IMAGEJ QA alone | `IMAGEJ-QA-5MIN` · `IMAGEJ-EPI-5MIN` |
| EPI×EQ | `EPI-EQ-5MIN` · `EPI-5MIN` · `EPI-SA01-EARLY-WINDOW` |
| EQ / leak | `EQ-M0M3-5MIN` · `LEAKAGE-EQ-5MIN` |
| ALERT A | `ALERT-EQ-5MIN` · `ALERT-SA01` |
| PB-001 | `PB001-EQ-5MIN` · `PB001-5MIN` |

## Cấm

- AUROC trên PCT khi ảnh chưa SOP  
- PCT D21 = early feature · order PEA vì “QA xong trên giấy”  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2) · Protocol: `../../rituals/daily-protocol.md`  
- Endpoints Ngày 10
