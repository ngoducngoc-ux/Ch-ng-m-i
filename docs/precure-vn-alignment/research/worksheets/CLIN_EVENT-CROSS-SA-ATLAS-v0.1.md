# Atlas — `clin_event` / sự kiện dọc × SA-01 / 02 / 05 · refresh v0.1b

**Mã:** CLIN_EVENT-CROSS-SA-ATLAS-v0.1b · **Ngày:** 2026-09-16  
**Goal:** ACTIVE · STREAK thật vẫn **2 DONE** · EQ bank **CLOSED** · densify ≠ DONE  
**STREAK&lt;3?** Path STREAK3 trước · **`STREAK3-PACK`** · **`STREAK3-EQ`** · NatMed → tick **19/09** · dừng OPENER/stack  
**STREAK≥3?** **`AFTER-STREAK3-OPENER`** → 1×EQ sibling → **`DAILY-STACK`** · bridges #0–14  
**Không:** agent tick DONE · UpdateGoal complete trên PREP/densify · invent EQ · PHI trong git · order PEA vì mã event đủ  
**Dùng khi:** EQ rotation T2/T4/T6 · drill A/B (L1) · Zhou Ngày 02 · BN-VISIT / y tế số  
**Hub:** `ALERT` (refresh v0.1b) · tip tiếp `SHIFT` (`PRECURE-SHIFT-CROSS-SA-BANK`) · Drive keep `1Vjchf1i…`  

```text
STREAK <3? → STREAK3 (PI-NEXT) · densify ≠ DONE
        ↓ STREAK ≥3
OPENER → EQ sibling → DAILY-STACK · ritual theo Ngày N
```

## Một câu

> Zhou: omics nhảy khi có **sự kiện** — Smart A bắt analog bằng event dọc trên eCRF; **mỗi SA một schema**, cùng nguyên tắc L1 (ID–visit–time–event–\(Z\)).

## Ma trận sự kiện (ôn trước EQ)

| SA | Schema sự kiện | Cửa sổ early | Gắn \(Z\) | Không làm |
|----|----------------|--------------|-----------|-----------|
| **01** | `clin_event` **0–4** (eCRF v0.2) | D0–D7 | PCT/CFU/VAS + A4 | Mã từ chính \(Y_{D21}\) · train “early” bằng outcome |
| **02** | Timestamp triệu chứng / AE / adherence event | ≤D3 (ưu tiên D1) | VAS/CFU · C1–C3 | Coi VAS_D3 = event “sớm” khi trùng \(Y\) |
| **05** | AE ICU / turn miss / can thiệp chăm sóc | ≤D7 | PUSH/CFU/TURN · B1–B3 | Auto-treat vì 1 event · gộp với SA-01 |

**Zhou map SA-01 (chi tiết mã):** `CLIN_EVENT-ZHOU-MAP` · luyện: `CLIN_EVENT-CODING-VIGNETTES`. densify ≠ DONE.

## L1 y tế số (PB-004) — 1 hàng đủ chưa?

| Thành phần | SA-01 | SA-02 | SA-05 |
|------------|-------|-------|-------|
| StudyID + visit + timestamp | bắt buộc | bắt buộc | bắt buộc |
| Event field | `clin_event` 0–4 | symptom/AE/adhere note | AE/turn/care event |
| \(Z\) cùng visit | PCT/CFU/VAS | VAS/CFU | PUSH/CFU/TURN |
| PHI trong git/Drive public | **Không** | **Không** | **Không** |
| Map luyện | `BN-VISIT-MAP-TEMPLATE` | cùng template · SA-02 | cùng · SA-05 ICU |

## Drill 8′ (điền — 1 SA theo EQ rotation)

```text
Thứ: T2|T4|T6 · SA: 01|02|05
Event hôm nay (mã / mô tả): ________
Visit + timestamp đủ L1? CÓ | CHƯA — thiếu: ________
Z cùng cửa sổ: ________
1 câu event ≠ label Y(t*): ________
1 câu vì sao chưa cần X/omics:
```

## Gắn ALERT / leakage (đừng nhầm)

| Atlas | Việc |
|-------|------|
| `ALERT-CROSS-SA-ATLAS` (refresh v0.1b) | Event + \(Z\) đứng → hành động nội bộ (A4/C/B) |
| `LEAKAGE-CROSS-SA-ATLAS` (refresh v0.1b) | Event/feature sau \(t^*\) hoặc trùng \(Y\) → không đưa M early |
| `CLIN_EVENT-CROSS-SA-ATLAS` | (file này) schema event × SA |

## Cấm

- Coi atlas PREP = STREAK DONE  
- Vignette / map de-ID = BN thật có PHI  
- Order PEA vì đã mã hoá đủ `clin_event`  
- UpdateGoal complete trên densify · invent EQ  

## Liên kết

- **Thẻ:** **`CLIN_EVENT-SCIENCE-CARD`** · **`CLIN_EVENT-EQ-SCIENCE-CARD`** · **`CLIN-BN-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`  
- `CLIN_EVENT-ZHOU-MAP` · `CLIN_EVENT-CODING-VIGNETTES` · **`CLIN_EVENT-5MIN`** · **`CLIN_EVENT-EQ-5MIN`** (T7)  
- `BN-VISIT-MAP-TEMPLATE` · `y-te-so-precure-bridge` (refresh v0.1b) · EQ-SA01|02|05  
- tip tiếp: `PRECURE-SHIFT-CROSS-SA-BANK` · Drive keep `1Vjchf1i…` · PREP≠DONE · densify≠DONE  
