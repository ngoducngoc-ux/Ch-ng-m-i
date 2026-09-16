# Phương trình early warning — SA-05 (PB-003)

**Mã:** EQ-SA05-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 09 (2026-09-25)

## Làm việc

\[
Y_{\text{improved}} = \mathbb{1}\{(\mathrm{PUSH}_{D14} - \mathrm{PUSH}_{D0}) \le -2\}
\]

\[
P(Y_{\text{improved}}=1) = \sigma\big(\beta_0 + \beta_1 \mathrm{PUSH}_{D0} + \beta_2 \mathrm{PUSH}_{D3} + \beta_3 \mathrm{PUSH}_{D7} + \beta_4 \mathrm{CFU}_{D0} + \beta_5 C_{\text{turn}} + \beta_6 \mathrm{GROUP}\big)
\]

| Ký hiệu | Ý nghĩa |
|---------|---------|
| \(C_{\text{turn}}\) | TURN_ADHERE (0–2) |
| M0 | chỉ PUSH_D0 + stage + age + group |
| M3 | thêm PUSH D3/D7 + CFU + turn |

**Precure shift:** tìm \(t' \le D7\) sao cho chuỗi PUSH/adherence dự báo \(Y\) tốt hơn snapshot D0 — **exploratory**, không auto-treat.

## Liên kết

- `EH-SA05-early-signal-v0.1.md` · `SAP-SA05-ES-v0.1-DRAFT.md` · sandbox `sa05_early_signal_synthetic_m0_m3.py`  
- Ritual: `worksheets/ENDPOINTS-EARLY-SIGNAL-RITUAL-CARD-v0.1.md` (Ngày 08–09)
