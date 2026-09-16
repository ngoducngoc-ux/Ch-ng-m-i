# Micro-drill 5′ — ImageJ / PCT_EPITH QA (SA-01)

**Mã:** IMAGEJ-QA-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T2** · EPI early-window · Ngày 10 · trước claim AI trên % biểu mô  
**Goal:** ACTIVE · primary D21 ImageJ **không đổi** · QA trước AUROC · L3 CLOSED · PREP ≠ DONE

## Một câu

> Early-signal trên PCT_EPITH chỉ đáng tin nếu **ảnh + SOP đo** đủ QA — không train “sớm” bằng PCT D21, không bỏ qua inter-rater.

## Drill (điền)

```text
t* = D21 · Y = biểu mô 100% ImageJ
t' ôn hôm nay: D0 | D3 | D7
SOP ảnh hôm nay đủ? (khoảng cách/ánh sáng/góc): CÓ | CHƯA — thiếu: ________
Blinded / 2nd rater trên subset? CÓ | CHƯA | N/A
PCT_EPITH_D21 làm predictor early? KHÔNG — vì: ________
1 rủi ro nếu AI trên % lệch đo:
1 câu gắn EPI card / EQ-SA01:
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Early window | `EPI-SA01-EARLY-WINDOW` · **`IMAGEJ-EPI-5MIN`** · `EPI-5MIN` |
| Token×EQ | **`IMAGEJ-EQ-5MIN`** · already_token · `EQ-SIBLING-MAP` |
| IMAGEJ×EQ | **`IMAGEJ-EQ-5MIN`** · EQ ladders |
| EQ / leakage | `EQ-SA01` · `LEAKAGE-5MIN` (PCT D21) |
| ALERT A (QA ImageJ) | `ALERT-5MIN` · `ALERT-SA01` |
| eCRF Z | `EH-SA01-ZX-variables` · dictionary v0.2 |

## Cấm

- Claim AUROC trên PCT khi ảnh chưa chuẩn SOP  
- Dùng PCT D21 làm “early feature”  
- Order PEA vì đã “QA xong trên giấy”  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2)  
- Endpoints Ngày 10 · Protocol: `../../rituals/daily-protocol.md`

- Cặp T2: `EPI-5MIN-MICRO-DRILL`
