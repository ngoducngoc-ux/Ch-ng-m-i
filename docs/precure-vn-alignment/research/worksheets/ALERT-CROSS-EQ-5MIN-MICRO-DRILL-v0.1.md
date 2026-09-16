# Micro-drill 5′ — ALERT × CROSS × EQ (schema · ladder Z · ≠ Dx / gộp Y)

**Mã:** ALERT-CROSS-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T2 / T4 / T6 / CN** · sau `ALERT-CROSS-5MIN` / `ALERT-EQ-5MIN` / `CROSS-EQ-5MIN` · trước deploy “app cảnh báo chung”  
**Goal:** ACTIVE · ALERT nội bộ · mỗi SA một \(Y\) · ladder trên \(Z\) · L3 CLOSED · PREP ≠ DONE  

## Một câu

> ALERT-CROSS×EQ 5′ = 1 hàng ALERT theo SA + schema \(t^*\)/\(Z\) **và** 1 dòng ladder M0–M3 — không gộp Y · không Dx app · Hawthorne ≠ primary.

## Drill (điền)

```text
SA đang ôn (không gộp): 01 | 02 | 05 — chọn: ________
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________
ALERT hàng (atlas A/B · 1 dòng): ________
t* primary đúng: D21 | VAS_D3 | PUSH_D14 — ghi: ________
1 dòng Z / M0→M3 (không = Y(t*)): ________
ALERT = Dx / gộp Y / Hawthorne = primary? KHÔNG
Cặp đã đụng: ALERT-CROSS | ALERT-EQ | CROSS-EQ | ALERT-HAWTHORNE-EQ | PUSH-ALERT-EQ | LEAK-CROSS — ghi: ________
1 việc nhỏ ≤30′ (atlas / CROSS map / EQ Drill 10′): ________
Đóng Goal / deploy vì ALERT-CROSS×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Thẻ khoa học | **`ALERT-CROSS-EQ-SCIENCE-CARD`** · **`ALERT-CROSS-SCIENCE-CARD`** · `ALERT-SCIENCE-CARD` · `CROSS-SA-SCIENCE-CARD` |
| ALERT×CROSS alone | `ALERT-CROSS-5MIN` · `ALERT-CROSS-SA-ATLAS` |
| ALERT×EQ / CROSS×EQ | `ALERT-EQ-5MIN` · `CROSS-EQ-5MIN` |
| Hawthorne / PUSH pairs | `ALERT-HAWTHORNE-EQ-5MIN` · `PUSH-ALERT-EQ-5MIN` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |

## Cấm

- Deploy ALERT app Dx · gộp endpoint “cảnh báo chung”  
- Coi ALERT/Hawthorne = primary · đóng Goal  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2/T4/T6/CN) · Protocol: `../../rituals/daily-protocol.md`
