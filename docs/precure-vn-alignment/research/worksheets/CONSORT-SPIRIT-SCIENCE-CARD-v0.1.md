# CONSORT-SPIRIT — thẻ khoa học 1 trang (khai ES · đặt ES · ≠ primary)

**Mã:** CONSORT-SPIRIT-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `CONSORT-SPIRIT-5MIN-MICRO-DRILL` · CONSORT-SCIENCE-CARD · SPIRIT-SCIENCE-CARD · AMENDMENT-ES · SAP-ES  
**DOI:** SPIRIT 2013 [10.7326/0003-4819-158-3-201302050-00583](https://doi.org/10.7326/0003-4819-158-3-201302050-00583) · CONSORT 2010 [10.1136/bmj.c332](https://doi.org/10.1136/bmj.c332)  
**Dùng khi:** STREAK≥3 · Daily stack **T5** · Ngày 15–17 · trước claim “đã báo ES đúng” · cặp CONSORT×SPIRIT  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · SPIRIT khai · CONSORT đặt exploratory · primary không đổi · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp CONSORT×SPIRIT**: S1–S3 phải **vào amendment** trước; khi báo cáo, ES/AUROC chỉ **exploratory** — không cùng hàng primary D21 / VAS_D3 / PUSH_D14; sandbox/`verify.sh` không vào Results lâm sàng. Khác `SPIRIT-SCIENCE-CARD` (khai S1–S3) / `CONSORT-SCIENCE-CARD` (placement alone) — thẻ này giữ **cặp bridge**.

**Mở song song:** thẻ này · `CONSORT-SPIRIT-5MIN` · **`CONSORT-SPIRIT-EQ-SCIENCE-CARD`** · `SPIRIT-SCIENCE-CARD` · `CONSORT-SCIENCE-CARD` · `AMENDMENT-ES-SCIENCE-CARD` · `SAP-ES-SCIENCE-CARD` · `TRIPOD-SYNTH-SCIENCE-CARD`

## Giữ / bỏ (CONSORT × SPIRIT)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **SPIRIT S1–S3** | Nháp → amendment trước claim | Git/SAP folder = đã duyệt |
| **Primary** | D21 / ΔVAS / ΔPUSH khoá | Adaptive primary vì “có ES” |
| **ES / AUROC** | Exploratory + limitation | Cùng hàng primary |
| **Sandbox** | Methods/appendix tech | Results lâm sàng BN |
| **Reporting** | Drill ≠ CLOSED | Coi đọc guideline = paper đúng |

## Phương trình ranh giới

```text
SPIRIT khai ES (S1–S3 → amendment)  →  CONSORT đặt ES = exploratory
Primary(t*) cố định  ·  sandbox ≠ Results lâm sàng
Đọc SPIRIT+CONSORT  ≠  protocol duyệt  ≠  Goal complete
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T5 · SA: 01|02|05 — ________
SPIRIT S1–S3 trong protocol/amendment? CHƯA|NHÁP|CÓ — ________
Primary CONSORT hàng: D21|ΔVAS|ΔPUSH — ________
ES / M0–M3 / AUROC đặt: PRIMARY|SECONDARY|EXPLORATORY|KHÔNG BÁO — ________
Cùng hàng primary với ES? KHÔNG
Sandbox / verify.sh → Results lâm sàng? KHÔNG
Adaptive primary vì đã đọc SPIRIT+CONSORT? KHÔNG
Cặp AMENDMENT / SAP / TRIPOD-SYNTH / TT43 hôm nay? ________
1 việc ≤30′ (placement / SPIRIT map / amendment S1): ________
Đóng Goal / reporting CLOSED vì drill? KHÔNG
```

## Checklist 15′

```text
Đã mở SPIRIT + CONSORT thẻ riêng trước cặp? ________
ES cùng hàng primary? KHÔNG
Git = HĐĐĐ duyệt? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | CONSORT×SPIRIT bridge 1 trang |
| `CONSORT-SPIRIT-5MIN` | Drill điền |
| `SPIRIT-SCIENCE-CARD` | S1–S3 · ES ≠ primary |
| `CONSORT-SCIENCE-CARD` | Placement exploratory |
| `AMENDMENT-ES-SCIENCE-CARD` | Outline ES |
| `SAP-ES-SCIENCE-CARD` | SAP § ES |
| `TRIPOD-SYNTH-SCIENCE-CARD` | Demo ≠ BN claim |
| `SPIRIT-G1-SCIENCE-CARD` | Nested ethics N1–N5 |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Báo ES cùng hàng primary  
- Coi đọc SPIRIT/CONSORT = protocol đã duyệt hoặc paper đã đúng  
- Đưa sandbox AUROC vào Results lâm sàng  
- Nhảy claim khi STREAK&lt;3 · UpdateGoal trên PREP  

## Liên kết

`CONSORT-SPIRIT-5MIN-MICRO-DRILL` · `CONSORT-SPIRIT-EQ-5MIN` · `SPIRIT-SCIENCE-CARD` · `CONSORT-SCIENCE-CARD` · `AMENDMENT-ES-SCIENCE-CARD` · `SAP-ES-SCIENCE-CARD` · `TRIPOD-SYNTH-SCIENCE-CARD` · `SPIRIT-G1-SCIENCE-CARD` · `SHIFT-PB007-SCIENCE-CARD` · **`TT43-AMEND-SCIENCE-CARD`** · **`CONSORT-EQ-SCIENCE-CARD`** · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
