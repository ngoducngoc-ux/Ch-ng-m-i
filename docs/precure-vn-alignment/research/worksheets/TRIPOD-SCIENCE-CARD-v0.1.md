# TRIPOD — thẻ khoa học 1 trang (trước claim AI · Y/predictors/validation)

**Mã:** TRIPOD-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `TRIPOD-INTERNAL-CHECKLIST` · SYNTH · LEAKAGE · AI-STACK · EQ  
**Dùng khi:** T4/T5 · Ngày 20 · Q3 104–105 · trước memo “model sớm”  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + **`MEDIA-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · exploratory ≠ Dx · synthetic ≠ BN · L3 CLOSED · PREP ≠ DONE  
**Nguồn:** Riley et al. DOI [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594)

## Mục đích

Ôn **cổng báo cáo AI** Precure/Smart A: trước “AI dự báo early-signal” — khoanh **Y / predictors pre-spec / validation / limitation**; AUROC sandbox ≠ evidence BN.

**Mở song song:** thẻ này · `TRIPOD-INTERNAL-CHECKLIST` · `SYNTH-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `AI-STACK-SCIENCE-CARD`

## Claim AI → giữ / bỏ

| Mục | Vai trò | Giữ hôm nay | Bỏ |
|-----|---------|-------------|-----|
| **Y(\(t^*\))** | Outcome primary | Khoá \(t^*\) | Đổi Y sau peek AUROC |
| **Predictors** | Pre-spec SAP ES | M0–M3 đã ghi | Thêm feature sau data peek |
| **Validation** | Hold-out / time-split | Ghi rõ loại | Coi `--demo` = BN |
| **Label** | Exploratory ES | Ghi limitation | “clinical Dx sẵn sàng” |

## Phương trình TRIPOD rút gọn

```text
Y(t*) khoá + predictors pre-spec + validation rõ + limitation
  ≥  trước  “AI early-signal” claim
AUROC sandbox  ≠  evidence BN  ·  L3 CLOSED
```

## Checklist 15′

```text
Thứ: T4|T5 · SA: 01|02|05 — ________
Y(t*) khoá primary? CÓ|CHƯA — t* = ________
Predictors pre-spec SAP ES? M0–M3 | peek sau data (CẤM)
1 pitfall tránh (#1 leakage|#5 synthetic): ________
Validation: hold-out|time-split|CHƯA (synth only)
Limitation 1 câu: ________
Label: exploratory ES | clinical Dx — khoanh đúng
1 việc ≤30′ (TRIPOD-5MIN / TRIPOD-SYNTH / LEAKAGE): ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / TRIPOD checklist | Báo cáo trước claim AI |
| `SYNTH-SCIENCE-CARD` | Demo ≠ BN |
| `LEAKAGE-SCIENCE-CARD` | Timestamp / \(t^*\) ≠ early |
| `AI-STACK-SCIENCE-CARD` | L1→L2 trước L3 |
| `EQ-SCIENCE-CARD` | Ladder M0–M3 |

## Cấm

- Báo “phát hiện sớm lâm sàng” từ sandbox  
- Thêm predictor sau peek AUROC  
- Mở G2 / đóng Goal vì đã điền đủ ô TRIPOD  

## Liên kết

`TRIPOD-INTERNAL-CHECKLIST` · `TRIPOD-5MIN` · `TRIPOD-EQ-5MIN` · `TRIPOD-SYNTH-5MIN` · `SYNTH-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `AI-STACK-SCIENCE-CARD` · `EQ-SCIENCE-CARD` · `PITFALLS-5MIN` · **`CONSORT-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3` · **`SAP-ES-SCIENCE-CARD`** · **`PITFALLS-SCIENCE-CARD`**
