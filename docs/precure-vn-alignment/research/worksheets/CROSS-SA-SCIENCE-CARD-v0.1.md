# CROSS-SA — thẻ khoa học 1 trang (schema \(t^*\)/\(Z\) · không gộp \(Y\))

**Mã:** CROSS-SA-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `CROSS-SA-EARLY-SIGNAL-MAP` · ENDPOINTS · EQ · OMICS-GATES · EPI · GLOSSARY  
**Dùng khi:** T4/T6/CN · Ngày 33–36 · STREAK3 · bridge #2 · trước claim “một model Smart A chung”  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + **`MEDIA-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · cờ đầu SA-01 · mỗi SA một \(Y(t^*)\) · L3 CLOSED · synthetic ≠ BN · PREP ≠ DONE  

## Mục đích

Ôn **cross-SA schema** Precure/Smart A: so sánh khung \(t^*\)/\(Z\) sớm giữa SA để học — **không** train chung một model; không gộp endpoint; không chọn cờ theo AUROC sandbox; không order L3 vì schema “đã khớp”.

**Mở song song:** thẻ này · `CROSS-SA-EARLY-SIGNAL-MAP` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `EPI-SCIENCE-CARD` · `OMICS-GATES-SCIENCE-CARD`

## Schema → giữ / bỏ

| SA | \(t^*\) giữ | \(Z\) sớm | Bỏ |
|----|-------------|-----------|-----|
| **01** (cờ) | D21 biểu mô | D0–D7 PCT/CFU/VAS/clin_event | Gộp với VAS/PUSH |
| **02** | VAS D3 | Series D0–D3 | Thay primary bằng marker |
| **05** | PUSH D14 | D0–D7 PUSH + TURN | Gộp Y với D21 |
| **03** | ATCC biofilm | — in-vitro | Coi = Dx BN |
| **04** | ISO 10993 | — | Skip trước L3 người |
| **Sandbox** | verify.sh QC | Cấu trúc feature | AUROC = evidence / chọn cờ |

## Phương trình CROSS-SA

```text
Cùng khung t' ≪ t*  ·  mỗi SA một Y(t*)
So sánh schema  ≠  train chung  ≠  gộp endpoint
AUROC synthetic  ≠  chọn cờ đầu  ≠  BN evidence
Schema khớp  ≠  order L3
```

## Checklist 15′

```text
Thứ: T4|T6|CN · SA: 01|02|05|03|04 — ________
t* đúng: D21|VAS_D3|PUSH_D14|ATCC|ISO — ________
1 Z sớm (không Y(t*)): ________
Gộp Y nhiều SA? KHÔNG — vì: ________
Chọn cờ theo AUROC synth? KHÔNG
verify.sh = BN? KHÔNG
Omics vì schema khớp? KHÔNG
1 việc ≤30′ (EQ/ENDPOINTS/OMICS-GATES/PB001): ________
Đóng Goal vì CROSS-SA? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / CROSS-SA map | Schema × SA · không gộp Y |
| `ENDPOINTS-WEEK1-SCIENCE-CARD` | \(t^*\neq Z\) sớm |
| `EPI-SCIENCE-CARD` | Window SA-01 |
| `OMICS-GATES-SCIENCE-CARD` | Cổng × SA |
| `GLOSSARY-SCIENCE-CARD` | Định nghĩa \(t^*\)/\(Z\) |
| `EQ-SCIENCE-CARD` | Ladder M0–M3 |

## Cấm

- Một model / một \(Y\) cho nhiều SA  
- Chọn cờ đầu hoặc power theo AUROC sandbox  
- Order L3 / đóng Goal vì schema “đã khớp”  

## Liên kết

`CROSS-SA-EARLY-SIGNAL-MAP` · `CROSS-SA-5MIN` · `CROSS-EQ-5MIN` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `EPI-SCIENCE-CARD` · `OMICS-GATES-SCIENCE-CARD` · `GLOSSARY-SCIENCE-CARD` · `EQ-SCIENCE-CARD` · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3` · **`TRANSLATION-SCIENCE-CARD`** · **`PB005-SCIENCE-CARD`** · **`PB001-SCIENCE-CARD`**
