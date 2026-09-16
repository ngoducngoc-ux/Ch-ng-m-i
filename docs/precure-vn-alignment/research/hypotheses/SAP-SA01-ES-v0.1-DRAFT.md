# SAP exploratory — Early-signal SA-01 (nháp)

**Mã:** SAP-SA01-ES-v0.1-DRAFT  
**Ngày:** 2026-09-16  
**Phạm vi:** phân tích thăm dò; **không** thay primary endpoint D21 đã duyệt.  
**Căn cứ khung:** đề cương SA-01 Ch.5 (mixed models/GEE, MICE); SPIRIT DOI [10.7326/0003-4819-158-3-201302050-00583](https://doi.org/10.7326/0003-4819-158-3-201302050-00583)

## 1. Mục tiêu exploratory

Đánh giá liệu chuỗi lâm sàng D0–D7 (ImageJ %, cấy định lượng, VAS) có cải thiện dự báo biểu mô hóa hoàn toàn tại D21 so với thông tin chỉ tại D0.

## 2. Quần thể

- ITT cho primary (không đổi).  
- Exploratory: đối tượng có ≥1 đo PCT_EPITH tại D0 và outcome D21; phân tích đầy đủ case + sensitivity MICE.

## 3. Outcome exploratory

- \(Y\): PRIMARY_OUT tại D21 (binary 100% biểu mô hóa).  
- Secondary descriptive: thời gian đến biểu mô hóa (nếu có ngày chính xác).

## 4. Predictors (pre-specified)

Xem `eCRF-SA01-early-signal-dictionary-v0.1.md` + CSV **v0.2** (`clin_event`) — mô hình M0–M3; sensitivity có CLIN_EVENT.

## 5. Phương pháp

1. Logistic regression (robust SE) hoặc GEE nếu dùng format dài.  
2. So sánh discrimination: AUROC (DeLong) M0 vs M1/M2/M3.  
3. Calibration: slope/intercept; Brier score.  
4. Không dùng \(X_{\text{mol}}\) trong v0.1 (chưa có mẫu).  
5. Multiplicity: exploratory — báo cáo FDR hoặc nhấn mạnh “hypothesis-generating”.

## 6. Missing data

Theo đề cương: MICE; báo cáo pattern missing theo visit.

## 7. Blind / leakage

- Người đánh giá ImageJ vẫn mù nhóm (PROBE).  
- Không dùng biến sau D7 để dự báo D21 trong mô hình “early”.  
- GROUP có thể đưa như covariate điều trị (ước lượng tiên lượng dưới điều trị) — báo cáo cả model có/không GROUP.

### 7.1 Hiệu ứng tham gia nghiên cứu (PB-008)

**Nguồn khái niệm:** profiling lặp có thể đổi adherence/VAS (Nat Med 2019, DOI 10.1038/s41591-019-0414-6) — xem `worksheets/PB-008-participation-effects-v0.1.md`.

**Phân tích sensitivity (exploratory, pre-specified khi có trường):**

1. **Model chính ES:** predictors D0–D7 như mục 4.  
2. **+ Compliance:** thêm biến visit đúng hạn / `DRESSING_ADH` nếu DM chốt trong v0.2+.  
3. **Subset:** loại visit có `CLIN_EVENT` hoặc (khi có) `STUDY_BEHAV_CHANGE=1` — báo cáo ΔAUROC so với model chính, không coi là primary.  
4. **Diễn giải:** cải thiện dự báo do \(Z\) dọc **không** được diễn giải đơn thuần là “tín hiệu phân tử Precure” trước khi có \(X_{\text{mol}}\) sau cổng G1–G2.

## 8. Báo cáo

Bảng 1 baseline; bảng AUROC; hình calibration; hạn chế N=120 và exploratory.

## 9. Việc nhỏ

- [x] Sandbox code synthetic M0–M3 (đã chạy; không phải bằng chứng lâm sàng)
- [ ] Chốt visit mapping D1–D3 / D5–D7 → D3/D7 với Data Manager
- [ ] Đưa nháp này vào SAP chính thức khi amendment
- [x] Ghi sensitivity PB-008 (mục 7.1) — 2026-09-16
