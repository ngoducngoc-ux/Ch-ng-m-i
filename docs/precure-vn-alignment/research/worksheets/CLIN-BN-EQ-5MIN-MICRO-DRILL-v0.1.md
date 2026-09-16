# Micro-drill 5′ — CLIN-BN × EQ (dọc L1 · ladder Z · ≠ Y)

**Mã:** CLIN-BN-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T7** · sau `CLIN-BN-5MIN` / `AI-STACK-EQ-5MIN` / `EQ-M0M3-5MIN` · trước claim “đã có dữ liệu dọc / ES”  
**Goal:** ACTIVE · event ≠ \(Y(t^*)\) · M0–M3 trên \(Z\) · không PHI · omics CLOSED · PREP ≠ DONE  

## Một câu

> CLIN-BN×EQ 5′ = map StudyID→visits→\(Z\)/`clin_event` **và** 1 dòng ladder M0–M3 — event **không** lấy từ primary; SYN ≠ BN; ladder trên map de-ID **≠** claim AUROC lâm sàng.

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
Cặp đã đụng: CLIN-BN | CLIN_EVENT | BN-VISIT | DEID-EQ | EQ-M0M3 | L1L2L3-EQ | AI-STACK-EQ — ghi: ________
1 việc nhỏ ≤30′ (map 1 hàng / EQ Drill 10′ / deny-list): ________
Đóng Goal / mở L3 vì CLIN-BN×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| CLIN×BN alone | `CLIN-BN-5MIN` · `CLIN_EVENT-5MIN` · `BN-VISIT-5MIN` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| De-ID×EQ | `DEID-EQ-5MIN` · `DEID-MISS-5MIN` |
| L1 gate | `L1L2L3-EQ-5MIN` · `L1L2L3-5MIN` |
| AI-STACK×EQ | `AI-STACK-EQ-5MIN` · `AI-STACK-5MIN` |
| ALERT | `ALERT-CROSS-5MIN` · `NATMED-ALERT-5MIN` |
| YTESO×EQ | **`YTESO-EQ-5MIN`** · `YTESO-5MIN` |
| PB004×EQ | **`PB004-EQ-5MIN`** · `PB004-5MIN` · `BN-VISIT-5MIN` |
| BN-VISIT×EQ | **`BN-VISIT-EQ-5MIN`** · `BN-VISIT-5MIN` |
| CLIN_EVENT×EQ | **`CLIN_EVENT-EQ-5MIN`** · `CLIN_EVENT-5MIN` |

## Cấm

- Event mã từ chính \(Y(t^*)\) / primary  
- Paste MRN/DOB/họ tên · coi SYN = BN  
- AUROC claim / mở omics vì đã map + ladder  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T7) · Protocol: `../../rituals/daily-protocol.md`  
- Atlas: `CLIN_EVENT-CROSS-SA-ATLAS` · `BN-VISIT-MAP-TEMPLATE`
