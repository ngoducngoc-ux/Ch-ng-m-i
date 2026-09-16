# Micro-drill 5′ — EQ-SA02 M0→M3 (ladder · M1+VAS_D3 = leakage)

**Mã:** EQ02-M0M3-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4** · sau/trước `EQ-5MIN` · kèm `VAS-LEAK-5MIN` · trước claim AUROC M1/M3 SA-02  
**Goal:** ACTIVE · primary ΔVAS/VAS D3 không đổi · M1* = D1/CFU · M1+VAS_D3 = QC leakage · L3 CLOSED · PREP ≠ DONE  
**Spec:** `EQ-SA02-early-warning` · `VAS-SCALE-HARMONIZE-SA02`

## Một câu

> EQ02-M0M3 5′ = ladder M0 (VAS_D0+C) → M1* (D1/CFU) → M2/M3 (CFU+ADHERE) — **M1 sandbox + VAS_D3 = leakage QC**, không phải evidence; **không** đổi primary · **không** marker niêm mạc / L3.

## Drill (điền)

```text
Y_prim: VAS D3 / ΔVAS D0→D3 — xác nhận không đổi? CÓ
eCRF thang: 0–10 — xác nhận? CÓ | lệch: ________
M0 (1 dòng): ________
M1* early đúng: VAS_D1 | CFU_D0 | khác — ghi: ________
M1 sandbox + VAS_D3 = leakage? CÓ — vì: ________
M2/M3 thêm CFU/ADHERE (1 dòng): ________
Gộp Y với SA-01/05? KHÔNG
AUROC M1 sandbox = claim BN? KHÔNG
Marker niêm mạc / L3 hôm nay? CLOSED
Cặp đã đụng: EQ-5MIN | EQ-M0M3 | VAS-LEAK | VAS-5MIN | LEAKAGE | TRIPOD-SYNTH | PB002 — ghi: ________
1 việc nhỏ ≤30′ (EQ-SA02 Drill 10′ / VAS-LEAK / EH-SA02): ________
Đóng Goal / mở L3 vì EQ02-M0M3? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| EQ đầy đủ | `EQ-SA02` · Drill 10′ |
| EQ 5′ chung | `EQ-5MIN` |
| SA-01 sibling | `EQ-M0M3-5MIN` |
| SA-05 sibling | `EQ05-M0M3-5MIN` |
| VAS × leakage | `VAS-LEAK-5MIN` · `VAS-5MIN` · `LEAKAGE-5MIN` |
| AI / synth | `TRIPOD-SYNTH-5MIN` · `SYNTH-5MIN` |
| Primary SA-02 | `PB002-5MIN` |
| PB×EQ | **`PB007-EQ-5MIN`** · `PB007-5MIN` |

## Cấm

- Báo M1+VAS_D3 AUROC như early-signal lâm sàng  
- Đổi primary / thang 0–100 trừ amendment  
- Mở marker / L3 / G2 vì đã viết ladder  

## Liên kết

- EQ: `../equations/EQ-SA02-early-warning-v0.1.md` · Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4)  
- Protocol: `../../rituals/daily-protocol.md`
