# PB004-EQ — thẻ khoa học 1 trang (StudyID–Visit–Obs × ladder · consent/PII · L3 CLOSED)

**Mã:** PB004-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `PB004-EQ-5MIN-MICRO-DRILL` · PB004-SCIENCE-CARD · DEID-EQ · YTESO-EQ · CLIN-BN-EQ · BN-VISIT · EQ-M0M3 / EQ02 / EQ05  
**Căn cứ:** PB-004-data-architecture · PB-004-DIAGRAM · G2 CLOSED · L3 CLOSED  
**Dùng khi:** STREAK≥3 · Daily stack **T5/T7** · trước claim “đã sẵn sàng omics/AI trên data” · cặp PB004×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · consent + de-ID trước omics · M0–M3 trên \(Z\) · PII ∉ git/Drive public · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp PB004×EQ**: 1 entity (StudyID / Visit / ClinicalObs) **và** 1 dòng ladder M0–M3 trên \(Z\) de-ID — sơ đồ Git ≠ REDCap live; consent nested trước Specimen; không AUROC khi còn PII. Khác `PB004-SCIENCE-CARD` (kiến trúc alone) / `YTESO-EQ` (ba trụ×ladder) / `CLIN-BN-EQ` (map×ladder) — thẻ này neo **kiến trúc data × ladder**.

**Mở song song:** thẻ này · `PB004-EQ-5MIN` · `PB004-SCIENCE-CARD` · `DEID-EQ-SCIENCE-CARD` · `YTESO-EQ-SCIENCE-CARD` · `CLIN-BN-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD`

## Giữ / bỏ (PB004 × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) de-ID + StudyID+visit | M4 / X / L3 |
| **StudyID** | SA-xx-NNN thay MRN analysis | Map ngược công khai |
| **Visit / Obs** | Chuỗi dọc · \(Z\)/`clin_event` | Snapshot = “dọc” · PHI trong Obs |
| **Specimen** | **CLOSED** đến G2+consent | Order vì đã vẽ sơ đồ + ladder |
| **PII** | Deny-list · export StudyID+visit+Z | PII trong git / memory / Drive public |
| **Order / Goal** | KHÔNG từ densify | AUROC trên file còn PII · đóng Goal |

## Phương trình ranh giới

```text
1 entity PB-004  +  EQ ladder M0–M3 trên Z de-ID
  =  bước data architecture hợp lệ hôm nay
Consent nested + de-ID  ≥  trước  Specimen / omics / AI claim
Git diagram  ≠  REDCap live site
PII  ∉  git / Drive public
Viết entity / ladder  ≠  order Specimen
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T5|T7 · SA neo: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
Entity hôm nay: StudyID|Visit|ClinicalObs|Media|Specimen — ________
Consent lưu mẫu / tái phân tích omics? CHƯA|NHÁP ICF|CÓ — version: ________
1 dòng Z / M0→M3 trên StudyID+visit (de-ID): ________
PII trong repo / memory / Drive public? KHÔNG — vì: ________
Export analysis DB có tên/SĐT/MRN? KHÔNG
Diagram mermaid = REDCap live? KHÔNG
Order Specimen / mở G2 vì PB004×EQ? KHÔNG
Cặp DEID-EQ / BN-VISIT-EQ / CLIN-BN-EQ / YTESO-EQ / ICF-EQ hôm nay? ________
1 việc ≤30′ (checklist consent / deny-list / EQ Drill 10′): ________
Đóng Goal vì PB004×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở PB004 + EQ sibling thẻ riêng trước cặp? ________
Entity+ladder = lý do order Specimen / AUROC? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | PB004×EQ bridge 1 trang |
| `PB004-EQ-5MIN` | Drill điền |
| `PB004-SCIENCE-CARD` | Kiến trúc alone |
| `DEID-EQ` / `BN-VISIT-EQ` / `CLIN-BN-EQ` | de-ID / visit / map × ladder |
| `EQ-M0M3` / EQ02 / EQ05 | Ladder sibling |
| `YTESO-EQ` / `ICF-EQ` / `TT43-EQ` | Y tế số / consent / TT43 × EQ |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Order Specimen/omics khi consent nested chưa duyệt  
- Đưa PII vào git / memory / Drive public  
- Coi mermaid = REDCap live · AUROC trên file còn PII · UpdateGoal trên PREP  

## Liên kết

`PB004-EQ-5MIN-MICRO-DRILL` · `PB004-SCIENCE-CARD` · `PB-004-data-architecture` · `PB-004-DIAGRAM` · `DEID-EQ-SCIENCE-CARD` · `YTESO-EQ-SCIENCE-CARD` · `CLIN-BN-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
