# PB-007 — Khung phương trình Precure shift (\(Z\) vs \(X\))

**Mã:** PB-007-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 10 / 23 · cờ đầu SA-01 (EQ) · support SA-02/05  
**Gắn:** EQ-SA01|02|05 · SHIFT bank · G2 CLOSED · L3 gated  

## Vấn đề

Có \(Y(t^*)\) đã chốt, nhưng chưa rõ: tồn tại \(t' \ll t^*\) sao cho **\(X_{\text{mol}}(t')\)** cải thiện dự báo so với chỉ **\(Z_{\text{lâm sàng}}(t')\)** — hay L1→L2 trên \(Z\) đã đủ cho giai đoạn này?

## Câu hỏi Smart A

1. Với SA cờ đầu, \(Y(t^*)\) và \(t'\) đang dùng là gì?  
2. M0–M3 trên \(Z\) trả lời được gì **trước** khi mở \(X\)?  
3. Điều kiện nào (G2 + ethics + câu hỏi \(X\) thêm giá trị) mới cho phép M4?

## Khung (điền theo SA)

\[
P(Y=1)=\sigma\big(\beta_0 + \boldsymbol{\beta}_Z^\top Z(t') + \cdots\big)
\quad\text{rồi (chỉ sau G2):}\quad
+\boldsymbol{\beta}_X^\top X(t')
\]

| SA | \(Y(t^*)\) | \(Z(t')\) | \(X\) (gated) | EQ |
|----|------------|-----------|---------------|-----|
| **01** | D21 biểu mô | PCT/CFU/VAS/`clin_event` D0–D7 | \(X_{\text{PEA}}\) | `EQ-SA01` |
| **02** | VAS relief D3 | D1/CFU / \(\Delta\)VAS (không leakage M1) | mucosa CLOSED | `EQ-SA02` |
| **05** | PUSH improved D14 | PUSH/CFU/turn ≤D7 | ICU omics CLOSED | `EQ-SA05` |

## Việc nhỏ

- [ ] Điền 1 dòng M0 vs M3 cho SA cờ đầu (`EQ-5MIN` hoặc Drill 10′)  
- [ ] 1 câu Precure shift (`SHIFT-5MIN`) — \(t'\) cải thiện vs \(Z(D0)\) only  
- [ ] Xác nhận M4/X: **CLOSED** (`G2-5MIN` / `L1L2L3-5MIN`)  
- [ ] **5′ drill:** `PB007-5MIN-MICRO-DRILL` · **`PB007-EQ-5MIN-MICRO-DRILL`** · **`SHIFT-PB007-5MIN-MICRO-DRILL`**  

## Không làm

- Order PEA vì đã viết \(\sigma(\ldots + X)\)  
- Coi AUROC synthetic = bằng chứng \(X\) thêm giá trị  
- Đổi primary vì PB-007 “đã có khung”  

## Liên kết

- **Thẻ khoa học:** **`EQ-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`

- `../problem-bank.md` (PB-007) · `../equations/EQ-SA01|02|05-early-warning-v0.1.md`  
- `EQ-5MIN-MICRO-DRILL` · `SHIFT-5MIN-MICRO-DRILL` · `G2-5MIN-MICRO-DRILL`  
- Bridge: `MULTI-OMICS-PEA-SA01-BRIDGE` · `ENDPOINTS-CROSS-SA-BRIDGE` · **`PB007-SCIENCE-CARD`**
