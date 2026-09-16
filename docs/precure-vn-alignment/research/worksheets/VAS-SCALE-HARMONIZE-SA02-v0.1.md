# VAS scale + early-signal — SA-02 (N=100)

**Mã:** VAS-SCALE-SA02-v0.1  
**Ngày:** 2026-09-16 · **Cập nhật:** drill 8′ · leakage/ALERT/shift hooks  
**Curriculum:** Ngày 12 · Daily stack **T4** · DOI [10.1186/1745-6215-15-263](https://doi.org/10.1186/1745-6215-15-263)  
**Primary đề cương:** ΔVAS D3 (không đổi) · SAP ES exploratory · Goal ACTIVE · L3 **CLOSED**

## Một câu

> Giữ VAS **0–10** trên eCRF; early-signal nhìn **D1/CFU trước D3** — **không** dùng VAS_D3 làm “early predictor”, **không** gộp Y với SA-01/05.

## So sánh thang

| | Smart A SA-02 (đề cương) | STPIS / sore throat trials |
|--|--------------------------|----------------------------|
| Scale | VAS **0–10** (đau rát họng) | VAS **0–100 mm** (STPIS) |
| Primary | **ΔVAS D3 − D0** | SPID / Δ theo giờ–ngày |
| Early window | D0, D1? `[CẦN XÁC NHẬN]`, D3 | 1h, 2h, 24h… |

## Harmonize (exploratory / meta)

1. **Không đổi** eCRF SA-02 sang 0–100 — giữ 0–10 cho site VN và primary đã duyệt.  
2. Khi so sánh literature: \(VAS_{100} = 10 \times VAS_{10}\) chỉ cho mô tả; không meta-merge without protocol `[CẦN XÁC NHẬN]`.  
3. SAP ES: MCID trên thang **0–10** riêng — không copy ngưỡng mm từ STPIS.  
4. Optional **D1**: học “đo sớm” từ STPIS — trade-off tải BN (EH-SA02 §3).

## Leakage / M0–M3 (neo EQ)

| Model | Cấm / ưu tiên |
|-------|----------------|
| **M1 sandbox** | Có `VAS_D3` gần \(Y_{\text{relief}}\) → AUROC cao = **QC**, ≠ evidence |
| **M1\*** khoa học | VAS_D1 nếu thu · hoặc CFU_D0 — trước / không trùng \(Y\) |
| **M2–M3** | CFU ± ADHERE trong \(t'\le D3\) |
| **L3 / mucosa** | **CLOSED** — SA-02 support, không order marker vì đã đọc VAS |

## Liên hệ phương trình / ALERT / cổng

| Khối | File |
|------|------|
| EQ M0–M3 | `EQ-SA02-early-warning` · Drill 10′ |
| ALERT C1–C3 | `ALERT-SA02` · `ALERT-CROSS-SA-ATLAS` |
| Leakage | `LEAKAGE-CROSS-SA-ATLAS` hàng SA-02 |
| L3 | `L1L2L3-DAILY-GATE-CARD` — CLOSED |
| Shift 1 câu | `PRECURE-SHIFT-CROSS-SA-BANK` hàng SA-02 |

## Drill 8′ (điền — T4 / Ngày 12)

```text
t* = D3 · t' ưu tiên: D1 | CFU_D0 | khác: ________
eCRF giữ thang: 0–10 | 0–100 (khoanh 1 đúng)
VAS_100 = 10×VAS_10 dùng khi: literature | đổi eCRF (khoanh đúng)
M1 sandbox gồm VAS_D3 → leakage? CÓ — vì: ________
M1* thay bằng: ________
ALERT C__ nếu VAS↑ sớm: ________
1 câu KHÔNG gộp Y với SA-01/05:
1 câu Precure shift (≤25 từ):
```

## Việc nhỏ

- [ ] Không đổi REDCap sang 0–100 trừ amendment `[CẦN XÁC NHẬN]`  
- [ ] Không dùng AUROC M1 sandbox làm claim early lâm sàng  
- [ ] T4: EQ-SA02 Drill 10′ + card này (hoặc thay một phần)

## Cấm

- Harmonize eCRF vì STPIS dùng mm  
- VAS_D3 = predictor “early” rồi claim ES  
- Marker niêm mạc / L3 vì đã ôn VAS  
- Gộp endpoint với SA-01/05  

## Liên kết

- Notes: `reading-notes/2026-09-28-vas-stpis-sore-throat.md`  
- SAP: `hypotheses/SAP-SA02-ES-v0.1-DRAFT.md` · EH: `EH-SA02-early-signal-v0.1.md`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T4) · Endpoints: `ENDPOINTS-CROSS-SA-BRIDGE`  
- EQ: `EQ-SA02-early-warning-v0.1.md`
