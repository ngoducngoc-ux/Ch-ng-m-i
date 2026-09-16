# Micro-drill 5′ — ISO swab / collection contact (G5 · trước L3)

**Mã:** ISO-SWAB-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5** · Ngày 14 / 48 · sau `PB006-5MIN` · OMICS-IF Ngày 48 · trước nested biospecimen  
**Goal:** ACTIVE · SA-04 = **cổng** · G5 SPEC-BIO · không order swab omics vì nháp · PREP ≠ DONE  
**Spec:** `ISO-SWAB-CONTACT-PRIORITY` · ISO 10993-1:2018

## Một câu

> ISO-SWAB 5′ = irritation + cytotoxicity trên **SKU swab thật** trước mọi nested omics (G5) — AI/REDCap **không** thay báo cáo ISO; không mở form omics trước G2.

## Drill (điền)

```text
Intended contact: surface swab/exudate | implant — chọn: ________
Duration class: limited | prolonged | [CẦN XÁC NHẬN] — ghi: ________
Hạng mục ưu tiên hôm nay: irritation+cytotox | sensitization | khác — chọn: ________
SKU swab dự kiến đã định? CHƯA [CẦN XÁC NHẬN] | CÓ — ghi: ________
AI early warning REDCap = ISO pass? KHÔNG
Mở form omics REDCap trước G2? KHÔNG
Order swab/PEA vì ISO-SWAB drill? KHÔNG
Cặp đã đụng: PB006-5MIN | OMICS-IF-5MIN | PREANALYTIC | G2-5MIN | EH-SA04 — ghi: ________
1 việc nhỏ ≤30′ (ISO-SWAB / PB006 / EH-SA04): ________
Đóng Goal / mở L3 vì ISO-SWAB? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Spec ưu tiên | `ISO-SWAB-CONTACT-PRIORITY` |
| PB-006 cổng rộng | `PB006-5MIN` · `EH-SA04-gates` |
| Omics-if Ngày 48 | `OMICS-IF-5MIN` |
| Pre-analytic | `PREANALYTIC-5MIN` |
| G2 / BIO G5 | `G2-5MIN` · `SPEC-SA01-BIO` |
| Nested G1 ethics | **`SPIRIT-G1-5MIN`** · `SPIRIT-NESTED-G1-CHECKLIST` |
| ISO-SWAB×EQ | **`ISO-SWAB-EQ-5MIN`** · EQ ladders |

## Cấm

- Coi checklist nháp = ISO pass trên SKU  
- Dùng AI/REDCap thay báo cáo irritation/cytotox  
- Mở form omics / order swab vì đã điền drill  

## Liên kết

- Spec: `ISO-SWAB-CONTACT-PRIORITY-v0.1.md` · Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5)  
- Protocol: `../../rituals/daily-protocol.md` · Notes: `../reading-notes/2026-09-30-iso10993-sa04-gates.md`
