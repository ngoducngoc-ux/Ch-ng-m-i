# LEAK-CROSS — thẻ khoa học 1 trang (leakage × schema · không gộp \(Y\))

**Mã:** LEAK-CROSS-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `LEAK-CROSS-5MIN-MICRO-DRILL` · LEAKAGE-SCIENCE-CARD · CROSS-SA-SCIENCE-CARD · VAS-LEAK · ENDPOINTS  
**Dùng khi:** STREAK≥3 · Daily stack **T4 / T6 / CN** · trước claim “một model early chung” / AUROC gộp SA · cặp Leakage×CROSS-SA  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · HAWTHORNE · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · mỗi SA một \(Y(t^*)\) · không \(Y(t^*)\) làm early · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp LEAK×CROSS**: so schema \(t^*\)/\(Z\) sớm giữa SA **và** cấm leakage — không đưa outcome primary làm feature early · không gộp \(Y\) · AUROC sandbox ≠ BN. Khác `LEAKAGE-SCIENCE-CARD` (3 SA pitfall) / `CROSS-SA-SCIENCE-CARD` (schema alone) / `VAS-LEAK-SCIENCE-CARD` (SA-02 pair) — thẻ này giữ **cặp bridge**.

**Mở song song:** thẻ này · `LEAK-CROSS-5MIN` · `LEAKAGE-SCIENCE-CARD` · `CROSS-SA-SCIENCE-CARD` · `VAS-LEAK-SCIENCE-CARD` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `TRIPOD-SCIENCE-CARD`

## Giữ / bỏ (Leakage × CROSS-SA)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **Schema** | Mỗi SA một \(Y(t^*)\) · so \(t'≪t^*\) | Một model / một \(Y\) cho 3 SA |
| **Early \(t'\)** | \(Z\) trước \(t^*\) (D0–D7 / D1) | PCT D21 · VAS_D3 · PUSH_D14 làm early |
| **Leakage QC** | M1+VAS_D3 / feature≥\(t^*\) = QC only | AUROC sandbox = evidence BN |
| **Cờ đầu** | SA-01 theo quyết định PI | Chọn cờ / power theo AUROC synth |
| **Omics / L3** | **CLOSED** | Order vì “đã so + tránh leak” |

## Ba SA → một hàng cặp

| SA | \(t^*\) bảo vệ | Leakage điển hình | \(Z\) sớm hợp lệ |
|----|----------------|-------------------|------------------|
| **01** | D21 biểu mô | PCT D21 / \(Y\) mã hoá | D0–D7 PCT/CFU/VAS/`clin_event` |
| **02** | VAS relief D3 | M1 gồm VAS_D3 ≈ \(Y\) | D1 / CFU trước D3 |
| **05** | PUSH D14 | PUSH_D14 làm “early” | D0–D7 PUSH + TURN |

## Phương trình ranh giới

```text
So schema t'/t* giữa SA  ≠  train chung  ≠  gộp Y
Feature t' ≪ t*          ≠  feature ≈ Y(t*)  ≠  nhìn tương lai
verify.sh / AUROC synth  ≠  BN evidence  ≠  mở G2/L3
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T4|T6|CN · SA đang ôn (không gộp): 01|02|05 — ________
t* primary: D21|VAS_D3|PUSH_D14 — ________
1 Z sớm hợp lệ (≠ Y(t*)): ________
1 feature SẼ leakage nếu vào M early: ________
Gộp Y nhiều SA? KHÔNG — vì: ________
Chọn cờ / power theo AUROC synth? KHÔNG
VAS_D3 / PUSH_D14 / PCT D21 = early? KHÔNG
Omics vì “đã so + tránh leak”? KHÔNG
Cặp VAS-LEAK / EQ / TRIPOD hôm nay? ________
1 việc ≤30′ (atlas / CROSS map / EQ sibling): ________
Đóng Goal / mở L3? KHÔNG
```

## Checklist 15′

```text
Đã mở LEAKAGE + CROSS-SA thẻ riêng trước cặp? ________
Outcome t* trong feature early (trừ QC)? KHÔNG
Một model cho nhiều SA? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | LEAK×CROSS bridge 1 trang |
| `LEAK-CROSS-5MIN` | Drill điền |
| `LEAKAGE-SCIENCE-CARD` | Pitfall #1 · 3 SA |
| `CROSS-SA-SCIENCE-CARD` | Schema · không gộp Y |
| `VAS-LEAK-SCIENCE-CARD` | SA-02 VAS×leak alone |
| `LEAKAGE-CROSS-SA-ATLAS` | Atlas chi tiết |
| `TRIPOD` / `SYNTH` | Không claim từ sandbox |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Outcome \(t^*\) làm predictor “early”  
- Một model / một \(Y\) cho nhiều SA · chọn cờ theo AUROC synth  
- Order L3 vì schema “đã khớp” và “đã tránh leak”  
- Nhảy claim khi STREAK&lt;3 · UpdateGoal trên PREP  

## Liên kết

`LEAK-CROSS-5MIN-MICRO-DRILL` · `LEAK-CROSS-EQ-5MIN` · `LEAKAGE-SCIENCE-CARD` · `CROSS-SA-SCIENCE-CARD` · `VAS-LEAK-SCIENCE-CARD` · `LEAKAGE-CROSS-SA-ATLAS` · `CROSS-SA-EARLY-SIGNAL-MAP` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `TRIPOD-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · `ALERT-HAWTHORNE-SCIENCE-CARD` · **`ALERT-CROSS-SCIENCE-CARD`** · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
