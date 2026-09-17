# Bridge — Q3 L2 export → early-signal AI (SA-01) · refresh v0.1b

**Mã:** Q3-L2-EXPORT-EARLY-SIGNAL-BRIDGE-v0.1  
**Ngày:** 2026-09-16 (refresh sau Q2-CHECKPOINT / EQ bank CLOSED)  
**Curriculum:** Ngày 91–105 · sau pass/fail Q2 · bridge **#8**  
**Thẻ:** `Q3-L2-EXPORT-RITUAL-CARD` · `L2-MISSINGNESS-AUDIT` · **`MISSINGNESS-EQ`** · **`LEAKAGE-EQ`** · **`TRIPOD-EQ`** · **`DEID-EQ`** · **`PB009-EQ`** · **`AI-STACK-EQ`**  
**Cờ đầu:** SA-01 · L3 / G2 **CLOSED** mặc định · Goal **ACTIVE** · EQ bank **CLOSED**  
**STREAK&lt;3?** Dừng · **`STREAK3-PACK`** · **`STREAK3-EQ`** · NOW · FILL-AID → tick **19/09** trước  
**Không:** AUROC synthetic = lâm sàng · mở L3 vì demo xanh · PII trong export · invent EQ mới

## Vì sao Q3 L2 thuộc “phát hiện sớm–dọc–AI”

| Việc Q3 | Precure logic | Artifact |
|---------|---------------|----------|
| Export de-ID thật (hoặc `--demo` + “chưa N”) | Y tế số → analysis layer | `REDCAP-DEID` · #5 staging · **`DEID-EQ`** |
| QC + missingness theo visit | Dữ liệu dọc đủ cửa sổ \(t'\) | `L2-MISSINGNESS-AUDIT` · **`MISSINGNESS-EQ`** · **`MISSINGNESS-5MIN`** |
| M0–M3 exploratory | AI L2 trên \(Z\) trước omics | `EQ-SA01` · SAP ES · PB-009 · **`PB009-EQ`** · **`AI-STACK-EQ`** |
| Leakage / TRIPOD | Báo cáo trung thực | pitfall #1 · **`LEAKAGE-EQ`** · **`TRIPOD-EQ`** |

Q2 = đường + protocol (#5–#7); Q3 = **chạy L2** (thật nếu có N; rehears nếu chưa) — multi-omics vẫn gated. Densify #8 ≠ DONE.

## Luồng một trang

```text
STREAK <3? → STREAK3-PACK / STREAK3-EQ · dừng #8
        ↓ STREAK ≥3
OPENER → 1×EQ sibling (MISSINGNESS-EQ / LEAKAGE-EQ / TRIPOD-EQ) → #8
Q2 pass/fail ghi rõ (#7)
        ↓
Export de-ID (deny D1–D7)  hoặc  --demo + “chưa N”
        ↓
redcap_import_qc + missingness D0/D3/D7
        ↓
M0–M3 exploratory (không Dx claim)
        ↓
Leakage check · TRIPOD nội bộ · hold-out plan
        ↓
L3 X_mol? → chỉ sau G2 data thật (CLOSED) · #9 cross-SA
Goal ACTIVE · PREP ≠ DONE
```

## Ba cổng trước mọi số AUROC “early”

| Cổng | Câu hỏi | Mặc định | EQ |
|------|---------|----------|-----|
| **N thật** | Export de-ID từ site? | Chưa → chỉ `--demo` + ghi rõ | **`DEID-EQ`** |
| **Leakage** | Predictor sau \(t^*\) / sau peek? | Cấm (pitfall #1) | **`LEAKAGE-EQ`** |
| **G2/L3** | Signal \(Z\) + ethics + lab? | **CLOSED** | **`G2-EQ`** · **`PB009-EQ`** |

## Map ngày → bridge fill-in

| N | Ôn | 1 câu |
|---|-----|-------|
| 91–93 | Có N? · deny · QC | PASS verify ≠ evidence BN |
| 94–97 | Map cột · M0–M3 · missing % · window D3 | `[CẦN XÁC NHẬN DM]` nếu trống |
| 99–105 | Pitfall #1/#5 · SAP §7 · TRIPOD | Exploratory label bắt buộc |

## Ritual fill-in (91 / 96 / 102 — mẫu)

```text
STREAK ≥3? ________ (nếu không → STREAK3 path)
Ngày: 91|96|102
EQ sibling kèm (1): ________
N thật: CÓ / CHƯA (--demo only)
1 câu QC hoặc leakage:
L3/G2: CLOSED · Goal: ACTIVE · densify ≠ DONE
```

## Cấm

- AUROC sandbox = claim lâm sàng  
- Mở L3 vì demo xanh / densify agent  
- PII trong export · đóng Goal · invent EQ mới (bank CLOSED)  

## Sau Ngày 105

Q3 cross-SA / y tế số · **`Q3-CROSS-SA-YTESO-EARLY-SIGNAL-BRIDGE`** · **#9**.  
`MONTHS-4-12-RITUAL-CARD` sau Ngày 120.

## Liên kết

`Q3-L2-EXPORT-RITUAL-CARD` · `L2-MISSINGNESS-AUDIT` · **`MISSINGNESS-EQ-SCIENCE-CARD`** · **`LEAKAGE-EQ-SCIENCE-CARD`** · **`TRIPOD-EQ-SCIENCE-CARD`** · **`DEID-EQ-SCIENCE-CARD`** · **`PB009-EQ-SCIENCE-CARD`** · **`AI-STACK-EQ-SCIENCE-CARD`** · **`AFTER-STREAK3-OPENER-1PAGE`** · **`BRIDGE-ROTATION`** · `#7` Q2-CHECKPOINT · `#5` Q2-STAGING-DEID · `#9` Q3-CROSS-SA-YTESO · `SCIENCE-BRIDGES-SCIENCE-CARD` · `SCIENCE-CARDS-INDEX` · `STREAK_TRACKER`
