# eCRF dictionary bổ sung — SA-05 early-signal (ICU / PUSH)

**Mã:** eCRF-SA05-ES-v0.1  
**Ngày:** 2026-09-16  
**Primary:** ΔPUSH D14−D0 · N=80 · loét 2–4  
**Trạng thái:** `[CẦN XÁC NHẬN]` trước amendment ICU.

## Baseline

| Field | Label |
|-------|-------|
| STAGE_NPUAP | Giai đoạn loét D0 |
| ICU_DAYS | Số ngày nằm ICU tại D0 |
| BRADEN | Braden (nếu thu) |

## Repeating `visit_icu`

| Field | Visit |
|-------|-------|
| VISIT_CODE | D0, D3, D7, D14, D21 |
| PUSH_TOTAL | 0–17 |
| PUSH_AREA / PUSH_EXUDATE / PUSH_TISSUE | thành phần PUSH |
| CULTURE_CFU | D0, D3 |
| TURN_ADHERE | 0–2 adherence xoay trở |
| CLIN_EVENT | sự kiện ICU (sepsis workup, đổi KS…) |

## Outcome

| Field | Note |
|-------|------|
| DELTA_PUSH_D14 | Primary |
| IMPROVED_D14 | Δ≤−2 exploratory (SAP ES) |

## M0–M3

Khớp sandbox `sa05_early_signal_synthetic_m0_m3.py`.

CSV: `redcap_sa05_early_signal_dictionary_v0.1.csv`
