# Actionable alerts nội bộ — SA-01 (không phải thiết bị chẩn đoán)

**Mã:** ALERT-SA01-v0.1  
**Ngày:** 2026-09-16  
**Phạm vi:** tín hiệu nội bộ nghiên cứu / điều dưỡng nghiên cứu; **không** claim chẩn đoán/điều trị tự động.

## Ba tiêu chí (nháp)

| ID | Điều kiện (cửa sổ sớm) | Hành động đề xuất | Không làm |
|----|------------------------|-------------------|-----------|
| A1 | PCT_EPITH tăng \<5 điểm từ D0→D3 **và** CULTURE_CFU không giảm | Hội chẩn PI/site; xem lại adherence thay băng; cân nhắc cấy lại theo SOP | Không đổi nhánh ngẫu nhiên; không “AI tự chỉ định” |
| A2 | VAS_DRESS tăng ≥2 điểm so với visit trước kèm AE_LOCAL=1 | Đánh giá AE; báo cáo theo Ch.7 nếu đủ tiêu chí | Không dừng nghiên cứu trừ quy tắc DSMB |
| A3 | PCT_EPITH_D7 \< PCT_EPITH_D0 (lùi) | Review ảnh ImageJ (QA); ghi chú exploratory early-signal | Không công bố cá thể |

Ngưỡng số là **nháp** — chốt sau pilot/`[CẦN XÁC NHẬN]` với nhóm lâm sàng.
