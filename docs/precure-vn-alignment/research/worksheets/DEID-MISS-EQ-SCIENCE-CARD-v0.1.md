# DEID-MISS-EQ — thẻ khoa học 1 trang (deny-list × %miss × ladder · trước AUROC)

**Mã:** DEID-MISS-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `DEID-MISS-EQ-5MIN-MICRO-DRILL` · DEID-MISS-SCIENCE-CARD · DEID-EQ · MISSINGNESS-EQ · EQ-M0M3 · VAS-LEAK-EQ · PB004  
**Dùng khi:** STREAK≥3 · Daily stack **T5 / T7** · trước M0–M3 trên N · cặp DEID-MISS×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · HAWTHORNE · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · không PHI · `[chưa N]` nếu demo · ladder chỉ khi miss chấp nhận được · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp DEID-MISS×EQ**: deny-list + %miss theo visit **và** 1 dòng ladder M0–M3 — demo/PII risk / miss chưa audit → **không** AUROC; ladder ≠ export đã sạch. Khác `DEID-MISS-SCIENCE-CARD` (cặp alone) / `DEID-EQ` / `MISSINGNESS-EQ` — thẻ này neo **deny×miss × ladder**.

**Mở song song:** thẻ này · `DEID-MISS-EQ-5MIN` · `DEID-MISS-SCIENCE-CARD` · `DEID-EQ-5MIN` · `MISSINGNESS-EQ-5MIN` · `EQ-M0M3-SCIENCE-CARD` · `VAS-LEAK-EQ-SCIENCE-CARD` · `PB004-SCIENCE-CARD`

## Giữ / bỏ (DEID-MISS × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 chỉ khi miss OK / `[chưa N]` ghi CHƯA | Ladder = AUROC khi demo/PII |
| **Deny / Allow** | PII cấm · StudyID+visit+\(Z\) | Export còn tên/SĐT/MRN |
| **N / %miss** | Ghi `--demo` \| de-ID · audit visit | % giả sandbox = N thật |
| **AUROC** | Sau deny + miss audit | Claim khi PII / demo / miss chưa audit |
| **Omics / L3** | **CLOSED** | Order / mở G2 vì QC giấy |
| **Order / Goal** | KHÔNG từ densify | Đóng Goal vì PREP |

## Phương trình ranh giới

```text
deny-list + %miss theo visit  +  EQ ladder M0–M3 (chỉ khi miss OK)
≠  AUROC khi demo/PII  ≠  ladder = export sạch  ≠  mở G2
Ôn DEID-MISS×EQ  ≠  claim N / UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T5|T7 · SA neo: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
N hôm nay: --demo | de-ID thật — ________
1 field CẤM export: ________ · 1 field CHO PHÉP (Z): ________
Visit / Z: D0|D3|D7 · PCT|CFU|VAS|clin_event — ________
%miss (hoặc [chưa N]): ________
1 dòng Z / M0→M3 (chỉ khi miss OK / [chưa N] ghi CHƯA): ________
Omics raw / PII trong export? KHÔNG
Báo AUROC khi demo / miss chưa audit / PII risk? KHÔNG
Cặp **`VAS-LEAK-EQ-SCIENCE-CARD`** / PB004-EQ / SPIRIT-G1-EQ / MISS-RESCUE-EQ hôm nay? ________
1 việc ≤30′ (deny-list / L2 audit 1 ô / EQ Drill 10′): ________
Đóng Goal / mở G2 vì DEID-MISS×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở DEID-MISS + EQ sibling thẻ riêng trước cặp? ________
Deny+miss+ladder = lý do AUROC / mở G2? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | DEID-MISS×EQ bridge 1 trang |
| `DEID-MISS-EQ-5MIN` | Drill điền |
| `DEID-MISS-SCIENCE-CARD` | Cặp alone |
| `DEID-EQ` / `MISSINGNESS-EQ` | DEID / miss × ladder |
| `EQ-M0M3` / `PB004-EQ` / `VAS-LEAK-EQ` | Ladder / StudyID / VAS×leak |
| `REDCAP-DEID-EXPORT-CHECKLIST` | Checklist export |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- %miss / AUROC giả từ sandbox như N thật  
- Train M early khi miss chưa audit · mở G2 · UpdateGoal trên PREP  

## Liên kết

`DEID-MISS-EQ-5MIN-MICRO-DRILL` · `DEID-MISS-SCIENCE-CARD` · `DEID-EQ-SCIENCE-CARD` · `MISSINGNESS-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `VAS-LEAK-EQ-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · `REDCAP-DEID-EXPORT-CHECKLIST` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
