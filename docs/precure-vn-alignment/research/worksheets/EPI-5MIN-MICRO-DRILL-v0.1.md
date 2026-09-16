# Micro-drill 5′ — EPI SA-01 early window (PCT/CFU/VAS D0–D7)

**Mã:** EPI-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T2** · EQ-SA01 · bridge #0 · sau `IMAGEJ-QA-5MIN`/`ALERT-5MIN` · trước claim “đã có early-signal SA-01”  
**Goal:** ACTIVE · primary D21 không đổi · L3 CLOSED · PREP ≠ DONE · synthetic ≠ BN  

## Một câu

> Early-signal SA-01 = \(Z\) **D0/D3/D7** (PCT_EPITH / CFU / VAS_DRESS / `clin_event`) — **không** dùng PCT **D21** làm predictor “early”; ImageJ QA trước mọi claim AI trên PCT.

## Drill (điền)

```text
t* primary: D21 biểu mô 100% ImageJ — ĐÚNG | SAI — ghi: ________
t' early window hôm nay dùng: D0 | D3 | D7 | D21 — chọn (không D21): ________
Z đang ôn: PCT_EPITH | CFU | VAS_DRESS | clin_event — chọn: ________
PCT_D21 làm feature early? KHÔNG — vì: ________
Order PEA vì đã ôn EPI? KHÔNG — L3 CLOSED
1 việc nhỏ ≤30′ (EQ / IMAGEJ / ALERT / shift): ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Window đầy đủ | `EPI-SA01-EARLY-WINDOW` |
| ImageJ QA | `IMAGEJ-QA-5MIN` |
| ALERT | `ALERT-5MIN` · NatMed map |
| Leakage | `LEAKAGE-5MIN` · atlas SA-01 |
| Omics gate | `PB009-5MIN` · `PEA-5MIN` |

## Cấm

- Coi PCT/CFU D21 là early-signal  
- AUROC sandbox = bằng chứng BN  
- Mở PEA vì đã đọc EPI/EQ  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2)  
- Shift: `PRECURE-SHIFT-CROSS-SA-BANK` · Protocol: `../../rituals/daily-protocol.md`
