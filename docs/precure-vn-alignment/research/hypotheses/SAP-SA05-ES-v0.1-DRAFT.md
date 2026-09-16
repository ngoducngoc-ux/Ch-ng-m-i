# SAP exploratory — Early-signal SA-05 (nháp)

**Mã:** SAP-SA05-ES-v0.1-DRAFT  
**Ngày:** 2026-09-16  
**Phạm vi:** thăm dò ICU; **không** thay primary ΔPUSH D14.

## 1. Mục tiêu

Chuỗi PUSH + adherence xoay trở + cấy D0–D7 có cải thiện dự báo **IMPROVED_D14** (ΔPUSH≤−2) so với chỉ PUSH D0?

## 2. Outcome exploratory

- \(Y\): IMPROVED_D14 (binary).  
- Descriptive: ΔPUSH liên tục.

## 3. Predictors

`eCRF-SA05-early-signal-dictionary-v0.1.md` — M0–M3; sandbox synthetic đã chạy.

## 4. Phương pháp

Logistic + AUROC/Brier; covariates STAGE_NPUAP, AGE, GROUP; exploratory FDR.

## 5. ICU đặc thù

Ghi nhận **TURN_ADHERE** là confounder bắt buộc; không dùng alert B1–B3 làm endpoint.

## 6. Việc nhỏ

- [x] Sandbox M0–M3  
- [ ] Review eCRF với điều dưỡng trưởng ICU  
- [ ] Amendment khi staging REDCap ICU  
- [x] Gap EQ↔SAP — `../worksheets/EQ-EH-SA05-GAP-v0.1.md` (Ngày 09)

## Liên kết

- `ALERT-SA05-v0.1.md` · DOI Stotts 2001 PUSH
