# Phương trình early warning — SA-02 (PB-002)

**Mã:** EQ-SA02-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 12 / Q2 staging · **Primary không đổi:** VAS D3

## Primary (không đổi)

\[
Y_{D3} = \text{VAS}_{\text{sore throat / triệu chứng}}(D3)
\quad\text{(hoặc } \Delta\text{VAS}_{D0\to D3}\text{ theo SAP primary)}
\]

## Exploratory early-signal (trước / cùng cửa sổ D3)

\[
P(\text{relief}|D3) = \sigma\big(\beta_0 + \boldsymbol{\beta}_Z^\top Z(D0,D3) + \beta_g GROUP + \boldsymbol{\beta}_C^\top C \big)
\]

| Khối | Ứng viên (eCRF SA-02 v0.1) |
|------|----------------------------|
| \(Z\) | VAS series, điểm khám họng, sốt/AE, (tương lai) marker niêm mạc |
| \(C\) | tuổi, baseline severity, adherence |
| \(X\) | **gated** — không mở trước G1–G2 / ISO liên quan |

**Câu hỏi Precure:** có \(t' \le D3\) sao cho tín hiệu sinh học / \(Z(t')\) **dẫn trước** hoặc bổ sung \(\Delta\)VAS — hay triệu chứng **trễ hơn** marker? Chỉ exploratory; không claim Dx sớm.

## Liên hệ Zhou / multi-omics

- Zhou: thay đổi mạnh khi **sự kiện** nhiễm — SA-02 cần timestamp triệu chứng + (nếu có) marker cùng cửa sổ.  
- Không train model trên \(Y_{D3}\) rồi báo “early” bằng cùng biến outcome.

## Liên kết

- `eCRF-SA02-early-signal-dictionary-v0.1.md` · `SAP-SA02-ES-v0.1-DRAFT.md` · `VAS-SCALE-HARMONIZE-SA02-v0.1.md`  
- `LONGITUDINAL-EARLY-SIGNAL-SA01-v0.1.md` (khung phương trình chung) · `problem-bank.md` PB-002
