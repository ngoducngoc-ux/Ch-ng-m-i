# Micro-drill 5′ — Export de-ID (y tế số · L2 trước AI)

**Mã:** DEID-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5 / T7** · Q2 #5 · y-te-so trụ AI · trước mọi claim M0–M3 trên “export”  
**Goal:** ACTIVE · không PHI trong git/Drive public · sandbox ≠ export thật · PREP ≠ DONE

## Một câu

> Trước khi nói “AI trên dữ liệu dọc” — xác nhận file analysis **không** mang PII; deny list trước allow list.

## Drill (điền — không cần BN thật)

```text
SA neo: 01|02|05
1 field CẤM nếu lọt export (D1–D7): ________
1 field CHO PHÉP analysis (Z / clin_event / visit): ________
StudyID có đủ thay MRN? CÓ | CHƯA
Omics raw trong export hôm nay? KHÔNG (CLOSED) vì: ________
1 câu: QC PASS ≠ bằng chứng BN vì: ________
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Deny/allow đầy đủ | `REDCAP-DEID-EXPORT-CHECKLIST-v0.1.md` |
| L1 event / visit | `CLIN_EVENT-CROSS-SA-ATLAS` · `BN-VISIT-MAP-TEMPLATE` |
| L2 gate | `L1L2L3-DAILY-GATE-CARD` · PB-009 L2.1 · **`DEID-MISS-5MIN`** |
| De-ID×EQ | **`DEID-EQ-5MIN`** · EQ ladders |
| Leakage sau de-ID | `LEAKAGE-CROSS-SA-ATLAS` |

## Cấm

- Commit CSV có tên/SĐT/MRN/DOB đầy đủ  
- Coi `--demo` / synthetic = export de-ID thật  
- Mở G2 vì đã điền đủ ô drill  

## Liên kết

- **Thẻ khoa học:** **`DEID-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`
- Q2: `Q2-STAGING-DEID-RITUAL-CARD` · bridge `#5`  
- Y tế số: `../y-te-so-precure-bridge-v0.1.md`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3-v0.1.md` (T5/T7)  
- Protocol: `../../rituals/daily-protocol.md`
