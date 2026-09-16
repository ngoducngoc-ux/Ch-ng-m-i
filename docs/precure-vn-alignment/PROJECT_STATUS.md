# PROJECT STATUS — Precure VN Alignment

**Cập nhật:** 2026-09-16  
**Goal Cursor:** ACTIVE (không đóng)  
**Cờ đầu khoa học:** SA-01 early-signal  
**Đối chiếu:** SA-05 ICU/PUSH

## Vận hành chống quên

| Thành phần | Trạng thái | Bằng chứng |
|------------|------------|------------|
| ACTIVE_PROJECT_CARD | OK | `ACTIVE_PROJECT_CARD.md` |
| Google Daily/Weekly/Quarterly | OK | calendar series PRECURE |
| Timer `precure-daily-check` | OK (renewed 2026-09-16) | cron 07:30 ICT; lịch remind 22/09 vẫn giữ |
| Drive REDCap CSV | OK | https://drive.google.com/file/d/1gSu-OVLnCOuEpKqNMu4gdtQDmHEd4vFJ/view |
| SA-02 worksheet | OK | `worksheets/EH-SA02-ZX-variables.md` |
| Drive `CURSOR_SYNC_BRIDGE` | OK | hub 00_AI… |
| Cursor rules + AGENTS.md | OK | `.cursor/rules/…`, `AGENTS.md` |
| Streak | 2 DONE | `research/STREAK_TRACKER.md` |
| Curriculum 30 ngày | OK | bắt đầu 17/09 |

## Khoa học / sản phẩm nghiên cứu

| Artifact | Trạng thái |
|----------|------------|
| EH-SA01 + eCRF + SAP ES + BIO gated + alerts + ICF nest | DRAFT sẵn review |
| Sandbox SA-01 M0–M3 synthetic | RAN |
| EH-SA05 worksheet + sandbox M0–M3 | RAN (script mới) |
| PB-001…007 | OPEN |
| Reading notes D02–D03 | PREP |

## Việc mở (ưu tiên)

1. Review / import `worksheets/redcap_sa01_early_signal_dictionary_v0.1.csv` với Data Manager  
2. Ritual Curriculum Ngày 01–02 theo lịch  
3. Renew timer trước 23/09  
4. Weekly 20/09: chọn giữ SA-01 cờ đầu hoặc nâng SA-05  
5. Chạy `research/analysis/verify.sh` khi đổi script phân tích

## Không làm

- Claim chẩn đoán sớm lâm sàng từ synthetic  
- Lấy biospecimen trước cổng G1–G2  
- Đóng goal Cursor khi mới chỉ mới dựng hạ tầng
