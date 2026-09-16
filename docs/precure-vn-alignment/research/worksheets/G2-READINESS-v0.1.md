# G2 readiness — tóm tắt điều kiện mở omics SA-01

**Mã:** G2-READINESS-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 07 · Wik MCP 2021 (PEA+NGS scale)  
**Nguồn đầy đủ:** `hypotheses/SPEC-SA01-BIO-v0.1-DRAFT.md`

## Ba điều kiện G2 (ghi vào log 23/09)

1. **Signal trên \(Z\):** exploratory SAP-SA01-ES — ít nhất một trong: ΔAUROC M1/M2 vs M0 đạt ngưỡng pre-specified **hoặc** quyết định DSMB/PI từ interim descriptive (chưa có data → **G2 chưa đạt**).  
2. **Ethics G1:** ICF/amendment cho phép lưu & phân tích mẫu — `[CẦN XÁC NHẬN]` HĐĐĐ trước lấy mẫu.  
3. **Logistics G3 (+ G5 nếu device mới):** SOP pre-analytic + chuỗi lạnh + lab/LIMS — tách layer khỏi REDCap (y tế số).

## Ba điều kiện **không** mở omics (nhắc lại)

- Chưa DM review REDCap v0.2 \(Z\)  
- Chưa pass G2 trên data thật  
- Synthetic AUROC **không** dùng để pass G2

## Y tế số — hai layer (từ Wik / PB-004)

| Layer | Vai trò | Smart A hiện tại |
|-------|---------|------------------|
| **Clinical** | REDCap visit, \(Z\), alerts | SA-01 v0.2 staging |
| **Omics** | LIMS, batch QC, de-ID analysis DB | **Chưa triển khai** — sau G2 |

## Việc nhỏ

- [ ] Map workflow visit → export → sandbox (`REDCap-to-M0-M3-PIPELINE-v0.1.md`) trước khi thiết kế LIMS  
- [ ] Curriculum Ngày 07: tick 3 điều kiện G2 trong daily log

## Liên kết

- `reading-notes/2026-09-23-wik-mcp-pea-ngs.md`  
- `y-te-so-precure-bridge-v0.1.md` §2  
- `PEA-L1L2L3-DECISION-CARD-v0.1.md` (Ngày 05–07 gộp)  
- Bridge Tier 3: `TIER3-INTERIM-G2-BRIDGE-v0.1.md` · `INTERIM-DESCRIPTIVE-MOCK` · `OMICS-IF-G2`
