# Micro-drill 5′ — CLIN_EVENT × EQ (dọc L1 · ladder Z · ≠ Y)

**Mã:** CLIN_EVENT-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T7** · sau `CLIN_EVENT-5MIN` / `CLIN-BN-EQ-5MIN` / `EQ-M0M3-5MIN` / `BN-VISIT-EQ-5MIN` · trước claim “đã có dữ liệu dọc ES”  
**Goal:** ACTIVE · event ≠ \(Y(t^*)\) · M0–M3 trên \(Z\) cùng cửa sổ · không PHI · L3 CLOSED · PREP ≠ DONE  

## Một câu

> CLIN_EVENT×EQ 5′ = 1 schema event (0–4 / AE / ICU) **và** 1 dòng ladder M0–M3 trên \(Z\) — event **không** lấy từ primary; map de-ID trước omics.

## Drill (điền — 1 SA)

```text
SA neo: 01|02|05 — chọn: ________
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________
Schema: clin_event 0–4 | symptom/AE | AE/turn ICU — chọn: ________
Mã / mô tả event: ________
Visit + timestamp đủ L1? CÓ | CHƯA — thiếu: ________
1 dòng Z / M0→M3 cùng cửa sổ: ________
Event = label Y(t*)? KHÔNG
PHI / omics? KHÔNG / CLOSED
Cặp đã đụng: CLIN_EVENT | CLIN-BN-EQ | BN-VISIT-EQ | DEID-EQ | ALERT-EQ — ghi: ________
1 việc nhỏ ≤30′ (vignette / EQ Drill 10′ / deny-list): ________
Đóng Goal / mở L3 vì CLIN_EVENT×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| CLIN_EVENT alone | `CLIN_EVENT-5MIN` · `CLIN_EVENT-CROSS-SA-ATLAS` · vignettes |
| CLIN-BN×EQ | `CLIN-BN-EQ-5MIN` · `CLIN-BN-5MIN` · `BN-VISIT-EQ-5MIN` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| De-ID | `DEID-EQ-5MIN` · `DEID-5MIN` |
| ALERT×EQ | `ALERT-EQ-5MIN` · `ALERT-5MIN` |

## Cấm

- Train early bằng chính \(Y(t^*)\) đóng vai event  
- Ghi PHI trong log/git · mở PEA vì đã mã 1 event  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T7) · Protocol: `../../rituals/daily-protocol.md`  
- Bridge: `y-te-so-precure-bridge` · PB-004
