# Cursor sync — Precure VN Alignment (laptop + desktop)

Khi mở repo này trên **laptop hoặc desktop**, agent phải:

1. Đọc `docs/precure-vn-alignment/ACTIVE_PROJECT_CARD.md` trước mọi việc liên quan Precure / early signal / multi-omics.
2. Tôn trọng ritual ngày/tuần và problem bank; không để dự án bị quên.
3. Đồng bộ hub Drive: thư mục `00_AI_TRUNG_TAM_DIEU_HANH/CURSOR_SYNC_BRIDGE/` (Google Drive của ngoducngoc@gmail.com).
4. Nguồn tin Precure khi trích dẫn: **Mạng lưới Y tế Số Việt Nam — Vietnam Digital Health Network**.
5. Không lưu secrets / PHI / hồ sơ BN định danh.

## Source of truth

| Lớp | Nơi | Vai trò |
|-----|-----|---------|
| GitHub | `ngoducngoc-ux/Ch-ng-m-i` branch/PR Precure | Chi tiết tài liệu + log |
| Drive hub | `00_AI_TRUNG_TAM_DIEU_HANH/CURSOR_SYNC_BRIDGE` | Pointer nhanh cho mọi máy |
| Calendar | Google primary | Nhắc hàng ngày / tuần / quý |
| Cursor Goal | Cloud agent goal | Mục tiêu dài hạn runtime |

## Lệnh nhanh trên máy local

```bash
git fetch origin
git checkout cursor/precure-vn-alignment-729d   # hoặc main sau khi merge
git pull
```

Mở folder repo trong Cursor Desktop — rules trong `.cursor/rules/` sẽ được nạp.

## Pointer Git (cập nhật 2026-09-16)

| Chủ đề | Path trong repo |
|--------|-----------------|
| Hub 1 trang | `docs/precure-vn-alignment/INDEX.md` |
| **Ritual handoff PI** | `research/RITUAL-HANDOFF-INDEX.md` |
| Tier 1 / Tier 2 | `TIER-1-7DAY-HANDOFF.md` · `TIER-2-30DAY-HANDOFF.md` |
| DM forward | `research/worksheets/DM-FORWARD-CHECKLIST-v0.1.md` |
| Omics gates G2 | `research/worksheets/G2-READINESS-v0.1.md` |
| PEA pre-analytic | `research/worksheets/PRE-ANALYTIC-PEA-SA01-v0.1.md` |
| SA-05 PUSH | `research/worksheets/PUSH-SA05-COMPONENTS-v0.1.md` |
| SA-05 EQ gap | `research/worksheets/EQ-EH-SA05-GAP-v0.1.md` |
| SA-02 VAS scale | `research/worksheets/VAS-SCALE-HARMONIZE-SA02-v0.1.md` |
| SA-03 biofilm | `research/worksheets/SA03-BIOFILM-TRANSLATION-v0.1.md` |
| SA-04 ISO swab | `research/worksheets/ISO-SWAB-CONTACT-PRIORITY-v0.1.md` |
| SPIRIT / nested G1 | `research/worksheets/SPIRIT-SA01-MAP-v0.1.md` · `SPIRIT-NESTED-G1-CHECKLIST-v0.1.md` |
| CONSORT exploratory | `research/worksheets/CONSORT-ES-PLACEMENT-v0.1.md` |
| TT43 amendment | `research/worksheets/TT43-AMENDMENT-HOOKS-v0.1.md` |
| PB-004 diagram | `research/worksheets/PB-004-DIAGRAM-v0.1.md` |
| Media vs Smart A | `research/worksheets/MEDIA-SMART-A-CLAIMS-v0.1.md` |
| Month-1 checkpoint | `research/checkpoints/MONTH-1-2026-10-16.md` |
| PI ưu tiên | `PI-ACTIONS-NOW.md` |
| PREP ≠ DONE | `research/RITUAL-DONE-vs-PREP.md` |
| Catch-up backlog | `research/BACKLOG-RITUAL-PRIORITY-v0.1.md` |
| Roadmap Ngày 1–120 | `research/CURRICULUM-ROADMAP.md` |
| AI / omics stack | `research/guides/AI-LONGITUDINAL-STACK-v0.1.md` · `MULTI-OMICS-GATES-SMART-A-v0.1.md` |
| Reading DOIs | `research/reading-notes/READING-INDEX.md` |
| Checkpoint 60 ngày | `research/checkpoints/MONTH-2-60D-2026-11-15.md` |
| Q2 / Q3 / Year-1 | `curriculum-days-61-90.md` · `91-120.md` · `checkpoints/YEAR-1-REVIEW-TEMPLATE.md` |
| Worksheet index | `research/worksheets/WORKSHEET-INDEX.md` |
| Verify + QC demo | `research/analysis/verify.sh` · `redcap_import_qc.py --demo` · `RUNBOOK-v0.1.md` |

*(Drive hub: copy full pointer từ `PRECURE-DRIVE-HUB-POINTER.md`.)*
