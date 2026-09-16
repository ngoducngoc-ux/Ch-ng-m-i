# CLIN-BN-EQ — thẻ khoa học 1 trang (dọc L1 × ladder · ≠ Y · omics CLOSED)

**Mã:** CLIN-BN-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `CLIN-BN-EQ-5MIN-MICRO-DRILL` · CLIN-BN-SCIENCE-CARD · CLIN_EVENT · BN-VISIT · DEID-EQ · AI-STACK-EQ · EQ-M0M3 / EQ02 / EQ05  
**Căn cứ:** CLIN_EVENT-CROSS-SA-ATLAS · BN-VISIT-MAP-TEMPLATE · G2 CLOSED · L3 CLOSED  
**Dùng khi:** STREAK≥3 · Daily stack **T7** · trước claim “đã có dữ liệu dọc / ES” · cặp CLIN-BN×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · event ≠ \(Y(t^*)\) · M0–M3 trên \(Z\) · không PHI · omics CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp CLIN-BN×EQ**: map StudyID→visits→\(Z\)/`clin_event` **và** 1 dòng ladder M0–M3 — event **không** lấy từ primary; SYN ≠ BN; ladder trên map de-ID **≠** claim AUROC lâm sàng / mở omics. Khác `CLIN-BN-SCIENCE-CARD` (bridge alone) / `AI-STACK-EQ` (pipeline×ladder) — thẻ này neo **map dọc L1 × ladder**.

**Mở song song:** thẻ này · `CLIN-BN-EQ-5MIN` · `CLIN-BN-SCIENCE-CARD` · `CLIN_EVENT-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD` · `DEID-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `AI-STACK-EQ-SCIENCE-CARD`

## Giữ / bỏ (CLIN-BN × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) ≤D7 = L2 exploratory | M4 / X / L3 |
| **StudyID** | SA-__-SYN-___ / de-ID | MRN · họ tên · SĐT |
| **Visits** | D0/D3/D7 (+D14/D21=\(Y\) theo SA) | Chỉ D21 làm “early visit” |
| **Event** | clin_event / AE / turn ICU schema | Mã event từ \(Y(t^*)\) |
| **Omics** | **CLOSED** | Order vì đã map + ladder |
| **Order / Goal** | KHÔNG từ densify | Claim AUROC / đóng Goal vì CLIN-BN×EQ |

## Phương trình ranh giới

```text
Map StudyID→visits→Z/clin_event  +  EQ ladder M0–M3 trên Z
  =  dọc L1 hợp lệ hôm nay
Event  ≠  Y(t*) / primary
SYN map  ≠  BN lâm sàng
Ladder trên map de-ID  ≠  AUROC claim  ≠  mở omics
Viết map / ladder  ≠  order PEA
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T7 · SA neo: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
StudyID (de-ID / SYN): ________
Visits tick: D0|D3|D7|D14|D21(Y) — ________
1 dòng Z / M0→M3 trên visits ≤D7: ________
Schema event: clin_event 0–4|symptom/AE|AE/ICU — ________
Event = label Y(t*)? KHÔNG
PHI / omics trên map? KHÔNG / CLOSED
Cặp AI-STACK-EQ / DEID-EQ / L1L2L3-EQ / BN-VISIT-EQ / YTESO-EQ hôm nay? ________
1 việc ≤30′ (map 1 hàng / EQ Drill 10′ / deny-list): ________
Đóng Goal / mở L3 vì CLIN-BN×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở CLIN-BN + EQ sibling thẻ riêng trước cặp? ________
Event từ primary / Y(t*)? KHÔNG
Map+ladder = lý do AUROC / order omics? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | CLIN-BN×EQ bridge 1 trang |
| `CLIN-BN-EQ-5MIN` | Drill điền |
| `CLIN-BN-SCIENCE-CARD` | CLIN×BN alone |
| `CLIN_EVENT` / `BN-VISIT` | Schema / map visit |
| `EQ-M0M3` / EQ02 / EQ05 | Ladder sibling |
| `DEID-EQ` / `AI-STACK-EQ` | de-ID×ladder / pipeline×ladder |
| `YTESO-EQ` / `PB004-EQ` / `BN-VISIT-EQ` | Y tế số / StudyID-Obs / visit×EQ |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Event mã từ chính \(Y(t^*)\) / primary  
- Paste MRN/DOB/họ tên · coi SYN = BN  
- AUROC claim / mở omics vì đã map + ladder · UpdateGoal trên PREP  

## Liên kết

`CLIN-BN-EQ-5MIN-MICRO-DRILL` · `CLIN-BN-SCIENCE-CARD` · `CLIN_EVENT-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD` · `DEID-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `AI-STACK-EQ-SCIENCE-CARD` · `L1L2L3-EQ-SCIENCE-CARD` · `BN-VISIT-MAP-TEMPLATE` · `DAILY-STACK-AFTER-STREAK3` · **`YTESO-EQ-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`
