# CLIN-BN — thẻ khoa học 1 trang (clin_event × BN-visit · dọc L1 · de-ID · ≠ Y)

**Mã:** CLIN-BN-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `CLIN-BN-5MIN-MICRO-DRILL` · CLIN_EVENT-SCIENCE-CARD · BN-VISIT-SCIENCE-CARD · DEID · PB004  
**Dùng khi:** STREAK≥3 · Daily stack **T7** · trước claim “đã có dữ liệu dọc” · cặp clin_event×BN-visit  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · event ≠ label \(Y(t^*)\) · không PHI · omics **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp CLIN×BN**: map **StudyID → visits → Z/`clin_event`** với event **không** lấy từ primary — luyện dọc y tế số L1; không MRN/họ tên · không omics · không coi SYN = BN. Khác `CLIN_EVENT-SCIENCE-CARD` (schema event) / `BN-VISIT-SCIENCE-CARD` (map visit) — thẻ này giữ **cặp bridge**.

**Mở song song:** thẻ này · `CLIN-BN-5MIN` · `CLIN_EVENT-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD` · `DEID-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · `L1L2L3-SCIENCE-CARD`

## Giữ / bỏ (CLIN × BN)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **StudyID** | SA-__-SYN-___ / de-ID | MRN · họ tên · SĐT |
| **Visits** | D0/D3/D7 (+D14/D21=\(Y\) theo SA) | Chỉ D21 làm “early visit” |
| **Event** | clin_event / AE / turn ICU schema | Mã event từ \(Y(t^*)\) |
| **\(Z\)** | Cùng cửa sổ ≤D7 | Feature sau \(t^*\) / trùng \(Y\) |
| **Omics** | **CLOSED** | Order vì đã map giấy |
| **SYN** | Rehearsal L1 | SYN = kết quả lâm sàng BN |

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
SA neo: 01|02|05 — ________
StudyID (de-ID): ________
Visits có: D0|D3|D7|D14|D21(Y) — ________
Schema event: clin_event 0–4|symptom/AE|AE/turn ICU — ________
Mã/mô tả event hôm nay: ________
Z cùng cửa sổ ≤D7: ________
Event = label Y(t*)? KHÔNG
PHI trong map/log? KHÔNG
Omics trên map? CLOSED
1 việc ≤30′ (atlas / map template / deny-list): ________
Đóng Goal / mở L3? KHÔNG
```

## Checklist 15′

```text
Đã mở CLIN_EVENT + BN-VISIT thẻ riêng trước cặp? ________
Event từ primary / Y(t*)? KHÔNG
PHI trong git/Drive? KHÔNG
SYN map = BN lâm sàng? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | CLIN×BN bridge 1 trang |
| `CLIN-BN-5MIN` | Drill điền |
| `CLIN_EVENT-SCIENCE-CARD` | Schema event × SA |
| `BN-VISIT-SCIENCE-CARD` | Map StudyID→visit→Z |
| `DEID-SCIENCE-CARD` | Deny-list PHI |
| `PB004-SCIENCE-CARD` | StudyID–Visit–Obs |
| `L1L2L3-SCIENCE-CARD` | Cổng L1 trước L3 |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Event mã từ chính \(Y(t^*)\) / primary  
- Paste MRN/DOB/họ tên vào log hoặc git  
- Coi SYN map = kết quả lâm sàng / mở omics  
- Nhảy claim dọc khi STREAK&lt;3 · UpdateGoal trên PREP  

## Liên kết

`CLIN-BN-5MIN-MICRO-DRILL` · `CLIN-BN-EQ-5MIN` · `CLIN_EVENT-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD` · `DEID-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · `L1L2L3-SCIENCE-CARD` · `BN-VISIT-MAP-TEMPLATE` · `CLIN_EVENT-5MIN` · `BN-VISIT-5MIN` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
