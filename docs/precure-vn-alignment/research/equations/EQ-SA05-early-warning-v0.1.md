# Phương trình early warning — SA-05 (PB-003)

**Mã:** EQ-SA05-v0.1  
**Ngày:** 2026-09-16 · **Cập nhật:** M0–M3/M4 rõ lớp · bridge endpoints · **Drill 10′**  
**Curriculum:** Ngày 08–09 (2026-09-24…25) · Q2 support ICU

## Primary (không đổi)

\[
Y_{\text{prim}} = \Delta\mathrm{PUSH}_{D14-D0}
\quad\text{(synopsis N=80 ICU)}
\]

## Exploratory early-signal (binary ES)

\[
Y_{\text{improved}} = \mathbb{1}\{(\mathrm{PUSH}_{D14}-\mathrm{PUSH}_{D0})\le -2\}
\]

\[
P(Y_{\text{improved}}=1)=\sigma\big(\beta_0 + \boldsymbol{\beta}_Z^\top Z(D0,D3,D7) + \beta_g GROUP + \boldsymbol{\beta}_C^\top C\big)
\]

| Khối | Biến (eCRF SA-05 v0.1) | Ghi chú |
|------|------------------------|---------|
| \(Z\) | PUSH_D0/D3/D7 · CULTURE_CFU_D0/D3 · (component PUSH) | Cửa sổ \(t'\le D7\) |
| \(C\) | AGE, STAGE_NPUAP, TURN_ADHERE | ICU confounder bắt buộc |
| Nhóm | GROUP | RCT arm |
| \(X\) | Omics / marker sâu | **gated G2** — mặc định CLOSED |

### M0–M3 (SAP ES — khớp sandbox QC)

| Model | Predictors (ý) | Mục đích |
|-------|----------------|----------|
| **M0** | PUSH_D0 + AGE + STAGE_NPUAP + GROUP | Baseline only |
| **M1** | + PUSH_D3, PUSH_D7 | Chuỗi sớm trước D14 |
| **M2** | + CULTURE_CFU_D0, CFU_D3 | Nhiễm / burden |
| **M3** | + TURN_ADHERE | Full early + adherence xoay trở |

**H0/H1 (exploratory):** M3 vs M0 — chuỗi PUSH/CFU/turn cải thiện dự báo \(Y_{\text{improved}}\) vs snapshot D0 — `EH-SA05-early-signal` · không đổi primary.

**Precure shift:** tồn tại \(t'\le D7\) sao cho chuỗi PUSH (± component) + adherence dự báo tốt hơn chỉ D0 — **exploratory**, không auto-treat ICU.

**Component vs total (Ngày 08):** early có thể trên thành phần PUSH (diện tích / xuất tiết / mô) — `PUSH-SA05-COMPONENTS` · Stotts DOI — không thay primary \(\Delta\)PUSH D14.

### Drill 10′ (điền — ICU early / không auto-treat)

```text
t* SA-05: ________     t' cửa sổ (≤D7): ________
Y_improved định nghĩa: ________
M0 vs M3 thêm gì (PUSH/CFU/turn): ________
Component PUSH early? CÓ|KHÔNG — 1 thành phần: ________
X / L3 ICU: CLOSED vì ________
1 câu KHÔNG gộp endpoint với SA-01/02:
```

## M4 / \(X\) — L3 (gated)

\[
P(Y_{\text{improved}}=1)=\sigma\big(\ldots + \boldsymbol{\beta}_X^\top X(t')\big)
\quad\text{chỉ sau G2 trên data thật ICU}
\]

Không mở vì đã đọc PUSH / EQ. Gap G1–G5: `EQ-EH-SA05-GAP`.

## ALERT (không phải model)

B1–B3 nội bộ trên PUSH/`TURN_ADHERE` — `ALERT-SA05` · atlas `ALERT-CROSS-SA-ATLAS`. Ngưỡng `[CẦN XÁC NHẬN]` lâm sàng. ALERT ≠ app Dx; ≠ đổi \(\beta\) SAP.

## Cấm

- Predictor sau \(t^*\) (PUSH_D14) làm “early”  
- \(\Delta\)PUSH / AUROC sandbox = chẩn đoán ICU  
- Gộp endpoint với SA-01/02  
- Order omics ICU trước G2

## Liên kết

- `EH-SA05-early-signal-v0.1.md` · `SAP-SA05-ES-v0.1-DRAFT.md` · `sa05_early_signal_synthetic_m0_m3.py`  
- Bridge: `ENDPOINTS-CROSS-SA-BRIDGE-v0.1.md` · thẻ `ENDPOINTS-EARLY-SIGNAL-RITUAL-CARD`  
- Drill hàng ngày: `../study-sheets/STUDY-SHEET-MULTI-OMICS-ES-DRILL-v0.1.md` (§ SA-05)  
- Leakage atlas: `../worksheets/LEAKAGE-CROSS-SA-ATLAS-v0.1.md`  
- ALERT atlas: `../worksheets/ALERT-CROSS-SA-ATLAS-v0.1.md`  
- clin_event atlas: `../worksheets/CLIN_EVENT-CROSS-SA-ATLAS-v0.1.md`  
- `PUSH-SA05-COMPONENTS` · `EQ-EH-SA05-GAP` · `CROSS-SA-EARLY-SIGNAL-MAP`
