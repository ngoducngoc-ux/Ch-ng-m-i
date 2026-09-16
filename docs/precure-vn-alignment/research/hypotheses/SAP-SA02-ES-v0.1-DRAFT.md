# SAP exploratory — Early-signal SA-02 (nháp)

**Mã:** SAP-SA02-ES-v0.1-DRAFT  
**Ngày:** 2026-09-16  
**Phạm vi:** thăm dò; **không** thay primary ΔVAS D3−D0.

## 1. Mục tiêu exploratory

Đánh giá liệu **CFU họng** và chuỗi **VAS D0–D3** (± D1) dự báo đáp ứng sớm (binary RELIEF_D3 hoặc ΔVAS liên tục) tốt hơn chỉ VAS tại D0.

## 2. Quần thể

ITT primary không đổi. Exploratory: có VAS D0 và D3; sensitivity nếu thiếu D1.

## 3. Outcome exploratory

- \(Y_1\): RELIEF_D3 = 1 nếu ΔVAS ≤ −2 (secondary binary).  
- \(Y_2\): ΔVAS_D3 liên tục (descriptive / linear regression).

Primary vẫn: ΔVAS D3−D0 theo đề cương — không gộp vào mô hình ES làm endpoint chính.

## 4. Predictors

`eCRF-SA02-early-signal-dictionary-v0.1.md` — M0–M3; sandbox `sa02_early_signal_synthetic_m0_m3.py`.

## 5. Phương pháp

Logistic (Y_1) / linear (Y_2); AUROC + Brier cho Y_1; DeLong M0 vs M2/M3; FDR exploratory.

## 6. Blind / leakage

Không dùng VAS D5/D7 để dự báo D3 trong mô hình “early”.

## 7. Việc nhỏ

- [x] Sandbox synthetic M0–M3  
- [ ] Chốt D1 visit với PI TMH  
- [ ] Gộp vào SAP chính khi amendment
