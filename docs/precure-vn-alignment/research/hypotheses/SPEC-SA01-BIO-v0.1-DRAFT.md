# Nested biospecimen — SA-01 early-signal (gated)

**Mã:** SPEC-SA01-BIO-v0.1-DRAFT  
**Ngày:** 2026-09-16  
**Nguyên tắc:** chỉ mở sau khi exploratory \(Z\) (SAP-SA01-ES) cho tín hiệu; không tăng rủi ro BN; không thay primary D21.

## 1. Cổng mở (gates) — phải đủ trước khi lấy mẫu

| # | Gate | Tiêu chí |
|---|------|----------|
| G1 | Ethics | ICF/amendment cho phép lưu & phân tích mẫu; `[CẦN XÁC NHẬN]` HĐĐĐ |
| G2 | Signal Z | Ít nhất một trong: ΔAUROC M1/M2 vs M0 ≥ ngưỡng pre-specified **hoặc** quyết định DSMB/PI dựa trên interim descriptive |
| G3 | Logistics | SOP lấy mẫu + chuỗi lạnh + lab partner sẵn |
| G4 | Safety | Không lấy mẫu nếu AE tại chỗ nặng / nhiễm nặng cần ưu tiên điều trị |
| G5 | SA-04 | Nếu dụng cụ lấy mẫu là device mới → cổng ISO 10993 liên quan |

**Mặc định hiện tại:** G2 chưa đạt (chưa có data) → **không lấy mẫu thật**.

## 2. Loại mẫu (ứng viên)

| Mẫu | Mục đích \(X\) | Visit đề xuất | Ghi chú |
|-----|----------------|---------------|---------|
| Swab bề mặt / dịch tiết | protein/cytokine panel | D0, D3, D7 | ưu tiên ít xâm lấn · pre-analytic: `worksheets/PRE-ANALYTIC-PEA-SA01-v0.1.md` |
| Cấy định lượng (đã có hướng) | vi sinh | D0, D7 | đã trong schedule |
| Không máu toàn thân ở v0.1 | — | — | giảm gánh cho BN |

## 3. Luồng

```text
Consent nested? --no--> stop
        |
       yes
        v
Exploratory Z (M0–M3) --> G2 fail --> chỉ lưu bank nếu đã lấy vì lý do khác / không lấy mới
        |
      G2 pass
        v
Collect swab D0/D3/D7 --> chain-of-custody --> assay batch --> link StudyID+VISIT
        v
Model M4 = M3 + X_mol (exploratory; multiplicity)
```

## 4. Liên kết dữ liệu

Theo `PB-004-data-architecture.md`: Specimen ↔ Visit ↔ StudyID; analysis DB khử định danh.

## 5. Việc nhỏ

- [ ] Chốt ngưỡng G2 (vd. ΔAUROC ≥ 0.05 với CI) trước interim  
- [ ] Draft ICF clause nested (1 đoạn)  
- [ ] Không triển khai lab cho đến G1+G2
