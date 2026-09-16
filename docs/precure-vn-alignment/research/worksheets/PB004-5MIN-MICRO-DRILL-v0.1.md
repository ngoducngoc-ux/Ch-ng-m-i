# Micro-drill 5′ — PB-004 data architecture (consent / StudyID / visit)

**Mã:** PB004-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5/T7** · bridge #3/#9 · Ngày 21 · sau `TT43-5MIN`/`DEID-5MIN` · trước claim “đã sẵn sàng omics/AI trên data”  
**Goal:** ACTIVE · L3 CLOSED · G2 CLOSED · PII không vào git/Drive public · PREP ≠ DONE  

## Một câu

> PB-004 = StudyID → Visit → ClinicalObs/Media/(Specimen) — **consent + de-ID** trước omics; sơ đồ Git ≠ hệ đã triển khai tại site.

## Drill (điền)

```text
Entity tối thiểu hôm nay: StudyID | Visit | ClinicalObs | Media | Specimen — chọn: ________
Consent cho lưu mẫu / tái phân tích omics? CHƯA | NHÁP ICF | CÓ — ghi version: ________
PII trong repo / agent memory / Drive public? KHÔNG — vì: ________
Export analysis DB có tên/SĐT/địa chỉ? KHÔNG — lớp: StudyID+visit+Z/X de-ID
1 việc nhỏ ≤30′ (checklist consent / diagram / DEID): ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Kiến trúc đầy đủ | `PB-004-data-architecture` |
| Sơ đồ | `PB-004-DIAGRAM` |
| De-ID cặp | `DEID-5MIN` · `REDCAP-DEID-EXPORT-CHECKLIST` |
| Visit map | `BN-VISIT-5MIN` |
| Phê duyệt VN | `TT43-5MIN` |
| Bridge T2 | `DESIGN-YTESO-EARLY-SIGNAL-BRIDGE` |

## Cấm

- Order Specimen/omics khi consent nested chưa duyệt  
- Đưa PII vào git / memory / Drive public  
- Coi mermaid diagram = REDCap đã live tại site  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5/T7)  
- Ritual: `DESIGN-YTESO-AI-RITUAL-CARD` · Protocol: `../../rituals/daily-protocol.md`
