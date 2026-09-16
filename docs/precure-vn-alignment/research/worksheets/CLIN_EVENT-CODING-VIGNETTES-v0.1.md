# `clin_event` coding — vignette luyện (synthetic / giáo dục)

**Mã:** CLIN_EVENT-CODING-VIGNETTES-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 02 · 28 · 31 · anytime ôn Zhou  
**Map mã:** `CLIN_EVENT-ZHOU-MAP-v0.1.md` · Glossary: `EARLY-SIGNAL-GLOSSARY`  
**Cấm:** coi vignette = BN thật · train model trên vignette · mở omics

## Cách dùng (10–15′)

1. Đọc vignette → chọn mã **0–4** (+ note nếu 4).  
2. Đối chiếu đáp án gợi ý (cuối file) — chỉnh nếu PI khác (ghi lý do).  
3. 1 câu vào daily log: *sự kiện này làm lệch PCT/CFU thế nào?*  
4. Tick STREAK khi ritual đủ.

## Vignette A — D3, không biến cố mới

BN SA-01, visit D3: PCT_EPITH tăng nhẹ so D0, CFU giảm, không sốt/AE_LOCAL mới, thay băng đúng lịch.  
**Mã đề xuất:** ___

## Vignette B — nhiễm cục bộ mới

Giữa D0 và D3: đỏ/sưng tăng, cấy lại dương tính loài mới theo SOP site; PI ghi “nhiễm cục bộ mới”. PCT đứng.  
**Mã đề xuất:** ___ · Alert nào? (A1/A4?) ___

## Vignette C — đổi chế độ chăm sóc

Site tăng tần suất thay băng + thêm sản phẩm hỗ trợ ngoài protocol local care (không đổi nhánh RCT). Adherence ghi nhận.  
**Mã đề xuất:** ___ · Liên hệ PB-008? ___

## Vignette D — cắt lọc

Ngày trước D7: cắt lọc tại phòng mổ nhỏ; ảnh ImageJ sau thủ thuật.  
**Mã đề xuất:** ___ · Exploratory: stratify hay exclude? `[CẦN XÁC NHẬN SAP]`

## Vignette E — không khớp 1–3

BN báo “ngã nhẹ” không liên quan vết; không nhiễm/can thiệp/phẫu thuật.  
**Mã đề xuất:** ___ (+ `clin_event_note`?)

## Đáp án gợi ý (đọc sau khi chọn)

| V | Mã | Ghi chú ngắn |
|---|-----|--------------|
| A | **0** | Không sự kiện mới — baseline ổn định trong cửa sổ |
| B | **1** | Nhiễm cục bộ mới → sensitivity / A4 nếu PCT đứng + event |
| C | **2** | Can thiệp/đổi chăm sóc đáng kể — confounder adherence (PB-008) |
| D | **3** | Phẫu thuật/cắt lọc — strong event; xử lý theo SAP ES |
| E | **4** | Khác + note “ngã nhẹ, không liên quan vết” — review PI |

PI có thể khác C vs 0 nếu “đổi chăm sóc” không đủ “đáng kể” — ghi lý do trong log.

## Liên hệ multi-omics / AI

- Zhou: event → dịch chuyển tín hiệu; Smart A bắt bằng `clin_event` trên **L1** trước L3.  
- PB-009: vignette luyện L1 đủ nghĩa trước khi nói cần PEA.  
- Không dùng 5 vignette làm tập train.

## Checklist DONE

- [ ] Làm ≥2 vignette · đối chiếu đáp án  
- [ ] 1 câu insight vào log ngày ôn  
- [ ] STREAK · không order assay

## Liên kết

`CLIN_EVENT-ZHOU-MAP` · `ALERT-SA01` · `STUDY-SHEET-ZHOU` · `RITUAL-CARDS-INDEX`
