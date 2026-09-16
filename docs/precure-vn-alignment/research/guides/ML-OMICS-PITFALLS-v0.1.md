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
- Exploratory Smart A: pre-spec M0–M3 trong SAP ES; mọi M4 + omics sau G2.

## Việc nhỏ

- [ ] Ghi trong log Ngày 20: pitfall nào đã kiểm trong `verify.sh`/QC
