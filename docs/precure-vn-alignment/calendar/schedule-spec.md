# Calendar schedule spec — Precure VN Alignment

**Timezone:** Asia/Ho_Chi_Minh  
**Calendar:** `ngoducngoc@gmail.com` (primary; lịch “Công việc” hiện chỉ reader nên không ghi được)  
**Tạo ngày:** 2026-09-16

## Series A — Daily focus (lặp dài hạn)

| Trường | Giá trị |
|--------|---------|
| Title | `[PRECURE] Daily 45′ — tài liệu + problem bank` |
| Start | 05:45 |
| End | 06:30 |
| Recurrence | `RRULE:FREQ=DAILY;UNTIL=20270916T000000Z` (~12 tháng) |
| Reminders | popup 10′ trước; popup lúc bắt đầu |
| Availability | BUSY / FOCUS nếu hỗ trợ |
| Body | STREAK&lt;3: **`STREAK3-5MIN`** → `PI-SESSION-SCRIPT-STREAK3` · STREAK≥3: **`DAILY-STACK-AFTER-STREAK3`** · densify PITFALLS/GLOSSARY/CROSS-SA/OMICS-GATES/AI-STACK/YTESO/TRANSLATION · `#13`/`#14` · PREP≠DONE |

## Series B — Weekly review

| Trường | Giá trị |
|--------|---------|
| Title | `[PRECURE] Weekly review — không để quên dự án` |
| Start | Chủ nhật 20:00 |
| End | 20:45 |
| Recurrence | `RRULE:FREQ=WEEKLY;BYDAY=SU;UNTIL=20270916T000000Z` |
| Reminders | popup 30′ trước |

## Series C — Quarterly checkpoint

| Trường | Giá trị |
|--------|---------|
| Title | `[PRECURE] Quarterly checkpoint — Smart A × early signal` |
| Start | 14:00 |
| End | 16:00 |
| Recurrence | `RRULE:FREQ=MONTHLY;INTERVAL=3;BYMONTHDAY=16;UNTIL=20270916T000000Z` |
| First instance | 2026-12-16 |

## Kickoff (một lần)

| Title | `[PRECURE] Kickoff — mở dự án lâu dài` |
| Start | 2026-09-16 21:00 |
| End | 2026-09-16 21:45 |
| Google event id | `538i4a3kiua2m19fuf6un782kc` |
| Outlook | đã mirror cùng giờ (Outlook MCP không hỗ trợ RRULE dài hạn) |

## Event IDs đã tạo (Google primary)

| Series | Event ID |
|--------|----------|
| Daily | `uen2htu2leiia6rjng4rjj3rq0` |
| Weekly | `imkur6nj9ubjg6kkg3k18cup1s` |
| Quarterly | `68lfmoo3nmppcskn5e8husvf88` |
| Kickoff | `538i4a3kiua2m19fuf6un782kc` |

## Cloud Agent timer

| Name | Cron (UTC) | Local ICT | Subscription |
|------|------------|-----------|--------------|
| `precure-daily-check` | `30 0 * * *` | 07:30 | Renew 2026-09-16 · `sub_69e3738e-d341-454d-b434-4a4654aed089` · tip → TRIPOD-EQ + NatMed if STREAK&lt;3 |

Prompt: `RITUAL-HANDOFF-INDEX` · `PI-NEXT-45MIN` · STREAK · không đóng goal.

**Google series description đã cập nhật 2026-09-16 (anti-forget densify):** Daily/Weekly → **`PB008-EQ-SCIENCE-CARD`** · **`PB007-EQ-SCIENCE-CARD`** · **`PB003-EQ-SCIENCE-CARD`** · **`PB002-EQ-SCIENCE-CARD`** · **`PB001-EQ-SCIENCE-CARD`** · **`GLOSSARY-EQ-SCIENCE-CARD`** · **`CROSS-EQ-SCIENCE-CARD`** · **`IMAGEJ-EQ-SCIENCE-CARD`** · **`LEAKAGE-EQ-SCIENCE-CARD`** · **`CLIN_EVENT-EQ-SCIENCE-CARD`** · **`PUSH-EQ-SCIENCE-CARD`** · **`VAS-EQ-SCIENCE-CARD`** · **`EPI-EQ-SCIENCE-CARD`** · **`ALERT-EQ-SCIENCE-CARD`** · **`MEDIA-EQ-SCIENCE-CARD`** · **`HAWTHORNE-EQ-SCIENCE-CARD`** · **`SHIFT-EQ-SCIENCE-CARD`** · **`BACKLOG-EQ-SCIENCE-CARD`** · **`MISS-RESCUE-EQ-SCIENCE-CARD`** · **`DEID-MISS-EQ-SCIENCE-CARD`** · **`VAS-LEAK-EQ-SCIENCE-CARD`** · **`IMAGEJ-EPI-EQ-SCIENCE-CARD`** · **`PUSH-ALERT-EQ-SCIENCE-CARD`** · **`ALERT-HAWTHORNE-EQ-SCIENCE-CARD`** · **`NATMED-ALERT-EQ-SCIENCE-CARD`** · **`ALERT-CROSS-EQ-SCIENCE-CARD`** · **`SHIFT-PB007-EQ-SCIENCE-CARD`** · **`L1L2L3-SHIFT-EQ-SCIENCE-CARD`** · **`MEDIA-SHIFT-EQ-SCIENCE-CARD`** · **`CONSORT-SPIRIT-EQ-SCIENCE-CARD`** · **`LEAK-CROSS-EQ-SCIENCE-CARD`** · **`PITFALLS-EQ-SCIENCE-CARD`** · **`TRIPOD-SYNTH-EQ-SCIENCE-CARD`** · **`SYNTH-EQ-SCIENCE-CARD`** · **`TRANSLATION-EQ-SCIENCE-CARD`** · **`PB006-EQ-SCIENCE-CARD`** · **`PB005-EQ-SCIENCE-CARD`** · **`BN-VISIT-EQ-SCIENCE-CARD`** · **`PB004-EQ-SCIENCE-CARD`** · **`YTESO-EQ-SCIENCE-CARD`** · **`CLIN-BN-EQ-SCIENCE-CARD`** · **`AI-STACK-EQ-SCIENCE-CARD`** · **`L1L2L3-EQ-SCIENCE-CARD`** · **`PB009-EQ-SCIENCE-CARD`** · **`OMICS-GATES-EQ-SCIENCE-CARD`** · **`G2-EQ-SCIENCE-CARD`** · **`OMICS-IF-EQ-SCIENCE-CARD`** · **`INTERIM-G2-EQ-SCIENCE-CARD`** · **`PEA-PANEL-EQ-SCIENCE-CARD`** · **`PREANALYTIC-EQ-SCIENCE-CARD`** · **`PEA-EQ-SCIENCE-CARD`** · **`MISSINGNESS-EQ-SCIENCE-CARD`** · **`ISO-SWAB-EQ-SCIENCE-CARD`** · **`DEID-EQ-SCIENCE-CARD`** · **`SPIRIT-G1-EQ-SCIENCE-CARD`** · **`CONSORT-EQ-SCIENCE-CARD`** · **`SPIRIT-EQ-SCIENCE-CARD`** · **`TT43-EQ-SCIENCE-CARD`** · **`AMENDMENT-EQ-SCIENCE-CARD`** · **`SAP-EQ-SCIENCE-CARD`** · **`ICF-EQ-SCIENCE-CARD`** · **`TT43-AMEND-SCIENCE-CARD`** · **`L1L2L3-SHIFT-SCIENCE-CARD`** · **`SHIFT-PB007-SCIENCE-CARD`** · **`CONSORT-SPIRIT-SCIENCE-CARD`** · **`TRIPOD-SYNTH-SCIENCE-CARD`** · **`MEDIA-SHIFT-SCIENCE-CARD`** · **`NATMED-ALERT-SCIENCE-CARD`** · **`ALERT-CROSS-SCIENCE-CARD`** · **`LEAK-CROSS-SCIENCE-CARD`** · **`ALERT-HAWTHORNE-SCIENCE-CARD`** · **`DEID-MISS-SCIENCE-CARD`** · **`VAS-LEAK-SCIENCE-CARD`** · **`CLIN-BN-SCIENCE-CARD`** · **`IMAGEJ-EPI-SCIENCE-CARD`** · **`PUSH-ALERT-SCIENCE-CARD`** · **`EQ05-M0M3-SCIENCE-CARD`** · **`EQ02-M0M3-SCIENCE-CARD`** · **`EQ-M0M3-SCIENCE-CARD`** · **`EQ-SIBLING-MAP-SCIENCE-CARD`** · **`STREAK3-EQ-5MIN-SCIENCE-CARD`** · **`STREAK3-5MIN-SCIENCE-CARD`** · **`STREAK3-FILL-AID-SCIENCE-CARD`** · **`STREAK3-NOW-SCIENCE-CARD`** · **`PI-SESSION-SCRIPT-STREAK3-SCIENCE-CARD`** · **`RITUAL-DONE-vs-PREP-SCIENCE-CARD`** · **`SHIFT-PRESS-SCIENCE-CARD`** · **`GLOSSARY-PRESS-SCIENCE-CARD`** · **`MEDIA-BOUND-SCIENCE-CARD`** · **`SCIENCE-BRIDGES-SCIENCE-CARD`** · **`STREAK3-PACK-SCIENCE-CARD`** · **`PB008-SCIENCE-CARD`** · **`PB009-SCIENCE-CARD`** · **`PB007-SCIENCE-CARD`** · **`PB003-SCIENCE-CARD`** · **`PB002-SCIENCE-CARD`** · **`PB001-SCIENCE-CARD`** · **`PB005-SCIENCE-CARD`** · **`PB006-SCIENCE-CARD`** · **`SPIRIT-SCIENCE-CARD`** · **`TRANSLATION-SCIENCE-CARD`** · **`CROSS-SA-SCIENCE-CARD`** · **`GLOSSARY-SCIENCE-CARD`** · **`EPI-SCIENCE-CARD`** · **`OMICS-IF-SCIENCE-CARD`** · **`INTERIM-G2-SCIENCE-CARD`** · **`IMAGEJ-SCIENCE-CARD`** · **`PEA-PANEL-SCIENCE-CARD`** · **`PITFALLS-SCIENCE-CARD`** · **`PREANALYTIC-SCIENCE-CARD`** · **`ISO-SWAB-SCIENCE-CARD`** · **`SAP-ES-SCIENCE-CARD`** · **`CONSORT-SCIENCE-CARD`** · **`TT43-SCIENCE-CARD`** · **`AMENDMENT-ES-SCIENCE-CARD`** · **`SPIRIT-G1-SCIENCE-CARD`** · **`TRIPOD-SCIENCE-CARD`** · **`ICF-NEST-SCIENCE-CARD`** · **`MISSINGNESS-SCIENCE-CARD`** · **`MEDIA-SCIENCE-CARD`** · **`PB004-SCIENCE-CARD`** · **`BN-VISIT-SCIENCE-CARD`** · **`HAWTHORNE-SCIENCE-CARD`** · **`DEID-SCIENCE-CARD`** · **`AI-STACK-SCIENCE-CARD`** · **`OMICS-GATES-SCIENCE-CARD`** · **`SYNTH-SCIENCE-CARD`** · **`SHIFT-SCIENCE-CARD`** · **`G2-SCIENCE-CARD`** · **`EQ-SCIENCE-CARD`** · **`L1L2L3-SCIENCE-CARD`** · **`CLIN_EVENT-SCIENCE-CARD`** · **`ALERT-SCIENCE-CARD`** · **`NATMED-STREAK3-SCIENCE-CARD`** · **`STREAK3-FILL-AID`** · PREP≠DONE.  
**Email PI:** Outlook → ngoducngoc@gmail.com 2026-09-16 ×128 (BACKLOG-EQ · MISS-RESCUE-EQ · NatMed · STREAK&lt;3 path).

## Quy tắc sửa lịch

- Đổi giờ chỉ khi anh chốt slot mới; cập nhật file này trước khi sửa series.
- Không xóa series khi bận ngắn hạn — dùng skip từng ngày + makeup.
