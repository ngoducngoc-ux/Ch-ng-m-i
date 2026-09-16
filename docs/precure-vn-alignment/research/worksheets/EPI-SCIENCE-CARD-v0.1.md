# EPI — thẻ khoa học 1 trang (early window SA-01 · D0–D7 · ≠ D21)

**Mã:** EPI-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `EPI-SA01-EARLY-WINDOW` · IMAGEJ · ENDPOINTS · LEAKAGE · ALERT · EQ  
**Dùng khi:** T2 · Ngày 10 · EQ-SA01 · bridge #0 · sau IMAGEJ-QA · trước claim “đã có early-signal SA-01”  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + **`MEDIA-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · primary D21 không đổi · L3/G2 CLOSED · synthetic ≠ BN · PREP ≠ DONE  

## Mục đích

Ôn **early window SA-01** Precure/Smart A: \(Z\) **D0/D3/D7** (PCT_EPITH / CFU / VAS_DRESS / `clin_event`) — **không** dùng PCT **D21** làm predictor early; ImageJ QA trước claim AI trên PCT; không order PEA vì đã ôn EPI.

**Mở song song:** thẻ này · `EPI-SA01-EARLY-WINDOW` · `IMAGEJ-SCIENCE-CARD` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD`

## Window → giữ / bỏ

| Khối | Vai trò | Giữ hôm nay | Bỏ |
|------|---------|-------------|-----|
| \(t^*\) | D21 · Y = 100% biểu mô ImageJ | Khoá primary | Đổi vì EPI drill |
| \(t'\) | D0 / D3 / D7 | Early exploratory | D21 làm \(t'\) |
| \(Z\) | PCT / CFU / VAS / clin_event | eCRF v0.2 dọc | PCT_D21 = early feature |
| ImageJ QA | SOP / rater | Trước AUROC | Claim AI trên PCT lệch đo |
| \(X_{\text{PEA}}\) | Panel hẹp | Sau G1–G2 | Order vì đã ôn EPI |

## Phương trình EPI

```text
t* = D21 ImageJ  cố định
t' ∈ {D0, D3, D7}  ·  Z(t')  =  early window
PCT_EPITH(D21)  ≠  early predictor
ImageJ QA  ≥  trước  AUROC trên PCT
L3 CLOSED  →  không order PEA vì EPI
```

## Checklist 15′

```text
Thứ: T2 · t* D21 ImageJ ĐÚNG? ________
t' hôm nay: D0|D3|D7 (không D21) — ________
Z: PCT|CFU|VAS|clin_event — ________
PCT_D21 = early feature? KHÔNG — vì: ________
Order PEA vì EPI? KHÔNG
1 việc ≤30′ (EQ / IMAGEJ / ALERT / shift): ________
Đóng Goal / mở L3 vì EPI? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / EPI-SA01 | Early window D0–D7 |
| `IMAGEJ-SCIENCE-CARD` | SOP/rater QA |
| `ENDPOINTS-WEEK1-SCIENCE-CARD` | \(t^*\neq Z\) sớm |
| `LEAKAGE-SCIENCE-CARD` | PCT D21 leakage |
| `ALERT-SCIENCE-CARD` | Actionable ≠ Dx |
| `EQ-SCIENCE-CARD` | Ladder M0–M3 |

## Cấm

- Coi PCT/CFU D21 là early-signal  
- AUROC sandbox = bằng chứng BN  
- Mở PEA / đóng Goal vì đã đọc EPI/EQ  

## Liên kết

`EPI-SA01-EARLY-WINDOW` · `EPI-5MIN` · `EPI-EQ-5MIN` · `IMAGEJ-SCIENCE-CARD` · `IMAGEJ-EPI-5MIN` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `ALERT-SCIENCE-CARD` · `EQ-SCIENCE-CARD` · `OMICS-IF-SCIENCE-CARD` · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3` · **`GLOSSARY-SCIENCE-CARD`** · **`CROSS-SA-SCIENCE-CARD`** · **`TRANSLATION-SCIENCE-CARD`** · **`PB001-SCIENCE-CARD`**
