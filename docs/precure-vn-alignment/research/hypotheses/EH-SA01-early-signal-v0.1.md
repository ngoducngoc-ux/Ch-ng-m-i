# Early-signal hypothesis — SA-01 (cờ đầu)

**Mã:** EH-SA01-v0.1  
**Ngày:** 2026-09-16  
**Khung tham chiếu:** Precure (tín hiệu phân tử/lâm sàng sớm trước endpoint) — không phải partnership Mayo/Thermo  
**Ngôn ngữ:** khoa học trung tính; claim chưa có DOI peer-review riêng cho giả thuyết này → `[CẦN XÁC NHẬN]` khi đưa vào đề cương chính thức

## 1. Bối cảnh endpoint hiện có

- Primary (theo chương trình): **biểu mô hóa tại D21**, N≈120 (RCT vết thương/bỏng).
- Logic Precure: nhiều quá trình sinh học lệch quỹ đạo **trước** khi endpoint lâm sàng “chốt”.

## 2. Câu hỏi nghiên cứu (Precure-aligned)

> Trong cửa sổ **D0–D7**, tổ hợp nào của biến lâm sàng dọc ± tín hiệu phân tử/vi môi trường dự báo **thất bại biểu mô hóa tại D21** tốt hơn so với đánh giá lâm sàng đơn thời điểm (vd. chỉ diện tích/độ sâu tại D0 hoặc D7)?

## 3. Phương trình làm việc

\[
Y_{D21} \;=\; f\big(X_{\text{mol}}(t\in\{0,3,7\}),\; Z_{\text{clin}}(t\in\{0,3,7\}),\; C\big) + \varepsilon
\]

| Ký hiệu | Nghĩa | Ví dụ ứng viên |
|---------|--------|----------------|
| \(Y_{D21}\) | Primary: biểu mô hóa đạt/không (hoặc % diện tích biểu mô) tại D21 | theo CRF SA-01 |
| \(X_{\text{mol}}\) | Tín hiệu phân tử/vi môi trường sớm | protein dịch tiết; cytokine viêm cục bộ; (tùy feasibility) microbiome bề mặt |
| \(Z_{\text{clin}}\) | Lâm sàng dọc sớm | diện tích, độ sâu, xuất tiết, nhiễm trùng lâm sàng, đau |
| \(C\) | Covariates | tuổi, vị trí vết thương, bệnh nền, tuân thủ chăm sóc |
| \(t\) | Thời điểm lấy mẫu đề xuất | **D0, D3, D7** (trước D21) |

**Giả thuyết H1 (hướng):** mô hình có \(X_{\text{mol}}(D0{-}D7)\) cải thiện AUROC / Brier / calibration so với mô hình chỉ \(Z_{\text{clin}}(D0{-}D7)\) trong dự báo \(Y_{D21}\).  
**H0:** không cải thiện có ý nghĩa lâm sàng/thống kê sau hiệu chỉnh multiplicity.

## 4. Thiết kế lồng (nested) — không phá RCT chính

1. Giữ primary D21 như đề cương đã duyệt.
2. Thêm **exploratory / secondary** early-signal (ghi rõ trong SAP).
3. Sampling chỉ khi **đạo đức + logistics ICU/phòng khám** cho phép; không tăng rủi ro BN.
4. SA-04 / ISO 10993: nếu gắn vật liệu/device lấy mẫu → kiểm cổng an toàn trước.

## 5. Việc nhỏ tiếp theo (≤2 tuần)

- [x] Liệt kê ≥5 biến \(Z\) từ schedule/synopsis SA-01 → `worksheets/EH-SA01-ZX-variables.md`
- [x] Liệt kê 3 biến \(X\) “muốn có” + feasibility
- [x] Quyết định v0.1: exploratory \(Z\) dọc trước biospecimen
- [x] Bổ sung dictionary eCRF thiếu → `worksheets/eCRF-SA01-early-signal-dictionary-v0.1.md`
- [x] Nháp SAP exploratory → `hypotheses/SAP-SA01-ES-v0.1-DRAFT.md`
- [ ] Spec nested biospecimen 1 trang (sau khi có tín hiệu \(Z\))
- [ ] Review dictionary với Data Manager REDCap

## 6. Nguồn khung

- Thông cáo Precure: Mạng lưới Y tế Số Việt Nam — Vietnam Digital Health Network; Mayo Clinic / Thermo Fisher (tham chiếu mô hình)
- Longitudinal multi-omics (ví dụ học thiết kế dọc): DOI [10.1038/s41586-019-1236-x](https://doi.org/10.1038/s41586-019-1236-x); DOI [10.1038/s41591-019-0414-6](https://doi.org/10.1038/s41591-019-0414-6)
- SPIRIT (protocol items): DOI [10.7326/0003-4819-158-3-201302050-00583](https://doi.org/10.7326/0003-4819-158-3-201302050-00583)
