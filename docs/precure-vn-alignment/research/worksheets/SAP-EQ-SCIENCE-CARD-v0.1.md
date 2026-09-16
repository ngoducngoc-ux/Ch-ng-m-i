# SAP-EQ — thẻ khoa học 1 trang (SAP-ES · ladder Z · ≠ primary)

**Mã:** SAP-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `SAP-EQ-5MIN-MICRO-DRILL` · SAP-ES-SCIENCE-CARD · EQ-M0M3 / EQ02 / EQ05 · LEAKAGE · ICF-EQ  
**Căn cứ:** SPIRIT 2013 · SAP-SA01-ES draft · §7 leakage · 7.1  
**Dùng khi:** STREAK≥3 · Daily stack **T5** · trước claim interim / adaptive / “đã có ES trong SAP” · cặp SAP×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · primary không đổi · M0–M3 exploratory trên \(Z\) · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp SAP×EQ**: neo 1 SA → ladder M0–M3 trên \(Z\) **khớp** SAP-ES (không đảo primary) — nhắc **§7 leakage** + 7.1 — **không** adaptive · **không** dùng \(Y(t^*)\) làm early feature. Khác `SAP-ES-SCIENCE-CARD` (SAP alone) / `EQ-*-SCIENCE-CARD` (ladder alone) — thẻ này giữ **cặp bridge**.

**Mở song song:** thẻ này · `SAP-EQ-5MIN` · `SAP-ES-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `ICF-EQ-SCIENCE-CARD` · `TRIPOD-SYNTH-SCIENCE-CARD`

## Giữ / bỏ (SAP × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **Primary** | D21 / ΔVAS / ΔPUSH khoá | Đổi vì AUROC / ladder |
| **EQ ladder** | M0–M3 trên \(Z\) khớp SAP-ES | PCT_D21 early · M4/X |
| **§7 leakage** | \(Y(t^*)\) không làm early | Outcome làm predictor |
| **7.1** | Sensitivity exploratory | = hiệu quả sản phẩm |
| **Adaptive / interim** | KHÔNG vì ES | Dừng sớm / đổi nhánh |
| **Sandbox AUROC** | Methods/tech | = bằng chứng BN |

## Phương trình ranh giới

```text
Primary(t*) cố định  +  EQ ladder M0–M3 trên Z  +  §7 no leakage
  ≥  trước  claim AUROC / interim / “SAP có ES”
§7.1 sensitivity  ≠  primary
Synthetic AUROC  ≠  bằng chứng BN
Adaptive / đổi nhánh vì ES  =  KHÔNG
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T5 · SA neo: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
Y(t*) primary (không đổi): ________
1 dòng Z / M0→M3 trong SAP-ES: ________
§7 leakage (Y(t*) làm early?): KHÔNG — vì: ________
7.1 / interim / adaptive hôm nay? KHÔNG
X / PEA / L3 vì đã viết SAP×EQ? CLOSED
Cặp LEAK-CROSS / ICF-EQ / AMENDMENT-EQ / TRIPOD hôm nay? ________
1 việc ≤30′ (SAP §7 skim / EQ Drill 10′ / LEAK-CROSS): ________
Đóng Goal / đổi primary vì SAP×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở SAP-ES + EQ sibling thẻ riêng trước cặp? ________
Predictors sau D7 vào early? KHÔNG
AUROC synthetic = BN? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | SAP×EQ bridge 1 trang |
| `SAP-EQ-5MIN` | Drill điền |
| `SAP-ES-SCIENCE-CARD` | §7 · 7.1 alone |
| `EQ-M0M3` / EQ02 / EQ05 | Ladder sibling |
| `LEAKAGE` / `LEAK-CROSS` | Pitfall thời gian |
| `ICF-EQ-SCIENCE-CARD` | Consent × ladder |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Đổi primary / adaptive / interim vì đã điền ladder  
- Outcome \(t^*\) làm predictor early · Mở G2/L3 vì “SAP đã có ES”  
- Nhảy claim khi STREAK&lt;3 · UpdateGoal trên PREP  

## Liên kết

`SAP-EQ-5MIN-MICRO-DRILL` · `SAP-ES-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `LEAK-CROSS-SCIENCE-CARD` · `ICF-EQ-SCIENCE-CARD` · `AMENDMENT-ES-SCIENCE-CARD` · **`AMENDMENT-EQ-SCIENCE-CARD`** · `TRIPOD-SYNTH-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
