# Bridge — Endpoints × early-signal (SA-01 / 02 / 05) · refresh v0.1b

**Mã:** ENDPOINTS-CROSS-SA-BRIDGE-v0.1  
**Ngày:** 2026-09-16 (refresh sau MULTI-OMICS-PEA / EQ bank CLOSED)  
**Curriculum:** Ngày 08–14 · ôn Tier 3 CROSS-SA 33–36 · T4 rotation · bridge **#2**  
**Thẻ:** `ENDPOINTS-EARLY-SIGNAL-RITUAL-CARD` · **`ENDPOINTS-WEEK1-SCIENCE-CARD`** · `CROSS-SA-EARLY-SIGNAL-MAP` · **`CROSS-EQ`** · **`VAS-EQ`** · **`PUSH-EQ`** · **`PB001/002/003-EQ`**  
**Cờ đầu:** SA-01 · SA-02/05 = support · SA-03/04 = cổng (không RCT người) · EQ bank **CLOSED**  
**STREAK&lt;3?** Dừng · **`STREAK3-PACK`** · **`STREAK3-EQ`** · NOW · FILL-AID → tick **19/09** trước  
**Không:** gộp Y cross-SA · train chung · AUROC sandbox = evidence BN · invent EQ mới

## Một câu

> Cùng khung **\(t' \ll t^*\)** + M0–M3 trên \(Z\) dọc — nhưng **mỗi SA một \(Y(t^*)\)**; không train chung, không gộp endpoint, không lấy AUROC sandbox làm evidence BN — đúng hướng Smart A sớm–dọc–AI.

## Ma trận \(t^*\) / \(Y\) / \(Z\) sớm / M0–M3

| SA | \(t^*\) | \(Y\) (primary / ES binary) | \(Z\) sớm | M0 → M3 (ý) | \(X\) / omics |
|----|---------|------------------------------|-----------|-------------|---------------|
| **01** | D21 | \(Y_{D21}\)= biểu mô 100% | PCT/CFU/VAS/`clin_event` D0–D7 | Baseline → D3 → delta → D7+event | PEA sau G2 (`MULTI-OMICS-PEA` #1) |
| **02** | D3 | \(Y\)= relief \(\Delta\)VAS≤−2 (ES) · primary VAS D3 | VAS/CFU D0–D3 · **D1 `[CẦN XÁC NHẬN]`** | D0 → (+D3 sandbox*) → CFU → CFU+ADHERE | Marker niêm mạc gated · ≠ primary |
| **05** | D14 | \(Y\)= \(\Delta\)PUSH≤−2 | PUSH D0–D7 + TURN_ADHERE + CFU | D0 → D3/D7 → +CFU → +turn | G2 ICU · không app Dx |
| **03** | ATCC | — | — | — | In-vitro ≠ Dx BN |
| **04** | ISO | — | — | — | Trước mọi L3 người |

\*Sandbox SA-02 M1 gồm `VAS_D3` → **leakage có chủ đích để QC pipeline** (outcome gần \(Y\)); ritual khoa học ưu tiên D1/CFU trước D3 — xem `EQ-SA02` · atlas `LEAKAGE-CROSS-SA-ATLAS` · **`LEAKAGE-EQ`** / **`VAS-LEAK-EQ`**.

## Phương trình chung (không train chung)

```text
Mỗi SA riêng:
  P(Y_SA=1) = σ( β0 + β_Z·Z_SA(t') + β_g·GROUP + β_C·C_SA )
  t' ≪ t*_SA
  X chỉ sau G2 trên SA đó (mặc định CLOSED)
```

Chi tiết: `EQ-SA01` · `EQ-SA02` · `EQ-SA05` · **`PB001-EQ`** · **`PB002-EQ`** · **`PB003-EQ`**.

## Luồng một trang (STREAK≥3 · T4 / Ngày 08–14)

```text
STREAK <3? → STREAK3-PACK / STREAK3-EQ · dừng #2
        ↓ STREAK ≥3
OPENER (phiên đầu) → 1×EQ sibling (CROSS-EQ / VAS-EQ / PUSH-EQ / LEAKAGE-EQ) → #2
Chọn 1 SA · điền 1 hàng ma trận · 1 câu “không gộp Y”
Goal ACTIVE · G2 CLOSED · PREP ≠ DONE · synthetic ≠ BN
```

## Zhou / Nat Med / PEA — chỗ gắn

| Logic Precure | Artifact | Áp vào endpoints tuần B |
|---------------|----------|-------------------------|
| Sự kiện dọc trước endpoint | `#0` Zhou/NatMed · `CLIN_EVENT-CROSS-SA-ATLAS` | SA-01 `clin_event`; SA-02 timestamp; SA-05 AE/ICU |
| Actionable ≠ đổi primary | `ALERT-CROSS-SA-ATLAS` · **`ALERT-EQ`** | ALERT A/B/C nội bộ trên \(Z\) |
| Multi-omics sau L1–L2 | `#1` MULTI-OMICS-PEA · PB-009 | Không order vì đã có 3 JSON synthetic |

## Sandbox (chỉ QC)

| File | Dùng đúng | Cấm |
|------|-----------|-----|
| `synthetic_sa0{1,2,5}_m0_m3_metrics.json` | So cấu trúc feature sets | Chọn cờ đầu / claim lâm sàng theo AUROC |
| `verify.sh` | PASS/FAIL pipeline | “Đã chứng minh early-signal” |

## Ritual fill-in (Ngày 08–14)

```text
STREAK ≥3? ________ (nếu không → STREAK3 path)
Ngày: 08|09|10|11|12|13|14 | T4 rotation
SA đang ôn: 05|05|01|weekly|02|03|04
EQ sibling kèm (1): ________
1 câu t* ≠ Z sớm:
1 câu vì sao không gộp endpoint với SA khác:
Goal: ACTIVE · densify ≠ DONE
```

## Cấm

- Một model “Smart A” gộp VAS + PUSH + biểu mô  
- Marker / CFU / PUSH component = thay primary  
- Đóng Goal vì đủ EQ draft · invent EQ mới (bank CLOSED)  

## Liên kết

`ENDPOINTS-EARLY-SIGNAL-RITUAL-CARD` · **`ENDPOINTS-WEEK1-SCIENCE-CARD`** · **`CROSS-EQ-SCIENCE-CARD`** · **`VAS-EQ-SCIENCE-CARD`** · **`PUSH-EQ-SCIENCE-CARD`** · **`LEAKAGE-EQ-SCIENCE-CARD`** · **`PB001-EQ`** · **`PB002-EQ`** · **`PB003-EQ`** · **`AFTER-STREAK3-OPENER-1PAGE`** · **`BRIDGE-ROTATION`** (T4=#2) · **`MULTI-OMICS-PEA`** (#1) · **`EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01`** (#0) · `#3` DESIGN-YTESO · `SCIENCE-BRIDGES-SCIENCE-CARD` · `SCIENCE-CARDS-INDEX` · `STREAK_TRACKER`
