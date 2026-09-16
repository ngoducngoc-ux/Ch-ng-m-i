# Micro-drill 5′ — CONSORT × SPIRIT (khai ES · đặt ES · ≠ primary)

**Mã:** CONSORT-SPIRIT-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T5** · Ngày 15–17 · sau `SPIRIT-5MIN` + `CONSORT-5MIN` · trước claim “đã báo ES đúng”  
**Goal:** ACTIVE · SPIRIT khai · CONSORT đặt exploratory · primary không đổi · PREP ≠ DONE  
**DOI:** SPIRIT 2013 [10.7326/0003-4819-158-3-201302050-00583](https://doi.org/10.7326/0003-4819-158-3-201302050-00583) · CONSORT 2010 [10.1136/bmj.c332](https://doi.org/10.1136/bmj.c332)

## Một câu

> CONSORT×SPIRIT 5′ = S1–S3 phải **vào amendment** trước; khi báo cáo, ES/AUROC chỉ **exploratory** — **không** cùng hàng primary D21 / VAS_D3 / PUSH_D14; sandbox/`verify.sh` **không** vào Results lâm sàng.

## Drill (điền)

```text
SPIRIT S1–S3 đã trong protocol/amendment? CHƯA | NHÁP | CÓ — ghi: ________
Primary CONSORT hàng (SA): D21 | ΔVAS | ΔPUSH — chọn: ________
ES / M0–M3 / AUROC đặt: PRIMARY | SECONDARY | EXPLORATORY | KHÔNG BÁO — chọn: ________
Cùng hàng primary với ES? KHÔNG
Sandbox / verify.sh → Results lâm sàng? KHÔNG
Adaptive primary vì đã đọc SPIRIT+CONSORT? KHÔNG
Cặp đã đụng: SPIRIT-5MIN | CONSORT-5MIN | AMENDMENT-ES | SAP-ES | TRIPOD | SYNTH | TT43-AMEND — ghi: ________
1 việc nhỏ ≤30′ (placement sheet / SPIRIT map / amendment S1): ________
Đóng Goal / coi reporting CLOSED vì drill? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| SPIRIT alone | `SPIRIT-5MIN` · `SPIRIT-SA01-MAP` |
| CONSORT alone | `CONSORT-5MIN` · `CONSORT-ES-PLACEMENT` |
| Amendment / SAP | `AMENDMENT-ES-5MIN` · `SAP-ES-5MIN` |
| TT43 | `TT43-AMEND-5MIN` · `TT43-5MIN` |
| AI / synth | `TRIPOD-5MIN` · `SYNTH-5MIN` |

## Cấm

- Báo ES cùng hàng primary  
- Coi đọc SPIRIT/CONSORT = protocol đã duyệt hoặc paper đã đúng  
- Đưa sandbox AUROC vào Results lâm sàng  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T5) · Protocol: `../../rituals/daily-protocol.md`  
- Bridge: `DESIGN-YTESO-EARLY-SIGNAL-BRIDGE`
