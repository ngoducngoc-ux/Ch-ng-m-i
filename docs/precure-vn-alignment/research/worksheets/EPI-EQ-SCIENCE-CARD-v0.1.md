# EPI-EQ — thẻ khoa học 1 trang (early window × ladder · ≠ PCT_D21)

**Mã:** EPI-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `EPI-EQ-5MIN-MICRO-DRILL` · EPI-SCIENCE-CARD · IMAGEJ-EPI-EQ · ALERT-EQ · EQ-M0M3 · PB001-EQ · LEAKAGE-EQ  
**Dùng khi:** STREAK≥3 · Daily stack **T2** · trước claim “đã có early-signal SA-01” · cặp EPI×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NOW · FILL-AID · NatMed · ALERT · HAWTHORNE · MEDIA → tick **19/09** trước  
**Goal:** ACTIVE · \(t^*\) D21 cố định · \(t'\) ∈ {D0,D3,D7} · 1 dòng ladder · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp EPI×EQ**: 1 \(Z\) early-window (PCT/CFU/VAS/`clin_event`) **và** 1 dòng ladder M0–M3 — không PCT_D21 early; ImageJ QA trước AUROC; không order PEA vì densify. Khác `EPI-SCIENCE-CARD` (alone) / `IMAGEJ-EPI-EQ` — thẻ này neo **window × ladder** chung.

**Mở song song:** thẻ này · `EPI-EQ-5MIN` · `EPI-SCIENCE-CARD` · `IMAGEJ-EPI-EQ-SCIENCE-CARD` · `ALERT-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `PB001-EQ-5MIN` · `EPI-SA01-EARLY-WINDOW`

## Giữ / bỏ (EPI × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) ≤D7 | Ladder = AUROC BN / PCT_D21 feature |
| **Primary \(t^*\)** | D21 · Y = 100% biểu mô ImageJ | Đổi primary vì densify |
| **Early \(t'\)** | D0 / D3 / D7 | D21 làm \(t'\) |
| **\(Z\)** | PCT_EPITH / CFU / VAS_DRESS / clin_event | PCT_D21 = early predictor |
| **Omics / L3** | **CLOSED** | Order PEA vì EPI×EQ |
| **Order / Goal** | KHÔNG từ densify | Train AI / đóng Goal vì PREP |

## Phương trình ranh giới

```text
t* = D21 ImageJ cố định
t' ∈ {D0,D3,D7}  +  Z(t')  +  EQ ladder M0–M3
≠  PCT_D21 early  ≠  AUROC sandbox = BN  ≠  order PEA
Ôn EPI×EQ  ≠  UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T2 · t* = D21 ImageJ — ĐÚNG
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________ (thường EQ-M0M3)
t' hôm nay: D0|D3|D7 — ________ (không D21)
Z đang ôn: PCT_EPITH|CFU|VAS_DRESS|clin_event — ________
1 dòng Z / M0→M3 (không PCT_D21): ________
PCT_D21 làm feature early? KHÔNG
Order PEA / AUROC sandbox = BN? KHÔNG
Cặp **`VAS-EQ-SCIENCE-CARD`** / ALERT-EQ / IMAGEJ-EPI-EQ / PB001-EQ hôm nay? ________
1 việc ≤30′ (IMAGEJ QA / EQ Drill 10′ / ALERT): ________
Order omics / đóng Goal vì EPI×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở EPI + EQ sibling thẻ riêng trước cặp? ________
Window+ladder = lý do PCT_D21 early / mở PEA? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | EPI×EQ bridge 1 trang |
| `EPI-EQ-5MIN` | Drill điền |
| `EPI-SCIENCE-CARD` / window sheet | Window alone |
| `IMAGEJ-EPI-EQ` / `ALERT-EQ` | Pair / ALERT bridges đã densify |
| `EQ-M0M3` / `PB001-EQ` | Ladder / cờ đầu |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- PCT/CFU D21 = early-signal  
- AUROC sandbox = BN · mở PEA / UpdateGoal trên PREP  

## Liên kết

`EPI-EQ-5MIN-MICRO-DRILL` · `EPI-SCIENCE-CARD` · `EPI-SA01-EARLY-WINDOW` · `IMAGEJ-EPI-EQ-SCIENCE-CARD` · `ALERT-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `PB001-EQ-5MIN` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
