# eCRF dictionary bổ sung — SA-01 early-signal (Precure)

**Mã:** eCRF-SA01-ES-v0.1  
**Ngày:** 2026-09-16  
**Mục đích:** bổ sung biến còn thiếu so với dictionary tối thiểu trong đề cương Ch.6, phục vụ exploratory early-signal (EH-SA01).  
**Trạng thái:** đề xuất tích hợp REDCap — `[CẦN XÁC NHẬN]` trước khi khóa CRF chính thức.

## Biến nền (đã có trong đề cương)

| Field | Label | Type | Validation |
|-------|-------|------|------------|
| SUBJ_ID | Mã đối tượng | text | `SA-01-XXX` |
| AGE | Tuổi | int | 18–70 (synopsis); dictionary ghi 18–75 → thống nhất `[CẦN XÁC NHẬN]` |
| GENDER | Giới | cat | 1=Nam, 2=Nữ |
| GROUP | Nhánh | cat | 1=Smart A, 2=Đối chứng |
| PRIMARY_OUT | Kết cục chính D21 | binary/num | biểu mô hóa 100% ImageJ |
| AE_OCCUR | Có AE | binary | 0/1 |
| COMPLETION | Hoàn thành | binary | 0/1 |

## Biến bổ sung — baseline / covariate

| Field | Label | Type | Validation | Visit |
|-------|-------|------|------------|-------|
| WOUND_TYPE | Loại tổn thương | cat | 1=vết thương ngoại khoa hở, 2=bỏng II, 3=bỏng III, 4=hỗn hợp | D0 |
| TBSA_PCT | % TBSA (nếu bỏng) | num | 0–\<20 theo inclusion | D0 |
| WOUND_SITE | Vị trí giải phẫu | text/cat | mã site chuẩn hóa | D0 |
| COMORBID_DM | Đái tháo đường | binary | 0/1 | D0 |
| COMORBID_SMOKE | Hút thuốc | cat | 0=không, 1=cũ, 2=hiện tại | D0 |

## Biến bổ sung — lặp theo visit (repeating instrument)

Visit codes đề xuất: `D0`, `D3`, `D7`, `D14`, `D21` (map D1–D3→D3; D5–D7→D7 nếu gộp theo EH-SA01).

| Field | Label | Type | Validation |
|-------|-------|------|------------|
| VISIT_CODE | Mã thăm | cat | D0/D3/D7/D14/D21 |
| VISIT_DATE | Ngày thăm | date | ISO |
| PCT_EPITH | % diện tích đã biểu mô (ImageJ) | num | 0–100 |
| AREA_OPEN_CM2 | Diện tích hở còn lại (cm²) | num | ≥0 |
| PHOTO_ID | ID ảnh chuẩn hóa | text | link media |
| VAS_DRESS | VAS đau rát khi thay băng | num | 0–10 |
| CULTURE_DONE | Có cấy định lượng | binary | 0/1 |
| CULTURE_CFU | Kết quả cấy (CFU/cm² hoặc log10) | num | ≥0; đơn vị ghi `CULTURE_UNIT` |
| CULTURE_UNIT | Đơn vị cấy | cat | 1=CFU/cm2, 2=log10 |
| CLIN_INFECTION | Nhiễm trùng lâm sàng | binary | 0/1 |
| ADHERENCE | Tuân thủ thay băng đúng lịch kể từ visit trước | cat | 0=không, 1=một phần, 2=đầy đủ |
| AE_LOCAL | AE tại chỗ mới | binary | 0/1 |

## Mapping exploratory models

| Model | Predictors (visit ≤ D7) | Outcome |
|-------|-------------------------|---------|
| M0 | PCT_EPITH@D0 + WOUND_TYPE + AGE + GROUP | PRIMARY_OUT@D21 |
| M1 | M0 + PCT_EPITH@D3 + PCT_EPITH@D7 | PRIMARY_OUT@D21 |
| M2 | M1 + CULTURE_CFU@D0 + CULTURE_CFU@D7 | PRIMARY_OUT@D21 |
| M3 | M2 + VAS_DRESS trajectory D0–D7 | PRIMARY_OUT@D21 |

So sánh AUROC/Brier M0→M3; pre-specify trong SAP exploratory.

## Việc tích hợp

- [ ] Review với Data Manager REDCap  
- [ ] Đồng bộ tuổi inclusion 18–70 vs dictionary 18–75  
- [ ] Thêm vào phụ lục đề cương / amendment nếu CRF đã khóa
