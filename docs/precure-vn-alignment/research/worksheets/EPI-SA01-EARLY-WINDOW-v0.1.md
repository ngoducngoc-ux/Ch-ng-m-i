# Early window — SA-01 PCT/CFU/VAS (N=120 · cờ đầu)

**Mã:** EPI-SA01-EARLY-WINDOW-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 10 · Daily stack **T2** · Zhou/NatMed #0 · ImageJ primary  
**Primary đề cương:** biểu mô hóa **100% tại D21** (ImageJ) · không đổi · SAP ES exploratory · Goal ACTIVE · L3/PEA **CLOSED**

## Một câu

> Early-signal SA-01 nhìn **PCT_EPITH / CFU / VAS_DRESS / `clin_event` trong D0–D7** — **không** dùng PCT D21 làm “early”, **không** order PEA vì đã ôn ImageJ.

## Primary vs early window

| Khối | Định nghĩa | Ghi chú |
|------|------------|---------|
| \(t^*\) | D21 · \(Y=\mathbb{1}\{\text{biểu mô 100\% ImageJ}\}\) | Primary PROBE — không đổi |
| \(t'\) | D0, D3, D7 | Cửa sổ exploratory trước \(t^*\) |
| \(Z\) | PCT_EPITH · CULTURE_CFU · VAS_DRESS | eCRF v0.2 · chuỗi dọc |
| Sự kiện | `clin_event` 0–4 | Zhou — không leakage từ \(Y\) |
| \(X_{\text{PEA}}\) | Panel hẹp | Chỉ sau G1–G2 · mặc định CLOSED |

## Leakage / ImageJ (neo ôn)

| Pitfall | Đúng |
|---------|------|
| PCT_EPITH **D21** làm predictor “early” | Chỉ dùng D0/D3/D7 (+ deltas) trong M0–M3 |
| AUROC sandbox = bằng chứng BN | Sandbox = QC cấu trúc · synthetic ≠ lâm sàng |
| Ảnh không chuẩn → % biểu mô lệch | SOP ảnh + QA ImageJ trước claim AI trên PCT |
| Mở PEA vì đã đọc EQ | L3 CLOSED · `L1L2L3-DAILY-GATE` · bridge PEA |

## Liên hệ phương trình / ALERT / cổng

| Khối | File |
|------|------|
| EQ M0–M3 | `EQ-SA01-early-warning` · Drill 10′ |
| ALERT A1–A4 | `ALERT-SA01` · `ALERT-CROSS-SA-ATLAS` · Nat Med map |
| clin_event | `CLIN_EVENT-CROSS-SA-ATLAS` · Zhou map |
| Leakage | `LEAKAGE-CROSS-SA-ATLAS` hàng SA-01 |
| L3 / PEA | `MULTI-OMICS-PEA-SA01-BRIDGE` · gate card — CLOSED |
| Shift 1 câu | `PRECURE-SHIFT-CROSS-SA-BANK` hàng SA-01 |

## Drill 8′ (điền — T2 / Ngày 10)

```text
t* = D21 · t' ∈ {D0, D3, D7} — khoanh 1 mốc ôn hôm nay: ________
Z early 1 biến: PCT_EPITH | CFU | VAS_DRESS | clin_event
PCT_EPITH_D21 làm predictor early? KHÔNG — vì: ________
ImageJ QA hôm nay cần gì (1 câu): ________
ALERT A__ nếu PCT↓ / CFU↑ sớm: ________
X_PEA / L3: CLOSED vì ________
1 câu Precure shift (≤25 từ):
```

## Việc nhỏ

- [ ] Không claim ImageJ % mà thiếu SOP ảnh / blinded QA  
- [ ] Không dùng synthetic M0–M3 AUROC làm evidence BN  
- [ ] T2: EQ-SA01 Drill 10′ + card này (hoặc thay một phần) · Zhou/NatMed nếu STREAK&lt;3 path

## Cấm

- PCT D21 = “early predictor”  
- Order biospecimen / PEA vì đã điền drill  
- Gộp Y với SA-02/05  
- Đóng Goal / coi PREP = STREAK DONE  

## Liên kết

- EH: `hypotheses/EH-SA01-early-signal-v0.1.md` · Z/X: `EH-SA01-ZX-variables.md`  
- SAP: `hypotheses/SAP-SA01-ES-v0.1-DRAFT.md`  
- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T2) · Bridge #0/#1  
- EQ: `EQ-SA01-early-warning-v0.1.md` · Endpoints: `ENDPOINTS-CROSS-SA-BRIDGE`  
- **EPI 5′:** `EPI-5MIN-MICRO-DRILL-v0.1.md`  
- **ImageJ QA 5′:** `IMAGEJ-QA-5MIN-MICRO-DRILL-v0.1.md`
