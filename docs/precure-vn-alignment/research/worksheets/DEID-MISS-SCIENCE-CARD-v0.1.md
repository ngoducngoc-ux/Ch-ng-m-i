# DEID-MISS — thẻ khoa học 1 trang (export de-ID × %miss · trước AUROC) · refresh v0.1b

**Mã:** DEID-MISS-SCIENCE-CARD-v0.1b · **Ngày:** 2026-09-16  
**Goal:** ACTIVE · STREAK thật vẫn **2 DONE** · EQ bank **CLOSED** · densify ≠ DONE  
**STREAK&lt;3?** Path STREAK3 trước · **`STREAK3-PACK`** · NATMED · ALERT · FILL-AID → tick **19/09** · dừng OPENER/stack  
**STREAK≥3?** **`AFTER-STREAK3-OPENER`** → 1×EQ sibling → **`DAILY-STACK`** · bridges #0–14  
**Không:** agent tick DONE · UpdateGoal complete trên PREP/densify · invent EQ · densify = DONE · PHI vào git · `--demo` = N lâm sàng · AUROC trước deny+miss  
**Neo:** VAS-LEAK (refresh v0.1b) · `DEID-MISS-5MIN` · DEID-SCIENCE-CARD · MISSINGNESS-SCIENCE-CARD · PB004 · TRIPOD · SYNTH  
**DOI:** TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594) (literature only) · SPIRIT [10.1136/bmj.e7586](https://doi.org/10.1136/bmj.e7586)  
**Dùng khi:** STREAK≥3 · Daily stack **T5 / T7** · Q2–Q3 L2 · trước claim M0–M3 trên N · cặp De-ID×Missingness  
**Hub:** `VAS-LEAK-SCIENCE-CARD` (refresh v0.1b) · tip tiếp `ALERT-HAWTHORNE-SCIENCE-CARD` · Drive keep `1Vjchf1i…`  

```text
STREAK <3? → STREAK3 (PI-NEXT) · densify ≠ DONE
        ↓ STREAK ≥3
OPENER → EQ sibling → DAILY-STACK · ritual theo Ngày N
```

## Mục đích

Ôn **cặp DEID×MISS**: deny-list trước allow-list **và** biết %miss theo visit — `--demo`/synthetic **≠** export de-ID thật; không báo AUROC khi miss chưa audit hoặc file còn PII; densify ≠ “đã chứng minh de-ID/L2”. Khác `DEID-SCIENCE-CARD` (deny/allow) / `MISSINGNESS-SCIENCE-CARD` (%miss) — thẻ này giữ **cặp bridge**.

**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · HAWTHORNE · MEDIA · FILL-AID → tick **19/09** trước  

**Mở song song:** thẻ này · `DEID-MISS-5MIN` · `DEID-SCIENCE-CARD` · `MISSINGNESS-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · `TRIPOD-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · **`VAS-LEAK-SCIENCE-CARD`**

## Giữ / bỏ (DEID × MISS)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **Deny** | PII · MRN · DOB · free-text · media · omics raw | Commit CSV còn tên/SĐT |
| **Allow** | StudyID + visit + \(Z\)/`clin_event` | Field ngoài allow vì “tiện” |
| **N** | Ghi `--demo` \| de-ID site | Coi demo = N lâm sàng · densify = proof N |
| **%miss** | Audit theo visit/Z · `[chưa N]` | % giả từ sandbox như N site |
| **AUROC** | Sau deny + miss audit | Claim khi PII risk / demo / densify |
| **G2 / L3** | **CLOSED** | Mở vì QC PASS giấy / đã ôn cặp |
| **Agent densify** | Anti-forget · hub wire | ≠ invent EQ / tick DONE |

## Phương trình nhắc

```text
deny → allow → %miss(visit,Z) → mới AUROC
--demo / synthetic  ≠  de-ID site  ≠  N lâm sàng
Ôn DEID-MISS / densify  ≠  L2 PASS  ≠  DONE
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
SA neo: 01|02|05 — ________
N hôm nay: --demo | de-ID thật — ________
1 field CẤM export: ________
1 field CHO PHÉP (Z/clin_event/visit): ________
StudyID đủ thay MRN? CÓ|CHƯA
Visit ôn: D0|D3|D7 · Z: ________
%miss (hoặc [chưa N]): ________
Omics raw trong export? KHÔNG
AUROC khi PII/miss/demo? KHÔNG
Densify = “đã chứng minh de-ID/L2”? KHÔNG
Cặp VAS-LEAK / ALERT-HAWTHORNE / PB004 hôm nay? ________
1 việc ≤30′ (deny-list / L2 audit 1 ô): ________
Đóng Goal / mở G2 / invent EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở DEID + MISSINGNESS thẻ riêng trước cặp? ________
PHI trong export/git? KHÔNG
--demo = N site? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | DEID×MISS bridge · refresh v0.1b |
| `DEID-MISS-5MIN` | Drill điền |
| `DEID-SCIENCE-CARD` | Deny/allow export |
| `MISSINGNESS-SCIENCE-CARD` | %miss · window |
| tip **`ALERT-HAWTHORNE-SCIENCE-CARD`** | ALERT×Hawthorne · ≠ Dx |
| `PB004-SCIENCE-CARD` | StudyID–Visit–Obs |
| **`VAS-LEAK-SCIENCE-CARD`** | SA-02 VAS×leakage (hub trước) |
| `TRIPOD` / `SYNTH` | Không claim từ demo |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Commit CSV có tên/SĐT/MRN/DOB · densify = proof de-ID  
- Điền %miss giả từ sandbox như N thật · invent EQ  
- Báo AUROC / mở G2 vì demo QC PASS  
- Nhảy claim khi STREAK&lt;3 · UpdateGoal trên PREP · agent tick DONE  

## Liên kết

`DEID-MISS-5MIN-MICRO-DRILL` · tip tiếp **`ALERT-HAWTHORNE-SCIENCE-CARD`** · `DEID-SCIENCE-CARD` · **`DEID-EQ-SCIENCE-CARD`** · `MISSINGNESS-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · `TRIPOD-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · **`VAS-LEAK-SCIENCE-CARD`** · `REDCAP-DEID-EXPORT-CHECKLIST` · `L2-MISSINGNESS-AUDIT` · `DEID-MISS-EQ-5MIN` · **`DEID-MISS-EQ-SCIENCE-CARD`** · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX` · `STREAK3-PACK-SCIENCE-CARD` · Drive keep `1Vjchf1i…` · PREP≠DONE · densify≠DONE  
