# CONSORT-SPIRIT-EQ — thẻ khoa học 1 trang (khai+đặt ES × ladder · ≠ primary)

**Mã:** CONSORT-SPIRIT-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `CONSORT-SPIRIT-EQ-5MIN-MICRO-DRILL` · CONSORT-SPIRIT-SCIENCE-CARD · CONSORT-EQ · SPIRIT-EQ · LEAK-CROSS-EQ · EQ-M0M3 · AMENDMENT-EQ · SAP-EQ  
**DOI:** SPIRIT [10.7326/0003-4819-158-3-201302050-00583](https://doi.org/10.7326/0003-4819-158-3-201302050-00583) · CONSORT [10.1136/bmj.c332](https://doi.org/10.1136/bmj.c332)  
**Dùng khi:** STREAK≥3 · Daily stack **T5** · trước claim “đã báo ES đúng” · cặp CONSORT-SPIRIT×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · SPIRIT khai · CONSORT exploratory · ladder ≠ hàng primary · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp CONSORT-SPIRIT×EQ**: S1–S3 vào amendment **và** 1 dòng ladder M0–M3 đặt exploratory — không cùng hàng primary; sandbox/`verify.sh` không vào Results lâm sàng. Khác `CONSORT-SPIRIT-SCIENCE-CARD` (cặp alone) / `CONSORT-EQ` / `SPIRIT-EQ` — thẻ này neo **khai+đặt × ladder**.

**Mở song song:** thẻ này · `CONSORT-SPIRIT-EQ-5MIN` · `CONSORT-SPIRIT-SCIENCE-CARD` · `CONSORT-EQ-5MIN` · `SPIRIT-EQ-5MIN` · `LEAK-CROSS-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `AMENDMENT-EQ-SCIENCE-CARD`

## Giữ / bỏ (CONSORT-SPIRIT × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 exploratory / \(Z\) | Ladder cùng hàng primary |
| **SPIRIT S1–S3** | Nháp → amendment trước claim | Git folder = đã duyệt |
| **Primary** | D21 / ΔVAS / ΔPUSH khoá | Adaptive primary vì “có ES” |
| **ES / AUROC** | Exploratory + limitation | Cùng hàng primary |
| **Sandbox** | Methods/appendix tech | Results lâm sàng BN |
| **Order / Goal** | KHÔNG từ densify | Reporting CLOSED / UpdateGoal |

## Phương trình ranh giới

```text
SPIRIT S1–S3 → amendment
  +  CONSORT đặt ES exploratory
  +  EQ ladder M0–M3 (không hàng primary)
≠  sandbox = Results lâm sàng  ≠  Goal complete
Đọc guideline  ≠  protocol duyệt  ≠  densify = DONE
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T5 · SA: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
SPIRIT S1–S3 trong protocol/amendment? CHƯA|NHÁP|CÓ — ________
Primary CONSORT hàng: D21|ΔVAS|ΔPUSH — ________
1 dòng Z / M0→M3 (exploratory only): ________
ES/AUROC đặt: EXPLORATORY|KHÔNG BÁO (không PRIMARY) — ________
Sandbox → Results lâm sàng / adaptive primary? KHÔNG
Cặp MEDIA-SHIFT-EQ / LEAK-CROSS-EQ / AMENDMENT-EQ / SAP-EQ hôm nay? ________
1 việc ≤30′ (placement / SPIRIT map / EQ Drill 10′): ________
Đóng Goal / coi reporting CLOSED vì drill? KHÔNG
```

## Checklist 15′

```text
Đã mở CONSORT-SPIRIT + EQ sibling thẻ riêng trước cặp? ________
Khai+đặt+ladder = lý do primary đổi / Results BN? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | CONSORT-SPIRIT×EQ bridge 1 trang |
| `CONSORT-SPIRIT-EQ-5MIN` | Drill điền |
| `CONSORT-SPIRIT-SCIENCE-CARD` | Cặp alone |
| `CONSORT-EQ` / `SPIRIT-EQ` | Placement / khai × ladder |
| `LEAK-CROSS-EQ` / `AMENDMENT-EQ` / `SAP-EQ` | Leak×schema / amend / SAP × EQ |
| `EQ-M0M3` | Ladder sibling |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Báo ES cùng hàng primary · sandbox vào Results lâm sàng  
- Coi đọc SPIRIT/CONSORT = protocol đã duyệt · UpdateGoal trên PREP  

## Liên kết

`CONSORT-SPIRIT-EQ-5MIN-MICRO-DRILL` · `CONSORT-SPIRIT-SCIENCE-CARD` · `CONSORT-ES-PLACEMENT` · `LEAK-CROSS-EQ-SCIENCE-CARD` · `SPIRIT-EQ-SCIENCE-CARD` · `CONSORT-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
