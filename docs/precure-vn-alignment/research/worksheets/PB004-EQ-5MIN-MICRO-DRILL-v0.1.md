# Micro-drill 5′ — PB-004 × EQ (StudyID→visit · ladder Z · consent/PII)

**Mã:** PB004-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5 / T7** · sau `PB004-5MIN` / `DEID-EQ-5MIN` / `YTESO-EQ-5MIN` / `EQ-M0M3-5MIN` · trước claim “đã sẵn sàng omics/AI trên data”  
**Goal:** ACTIVE · consent + de-ID trước omics · M0–M3 trên \(Z\) · PII không vào git/Drive public · L3 CLOSED · PREP ≠ DONE  

## Một câu

> PB004×EQ 5′ = 1 entity (StudyID / Visit / ClinicalObs) **và** 1 dòng ladder M0–M3 trên \(Z\) de-ID — sơ đồ Git ≠ REDCap live; consent nested trước Specimen; không AUROC khi còn PII.

## Drill (điền)

```text
SA neo: 01 | 02 | 05 — chọn: ________
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________
Entity tối thiểu hôm nay: StudyID | Visit | ClinicalObs | Media | Specimen — chọn: ________
Consent lưu mẫu / tái phân tích omics? CHƯA | NHÁP ICF | CÓ — version: ________
1 dòng Z / M0→M3 trên StudyID+visit (de-ID): ________
PII trong repo / memory / Drive public? KHÔNG — vì: ________
Export analysis DB có tên/SĐT/MRN? KHÔNG — lớp: StudyID+visit+Z
Diagram mermaid = REDCap live site? KHÔNG
Order Specimen / mở G2 vì PB004×EQ? KHÔNG
Cặp đã đụng: PB004 | DEID-EQ | BN-VISIT | CLIN-BN-EQ | YTESO-EQ | TT43-EQ — ghi: ________
1 việc nhỏ ≤30′ (checklist consent / deny-list / EQ Drill 10′): ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| PB-004 alone | `PB004-5MIN` · `PB-004-data-architecture` · `PB-004-DIAGRAM` |
| De-ID×EQ | `DEID-EQ-5MIN` · `DEID-MISS-5MIN` · `REDCAP-DEID-EXPORT-CHECKLIST` |
| BN visit / CLIN | `BN-VISIT-5MIN` · `CLIN-BN-EQ-5MIN` · `CLIN-BN-5MIN` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| YTESO×EQ | `YTESO-EQ-5MIN` · `YTESO-5MIN` |
| TT43 / ICF | `TT43-EQ-5MIN` · `ICF-EQ-5MIN` · `ICF-NEST-5MIN` |

## Cấm

- Order Specimen/omics khi consent nested chưa duyệt  
- Đưa PII vào git / memory / Drive public  
- Coi mermaid / diagram = REDCap đã live · AUROC trên file còn PII  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5/T7) · Protocol: `../../rituals/daily-protocol.md`  
- Bridge: `DESIGN-YTESO-EARLY-SIGNAL-BRIDGE` · `y-te-so-precure-bridge-v0.1.md`
