# Checklist export de-ID — REDCap SA-01 (pilot)

**Mã:** REDCAP-DEID-EXPORT-v0.1  
**Ngày:** 2026-09-16  
**Phạm vi:** pilot export analysis (L2) · **không** claim lâm sàng · **không** biospecimen  
**Tham chiếu:** PB-004 · `DATA-MANAGER-HANDOFF-REDCap-v0.2.md` · PIPELINE M0–M3 · Q2 Ngày 61–65

## Mục tiêu 1 câu

Một file CSV analysis **không** chứa PII site — đủ schema M0–M3 / `clin_event` để QC, **không** đủ để nhận diện BN ngoài StudyID.

## Lớp dữ liệu (PB-004)

| Lớp | Ví dụ | Được phép rời site? |
|-----|-------|---------------------|
| Identified | Họ tên, SĐT, địa chỉ, hồ sơ viện, chữ ký ICF | **Không** |
| StudyID | `subj_id` (SA-01-XXX) | Có (analysis) |
| Analysis | visit_code · Z lâm sàng · `clin_event` 0–4 · adherence | Có (de-ID) |
| Public | aggregate only | Công bố |

## Cột **cấm** trong export pilot (deny list)

Đánh dấu khi review file trước khi copy ra ngoài site / gửi thống kê / đưa vào sandbox agent:

| # | Loại | Ví dụ field / nội dung | Tick |
|---|------|------------------------|------|
| D1 | Định danh trực tiếp | họ tên, CCCD, SĐT, email, địa chỉ | [ ] |
| D2 | Định danh viện | số bệnh án / MRN / mã BHYT | [ ] |
| D3 | Ngày sinh đầy đủ | DOB (dùng `age` hoặc band tuổi) | [ ] |
| D4 | Free-text nhận diện | note có tên BN / địa điểm cụ thể | [ ] |
| D5 | Media nhận diện | ảnh mặt / ảnh có biển số / watermark tên | [ ] |
| D6 | Consent scan | PDF ICF có chữ ký | [ ] |
| D7 | Omics raw | bất kỳ file assay trước G2 | [ ] **CLOSED** |

## Cột **cho phép** analysis (allow list — SA-01 ES)

Khớp dictionary v0.2 / handoff (điều chỉnh khi DM review):

| Nhóm | Field gợi ý | Ghi chú |
|------|-------------|---------|
| ID nghiên cứu | `subj_id` | StudyID — không map ngược ngoài site |
| Baseline | `age` · `gender` · `group` · `wound_type` · `tbsa_pct` · `wound_site` · comorbid | Age band nếu N nhỏ |
| Visit | `visit_code` · `visit_date` (hoặc day-index) | Prefer relative day vs calendar nếu rủi ro |
| Z sớm | `pct_epith` · `area_open_cm2` · `vas_dress` · culture_* · `clin_infection` | Primary exploratory |
| Sự kiện dọc | `clin_event` · `clin_event_note` (đã scrub) | Zhou 0–4 — xem vignettes |
| Process | `adherence` · `ae_local` · `ae_occur` | PB-008 |
| Outcome | `primary_out` (cửa sổ đúng SAP) | Không dùng làm predictor “early” sai cửa sổ |

**Không import:** form omics / Specimen — G1–G2 gated (`SPEC-SA01-BIO`).

## Quy trình pilot (45′ hoặc cùng DM)

1. [ ] Export từ **staging** REDCap (không production PHI dump)  
2. [ ] Chạy deny list D1–D7 trên header + 5 dòng mẫu  
3. [ ] `python3 …/redcap_import_qc.py path/to/export.csv` (sau `--demo` quen schema)  
4. [ ] Ghi PASS/FAIL + % missing vào log Ngày 61–62  
5. [ ] Xác nhận: PASS QC ≠ bằng chứng BN / ≠ mở G2  

## Liên kết ritual

- **Micro-drill 5′:** `DEID-5MIN-MICRO-DRILL-v0.1.md` (T5/T7 daily stack)  
- Card Q2: `Q2-STAGING-DEID-RITUAL-CARD-v0.1.md`  
- Bridge: `Q2-STAGING-DEID-EARLY-SIGNAL-BRIDGE-v0.1.md`  
- PB-009 L1.4 / L2.1 · Glossary L2  
- Forward DM: `DM-FORWARD-CHECKLIST-v0.1.md`

## Cấm

- Commit CSV có PII vào git  
- Đưa Identified layer vào Drive public / memory agent  
- Coi synthetic sandbox = export thật
