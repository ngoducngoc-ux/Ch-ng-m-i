# Micro-drill 5′ — Leakage thời gian (pitfall #1)

**Mã:** LEAKAGE-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T4** (ưu tiên) · EQ T2/T6 · drill B · Ngày 20 · Q3 #8  
**Goal:** ACTIVE · sandbox ≠ BN · G2/L3 CLOSED · PREP ≠ DONE  
**Pitfall:** ML-OMICS #1 · DOI TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594) (báo cáo trung thực)

## Một câu

> Trước khi nhìn AUROC — hỏi feature có **timestamp &lt; \(t^*\)** và **không trùng định nghĩa \(Y\)** không; M1 SA-02 + VAS_D3 = QC leakage, ≠ evidence.

## Drill (điền — 1 SA)

```text
Thứ: T2|T4|T6 · SA: 01|02|05
t* / Y: ________
1 feature sẽ là leakage nếu vào M early: ________
Vì sao (sau t* | trùng Y | mã từ Y): ________
1 feature HỢP LỆ cho t' hôm nay: ________
Sandbox AUROC “đẹp” → claim BN? KHÔNG — vì: ________
```

## Đối chiếu nhanh

| SA | Leakage điển hình | Early đúng |
|----|-------------------|------------|
| 01 | PCT D21 · event từ \(Y_{D21}\) | \(Z\)/`clin_event` ≤D7 |
| 02 | **M1 + VAS_D3** gần \(Y_{\text{relief}}\) · **`VAS-LEAK-5MIN`** | D1/CFU · M1* |
| 05 | PUSH_D14 làm “early” | \(t'\le D7\) · component exploratory |
| Atlas | ma trận đầy đủ | `LEAKAGE-CROSS-SA-ATLAS` |
| Pair densify | T4/T6/CN | **`LEAK-CROSS-5MIN`** |
| Cặp | TRIPOD / DEID / SYNTH trước train | `TRIPOD-5MIN` · `DEID-5MIN` · `SYNTH-5MIN` |

## Cấm

- Báo M1 sandbox AUROC như early-signal lâm sàng  
- Mở G2 vì đã “phát hiện” leakage trên synthetic  
- Một câu “không leakage” cho cả 3 SA  

## Liên kết

- PITFALLS 5′: **`PITFALLS-5MIN-MICRO-DRILL`**

- Atlas: `LEAKAGE-CROSS-SA-ATLAS-v0.1.md` · Pitfalls: `../guides/ML-OMICS-PITFALLS-v0.1.md`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3-v0.1.md` (T4 · EQ days)  
- EQ-SA02 M1 note · Protocol: `../../rituals/daily-protocol.md`

- Cặp T4: `VAS-5MIN-MICRO-DRILL`

- Cặp SAP ES §7: **`SAP-ES-5MIN-MICRO-DRILL`**
