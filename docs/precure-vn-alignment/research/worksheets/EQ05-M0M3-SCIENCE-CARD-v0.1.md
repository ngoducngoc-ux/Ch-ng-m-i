# EQ05-M0M3 — thẻ khoa học 1 trang (SA-05 ladder · PUSH_D14 = leakage · ≠ auto-treat)

**Mã:** EQ05-M0M3-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `EQ05-M0M3-5MIN-MICRO-DRILL` · EQ-SCIENCE-CARD · EQ-SIBLING-MAP · PB003 · PUSH-ALERT · LEAKAGE  
**Dùng khi:** STREAK≥3 · Daily stack **T6** · trước AUROC M1/M3 SA-05 · sibling SA-05  
**Ưu tiên STREAK&lt;3:** **`STREAK3-EQ-5MIN-SCIENCE-CARD`** · NOW · FILL-AID → tick **19/09** · **không** mở ladder  
**Goal:** ACTIVE · \(Y_{\text{prim}}\) ΔPUSH D14 không đổi · M0→M3 exploratory · PUSH_D14 early = QC leakage · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **ladder SA-05**: M0(PUSH_D0+C) → M1(PUSH_D3/D7) → M2(+CFU) → M3(+TURN_ADHERE) — **PUSH_D14 làm early = leakage QC**, không phải evidence ICU. Khác `EQ02-M0M3-SCIENCE-CARD` (VAS) — thẻ này chỉ **SA-05 · PUSH · ≠ auto-treat**.

**Mở song song:** thẻ này · `EQ05-M0M3-5MIN` · `EQ-SCIENCE-CARD` · `EQ-SIBLING-MAP-SCIENCE-CARD` · `PB003-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · **`PUSH-ALERT-SCIENCE-CARD`** · `PUSH-ALERT-5MIN`

## M0–M3 → giữ / bỏ

| Bậc | Predictors (ý) | Giữ | Bỏ |
|-----|----------------|-----|-----|
| **M0** | PUSH_D0 + AGE + STAGE_NPUAP + GROUP | Baseline early | Claim baseline = Dx ICU |
| **M1** | + PUSH_D3 / PUSH_D7 | Chuỗi sớm trước D14 | PUSH_D14 trong feature “early” |
| **M2** | + CFU_D0 / CFU_D3 | Nhiễm / burden | Gộp \(Y\) với SA-01/02 |
| **M3** | + TURN_ADHERE | Full early + xoay trở | Auto-treat từ AUROC |
| **Leakage QC** | PUSH_D14 làm predictor | **QC only** | AUROC M1/M3 = evidence ICU |
| **M4 / \(X\)** | Omics ICU | **CLOSED** đến G2 | Order omics vì đã viết ladder |

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Y_prim: ΔPUSH D14−D0 — không đổi? CÓ
Y_improved: 1{ΔPUSH≤−2} exploratory? CÓ
M0|M1|M2|M3 (1 dòng mỗi): ________
PUSH_D14 làm early? KHÔNG — leakage vì: ________
Component = co-primary / thay ΔPUSH D14? KHÔNG
AUROC M3 sandbox = claim ICU? KHÔNG
Gộp Y với SA-01/02? KHÔNG
X / L3 ICU: CLOSED vì ________
Sibling SA-01/02 hôm nay? EQ-M0M3|EQ02|không — ________
1 việc ≤30′ (EQ-SA05 / PUSH-ALERT / EH-SA05): ________
Đóng Goal / mở L3? KHÔNG
```

## Checklist 15′

```text
Đã mở EQ-SIBLING-MAP chọn sibling SA-05? ________
Leakage t* (PUSH_D14) trong feature early? KHÔNG (trừ sandbox QC)
Z rồi X (PB-007)? CÓ · X CLOSED hôm nay
Auto-treat / app ICU từ model? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | SA-05 M0–M3 + PUSH_D14 leakage 1 trang |
| `EQ05-M0M3-5MIN` | Drill điền |
| `EQ-M0M3-SCIENCE-CARD` | Sibling SA-01 |
| `EQ02-M0M3-SCIENCE-CARD` | Sibling SA-02 |
| `EQ-SCIENCE-CARD` | 3 SA ladder |
| `EQ-SIBLING-MAP-SCIENCE-CARD` | Chọn sibling |
| `PB003-SCIENCE-CARD` | Primary SA-05 |
| `PUSH-ALERT` / `LEAKAGE` | ALERT ≠ Dx · pitfall thời gian |
| `STREAK3-EQ-5MIN-SCIENCE-CARD` | Cổng trước ≥3 |

## Cấm

- Báo AUROC M1/M3 sandbox như early-signal ICU lâm sàng  
- PUSH_D14 / outcome D14 làm predictor “early”  
- Component = co-primary · auto-treat · mở X/L3 vì đã viết ladder  
- Nhảy ladder khi STREAK&lt;3 · UpdateGoal trên PREP  

## Liên kết

`EQ05-M0M3-5MIN-MICRO-DRILL` · `EQ-SCIENCE-CARD` · `EQ-SIBLING-MAP-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `PB003-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · **`PUSH-ALERT-SCIENCE-CARD`** · `PUSH-ALERT-5MIN` · `PUSH-5MIN` · `STREAK3-EQ-5MIN-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
