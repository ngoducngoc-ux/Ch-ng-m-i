# Micro-drill 5′ — CONSORT early-signal placement (SA-01/02/05)

**Mã:** CONSORT-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5** · bridge #3 DESIGN-YTESO · Ngày 17 · sau `SPIRIT-5MIN` · trước claim “đã báo ES đúng chỗ”  
**Goal:** ACTIVE · ES = exploratory · primary D21/ΔVAS/ΔPUSH không đổi · L3 CLOSED · PREP ≠ DONE  
**DOI:** CONSORT 2010 [10.1136/bmj.c332](https://doi.org/10.1136/bmj.c332)

## Một câu

> SPIRIT **khai** ES trước; CONSORT **đặt** ES ở Methods/Results exploratory — **không** cùng hàng primary; `verify.sh`/sandbox **không** vào Results lâm sàng.

## Drill (điền)

```text
Primary outcome hàng CONSORT (SA): D21 | ΔVAS | ΔPUSH — ghi: ________
M0–M3 / AUROC demo đặt ở: PRIMARY | SECONDARY | EXPLORATORY | KHÔNG BÁO — chọn: ________
Sandbox / verify.sh vào Results lâm sàng? KHÔNG — vì: ________
CONSORT-AI extension cần ngay? CHƯA | [CẦN XÁC NHẬN] — ghi: ________
1 việc nhỏ ≤30′ (placement / SAP / PI): ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Placement đầy đủ | `CONSORT-ES-PLACEMENT` |
| SPIRIT trước báo cáo | `SPIRIT-5MIN` · `SPIRIT-SA01-MAP` · **`CONSORT-SPIRIT-5MIN`** · **`SPIRIT-EQ-5MIN`** |
| CONSORT×EQ | **`CONSORT-EQ-5MIN`** · EQ ladders |
| Bridge T2 | `DESIGN-YTESO-EARLY-SIGNAL-BRIDGE` |
| Cặp AI / phê duyệt | `TRIPOD-5MIN` · `SYNTH-5MIN` · `TT43-5MIN` |

## Cấm

- Đặt ES / AUROC sandbox cùng hàng primary D21  
- Coi `verify.sh` PASS = kết quả RCT  
- Publish model AI mà quên CONSORT-AI `[CẦN XÁC NHẬN]`  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5)  
- Ritual: `DESIGN-YTESO-AI-RITUAL-CARD` · Protocol: `../../rituals/daily-protocol.md`
