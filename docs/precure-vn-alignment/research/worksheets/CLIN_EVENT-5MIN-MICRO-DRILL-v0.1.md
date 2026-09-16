# Micro-drill 5′ — `clin_event` / sự kiện dọc (L1)

**Mã:** CLIN_EVENT-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T7** · Zhou #0 · EQ T2 drill A · trước mọi claim “dữ liệu dọc”  
**Goal:** ACTIVE · event ≠ label \(Y(t^*)\) · không PHI · L3 CLOSED · PREP ≠ DONE

## Một câu

> Zhou: omics nhảy khi có **sự kiện** — Smart A bắt analog bằng event dọc trên eCRF **trước** \(X\); mã event **không** lấy từ chính primary endpoint.

## Drill (điền — 1 SA)

```text
SA neo: 01|02|05
Schema event: clin_event 0–4 | symptom/AE | AE/turn ICU
Mã / mô tả event hôm nay: ________
Visit + timestamp đủ L1? CÓ | CHƯA — thiếu: ________
Z cùng cửa sổ: ________
Event = label Y(t*)? KHÔNG — vì: ________
1 câu vì sao chưa cần X/omics hôm nay:
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Atlas 3 SA | `CLIN_EVENT-CROSS-SA-ATLAS-v0.1.md` |
| Mã 0–4 SA-01 | `CLIN_EVENT-ZHOU-MAP` · vignette `CLIN_EVENT-CODING-VIGNETTES` |
| Map BN de-ID | `BN-VISIT-MAP-TEMPLATE` (cùng T7) |
| De-ID trước export | `DEID-5MIN-MICRO-DRILL` |
| Gate L1 | `L1L2L3-DAILY-GATE-CARD` |

## Cấm

- Train “early” bằng chính \(Y(t^*)\) đóng vai event  
- Ghi PHI / tên BN trong log git  
- Mở PEA vì đã mã hóa 1 event  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3-v0.1.md` (T7)  
- Y tế số: `../y-te-so-precure-bridge-v0.1.md` · PB-004  
- Protocol: `../../rituals/daily-protocol.md`
