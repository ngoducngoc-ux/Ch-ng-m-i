# Worksheet Z/X — EH-SA01 (từ đề cương SA-01 toàn văn)

**Nguồn đề cương:** Drive `03-09-26_CHIEU_50P_DE_CUONG_TOAN_VAN_SA-01.docx`  
**fileId:** `1uxs00YPiMbFwgkeVFu0aV8We4Ho07F5e`  
**Ngày lập:** 2026-09-16  
**Primary:** biểu mô hóa hoàn toàn 100% tại **D21** (ImageJ), N=120, PROBE

## A. Biến Z lâm sàng dọc — đã có trong schedule/synopsis

| # | Biến Z | Mốc thời gian trong đề cương | Vai trò early-signal | Ghi chú eCRF |
|---|--------|------------------------------|----------------------|--------------|
| 1 | Diện tích / % biểu mô (ImageJ) | D0, D1–D3, D5–D7, D14, **D21** | \(Z\) chính dự báo \(Y_{D21}\) | PRIMARY_OUT + chuỗi ảnh |
| 2 | Ảnh tổn thương chuẩn hóa | D0…D90 | feature lâm sàng / QA đo | SOP-SA-01-03 |
| 3 | Cấy vi sinh định lượng / tải lượng | D0, D1–D3; **sạch khuẩn D7** (secondary) | tín hiệu nhiễm sớm trước D21 | cần tên biến eCRF đầy đủ `[CẦN XÁC NHẬN]` |
| 4 | VAS đau rát khi thay băng | theo secondary (chuỗi thăm khám) | đáp ứng triệu chứng sớm | bổ sung dictionary |
| 5 | AE/SAE tại chỗ / toàn thân | mọi mốc | an toàn + confounder lành | AE_OCCUR |
| 6 | Tuân thủ thay băng 1–2 lần/ngày | D1–D21 (implied) | covariate \(C\) | chưa thấy biến riêng → **cần thêm** |
| 7 | Loại tổn thương (vết thương hở vs bỏng II–III), %TBSA | D0 | \(C\) / stratum | AGE/GENDER/GROUP có; loại tổn thương cần rõ trong eCRF |

**≥5 biến Z dùng ngay cho exploratory (không biospecimen):** (1)(2)(3)(4)(5).

## B. Biến X phân tử — “muốn có” (chưa có trong đề cương hiện tại)

| # | Biến X ứng viên | Thời điểm đề xuất | Feasibility | Rủi ro / cổng |
|---|-----------------|-------------------|-------------|----------------|
| 1 | Panel protein/cytokine dịch tiết hoặc swab | D0, D3, D7 | trung bình — cần SOP lấy + chuỗi lạnh | đạo đức bổ sung; chi phí |
| 2 | Marker viêm cục bộ (vd. IL-1/IL-6/CRP cục bộ nếu validated) | D0, D3, D7 | thấp–trung bình | tránh overclaim systemic |
| 3 | Đặc trưng biofilm/EPS proxy (nếu lab SA-03 hỗ trợ) | D0, D7 | liên kết SA-03 | ngoại suy in-vitro |

**Quyết định v0.1 (Precure-aligned, thực dụng):**  
Ưu tiên **exploratory trên \(Z\) dọc đã có** (ImageJ + vi sinh D0/D7 + VAS) trước khi mở \(X\) biospecimen.

## C. Phương trình áp vào biến thật

\[
Y_{D21}=\mathbb{1}\{\text{biểu mô hóa 100\% ImageJ}\}
\]
\[
\text{Candidate predictors: } Z_{\%}(D0,D3,D7),\; Z_{\text{culture}}(D0,D7),\; Z_{\text{VAS}}(D0..D7),\; C(\text{age, type, TBSA, group})
\]

H1 exploratory: mô hình mixed/GEE hoặc logistic với \(Z(D0{-}D7)\) cải thiện dự báo \(Y_{D21}\) so với chỉ \(Z(D0)\).

## D. Việc nhỏ tiếp

- [x] Bổ sung dictionary eCRF: `WOUND_TYPE`, `TBSA_PCT`, `AREA`/`PCT_EPITH` theo visit, `VAS_DRESS`, `CULTURE_CFU`, `ADHERENCE` → `eCRF-SA01-early-signal-dictionary-v0.1.md`
- [x] Nháp SAP exploratory M0–M3 → `../hypotheses/SAP-SA01-ES-v0.1-DRAFT.md`
- [x] Spec 1 trang nested biospecimen (gated) → `../hypotheses/SPEC-SA01-BIO-v0.1-DRAFT.md`
- [ ] Review với Data Manager REDCap (chờ)
- [x] Sandbox M0–M3 synthetic → `../analysis/sa01_early_signal_synthetic_m0_m3.py`

## Liên kết

`PB001-SCIENCE-CARD`
