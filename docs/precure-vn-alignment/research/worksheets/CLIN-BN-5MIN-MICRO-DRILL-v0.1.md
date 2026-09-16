# Micro-drill 5′ — clin_event × BN-visit (dọc L1 · de-ID · ≠ Y)

**Mã:** CLIN-BN-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T7** · sau/trước `CLIN_EVENT-5MIN` + `BN-VISIT-5MIN` · trước claim “đã có dữ liệu dọc”  
**Goal:** ACTIVE · event ≠ label \(Y(t^*)\) · không PHI · omics CLOSED · PREP ≠ DONE  

## Một câu

> CLIN×BN 5′ = map **StudyID → visits → Z/`clin_event`** với event **không** lấy từ primary — luyện dọc y tế số; **không** MRN/họ tên · **không** omics · **không** coi SYN = BN.

## Drill (điền)

```text
SA neo: 01|02|05 — chọn: ________
StudyID: SA-__-SYN-___ | SA-__-___ (de-ID) — ghi: ________
Visits: D0 | D3 | D7 | D14 | D21(Y) — tick có: ________
Schema event: clin_event 0–4 | symptom/AE | AE/turn ICU — chọn: ________
Mã/mô tả event hôm nay: ________
Z cùng cửa sổ ≤D7: ________
Event = label Y(t*)? KHÔNG
PHI trong map/log? KHÔNG
Omics/specimen trên map? CLOSED
Cặp đã đụng: CLIN_EVENT-5MIN | BN-VISIT-5MIN | DEID-MISS | PB004 | ALERT | L1L2L3 — ghi: ________
1 việc nhỏ ≤30′ (atlas 1 hàng / map template / deny-list skim): ________
Đóng Goal / mở L3 vì CLIN-BN? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Event alone | `CLIN_EVENT-5MIN` · atlas · Zhou map |
| Visit alone | `BN-VISIT-5MIN` · `BN-VISIT-MAP-TEMPLATE` |
| De-ID / miss | `DEID-MISS-5MIN` · `DEID-5MIN` · `PB004-5MIN` |
| Gate L1 | `L1L2L3-5MIN` · `L1L2L3-DAILY-GATE-CARD` |
| ALERT dọc | `ALERT-5MIN` · `NATMED-ALERT-5MIN` |
| CLIN-BN×EQ | **`CLIN-BN-EQ-5MIN`** · EQ ladders |

## Cấm

- Event mã từ chính \(Y(t^*)\) / primary  
- Paste MRN/DOB/họ tên vào log hoặc git  
- Coi SYN map = kết quả lâm sàng / mở omics  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T7) · Protocol: `../../rituals/daily-protocol.md`  
- Bridge: `Q3-CROSS-SA-YTESO-EARLY-SIGNAL-BRIDGE`
