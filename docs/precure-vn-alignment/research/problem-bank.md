# Problem bank — câu hỏi / “phương trình” nghiên cứu theo hướng Precure

Mỗi mục: **ID · Đề tài · Câu hỏi · Biến / đại lượng · Việc nhỏ tiếp theo · Trạng thái**.

> **Lens 1 trang (weekly):** `worksheets/PB-EARLY-SIGNAL-LENS-BRIDGE-v0.1.md` · `SCIENCE-BRIDGES-INDEX` #13  
> **Q2 Ngày 81–83:** dùng `worksheets/PB-CLOSE-DECISION-CARD-v0.1.md` trước khi CLOSED/PARKED — chỉ PI tick.

---

## PB-001 · SA-01 · Tín hiệu sớm lành vết thương

- **Câu hỏi:** Những đại lượng nào ở ngày 0–7 dự báo thất bại biểu mô hóa tại D21 tốt hơn chỉ số lâm sàng đơn thuần?
- **Đại lượng ứng viên:** diện tích/độ sâu; marker viêm cục bộ; protein dịch tiết; tuân thủ chăm sóc (covariate).
- **Phương trình:** `equations/EQ-SA01-early-warning-v0.1.md` (Ngày 10)
- **Việc nhỏ:** DM review eCRF v0.2; `redcap_import_qc.py --demo` trên export đầu tiên
- **Trạng thái:** OPEN · cờ đầu · hypothesis v0.1 đã viết 2026-09-16 (`hypotheses/EH-SA01-early-signal-v0.1.md`)

## PB-002 · SA-02 · Early biological response vs VAS

- **Câu hỏi:** ΔVAS D0→D3 có đồng bộ với thay đổi marker niêm mạc/hô hấp, hay triệu chứng trễ hơn tín hiệu sinh học?
- **Đại lượng ứng viên:** VAS; CRP/cytokine (nếu có); điểm khám họng; thời gian hết sốt.
- **Phương trình:** `equations/EQ-SA02-early-warning-v0.1.md`
- **Việc nhỏ:** 1 trang giả thuyết “early biological response” tách khỏi primary VAS.
- **Trạng thái:** OPEN · hypothesis v0.1 · SAP ES + eCRF CSV v0.1 · sandbox SA-02 · EQ-SA02

## PB-003 · SA-05 · Cảnh báo sớm trước PUSH xấu

- **Câu hỏi:** Có thể định nghĩa cửa sổ cảnh báo trước khi PUSH tăng hạng, dựa trên chuỗi điểm chăm sóc + tín hiệu mô/vi tuần hoàn?
- **Đại lượng ứng viên:** PUSH theo thời gian; Braden; giờ thay tư thế; ảnh/chuẩn hóa vết thương; (tương lai) proteomics dịch tiết.
- **Việc nhỏ:** phác thảo sampling schedule ICU khả thi (không tăng rủi ro BN).  
- **Phương trình:** `equations/EQ-SA05-early-warning-v0.1.md` (Ngày 09)
- **Trạng thái:** OPEN · EH-SA05 · eCRF/SAP ES · sandbox · alerts B1–B3

## PB-004 · Hạ tầng dữ liệu · Liên kết mẫu–lâm sàng VN

- **Câu hỏi:** Kiến trúc tối thiểu để liên kết mẫu–lâm sàng theo thời gian ở mức đề tài VN, học từ tinh thần Precure nhưng phù hợp quy mô/đạo đức địa phương?
- **Đại lượng ứng viên:** ID nghiên cứu; timestamp; loại mẫu; phiên bản CRF; audit trail.
- **Việc nhỏ:** 1 sơ đồ 1 trang (entities + consent boundaries).
- **Trạng thái:** OPEN · worksheet 2026-09-16 (`worksheets/PB-004-data-architecture.md`)

## PB-005 · SA-03 · Biofilm như proxy giai đoạn sớm

- **Câu hỏi:** Chỉ số nào của biofilm in-vitro (sinh khối, viability, matrix protein) map được sang “nguy cơ chuyển pha” trước biểu hiện nhiễm trùng lâm sàng — và giới hạn ngoại suy là gì?
- **Đại lượng ứng viên:** CFU/biomass; độ dày biofilm; marker protein matrix; thời gian tiếp xúc chế phẩm.
- **Việc nhỏ:** 1 bảng “in-vitro → lâm sàng” 5 dòng (cột: đại lượng / có thể đo ở người? / rủi ro overclaim).
- **Trạng thái:** OPEN · worksheet 2026-09-16 (`worksheets/EH-SA03-ZX-variables.md`)

## PB-006 · SA-04 · Cổng ISO trước omics người

- **Câu hỏi:** Những hạng mục ISO 10993 nào là cổng bắt buộc trước khi gắn omics/diagnostics vào sản phẩm chăm sóc vết thương?
- **Đại lượng ứng viên:** cytotoxicity; sensitization; irritation; (theo intended contact) systemic toxicity.
- **Việc nhỏ:** checklist 1 trang “cổng ISO trước omics người”.
- **Trạng thái:** OPEN · gates 2026-09-16 (`worksheets/EH-SA04-gates.md`)

## PB-007 · Khung phương trình · Precure shift

- **Câu hỏi:** Với endpoint lâm sàng \(Y(t^*)\), tồn tại cửa sổ \(t' \ll t^*\) sao cho \(X_{\text{phân tử}}(t')\) cải thiện dự báo so với chỉ \(Z_{\text{lâm sàng}}(t')\)?
- **Đại lượng ứng viên:** xem curriculum Ngày 23 template.
- **Việc nhỏ:** điền phương trình cho SA đang chọn làm cờ đầu (01 hoặc 05).
- **Trạng thái:** OPEN · 2026-09-16

## PB-008 · Longitudinal · Hiệu ứng tham gia nghiên cứu

- **Câu hỏi:** Profiling lặp + phản hồi có làm lệch \(Z\) dọc (adherence, VAS) tách khỏi hiệu quả sản phẩm và tín hiệu sớm?
- **Nguồn:** Nat Med 2019 DOI 10.1038/s41591-019-0414-6 (Curriculum Ngày 03).
- **Việc nhỏ:** worksheet `worksheets/PB-008-participation-effects-v0.1.md` · xem ICF/SAP sensitivity.
- **Trạng thái:** OPEN · 2026-09-16

## PB-009 · Y tế số / AI · Stack L1→L2 trước omics

- **Câu hỏi:** Kiến trúc tối thiểu nào (visit + `clin_event` + export de-ID + M0–M3 pre-spec) đủ để nói “AI trên dữ liệu dọc” mà **không** cần L3 multi-omics — và khi nào L3 thật sự thêm giá trị dự báo \(Y(t^*)\)?
- **Đại lượng ứng viên:** missingness theo visit; AUROC/Brier M0 vs M3 (nội bộ); calibration; site effect.
- **Việc nhỏ:** checklist L1/L2 — `worksheets/PB-009-AI-BEFORE-OMICS-v0.1.md` · stack `guides/AI-LONGITUDINAL-STACK-v0.1.md` khi có export thật đầu tiên.
- **Trạng thái:** OPEN · 2026-09-16 · gắn `y-te-so-precure-bridge-v0.1.md` · worksheet PB-009 DRAFT

---

## Cách thêm mục mới (copy)

```markdown
## PB-00X · SA-0Y · Tiêu đề ngắn
- **Câu hỏi:**
- **Đại lượng ứng viên:**
- **Việc nhỏ:**
- **Trạng thái:** OPEN · YYYY-MM-DD
```
