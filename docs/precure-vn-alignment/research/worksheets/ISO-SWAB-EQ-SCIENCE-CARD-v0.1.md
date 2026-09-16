# ISO-SWAB-EQ — thẻ khoa học 1 trang (SKU cổng · ladder Z · trước nested)

**Mã:** ISO-SWAB-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `ISO-SWAB-EQ-5MIN-MICRO-DRILL` · ISO-SWAB-SCIENCE-CARD · EQ-M0M3 / EQ02 / EQ05 · OMICS-IF · DEID-EQ  
**Căn cứ:** ISO-SWAB-CONTACT-PRIORITY · SA-04 cổng · G5 SPEC-BIO · ISO 10993  
**Dùng khi:** STREAK≥3 · Daily stack **T5** · trước nested biospecimen / claim “đã có ES trên swab” · cặp ISO-SWAB×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · SA-04 = **cổng** · M0–M3 trên \(Z\) **không** cần swab · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp ISO-SWAB×EQ**: ladder M0–M3 trên \(Z\) **song song** irritation+cytotox trên SKU swab — checklist/drill/ladder **≠** ISO pass; **không** order swab/PEA vì đã viết M0–M3. Khác `ISO-SWAB-SCIENCE-CARD` (G5 alone) / `EQ-*-SCIENCE-CARD` (ladder alone) — thẻ này giữ **cặp bridge**.

**Mở song song:** thẻ này · `ISO-SWAB-EQ-5MIN` · `ISO-SWAB-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `OMICS-IF-SCIENCE-CARD` · `DEID-EQ-SCIENCE-CARD` · `SPIRIT-G1-EQ-SCIENCE-CARD`

## Giữ / bỏ (ISO-SWAB × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) | X/swab · PCT_D21 early |
| **SKU swab** | Định + irritation+cytotox | Checklist = ISO pass |
| **SA-04** | Cổng trước nested | = đã có ES trên swab |
| **Order** | Sau G1–G2 + ISO cổng | Order vì đã điền ladder |
| **AI/REDCap** | Không thay ISO | Claim ISO pass từ alert |

## Phương trình ranh giới

```text
EQ ladder M0–M3 trên Z  +  ISO contact (irritation+cytotox) trên SKU
  ≥  trước  nested swab / PEA / claim “ES trên swab”
Checklist / densify / ladder  ≠  ISO pass
AI early warning  ≠  ISO pass
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T5 · SA neo: 01 (flagship nested)|khác — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
1 dòng Z / M0→M3 (không X / không swab): ________
SKU swab dự kiến đã định? CHƯA [CẦN XÁC NHẬN]|CÓ — ________
Hạng mục ISO hôm nay: irritation+cytotox|khác — ________
Ladder / drill = ISO pass trên SKU? KHÔNG
Order swab / PEA / mở form omics vì ISO×EQ? KHÔNG
AI early warning REDCap = ISO pass? KHÔNG
Cặp DEID-EQ / SPIRIT-G1-EQ / OMICS-IF / PB006 hôm nay? ________
1 việc ≤30′ (ISO-SWAB skim / EQ Drill 10′ / OMICS-IF): ________
Đóng Goal / mở L3 vì ISO-SWAB×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở ISO-SWAB + EQ sibling thẻ riêng trước cặp? ________
Ladder = lý do order swab? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | ISO-SWAB×EQ bridge 1 trang |
| `ISO-SWAB-EQ-5MIN` | Drill điền |
| `ISO-SWAB-SCIENCE-CARD` | G5 contact alone |
| `EQ-M0M3` / EQ02 / EQ05 | Ladder sibling |
| `OMICS-IF` / `G2` | Omics gate |
| `DEID-EQ` / `SPIRIT-G1-EQ` | Export / nested ethics |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Coi checklist/ladder = ISO pass trên SKU  
- Order swab / mở form omics vì đã điền ISO×EQ  
- Mở \(X\) / L3 trước G1–G2 + ISO cổng · UpdateGoal trên PREP  

## Liên kết

`ISO-SWAB-EQ-5MIN-MICRO-DRILL` · `ISO-SWAB-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `OMICS-IF-SCIENCE-CARD` · `DEID-EQ-SCIENCE-CARD` · `SPIRIT-G1-EQ-SCIENCE-CARD` · `PB006-SCIENCE-CARD` · `G2-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
