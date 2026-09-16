# Bridge — MISS rescue · early-signal (chống quên)

**Mã:** MISS-RESCUE-EARLY-SIGNAL-BRIDGE-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** mọi lúc khi bỏ ritual · STREAK thấp · sau STREAK≥3  
**Thẻ:** `BACKLOG-RITUAL-PRIORITY` · `STREAK_TRACKER` · `PI-NEXT-45MIN` · Rotation #12  
**Cờ đầu:** SA-01 · Goal **ACTIVE** · L3 **CLOSED**  
**Không:** bỏ STREAK3 vì “đọc rescue” · tick DONE hàng PREP · đóng Goal vì MISS

## Vì sao MISS rescue thuộc mục tiêu 12 tháng

| Mục tiêu | Khi MISS | Rescue |
|----------|----------|--------|
| **Ôn hàng ngày** | STREAK đứt | 1 session 45′ khôi phục |
| **Smart A / ES** | Quên ba trụ | Ôn #0 hoặc #13 (1 PB) |
| **Y tế số** | Quên de-ID / PHI | #5 hoặc #9 · PB-004 |
| **Không quên dự án** | MISS≥3/7 | Weekly / quarterly pack |

Scaffold #0–13 đủ nội dung; **#14** = **khi đứt thì làm gì** — anti-forget vận hành.

## Bậc MISS → việc 45′

| Mức | Điều kiện | Việc PI (1 session) | Artifact |
|-----|-----------|---------------------|----------|
| **A** | MISS 1 ngày | Makeup theo **`DAILY-STACK-AFTER-STREAK3`** (thứ bị miss) hoặc STREAK3 nếu STREAK&lt;3 | Daily stack · Rotation · STREAK3 |
| **B** | MISS ≥3 (tuần) | Weekly: 1 PB × lens #13 + đếm STREAK + 1 ưu tiên tuần | `weekly-review` · #13 |
| **C** | MISS ≥7 | Quarterly pack + STREAK audit + Goal ACTIVE check | `quarterly-*-prep` · #10/#11 |
| **D** | STREAK &lt;3 mãi | **Bắt buộc** `PI-SESSION-SCRIPT-STREAK3` trước rotation | STREAK3 · #0 |

## Luồng một trang

```text
Đếm STREAK DONE / MISS gần đây (STREAK_TRACKER)
        ↓
STREAK <3? → D (STREAK3) · dừng
MISS ≥7? → C (quarterly)
MISS ≥3? → B (weekly + #13)
MISS 1? → A (makeup #12)
        ↓
1 insight ES / multi-omics / y tế số
Tick DONE chỉ khi PI xong ritual
Goal: ACTIVE
```

## Ba câu “không bao giờ” (rescue)

1. **Rescue PREP agent** = STREAK DONE.  
2. **MISS≥7** rồi đóng Goal / bỏ timer.  
3. **Nhảy curriculum Ngày 60+** để “bù” thay vì 1 bridge/ngày.

## Ritual fill-in

```text
Mức MISS: A|B|C|D
STREAK DONE hiện: __
Session hôm nay (1 câu ES / PB / y tế số):
G2: CLOSED
Goal: ACTIVE
PREP → DONE chỉ PI
```

## Liên kết

- `SCIENCE-BRIDGES-INDEX` #14  
- `DAILY-STACK-AFTER-STREAK3-v0.1.md` · `BACKLOG-RITUAL-PRIORITY` · `STREAK_TRACKER` · `PI-NEXT-45MIN`  
- `#12` rotation · `#13` PB lens · `#0` Zhou/NatMed  
- Quarterly: `rituals/quarterly-review.md`
