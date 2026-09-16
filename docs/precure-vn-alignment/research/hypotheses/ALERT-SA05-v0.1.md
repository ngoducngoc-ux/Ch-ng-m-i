# Actionable alerts nội bộ — SA-05 (ICU / PUSH)

**Mã:** ALERT-SA05-v0.1  
**Ngày:** 2026-09-16  
**Phạm vi:** nghiên cứu / điều dưỡng ICU; **không** thiết bị chẩn đoán tự động.

## Ba tiêu chí (nháp)

| ID | Điều kiện (cửa sổ sớm) | Hành động đề xuất | Không làm |
|----|------------------------|-------------------|-----------|
| B1 | PUSH tăng ≥1 điểm từ D0→D3 **hoặc** D3→D7 | Review xoay trở/adherence; hội chẩn điều dưỡng trưởng | Không đổi nhánh ngẫu nhiên |
| B2 | CULTURE_CFU không giảm D0→D3 kèm PUSH ≥ D0 | Ghi nhận exploratory early-signal; cân nhắc cấy lại theo SOP | Không tự chỉ định KS ngoài protocol |
| B3 | TURN_ADHERE = 0 (kém) tại 2 visit liên tiếp | Nhắc protocol chăm sóc; ghi confounder cho SAP | Không công bố cá thể |

Ngưỡng **nháp** — chốt sau pilot / `[CẦN XÁC NHẬN]` với nhóm ICU.

## Liên kết

- `EH-SA05-early-signal-v0.1.md` · sandbox `../analysis/sa05_early_signal_synthetic_m0_m3.py`
