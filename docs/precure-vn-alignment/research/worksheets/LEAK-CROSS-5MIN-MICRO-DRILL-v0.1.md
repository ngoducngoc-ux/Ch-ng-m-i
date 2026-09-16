# Micro-drill 5′ — LEAKAGE × CROSS-SA (Y(t*) ≠ early · không gộp Y)

**Mã:** LEAK-CROSS-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4**/ **T6**/ **CN** · sau `LEAKAGE-5MIN` / `CROSS-SA-5MIN` / `CROSS-EQ-5MIN` · trước claim “một model early chung” hoặc AUROC gộp SA  
**Goal:** ACTIVE · mỗi SA một \(Y(t^*)\) · không dùng \(Y(t^*)\) làm predictor early · L3 **CLOSED** · PREP ≠ DONE  

## Một câu

> LEAK×CROSS 5′ = so schema \(t^*\)/\(Z\) sớm giữa SA **và** cấm leakage: **không** đưa outcome primary làm feature early · **không** gộp Y · AUROC sandbox ≠ BN.

## Drill (điền)

```text
SA đang ôn (không gộp): 01 | 02 | 05 — chọn: ________
t* primary: D21 | VAS_D3 | PUSH_D14 — ghi: ________
1 Z sớm hợp lệ (không = Y(t*)): ________
Leakage nếu dùng Y(t*) làm early? CÓ — ví dụ 1 dòng: ________
Gộp Y SA-01+02+05? KHÔNG — vì: ________
Chọn cờ / power theo AUROC synthetic? KHÔNG
VAS_D3 (SA-02 M1) / PUSH_D14 = early feature? KHÔNG
Omics vì “đã so sánh + tránh leak”? KHÔNG
Cặp đã đụng: LEAKAGE | VAS-LEAK | CROSS-SA | CROSS-EQ | EQ ladders | TRIPOD-EQ | PB007-EQ — ghi: ________
1 việc nhỏ ≤30′ (LEAKAGE atlas / CROSS map / EQ sibling): ________
Đóng Goal vì LEAK×CROSS? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Leakage alone | `LEAKAGE-5MIN` · `LEAKAGE-CROSS-SA-ATLAS` · `VAS-LEAK-5MIN` |
| CROSS alone | `CROSS-SA-5MIN` · `CROSS-EQ-5MIN` |
| EQ ladders | `EQ-M0M3` · `EQ02-M0M3` · `EQ05-M0M3` |
| AI claim | `TRIPOD-EQ-5MIN` · `SYNTH-5MIN` |
| SAP×EQ | **`SAP-EQ-5MIN`** · `SAP-ES-5MIN` |
| ALERT×CROSS | **`ALERT-CROSS-5MIN`** · `ALERT-HAWTHORNE-5MIN` |
| LEAKAGE×EQ | **`LEAKAGE-EQ-5MIN`** · `LEAKAGE-5MIN` |

## Cấm

- Outcome \(t^*\) làm predictor “early” (PCT D21 · VAS_D3-as-M1 claim · PUSH_D14)  
- Một model / một \(Y\) cho nhiều SA  
- Order L3 vì schema “đã khớp” và “đã tránh leak”  

## Liên kết

- Atlas: `LEAKAGE-CROSS-SA-ATLAS-v0.1.md` · Map: `CROSS-SA-EARLY-SIGNAL-MAP-v0.1.md`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4/T6/CN) · Protocol: `../../rituals/daily-protocol.md`
