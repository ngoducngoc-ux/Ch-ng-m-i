# clin_event — thẻ khoa học 1 trang (dọc L1 · Zhou analog · sớm–dọc–AI)

**Mã:** CLIN_EVENT-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**DOI neo:** Zhou Nature prediabetes [10.1038/s41586-019-1231-2](https://doi.org/10.1038/s41586-019-1231-2)  
**Dùng khi:** Makeup Zhou 18/09 · T7 · EQ L1 · BN-VISIT · sau STREAK≥3  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · event trên \(Z\) **trước** \(X\) · không PHI · G2 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn analog Zhou trên Smart A: omics nhảy khi có **sự kiện** → bắt bằng **event dọc** trên eCRF (ID–visit–time–event–\(Z\)) — **không** mã event từ \(Y(t^*)\), **không** mở omics vì đã có schema.

**Mở song song:** thẻ này · `ZHOU-STREAK3-SCIENCE-CARD` · `CLIN_EVENT-CROSS-SA-ATLAS` · `CLIN_EVENT-ZHOU-MAP`

## Ba SA → ba schema (giữ / bỏ)

| SA | Schema sự kiện | Cửa sổ early | Giữ | Bỏ |
|----|----------------|--------------|-----|-----|
| **01** | `clin_event` 0–4 (eCRF v0.2) | D0–D7 | PCT/CFU/VAS + A4 cùng visit | Mã từ \(Y_{D21}\) · train “early” bằng outcome |
| **02** | Timestamp triệu chứng / AE / adhere | ≤D3 (ưu tiên D1) | VAS/CFU · C1–C3 | Coi VAS_D3 = event sớm khi trùng \(Y\) |
| **05** | AE ICU / turn miss / care event | ≤D7 | PUSH/CFU/TURN · B1–B3 | Auto-treat vì 1 event · gộp SA-01 |

## Phương trình L1

```text
L1 đủ:  StudyID + Visit(t) + timestamp + event + Z cùng cửa sổ
Event ≠ Y(t*)     ·     t' ≪ t*
X / omics: CLOSED  — event schema ≠ lý do order PEA
PHI: không vào git / Drive public
```

## Checklist 15′ (1 SA)

```text
Thứ: T2|T4|T6|T7 · SA: 01|02|05 — chọn: ________
Event hôm nay (mã / mô tả): ________
Visit + timestamp đủ L1? CÓ | CHƯA — thiếu: ________
Z cùng cửa sổ: ________
1 câu event ≠ label Y(t*): ________
1 câu vì sao chưa cần X/omics: ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / `CLIN_EVENT-…` | Schema event × SA |
| `ALERT-SCIENCE-CARD` | Event+\(Z\) → hành động nội bộ |
| `LEAKAGE-SCIENCE-CARD` | Event/feature sau \(t^*\) hoặc trùng \(Y\) → không vào M early |

Cặp: `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · `BN-VISIT-5MIN` · **`CLIN-BN-SCIENCE-CARD`** · `CLIN-BN-5MIN`

## Cấm

- PHI trong repo · event = primary label · order omics vì schema  
- Agent tick DONE · đóng Goal  

## Liên kết

**`CLIN-BN-SCIENCE-CARD`** · `ZHOU-STREAK3-SCIENCE-CARD` · `CLIN_EVENT-CROSS-SA-ATLAS` · `CLIN_EVENT-ZHOU-MAP` · `CLIN_EVENT-5MIN` · `CLIN-BN-5MIN` · `BN-VISIT-5MIN` · `ALERT-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · **`L1L2L3-SCIENCE-CARD`** · **`DEID-SCIENCE-CARD`** · **`BN-VISIT-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3`
