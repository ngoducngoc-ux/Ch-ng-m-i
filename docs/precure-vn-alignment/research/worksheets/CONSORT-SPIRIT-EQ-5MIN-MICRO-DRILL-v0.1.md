# Micro-drill 5′ — CONSORT × SPIRIT × EQ (khai+đặt ES · ladder Z · ≠ primary)

**Mã:** CONSORT-SPIRIT-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5** · sau `CONSORT-SPIRIT-5MIN` / `CONSORT-EQ-5MIN` / `SPIRIT-EQ-5MIN` · trước claim “đã báo ES đúng”  
**Goal:** ACTIVE · SPIRIT khai · CONSORT exploratory · ladder ≠ hàng primary · PREP ≠ DONE  
**DOI:** SPIRIT [10.7326/0003-4819-158-3-201302050-00583](https://doi.org/10.7326/0003-4819-158-3-201302050-00583) · CONSORT [10.1136/bmj.c332](https://doi.org/10.1136/bmj.c332)  
**≠** `CONSORT-EQ-5MIN` / `SPIRIT-EQ-5MIN` alone — drill này = **cặp khai+đặt + ladder**

## Một câu

> CONSORT-SPIRIT×EQ 5′ = S1–S3 vào amendment **và** 1 dòng ladder M0–M3 đặt exploratory — không cùng hàng primary; sandbox/`verify.sh` không vào Results lâm sàng.

## Drill (điền)

```text
SA neo: 01 | 02 | 05 — chọn: ________
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________
SPIRIT S1–S3 trong protocol/amendment? CHƯA | NHÁP | CÓ — ghi: ________
Primary CONSORT hàng: D21 | ΔVAS | ΔPUSH — chọn: ________
1 dòng Z / M0→M3 (exploratory only): ________
ES/AUROC đặt: EXPLORATORY | KHÔNG BÁO — chọn (không PRIMARY): ________
Sandbox → Results lâm sàng / adaptive primary? KHÔNG
Cặp đã đụng: CONSORT-SPIRIT | CONSORT-EQ | SPIRIT-EQ | AMENDMENT-EQ | TRIPOD-SYNTH-EQ | SAP-EQ — ghi: ________
1 việc nhỏ ≤30′ (placement / SPIRIT map / EQ Drill 10′): ________
Đóng Goal / coi reporting CLOSED vì drill? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Thẻ khoa học | **`CONSORT-SPIRIT-SCIENCE-CARD`** · `SPIRIT-SCIENCE-CARD` · `CONSORT-SCIENCE-CARD` |
| CONSORT×SPIRIT alone | `CONSORT-SPIRIT-5MIN` · `CONSORT-5MIN` · `SPIRIT-5MIN` |
| CONSORT×EQ / SPIRIT×EQ | `CONSORT-EQ-5MIN` · `SPIRIT-EQ-5MIN` |
| Amendment / SAP | `AMENDMENT-EQ-5MIN` · `SAP-EQ-5MIN` |
| TRIPOD×SYNTH×EQ | `TRIPOD-SYNTH-EQ-5MIN` · `TRIPOD-SYNTH-5MIN` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |

## Cấm

- Báo ES cùng hàng primary · sandbox vào Results lâm sàng  
- Coi đọc SPIRIT/CONSORT = protocol đã duyệt  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5) · Protocol: `../../rituals/daily-protocol.md`  
- Placement: `CONSORT-ES-PLACEMENT`
