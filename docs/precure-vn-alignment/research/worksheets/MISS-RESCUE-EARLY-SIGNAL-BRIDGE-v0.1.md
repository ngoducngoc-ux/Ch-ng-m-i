# Bridge — MISS rescue · early-signal (chống quên) · refresh v0.1b

**Mã:** MISS-RESCUE-EARLY-SIGNAL-BRIDGE-v0.1  
**Ngày:** 2026-09-16 (refresh sau PB-EARLY-SIGNAL-LENS / EQ bank CLOSED)  
**Curriculum:** mọi lúc khi bỏ ritual · STREAK thấp · sau STREAK≥3 · bridge **#14**  
**Thẻ:** `BACKLOG-RITUAL-PRIORITY` · `STREAK_TRACKER` · `PI-NEXT-45MIN` · Rotation #12 · `PB-EARLY-SIGNAL-LENS` · `MISS-RESCUE-EQ`  
**Cờ đầu:** SA-01 · Goal **ACTIVE** · L3 **CLOSED** · EQ bank **CLOSED**  
**STREAK&lt;3?** Dừng · **`STREAK3-PACK`** · **`STREAK3-EQ`** · NOW · FILL-AID → tick **19/09** trước (mức **D**)  
**Không:** bỏ STREAK3 vì “đọc rescue” · tick DONE hàng PREP · đóng Goal vì MISS · invent EQ mới · nhảy Ngày 60+ để “bù”

## Vì sao MISS rescue thuộc mục tiêu 12 tháng

| Mục tiêu | Khi MISS | Rescue |
|----------|----------|--------|
| **Ôn hàng ngày** | STREAK đứt | 1 session 45′ khôi phục |
| **Smart A / ES** | Quên ba trụ | Ôn #0 hoặc #13 (1 PB) · **`PB-EARLY-SIGNAL-LENS`** |
| **Y tế số** | Quên de-ID / PHI | #5 hoặc #9 · PB-004 · **`DEID-MISS-EQ`** |
| **Không quên dự án** | MISS≥3/7 | Weekly / quarterly pack · Goal ACTIVE |

Scaffold #0–13 đủ nội dung; **#14** = **khi đứt thì làm gì** — anti-forget vận hành (đúng “không để dự án bị quên”).

## Bậc MISS → việc 45′

| Mức | Điều kiện | Việc PI (1 session) | Artifact |
|-----|-----------|---------------------|----------|
| **A** | MISS 1 ngày | Makeup theo **`DAILY-STACK-AFTER-STREAK3`** (thứ bị miss) **hoặc** STREAK3 nếu STREAK&lt;3 | Daily stack · Rotation · STREAK3 |
| **B** | MISS ≥3 (tuần) | Weekly: 1 PB × lens **#13** + đếm STREAK + 1 ưu tiên tuần | `weekly-review` · **`PB-EARLY-SIGNAL-LENS`** |
| **C** | MISS ≥7 | Quarterly pack + STREAK audit + Goal ACTIVE check | `quarterly-*-prep` · #10/#11 |
| **D** | STREAK &lt;3 mãi | **Bắt buộc** `PI-SESSION-SCRIPT-STREAK3` / **`STREAK3-PACK`** trước rotation | STREAK3 · **`STREAK3-EQ`** · #0 |

## Luồng một trang

```text
Đếm STREAK DONE / MISS gần đây (STREAK_TRACKER)
        ↓
STREAK <3? → D (STREAK3-PACK / STREAK3-EQ / FILL-AID) · dừng rotation
MISS ≥7? → C (quarterly)
MISS ≥3? → B (weekly + #13 PB lens)
MISS 1? → A (makeup #12 / DAILY-STACK)
        ↓ (nếu STREAK ≥3 và phiên đầu)
OPENER → 1×EQ sibling (map) → bridge makeup · không invent EQ
        ↓
1 insight ES / multi-omics / y tế số
Tick DONE chỉ khi PI xong ritual
Goal: ACTIVE · PREP ≠ DONE · G2 CLOSED
```

## Ba câu “không bao giờ” (rescue)

1. **Rescue PREP agent** = STREAK DONE.  
2. **MISS≥7** rồi đóng Goal / bỏ timer.  
3. **Nhảy curriculum Ngày 60+** để “bù” thay vì 1 bridge/ngày · invent EQ mới (bank CLOSED).

## Ritual fill-in

```text
Mức MISS: A|B|C|D
STREAK DONE hiện: __ (vẫn 2 → D / STREAK3 path)
EQ sibling / MISS-RESCUE-EQ kèm (1)? ________
Session hôm nay (1 câu ES / PB / y tế số):
Cặp #13 PB lens nếu mức B? ________
G2: CLOSED
Goal: ACTIVE
PREP → DONE chỉ PI · densify ≠ DONE
```

## Rotation / cặp

- Trước #14 khi STREAK&lt;3: **`STREAK3-PACK`** · **`MISS-RESCUE-EQ-SCIENCE-CARD`** · **`MISS-RESCUE-5MIN`**  
- Sau rescue mức B: **`PB-EARLY-SIGNAL-LENS`** (#13)  
- Hàng ngày sau chuỗi: **`BRIDGE-ROTATION`** (#12)

## Liên kết

`SCIENCE-BRIDGES-INDEX` #14 · **`SCIENCE-BRIDGES-SCIENCE-CARD`** · **`MISS-RESCUE-5MIN-MICRO-DRILL`** · **`MISS-RESCUE-EQ-SCIENCE-CARD`** · **`MISS-RESCUE-EQ-5MIN-MICRO-DRILL`** · **`PB-EARLY-SIGNAL-LENS-BRIDGE`** · **`AFTER-STREAK3-OPENER-1PAGE`** · **`EQ-SIBLING-MAP-SCIENCE-CARD`** · **`STREAK3-EQ-SCIENCE-CARD`** · **`STREAK3-PACK-SCIENCE-CARD`** · `DAILY-STACK-AFTER-STREAK3` · `BACKLOG-RITUAL-PRIORITY` · `STREAK_TRACKER` · `PI-NEXT-45MIN` · `#12` rotation · `#13` PB lens · `#0` Zhou/NatMed · `SCIENCE-CARDS-INDEX` · `rituals/quarterly-review.md`
