# Micro-drill 5′ — IMAGEJ × EPI × EQ (QA ảnh · window D0–D7 · ladder Z)

**Mã:** IMAGEJ-EPI-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T2** · sau `IMAGEJ-EPI-5MIN` / `IMAGEJ-EQ-5MIN` / `EPI-EQ-5MIN` · trước claim AI trên PCT  
**Goal:** ACTIVE · \(Y_{D21}\) ImageJ không đổi · \(t'\) ∈ {D0,D3,D7} · QA trước AUROC · L3 CLOSED · PREP ≠ DONE  
**≠** `IMAGEJ-EQ-5MIN` (QA×ladder) — drill này = **EPI window + QA + ladder** cùng lúc  

## Một câu

> IMAGEJ-EPI×EQ 5′ = SOP/rater + \(t'\) D0/D3/D7 **và** 1 dòng ladder M0–M3 trên PCT/CFU/VAS ≤D7 — không PCT_D21 early · không AUROC khi SOP lệch.

## Drill (điền)

```text
t* = D21 · Y = biểu mô 100% ImageJ — ĐÚNG
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________ (thường EQ-M0M3)
t' hôm nay: D0 | D3 | D7 — chọn (không D21): ________
Z ôn: PCT_EPITH | CFU | VAS_DRESS | clin_event — chọn: ________
SOP ảnh đủ? CÓ | CHƯA — thiếu: ________
Blinded / 2nd rater? CÓ | CHƯA | N/A
1 dòng Z / M0→M3 (không PCT_D21 feature): ________
PCT_D21 early / AUROC khi SOP lệch / order PEA? KHÔNG
Cặp đã đụng: IMAGEJ-EPI | IMAGEJ-EQ | EPI-EQ | EQ-M0M3 | LEAKAGE-EQ | NATMED-ALERT-EQ — ghi: ________
1 việc nhỏ ≤30′ (SOP / EPI window / EQ Drill 10′): ________
Đóng Goal vì IMAGEJ-EPI×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| IMAGEJ×EPI alone | `IMAGEJ-EPI-5MIN` · `IMAGEJ-QA-5MIN` · `EPI-5MIN` |
| IMAGEJ×EQ / EPI×EQ | `IMAGEJ-EQ-5MIN` · `EPI-EQ-5MIN` |
| EQ / leak | `EQ-M0M3-5MIN` · `LEAKAGE-EQ-5MIN` |
| NatMed / ALERT | `NATMED-ALERT-EQ-5MIN` · `ALERT-EQ-5MIN` |

## Cấm

- PCT/CFU D21 = early-signal · train AI khi ảnh chưa QA  
- Order PEA / mở G2 vì đã điền cặp×EQ  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2) · Protocol: `../../rituals/daily-protocol.md`  
- Window: `EPI-SA01-EARLY-WINDOW-v0.1.md`
