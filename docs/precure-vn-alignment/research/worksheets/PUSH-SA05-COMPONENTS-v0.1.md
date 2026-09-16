# PUSH components — SA-05 early-signal (N=80)

**Mã:** PUSH-SA05-COMPONENTS-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 08 · Stotts 2001 DOI 10.1093/gerona/56.12.m795  
**Primary đề cương:** ΔPUSH D14 (không đổi) · SAP ES exploratory.

## PUSH gồm gì (Stotts)

| Thành phần | Mô tả ngắn | Ghi chú ES |
|------------|------------|------------|
| **Length × width** | Diện tích ước lượng | Total PUSH thường dùng cho primary |
| **Exudate** | Mức xuất tiết (0–3) | Có thể **dẫn trước** total khi turn xoay trở kém |
| **Tissue type** | Loại mô (slough/granulation…) | Khó inter-rater — cần QA ảnh blinded |

## Gợi ý ưu tiên exploratory (log 24/09 — một dòng)

> Với **N=80**, SAP ES mô tả **total PUSH** cho M0–M3; **sensitivity** riêng **exudate + turn adherence** (`TURN_ADHERE`) vì confounder ICU — không mở thêm component làm co-primary.

## Liên hệ phương trình

- `equations/EQ-SA05-early-warning-v0.1.md` — M3 dùng PUSH D3/D7 + \(C_{\text{turn}}\).  
- Alerts **B1–B3** (`ALERT-SA05-v0.1.md`): pilot ngưỡng trên total + adherence.

## Việc nhỏ

- [ ] Rater training: inter-rater ICC trên subset ảnh trước khi claim AI trên PUSH  
- [ ] Không dùng synthetic SA-05 để chốt ngưỡng B1–B3 lâm sàng

## Liên kết

- `reading-notes/2026-09-24-push-stotts-2001.md`  
- `hypotheses/SAP-SA05-ES-v0.1-DRAFT.md`
