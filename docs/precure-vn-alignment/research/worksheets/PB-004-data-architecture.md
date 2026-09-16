# PB-004 — Kiến trúc tối thiểu mẫu ↔ lâm sàng dọc (VN)

**Ngày:** 2026-09-16  
**Tham chiếu tinh thần Precure:** liên kết omics/mẫu với lâm sàng theo thời gian, khử định danh, chuẩn hóa — **quy mô đề tài**, không 1 triệu mẫu.

## Sơ đồ entities

```text
[Participant] --1:1-- [StudyID (SA-xx-NNN)]
      |
      +-- consent (ICF version, date)
      |
      +--* [Visit] (visit_code, timestamp, site)
             |
             +--* [ClinicalObs]  eCRF REDCap (Z, AE, adherence)
             |
             +--* [Media]        ảnh chuẩn hóa / ImageJ measures
             |
             +--0..* [Specimen]  (type, collected_at, chain-of-custody)
                    |
                    +--0..* [AssayResult] (X_mol; lab batch_id)
```

## Ranh giới đạo đức / PII

| Lớp | Nội dung | Ai thấy |
|-----|----------|---------|
| Identified | Họ tên, hồ sơ bệnh án viện | site only |
| StudyID | SA-01-XXX | nghiên cứu |
| Analysis | StudyID + visit + biến Z/X đã khử định danh | thống kê / AI |
| Public | aggregate only | công bố |

**Cấm:** đưa PII vào repo git / memory agent / Drive public.

## Tối thiểu triển khai Smart A

1. REDCap + audit trail (đã nêu SA-01 Ch.6)  
2. Visit calendar khớp schedule (D0, D1–3, D5–7, D14, D21…)  
3. Bảng Specimen chỉ khi nested được duyệt  
4. Export analysis DB: không tên, không địa chỉ, không SĐT  

## Việc nhỏ

- [ ] Vẽ lại sơ đồ này vào 1 slide nội bộ (không public)
- [ ] Checklist consent: có/không cho phép lưu mẫu & tái phân tích omics
