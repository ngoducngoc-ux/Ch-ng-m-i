# PUSH components — SA-05 early-signal (N=80)

**Mã:** PUSH-SA05-COMPONENTS-v0.1  
**Ngày:** 2026-09-16 · **Cập nhật:** drill 8′ · ALERT/gate/shift hooks  
**Curriculum:** Ngày 08 · Daily stack **T6** · Stotts 2001 DOI [10.1093/gerona/56.12.m795](https://doi.org/10.1093/gerona/56.12.m795)  
**Primary đề cương:** ΔPUSH D14 (không đổi) · SAP ES exploratory · Goal ACTIVE · L3 **CLOSED**

## Một câu

> Early-signal ICU có thể nhìn **thành phần PUSH** (vd. exudate) + `TURN_ADHERE` trước D14 — **không** thay primary, **không** auto-treat.

## PUSH gồm gì (Stotts)

| Thành phần | Mô tả ngắn | Ghi chú ES |
|------------|------------|------------|
| **Length × width** | Diện tích ước lượng | Total PUSH thường dùng cho primary |
| **Exudate** | Mức xuất tiết (0–3) | Có thể **dẫn trước** total khi turn xoay trở kém |
| **Tissue type** | Loại mô (slough/granulation…) | Khó inter-rater — cần QA ảnh blinded |

## Gợi ý ưu tiên exploratory (N=80)

> SAP ES mô tả **total PUSH** cho M0–M3; **sensitivity** riêng **exudate + TURN_ADHERE** vì confounder ICU — không mở component làm co-primary.

## Liên hệ phương trình / ALERT / cổng

| Khối | File |
|------|------|
| EQ M0–M3 | `EQ-SA05-early-warning` · Drill 10′ |
| ALERT B1–B3 | `ALERT-SA05` · `ALERT-CROSS-SA-ATLAS` |
| Leakage | Không dùng PUSH_D14 làm “early” — `LEAKAGE-CROSS-SA-ATLAS` |
| L3 ICU | `L1L2L3-DAILY-GATE-CARD` — CLOSED |
| Shift 1 câu | `PRECURE-SHIFT-CROSS-SA-BANK` hàng SA-05 |

## Drill 8′ (điền — T6 / Ngày 08)

```text
t* = D14 · t' ≤ D7
Total PUSH vs 1 component early hôm nay: TOTAL | exudate | tissue | area
Vì sao N=80 không co-primary component: ________
TURN_ADHERE gắn trụ nào: Dọc | AI | Sớm
ALERT B__ nếu PUSH↑ sớm: ________
1 câu cấm auto-treat ICU:
1 câu Precure shift (≤25 từ):
```

## Việc nhỏ

- [ ] Rater training: inter-rater ICC trên subset ảnh trước khi claim AI trên PUSH  
- [ ] Không dùng synthetic SA-05 để chốt ngưỡng B1–B3 lâm sàng  
- [ ] T6: EQ-SA05 Drill 10′ + card này (hoặc thay một phần)

## Cấm

- Component = thay \(\Delta\)PUSH D14  
- Deploy ALERT B ra app ICU  
- Order omics ICU vì đã đọc Stotts / EQ  

## Liên kết

- Notes: `reading-notes/2026-09-24-push-stotts-2001.md`  
- SAP: `hypotheses/SAP-SA05-ES-v0.1-DRAFT.md`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T6) · Endpoints: `ENDPOINTS-CROSS-SA-BRIDGE`
