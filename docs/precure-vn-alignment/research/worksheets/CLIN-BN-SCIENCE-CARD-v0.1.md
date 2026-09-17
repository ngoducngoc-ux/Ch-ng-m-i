# CLIN-BN — thẻ khoa học 1 trang (clin_event × BN-visit · dọc L1 · de-ID · ≠ Y) · refresh v0.1b

**Mã:** CLIN-BN-SCIENCE-CARD-v0.1b · **Ngày:** 2026-09-16  
**Goal:** ACTIVE · STREAK thật vẫn **2 DONE** · EQ bank **CLOSED** · densify ≠ DONE  
**STREAK&lt;3?** Path STREAK3 trước · **`STREAK3-PACK`** · NATMED · ALERT · FILL-AID → tick **19/09** · dừng OPENER/stack  
**STREAK≥3?** **`AFTER-STREAK3-OPENER`** → 1×EQ sibling → **`DAILY-STACK`** · bridges #0–14  
**Không:** agent tick DONE · UpdateGoal complete trên PREP/densify · invent EQ · densify = DONE · PHI vào git · event = \(Y\)  
**Neo:** IMAGEJ-EPI (refresh v0.1b) · `CLIN-BN-5MIN` · CLIN_EVENT-SCIENCE-CARD · BN-VISIT-SCIENCE-CARD · DEID · PB004  
**Dùng khi:** STREAK≥3 · Daily stack **T7** · trước claim “đã có dữ liệu dọc” · cặp clin_event×BN-visit  
**Hub:** `IMAGEJ-EPI-SCIENCE-CARD` (refresh v0.1b) · tip tiếp `VAS-LEAK-SCIENCE-CARD` · Drive keep `1Vjchf1i…`  

```text
STREAK <3? → STREAK3 (PI-NEXT) · densify ≠ DONE
        ↓ STREAK ≥3
OPENER → EQ sibling → DAILY-STACK · ritual theo Ngày N
```

## Mục đích

Ôn **cặp CLIN×BN**: map **StudyID → visits → Z/`clin_event`** với event **không** lấy từ primary — luyện dọc y tế số L1; không MRN/họ tên · không omics · không coi SYN = BN; densify ≠ “đã có dữ liệu dọc thật”. Khác `CLIN_EVENT-SCIENCE-CARD` (schema event) / `BN-VISIT-SCIENCE-CARD` (map visit) — thẻ này giữ **cặp bridge**.

**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · HAWTHORNE · MEDIA · FILL-AID → tick **19/09** trước  

**Mở song song:** thẻ này · `CLIN-BN-5MIN` · `CLIN_EVENT-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD` · `DEID-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · **`IMAGEJ-EPI-SCIENCE-CARD`**

## Giữ / bỏ (CLIN × BN)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **StudyID** | SA-__-SYN-___ / de-ID | MRN · họ tên · SĐT |
| **Visits** | D0/D3/D7 (+D14/D21=\(Y\) theo SA) | Chỉ D21 làm “early visit” |
| **Event** | clin_event / AE / turn ICU schema | Mã event từ \(Y(t^*)\) |
| **\(Z\)** | Cùng cửa sổ ≤D7 | Feature sau \(t^*\) / trùng \(Y\) |
| **Omics** | **CLOSED** | Order vì đã map / densify giấy |
| **SYN** | Rehearsal L1 | SYN = kết quả lâm sàng BN · densify = proof |
| **Agent densify** | Anti-forget · hub wire | ≠ invent EQ / tick DONE |

## Phương trình nhắc

```text
StudyID → Visit(t) → Z(t') / clin_event(t')   ·  t' ≪ t*
clin_event ≠ Y(t*)  ·  PHI ∉ git  ·  SYN ≠ BN
Ôn CLIN-BN / densify  ≠  dữ liệu dọc lâm sàng  ≠  DONE
```

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
Densify = “đã có dữ liệu dọc thật”? KHÔNG
Omics trên map? CLOSED
1 việc ≤30′ (atlas / map template / deny-list / VAS-LEAK): ________
Đóng Goal / mở L3 / invent EQ? KHÔNG
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
| **thẻ này** | CLIN×BN bridge · refresh v0.1b |
| `CLIN-BN-5MIN` | Drill điền |
| `CLIN_EVENT-SCIENCE-CARD` | Schema event × SA |
| `BN-VISIT-SCIENCE-CARD` | Map StudyID→visit→Z |
| tip **`VAS-LEAK-SCIENCE-CARD`** | SA-02 VAS×leakage |
| `DEID-SCIENCE-CARD` | Deny-list PHI |
| `PB004-SCIENCE-CARD` | StudyID–Visit–Obs |
| `L1L2L3-SCIENCE-CARD` | Cổng L1 trước L3 |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Event mã từ chính \(Y(t^*)\) / primary · densify = proof  
- Paste MRN/DOB/họ tên vào log hoặc git · invent EQ  
- Coi SYN map = kết quả lâm sàng / mở omics  
- Nhảy claim dọc khi STREAK&lt;3 · UpdateGoal trên PREP · agent tick DONE  

## Liên kết

`CLIN-BN-5MIN-MICRO-DRILL` · tip tiếp **`VAS-LEAK-SCIENCE-CARD`** · `CLIN_EVENT-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD` · `DEID-SCIENCE-CARD` · `PB004-SCIENCE-CARD` · **`IMAGEJ-EPI-SCIENCE-CARD`** · `L1L2L3-SCIENCE-CARD` · `CLIN-BN-EQ-5MIN` · **`CLIN-BN-EQ-SCIENCE-CARD`** · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX` · `STREAK3-PACK-SCIENCE-CARD` · Drive keep `1Vjchf1i…` · PREP≠DONE · densify≠DONE  
