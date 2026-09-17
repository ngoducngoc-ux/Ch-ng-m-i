# PB004-EQ — thẻ khoa học 1 trang (StudyID–Visit–Obs × ladder · consent/PII · L3 CLOSED) · refresh v0.1b

**Mã:** PB004-EQ-SCIENCE-CARD-v0.1b · **Ngày:** 2026-09-16  
**Goal:** ACTIVE · STREAK thật vẫn **2 DONE** · EQ bank **CLOSED** · densify ≠ DONE  
**STREAK&lt;3?** Path STREAK3 trước · **`STREAK3-PACK`** · NATMED · ALERT · FILL-AID → tick **19/09** · dừng OPENER/stack  
**STREAK≥3?** **`AFTER-STREAK3-OPENER`** → 1×EQ sibling → **`DAILY-STACK`** · bridges #0–14  
**Không:** agent tick DONE · UpdateGoal complete trên PREP/densify · invent EQ · densify = DONE · PII vào git · order Specimen vì sơ đồ+ladder · AUROC trên file còn PII · M4/X mở  
**Neo:** YTESO-EQ (refresh v0.1b) · `PB004-EQ-5MIN` · PB004-SCIENCE-CARD · DEID-EQ · CLIN-BN-EQ · BN-VISIT · EQ-M0M3 / EQ02 / EQ05  
**Căn cứ:** PB-004-data-architecture · PB-004-DIAGRAM · G2 CLOSED · L3 CLOSED  
**Dùng khi:** STREAK≥3 · Daily stack **T5/T7** · trước claim “đã sẵn sàng omics/AI trên data” · cặp PB004×EQ  
**Hub:** `YTESO-EQ-SCIENCE-CARD` (refresh v0.1b) · tip tiếp `BN-VISIT-EQ-SCIENCE-CARD` · Drive keep `1Vjchf1i…`  

```text
STREAK <3? → STREAK3 (PI-NEXT) · densify ≠ DONE
        ↓ STREAK ≥3
OPENER → EQ sibling → DAILY-STACK · ritual theo Ngày N
```

## Mục đích

Ôn **cặp PB004×EQ**: 1 entity (StudyID / Visit / ClinicalObs) **và** 1 dòng ladder M0–M3 trên \(Z\) de-ID (EQ sibling **đã có**, không invent) — sơ đồ Git ≠ REDCap live; consent nested trước Specimen; không AUROC khi còn PII. Khác `PB004-SCIENCE-CARD` (kiến trúc alone) / `YTESO-EQ` (ba trụ×ladder) / `CLIN-BN-EQ` (map×ladder) — thẻ này neo **kiến trúc data × ladder**.

**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · HAWTHORNE · MEDIA · FILL-AID → tick **19/09** trước  

**Mở song song:** thẻ này · `PB004-EQ-5MIN` · `PB004-SCIENCE-CARD` · `DEID-EQ-SCIENCE-CARD` · **`YTESO-EQ-SCIENCE-CARD`** · `CLIN-BN-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD`

## Giữ / bỏ (PB004 × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) de-ID + StudyID+visit · bank **CLOSED** | M4 / X / L3 · invent EQ |
| **StudyID** | SA-xx-NNN thay MRN analysis | Map ngược công khai |
| **Visit / Obs** | Chuỗi dọc · \(Z\)/`clin_event` | Snapshot = “dọc” · PHI trong Obs |
| **Specimen** | **CLOSED** đến G2+consent | Order vì đã vẽ sơ đồ + ladder |
| **PII** | Deny-list · export StudyID+visit+Z | PII trong git / memory / Drive public |
| **Order / Goal** | KHÔNG từ densify | AUROC trên file còn PII · đóng Goal |
| **Agent densify** | Anti-forget · hub wire | ≠ invent EQ / tick DONE / paste PII |

## Phương trình ranh giới

```text
1 entity PB-004  +  EQ ladder M0–M3 trên Z de-ID
  =  bước data architecture hợp lệ hôm nay
Consent nested + de-ID  ≥  trước  Specimen / omics / AI claim
Git diagram  ≠  REDCap live site
PII  ∉  git / Drive public
Viết entity / ladder / densify  ≠  order Specimen  ≠  DONE
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T5|T7 · SA neo: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________ (không invent)
Entity hôm nay: StudyID|Visit|ClinicalObs|Media|Specimen — ________
Consent lưu mẫu / tái phân tích omics? CHƯA|NHÁP ICF|CÓ — version: ________
1 dòng Z / M0→M3 trên StudyID+visit (de-ID): ________
PII trong repo / memory / Drive public? KHÔNG — vì: ________
Export analysis DB có tên/SĐT/MRN? KHÔNG
Diagram mermaid = REDCap live? KHÔNG
Order Specimen / mở G2 vì PB004×EQ? KHÔNG
Cặp DEID-EQ / BN-VISIT-EQ / CLIN-BN-EQ / YTESO-EQ / ICF-EQ hôm nay? ________
1 việc ≤30′ (checklist consent / deny-list / EQ Drill 10′): ________
Đóng Goal / invent EQ / mở L3 vì PB004×EQ? KHÔNG
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
| **thẻ này** | PB004×EQ bridge · refresh v0.1b |
| `PB004-EQ-5MIN` | Drill điền |
| `PB004-SCIENCE-CARD` | Kiến trúc alone |
| **`YTESO-EQ-SCIENCE-CARD`** | Ba trụ × ladder (hub trước) |
| tip **`BN-VISIT-EQ-SCIENCE-CARD`** | StudyID→visits × ladder |
| `DEID-EQ` / `CLIN-BN-EQ` / EQ siblings | de-ID / map / ladder |
| `ICF-EQ` / `TT43-EQ` | Consent / TT43 × EQ |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Order Specimen/omics khi consent nested chưa duyệt · densify = proof  
- Đưa PII vào git / memory / Drive public · invent EQ  
- Coi mermaid = REDCap live · AUROC trên file còn PII · UpdateGoal trên PREP · agent tick DONE  

## Liên kết

`PB004-EQ-5MIN-MICRO-DRILL` · tip tiếp **`BN-VISIT-EQ-SCIENCE-CARD`** · `PB004-SCIENCE-CARD` · `PB-004-data-architecture` · `PB-004-DIAGRAM` · `DEID-EQ-SCIENCE-CARD` · **`YTESO-EQ-SCIENCE-CARD`** · `CLIN-BN-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · **`BN-VISIT-EQ-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `STREAK3-PACK-SCIENCE-CARD` · Drive keep `1Vjchf1i…` · PREP≠DONE · densify≠DONE  
