# Bridge — Q3 L2 export → early-signal AI (SA-01)

**Mã:** Q3-L2-EXPORT-EARLY-SIGNAL-BRIDGE-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 91–105 · sau pass/fail Q2  
**Thẻ:** `Q3-L2-EXPORT-RITUAL-CARD` · Audit: `L2-MISSINGNESS-AUDIT` · Drill: `MISSINGNESS-5MIN` · Stack: `AI-LONGITUDINAL-STACK`  
**Cờ đầu:** SA-01 · L3 / G2 **CLOSED** mặc định · Goal **ACTIVE**  
**Không:** AUROC synthetic = lâm sàng · mở L3 vì demo xanh · PII trong export

## Vì sao Q3 L2 thuộc “phát hiện sớm–dọc–AI”

| Việc Q3 | Precure logic | Artifact |
|---------|---------------|----------|
| Export de-ID thật (hoặc `--demo` + “chưa N”) | Y tế số → analysis layer | `REDCAP-DEID` · Q2 staging bridge |
| QC + missingness theo visit | Dữ liệu dọc đủ cửa sổ \(t'\) | `L2-MISSINGNESS-AUDIT` · `MISSINGNESS-5MIN` · PIPELINE |
| M0–M3 exploratory | AI L2 trên \(Z\) trước omics | `EQ-SA01` · SAP ES · PB-009 |
| Leakage / TRIPOD | Báo cáo trung thực | `ML-OMICS-PITFALLS` · `TRIPOD-INTERNAL-CHECKLIST` |

Q2 = đường + protocol; Q3 = **chạy L2** (thật nếu có N; rehears nếu chưa) — multi-omics vẫn gated.

## Luồng một trang

```text
Q2 pass/fail ghi rõ
        ↓
Export de-ID (deny D1–D7)  hoặc  --demo + “chưa N”
        ↓
redcap_import_qc + missingness D0/D3/D7
        ↓
M0–M3 exploratory (không Dx claim)
        ↓
Leakage check · TRIPOD nội bộ · hold-out plan
        ↓
L3 X_mol? → chỉ sau G2 data thật (CLOSED)
```

## Ba cổng trước mọi số AUROC “early”

| Cổng | Câu hỏi | Mặc định |
|------|---------|----------|
| **N thật** | Export de-ID từ site? | Chưa → chỉ `--demo` + ghi rõ |
| **Leakage** | Predictor sau \(t^*\) / sau peek? | Cấm (pitfall #1) |
| **G2/L3** | Signal \(Z\) + ethics + lab? | **CLOSED** |

## Map ngày → bridge fill-in

| N | Ôn | 1 câu |
|---|-----|-------|
| 91–93 | Có N? · deny · QC | PASS verify ≠ evidence BN |
| 94–97 | Map cột · M0–M3 · missing % · window D3 | `[CẦN XÁC NHẬN DM]` nếu trống |
| 99–105 | Pitfall #1/#5 · SAP §7 · TRIPOD | Exploratory label bắt buộc |

## Ritual fill-in (91 / 96 / 102 — mẫu)

```text
Ngày: 91|96|102
N thật: CÓ / CHƯA (--demo only)
1 câu QC hoặc leakage:
L3/G2: CLOSED
```

## Sau Ngày 105

Q3 cross-SA / y tế số (`Q3-CROSS-SA-YTESO-RITUAL-CARD` 106–120) · `SCIENCE-BRIDGES-INDEX` #9 khi có bridge.

## Liên kết

- Thẻ: `Q3-L2-EXPORT-RITUAL-CARD-v0.1.md`  
- `Q2-STAGING-DEID-EARLY-SIGNAL-BRIDGE` · `Q2-CHECKPOINT-EARLY-SIGNAL-BRIDGE` · `PB-009`  
- `SCIENCE-BRIDGES-INDEX` #8
