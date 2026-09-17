# Micro-drill 5′ — SPIRIT nested G1 ethics (trước biospecimen)

**Mã:** SPIRIT-G1-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5** · Ngày 16 · sau `SPIRIT-5MIN` · trước mọi order swab/PEA/omics  
**Goal:** ACTIVE · G1 ethics nested · **không** biospecimen trước G1+G2 · PREP ≠ DONE  
**Spec:** `SPIRIT-NESTED-G1-CHECKLIST` · SPIRIT E&E DOI [10.1136/bmj.e7586](https://doi.org/10.1136/bmj.e7586)

## Một câu

> SPIRIT-G1 5′ = nested biospecimen chỉ sau N1–N5 (amendment + ICF tách + G2 pre-spec + ISO G5 nếu cần) — đọc SPIRIT / nháp Git **không** = G1 pass; **không** lấy mẫu trước G1 và G2 trên \(Z\).

## Drill (điền)

```text
N1 Amendment nested + visit D0/D3/D7? CHƯA [CẦN XÁC NHẬN] | NHÁP | CÓ — ghi: ________
N2 ICF/PIS optional tách consent omics? CHƯA | nháp ICF-NEST | CÓ — ghi: ________
N3 G2 pre-specify trong amendment (không ad hoc)? CHƯA | G2-READINESS | CÓ
N4 ISO G5 nếu swab/device mới? N/A | CHƯA | ISO-SWAB — ghi: ________
N5 Lấy mẫu trước G1 VÀ G2 trên Z? KHÔNG
Order swab / PEA / mở form omics vì SPIRIT-G1 drill? KHÔNG
Adaptive primary vì nested ES? KHÔNG
Cặp đã đụng: SPIRIT-5MIN | ISO-SWAB-5MIN | G2-5MIN | OMICS-IF | PREANALYTIC | TT43 — ghi: ________
1 việc nhỏ ≤30′ (ICF-NEST / amendment / SPIRIT-NESTED checklist): ________
Đóng Goal / coi G1 CLOSED vì drill? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Checklist đầy đủ | `SPIRIT-NESTED-G1-CHECKLIST` |
| SPIRIT S1–S3 | `SPIRIT-5MIN` · `SPIRIT-SA01-MAP` |
| ICF nháp | `ICF-NEST-SA01` · **`ICF-NEST-5MIN`** |
| ISO G5 | `ISO-SWAB-5MIN` · `PB006-5MIN` |
| G2 / BIO | `G2-5MIN` · `OMICS-IF-5MIN` · `SPEC-SA01-BIO` |
| TT43 | `TT43-5MIN` |
| SPIRIT-G1×EQ | **`SPIRIT-G1-EQ-5MIN`** · EQ ladders |

## Cấm

- Coi đọc SPIRIT / folder Precure = G1 ethics pass  
- Lấy / order biospecimen trước G1 **và** G2 trên data \(Z\)  
- Gộp consent omics vào RCT chính mà không amendment/ICF tách  
- Mở form omics REDCap / L3 vì đã điền drill  

## Liên kết

- **Thẻ khoa học:** **`SPIRIT-G1-SCIENCE-CARD`** · **`ICF-NEST-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`

- Checklist: `SPIRIT-NESTED-G1-CHECKLIST-v0.1.md` · Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5)  
- Protocol: `../../rituals/daily-protocol.md` · Notes: `../reading-notes/2026-10-02-spirit-ee-nested.md`
