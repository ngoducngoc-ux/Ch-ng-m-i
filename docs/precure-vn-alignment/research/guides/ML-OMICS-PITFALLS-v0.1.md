# ML / omics predictive — 5 pitfalls (Precure alignment)

**Mã:** ML-PITFALLS-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 20 · Không thay SAP primary

1. **Leakage thời gian** — dùng biến sau \(t^*\) hoặc outcome proxy để dự báo \(Y(t^*)\).  
2. **Leakage nhóm** — tune trên cùng tập đánh giá AUROC (cần nested CV / hold-out site).  
3. **Multiplicity** — quét hàng trăm protein không FDR → false discovery.  
4. **Batch / site** — omics và site confounded; cần batch correction hoặc stratify.  
5. **Synthetic → lâm sàng** — AUROC sandbox **không** báo cáo như evidence BN.

## Khung báo cáo

- TRIPOD: DOI [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594) (prediction model reporting)  
- Micro-drill 5′: **`PITFALLS-5MIN-MICRO-DRILL`** (T4/T5 · cả 5) · `TRIPOD-5MIN` · **`SYNTH-5MIN`** (#5) · **`LEAKAGE-5MIN`** (#1)  
- Exploratory Smart A: pre-spec M0–M3 trong SAP ES; mọi M4 + omics sau G2.

## Việc nhỏ

- [x] Pitfall ↔ kiểm trong repo (Ngày 20 prep):
  - **#5 Synthetic→lâm sàng:** `verify.sh` + sandbox — chỉ QC pipeline · **`SYNTH-5MIN-MICRO-DRILL`**.
  - **#1 Leakage thời gian:** SAP ES §7 · atlas `LEAKAGE-CROSS-SA-ATLAS` · **`LEAKAGE-5MIN-MICRO-DRILL`** (T4).
  - **#3 Multiplicity:** SAP ES FDR / hypothesis-generating; PEA panel hẹp worksheet.
  - **#2/#4:** cần data thật + site hold-out — `[CẦN XÁC NHẬN]` khi có omics.
