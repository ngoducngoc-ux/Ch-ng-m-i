# H0 / H1 — SA-01 early-signal (Precure exploratory)

**Mã:** HYP-SA01-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 23

## Đại lượng thời gian

| Ký hiệu | Mốc |
|---------|-----|
| \(t^*\) | D21 (primary biểu mô hóa) |
| \(t'\) | D0, D3, D7 (exploratory predictors) |

## Giả thuyết

**H0:** Mô hình M0 (chỉ \(Z(D0)\) + covariates) và M3 (\(Z(D0{-}D7)\)) có **AUROC dự báo \(Y_{D21}\)** không khác có ý nghĩa (sau CV nội bộ / DeLong exploratory).

**H1:** M3 cải thiện discrimination (AUROC) và/hoặc calibration (Brier) so với M0 trên cùng ITT exploratory population.

**H0\_mol (tương lai, sau G2):** Thêm \(X_{\text{mol}}(t')\) không cải thiện so với M3 chỉ \(Z\).

## Không claim

- Không thay primary D21.  
- Không dùng kết quả synthetic làm bằng chứng BN.

## Liên kết

- `EQ-SA01-early-warning-v0.1.md` · `SAP-SA01-ES-v0.1-DRAFT.md`
