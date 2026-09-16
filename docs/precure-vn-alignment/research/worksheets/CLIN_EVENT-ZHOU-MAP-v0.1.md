# `clin_event` ↔ Zhou — map sự kiện dọc (early-signal)

**Mã:** CLIN_EVENT-ZHOU-MAP-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 02 · 23–24 · 28 · 31 (ôn) · **DOI Zhou:** [10.1038/s41586-019-1236-x](https://doi.org/10.1038/s41586-019-1236-x)  
**eCRF:** `redcap_sa01_early_signal_dictionary_v0.2.csv` · Study sheet: `STUDY-SHEET-ZHOU-LONGITUDINAL`

## Một câu

> Zhou: omics dịch mạnh khi có **sự kiện** (nhiễm/tiêm) — Smart A bắt analog bằng `clin_event` trên \(Z\) REDCap **trước** mọi \(X\) PEA; không train “early” bằng cùng biến outcome.

## Mã eCRF v0.2 → Zhou / SA-01

| `clin_event` | Nhãn eCRF | Analog Zhou | Dùng early-signal SA-01 | Không làm |
|--------------|-----------|-------------|-------------------------|-----------|
| **0** | Không | Baseline ổn định | Đối chứng trong chuỗi D0–D7 | Bỏ qua missing vs 0 |
| **1** | Nhiễm trùng cục bộ mới | Infection event | Sensitivity / ALERT A4 · lệch PCT/CFU | Gán nhân quả omics |
| **2** | Can thiệp / đổi chăm sóc đáng kể | “Intervention” làm lệch quỹ đạo | Confounder adherence / PB-008 | Đổi nhánh RCT |
| **3** | Phẫu thuật / cắt lọc | Strong clinical event | Stratify / exclude exploratory tùy SAP | Claim chữ ký “trước Dx” từ 1 case |
| **4** | Khác (+ `clin_event_note`) | Event không chuẩn hóa | Ghi note; review PI | Mã ẩn hàng loạt không note |

## Map sang H0/H1 & sampling

| Câu hỏi | File | Quyết định ritual |
|---------|------|-------------------|
| Chuỗi \(Z\)+event cải thiện vs snapshot D0? | `HYP-SA01-H0H1` · `EQ-SA01` | H1 exploratory M3 vs M0 — **không** claim lâm sàng |
| Event bắt ở visit nào? | `SAMPLING-SCHEDULE-SA01` | D0/D3/D7 — D3 `[CẦN XÁC NHẬN DM]` |
| Alert khi event + PCT đứng? | `ALERT-SA01` A4 · NatMed map | Nội bộ nghiên cứu |

## Y tế số (PB-004 / PB-009)

- `clin_event` = entity **event** kèm visit + timestamp — nền L1 trước L2 AI.  
- L3 multi-omics chỉ giải thích thêm **sau** khi event+\(Z\) đã có signal (G2).  
- **Cross-SA + BN map:** `CLIN_EVENT-CROSS-SA-ATLAS-v0.1.md` · `BN-VISIT-MAP-TEMPLATE-v0.1.md`

## Checklist DONE (PI — chọn 1 ngày ôn)

- [ ] 1 hàng bảng mã → 1 câu trong log (sự kiện nào lệch PCT_EPITH?)  
- [ ] (Khuyến nghị) ≥2 vignette: `CLIN_EVENT-CODING-VIGNETTES-v0.1.md`  
- [ ] (Sau STREAK≥3) 1 hàng `CLIN_EVENT-CROSS-SA-ATLAS` nếu ôn SA-02/05  
- [ ] STREAK tick · không order assay  
- [ ] (Ngày 22) cờ SA-01 vẫn hợp lý vì có `clin_event`+pipeline?

## Liên kết

- Notes Zhou: `reading-notes/2026-09-18-zhou-nature-prediabetes.md`  
- Cards: `RITUAL-CARDS-INDEX.md` · `NATMED-ACTIONABLE-ALERT-MAP` · `PEA-L1L2L3-DECISION-CARD`  
- Luyện: `CLIN_EVENT-CODING-VIGNETTES-v0.1.md`  
- Cross-SA: `CLIN_EVENT-CROSS-SA-ATLAS-v0.1.md`  
- DM: `DATA-MANAGER-HANDOFF-RedCap-v0.2.md` (clin_event)
