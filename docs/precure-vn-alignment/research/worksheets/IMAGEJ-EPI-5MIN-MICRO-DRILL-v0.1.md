# Micro-drill 5′ — ImageJ × EPI (QA ảnh · early window D0–D7)

**Mã:** IMAGEJ-EPI-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T2** · sau/trước `IMAGEJ-QA-5MIN` + `EPI-5MIN` · kèm `EQ-M0M3-5MIN` · trước claim AI trên PCT  
**Goal:** ACTIVE · \(Y_{D21}\) ImageJ không đổi · \(t'\) ∈ {D0,D3,D7} · L3 CLOSED · PREP ≠ DONE  

## Một câu

> IMAGEJ×EPI 5′ = SOP ảnh + blind/rater **và** \(Z\) chỉ trên D0/D3/D7 — **không** PCT_D21 làm early · **không** AUROC khi ảnh lệch SOP · **không** order PEA vì đã QA giấy.

## Drill (điền)

```text
t* = D21 · Y = biểu mô 100% ImageJ — xác nhận? CÓ
t' hôm nay: D0 | D3 | D7 — chọn (không D21): ________
Z ôn: PCT_EPITH | CFU | VAS_DRESS | clin_event — chọn: ________
SOP ảnh (khoảng cách/ánh sáng/góc) đủ? CÓ | CHƯA — thiếu: ________
Blinded / 2nd rater subset? CÓ | CHƯA | N/A
PCT_EPITH_D21 làm predictor early? KHÔNG
AUROC trên PCT khi SOP chưa chuẩn? KHÔNG
Order PEA / mở G2 vì IMAGEJ-EPI? KHÔNG
Cặp đã đụng: IMAGEJ-QA | EPI-5MIN | EQ-M0M3 | EQ-5MIN | LEAKAGE | ALERT | NATMED-ALERT — ghi: ________
1 việc nhỏ ≤30′ (SOP checklist / EPI window / EQ ladder 1 dòng): ________
Đóng Goal vì đã ôn cặp ImageJ×EPI? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| ImageJ alone | `IMAGEJ-QA-5MIN` |
| EPI alone | `EPI-5MIN` · `EPI-SA01-EARLY-WINDOW` |
| EQ ladder | `EQ-M0M3-5MIN` · `EQ-5MIN` · `EQ-SA01` |
| Leakage PCT D21 | `LEAKAGE-5MIN` |
| ALERT / Nat Med | `ALERT-5MIN` · `NATMED-ALERT-5MIN` |
| EPI×EQ | **`EPI-EQ-5MIN`** · `EPI-5MIN` |
| IMAGEJ×EQ | **`IMAGEJ-EQ-5MIN`** · `IMAGEJ-QA-5MIN` |
| IMAGEJ-EPI×EQ | **`IMAGEJ-EPI-EQ-5MIN`** · EQ ladders |

## Cấm

- PCT/CFU D21 = early-signal  
- Train AI trên % khi ảnh chưa QA  
- Order PEA / mở G2 vì đã điền cặp drill  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2) · Protocol: `../../rituals/daily-protocol.md`  
- Window: `EPI-SA01-EARLY-WINDOW-v0.1.md`
