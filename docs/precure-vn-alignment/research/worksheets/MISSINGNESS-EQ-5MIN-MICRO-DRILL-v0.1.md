# Micro-drill 5′ — MISSINGNESS × EQ (%miss · ladder Z · trước AUROC)

**Mã:** MISSINGNESS-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5** · sau `MISSINGNESS-5MIN` / `DEID-MISS-5MIN` / `EQ-M0M3-5MIN` / `DEID-EQ-5MIN` · trước AUROC / M0–M3 trên N  
**Goal:** ACTIVE · `[chưa N]` nếu chỉ `--demo` · M0–M3 chỉ khi miss audit · L3 CLOSED · PREP ≠ DONE  

## Một câu

> MISSINGNESS×EQ 5′ = %miss theo visit **và** 1 dòng ladder M0–M3 — `--demo` xanh ≠ missingness lâm sàng; không báo AUROC khi miss cao / demo.

## Drill (điền)

```text
N hôm nay: --demo | de-ID thật (site) — ghi: ________
EQ sibling: EQ-M0M3 | EQ02 | EQ05 — chọn: ________
Visit ôn: D0 | D3 | D7 · 1 Z: PCT|CFU|VAS|clin_event — ________
%miss (hoặc [chưa N]): ________
1 dòng Z / M0→M3 (chỉ khi miss chấp nhận được / [chưa N] ghi CHƯA): ________
Window D3 = bắt buộc | D1–D3 | [CẦN XÁC NHẬN DM]
QC gate redcap_import_qc / deny-list? CÓ | CHƯA
Báo AUROC khi miss cao / demo? KHÔNG
Cặp đã đụng: MISSINGNESS | DEID-MISS | DEID-EQ | LEAKAGE-EQ | TRIPOD-EQ | SYNTH-EQ — ghi: ________
1 việc nhỏ ≤30′ (L2 audit 1 ô / EQ Drill 10′): ________
Đóng Goal / mở G2 vì demo PASS? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| MISSINGNESS alone | `MISSINGNESS-5MIN` · `L2-MISSINGNESS-AUDIT` |
| De-ID×MISS / EQ | `DEID-MISS-5MIN` · `DEID-EQ-5MIN` |
| DEID-MISS×EQ | **`DEID-MISS-EQ-5MIN`** · `DEID-MISS-5MIN` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| Leak / TRIPOD | `LEAKAGE-EQ-5MIN` · `TRIPOD-EQ-5MIN` |
| Q3 L2 | `Q3-L2-EXPORT-EARLY-SIGNAL-BRIDGE` |
| PITFALLS×EQ | **`PITFALLS-EQ-5MIN`** · `PITFALLS-5MIN` |

## Cấm

- %miss giả từ sandbox như N thật  
- Train M early khi miss D0–D7 chưa audit · mở G2 vì QC demo PASS  

## Liên kết

- **Thẻ khoa học:** **`MISSINGNESS-EQ-SCIENCE-CARD`** · **`MISSINGNESS-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5) · Protocol: `../../rituals/daily-protocol.md`  
- Ritual: `Q3-L2-EXPORT-RITUAL-CARD`
