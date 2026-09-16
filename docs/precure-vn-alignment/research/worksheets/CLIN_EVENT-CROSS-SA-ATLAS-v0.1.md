# Atlas — `clin_event` / sự kiện dọc × SA-01 / 02 / 05

**Mã:** CLIN_EVENT-CROSS-SA-ATLAS-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** EQ rotation T2/T4/T6 · drill A/B (L1) · Zhou Ngày 02 · BN-VISIT / y tế số  
**Thẻ khoa học:** **`CLIN_EVENT-SCIENCE-CARD-v0.1.md`** · định tuyến `SCIENCE-CARDS-INDEX`  
**Goal:** ACTIVE · event analog Zhou trên \(Z\) **trước** \(X\) · không PHI · PREP ≠ DONE

## Một câu

> Zhou: omics nhảy khi có **sự kiện** — Smart A bắt analog bằng event dọc trên eCRF; **mỗi SA một schema**, cùng nguyên tắc L1 (ID–visit–time–event–\(Z\)).

## Ma trận sự kiện (ôn trước EQ)

| SA | Schema sự kiện | Cửa sổ early | Gắn \(Z\) | Không làm |
|----|----------------|--------------|-----------|-----------|
| **01** | `clin_event` **0–4** (eCRF v0.2) | D0–D7 | PCT/CFU/VAS + A4 | Mã từ chính \(Y_{D21}\) · train “early” bằng outcome |
| **02** | Timestamp triệu chứng / AE / adherence event | ≤D3 (ưu tiên D1) | VAS/CFU · C1–C3 | Coi VAS_D3 = event “sớm” khi trùng \(Y\) |
| **05** | AE ICU / turn miss / can thiệp chăm sóc | ≤D7 | PUSH/CFU/TURN · B1–B3 | Auto-treat vì 1 event · gộp với SA-01 |

**Zhou map SA-01 (chi tiết mã):** `CLIN_EVENT-ZHOU-MAP` · luyện: `CLIN_EVENT-CODING-VIGNETTES`.

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
| `ALERT-CROSS-SA-ATLAS` | Event + \(Z\) đứng → hành động nội bộ (A4/C/B) |
| `LEAKAGE-CROSS-SA-ATLAS` | Event/feature sau \(t^*\) hoặc trùng \(Y\) → không đưa M early |
| `CLIN_EVENT-CROSS-SA-ATLAS` | (file này) schema event × SA |

## Cấm

- Coi atlas PREP = STREAK DONE  
- Vignette / map de-ID = BN thật có PHI  
- Order PEA vì đã mã hoá đủ `clin_event`  

## Liên kết

- **Thẻ khoa học:** **`CLIN_EVENT-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`
- `CLIN_EVENT-ZHOU-MAP-v0.1.md` · `CLIN_EVENT-CODING-VIGNETTES-v0.1.md`  
- **Micro-drill 5′:** `CLIN_EVENT-5MIN-MICRO-DRILL-v0.1.md` (T7)  
- `BN-VISIT-MAP-TEMPLATE-v0.1.md` · `../y-te-so-precure-bridge-v0.1.md`  
- EQ: `../equations/EQ-SA01|02|05-early-warning-v0.1.md`  
- `ALERT-CROSS-SA-ATLAS` · `LEAKAGE-CROSS-SA-ATLAS`  
- Bridge #0: `EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01` · drill: `STUDY-SHEET-MULTI-OMICS-ES-DRILL`
