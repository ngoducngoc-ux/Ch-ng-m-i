# MISSINGNESS-EQ — thẻ khoa học 1 trang (%miss · ladder Z · trước AUROC)

**Mã:** MISSINGNESS-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `MISSINGNESS-EQ-5MIN-MICRO-DRILL` · MISSINGNESS-SCIENCE-CARD · DEID-EQ · DEID-MISS · EQ-M0M3 / EQ02 / EQ05  
**Căn cứ:** L2-MISSINGNESS-AUDIT · Q3-L2-EXPORT · PB-009 L2  
**Dùng khi:** STREAK≥3 · Daily stack **T5** · trước AUROC / M0–M3 trên N · cặp Missingness×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · `[chưa N]` nếu chỉ `--demo` · M0–M3 chỉ khi miss audit · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp MISSINGNESS×EQ**: %miss theo visit **và** 1 dòng ladder M0–M3 — `--demo` xanh ≠ missingness lâm sàng; không báo AUROC khi miss cao / demo. Khác `MISSINGNESS-SCIENCE-CARD` (audit alone) / `DEID-EQ-SCIENCE-CARD` (export×ladder) — thẻ này neo **%miss × ladder**.

**Mở song song:** thẻ này · `MISSINGNESS-EQ-5MIN` · `MISSINGNESS-SCIENCE-CARD` · `DEID-EQ-SCIENCE-CARD` · `DEID-MISS-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `ISO-SWAB-EQ-SCIENCE-CARD`

## Giữ / bỏ (Missingness × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **%miss** | Theo visit · `[chưa N]` nếu demo | %miss giả từ sandbox = N |
| **EQ ladder** | M0–M3 khi miss chấp nhận | Ladder khi miss cao / chưa audit |
| **QC gate** | redcap_import_qc / deny-list | Bỏ qua QC |
| **AUROC** | Sau miss audit + de-ID | Claim trên demo / miss cao |
| **G2** | Không vì QC demo PASS | Mở G2 vì sandbox xanh |

## Phương trình ranh giới

```text
%miss audit (visit×Z)  +  EQ ladder M0–M3 (khi miss OK)
  ≥  trước  AUROC / M3 claim
--demo PASS  ≠  missingness lâm sàng  ≠  N thật
Miss cao / chưa audit  →  KHÔNG claim
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T5 · N hôm nay: --demo|de-ID thật (site) — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
Visit ôn: D0|D3|D7 · 1 Z: PCT|CFU|VAS|clin_event — ________
%miss (hoặc [chưa N]): ________
1 dòng Z / M0→M3 (chỉ khi miss OK / [chưa N] ghi CHƯA): ________
Window D3 = bắt buộc|D1–D3|[CẦN XÁC NHẬN DM]
QC gate redcap_import_qc / deny-list? CÓ|CHƯA
Báo AUROC khi miss cao / demo? KHÔNG
Cặp DEID-EQ / DEID-MISS / ISO-SWAB-EQ / TRIPOD hôm nay? ________
1 việc ≤30′ (L2 audit 1 ô / EQ Drill 10′): ________
Đóng Goal / mở G2 vì demo PASS? KHÔNG
```

## Checklist 15′

```text
Đã mở MISSINGNESS + EQ sibling thẻ riêng trước cặp? ________
Demo = N lâm sàng? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | Missingness×EQ bridge 1 trang |
| `MISSINGNESS-EQ-5MIN` | Drill điền |
| `MISSINGNESS-SCIENCE-CARD` | %miss audit alone |
| `DEID-EQ` / `DEID-MISS` | Export / miss×de-ID |
| `EQ-M0M3` / EQ02 / EQ05 | Ladder sibling |
| `LEAKAGE` / `TRIPOD` | Timing / AI claim |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- %miss giả từ sandbox như N thật  
- Train M early khi miss D0–D7 chưa audit · mở G2 vì QC demo PASS  
- UpdateGoal trên PREP · nhảy claim khi STREAK&lt;3  

## Liên kết

`MISSINGNESS-EQ-5MIN-MICRO-DRILL` · `MISSINGNESS-SCIENCE-CARD` · `DEID-EQ-SCIENCE-CARD` · `DEID-MISS-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `ISO-SWAB-EQ-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `TRIPOD-SYNTH-SCIENCE-CARD` · **`PEA-EQ-SCIENCE-CARD`** · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
