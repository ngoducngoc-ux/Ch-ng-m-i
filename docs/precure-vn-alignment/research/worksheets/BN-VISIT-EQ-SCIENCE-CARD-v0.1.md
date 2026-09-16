# BN-VISIT-EQ — thẻ khoa học 1 trang (StudyID→visits × ladder · ≠ PHI · omics CLOSED)

**Mã:** BN-VISIT-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `BN-VISIT-EQ-5MIN-MICRO-DRILL` · BN-VISIT-SCIENCE-CARD · CLIN-BN-EQ · PB004-EQ · DEID-EQ · EQ-M0M3 / EQ02 / EQ05  
**Căn cứ:** BN-VISIT-MAP-TEMPLATE · CLIN_EVENT-CROSS-SA-ATLAS · G2 CLOSED · L3 CLOSED  
**Dùng khi:** STREAK≥3 · Daily stack **T7** · trước claim “đã có dữ liệu dọc ES” · cặp BN-VISIT×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · map de-ID · event ≠ \(Y(t^*)\) · M0–M3 trên \(Z\) · omics CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp BN-VISIT×EQ**: map StudyID→visits→\(Z\)/`clin_event` **và** 1 dòng ladder M0–M3 — không họ tên/MRN; SYN ≠ BN; ladder trên map de-ID **≠** AUROC lâm sàng. Khác `BN-VISIT-SCIENCE-CARD` (map alone) / `CLIN-BN-EQ` (clin×BN×ladder) / `PB004-EQ` (architecture×ladder) — thẻ này neo **visit map × ladder**.

**Mở song song:** thẻ này · `BN-VISIT-EQ-5MIN` · `BN-VISIT-SCIENCE-CARD` · `CLIN-BN-EQ-SCIENCE-CARD` · `PB004-EQ-SCIENCE-CARD` · `DEID-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `CLIN_EVENT-SCIENCE-CARD`

## Giữ / bỏ (BN-VISIT × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) ≤D7 = L2 exploratory | M4 / X / L3 |
| **StudyID** | SA-__-SYN-___ / de-ID | MRN · họ tên · SĐT |
| **Visits** | D0/D3/D7 (+D14/D21=\(Y\) theo SA) | Chỉ D21 làm “early visit” |
| **Event / \(Z\)** | clin_event / AE schema · \(Z\) cùng cửa sổ | Event từ \(Y(t^*)\) |
| **Omics** | **CLOSED** | Order vì đã map + ladder |
| **Order / Goal** | KHÔNG từ densify | AUROC claim · đóng Goal vì BN-VISIT×EQ |

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
Cặp CLIN-BN-EQ / PB004-EQ / DEID-EQ / PB005-EQ / YTESO-EQ hôm nay? ________
1 việc ≤30′ (map 1 hàng / EQ Drill 10′ / deny-list): ________
Đóng Goal / mở L3 vì BN-VISIT×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở BN-VISIT + EQ sibling thẻ riêng trước cặp? ________
Map+ladder = lý do AUROC / order omics? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | BN-VISIT×EQ bridge 1 trang |
| `BN-VISIT-EQ-5MIN` | Drill điền |
| `BN-VISIT-SCIENCE-CARD` | Map alone |
| `CLIN-BN-EQ` / `PB004-EQ` | CLIN×BN / architecture × ladder |
| `EQ-M0M3` / EQ02 / EQ05 | Ladder sibling |
| `DEID-EQ` / `CLIN_EVENT` / `PB005-EQ` | de-ID / schema / SA-03 proxy × EQ |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Paste MRN / DOB / họ tên / ảnh nhận diện vào log hoặc git  
- Coi SYN map = kết quả lâm sàng · AUROC claim  
- Order PEA / mở L3 vì đã map + ladder · UpdateGoal trên PREP  

## Liên kết

`BN-VISIT-EQ-5MIN-MICRO-DRILL` · `BN-VISIT-SCIENCE-CARD` · `BN-VISIT-MAP-TEMPLATE` · `CLIN-BN-EQ-SCIENCE-CARD` · `PB004-EQ-SCIENCE-CARD` · `DEID-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `CLIN_EVENT-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
