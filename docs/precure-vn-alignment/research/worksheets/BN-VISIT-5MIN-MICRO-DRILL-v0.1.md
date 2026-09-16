# Micro-drill 5′ — BN visit map (de-ID · y tế số dọc)

**Mã:** BN-VISIT-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T7** · Q3 #9 · sau `CLIN_EVENT-5MIN` · rehearsal PB-004  
**Goal:** ACTIVE · PHI ngoài git/Drive public · synthetic ≠ BN · L3 CLOSED · PREP ≠ DONE

## Một câu

> Map **StudyID → visits → Z/`clin_event`** là luyện dọc y tế số — **không** họ tên/SĐT/MRN; omics mặc định CLOSED.

## Drill (điền)

```text
StudyID hôm nay: SA-__-SYN-___ | SA-__-___ (nếu có N de-ID)
Visits có (tick): D0 | D3 | D7 | D14 | D21(Y)
1 Z chính ≤D7: ________ · clin_event 0–4: __
PHI trong map? KHÔNG — vì: ________
Omics/specimen trên map? KHÔNG | chỉ nếu G2 — trạng thái: CLOSED
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Template đầy đủ | `BN-VISIT-MAP-TEMPLATE` |
| Event ≠ Y | `CLIN_EVENT-5MIN` · atlas clin_event · **`CLIN-BN-5MIN`** |
| De-ID deny/allow | `DEID-5MIN` · `REDCAP-DEID-EXPORT-CHECKLIST` |
| Bridge Q3 | `Q3-CROSS-SA-YTESO-EARLY-SIGNAL-BRIDGE` |

## Cấm

- Paste MRN / DOB / ảnh nhận diện vào log hoặc git  
- Coi rehearsal SYN = kết quả lâm sàng  
- Order PEA vì đã “map đủ visit trên giấy”  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T7)  
- PB-004 · `y-te-so-precure-bridge` · Protocol: `../../rituals/daily-protocol.md`
