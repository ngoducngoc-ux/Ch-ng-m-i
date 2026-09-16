# Micro-drill 5′ — VAS × LEAK × EQ (0–10 · ladder Z · ≠ VAS_D3 early)

**Mã:** VAS-LEAK-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4** · sau `VAS-LEAK-5MIN` / `VAS-EQ-5MIN` / `LEAKAGE-EQ-5MIN` · trước claim “ES SA-02”  
**Goal:** ACTIVE · primary ΔVAS D3 không đổi · eCRF **0–10** · M1+VAS_D3 = leakage · ladder chỉ feature hợp lệ · L3 CLOSED · PREP ≠ DONE  
**DOI:** TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594)

## Một câu

> VAS-LEAK×EQ 5′ = thang 0–10 + 1 feature leakage + 1 feature hợp lệ **và** 1 dòng ladder M0–M3 chỉ trên feature hợp lệ — VAS_D3 trong M early = QC leakage ≠ evidence.

## Drill (điền)

```text
eCRF thang: 0–10 | 0–100 — chọn: ________ (đúng = 0–10)
EQ sibling: EQ02-M0M3 | EQ-M0M3 — chọn: ________ (thường EQ02)
t* = ΔVAS D3 — xác nhận? CÓ
1 feature LEAKAGE nếu vào M early: ________ (thường VAS_D3)
1 feature HỢP LỆ cho t': ________
1 dòng Z / M0→M3 (chỉ feature hợp lệ): ________
Gộp Y SA-01/05 / AUROC SYN = BN? KHÔNG
Cặp đã đụng: VAS-LEAK | VAS-EQ | LEAKAGE-EQ | EQ02-M0M3 | PB002-EQ | PITFALLS-EQ — ghi: ________
1 việc nhỏ ≤30′ (harmonize / EQ Drill 10′ / atlas 1 hàng): ________
Đóng Goal / mở L3 vì VAS-LEAK×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Thẻ khoa học | **`VAS-LEAK-EQ-SCIENCE-CARD`** · `VAS-LEAK-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` |
| VAS×LEAK alone | `VAS-LEAK-5MIN` · `VAS-5MIN` · `LEAKAGE-5MIN` |
| VAS×EQ / LEAK×EQ | `VAS-EQ-5MIN` · `LEAKAGE-EQ-5MIN` |
| LEAK-CROSS×EQ | **`LEAK-CROSS-EQ-5MIN`** · `LEAK-CROSS-5MIN` |
| EQ T4 | `EQ02-M0M3-5MIN` · `EQ-5MIN` |
| PB002 / pitfalls | `PB002-EQ-5MIN` · `PITFALLS-EQ-5MIN` |

## Cấm

- VAS_D3 làm early feature · gộp Y · đổi 0–100 vì STPIS mm  
- Báo M1 sandbox AUROC như ES lâm sàng  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4) · Protocol: `../../rituals/daily-protocol.md`  
- Harmonize: `VAS-SCALE-HARMONIZE-SA02`
