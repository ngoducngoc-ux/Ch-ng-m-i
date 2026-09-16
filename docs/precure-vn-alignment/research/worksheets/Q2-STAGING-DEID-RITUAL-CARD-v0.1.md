# Q2 — Staging · de-ID · SA support (Ngày 61–70)

**Mã:** Q2-STAGING-DEID-RITUAL-CARD-v0.1  
**Ngày:** 2026-09-16  
**Mở sau** checkpoint 60d · Curriculum: `curriculum-days-61-90.md`  
**Hub:** `RITUAL-CARDS-INDEX.md` · Checklist: `REDCAP-DEID-EXPORT-CHECKLIST-v0.1.md`  
**Cờ đầu:** SA-01 · G2 **CLOSED** mặc định · Goal **ACTIVE**

## Một câu (mọi ngày Q2 tuần 9–10)

> Staging = **đường dữ liệu thật tối thiểu** (REDCap → export de-ID → QC) + staging SA-02/05 **support** — cấm biospecimen / cấm gộp endpoint / cấm đếm PREP = DONE.

## Hai khối

| Khối | Ngày N | Việc | Artifact |
|------|--------|------|----------|
| **Staging & de-ID** | 61–65 | Production path · QC schema · consent boundary · DM · PB-004 | `REDCAP-DEID-EXPORT-CHECKLIST` · DM INDEX · PIPELINE |
| **SA support** | 66–70 | Weekly · SA-02 VAS · SA-05 PUSH · cross-SA · recap | CROSS-SA map · EQ · endpoints card |

## Ritual tối thiểu (1 câu DONE)

| N | Log | Quyết định / việc |
|---|-----|-------------------|
| **61** | `2026-11-17.md` | 1 cột **cấm** rời site (deny D#) từ checklist de-ID |
| **62** | `2026-11-18.md` | verify / `redcap_import_qc` — PASS = schema, ≠ lâm sàng |
| **63** | `2026-11-19.md` | 1 field PII vs analysis (consent / PB-004) |
| **64** | `2026-11-20.md` | DM review trống? → forward checklist (không gửi thay PI) |
| **65** | `2026-11-21.md` | 1 dòng problem-bank PB-004 / y tế số |
| **66** | `2026-11-22.md` | Weekly: 1 ưu tiên staging SA-01 tuần tới |
| **67** | `2026-11-23.md` | SA-02: VAS D3 primary; `clin_event` khác SA-01 thế nào? |
| **68** | `2026-11-24.md` | SA-05: 1 bullet EQ gap / missingness PUSH |
| **69** | `2026-11-25.md` | Cross-SA: 1 rủi ro multiplicity nếu mở omics 3 SA |
| **70** | `2026-11-26.md` | 3 bullet còn mở (REDCap · SA-02 · SA-05) → tuần 11 SPIRIT/TT43 |

## Stack nhắc

```text
Site PHI → StudyID → export de-ID → QC → M0–M3 (L2)
L3 X_mol chỉ sau G2 data thật · synthetic ≠ lâm sàng
```

## Checklist DONE (PI)

- [ ] 1 hàng deny/allow hoặc 1 câu SA support trong log  
- [ ] STREAK PREP → **DONE**  
- [ ] Tier 0 còn mở (DM · cờ SA-01) → ưu tiên song song  
- [ ] Goal vẫn ACTIVE · không biospecimen  

## Trước khi vào Ngày 61 (nếu STREAK <3)

Làm xong `PI-SESSION-SCRIPT-STREAK3` / Nat Med → STREAK ≥3 trước khi “nuốt” Q2 PREP.

## Sau Ngày 70

Tuần 11–12 (`curriculum-days-61-90.md` Ngày 71–80): SPIRIT S1–S3 · TT43 · interim **data thật** (không synthetic → G2).

## Cấm

- Pass G2 / order omics vì đã có checklist de-ID  
- Gộp primary SA-01/02/05  
- Đóng Cursor Goal sau staging scaffold
