# Micro-drill 5′ — De-ID × Missingness (export · %miss · trước AUROC)

**Mã:** DEID-MISS-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5 / T7** · Q2–Q3 L2 · sau `DEID-5MIN` + `MISSINGNESS-5MIN` · trước claim M0–M3 trên N  
**Goal:** ACTIVE · không PHI · `[chưa N]` nếu chỉ demo · L3 CLOSED · PREP ≠ DONE  

## Một câu

> DEID×MISS 5′ = deny-list trước allow-list **và** biết %miss theo visit — `--demo`/synthetic **≠** export de-ID thật; **không** báo AUROC khi miss chưa audit hoặc file còn PII.

## Drill (điền)

```text
SA neo: 01|02|05 — chọn: ________
N hôm nay: --demo | de-ID thật (site) — ghi: ________
1 field CẤM export (D1–D7): ________
1 field CHO PHÉP (Z / clin_event / visit): ________
StudyID đủ thay MRN? CÓ | CHƯA
Visit ôn: D0 | D3 | D7 · Z: PCT|CFU|VAS|clin_event — chọn: ________
%miss (hoặc [chưa N]): ________
Omics raw trong export? KHÔNG
Báo AUROC khi PII risk / miss chưa audit / demo? KHÔNG
Cặp đã đụng: DEID-5MIN | MISSINGNESS-5MIN | TRIPOD-SYNTH | PB004 | BN-VISIT | LEAKAGE — ghi: ________
1 việc nhỏ ≤30′ (deny-list skim / L2 audit 1 ô / QC note): ________
Đóng Goal / mở G2 vì DEID-MISS? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| De-ID alone | `DEID-5MIN` · `REDCAP-DEID-EXPORT-CHECKLIST` |
| Missingness alone | `MISSINGNESS-5MIN` · `L2-MISSINGNESS-AUDIT` |
| StudyID / visit | `PB004-5MIN` · `BN-VISIT-5MIN` |
| AI claim | `TRIPOD-SYNTH-5MIN` · `LEAKAGE-5MIN` |
| Q2/Q3 | `Q2-STAGING-DEID-RITUAL-CARD` · `Q3-L2-EXPORT-EARLY-SIGNAL-BRIDGE` |

## Cấm

- Commit CSV có tên/SĐT/MRN/DOB  
- Điền %miss giả từ sandbox như N thật  
- Báo AUROC / mở G2 vì demo QC PASS  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5/T7) · Protocol: `../../rituals/daily-protocol.md`  
- Gate: `L1L2L3-DAILY-GATE-CARD` · PB-009 L2.1
