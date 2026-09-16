# Longitudinal early-signal — SA-01 × Precure (worksheet)

**Mã:** LONGITUDINAL-ES-SA01-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Q2 Ngày 89 (ôn) · gắn Ngày 02–03 · **Cờ:** SA-01 exploratory  
**Không:** claim chẩn đoán sớm · không mở biospecimen trước G1–G2

## Phương trình (curriculum Ngày 23+)

```text
Y_lâm_sàng(D21) = f( X_phân_tử(t0…t*), Z_dọc(D0…D7…), C_baseline ) + ε
t* = endpoint chính (% biểu mô / lành thương D21)
Câu hỏi Precure: tồn tại t' ∈ {D0,D3,D7} sao cho Z(t') hoặc X(t')
dự báo Y(D21) tốt hơn Z(t') đơn thuần — chỉ exploratory?
```

| Thành phần | SA-01 (v0.1–v0.2) | Sau G1–G2 |
|------------|-------------------|-----------|
| \(Y\) | PCT_EPITH / lành D21 | không đổi primary |
| \(Z\) dọc | % biểu mô, CFU, VAS, AE, `clin_event` | cùng + QC dày hơn |
| \(X\) | **gated** (`SPEC-SA01-BIO`) | PEA/panel nếu PI/DSMB pass |
| \(C\) | baseline D0 | stratum + covariates SAP |

## Map nguồn đã kiểm → Smart A

| Nguồn | Insight giữ | Không suy diễn |
|-------|-------------|----------------|
| Zhou *Nature* 2019 DOI 10.1038/s41586-019-1236-x | Biến thiên **trong người** + **sự kiện** (nhiễm) trước triệu chứng rõ | Cohort khỏe ≠ BN vết thương RCT |
| Nat Med 2019 DOI 10.1038/s41591-019-0414-6 | Profiling → **đổi hành vi** (PB-008) | “Actionable” ≠ sản phẩm Dx thương mại |
| DESIGN-SA01-minimal-longitudinal | D0/D3/D7 đủ quỹ đạo \(Z\) trước D21 | Không tăng rủi ro BN bằng visit thừa |
| INTERIM-MOCK | Rehearse báo cáo descriptive | Synthetic AUROC ≠ pass G2 |

## Ba câu hỏi PI (điền khi ritual)

1. Window D3 bắt buộc hay D1–D3? `[CẦN XÁC NHẬN / DM]`  
2. `clin_event` đủ bắt infection/AE để song song Zhou? `[ ]`  
3. Khi nào (nếu) mở \(X\) — chỉ sau G2 trên **data thật**? `[CLOSED mặc định]`

## Liên kết

- `hypotheses/DESIGN-SA01-minimal-longitudinal-v0.1.md`  
- `worksheets/PB-008-participation-effects-v0.1.md` · `G2-READINESS-v0.1.md` · `INTERIM-DESCRIPTIVE-MOCK-v0.1.md`  
- `equations/EQ-SA01-early-warning-v0.1.md` · `guides/AI-LONGITUDINAL-STACK-v0.1.md` · `y-te-so-precure-bridge-v0.1.md`
