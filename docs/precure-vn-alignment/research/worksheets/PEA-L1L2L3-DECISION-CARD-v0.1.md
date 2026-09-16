# PEA → L1 / L2 / L3 — thẻ quyết định (Ngày 05–07)

**Mã:** PEA-L1L2L3-DECISION-CARD-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 05 Lundberg · 06 Assarsson · 07 Wik  
**Dùng với:** `STUDY-SHEET-NATMED-PEA` §05–07 · `AI-LONGITUDINAL-STACK` · `MULTI-OMICS-GATES`  
**Mặc định:** **không order assay** · G2 **CLOSED**

## Một câu (mọi ngày PEA)

> PEA/Olink-class là **L3 (\(X\))** — chỉ có nghĩa sau khi L1 (\(Z\) dọc + `clin_event`) và L2 (M0–M3 exploratory trên data thật) đã có tín hiệu; N=120 ≠ discovery 96-plex mù.

## Ba ngày → ba quyết định

| Ngày | DOI / ý cốt | Quyết định ghi vào log | Artifact |
|------|-------------|------------------------|----------|
| **05** | Lundberg PEA = proximity + qPCR | 1 câu *vì sao chưa lấy mẫu*: pre-analytic R1–R3 chưa chốt trên exudate | `PRE-ANALYTIC-PEA-SA01-v0.1.md` |
| **06** | Assarsson 96-plex ↑ throughput | 1 câu *panel hẹp ≤15–20* nếu G2 pass — không full 96 | `PEA-PANEL-FEASIBILITY-SA01-v0.1.md` |
| **07** | Wik PEA+NGS scale ≠ REDCap | Tick 3 điều kiện G2 → expected **CLOSED**; 2 layer Clinical vs Omics | `G2-READINESS-v0.1.md` |

## Map sang phương trình SA-01

\[
P(Y_{D21}=1)=\sigma(\beta_0+\boldsymbol{\beta}_Z^\top Z+\cdots)
\quad\text{hiện tại: chỉ }Z\text{ (L1/L2)}
\]

- **M4 / \(X_{\text{PEA}}\)** chỉ vào SAP amendment **sau G2** trên N thật — không thay primary \(Y_{D21}\).  
- Chi tiết: `equations/EQ-SA01-early-warning-v0.1.md` · `SAP-SA01-ES-v0.1-DRAFT.md`

## Y tế số (2 layer — Wik / PB-004)

| Layer | Hệ | Smart A hôm nay |
|-------|-----|-----------------|
| Clinical (L1) | REDCap visit · \(Z\) · ALERT | Đang build SA-01 v0.2 |
| Analysis (L2) | Export de-ID → M0–M3 | Sandbox + `verify.sh` (≠ lâm sàng) |
| Omics (L3) | LIMS / PEA batch QC | **CLOSED** đến G2 |

Bridge: `y-te-so-precure-bridge-v0.1.md` §2 · `G2-READINESS` §y tế số

## Cấm (ghi nhớ)

- Order Olink/PEA vì đã đọc abstract / vì curriculum PREP  
- Pass G2 bằng AUROC synthetic  
- Claim “multi-omics phát hiện sớm” kiểu VDHN trước khi có \(Z\) + G2  
- Gộp SA-03 biofilm in-vitro thành Dx bệnh nhân

## Checklist DONE (PI — mỗi ngày 05/06/07)

- [ ] Abstract + 1 dòng insight  
- [ ] 1 câu quyết định (cột trên)  
- [ ] STREAK PREP → **DONE**  
- [ ] Không lab order · không đóng Goal

## Sau Ngày 07

Endpoints sheet Ngày 08–14 · `STUDY-SHEET-SMART-A-ENDPOINTS-v0.1.md` · Tier 2 SPIRIT: `STUDY-SHEET-DESIGN-YTESO-AI-v0.1.md`

## Liên kết

- Notes: `2026-09-21-pea-lundberg` · `09-22-assarsson` · `09-23-wik`  
- Ôn lại: `OMICS-IF-G2-v0.1.md` (Ngày 47–49) · `NATMED-ACTIONABLE-ALERT-MAP` (actionable ≠ mở PEA)
