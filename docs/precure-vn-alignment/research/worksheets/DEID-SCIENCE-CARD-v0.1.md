# DEID — thẻ khoa học 1 trang (export dọc · y tế số · L2 trước AI) · refresh v0.1b

**Mã:** DEID-SCIENCE-CARD-v0.1b · **Ngày:** 2026-09-16  
**Goal:** ACTIVE · STREAK thật vẫn **2 DONE** · EQ bank **CLOSED** · densify ≠ DONE  
**STREAK&lt;3?** Path STREAK3 trước · **`STREAK3-PACK`** · **`STREAK3-EQ`** · NatMed → tick **19/09** · dừng OPENER/stack  
**STREAK≥3?** **`AFTER-STREAK3-OPENER`** → 1×EQ sibling → **`DAILY-STACK`** · bridges #0–14  
**Không:** agent tick DONE · UpdateGoal complete trên PREP/densify · invent EQ · densify = DONE · PHI vào git  
**Neo:** BN-VISIT (refresh v0.1b) · `REDCAP-DEID-EXPORT-CHECKLIST` · PB-004 · Q2 #5  
**Dùng khi:** T5/T7 · Q2 staging · trước mọi claim M0–M3 trên “export” · y tế số trụ AI  
**Hub:** `BN-VISIT-SCIENCE-CARD` (refresh v0.1b) · tip tiếp `AI-STACK-SCIENCE-CARD` · Drive keep `1Vjchf1i…`  

```text
STREAK <3? → STREAK3 (PI-NEXT) · densify ≠ DONE
        ↓ STREAK ≥3
OPENER → EQ sibling → DAILY-STACK · ritual theo Ngày N
```

## Mục đích

Ôn **cổng de-ID** trước AI trên dữ liệu dọc Smart A: file analysis chỉ StudyID + \(Z\)/`clin_event`/visit — **deny list trước allow list**. Không PHI · không omics raw trước G2; densify ≠ export lâm sàng / L2 CLOSED.

**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · HAWTHORNE · MEDIA · FILL-AID → tick **19/09** trước  

**Mở song song:** thẻ này · `REDCAP-DEID-EXPORT-CHECKLIST` · tip **`AI-STACK-SCIENCE-CARD`** · **`BN-VISIT-SCIENCE-CARD`** (refresh v0.1b) · **`DEID-EQ-SCIENCE-CARD`** · `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · `CLIN_EVENT-SCIENCE-CARD`

## Bốn lớp PB-004

| Lớp | Ví dụ | Rời site? |
|-----|-------|-----------|
| **Identified** | Họ tên · SĐT · MRN · DOB đầy đủ · ICF scan | **Không** |
| **StudyID** | `SA-01-XXX` | Có (analysis) |
| **Analysis** | visit · \(Z\) · `clin_event` · adhere | Có (de-ID) |
| **Public** | Aggregate only | Công bố |
| **Agent densify** | Anti-forget · hub wire | ≠ export thật / PHI OK |

## Deny → allow (1 hàng)

```text
Deny trước: D1–D7 (PII · MRN · DOB · free-text · media · ICF · omics raw)
Allow: StudyID + visit + Z + clin_event (không PHI)
QC PASS ≠ bằng chứng BN   ·   --demo ≠ export thật
Ôn DEID / densify  ≠  L2 CLOSED  ≠  DONE
```

## Checklist 15′ (1 SA)

```text
Thứ: T5|T7|STREAK3 · SA: 01|02|05 — chọn: ________
Đã mở DEID + BN-VISIT + AI-STACK thẻ? ________
1 field CẤM nếu lọt export: ________
1 field CHO PHÉP analysis: ________
StudyID đủ thay MRN? CÓ | CHƯA
Omics raw trong export? KHÔNG (CLOSED) — vì: ________
1 câu QC PASS ≠ BN: ________
Densify = export lâm sàng? KHÔNG
1 việc ≤30′ (REDCAP-DEID tick / DEID-5MIN / **DEID-MISS-SCIENCE-CARD** / PB004 / BN-VISIT): ________
Đóng Goal / claim M0–M3 vì “đã de-ID drill”? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / REDCAP-DEID | Deny/allow export |
| tip **`AI-STACK-SCIENCE-CARD`** | L2 cần de-ID trước M0–M3 · densify tiếp |
| **`BN-VISIT-SCIENCE-CARD`** (refresh v0.1b) | Hub trước · StudyID→visit→Z trước export |
| `CLIN_EVENT-SCIENCE-CARD` | Schema event trong allow list |
| `LEAKAGE-SCIENCE-CARD` | Feature hợp lệ sau de-ID vẫn ≠ leakage-free nếu \(t^*\) |
| `SYNTH-SCIENCE-CARD` | `--demo` ≠ export de-ID thật |

## Cấm

- Commit CSV có tên/SĐT/MRN/DOB / ICF scan  
- Coi synthetic / densify = export de-ID thật · mở G2 vì đã điền drill  
- Agent tick DONE · đóng Goal / invent EQ · densify = DONE  

## Liên kết

`REDCAP-DEID-EXPORT-CHECKLIST` · tip tiếp **`AI-STACK-SCIENCE-CARD`** · **`DEID-MISS-SCIENCE-CARD`** · `DEID-5MIN` · `DEID-EQ-5MIN` · **`DEID-EQ-SCIENCE-CARD`** · `DEID-MISS-5MIN` · `PB004-5MIN` · **`BN-VISIT-SCIENCE-CARD`** (refresh v0.1b) · `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · `CLIN_EVENT-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · **`PB004-SCIENCE-CARD`** · **`MISSINGNESS-SCIENCE-CARD`** · **`ICF-NEST-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · **`PB009-SCIENCE-CARD`** · `DAILY-STACK-AFTER-STREAK3` · `STREAK3-PACK-SCIENCE-CARD` · Drive keep `1Vjchf1i…` · PREP≠DONE · densify≠DONE  
