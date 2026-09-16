# LEAKAGE-EQ — thẻ khoa học 1 trang (timestamp × ladder · ≠ AUROC claim)

**Mã:** LEAKAGE-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `LEAKAGE-EQ-5MIN-MICRO-DRILL` · LEAKAGE-SCIENCE-CARD · VAS-LEAK-EQ · LEAK-CROSS-EQ · CLIN_EVENT-EQ · EQ-M0M3 · PITFALLS-EQ  
**DOI:** TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594) · pitfall ML-OMICS #1  
**Dùng khi:** STREAK≥3 · Daily stack **T4** (T2/T6) · trước claim AUROC “đẹp” · cặp LEAKAGE×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NOW · FILL-AID · NatMed · ALERT · HAWTHORNE · MEDIA → tick **19/09** trước  
**Goal:** ACTIVE · feature \(t' < t^*\) · ladder chỉ feature hợp lệ · sandbox ≠ BN · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp LEAKAGE×EQ**: 1 feature leakage + 1 feature hợp lệ **và** 1 dòng ladder M0–M3 chỉ trên feature hợp lệ — M1+VAS_D3 = QC leakage ≠ evidence. Khác `LEAKAGE-SCIENCE-CARD` (alone) / `VAS-LEAK-EQ` / `LEAK-CROSS-EQ` — thẻ này neo **leakage × ladder** chung.

**Mở song song:** thẻ này · `LEAKAGE-EQ-5MIN` · `LEAKAGE-SCIENCE-CARD` · `VAS-LEAK-EQ-SCIENCE-CARD` · `LEAK-CROSS-EQ-SCIENCE-CARD` · `CLIN_EVENT-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD`

## Giữ / bỏ (LEAKAGE × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 chỉ feature hợp lệ (\(t' < t^*\)) | Ladder = AUROC sandbox = BN |
| **Leakage** | 1 feature sẽ leak nếu vào M early (QC) | Báo “đã chứng minh ES” từ SYN |
| **Hợp lệ** | 1 feature \(t' ≪ t^*\) · không ≈ \(Y\) | Feature ≥ \(t^*\) / trùng \(Y\) |
| **Omics / L3** | **CLOSED** | Mở G2 vì “phát hiện” leakage trên SYN |
| **Order / Goal** | KHÔNG từ densify | Claim ES / đóng Goal vì PREP |

## Phương trình ranh giới

```text
1 feature LEAKAGE (QC)  +  1 feature HỢP LỆ  +  EQ ladder M0–M3 (chỉ hợp lệ)
≠  sandbox AUROC = BN  ≠  verify.sh PASS = ES lâm sàng
Ôn LEAKAGE×EQ  ≠  UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T2|T4|T6 · SA: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
t* / Y: ________
1 feature LEAKAGE nếu vào M early: ________
1 feature HỢP LỆ cho t': ________
1 dòng Z / M0→M3 (chỉ feature hợp lệ): ________
Sandbox AUROC đẹp → claim BN? KHÔNG
Cặp **`CLIN_EVENT-EQ-SCIENCE-CARD`** / VAS-LEAK-EQ / LEAK-CROSS-EQ / IMAGEJ-EQ hôm nay? ________
1 việc ≤30′ (atlas 1 hàng / EQ Drill 10′ / pitfalls): ________
Order omics / đóng Goal vì LEAKAGE×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở LEAKAGE + EQ sibling thẻ riêng trước cặp? ________
Leak+ladder = lý do AUROC claim / mở G2? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | LEAKAGE×EQ bridge 1 trang |
| `LEAKAGE-EQ-5MIN` | Drill điền |
| `LEAKAGE-SCIENCE-CARD` / atlas | Leak alone |
| `VAS-LEAK-EQ` / `LEAK-CROSS-EQ` | Pair bridges đã densify |
| `CLIN_EVENT-EQ` / `EQ-M0M3` | Event / ladder |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Báo M1 sandbox AUROC như ES lâm sàng  
- Mở G2 vì leakage trên SYN · UpdateGoal trên PREP  

## Liên kết

`LEAKAGE-EQ-5MIN-MICRO-DRILL` · `LEAKAGE-SCIENCE-CARD` · `LEAKAGE-CROSS-SA-ATLAS` · `VAS-LEAK-EQ-SCIENCE-CARD` · `LEAK-CROSS-EQ-SCIENCE-CARD` · `CLIN_EVENT-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
