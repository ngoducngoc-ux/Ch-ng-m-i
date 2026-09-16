# Micro-drill 5′ — VAS SA-02 early-signal (0–10 · D1 trước D3)

**Mã:** VAS-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4** · EQ-SA02 · bridge #2 · sau `LEAKAGE-5MIN`/`SYNTH-5MIN` · trước claim “đã có early-signal SA-02”  
**Goal:** ACTIVE · primary ΔVAS D3 không đổi · eCRF **0–10** · L3 CLOSED · PREP ≠ DONE  
**DOI:** [10.1186/1745-6215-15-263](https://doi.org/10.1186/1745-6215-15-263) (STPIS — chỉ so sánh literature)

## Một câu

> Giữ VAS **0–10**; early-signal nhìn **D1/CFU trước D3** — **không** dùng VAS_D3 làm predictor “early”; không đổi eCRF sang 0–100 vì STPIS dùng mm.

## Drill (điền)

```text
eCRF thang đúng: 0–10 | 0–100 — chọn: ________
t* primary: ΔVAS D3 — ĐÚNG | SAI
t' early ưu tiên: D1 | CFU_D0 | VAS_D3 — chọn (không VAS_D3): ________
M1 sandbox có VAS_D3 → leakage? CÓ — vì: ________
Gộp Y với SA-01/05? KHÔNG — vì: ________
1 việc nhỏ ≤30′ (EQ / LEAKAGE / shift): ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Harmonize đầy đủ | `VAS-SCALE-HARMONIZE-SA02` |
| Leakage | `LEAKAGE-5MIN` · atlas SA-02 · **`VAS-LEAK-5MIN`** |
| VAS×EQ | **`VAS-EQ-5MIN`** · EQ ladders |
| Synth | `SYNTH-5MIN` |
| ALERT | `ALERT-5MIN` |
| Cặp SA-01/05 | `EPI-5MIN` · `PUSH-5MIN` |
| EQ 5′ | `EQ-5MIN-MICRO-DRILL` (T4) |

## Cấm

- Đổi eCRF sang 0–100 trừ amendment `[CẦN XÁC NHẬN]`  
- VAS_D3 = early predictor → claim ES  
- Marker niêm mạc / L3 vì đã ôn VAS  
- Gộp endpoint với SA-01/05  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4)  
- PB-002 5′: **`PB002-5MIN-MICRO-DRILL`** · EQ 5′: `EQ-5MIN-MICRO-DRILL`  
- CROSS-SA 5′: **`CROSS-SA-5MIN-MICRO-DRILL`**  
- Shift: `PRECURE-SHIFT-CROSS-SA-BANK` · Protocol: `../../rituals/daily-protocol.md`
