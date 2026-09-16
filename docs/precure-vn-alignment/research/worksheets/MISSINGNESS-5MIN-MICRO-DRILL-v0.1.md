# Micro-drill 5′ — L2 missingness / visit window (trước claim AI)

**Mã:** MISSINGNESS-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5** · Q3 #8 · sau `DEID-5MIN` · trước AUROC / M0–M3 trên N  
**Goal:** ACTIVE · `[chưa N]` nếu chỉ `--demo` · synthetic ≠ BN · L3 CLOSED · PREP ≠ DONE

## Một câu

> Trước claim early-signal trên L2 — biết **% miss theo visit** và **window D3** đã rõ chưa; `--demo` xanh ≠ missingness lâm sàng.

## Drill (điền)

```text
N hôm nay: --demo | de-ID thật (site) — ghi: ________
Visit ôn: D0 | D3 | D7 · 1 Z: PCT|CFU|VAS|clin_event
%miss (hoặc [chưa N]): ________
Window D3 = bắt buộc | D1–D3 | [CẦN XÁC NHẬN DM]
QC gate: redcap_import_qc PASS? CÓ | CHƯA · deny-list skim? CÓ | CHƯA
Báo AUROC khi miss cao / demo? KHÔNG — vì: ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Audit đầy đủ | `L2-MISSINGNESS-AUDIT` |
| De-ID trước export | `DEID-5MIN` · checklist REDCap |
| Leakage / TRIPOD | `LEAKAGE-5MIN` · `TRIPOD-5MIN` |
| Bridge Q3 L2 | `Q3-L2-EXPORT-EARLY-SIGNAL-BRIDGE` |

## Cấm

- Điền %miss giả từ sandbox như N thật  
- Train M early khi miss D0–D7 chưa audit  
- Mở G2 vì “QC demo PASS”  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5)  
- Ritual: `Q3-L2-EXPORT-RITUAL-CARD` · Protocol: `../../rituals/daily-protocol.md`
