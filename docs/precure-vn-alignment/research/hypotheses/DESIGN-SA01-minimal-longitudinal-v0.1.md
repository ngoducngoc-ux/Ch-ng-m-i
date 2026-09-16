# Thiết kế dọc tối thiểu — SA-01 early-signal (exploratory)

**Mã:** DESIGN-SA01-v0.1  
**Ngày:** 2026-09-16  
**Nguồn:** Curriculum Ngày 02 (Zhou 2019) + eCRF `redcap_sa01_early_signal_dictionary_v0.1.csv`  
**Không thay đổi** primary D21 hay N=120.

## Tóm tắt 3 dòng (cho daily log)

1. **3 mốc cốt lõi** trước endpoint: **D0, D3, D7** — đủ để ước lượng quỹ đạo \(Z\) và so sánh M0→M3 (SAP synthetic).  
2. **3 lớp dữ liệu** (không biospecimen v0.1): **(C)** baseline D0; **(Z_dọc)** % biểu mô ImageJ + CFU + VAS + AE; **(E_sự kiện)** nhiễm lâm sàng / adherence / AE_LOCAL ghi theo timestamp visit.  
3. **Endpoint khóa** tại **D21** (\(Y_{D21}\)); mọi tín hiệu D0–D7 chỉ **exploratory** — không dùng để đổi nhánh RCT hay claim chẩn đoán.

## Ma trận thời điểm × lớp

| Lớp | D0 | D3 | D7 | D14 | D21 |
|-----|----|----|----|----|-----|
| C (covariates) | ✓ | — | — | — | — |
| Z % biểu mô (PCT_EPITH) | ✓ | ✓ | ✓ | tùy SOP | **Y primary** |
| Z vi sinh (CULTURE_CFU) | ✓ | tùy site | ✓ | — | — |
| Z triệu chứng (VAS_DRESS) | ✓ | ✓ | ✓ | — | — |
| Z an toàn (AE_LOCAL…) | mọi visit | | | | |
| E (sự kiện lâm sàng) | ghi khi xảy ra | | | | |
| X phân tử | — | — | — | — | **sau cổng G1–G2** (`SPEC-SA01-BIO-v0.1-DRAFT.md`) |

## Liên hệ Zhou / Precure

- Biến thiên **trong người** + **sự kiện** (nhiễm cục bộ ≈ respiratory infection trong cohort Zhou) — cần trường sự kiện trong eCRF, không chỉ baseline.  
- “Khỏe mặc định” khác nhau giữa BN → stratum + mixed model / covariates trong SAP.

## Việc nhỏ

- [x] Viết tài liệu này từ log Ngày 02  
- [ ] Data Manager: xác nhận visit D3 bắt buộc vs D1–D3 window trong đề cương  
- [x] Gắn trường **CLIN_EVENT** → CSV v0.2 + handoff DM  

## Liên kết

- `EH-SA01-early-signal-v0.1.md` · `ALERT-SA01-v0.1.md` · `SAP-SA01-ES-v0.1-DRAFT.md`
