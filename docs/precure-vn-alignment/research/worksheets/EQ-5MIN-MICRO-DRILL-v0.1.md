# Micro-drill 5′ — EQ early-warning (SA-01 / 02 / 05 · T2/T4/T6)

**Mã:** EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T2/T4/T6** · trước/sau Drill 10′ EQ · kèm `EPI-5MIN`/`VAS-5MIN`/`PUSH-5MIN` · khi chỉ còn 5′ nhưng vẫn phải đụng \(Y(t^*)\)/M0–M3  
**Goal:** ACTIVE · primary không đổi · L3/M4 **CLOSED** · synthetic ≠ BN · PREP ≠ DONE  

## Một câu

> EQ 5′ = chọn **1 SA** · nhắc \(Y(t^*)\) · 1 dòng M0→M3 · 1 cấm leakage · **không** mở omics vì đã viết \(\sigma(\ldots)\).

## Drill (điền)

```text
Thứ / SA hôm nay: T2·01 | T4·02 | T6·05 — chọn: ________
Y(t*): ________     t' early (≠ t*): ________
M0 predictors (1 dòng): ________
M3 thêm gì so M0 (1 dòng): ________
Leakage risk hôm nay? CÓ|KHÔNG — biến cấm: ________
M4 / X / L3: CLOSED vì ________
Cặp 5′ đã đụng: EPI|VAS|PUSH|LEAKAGE|ALERT|SYNTH — ghi: ________
1 câu Precure shift (≤20 từ):
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| SA | EQ đầy đủ | Cặp clinical 5′ | Cấm nổi |
|----|-----------|-----------------|---------|
| **01** | `EQ-SA01` Drill 10′ | `EPI-5MIN` · `IMAGEJ-QA-5MIN` | PCT D21 làm early · order PEA |
| **02** | `EQ-SA02` Drill 10′ | `VAS-5MIN` · `LEAKAGE-5MIN` | M1 = VAS_D3 · gộp Y SA khác |
| **05** | `EQ-SA05` Drill 10′ | `PUSH-5MIN` · `ALERT-5MIN` | Component = primary · auto-treat ICU |

## Cấm

- Coi AUROC sandbox / `verify.sh` = evidence BN  
- Đổi primary vì đã điền EQ  
- Mở G2 / order \(X\) vì đã viết M0–M3  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2/T4/T6)  
- Shift: `PRECURE-SHIFT-CROSS-SA-BANK` · Gate: `L1L2L3-DAILY-GATE-CARD` · **`SHIFT-5MIN-MICRO-DRILL`** · **`PB007-5MIN-MICRO-DRILL`** · **`PB001-5MIN-MICRO-DRILL`** · **`PB002-5MIN-MICRO-DRILL`** · **`PB003-5MIN-MICRO-DRILL`** · **`PB005-5MIN-MICRO-DRILL`** · **`PB006-5MIN-MICRO-DRILL`**  
- Study sheet: `../study-sheets/STUDY-SHEET-MULTI-OMICS-ES-DRILL-v0.1.md`  
- Protocol: `../../rituals/daily-protocol.md`
