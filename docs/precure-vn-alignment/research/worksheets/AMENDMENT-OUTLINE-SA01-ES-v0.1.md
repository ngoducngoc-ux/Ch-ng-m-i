# Outline amendment — SA-01 early-signal exploratory (1 trang)

**Mã:** AMENDMENT-OUTLINE-SA01-ES-v0.1  
**Ngày:** 2026-09-16  
**Dành cho:** PI / coordinator · **không** gửi HĐĐĐ từ bản PREP agent  
**Nguồn:** `SPIRIT-SA01-MAP` S1–S3 · `TT43-AMENDMENT-HOOKS` · eCRF v0.2 · SAP ES  
**Ritual:** Ngày 74 · card `Q2-AMENDMENT-INTERIM-RITUAL-CARD`

## Mục đích (1 câu)

Bổ sung **exploratory early-signal** (Z dọc · `clin_event` · M0–M3) vào hồ sơ TN mà **không** đổi primary endpoint D21 biểu mô hóa.

## Năm bullet draft (PI chỉnh trước khi nộp)

1. **Outcomes exploratory (SPIRIT S1)**  
   Mô tả trong đề cương/amendment: tín hiệu sớm trên cửa sổ D0–D7 (vd. ΔPCT_EPITH, CFU, VAS_DRESS) và `clin_event` 0–4 — **hypothesis-generating**, không thay primary D21.  
   Pointer: `SAP-SA01-ES-v0.1-DRAFT.md` · `SPIRIT-SA01-MAP`

2. **Không adaptive / không đổi nhánh (SPIRIT S2)**  
   Interim mô tả / early-signal **không** kích hoạt dừng sớm hiệu quả hay đổi phân bổ RCT. Policy SAP ES §7 — PI xác nhận 1 câu trong log.

3. **Data / eCRF version (SPIRIT S3)**  
   Cite dictionary **v0.2** + trường `clin_event` trên visit repeating; luồng DM staging → production.  
   Pointer: `DATA-MANAGER-HANDOFF-REDCap-v0.2.md` · CSV Drive v0.2

4. **TT43 / phê duyệt VN**  
   Hook: bổ sung CRF exploratory · (nếu sau này) nested biospecimen/ICF · bảo mật dữ liệu · AE.  
   Số điều: **`[CẦN XÁC NHẬN]`** — PI dán từ PDF TT 43/2024/TT-BYT (`TT43-AMENDMENT-HOOKS`).

5. **Nested omics / G1–G2 (nếu có mục mẫu)**  
   Chỉ mở sau cổng G1–G2 trên **data thật** + ICF; amendment không bypass.  
   Pointer: `SPIRIT-NESTED-G1-CHECKLIST` · `G2-READINESS` · PB-009 L1→L2 trước L3

## Ngôn ngữ cấm trong bản nộp

- “Chẩn đoán sớm lâm sàng đã chứng minh từ sandbox”  
- “AUROC synthetic = bằng chứng BN”  
- Đổi primary D21 / claim diệt khuẩn 100% / an toàn tuyệt đối  

## Checklist trước nộp (PI)

- [ ] Primary D21 không đổi  
- [ ] S1–S3 có đoạn trong amendment  
- [ ] ≥1 số điều TT43 thật (không để trống nếu bắt buộc form)  
- [ ] DM đã biết version eCRF  
- [ ] G2 vẫn CLOSED trừ khi mục nested đã duyệt riêng  

## Liên kết

`Q2-AMENDMENT-INTERIM-RITUAL-CARD` · bridge `Q2-AMENDMENT-INTERIM-EARLY-SIGNAL-BRIDGE` · `SCIENCE-BRIDGES-INDEX` #6 · `DECISION-FLAGSHIP-SA01` · `PI-ACTIONS-NOW`

## Micro-drill 5′

- **`AMENDMENT-ES-5MIN-MICRO-DRILL-v0.1.md`** — S1–S3 + TT43 + nested gates · T5 · không gửi HĐĐĐ từ PREP
- **`SAP-ES-5MIN-MICRO-DRILL-v0.1.md`** — SAP §7/7.1 · không adaptive · T5
