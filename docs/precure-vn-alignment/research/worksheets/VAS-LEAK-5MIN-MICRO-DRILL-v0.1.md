# Micro-drill 5′ — VAS × Leakage (SA-02 · 0–10 · VAS_D3 ≠ early)

**Mã:** VAS-LEAK-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4** · EQ-SA02 · sau/trước `VAS-5MIN` + `LEAKAGE-5MIN` · trước claim “ES SA-02”  
**Goal:** ACTIVE · primary ΔVAS D3 không đổi · eCRF **0–10** · M1+VAS_D3 = leakage · L3 CLOSED · PREP ≠ DONE  
**DOI:** STPIS [10.1186/1745-6215-15-263](https://doi.org/10.1186/1745-6215-15-263) (literature only) · TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594)

## Một câu

> VAS×LEAK 5′ = thang **0–10** + early chỉ D1/CFU trước D3 — **VAS_D3 trong M early = QC leakage**, không phải evidence; **không** gộp Y với SA-01/05 · **không** đổi 0–100 vì STPIS mm.

## Drill (điền)

```text
eCRF thang: 0–10 | 0–100 — chọn: ________
t* primary: ΔVAS D3 — xác nhận? CÓ
t' early: D1 | CFU_D0 | VAS_D3 — chọn (không VAS_D3): ________
M1 + VAS_D3 = leakage? CÓ — vì: ________
1 feature HỢP LỆ cho t' hôm nay: ________
Gộp Y SA-01/05? KHÔNG
Sandbox AUROC “đẹp” = claim BN? KHÔNG
Cặp đã đụng: VAS-5MIN | LEAKAGE-5MIN | EQ-5MIN | TRIPOD-SYNTH | SYNTH | ALERT-HAWTHORNE | PB002 — ghi: ________
1 việc nhỏ ≤30′ (harmonize sheet / EQ-SA02 / atlas 1 hàng): ________
Đóng Goal / mở L3 vì VAS-LEAK? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| VAS alone | `VAS-5MIN` · `VAS-SCALE-HARMONIZE-SA02` |
| Leakage alone | `LEAKAGE-5MIN` · atlas SA-02 |
| EQ T4 | `EQ-5MIN` · `EQ-SA02` · **`EQ02-M0M3-5MIN`** |
| AI / synth | `TRIPOD-SYNTH-5MIN` · `SYNTH-5MIN` |
| Primary SA-02 | `PB002-5MIN` |
| Cross-SA | `CROSS-SA-5MIN` · `ALERT-HAWTHORNE-5MIN` |
| VAS×EQ | **`VAS-EQ-5MIN`** · `VAS-5MIN` |
| LEAKAGE×EQ | **`LEAKAGE-EQ-5MIN`** · `LEAKAGE-5MIN` |

## Cấm

- VAS_D3 = early predictor / claim ES lâm sàng  
- Đổi eCRF 0–100 trừ amendment `[CẦN XÁC NHẬN]`  
- Báo M1 sandbox AUROC như bằng chứng BN  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4) · Protocol: `../../rituals/daily-protocol.md`  
- Harmonize: `VAS-SCALE-HARMONIZE-SA02-v0.1.md`
