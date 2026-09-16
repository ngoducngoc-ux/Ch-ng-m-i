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
| `precure-daily-check` | `30 0 * * *` | 07:30 | Renew 2026-09-16 · `sub_69eee79b-…` · expires ~2026-09-23 · L1L2L3-SHIFT in prompt |

Prompt: `RITUAL-HANDOFF-INDEX` · `PI-NEXT-45MIN` · STREAK · không đóng goal.

**Google series description đã cập nhật 2026-09-16 (anti-forget densify):** Daily/Weekly → **`STREAK3-5MIN`** · **`DAILY-STACK`** · PITFALLS/GLOSSARY/CROSS-SA/OMICS-GATES/AI-STACK/YTESO/TRANSLATION · `#13`/`#14` · PREP≠DONE.  
**Email PI:** Outlook → ngoducngoc@gmail.com 2026-09-16 (STREAK≥3 reminder + densify bank + hub pointers).

## Quy tắc sửa lịch

- Đổi giờ chỉ khi anh chốt slot mới; cập nhật file này trước khi sửa series.
- Không xóa series khi bận ngắn hạn — dùng skip từng ngày + makeup.
