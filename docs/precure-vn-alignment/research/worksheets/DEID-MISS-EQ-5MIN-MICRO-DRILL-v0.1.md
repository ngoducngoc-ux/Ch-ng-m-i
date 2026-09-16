# Micro-drill 5′ — DEID × MISS × EQ (%miss · deny-list · ladder Z · trước AUROC)

**Mã:** DEID-MISS-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5 / T7** · sau `DEID-MISS-5MIN` / `DEID-EQ-5MIN` / `MISSINGNESS-EQ-5MIN` · trước M0–M3 trên N  
**Goal:** ACTIVE · không PHI · `[chưa N]` nếu demo · ladder chỉ khi miss chấp nhận được · L3 CLOSED · PREP ≠ DONE  

## Một câu

> DEID-MISS×EQ 5′ = deny-list + %miss theo visit **và** 1 dòng ladder M0–M3 — demo/PII risk / miss chưa audit → **không** AUROC; ladder ≠ export đã sạch.

## Drill (điền)

```text
SA neo: 01|02|05 — chọn: ________
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________
N hôm nay: --demo | de-ID thật — ghi: ________
1 field CẤM export: ________ · 1 field CHO PHÉP (Z): ________
Visit / Z: D0|D3|D7 · PCT|CFU|VAS|clin_event — ________
%miss (hoặc [chưa N]): ________
1 dòng Z / M0→M3 (chỉ khi miss OK / [chưa N] ghi CHƯA): ________
Omics raw / PII trong export? KHÔNG
Báo AUROC khi demo / miss chưa audit / PII risk? KHÔNG
Cặp đã đụng: DEID-MISS | DEID-EQ | MISSINGNESS-EQ | PB004-EQ | LEAKAGE-EQ — ghi: ________
1 việc nhỏ ≤30′ (deny-list / L2 audit 1 ô / EQ Drill 10′): ________
Đóng Goal / mở G2 vì DEID-MISS×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| DEID×MISS alone | `DEID-MISS-5MIN` · `DEID-5MIN` · `MISSINGNESS-5MIN` |
| DEID×EQ / MISS×EQ | `DEID-EQ-5MIN` · `MISSINGNESS-EQ-5MIN` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| PB004 / leak | `PB004-EQ-5MIN` · `LEAKAGE-EQ-5MIN` |

## Cấm

- %miss / AUROC giả từ sandbox như N thật  
- Train M early khi miss D0–D7 chưa audit · mở G2 vì QC demo  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5/T7) · Protocol: `../../rituals/daily-protocol.md`  
- Checklist: `REDCAP-DEID-EXPORT-CHECKLIST`
