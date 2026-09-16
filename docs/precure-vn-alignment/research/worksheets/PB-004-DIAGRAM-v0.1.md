# PB-004 — sơ đồ 1 trang (slide nội bộ)

**Mã:** PB-004-DIAGRAM-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 21 · `worksheets/PB-004-data-architecture.md`

## Sơ đồ (copy slide)

```mermaid
flowchart TB
  subgraph identified [Site — identified]
    BN[Bệnh nhân / hồ sơ viện]
  end
  BN --> StudyID[StudyID SA-xx-NNN]
  StudyID --> Consent[ICF version + nested optional]
  StudyID --> Visit[Visit D0…D21]
  Visit --> REDCap[eCRF REDCap Z AE adherence]
  Visit --> Media[Ảnh / ImageJ]
  Visit --> Spec[Specimen 0..n sau G1 G2]
  Spec --> Assay[Assay X_mol batch]
  REDCap --> Export[Export de-ID]
  Assay --> Export
  Export --> Sandbox[Sandbox verify.sh exploratory]
  Export --> Analysis[Analysis DB stats AI]
  Analysis --> Pub[Aggregate publication only]
```

## Consent tách lớp

| Lớp | Consent |
|-----|---------|
| RCT + \(Z\) dọc | ICF chính |
| Lưu mẫu / omics | ICF nested `ICF-NEST-SA01-v0.1-DRAFT.md` |

## Ranh giới agent / Git

- **Không** PII trong repo · Drive pointer only · xem `y-te-so-precure-bridge-v0.1.md`

## Việc nhỏ

- [x] Sơ đồ 1 trang (file này) — tick worksheet PB-004 khi ritual  
- [ ] PI: export slide PNG nội bộ nếu cần họp Smart A

## Liên kết

- `reading-notes/2026-10-07-pb004-consent-data.md` · problem-bank PB-004
