# Bridge — Endpoints × early-signal (SA-01 / 02 / 05)

**Mã:** ENDPOINTS-CROSS-SA-BRIDGE-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 08–14 · ôn Tier 3 CROSS-SA 33–36  
**Thẻ:** `ENDPOINTS-EARLY-SIGNAL-RITUAL-CARD` · map `CROSS-SA-EARLY-SIGNAL-MAP`  
**Cờ đầu:** SA-01 · SA-02/05 = support · SA-03/04 = cổng (không RCT người)

## Một câu

> Cùng khung **\(t' \ll t^*\)** + M0–M3 trên \(Z\) dọc — nhưng **mỗi SA một \(Y(t^*)\)**; không train chung, không gộp endpoint, không lấy AUROC sandbox làm evidence BN.

## Ma trận \(t^*\) / \(Y\) / \(Z\) sớm / M0–M3

| SA | \(t^*\) | \(Y\) (primary / ES binary) | \(Z\) sớm | M0 → M3 (ý) | \(X\) / omics |
|----|---------|------------------------------|-----------|-------------|---------------|
| **01** | D21 | \(Y_{D21}\)= biểu mô 100% | PCT/CFU/VAS/`clin_event` D0–D7 | Baseline → D3 → delta → D7+event | PEA sau G2 (`MULTI-OMICS-PEA-SA01-BRIDGE`) |
| **02** | D3 | \(Y\)= relief \(\Delta\)VAS≤−2 (ES) · primary VAS D3 | VAS/CFU D0–D3 · **D1 `[CẦN XÁC NHẬN]`** | D0 → (+D3 sandbox*) → CFU → CFU+ADHERE | Marker niêm mạc gated · ≠ primary |
| **05** | D14 | \(Y\)= \(\Delta\)PUSH≤−2 | PUSH D0–D7 + TURN_ADHERE + CFU | D0 → D3/D7 → +CFU → +turn | G2 ICU · không app Dx |
| **03** | ATCC | — | — | — | In-vitro ≠ Dx BN |
| **04** | ISO | — | — | — | Trước mọi L3 người |

\*Sandbox SA-02 M1 gồm `VAS_D3` → **leakage có chủ đích để QC pipeline** (outcome gần \(Y\)); ritual khoa học ưu tiên D1/CFU trước D3 — xem `EQ-SA02`.

## Phương trình chung (không train chung)

```text
Mỗi SA riêng:
  P(Y_SA=1) = σ( β0 + β_Z·Z_SA(t') + β_g·GROUP + β_C·C_SA )
  t' ≪ t*_SA
  X chỉ sau G2 trên SA đó (mặc định CLOSED)
```

Chi tiết: `EQ-SA01` · `EQ-SA02` · `EQ-SA05`.

## Zhou / Nat Med / PEA — chỗ gắn

| Logic Precure | Artifact | Áp vào endpoints tuần B |
|---------------|----------|-------------------------|
| Sự kiện dọc trước endpoint | `EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01` · `CLIN_EVENT-ZHOU-MAP` | SA-01 `clin_event`; SA-02 timestamp triệu chứng; SA-05 AE/ICU event |
| Actionable ≠ đổi primary | `NATMED-ACTIONABLE-ALERT-MAP` | ALERT A/B nội bộ trên \(Z\) |
| Multi-omics sau L1–L2 | `MULTI-OMICS-PEA-SA01-BRIDGE` · PB-009 | Không order vì đã có 3 JSON synthetic |

## Sandbox (chỉ QC)

| File | Dùng đúng | Cấm |
|------|-----------|-----|
| `synthetic_sa0{1,2,5}_m0_m3_metrics.json` | So cấu trúc feature sets | Chọn cờ đầu / claim lâm sàng theo AUROC |
| `verify.sh` | PASS/FAIL pipeline | “Đã chứng minh early-signal” |

## Ritual fill-in (Ngày 08–14)

```text
Ngày: 08|09|10|11|12|13|14
SA đang ôn: 05|05|01|weekly|02|03|04
1 câu t* ≠ Z sớm:
1 câu vì sao không gộp endpoint với SA khác:
```

## Cấm

- Một model “Smart A” gộp VAS + PUSH + biểu mô  
- Marker / CFU / PUSH component = thay primary  
- Đóng Goal vì đủ EQ draft  

## Liên kết

- Thẻ ngày: `ENDPOINTS-EARLY-SIGNAL-RITUAL-CARD-v0.1.md`  
- Study sheet: `STUDY-SHEET-SMART-A-ENDPOINTS-v0.1.md`  
- Tier 3 schema: `CROSS-SA-EARLY-SIGNAL-MAP-v0.1.md`  
- Glossary: `EARLY-SIGNAL-GLOSSARY-v0.1.md`
