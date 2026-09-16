# eCRF dictionary bổ sung — SA-02 early-signal (Precure)

**Mã:** eCRF-SA02-ES-v0.1  
**Ngày:** 2026-09-16  
**Primary (synopsis):** ΔVAS họng D3−D0 · N=100  
**Trạng thái:** đề xuất REDCap — `[CẦN XÁC NHẬN]` trước amendment.

## Biến nền

| Field | Label | Type | Visit |
|-------|-------|------|-------|
| SUBJ_ID | Mã đối tượng | text | — |
| AGE | Tuổi | int | D0 |
| GENDER | Giới | cat | D0 |
| GROUP | Nhánh | cat | randomization |
| DX_CAT | Chẩn đoán phân loại | cat | D0 |

## Repeating visit (`visit_es`)

| Field | Label | Mốc |
|-------|-------|-----|
| VISIT_CODE | D0 / D1 / D3 / D5 / D7 | |
| VAS_THROAT | VAS đau rát họng 0–10 | mọi visit |
| CULTURE_DONE / CULTURE_CFU | Cấy định lượng họng | D0, D1, D3 |
| ADHERE_SPRAY | Tuân thủ súc/xịt | D0–D7 |
| CLIN_EVENT / CLIN_EVENT_NOTE | Sự kiện lâm sàng (Zhou) | mọi visit |
| AE_LOCAL | AE tại chỗ | mọi visit |

## Outcome

| Field | Label | Note |
|-------|-------|------|
| VAS_D0 / VAS_D3 | Snapshot primary | hoặc derive từ visit |
| DELTA_VAS_D3 | D3−D0 | **Primary** |
| RELIEF_D3 | Δ≤−2 (exploratory binary) | secondary SAP ES |

## Mô hình M0–M3 (SAP ES)

| Model | Predictors (≤D3) | Outcome exploratory |
|-------|------------------|---------------------|
| M0 | VAS@D0 + DX_CAT + AGE + GROUP | RELIEF_D3 |
| M1 | M0 + VAS@D3 | RELIEF_D3 |
| M2 | M1 + CFU@D0 + CFU@D3 | RELIEF_D3 |
| M3 | M2 + CFU@D1 + ADHERE | RELIEF_D3 |

CSV import: `redcap_sa02_early_signal_dictionary_v0.1.csv`

## Việc tích hợp

- [ ] PI TMH: D1 visit bắt buộc hay optional  
- [ ] Review Data Manager (staging REDCap)  
- [ ] Không thay primary ΔVAS trong SAP chính
