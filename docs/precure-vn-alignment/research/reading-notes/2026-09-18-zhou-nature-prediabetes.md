# Reading notes — Curriculum Ngày 02 (chuẩn bị)

**Paper:** Zhou et al., Longitudinal multi-omics of host–microbe dynamics in prediabetes, *Nature* 2019  
**DOI:** [10.1038/s41586-019-1236-x](https://doi.org/10.1038/s41586-019-1236-x)  
**PMID:** [31142858](https://pubmed.ncbi.nlm.nih.gov/31142858/)

## Điểm rút cho Precure / Smart A (đọc abstract + khung; chưa thay thế đọc full)

1. Cohort ~106, theo dõi ~4 năm: transcriptome, metabolome, cytokine, proteome, microbiome.
2. Hồ sơ “khỏe” khác nhau giữa cá thể; có biến thiên trong và giữa người.
3. Thay đổi mạnh khi nhiễm virus hô hấp / tiêm chủng — tín hiệu sớm gắn **bối cảnh lâm sàng**, không chỉ baseline tĩnh.
4. Có ví dụ chữ ký phân tử cá nhân (IL-1RA, hs-CRP…) **trước** khởi phát T2D ở một cá thể — minh họa logic “trước triệu chứng/chẩn đoán”.
5. Bài học Smart A: cần **chuỗi thời gian + sự kiện lâm sàng** (không chỉ một snapshot), và phân tầng (vd. kháng insulin) trước khi train AI.

## Map sang SA-01 (cờ đầu) — không ngoại suy cohort

| Zhou | SA-01 analog | Artifact |
|------|--------------|----------|
| Host–microbe + multi-omics dài hạn | \(Z\) dọc trước; \(X\) sau G2 | DESIGN-SA01 · SPEC-BIO |
| Sự kiện nhiễm / tiêm | `clin_event` / AE / nhiễm cục bộ | eCRF v0.2 |
| Chữ ký trước chẩn đoán T2D (minh họa) | Exploratory M0–M3 → \(Y_{D21}\) | EQ-SA01 · SAP ES |
| Khác biệt “khỏe” giữa người | Covariates + stratum SAP | C_baseline |

**Ranh giới:** cohort Precure/Zhou ≠ RCT vết thương N=120; không claim cùng effect size hay Dx sản phẩm.

## Câu hỏi gắn SA khi đọc sáng 18/09

- SA-02: marker viêm có dẫn trước ΔVAS không? → `EQ-SA02-early-warning-v0.1.md`
- SA-01/05: “sự kiện” tương đương infection/immunization trong vết thương là gì (nhiễm trùng cục bộ, thay băng, phẫu thuật)?
- PB-009: L1+L2 đủ chưa trước khi mở L3?

## Việc nhỏ đề xuất cho log 18/09

- [x] DESIGN dọc tối thiểu → `../hypotheses/DESIGN-SA01-minimal-longitudinal-v0.1.md` (repo)
- [ ] PI: xác nhận insight Zhou + STREAK DONE (cột còn “DONE prep”)
- [ ] Study sheet: `../study-sheets/STUDY-SHEET-ZHOU-LONGITUDINAL-v0.1.md`
- [ ] Đối chiếu `LONGITUDINAL-EARLY-SIGNAL-SA01-v0.1.md` + `AI-LONGITUDINAL-STACK-v0.1.md`
