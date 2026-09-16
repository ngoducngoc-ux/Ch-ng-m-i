# Worksheet Z — EH-SA05 early-signal (từ đề cương SA-05)

**Nguồn:** Drive `03-09-26_CHIEU_50P_DE_CUONG_TOAN_VAN_SA-05.docx`  
**fileId:** `1kiXycmEPHAqndR5DEMyQpCQNCGTl2YEa`  
**Ngày:** 2026-09-16  
**Primary (synopsis):** Δ PUSH (0–17) **D14 − D0**, N=80, ICU, loét độ 2–4  
**Lưu ý:** bảng schedule ghi cột “D21 (Primary)” mang tính template — **ưu tiên synopsis: D14 là mốc chính PUSH**.

## Biến Z / C ứng viên

| # | Biến | Mốc | Vai trò early-signal |
|---|------|-----|----------------------|
| 1 | PUSH total (0–17) | D0, D1–3, D5–7, **D14**, D21 | \(Y\)=ΔPUSH_D14; chuỗi sớm D0–D7 dự báo |
| 2 | Thành phần PUSH (diện tích×, xuất tiết, loại mô) | cùng visit | decomposite tín hiệu |
| 3 | Ảnh chuẩn hóa (blinded rater) | mọi mốc | QA / diện tích phụ D21 |
| 4 | Cấy định lượng ổ loét | D0, D1–3 | nhiễm sớm |
| 5 | AE/SAE; nhiễm trùng huyết từ ổ loét | mọi mốc | an toàn + outcome phụ |
| 6 | Xoay trở mỗi 2h / đệm khí (adherence) | hàng ngày ICU | \(C\) — **cần biến eCRF** |
| 7 | NPUAP/EPUAP stage D0; ngày nằm ICU | D0 | \(C\) |

## Phương trình exploratory

\[
\Delta\mathrm{PUSH}_{D14} = f\big(\mathrm{PUSH}(D0,D3,D7),\; Z_{\text{culture}},\; C_{\text{ICU}}\big)+\varepsilon
\]

H1: thông tin D0–D7 cải thiện dự báo ΔPUSH_D14 (hoặc xấu đi PUSH) so với chỉ D0.

## Việc nhỏ

- [x] Bổ sung eCRF → `eCRF-SA05-early-signal-dictionary-v0.1.md` + CSV  
- [x] Sandbox synthetic SA-05 M0–M3  
- [x] SAP ES nháp → `../hypotheses/SAP-SA05-ES-v0.1-DRAFT.md`
- [ ] Giữ SA-01 là cờ đầu; SA-05 = đối chiếu ICU
