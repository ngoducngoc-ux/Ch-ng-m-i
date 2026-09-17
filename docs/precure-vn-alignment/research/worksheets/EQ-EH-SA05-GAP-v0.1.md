# Gap EQ-SA05 ↔ EH-SA05 ↔ SAP ES (trước SAP chính)

**Mã:** EQ-EH-SA05-GAP-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 09 · `equations/EQ-SA05-early-warning-v0.1.md` · PB-003

## Đã khớp

| Hạng mục | EQ-SA05 | EH-SA05 / SAP ES |
|----------|---------|------------------|
| Outcome exploratory | \(Y_{\text{improved}}\) ΔPUSH≤−2 | IMPROVED_D14 binary |
| Chuỗi sớm | PUSH D3, D7 | M1–M3 predictors |
| Confounder ICU | \(C_{\text{turn}}\) | TURN_ADHERE bắt buộc |
| M0 baseline | PUSH_D0 + stage + group | Cùng trong SAP §4 |
| Sandbox | — | `sa05_early_signal_synthetic_m0_m3.py` + verify |

## Còn thiếu trước amendment SAP chính

| # | Gap | Việc nhỏ | Owner |
|---|-----|----------|-------|
| G1 | **Ngưỡng ΔPUSH −2** chưa cite pilot ICU | Xác nhận với đề cương SA-05 synopsis | PI `[CẦN XÁC NHẬN]` |
| G2 | **CFU_D0** trong EQ — field REDCap staging chưa review DM | INDEX SA-05 sau SA-01 v0.2 | Data Manager |
| G3 | **Alerts B1–B3** ngưỡng ≠ SAP ES coefficients | Tách: alert = vận hành; SAP = ước lượng | Clinical + stats |
| G4 | **Component PUSH** (exudate) chỉ sensitivity | `PUSH-SA05-COMPONENTS-v0.1.md` → 1 dòng SAP ES | Stats nháp |
| G5 | Synthetic AUROC **không** pass G2 / không chốt B1–B3 | Ghi rõ trong ALERT + SAP | Done (policy) |

## Một câu trả lời daily log 25/09

> EQ và EH/SAP ES đã cùng khung M0–M3; thiếu chủ yếu **chốt ngưỡng lâm sàng (G1)**, **REDCap ICU (G2)**, và **tách alert vs model (G3)** trước amendment.

## Liên kết

- `EH-SA05-early-signal-v0.1.md` · `SAP-SA05-ES-v0.1-DRAFT.md` · `ALERT-SA05-v0.1.md`
