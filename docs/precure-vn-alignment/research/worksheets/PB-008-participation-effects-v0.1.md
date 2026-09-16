# PB-008 — Hiệu ứng tham gia nghiên cứu (longitudinal profiling)

**Mã:** PB-008-v0.1  
**Ngày:** 2026-09-16  
**Nguồn curriculum:** Ngày 03 · DOI [10.1038/s41591-019-0414-6](https://doi.org/10.1038/s41591-019-0414-6)  
**Gắn:** SA-01 · SA-02 · SPIRIT/CONSORT covariates

## Vấn đề

Profiling lặp + phản hồi kết quả có thể làm đổi **adherence chăm sóc vết thương / VAS / lifestyle** — tách khỏi hiệu quả sản phẩm và khỏi tín hiệu omics sớm.

## Câu hỏi Smart A

1. Trường eCRF nào đủ để ghi **thay đổi hành vi do nghiên cứu** (không nhầm với AE sản phẩm)?  
2. Khi so sánh \(Z(t)\) dọc, có cần covariate “intensity follow-up” (số visit thực tế / đi muộn)?  
3. Alert nội bộ (A1–A4) có kích hoạt hành vi chăm sóc tốt hơn → làm lệch exploratory ES?

## Đại lượng ứng viên (nháp)

| Biến | Ý nghĩa | Ghi chú |
|------|---------|---------|
| `VISIT_COMPLIANCE` | % visit trong window | REDCap v0.2 — xác nhận DM |
| `DRESSING_ADH` | adherence thay băng (Likert) | đã có trong EH-SA01 nháp |
| `STUDY_BEHAV_CHANGE` | BN tự báo đổi chăm sóc vì biết đang tham gia TN | **thiếu** — đề xuất 1 câu SPIRIT optional |

## Việc nhỏ

- [ ] PI: quyết định có thêm 1 câu self-report cuối tuần 1 không (ICF nested)  
- [ ] SAP ES: ghi sensitivity “exclude visits with documented behavior change” — exploratory only  
- [ ] Weekly 20/09: nêu PB-008 khi chốt cờ SA-01  

## Không làm

- Không claim “loại bỏ hoàn toàn Hawthorne” bằng thống kê một biến.  
- Không dùng participation effect để giải thích primary D21 trước khi có dữ liệu.

## Liên kết

- `reading-notes/2026-09-19-natmed-longitudinal-precision-health.md`  
- `hypotheses/DESIGN-SA01-minimal-longitudinal-v0.1.md`  
- `problem-bank.md` (PB-008)
