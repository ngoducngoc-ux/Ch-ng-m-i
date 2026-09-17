# Micro-drill 5′ — BN-VISIT × EQ (StudyID→visits · ladder Z · ≠ PHI)

**Mã:** BN-VISIT-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T7** · sau `BN-VISIT-5MIN` / `CLIN-BN-EQ-5MIN` / `PB004-EQ-5MIN` / `EQ-M0M3-5MIN` · trước claim “đã có dữ liệu dọc ES”  
**Goal:** ACTIVE · map de-ID · event ≠ \(Y(t^*)\) · M0–M3 trên \(Z\) · omics CLOSED · PREP ≠ DONE  

## Một câu

> BN-VISIT×EQ 5′ = map StudyID→visits→\(Z\)/`clin_event` **và** 1 dòng ladder M0–M3 — không họ tên/MRN; SYN ≠ BN; ladder trên map de-ID **≠** AUROC lâm sàng.

## Drill (điền)

```text
SA neo: 01 | 02 | 05 — chọn: ________
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________
StudyID: SA-__-SYN-___ | de-ID — ghi: ________
Visits tick: D0 | D3 | D7 | D14 | D21(Y) — ________
1 dòng Z / M0→M3 trên visits ≤D7: ________
Schema event: clin_event 0–4 | symptom/AE | AE/ICU — chọn: ________
Event = label Y(t*)? KHÔNG
PHI / omics trên map? KHÔNG / CLOSED
Cặp đã đụng: BN-VISIT | CLIN-BN-EQ | PB004-EQ | DEID-EQ | EQ-M0M3 | CLIN_EVENT — ghi: ________
1 việc nhỏ ≤30′ (map 1 hàng / EQ Drill 10′ / deny-list): ________
Đóng Goal / mở L3 vì BN-VISIT×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| BN-VISIT alone | `BN-VISIT-5MIN` · `BN-VISIT-MAP-TEMPLATE` |
| CLIN-BN×EQ | `CLIN-BN-EQ-5MIN` · `CLIN-BN-5MIN` · `CLIN_EVENT-5MIN` |
| PB004×EQ | `PB004-EQ-5MIN` · `PB004-5MIN` |
| De-ID×EQ | `DEID-EQ-5MIN` · `DEID-MISS-5MIN` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| YTESO / AI | `YTESO-EQ-5MIN` · `AI-STACK-EQ-5MIN` |
| PB005×EQ | **`PB005-EQ-5MIN`** · `PB005-5MIN` |

## Cấm

- Paste MRN / DOB / họ tên / ảnh nhận diện vào log hoặc git  
- Coi SYN map = kết quả lâm sàng · AUROC claim  
- Order PEA / mở L3 vì đã “map đủ visit + ladder”  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T7) · Protocol: `../../rituals/daily-protocol.md`  
- Atlas: `CLIN_EVENT-CROSS-SA-ATLAS` · bridge `Q3-CROSS-SA-YTESO-EARLY-SIGNAL-BRIDGE`

**Densify:** **`BN-VISIT-EQ-SCIENCE-CARD`**
