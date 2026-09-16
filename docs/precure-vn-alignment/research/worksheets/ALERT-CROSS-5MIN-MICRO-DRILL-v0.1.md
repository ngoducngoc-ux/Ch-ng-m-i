# Micro-drill 5′ — ALERT × CROSS-SA (actionable ≠ Dx · không gộp Y)

**Mã:** ALERT-CROSS-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T2**/ **T4**/ **T6**/ **CN** · sau `ALERT-5MIN` / `ALERT-HAWTHORNE-5MIN` / `CROSS-SA-5MIN` / `CROSS-EQ-5MIN` · trước deploy “app cảnh báo Smart A chung”  
**Goal:** ACTIVE · ALERT nội bộ có cột làm/không làm · ≠ Dx · ≠ primary · mỗi SA một \(Y\) · L3 **CLOSED** · PREP ≠ DONE  

## Một câu

> ALERT×CROSS 5′ = 1 hàng ALERT (A/B) **theo SA** + so schema \(t^*\)/\(Z\) — **không** gộp Y · **không** deploy app Dx · Hawthorne/ALERT ≠ primary endpoint.

## Drill (điền)

```text
SA đang ôn (không gộp): 01 | 02 | 05 — chọn: ________
ALERT hàng hôm nay (atlas A hoặc B · 1 dòng): ________
t* primary đúng: D21 | VAS_D3 | PUSH_D14 — ghi: ________
1 Z sớm / tín hiệu ALERT (không = Y(t*)): ________
ALERT = Dx / app / đổi primary? KHÔNG
Gộp Y SA-01+02+05? KHÔNG — vì: ________
Hawthorne / compliance = primary? KHÔNG
Order omics vì ALERT×CROSS? KHÔNG
Cặp đã đụng: ALERT | ALERT-HAWTHORNE | NATMED-ALERT | PUSH-ALERT | CROSS-SA | CROSS-EQ | LEAK-CROSS — ghi: ________
1 việc nhỏ ≤30′ (ALERT atlas / CROSS map / HAWTHORNE): ________
Đóng Goal / deploy vì ALERT×CROSS? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| ALERT alone | `ALERT-5MIN` · `ALERT-CROSS-SA-ATLAS` · `NATMED-ALERT-5MIN` |
| ALERT×Hawthorne | `ALERT-HAWTHORNE-5MIN` |
| SA-05 pair | `PUSH-ALERT-5MIN` |
| CROSS | `CROSS-SA-5MIN` · `CROSS-EQ-5MIN` · `LEAK-CROSS-5MIN` |

## Cấm

- Deploy ALERT ra app Dx / auto-treat  
- Gộp endpoint / một model “cảnh báo chung”  
- Coi ALERT hoặc Hawthorne = primary / đóng Goal  

## Liên kết

- Atlas: `ALERT-CROSS-SA-ATLAS-v0.1.md` · Map: `CROSS-SA-EARLY-SIGNAL-MAP-v0.1.md`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2/T4/T6/CN) · Protocol: `../../rituals/daily-protocol.md`
