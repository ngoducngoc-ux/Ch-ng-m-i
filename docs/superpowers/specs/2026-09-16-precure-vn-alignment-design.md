# Design — Precure VN Alignment (long-running research habit + project)

**Date:** 2026-09-16  
**Owner:** PGS.TS.BS. Ngô Đức Ngọc  
**Status:** Approved for implementation (user directed: lập dự án lâu dài + lưu lịch; không sơ lơ quên)

## Problem

Tin Precure (Mayo × Thermo Fisher) là tín hiệu chiến lược về multi-omics + lâm sàng dọc + AI cho tín hiệu bệnh sớm. Anh muốn **không chỉ đọc một lần**, mà lập dự án nghiêm túc, neo lịch hàng ngày, đưa vấn đề/phương trình nghiên cứu (Smart A, y tế số) theo hướng đó và giữ lâu dài.

## Goals

1. Có “ngôi nhà” tài liệu lâu dài trong repo (charter, nguồn, ritual, problem bank).
2. Có neo lịch Google lặp (ngày / tuần / quý) để không bị quên.
3. Có Cursor Goal dài hạn song song với lịch.
4. Giữ văn phong khoa học trung tính; ghi nguồn VDHN khi dùng bản tin.

## Non-goals

- Không dựng joint venture / không claim quan hệ đối tác với Mayo/Thermo Fisher.
- Không xây data platform production trong vòng đầu.
- Không lưu PHI/PII bệnh nhân.

## Approaches considered

| Option | Mô tả | Trade-off |
|--------|-------|-----------|
| A. Chỉ calendar reminder | Nhanh | Dễ quên ngữ cảnh khoa học |
| B. Chỉ thư mục tài liệu | Có trí nhớ | Không “đẩy” hàng ngày |
| **C. Charter + rituals + problem bank + calendar + Cursor Goal (chọn)** | Hệ thống giữ dự án sống | Cần 1 lần setup |

## Architecture (vòng đầu)

- `docs/precure-vn-alignment/` — single source of truth trong git.
- Google Calendar primary — recurrence 12 tháng.
- Cursor Goal — objective dài hạn trong agent runtime.
- Daily log files tạo dần khi anh/agent làm ritual.

## Success criteria

- [x] ACTIVE_PROJECT_CARD tồn tại và nêu quy tắc chống quên.
- [x] Nguồn VDHN/Mayo được lưu có cấu trúc.
- [x] Ít nhất 3 series lịch Google đã tạo và xác minh bằng list_events.
- [x] Problem bank có ≥3 câu hỏi gắn SA.
- [x] Cursor Goal đã tạo.
- [x] CI `precure-verify` trên GitHub (verify.sh).
- [x] Curriculum 30 ngày + log PREP + checkpoint tháng 1 (2026-09-16 batch).
- [x] Curriculum 31–60 daily PREP + worksheets + checkpoint 60d draft (2026-09-16).
- [x] Curriculum 61–90 Q2 draft + daily PREP 61–90 + `CURRICULUM-ROADMAP.md` + `PI-ACTIONS-NOW.md`.
- [x] Curriculum 91–120 Q3 outline + `AI-LONGITUDINAL-STACK` + `MULTI-OMICS-GATES-SMART-A` + `CURRICULUM-MONTHS-4-12-OUTLINE.md`.
- [x] `READING-INDEX.md` · EQ-SA02 · PB-009.
- [ ] Ritual DONE ≥20/30 tháng 1 — **PI** (`STREAK_TRACKER.md`).
- [ ] DM review SA-01 v0.2 — **PI/DM**.

## Risks

- Lịch “Công việc” chỉ reader → dùng primary.
- Slot 05:45 có thể lệch thói quen → chỉnh sau khi anh phản hồi 1 lần.
