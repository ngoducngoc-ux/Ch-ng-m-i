# Micro-drill 5′ — Backlog ritual priority (Tier 0→4 · PREP ≠ DONE)

**Mã:** BACKLOG-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** STREAK thấp · nhiều PREP · sau MISS rescue · trước khi đòi scaffold thêm · CN catch-up  
**Goal:** ACTIVE · chỉ **PI** tick DONE · tối đa **1 DONE/ngày lịch** · L3 **CLOSED** · G2 **CLOSED**  
**Nguồn:** `BACKLOG-RITUAL-PRIORITY` · `RITUAL-DONE-vs-PREP`

## Một câu

> BACKLOG 5′ = chọn **đúng 1** hàng Tier 0→1 (không nhảy Tier 4) rồi mở file ritual tương ứng — tick DONE chỉ khi PI đọc xong; PREP agent không đếm.

## Drill (điền)

```text
STREAK DONE hiện: ________ (cần ≥3 trước DAILY-STACK bền)
Số hàng PREP đang “chờ tick”: ________
Tier hôm nay: 0 (PI-ACTIONS) | 1 (Ngày 02–14) | 2 (15–30) | 3 (31–60) | 4 (61–120 — chỉ sau pass) — chọn: ________
1 hàng cụ thể (Ngày N / DOI / card): ________
File mở ngay: PI-ACTIONS-NOW | Zhou bridge | NatMed+ALERT | PEA card | Endpoints | STREAK3 — ghi: ________
Nhảy Tier 4 / Ngày 91+ vì “bù PREP”? KHÔNG
Agent tick DONE thay PI? KHÔNG
verify.sh / CI = STREAK DONE? KHÔNG
1 việc ≤45′ hôm nay: ________
Đóng Goal vì backlog scaffold đủ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Tier | Việc PI (1 session) | Artifact |
|------|---------------------|----------|
| **0** | PI-ACTIONS · không mở G2 biospecimen | `PI-ACTIONS-NOW` |
| **1** | Zhou → NatMed/ALERT → PEA → endpoints → VAS/ISO | `BACKLOG-RITUAL-PRIORITY` · Tier1 handoff |
| **2** | SPIRIT…TRIPOD…PB-004…Ngày 30 | `DESIGN-YTESO-AI-RITUAL-CARD` |
| **3** | Sau pass tháng 1 | `TIER3-INTERIM-G2-RITUAL-CARD` |
| **4** | Chỉ sau 60d/Q2 pass | Q2/Q3 cards · **không** đọc 120 ngày thay ritual |
| STREAK&lt;3 | Dừng backlog deep · STREAK3 trước | `STREAK3-5MIN` · `MISS-RESCUE-5MIN` |
| BACKLOG×EQ | **`BACKLOG-EQ-5MIN`** · Tier 0→1 · ladder sau pass | `STREAK3-EQ-5MIN` |

## Cấm

- Tick DONE hàng PREP chưa đọc  
- Nhảy Ngày 60+/91+ để “quét scaffold”  
- Mở G2 biospecimen từ backlog drill  

## Liên kết

- Backlog: `../BACKLOG-RITUAL-PRIORITY-v0.1.md` · PREP≠DONE: `../RITUAL-DONE-vs-PREP.md`  
- MISS: **`MISS-RESCUE-5MIN-MICRO-DRILL`** · STREAK3: **`STREAK3-5MIN-MICRO-DRILL`**  
- Daily stack: `DAILY-STACK-AFTER-STREAK3` · Protocol: `../../rituals/daily-protocol.md`  
- PI: `../../PI-NEXT-45MIN.md` · Tracker: `../STREAK_TRACKER.md`
