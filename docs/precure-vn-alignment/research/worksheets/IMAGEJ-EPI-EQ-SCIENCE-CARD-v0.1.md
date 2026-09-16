# IMAGEJ-EPI-EQ — thẻ khoa học 1 trang (QA × window × ladder · ≠ PCT_D21)

**Mã:** IMAGEJ-EPI-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `IMAGEJ-EPI-EQ-5MIN-MICRO-DRILL` · IMAGEJ-EPI-SCIENCE-CARD · IMAGEJ-EQ · EPI-EQ · EQ-M0M3 · LEAKAGE-EQ · PUSH-ALERT-EQ  
**Dùng khi:** STREAK≥3 · Daily stack **T2** · trước claim AI trên PCT · cặp IMAGEJ-EPI×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · HAWTHORNE · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · \(Y_{D21}\) ImageJ không đổi · \(t'\) ∈ {D0,D3,D7} · QA trước AUROC · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp IMAGEJ-EPI×EQ**: SOP/rater + \(t'\) D0/D3/D7 **và** 1 dòng ladder M0–M3 trên PCT/CFU/VAS ≤D7 — không PCT_D21 early · không AUROC khi SOP lệch. Khác `IMAGEJ-EPI-SCIENCE-CARD` (cặp alone) / `IMAGEJ-EQ` / `EPI-EQ` — thẻ này neo **QA×window × ladder**.

**Mở song song:** thẻ này · `IMAGEJ-EPI-EQ-5MIN` · `IMAGEJ-EPI-SCIENCE-CARD` · `IMAGEJ-EQ-5MIN` · `EPI-EQ-5MIN` · `EQ-M0M3-SCIENCE-CARD` · `LEAKAGE-EQ-SCIENCE-CARD` · `PUSH-ALERT-EQ-SCIENCE-CARD`

## Giữ / bỏ (IMAGEJ-EPI × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) ≤D7 | Ladder = AUROC khi SOP lệch |
| **Primary \(t^*\)** | D21 · Y = 100% biểu mô ImageJ | Đổi primary vì densify |
| **Early \(t'\)** | D0 / D3 / D7 | D21 làm \(t'\) / PCT_D21 early |
| **SOP / rater** | Khoảng cách · ánh sáng · 2nd rater | Claim đủ QA vì đã điền |
| **Omics / L3** | **CLOSED** | Order PEA vì IMAGEJ-EPI×EQ |
| **Order / Goal** | KHÔNG từ densify | Deploy AI / đóng Goal vì PREP |

## Phương trình ranh giới

```text
SOP/rater + t' ∈ {D0,D3,D7}  +  EQ ladder M0–M3 trên Z ≤D7
≠  PCT_D21 early  ≠  AUROC khi SOP lệch  ≠  order PEA
Ôn IMAGEJ-EPI×EQ  ≠  train AI / UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T2 · t* = D21 ImageJ — ĐÚNG
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________ (thường EQ-M0M3)
t' hôm nay: D0|D3|D7 — ________ (không D21)
Z ôn: PCT_EPITH|CFU|VAS_DRESS|clin_event — ________
SOP ảnh đủ? CÓ|CHƯA — thiếu: ________
Blinded / 2nd rater? CÓ|CHƯA|N/A — ________
1 dòng Z / M0→M3 (không PCT_D21 feature): ________
PCT_D21 early / AUROC khi SOP lệch / order PEA? KHÔNG
Cặp **`PUSH-ALERT-EQ-SCIENCE-CARD`** / LEAKAGE-EQ / VAS-LEAK-EQ / EPI-EQ hôm nay? ________
1 việc ≤30′ (SOP / EPI window / EQ Drill 10′): ________
Đóng Goal vì IMAGEJ-EPI×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở IMAGEJ-EPI + EQ sibling thẻ riêng trước cặp? ________
QA+window+ladder = lý do PCT_D21 early / train AI? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | IMAGEJ-EPI×EQ bridge 1 trang |
| `IMAGEJ-EPI-EQ-5MIN` | Drill điền |
| `IMAGEJ-EPI-SCIENCE-CARD` | Cặp alone |
| `IMAGEJ-EQ` / `EPI-EQ` | QA×ladder / window×ladder |
| `EQ-M0M3` / `LEAKAGE-EQ` | Ladder / anti-leak |
| `EPI-SA01-EARLY-WINDOW` | Spec cửa sổ |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- PCT/CFU D21 = early-signal · train AI khi ảnh chưa QA  
- Order PEA / mở G2 · UpdateGoal trên PREP  

## Liên kết

`IMAGEJ-EPI-EQ-5MIN-MICRO-DRILL` · `IMAGEJ-EPI-SCIENCE-CARD` · `IMAGEJ-SCIENCE-CARD` · `EPI-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `LEAKAGE-EQ-SCIENCE-CARD` · `PUSH-ALERT-EQ-SCIENCE-CARD` · `EPI-SA01-EARLY-WINDOW` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
