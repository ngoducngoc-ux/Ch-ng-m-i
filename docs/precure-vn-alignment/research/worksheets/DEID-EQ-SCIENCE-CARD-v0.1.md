# DEID-EQ — thẻ khoa học 1 trang (export · ladder Z · trước AUROC)

**Mã:** DEID-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `DEID-EQ-5MIN-MICRO-DRILL` · DEID-SCIENCE-CARD · DEID-MISS · EQ-M0M3 / EQ02 / EQ05 · PB004  
**Căn cứ:** REDCAP-DEID-EXPORT-CHECKLIST · PB-004 · PB-009 L2.1  
**Dùng khi:** STREAK≥3 · Daily stack **T5 / T7** · trước claim M0–M3 / AUROC trên “export” · cặp De-ID×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · không PHI · ladder chỉ trên \(Z\) de-ID · `--demo` ≠ N · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp DEID×EQ**: 1 dòng ladder M0–M3 trên field \(Z\) **đã** deny-list — StudyID thay MRN; **không** AUROC / M3 claim khi còn PII risk, miss chưa audit, hoặc chỉ `--demo`. Khác `DEID-SCIENCE-CARD` (export alone) / `EQ-*-SCIENCE-CARD` (ladder alone) — thẻ này giữ **cặp bridge**.

**Mở song song:** thẻ này · `DEID-EQ-5MIN` · `DEID-SCIENCE-CARD` · `DEID-MISS-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · `SPIRIT-G1-EQ-SCIENCE-CARD`

## Giữ / bỏ (De-ID × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **Export** | StudyID + \(Z\)/`clin_event`/visit | MRN · tên · SĐT · DOB |
| **EQ ladder** | M0–M3 trên field allow | Field deny / X_PEA |
| **N / demo** | De-ID thật (site) trước claim | AUROC trên `--demo` |
| **Miss audit** | L2 trước M3 claim | Bỏ qua miss |
| **Omics raw** | CLOSED đến G2 | Export / ladder trên X |

## Phương trình ranh giới

```text
Deny-list pass  +  EQ ladder M0–M3 trên Z allow-only
  ≥  trước  AUROC / M3 claim
--demo  ≠  N thật  ≠  bằng chứng BN
PII risk / miss chưa audit  →  KHÔNG claim
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T5|T7 · SA neo: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
N hôm nay: --demo|de-ID thật (site) — ________
1 field CẤM export (D1–D7): ________
1 field CHO PHÉP = Z / clin_event / visit: ________
1 dòng Z / M0→M3 (chỉ field allow): ________
StudyID đủ thay MRN? CÓ|CHƯA
Omics raw / X_PEA trong export? KHÔNG
Báo AUROC khi PII / demo / miss chưa audit? KHÔNG
Cặp DEID-MISS / SPIRIT-G1-EQ / TRIPOD / LEAK-CROSS hôm nay? ________
1 việc ≤30′ (deny-list skim / EQ Drill 10′ / L2 audit 1 ô): ________
Đóng Goal / mở G2 vì DEID×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở DEID + EQ sibling thẻ riêng trước cặp? ________
CSV còn PII? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | DEID×EQ bridge 1 trang |
| `DEID-EQ-5MIN` | Drill điền |
| `DEID-SCIENCE-CARD` | Export alone |
| `DEID-MISS-SCIENCE-CARD` | De-ID × missingness |
| `EQ-M0M3` / EQ02 / EQ05 | Ladder sibling |
| `PB004` / `MISSINGNESS` | Schema / miss |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Commit CSV có tên/SĐT/MRN/DOB  
- Claim AUROC / M3 trên demo hoặc file còn PII  
- Mở G2 / L3 vì đã viết ladder trên sandbox · UpdateGoal trên PREP  

## Liên kết

`DEID-EQ-5MIN-MICRO-DRILL` · `DEID-SCIENCE-CARD` · `DEID-MISS-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · `MISSINGNESS-SCIENCE-CARD` · `SPIRIT-G1-EQ-SCIENCE-CARD` · **`ISO-SWAB-EQ-SCIENCE-CARD`** · **`MISSINGNESS-EQ-SCIENCE-CARD`** · `TRIPOD-SYNTH-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
