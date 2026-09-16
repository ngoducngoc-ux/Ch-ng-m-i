# DEID-MISS — thẻ khoa học 1 trang (export de-ID × %miss · trước AUROC)

**Mã:** DEID-MISS-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `DEID-MISS-5MIN-MICRO-DRILL` · DEID-SCIENCE-CARD · MISSINGNESS-SCIENCE-CARD · PB004 · TRIPOD  
**Dùng khi:** STREAK≥3 · Daily stack **T5 / T7** · Q2–Q3 L2 · trước claim M0–M3 trên N · cặp De-ID×Missingness  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · không PHI · `[chưa N]` nếu chỉ demo · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp DEID×MISS**: deny-list trước allow-list **và** biết %miss theo visit — `--demo`/synthetic **≠** export de-ID thật; không báo AUROC khi miss chưa audit hoặc file còn PII. Khác `DEID-SCIENCE-CARD` (deny/allow) / `MISSINGNESS-SCIENCE-CARD` (%miss) — thẻ này giữ **cặp bridge**.

**Mở song song:** thẻ này · `DEID-MISS-5MIN` · `DEID-SCIENCE-CARD` · `MISSINGNESS-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · `TRIPOD-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD`

## Giữ / bỏ (DEID × MISS)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **Deny** | PII · MRN · DOB · free-text · media · omics raw | Commit CSV còn tên/SĐT |
| **Allow** | StudyID + visit + \(Z\)/`clin_event` | Field ngoài allow vì “tiện” |
| **N** | Ghi `--demo` \| de-ID site | Coi demo = N lâm sàng |
| **%miss** | Audit theo visit/Z · `[chưa N]` | % giả từ sandbox |
| **AUROC** | Sau deny + miss audit | Claim khi PII risk / demo |
| **G2 / L3** | **CLOSED** | Mở vì QC PASS giấy |

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
1 việc ≤30′ (deny-list / L2 audit 1 ô): ________
Đóng Goal / mở G2? KHÔNG
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
| **thẻ này** | DEID×MISS bridge 1 trang |
| `DEID-MISS-5MIN` | Drill điền |
| `DEID-SCIENCE-CARD` | Deny/allow export |
| `MISSINGNESS-SCIENCE-CARD` | %miss · window |
| `PB004-SCIENCE-CARD` | StudyID–Visit–Obs |
| `TRIPOD` / `SYNTH` | Không claim từ demo |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Commit CSV có tên/SĐT/MRN/DOB  
- Điền %miss giả từ sandbox như N thật  
- Báo AUROC / mở G2 vì demo QC PASS  
- Nhảy claim khi STREAK&lt;3 · UpdateGoal trên PREP  

## Liên kết

`DEID-MISS-5MIN-MICRO-DRILL` · `DEID-MISS-EQ-5MIN` · `DEID-SCIENCE-CARD` · `MISSINGNESS-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · `TRIPOD-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · `REDCAP-DEID-EXPORT-CHECKLIST` · `L2-MISSINGNESS-AUDIT` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
