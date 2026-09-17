# Micro-drill 5′ — De-ID × EQ (export · ladder Z · trước AUROC)

**Mã:** DEID-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5 / T7** · sau `DEID-5MIN` / `DEID-MISS-5MIN` / `EQ-M0M3-5MIN` · trước claim M0–M3 / AUROC trên “export”  
**Goal:** ACTIVE · không PHI · ladder chỉ trên \(Z\) de-ID · `--demo` ≠ N · L3 CLOSED · PREP ≠ DONE  

## Một câu

> DEID×EQ 5′ = 1 dòng ladder M0–M3 trên field \(Z\) **đã** deny-list — StudyID thay MRN; **không** AUROC / M3 claim khi còn PII risk, miss chưa audit, hoặc chỉ `--demo`.

## Drill (điền)

```text
SA neo: 01 | 02 | 05 — chọn: ________
EQ sibling: EQ-M0M3 | EQ02-M0M3 | EQ05-M0M3 — chọn: ________
N hôm nay: --demo | de-ID thật (site) — ghi: ________
1 field CẤM export (D1–D7): ________
1 field CHO PHÉP = Z / clin_event / visit: ________
1 dòng Z / M0→M3 (chỉ field allow): ________
StudyID đủ thay MRN? CÓ | CHƯA
Omics raw / X_PEA trong export? KHÔNG
Báo AUROC khi PII / demo / miss chưa audit? KHÔNG
Cặp đã đụng: DEID-5MIN | DEID-MISS | EQ-M0M3 | TRIPOD-EQ | LEAK-CROSS | PB004 — ghi: ________
1 việc nhỏ ≤30′ (deny-list skim / EQ Drill 10′ / L2 audit 1 ô): ________
Đóng Goal / mở G2 vì DEID×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| De-ID alone | `DEID-5MIN` · `REDCAP-DEID-EXPORT-CHECKLIST` |
| De-ID×MISS | `DEID-MISS-5MIN` · `L2-MISSINGNESS-AUDIT` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| AI / TRIPOD | `TRIPOD-EQ-5MIN` · `TRIPOD-SYNTH-5MIN` |
| Leakage | `LEAK-CROSS-5MIN` · `LEAKAGE-5MIN` |
| Q2/Q3 | `Q2-STAGING-DEID-RITUAL-CARD` · `Q3-L2-EXPORT-EARLY-SIGNAL-BRIDGE` |
| ISO-SWAB×EQ | **`ISO-SWAB-EQ-5MIN`** · `OMICS-IF-5MIN` |
| CLIN-BN×EQ | **`CLIN-BN-EQ-5MIN`** · `CLIN-BN-5MIN` |
| PB004×EQ | **`PB004-EQ-5MIN`** · `PB004-5MIN` |
| BN-VISIT×EQ | **`BN-VISIT-EQ-5MIN`** · `BN-VISIT-5MIN` |
| MISSINGNESS×EQ | **`MISSINGNESS-EQ-5MIN`** · `MISSINGNESS-5MIN` |

## Cấm

- Commit CSV có tên/SĐT/MRN/DOB  
- Claim AUROC / M3 trên demo hoặc file còn PII  
- Mở G2 / L3 vì đã viết ladder trên sandbox  

## Liên kết

- **Thẻ khoa học:** **`DEID-EQ-SCIENCE-CARD`** · **`DEID-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`
- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5/T7) · Protocol: `../../rituals/daily-protocol.md`  
- Gate: `L1L2L3-DAILY-GATE-CARD` · PB-009 L2.1
