# Atlas — Leakage × early-signal (SA-01 / 02 / 05)

**Mã:** LEAKAGE-CROSS-SA-ATLAS-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** EQ rotation T2/T4/T6 · drill B · Q3 L2 (#8) · Ngày 20 pitfalls  
**Thẻ khoa học:** **`LEAKAGE-SCIENCE-CARD-v0.1.md`** · định tuyến `SCIENCE-CARDS-INDEX`  
**Goal:** ACTIVE · G2/L3 **CLOSED** · PREP ≠ DONE · synthetic ≠ lâm sàng

## Một câu

> Cùng pitfall **#1 leakage thời gian** — nhưng **mỗi SA một hình thái**; nhận diện đúng trước khi nhìn AUROC sandbox.

## Ma trận leakage (ôn trước EQ)

| SA | \(t^*\) / \(Y\) | Rủi ro leakage điển hình | Dấu hiệu “đỏ” | Cách đúng (early) |
|----|-----------------|--------------------------|---------------|-------------------|
| **01** | D21 · \(Y_{D21}\) biểu mô | Predictor sau cửa sổ early (vd. PCT D21) · `clin_event` mã hoá từ chính \(Y\) | Feature thời điểm ≥ \(t^*\) trong M0–M3 | \(Z\)/`clin_event` chỉ đến \(t'\le D7\); event ≠ label D21 |
| **02** | D3 · \(Y_{\text{relief}}\) ≈ \(\Delta\)VAS | **M1 sandbox** cố ý gồm `VAS_D3` gần định nghĩa \(Y\) | AUROC M1 “đẹp” trên synthetic | Ritual: D1/`CFU` dẫn trước; M1* không dùng chính \(Y\) |
| **05** | D14 · \(Y_{\text{improved}}\) \(\Delta\)PUSH | PUSH_D14 / component sau \(t'\) làm “early” · auto-treat ICU | Model thay quyết định lâm sàng | \(t'\le D7\); component exploratory; ALERT ≠ Dx |

**Pitfall chung:** #2 tune trên cùng hold-out · #5 AUROC synthetic = BN · gộp Y giữa SA.

## Sandbox (chỉ QC)

| Artifact | Được | Cấm |
|----------|------|-----|
| `sa02_…_m0_m3.py` M1 + VAS_D3 | Chứng minh pipeline bắt leakage | Báo cáo như early-signal lâm sàng |
| `verify.sh` PASS | Cấu trúc M0–M3 OK | “Đã chứng minh” SA bất kỳ |
| JSON metrics SA-01/02/05 | So feature set | Chọn cờ đầu theo AUROC |

## Drill 8′ (điền — 1 SA / ngày theo EQ rotation)

```text
Thứ: T2|T4|T6 · SA: 01|02|05
t* / Y: ________
1 feature sẽ là leakage nếu đưa vào M early: ________
Vì sao (thời gian / trùng Y / sau t*): ________
1 feature HỢP LỆ cho t' hôm nay: ________
1 câu cấm claim từ sandbox:
```

## Gắn y tế số / AI (1 dòng)

| Trụ | Câu kiểm |
|-----|----------|
| **Sớm** | Feature có timestamp &lt; \(t^*\) trên eCRF? |
| **Dọc** | Visit–ID–time đủ để chứng minh không nhìn tương lai? |
| **AI** | Export de-ID + deny list trước train? (`REDCAP-DEID` · TRIPOD) |

## Cấm

- Coi atlas PREP = STREAK DONE  
- Dùng leakage sandbox như bằng chứng mở G2 / order omics  
- Một câu “Smart A không leakage” cho cả 3 SA  

## Liên kết

- **Thẻ khoa học:** **`LEAKAGE-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`  
- EQ: `../equations/EQ-SA01|02|05-early-warning-v0.1.md` (Drill 10′)  
- Pitfalls: `../guides/ML-OMICS-PITFALLS-v0.1.md` #1 · #5  
- **Micro-drill 5′:** `LEAKAGE-5MIN-MICRO-DRILL-v0.1.md` (T4)  
- Bridge endpoints: `ENDPOINTS-CROSS-SA-BRIDGE-v0.1.md`  
- Drill: `../study-sheets/STUDY-SHEET-MULTI-OMICS-ES-DRILL-v0.1.md`  
- Q3: `Q3-L2-EXPORT-EARLY-SIGNAL-BRIDGE` (#8) · TRIPOD checklist  
- ALERT (đừng nhầm với leakage): `ALERT-CROSS-SA-ATLAS-v0.1.md`  
- clin_event atlas: `CLIN_EVENT-CROSS-SA-ATLAS-v0.1.md`  
- Y tế số: `../y-te-so-precure-bridge-v0.1.md`  
- Glossary: `EARLY-SIGNAL-GLOSSARY-v0.1.md`
