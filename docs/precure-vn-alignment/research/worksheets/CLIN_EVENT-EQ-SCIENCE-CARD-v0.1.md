# CLIN_EVENT-EQ — thẻ khoa học 1 trang (dọc L1 × ladder · ≠ Y)

**Mã:** CLIN_EVENT-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `CLIN_EVENT-EQ-5MIN-MICRO-DRILL` · CLIN_EVENT-SCIENCE-CARD · CLIN-BN-EQ · PUSH-EQ · EQ-M0M3 · BN-VISIT-EQ · DEID-EQ  
**DOI:** Zhou Nature [10.1038/s41586-019-1231-2](https://doi.org/10.1038/s41586-019-1231-2)  
**Dùng khi:** STREAK≥3 · Daily stack **T7** · trước claim “đã có dữ liệu dọc ES” · cặp CLIN_EVENT×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NOW · FILL-AID · NatMed · ALERT · HAWTHORNE · MEDIA → tick **19/09** trước  
**Goal:** ACTIVE · event ≠ \(Y(t^*)\) · 1 dòng ladder trên \(Z\) · không PHI · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp CLIN_EVENT×EQ**: 1 schema event (0–4 / AE / ICU) **và** 1 dòng ladder M0–M3 trên \(Z\) cùng cửa sổ — event không lấy từ primary; de-ID trước omics. Khác `CLIN_EVENT-SCIENCE-CARD` (alone) / `CLIN-BN-EQ` — thẻ này neo **event × ladder** chung.

**Mở song song:** thẻ này · `CLIN_EVENT-EQ-5MIN` · `CLIN_EVENT-SCIENCE-CARD` · `CLIN-BN-EQ-SCIENCE-CARD` · `PUSH-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `BN-VISIT-EQ-SCIENCE-CARD`

## Giữ / bỏ (CLIN_EVENT × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) cùng cửa sổ event | Ladder = label \(Y(t^*)\) |
| **Event** | Schema 0–4 / AE / turn ICU · visit+time | Mã event từ primary |
| **L1** | StudyID + Visit + timestamp + event + \(Z\) | PHI trong log/git |
| **Omics / L3** | **CLOSED** | Order PEA vì đã mã 1 event |
| **Order / Goal** | KHÔNG từ densify | Đóng Goal / tick DONE vì PREP |

## Phương trình ranh giới

```text
1 schema event  +  visit+time  +  EQ ladder M0–M3 trên Z cùng cửa sổ
≠  Event = Y(t*)  ≠  PHI  ≠  order PEA
Ôn CLIN_EVENT×EQ  ≠  UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T7 · SA: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
Schema: clin_event 0–4|symptom/AE|AE/turn ICU — ________
Mã / mô tả event: ________
Visit + timestamp đủ L1? CÓ|CHƯA — thiếu: ________
1 dòng Z / M0→M3 cùng cửa sổ: ________
Event = label Y(t*)? KHÔNG
PHI / omics? KHÔNG / CLOSED
Cặp **`LEAKAGE-EQ-SCIENCE-CARD`** / PUSH-EQ / CLIN-BN-EQ / BN-VISIT-EQ hôm nay? ________
1 việc ≤30′ (vignette / EQ Drill 10′ / deny-list): ________
Đóng Goal / mở L3 vì CLIN_EVENT×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở CLIN_EVENT + EQ sibling thẻ riêng trước cặp? ________
Event+ladder = lý do train bằng Y(t*) / mở PEA? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | CLIN_EVENT×EQ bridge 1 trang |
| `CLIN_EVENT-EQ-5MIN` | Drill điền |
| `CLIN_EVENT-SCIENCE-CARD` / atlas | Event alone |
| `CLIN-BN-EQ` / `BN-VISIT-EQ` | Pair bridges đã densify |
| `PUSH-EQ` / `EQ-M0M3` | Sibling / ladder |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Train early bằng chính \(Y(t^*)\) đóng vai event  
- Ghi PHI · mở PEA / UpdateGoal trên PREP  

## Liên kết

`CLIN_EVENT-EQ-5MIN-MICRO-DRILL` · `CLIN_EVENT-SCIENCE-CARD` · `CLIN_EVENT-CROSS-SA-ATLAS` · `CLIN-BN-EQ-SCIENCE-CARD` · `PUSH-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `BN-VISIT-EQ-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
