# Study sheet — Zhou 2019 (longitudinal multi-omics · Ngày 02 / 28)

**Mã:** STUDY-ZHOU-v0.1 · **Ngày:** 2026-09-16  
**DOI:** [10.1038/s41586-019-1236-x](https://doi.org/10.1038/s41586-019-1236-x) · Notes: `reading-notes/2026-09-18-zhou-nature-prediabetes.md`

## Ba ý giữ (đọc abstract)

1. **Trong người + giữa người** — hồ sơ “khỏe” không đồng nhất.  
2. **Sự kiện** (nhiễm / tiêm) làm dịch chuyển omics mạnh hơn baseline tĩnh.  
3. Chữ ký phân tử **trước** chẩn đoán (minh họa cá thể) = logic Precure — không = sản phẩm Dx.

## Map SA-01 (cờ đầu)

| Zhou | SA-01 | Artifact |
|------|-------|----------|
| Chuỗi thời gian multi-omics | \(Z\) D0/D3/D7 trước; \(X\) sau G2 | DESIGN-SA01 · SPEC-BIO |
| Infection event | `clin_event` / AE / nhiễm cục bộ | eCRF v0.2 |
| Prediabetes signature | M0–M3 → \(Y_{D21}\) exploratory | EQ-SA01 · SAP ES |

**Ranh giới:** cohort ~106 ≠ RCT N=120; không claim cùng AUROC.

**Viết vào log (DONE)**

1 câu: sự kiện nào trong D0–D7 làm lệch quỹ đạo PCT_EPITH? + STREAK.  
**Map mã eCRF:** `worksheets/CLIN_EVENT-ZHOU-MAP-v0.1.md` (0–4 ↔ Zhou).  
**Cross-SA event:** `worksheets/CLIN_EVENT-CROSS-SA-ATLAS-v0.1.md` (sau STREAK≥3).  
**Luyện:** `worksheets/CLIN_EVENT-CODING-VIGNETTES-v0.1.md` (≥2 vignette).  
**Bridge:** `worksheets/EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01-v0.1.md` (cùng logic Nat Med Ngày 03).  
**Thẻ khoa học STREAK/T2:** `worksheets/ZHOU-STREAK3-SCIENCE-CARD-v0.1.md`.  
**1 câu lệch hướng:** `PRECURE-SHIFT-CROSS-SA-BANK` hàng SA-01 · Dọc.

### Fill-in 15′ (abstract → log)

```text
3 ý giữ: trong/giữa người · sự kiện nhiễm/tiêm · chữ ký trước chẩn đoán (minh họa)
Sự kiện SA-01 analog: nhiễm cục bộ | AE_LOCAL | thay băng | phẫu thuật | …
clin_event mã gợi ý: 0–4 (xem map)
Câu hỏi: sự kiện nào lệch PCT_EPITH → Y_D21?
1 câu Precure shift (Dọc): ________
L3 hôm nay: CLOSED (gate) vì: ________
```

## Liên kết

`CLIN_EVENT-ZHOU-MAP` · `CLIN_EVENT-CROSS-SA-ATLAS` · `CLIN_EVENT-CODING-VIGNETTES` · **`ZHOU-STREAK3-SCIENCE-CARD`** · `LONGITUDINAL-EARLY-SIGNAL-SA01` · `AI-LONGITUDINAL-STACK` · `L1L2L3-DAILY-GATE-CARD` · `PRECURE-SHIFT-CROSS-SA-BANK` · `daily-log/2026-09-18.md` · `RITUAL-CARDS-INDEX`
