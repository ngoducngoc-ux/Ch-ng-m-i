# Micro-drill 5′ — SAP-ES SA-01 (§7 blind/leakage · 7.1 Hawthorne · ≠ primary)

**Mã:** SAP-ES-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5** · sau `AMENDMENT-ES-5MIN` / `SPIRIT-5MIN` · trước claim AUROC / interim  
**Goal:** ACTIVE · SAP ES = exploratory · primary D21 không đổi · §7 no leakage · 7.1 ≠ primary · PREP ≠ DONE  
**Spec:** `SAP-SA01-ES-v0.1-DRAFT` §7–7.1 · `AMENDMENT-OUTLINE-SA01-ES` · SPIRIT S2

## Một câu

> SAP-ES 5′ = mô hình early chỉ predictors **trước/cùng D7**; ImageJ mù PROBE; sensitivity 7.1 (compliance) **không** giải thích primary; AUROC synthetic **≠** bằng chứng BN; **không** adaptive RCT vì tín hiệu sớm.

## Drill (điền)

```text
Primary D21 có đổi trong SAP ES? KHÔNG
Predictors sau D7 vào model “early”? KHÔNG — nếu lệch: ________
ImageJ đánh giá mù nhóm (PROBE)? CÓ | CHƯA [CẦN XÁC NHẬN] | N/A — ghi: ________
§7.1 +compliance / subset CLIN_EVENT = primary? KHÔNG
Adaptive / dừng sớm / đổi nhánh vì ES? KHÔNG
AUROC synthetic / sandbox = bằng chứng BN? KHÔNG
X_mol trong v0.1 SAP ES? KHÔNG (trước G1–G2)
Cặp đã đụng: AMENDMENT-ES | SPIRIT-5MIN | LEAKAGE | HAWTHORNE | ALERT-HAWTHORNE | TRIPOD — ghi: ________
1 việc nhỏ ≤30′ (SAP §7 skim / visit map DM / amendment S2 1 câu): ________
Đóng Goal / coi SAP CLOSED vì drill? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| SAP nháp đầy đủ | `SAP-SA01-ES` (hypotheses) |
| Token×EQ | **`SAP-EQ-5MIN`** · already_token · `EQ-SIBLING-MAP` |
| Amendment outline | `AMENDMENT-ES-5MIN` · `AMENDMENT-OUTLINE-SA01-ES` |
| Leakage | `LEAKAGE-5MIN` · atlas |
| Hawthorne / ALERT | `HAWTHORNE-5MIN` · `ALERT-HAWTHORNE-5MIN` · `PB008-5MIN` |
| SPIRIT S1–S3 | `SPIRIT-5MIN` |
| TRIPOD / AI claim | `TRIPOD-5MIN` · `SYNTH-5MIN` · **`TRIPOD-EQ-5MIN`** |
| SAP×EQ | **`SAP-EQ-5MIN`** · EQ ladders |

## Cấm

- Đưa biến sau D7 vào model “early”  
- Diễn giải ΔAUROC 7.1 = hiệu quả sản phẩm / primary  
- Adaptive RCT hoặc đổi primary vì ES  
- Claim sandbox = bằng chứng lâm sàng  

## Liên kết

- Draft: `../hypotheses/SAP-SA01-ES-v0.1-DRAFT.md` · Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5)  
- Protocol: `../../rituals/daily-protocol.md` · PB-008: `PB-008-participation-effects`
