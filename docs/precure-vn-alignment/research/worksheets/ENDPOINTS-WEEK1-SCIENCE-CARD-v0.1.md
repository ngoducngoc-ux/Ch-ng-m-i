# Endpoints week 1 — thẻ khoa học 1 trang (Ngày 08–14 · \(t^*\neq Z\) sớm)

**Mã:** ENDPOINTS-WEEK1-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**DOI neo:** Stotts PUSH [10.1093/gerona/56.12.m795](https://doi.org/10.1093/gerona/56.12.m795) · STPIS VAS [10.1186/1745-6215-15-263](https://doi.org/10.1186/1745-6215-15-263)  
**Dùng khi:** T4/T6 (và T2 Ngày 10) sau STREAK≥3 · logs `2026-09-24`…`09-30` · bridge #2  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · cờ đầu **SA-01** · G2 **CLOSED** · không gộp \(Y\) · PREP ≠ DONE  

## Mục đích

Ôn khung Precure/Smart A trên **ba RCT người** (01/02/05) + **hai cổng** (03/04): mỗi SA một \(Y(t^*)\); early-signal = \(Z(t')\) với \(t'\ll t^*\) — **không** đổi primary, **không** Dx app, **không** mở \(X\) trước G2.

**Mở song song:** thẻ này · `ENDPOINTS-EARLY-SIGNAL-RITUAL-CARD` · `ENDPOINTS-CROSS-SA-BRIDGE` · `LEAKAGE-CROSS-SA-ATLAS`

## Ba trụ RCT → ba ý (giữ / bỏ)

| SA | \(t^*\) | Giữ (sớm–dọc–AI) | Bỏ |
|----|---------|------------------|-----|
| **05** PUSH | D14 | Component (exudate/TURN) + chuỗi D0–D7 → exploratory \(Y\) | \(\Delta\)PUSH = app ICU Dx · gộp với D21 |
| **01** biểu mô | D21 | \(Z\) D0–D7 (PCT/CFU/VAS/`clin_event`) exploratory | AUROC sandbox = lâm sàng · PCT D21 = “early” |
| **02** VAS | D3 | Series D0–D3 · M1\* ưu tiên D1/CFU trước D3 | Train bằng `VAS_D3` làm feature (= leakage) · marker = primary |

**Cổng:** SA-03 biofilm ATCC ≠ Dx BN · SA-04 ISO trước mọi L3 người.

## Phương trình — không train chung

```text
Mỗi SA riêng:
  P(Y_SA=1) = σ( β0 + β_Z·Z_SA(t') + … )   ·  t' ≪ t*_SA
  X_mol chỉ sau G2 trên SA đó (mặc định CLOSED)
Cấm: 1 model gộp VAS + PUSH + biểu mô
```

## Checklist 15′ (1 ngày endpoints)

```text
Ngày: 08|09|10|11|12|13|14 — chọn: ________
SA đang ôn: 05|05|01|weekly|02|03|04
1 câu t* ≠ Z sớm: ________
1 câu vì sao KHÔNG gộp endpoint với SA khác: ________
Leakage check hôm nay? CÓ | CHƯA | N/A (atlas)
1 việc ≤30′ (ritual card hàng | EQ M0–M3 | bridge fill): ________
Order omics / đổi primary? KHÔNG
```

## Y tế số (L1→L2→L3 — PB-009)

| Layer | Việc endpoints tuần | Hôm nay |
|-------|---------------------|---------|
| L1 | Visit + \(Z\) + `clin_event` theo SA | eCRF / REDCap build |
| L2 | M0–M3 exploratory · de-ID | Sandbox = QC ≠ BN |
| L3 | Omics / marker gated | **CLOSED** đến G2 |

Cặp: `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · `PEA-WEEK1-SCIENCE-CARD` (L3 reminder)

## Cấm

- Gộp endpoint · claim “early-signal đã chứng minh” từ `verify.sh`  
- App Dx ICU / họng / vết thương vì đã ôn PUSH/VAS  
- Agent tick DONE · đóng Goal  

## Liên kết

`ENDPOINTS-EARLY-SIGNAL-RITUAL-CARD` · `ENDPOINTS-CROSS-SA-BRIDGE` · `PUSH-SA05-COMPONENTS` · `EPI-SA01-EARLY-WINDOW` · `VAS-SCALE-HARMONIZE-SA02` · `EQ-SA01|02|05` · `CROSS-SA-5MIN` · **`LEAKAGE-SCIENCE-CARD`** · `LEAK-CROSS-5MIN` · **`EQ-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3` · **`IMAGEJ-SCIENCE-CARD`** · **`EPI-SCIENCE-CARD`** · **`CROSS-SA-SCIENCE-CARD`**
