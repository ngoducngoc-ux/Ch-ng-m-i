# VAS-EQ — thẻ khoa học 1 trang (0–10 × ladder · ≠ VAS_D3 early)

**Mã:** VAS-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `VAS-EQ-5MIN-MICRO-DRILL` · VAS-LEAK-EQ · EPI-EQ · EQ02-M0M3 · PB002-EQ · LEAKAGE-EQ · ALERT-EQ  
**DOI:** STPIS literature [10.1186/1745-6215-15-263](https://doi.org/10.1186/1745-6215-15-263) (chỉ so sánh — không đổi eCRF)  
**Dùng khi:** STREAK≥3 · Daily stack **T4** · trước claim “đã có early-signal SA-02” · cặp VAS×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NOW · FILL-AID · NatMed · ALERT · HAWTHORNE · MEDIA → tick **19/09** trước  
**Goal:** ACTIVE · primary ΔVAS D3 không đổi · eCRF **0–10** · 1 dòng ladder · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp VAS×EQ**: giữ thang **0–10** **và** 1 dòng ladder M0–M3 trên \(Z\) D1/CFU — không VAS_D3 early; không đổi eCRF 0–100 vì STPIS mm. Khác `VAS-LEAK-EQ` (scale×leak) — thẻ này neo **VAS × ladder** chung.

**Mở song song:** thẻ này · `VAS-EQ-5MIN` · `VAS-LEAK-EQ-SCIENCE-CARD` · `EPI-EQ-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `PB002-EQ-5MIN` · `VAS-SCALE-HARMONIZE-SA02`

## Giữ / bỏ (VAS × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) hợp lệ (thường EQ02) | Ladder = VAS_D3 early / AUROC sandbox = BN |
| **Thang eCRF** | 0–10 | Đổi 0–100 trừ amendment `[CẦN XÁC NHẬN]` |
| **Primary \(t^*\)** | ΔVAS D3 | Co-primary / gộp Y SA-01/05 |
| **Early \(t'\)** | VAS_D1 · CFU_D0 | VAS_D3 = early predictor |
| **Omics / L3** | **CLOSED** | Order vì đã ôn VAS×EQ |
| **Order / Goal** | KHÔNG từ densify | Claim ES / đóng Goal vì PREP |

## Phương trình ranh giới

```text
eCRF 0–10  +  Z(t') D1/CFU  +  EQ ladder M0–M3
≠  VAS_D3 early  ≠  gộp Y  ≠  STPIS mm → đổi thang
Ôn VAS×EQ  ≠  UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T4 · eCRF thang: 0–10 — ĐÚNG (không 0–100)
EQ sibling: EQ02-M0M3|EQ-M0M3|EQ05 — ________ (thường EQ02)
t* = ΔVAS D3 — ĐÚNG
t' early: D1|CFU_D0 — ________ (không VAS_D3)
1 dòng Z / M0→M3 (không VAS_D3 feature): ________
M1 sandbox có VAS_D3 → leakage? CÓ
Gộp Y với SA-01/05? KHÔNG
Cặp **`PUSH-EQ-SCIENCE-CARD`** / EPI-EQ / VAS-LEAK-EQ / PB002-EQ hôm nay? ________
1 việc ≤30′ (LEAKAGE / EQ Drill 10′ / SHIFT): ________
Order omics / đóng Goal vì VAS×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở VAS + EQ sibling thẻ riêng trước cặp? ________
Scale+ladder = lý do VAS_D3 early / đổi eCRF? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | VAS×EQ bridge 1 trang |
| `VAS-EQ-5MIN` | Drill điền |
| `VAS-LEAK-EQ` / harmonize | Scale×leak / literature |
| `EPI-EQ` / `EQ02-M0M3` | Sibling window / ladder SA-02 |
| `PB002-EQ` | SA-02 support |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Đổi eCRF 0–100 trừ amendment `[CẦN XÁC NHẬN]`  
- VAS_D3 = early predictor · gộp Y · mở L3 / UpdateGoal trên PREP  

## Liên kết

`VAS-EQ-5MIN-MICRO-DRILL` · `VAS-SCALE-HARMONIZE-SA02` · `VAS-LEAK-EQ-SCIENCE-CARD` · `EPI-EQ-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `PB002-EQ-5MIN` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
