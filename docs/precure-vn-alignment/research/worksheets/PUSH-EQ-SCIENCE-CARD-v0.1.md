# PUSH-EQ — thẻ khoa học 1 trang (components × ladder · ≠ D14 early)

**Mã:** PUSH-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `PUSH-EQ-5MIN-MICRO-DRILL` · PUSH-ALERT-EQ · VAS-EQ · EQ05-M0M3 · PB003-EQ · ALERT-EQ · CLIN_EVENT-EQ  
**DOI:** Stotts 2001 [10.1093/gerona/56.12.m795](https://doi.org/10.1093/gerona/56.12.m795)  
**Dùng khi:** STREAK≥3 · Daily stack **T6** · trước claim “đã có early-signal SA-05” · cặp PUSH×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NOW · FILL-AID · NatMed · ALERT · HAWTHORNE · MEDIA → tick **19/09** trước · **không** deploy ICU  
**Goal:** ACTIVE · primary ΔPUSH D14 không đổi · 1 component \(Z\) + 1 dòng ladder · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp PUSH×EQ**: 1 component \(Z\) trước D14 **và** 1 dòng ladder M0–M3 — không thay primary; component ≠ co-primary; không deploy ALERT ICU. Khác `PUSH-ALERT-EQ` (components×ALERT) — thẻ này neo **PUSH × ladder** chung.

**Mở song song:** thẻ này · `PUSH-EQ-5MIN` · `PUSH-ALERT-EQ-SCIENCE-CARD` · `VAS-EQ-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `PB003-EQ-5MIN` · `PUSH-SA05-COMPONENTS`

## Giữ / bỏ (PUSH × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) ≤D7 (thường EQ05) | Ladder = Dx / AUROC = claim ICU |
| **Primary \(t^*\)** | ΔPUSH D14−D0 | Component = co-primary |
| **Early \(t'\)** | exudate · TURN_ADHERE · tissue · area | PUSH_D14 = early feature |
| **ALERT B** | Nội bộ (nếu đụng) | App ICU · auto-treat |
| **Omics / L3** | **CLOSED** | Order vì đã ôn PUSH×EQ |
| **Order / Goal** | KHÔNG từ densify | Deploy / đóng Goal vì PREP |

## Phương trình ranh giới

```text
1 component Z trước D14  +  EQ ladder M0–M3
≠  co-primary  ≠  PUSH_D14 early  ≠  app ICU
Ôn PUSH×EQ  ≠  UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T6 · t* = ΔPUSH D14 — ĐÚNG
EQ sibling: EQ05-M0M3|EQ-M0M3|EQ02 — ________ (thường EQ05)
t' early: exudate|TURN_ADHERE|tissue|area — ________ (không D14)
1 dòng Z / M0→M3 (không D14 feature): ________
Component = co-primary? KHÔNG
ALERT B deploy app ICU? KHÔNG
Cặp **`CLIN_EVENT-EQ-SCIENCE-CARD`** / VAS-EQ / PUSH-ALERT-EQ / PB003-EQ hôm nay? ________
1 việc ≤30′ (EQ Drill 10′ / ALERT / rater QA): ________
Order omics ICU / đóng Goal vì PUSH×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở PUSH + EQ sibling thẻ riêng trước cặp? ________
Component+ladder = lý do co-primary / app ICU? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | PUSH×EQ bridge 1 trang |
| `PUSH-EQ-5MIN` | Drill điền |
| `PUSH-ALERT-EQ` / components sheet | Pair ALERT / component alone |
| `VAS-EQ` / `EQ05-M0M3` | Sibling / ladder SA-05 |
| `PB003-EQ` | SA-05 support |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Component thay ΔPUSH D14 / co-primary  
- Deploy ALERT ICU · order omics · UpdateGoal trên PREP  

## Liên kết

`PUSH-EQ-5MIN-MICRO-DRILL` · `PUSH-SA05-COMPONENTS` · `PUSH-ALERT-EQ-SCIENCE-CARD` · `VAS-EQ-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `PB003-EQ-5MIN` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
