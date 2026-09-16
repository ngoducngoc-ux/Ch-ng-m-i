# PROJECT STATUS — Precure VN Alignment

**Cập nhật:** 2026-09-16 (PUSH SA-05 Ngày 08 · timer renew ×3 · verify PASS)
**Goal Cursor:** ACTIVE (không đóng)  
**Cờ đầu khoa học:** SA-01 early-signal  
**Đối chiếu:** SA-05 ICU/PUSH · SA-02 VAS · SA-03/04 cổng

## Vận hành chống quên

| Thành phần | Trạng thái | Bằng chứng |
|------------|------------|------------|
| Email handoff | SENT | Outlook → ngoducngoc@gmail.com 2026-09-16 |
| Weekly pack 20/09 | OK | `rituals/weekly-2026-09-20.md` |
| ACTIVE_PROJECT_CARD | OK | `ACTIVE_PROJECT_CARD.md` |
| Google Daily/Weekly/Quarterly | OK | calendar series PRECURE |
| Timer `precure-daily-check` | OK (renewed 2026-09-16 ×3) | 07:30 ICT · xem `list_subscriptions` |
| REDCap index (SA-01/02/05) | OK | `worksheets/DATA-MANAGER-REDCap-INDEX.md` |
| Drive REDCap CSV | OK v0.2 | v0.1 [Drive](https://drive.google.com/file/d/1gSu-OVLnCOuEpKqNMu4gdtQDmHEd4vFJ/view) · v0.2 [Drive](https://drive.google.com/file/d/1EnHP9GfGJEnDt-qs-eTbH8VayclX4gfH/view) |
| Drive `CURSOR_SYNC_BRIDGE` | OK | hub 00_AI… |
| Cursor rules + AGENTS.md | OK | `.cursor/rules/…`, `AGENTS.md` |
| Streak | 2 DONE + PREP 18–25 | `research/STREAK_TRACKER.md` |
| Decision cờ đầu | PROPOSED SA-01 | `research/decisions/DECISION-FLAGSHIP-SA01-2026-09-20.md` |
| Email DM | OK | `worksheets/DM-EMAIL-TEMPLATE-v0.1.md` · checklist `DM-FORWARD-CHECKLIST-v0.1.md` |
| Weekly pack 27/09 | OK | `rituals/weekly-2026-09-27.md` |
| Export pipeline | OK | `research/analysis/REDCap-to-M0-M3-PIPELINE-v0.1.md` + `redcap_import_qc.py` |
| CI `precure-verify` | **SUCCESS** | [PR #2 checks](https://github.com/ngoducngoc-ux/Ch-ng-m-i/pull/2) · `.github/workflows/precure-verify.yml` |
| Curriculum 30 ngày | OK | log PREP 17/09→16/10 · `INDEX.md` |

## Khoa học / sản phẩm nghiên cứu

| Artifact | Trạng thái |
|----------|------------|
| EH-SA01 + eCRF + SAP ES + BIO gated + alerts + ICF nest | DRAFT sẵn review |
| EH-SA02 VAS + DESIGN-SA01 longitudinal | DRAFT 2026-09-16 |
| ALERT-SA05 ICU | DRAFT |
| DM handoff REDCap v0.2 | READY | `worksheets/DATA-MANAGER-HANDOFF-REDCap-v0.2.md` |
| Sandbox SA-01 / SA-02 / SA-05 synthetic | RAN + verify.sh PASS |
| Worksheets SA-02/03/04/05 | OK |
| PB-001…008 | OPEN |
| Reading notes D02–D03 | PREP |
| Reading notes D12–D14 (VAS/biofilm/ISO) | PREP |
| GAP SA-01 eCRF v0.2 | OK | `worksheets/GAP-SA01-eCRF-alignment-v0.1.md` |
| Month-1 checkpoint | PREP + snapshot 2026-09-16 | `research/checkpoints/MONTH-1-2026-10-16.md` |
| Curriculum 31–60 | DRAFT tuần 5–6 | `research/curriculum-days-31-60.md` |
| Weekly pack 22/10 | OK | `rituals/weekly-2026-10-22.md` |
| Daily PREP 31–40 | OK | log 2026-10-17 … 2026-10-26 |
| SA-02 eCRF + SAP ES + ALERT | DRAFT |
| SA-05 eCRF + SAP ES + ALERT | DRAFT |
| Y tế số bridge | `research/y-te-so-precure-bridge-v0.1.md` |
| Quarterly ritual | `rituals/quarterly-review.md` |
| Reading notes D05–D07 (PEA/G2) | PREP + worksheets |
| Reading notes D08 (PUSH SA-05) | PREP + `PUSH-SA05-COMPONENTS-v0.1.md` |
| Reading notes D09 (EQ SA-05) | PREP + `EQ-EH-SA05-GAP-v0.1.md` |
| Reading notes D12 (VAS SA-02) | PREP + `VAS-SCALE-HARMONIZE-SA02-v0.1.md` |
| Ngày 10 EQ-SA01 + GAP | PREP + QC demo PASS |
| Tuần 3 SPIRIT (Ngày 15–16) | PREP + `SPIRIT-SA01-MAP` · `SPIRIT-NESTED-G1-CHECKLIST` |
| Tuần 3 CONSORT/TT43/PB-004 | PREP + placement/TT43 hooks/diagram worksheets |

## Việc mở (ưu tiên)

1. Ritual daily theo `curriculum-30-days.md` + `STREAK_TRACKER.md`  
2. Data Manager review REDCap SA-01 **v0.2**  
3. Weekly 20/09 · Quarterly checklist sẵn  
4. Không biospecimen trước cổng G1–G2  

## Không làm

- Claim chẩn đoán sớm lâm sàng từ synthetic  
- Lấy biospecimen trước cổng G1–G2  
- Đóng goal Cursor khi mới chỉ mới dựng hạ tầng
