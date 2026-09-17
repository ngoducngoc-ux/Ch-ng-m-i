# IMAGEJ-EQ — thẻ khoa học 1 trang (PCT QA × ladder · ≠ PCT_D21)

**Mã:** IMAGEJ-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `IMAGEJ-EQ-5MIN-MICRO-DRILL` · IMAGEJ-SCIENCE-CARD · IMAGEJ-EPI-EQ · EPI-EQ · EQ-M0M3 · LEAKAGE-EQ · PB001-EQ  
**Dùng khi:** STREAK≥3 · Daily stack **T2** · trước claim AI trên % biểu mô · cặp IMAGEJ×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NOW · FILL-AID · NatMed · ALERT · HAWTHORNE · MEDIA → tick **19/09** trước  
**Goal:** ACTIVE · primary D21 ImageJ không đổi · QA trước AUROC · M0–M3 trên \(Z\) D0–D7 · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp IMAGEJ×EQ**: SOP ảnh/rater **và** 1 dòng ladder M0–M3 trên PCT_EPITH ≤D7 — không PCT_D21 làm early feature; QA trước mọi claim AI. Khác `IMAGEJ-SCIENCE-CARD` (alone) / `IMAGEJ-EPI-EQ` — thẻ này neo **QA × ladder** chung.

**Mở song song:** thẻ này · `IMAGEJ-EQ-5MIN` · `IMAGEJ-SCIENCE-CARD` · `IMAGEJ-EPI-EQ-SCIENCE-CARD` · `EPI-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `LEAKAGE-EQ-SCIENCE-CARD`

## Giữ / bỏ (IMAGEJ × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) ≤D7 | Ladder = AUROC khi SOP lệch |
| **Primary \(t^*\)** | D21 · Y = 100% biểu mô ImageJ | Đổi primary vì densify |
| **Early \(t'\)** | D0 / D3 / D7 | PCT_EPITH_D21 làm predictor early |
| **SOP / rater** | Khoảng cách · ánh sáng · góc · 2nd rater | Claim đủ QA vì đã điền |
| **Omics / L3** | **CLOSED** | Order PEA vì IMAGEJ×EQ |
| **Order / Goal** | KHÔNG từ densify | Train AI / đóng Goal vì PREP |

## Phương trình ranh giới

```text
SOP/rater  +  EQ ladder M0–M3 trên PCT/Z ≤D7
≠  PCT_D21 early  ≠  AUROC khi SOP lệch  ≠  order PEA
Ôn IMAGEJ×EQ  ≠  UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T2 · t* = D21 ImageJ — ĐÚNG
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________ (thường EQ-M0M3)
t' ôn: D0|D3|D7 — ________ (không D21)
SOP ảnh đủ? CÓ|CHƯA — thiếu: ________
Blinded / 2nd rater subset? CÓ|CHƯA|N/A — ________
1 dòng Z PCT / M0→M3 (không D21 feature): ________
PCT_D21 = predictor early? KHÔNG
AUROC khi ảnh chưa SOP / order PEA vì QA giấy? KHÔNG
Cặp **`CROSS-EQ-SCIENCE-CARD`** / IMAGEJ-EPI-EQ / EPI-EQ / LEAKAGE-EQ hôm nay? ________
1 việc ≤30′ (SOP skim / EQ Drill 10′ / EPI): ________
Order omics / đóng Goal vì IMAGEJ×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở IMAGEJ + EQ sibling thẻ riêng trước cặp? ________
QA+ladder = lý do PCT_D21 early / train AI? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | IMAGEJ×EQ bridge 1 trang |
| `IMAGEJ-EQ-5MIN` | Drill điền |
| `IMAGEJ-SCIENCE-CARD` / QA | SOP · rater alone |
| `IMAGEJ-EPI-EQ` / `EPI-EQ` | Triple / window×ladder đã densify |
| `EQ-M0M3` / `LEAKAGE-EQ` | Ladder / anti-leak |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- AUROC trên PCT khi ảnh chưa SOP  
- PCT D21 = early feature · order PEA / UpdateGoal trên PREP  

## Liên kết

`IMAGEJ-EQ-5MIN-MICRO-DRILL` · `IMAGEJ-SCIENCE-CARD` · `IMAGEJ-EPI-EQ-SCIENCE-CARD` · `EPI-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `LEAKAGE-EQ-SCIENCE-CARD` · `PB001-EQ-5MIN` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
