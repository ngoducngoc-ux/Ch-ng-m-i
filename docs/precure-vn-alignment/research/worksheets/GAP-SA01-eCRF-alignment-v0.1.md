# Gap analysis — SA-01 eCRF v0.2 vs alignment / đề cương

**Ngày:** 2026-09-16  
**CSV:** `redcap_sa01_early_signal_dictionary_v0.2.csv`  
**Mục đích:** biết còn thiếu gì trước staging REDCap (không phải audit chính thức).

| Nhu cầu alignment / EH-SA01 | Trong CSV v0.2? | Ghi chú |
|-----------------------------|-----------------|---------|
| % biểu mô ImageJ dọc D0/D3/D7 | ✓ `pct_epith` + visit | map visit_code |
| CFU D0/D7 | ✓ `culture_*` | D3 cấy tùy site |
| VAS thay băng | ✓ `vas_dress` | |
| Adherence thay băng | ✓ `adherence` | |
| AE tại chỗ | ✓ `ae_local` | |
| Sự kiện lâm sàng (Zhou) | ✓ `clin_event` | v0.2 |
| Loại tổn thương / TBSA | ✓ `wound_type`, `tbsa_pct` | |
| Ảnh QA `PHOTO_ID` | ✓ `photo_id` | |
| Primary D21 | ✓ `primary_out` | form riêng |
| Braden / %TBSA toàn thân ngoài bỏng | — | không thuộc SA-01 synopsis |
| \(X_{\text{mol}}\) omics | — | **đúng** — sau G2 BIO |
| Biến `AREA` cm² vs chỉ % | △ `area_open_cm2` | đủ cho exploratory |

## Kết luận v0.2

**Đủ cho SAP ES M0–M3 trên \(Z\)** pending DM review visit bắt buộc và tuổi 18–70.

## Việc nhỏ

- [ ] DM xác nhận repeating instrument  
- [x] Gap scan v0.2 → `GAP-SA01-eCRF-alignment-v0.1.md`
