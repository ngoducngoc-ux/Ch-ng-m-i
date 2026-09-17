# Early-signal hypothesis — SA-02 (nhánh TMH / VAS)

**Mã:** EH-SA02-v0.1  
**Ngày:** 2026-09-16  
**Primary (synopsis):** ΔVAS đau rát họng **D3 − D0**, N=100  
**Khung:** Precure-aligned exploratory — **không** thay primary VAS D3  
**Ngôn ngữ:** khoa học trung tính; `[CẦN XÁC NHẬN]` khi đưa vào đề cương chính thức

## 1. Câu hỏi nghiên cứu

> Trong cửa sổ **D0–D3** (và D1 nếu thu thêm), tổ hợp **CFU niêm mạc họng** và/hoặc dấu hiệu lâm sàng sớm có **dẫn trước** ΔVAS_D3 tốt hơn so với chỉ VAS tại D0 — hay triệu chứng và vi sinh **đồng phát**?

## 2. Phương trình làm việc

\[
\Delta VAS_{D3} = VAS_{D3} - VAS_{D0}
\]

Exploratory binary (ví dụ): \(Y_{\text{respond}} = \mathbb{1}\{\Delta VAS_{D3} \le -2\}\) — **chỉ secondary**, không thay primary.

\[
Y_{\text{respond}} = f\big(X_{\text{CFU/micro}}(t\in\{0,1,3\}),\; Z_{\text{clin}}(t\in\{0,1,3\}),\; C\big) + \varepsilon
\]

| Ký hiệu | Nghĩa | Ứng viên |
|---------|--------|----------|
| \(X\) | Vi sinh / marker niêm mạc | CFU họng D0, D1, D3 |
| \(Z\) | Lâm sàng | VAS; chẩn đoán phân loại D0; sạch giả mạc D5 (muộn hơn) |
| \(C\) | Covariates | adherence súc/xịt; nhóm điều trị |
| \(t\) | Mốc đề xuất | **D0, D1 (optional), D3** |

**H1 (hướng):** mô hình có \(X(D0{-}D1)\) cải thiện dự báo \(Y_{\text{respond}}\) hoặc \(\Delta VAS_{D3}\) so với chỉ \(Z(D0)\).  
**H0:** không cải thiện sau hiệu chỉnh multiplicity.

## 3. Thiết kế lồng

1. Giữ primary ΔVAS D3 như đề cương.  
2. Early-signal = **exploratory**; không dùng để đổi liều/KS ngoài protocol.  
3. Quyết định **D1 visit** = trade-off tải BN vs cửa sổ “trước D3” (Zhou: cần chuỗi thời gian).  
4. Cờ đầu dự án vẫn **SA-01**; SA-02 song song TMH.

## 4. Việc nhỏ tiếp theo

- [x] Worksheet Z → `worksheets/EH-SA02-ZX-variables.md`  
- [ ] Quyết định D1 VAS/CFU với PI TMH  
- [x] Nháp eCRF early-signal SA-02 → `worksheets/eCRF-SA02-early-signal-dictionary-v0.1.md` + CSV  
- [x] Sandbox synthetic M0–M3 → `../analysis/sa02_early_signal_synthetic_m0_m3.py`  
- [x] SAP ES nháp → `SAP-SA02-ES-v0.1-DRAFT.md` · alerts → `ALERT-SA02-v0.1.md`

## 5. Nguồn khung

- Zhou et al., *Nature* 2019 — DOI [10.1038/s41586-019-1236-x](https://doi.org/10.1038/s41586-019-1236-x)  
- Worksheet: `worksheets/EH-SA02-ZX-variables.md`
