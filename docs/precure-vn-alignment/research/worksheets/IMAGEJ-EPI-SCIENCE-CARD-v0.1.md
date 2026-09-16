# IMAGEJ-EPI — thẻ khoa học 1 trang (QA ảnh × early window D0–D7)

**Mã:** IMAGEJ-EPI-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `IMAGEJ-EPI-5MIN-MICRO-DRILL` · IMAGEJ-SCIENCE-CARD · EPI-SCIENCE-CARD · EQ-M0M3 · LEAKAGE  
**Dùng khi:** STREAK≥3 · Daily stack **T2** · trước claim AI trên PCT · cặp ImageJ×EPI  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · \(Y_{D21}\) ImageJ không đổi · \(t'\) ∈ {D0,D3,D7} · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp IMAGEJ×EPI SA-01**: SOP ảnh + blind/rater **và** \(Z\) chỉ trên D0/D3/D7 — không PCT_D21 early · không AUROC khi ảnh lệch SOP · không order PEA vì QA giấy. Khác `IMAGEJ-SCIENCE-CARD` (QA thuần) / `EPI-SCIENCE-CARD` (window thuần) — thẻ này giữ **cặp bridge**.

**Mở song song:** thẻ này · `IMAGEJ-EPI-5MIN` · `IMAGEJ-SCIENCE-CARD` · `EPI-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `EPI-SA01-EARLY-WINDOW`

## Giữ / bỏ (ImageJ × EPI)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **Primary \(t^*\)** | D21 · Y = 100% biểu mô ImageJ | Đổi primary vì drill |
| **Early \(t'\)** | D0 / D3 / D7 | D21 làm \(t'\) / PCT_D21 early |
| **SOP ảnh** | Khoảng cách / ánh sáng / góc | Claim đủ QA vì đã điền |
| **Blind / rater** | 2nd rater subset | Bỏ inter-rater vì “AI sửa” |
| **AUROC** | Chỉ sau QA + \(t'\) đúng | Train trên PCT lệch đo |
| **PEA / L3** | **CLOSED** | Order vì IMAGEJ-EPI giấy |

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
t* = D21 ImageJ — không đổi? CÓ
t' hôm nay: D0|D3|D7 — ________ (không D21)
Z: PCT_EPITH|CFU|VAS_DRESS|clin_event — ________
SOP ảnh đủ? CÓ|CHƯA — thiếu: ________
Blinded / 2nd rater? CÓ|CHƯA|N/A — ________
PCT_EPITH_D21 = early predictor? KHÔNG
AUROC khi SOP chưa chuẩn? KHÔNG
Order PEA / mở G2 vì IMAGEJ-EPI? KHÔNG
Cặp EQ-M0M3 / LEAKAGE / ALERT hôm nay? ________
1 việc ≤30′ (SOP / EPI window / EQ ladder): ________
Đóng Goal / mở L3? KHÔNG
```

## Checklist 15′

```text
Đã mở IMAGEJ + EPI thẻ riêng trước cặp? ________
PCT_D21 trong feature early? KHÔNG
QA giấy = DONE lâm sàng? KHÔNG
EQ-M0M3 ladder trước AUROC (T2)? CÓ nếu STREAK≥3
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | ImageJ×EPI bridge 1 trang |
| `IMAGEJ-EPI-5MIN` | Drill điền |
| `IMAGEJ-SCIENCE-CARD` | QA SOP / rater |
| `EPI-SCIENCE-CARD` | Window D0–D7 |
| `EQ-M0M3-SCIENCE-CARD` | Ladder SA-01 |
| `LEAKAGE-SCIENCE-CARD` | PCT D21 leakage |
| `EPI-SA01-EARLY-WINDOW` | Spec cửa sổ |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- PCT/CFU D21 = early-signal  
- Train AI trên % khi ảnh chưa QA  
- Order PEA / mở G2 vì đã điền cặp drill  
- Nhảy AUROC khi STREAK&lt;3 · UpdateGoal trên PREP  

## Liên kết

`IMAGEJ-EPI-5MIN-MICRO-DRILL` · `IMAGEJ-EPI-EQ-5MIN` · `IMAGEJ-SCIENCE-CARD` · `EPI-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `EPI-SA01-EARLY-WINDOW` · `IMAGEJ-QA-5MIN` · `EPI-5MIN` · `DAILY-STACK-AFTER-STREAK3` · **`IMAGEJ-EPI-EQ-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`
