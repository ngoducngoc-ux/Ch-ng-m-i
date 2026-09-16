# DEID — thẻ khoa học 1 trang (export dọc · y tế số · L2 trước AI)

**Mã:** DEID-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `REDCAP-DEID-EXPORT-CHECKLIST` · PB-004 · Q2 #5  
**Dùng khi:** T5/T7 · Q2 staging · trước mọi claim M0–M3 trên “export” · y tế số trụ AI  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · không PHI git/Drive public · sandbox ≠ export thật · L3/omics raw CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cổng de-ID** trước AI trên dữ liệu dọc Smart A: file analysis chỉ StudyID + \(Z\)/`clin_event`/visit — **deny list trước allow list**. Không PHI · không omics raw trước G2.

**Mở song song:** thẻ này · **`DEID-EQ-SCIENCE-CARD`** · `REDCAP-DEID-EXPORT-CHECKLIST` · `AI-STACK-SCIENCE-CARD` · `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · `CLIN_EVENT-SCIENCE-CARD`

## Bốn lớp PB-004

| Lớp | Ví dụ | Rời site? |
|-----|-------|-----------|
| **Identified** | Họ tên · SĐT · MRN · DOB đầy đủ · ICF scan | **Không** |
| **StudyID** | `SA-01-XXX` | Có (analysis) |
| **Analysis** | visit · \(Z\) · `clin_event` · adhere | Có (de-ID) |
| **Public** | Aggregate only | Công bố |

## Deny → allow (1 hàng)

```text
Deny trước: D1–D7 (PII · MRN · DOB · free-text · media · ICF · omics raw)
Allow: StudyID + visit + Z + clin_event (không PHI)
QC PASS ≠ bằng chứng BN   ·   --demo ≠ export thật
```

## Checklist 15′ (1 SA)

```text
Thứ: T5|T7 · SA: 01|02|05 — chọn: ________
1 field CẤM nếu lọt export: ________
1 field CHO PHÉP analysis: ________
StudyID đủ thay MRN? CÓ | CHƯA
Omics raw trong export? KHÔNG (CLOSED) — vì: ________
1 câu QC PASS ≠ BN: ________
1 việc ≤30′ (REDCAP-DEID tick / DEID-5MIN / **DEID-MISS-SCIENCE-CARD** / PB004): ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / REDCAP-DEID | Deny/allow export |
| `AI-STACK-SCIENCE-CARD` | L2 cần de-ID trước M0–M3 |
| `CLIN_EVENT-SCIENCE-CARD` | Schema event trong allow list |
| `LEAKAGE-SCIENCE-CARD` | Feature hợp lệ sau de-ID vẫn ≠ leakage-free nếu \(t^*\) |
| `SYNTH-SCIENCE-CARD` | `--demo` ≠ export de-ID thật |

## Cấm

- Commit CSV có tên/SĐT/MRN/DOB / ICF scan  
- Coi synthetic = export de-ID thật · mở G2 vì đã điền drill  
- Agent tick DONE · đóng Goal  

## Liên kết

`REDCAP-DEID-EXPORT-CHECKLIST` · **`DEID-MISS-SCIENCE-CARD`** · `DEID-5MIN` · `DEID-EQ-5MIN` · **`DEID-EQ-SCIENCE-CARD`** · `DEID-MISS-5MIN` · `PB004-5MIN` · `AI-STACK-SCIENCE-CARD` · `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · `CLIN_EVENT-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · **`BN-VISIT-SCIENCE-CARD`** · **`PB004-SCIENCE-CARD`** · **`MISSINGNESS-SCIENCE-CARD`** · **`ICF-NEST-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · **`PB009-SCIENCE-CARD`** · `DAILY-STACK-AFTER-STREAK3`
