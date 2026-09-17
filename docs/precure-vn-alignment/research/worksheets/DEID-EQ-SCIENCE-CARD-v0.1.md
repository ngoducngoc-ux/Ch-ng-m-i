# DEID-EQ — thẻ khoa học 1 trang (export · ladder Z · trước AUROC) · refresh v0.1b

**Mã:** DEID-EQ-SCIENCE-CARD-v0.1b · **Ngày:** 2026-09-16  
**Goal:** ACTIVE · STREAK thật vẫn **2 DONE** · EQ bank **CLOSED** · densify ≠ DONE  
**STREAK&lt;3?** Path STREAK3 trước · **`STREAK3-PACK`** · NATMED · ALERT · FILL-AID → tick **19/09** · dừng OPENER/stack  
**STREAK≥3?** **`AFTER-STREAK3-OPENER`** → 1×EQ sibling → **`DAILY-STACK`** · bridges #0–14  
**Không:** agent tick DONE · UpdateGoal complete trên PREP/densify · invent EQ · densify = DONE · PHI vào git · AUROC trên `--demo` / PII · mở G2 vì ladder  
**Neo:** SPIRIT-G1-EQ (refresh v0.1b) · `DEID-EQ-5MIN` · DEID-SCIENCE-CARD · DEID-MISS · EQ-M0M3 / EQ02 / EQ05 · PB004  
**Căn cứ:** REDCAP-DEID-EXPORT-CHECKLIST · PB-004 · PB-009 L2.1  
**Dùng khi:** STREAK≥3 · Daily stack **T5 / T7** · trước claim M0–M3 / AUROC trên “export” · cặp De-ID×EQ  
**Hub:** `SPIRIT-G1-EQ-SCIENCE-CARD` (refresh v0.1b) · tip tiếp `ISO-SWAB-EQ-SCIENCE-CARD` · Drive keep `1Vjchf1i…`  

```text
STREAK <3? → STREAK3 (PI-NEXT) · densify ≠ DONE
        ↓ STREAK ≥3
OPENER → EQ sibling → DAILY-STACK · ritual theo Ngày N
```

## Mục đích

Ôn **cặp DEID×EQ**: 1 dòng ladder M0–M3 trên field \(Z\) **đã** deny-list (EQ sibling **đã có**, không invent) — StudyID thay MRN · densify ≠ export CLOSED · **không** AUROC / M3 claim khi còn PII risk, miss chưa audit, hoặc chỉ `--demo`. Khác `DEID-SCIENCE-CARD` (export alone) / `EQ-*-SCIENCE-CARD` (ladder alone) — thẻ này giữ **cặp bridge**.

**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · HAWTHORNE · MEDIA · FILL-AID → tick **19/09** trước  

**Mở song song:** thẻ này · `DEID-EQ-5MIN` · `DEID-SCIENCE-CARD` · `DEID-MISS-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · **`SPIRIT-G1-EQ-SCIENCE-CARD`**

## Giữ / bỏ (De-ID × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **Export** | StudyID + \(Z\)/`clin_event`/visit | MRN · tên · SĐT · DOB · densify = proof |
| **EQ ladder** | M0–M3 trên field allow · bank **CLOSED** | Field deny / X_PEA · invent EQ |
| **N / demo** | De-ID thật (site) trước claim | AUROC trên `--demo` |
| **Miss audit** | L2 trước M3 claim | Bỏ qua miss |
| **Omics raw** | CLOSED đến G2 | Export / ladder trên X |
| **Agent densify** | Anti-forget · hub wire | ≠ invent EQ / tick DONE / claim AUROC |

## Phương trình ranh giới

```text
Deny-list pass  +  EQ ladder M0–M3 trên Z allow-only
  ≥  trước  AUROC / M3 claim
--demo  ≠  N thật  ≠  bằng chứng BN
PII risk / miss chưa audit / densify  →  KHÔNG claim
Ôn DEID-EQ / densify  ≠  “export CLOSED / AUROC OK”  ≠  DONE
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T5|T7 · SA neo: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________ (không invent)
N hôm nay: --demo|de-ID thật (site) — ________
1 field CẤM export (D1–D7): ________
1 field CHO PHÉP = Z / clin_event / visit: ________
1 dòng Z / M0→M3 (chỉ field allow · không X): ________
StudyID đủ thay MRN? CÓ|CHƯA
Omics raw / X_PEA trong export? KHÔNG
Báo AUROC khi PII / demo / miss chưa audit? KHÔNG
Densify = “export CLOSED / AUROC OK”? KHÔNG
Cặp DEID-MISS / SPIRIT-G1-EQ / TRIPOD / LEAK-CROSS hôm nay? ________
1 việc ≤30′ (deny-list skim / EQ Drill 10′ / L2 audit 1 ô): ________
Đóng Goal / invent EQ / mở G2 vì DEID×EQ? KHÔNG
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
| **thẻ này** | DEID×EQ bridge · refresh v0.1b |
| `DEID-EQ-5MIN` | Drill điền |
| `DEID-SCIENCE-CARD` | Export alone |
| `DEID-MISS-SCIENCE-CARD` | De-ID × missingness |
| **`SPIRIT-G1-EQ-SCIENCE-CARD`** | G1 gates × ladder (hub trước) |
| tip **`ISO-SWAB-EQ-SCIENCE-CARD`** | ISO swab × ladder |
| `EQ-M0M3` / EQ02 / EQ05 | Ladder sibling (bank CLOSED) |
| `PB004` / `MISSINGNESS` | Schema / miss |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Commit CSV có tên/SĐT/MRN/DOB · densify = proof de-ID  
- Claim AUROC / M3 trên demo hoặc file còn PII · invent EQ  
- Mở G2 / L3 vì đã viết ladder trên sandbox · UpdateGoal trên PREP · agent tick DONE  

## Liên kết

`DEID-EQ-5MIN-MICRO-DRILL` · tip tiếp **`ISO-SWAB-EQ-SCIENCE-CARD`** · `DEID-SCIENCE-CARD` · `DEID-MISS-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · `MISSINGNESS-SCIENCE-CARD` · **`SPIRIT-G1-EQ-SCIENCE-CARD`** · **`ISO-SWAB-EQ-SCIENCE-CARD`** · **`MISSINGNESS-EQ-SCIENCE-CARD`** · `TRIPOD-SYNTH-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX` · `STREAK3-PACK-SCIENCE-CARD` · Drive keep `1Vjchf1i…` · PREP≠DONE · densify≠DONE  
