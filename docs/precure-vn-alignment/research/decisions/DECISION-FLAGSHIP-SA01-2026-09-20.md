# Quyết định cờ đầu — SA-01 (weekly 2026-09-20)

**Mã:** DECISION-FLAGSHIP-2026-09-20  
**Ngày quyết định:** 2026-09-20 (CN weekly — mặc định agent pre-fill; PI xác nhận `[CẦN XÁC NHẬN]`)  
**Trạng thái:** **PROPOSED — giữ SA-01**

## Quyết định

| Cờ đầu early-signal Precure alignment | SA-01 vết thương/bỏng |
|----------------------------------------|------------------------|
| SA-05 ICU | Đối chiếu song song (eCRF/SAP/alerts sẵn) |
| SA-02 TMH | Nhánh VAS; không thay cờ đầu |

## Lý do (khoa học + vận hành)

1. eCRF **v0.2** + DM handoff + DESIGN dọc D0/D3/D7 đầy đủ nhất.  
2. Sandbox + SAP ES + alerts A1–A4 + biospecimen **gated** đã khớp một pipeline.  
3. SA-05 phụ thuộc adherence ICU; SA-02 primary D3 ngắn — khó so sánh omics tương lai.

## Điều kiện đổi cờ đầu

- Site SA-01 không mở trong 90 ngày **và** ICU SA-05 staging REDCap sẵn → xem xét nâng SA-05.  
- Hoặc PI chốt bằng văn bản → cập nhật file này + `PROJECT_STATUS.md`.

## Việc sau quyết định

- [ ] PI tick xác nhận  
- [ ] Forward `DATA-MANAGER-REDCap-INDEX.md` (ưu tiên SA-01 v0.2) — dùng `DM-FORWARD-CHECKLIST-v0.1.md`
