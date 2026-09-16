# Micro-drill 5′ — CONSORT × EQ (placement ES · ladder Z · ≠ primary)

**Mã:** CONSORT-EQ-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5** · sau `CONSORT-5MIN` / `CONSORT-SPIRIT-5MIN` / `SPIRIT-EQ-5MIN` · trước claim “đã báo ES đúng chỗ”  
**Goal:** ACTIVE · ES = exploratory · primary không đổi · M0–M3 / AUROC demo ≠ hàng primary · L3 **CLOSED** · PREP ≠ DONE  

## Một câu

> CONSORT×EQ 5′ = neo 1 SA + ladder M0–M3 trên \(Z\) → **đặt** ES ở Methods/Results exploratory — **không** cùng hàng primary; sandbox/`verify.sh` **không** vào Results lâm sàng.

## Drill (điền)

```text
SA neo: 01 | 02 | 05 — chọn: ________
EQ sibling: EQ-M0M3 | EQ02-M0M3 | EQ05-M0M3 — chọn: ________
Primary CONSORT hàng: D21 | ΔVAS | ΔPUSH — ghi: ________
1 dòng Z / M0→M3 (exploratory only): ________
M0–M3 / AUROC demo đặt ở: PRIMARY | SECONDARY | EXPLORATORY | KHÔNG BÁO — chọn (không PRIMARY): ________
Sandbox / verify.sh vào Results lâm sàng? KHÔNG — vì: ________
CONSORT-AI extension cần ngay? CHƯA | [CẦN XÁC NHẬN] — ghi: ________
Cặp đã đụng: CONSORT-5MIN | CONSORT-SPIRIT | SPIRIT-EQ | SAP-EQ | TRIPOD-EQ | EQ ladders — ghi: ________
1 việc nhỏ ≤30′ (placement sheet / EQ Drill 10′ / SAP ES): ________
Đóng Goal / coi báo cáo CLOSED vì CONSORT×EQ? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| CONSORT alone | `CONSORT-5MIN` · `CONSORT-ES-PLACEMENT` |
| CONSORT×SPIRIT | `CONSORT-SPIRIT-5MIN` |
| CONSORT-SPIRIT×EQ | **`CONSORT-SPIRIT-EQ-5MIN`** · `CONSORT-SPIRIT-5MIN` |
| SPIRIT×EQ | `SPIRIT-EQ-5MIN` |
| EQ ladders | `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` |
| AI claim | `TRIPOD-EQ-5MIN` · `SYNTH-5MIN` |

## Cấm

- Đặt ES / AUROC sandbox cùng hàng primary  
- Coi Git/`verify.sh` = Results lâm sàng  
- Đóng Goal vì đã điền placement × ladder  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5) · Protocol: `../../rituals/daily-protocol.md`  
- DOI: CONSORT 2010 [10.1136/bmj.c332](https://doi.org/10.1136/bmj.c332)
