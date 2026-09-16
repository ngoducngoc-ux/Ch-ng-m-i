# PITFALLS — thẻ khoa học 1 trang (5 cổng anti-overclaim)

**Mã:** PITFALLS-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `ML-OMICS-PITFALLS` · LEAKAGE · SYNTH · TRIPOD · SAP-ES · EQ  
**Dùng khi:** T4/T5 · Ngày 20 · STREAK3 · trước claim model sớm / AUROC / “đã chống pitfall”  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + **`MEDIA-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · không thay SAP primary · L3/G2 CLOSED · synthetic ≠ BN · PREP ≠ DONE  
**DOI:** TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594)

## Mục đích

Ôn **5 cổng anti-overclaim** Precure/Smart A: chọn **1** pitfall hôm nay + 1 hàng kiểm trong repo — không báo cáo sandbox như evidence; không đổi primary; không mở M4/\(X_{\text{mol}}\) vì đã ôn.

**Mở song song:** thẻ này · `ML-OMICS-PITFALLS` · `LEAKAGE-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · `TRIPOD-SCIENCE-CARD`

## 5 pitfalls → giữ / bỏ

| # | Pitfall | Giữ hôm nay | Bỏ |
|---|---------|-------------|-----|
| **1** | Leakage thời gian | Predictors ≤ cửa sổ early | Biến sau \(t^*\) vào “early” |
| **2** | Leakage nhóm / tune | Hold-out / nested CV | Tune trên cùng tập đánh giá |
| **3** | Multiplicity | FDR / panel hẹp | Quét hàng trăm protein không FDR |
| **4** | Batch / site | Ghi site effect `[CẦN XÁC NHẬN]` | Claim generalise mọi site |
| **5** | Synthetic → BN | Methods/tech only | AUROC sandbox = bằng chứng lâm sàng |

## Phương trình PITFALLS

```text
1 pitfall (#1–#5)  +  1 hàng kiểm repo  ≥  trước  claim AUROC / model sớm
verify.sh PASS  ≠  BN evidence  (#5)
SAP primary  không đổi  vì  drill
M4 / X_mol  CLOSED  trước  G1–G2
```

## Checklist 15′

```text
Thứ: T4|T5 · Pitfall: #1|#2|#3|#4|#5 — ________
1 câu “đúng kiểm” (file/atlas): ________
1 câu SAI hôm nay: ________
SAP primary đổi? KHÔNG
verify.sh PASS = BN? KHÔNG (#5)
M4/X mở vì pitfalls? KHÔNG
Cặp: LEAKAGE|SYNTH|TRIPOD|SAP-ES|EQ — ________
1 việc ≤30′: ________
Đóng Goal vì PITFALLS? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / ML-OMICS-PITFALLS | Hub 5 cổng · chọn 1 |
| `LEAKAGE-SCIENCE-CARD` | Pitfall #1 thời gian |
| `SYNTH-SCIENCE-CARD` | Pitfall #5 sandbox ≠ BN |
| `TRIPOD-SCIENCE-CARD` | Y/predictors/validation |
| `SAP-ES-SCIENCE-CARD` | §7 / FDR exploratory |
| `EQ-SCIENCE-CARD` | Ladder M0–M3 |

## Cấm

- Báo cáo AUROC sandbox như bằng chứng lâm sàng  
- Tune trên cùng tập đánh giá (#2)  
- Quét hàng trăm protein không FDR (#3) · đóng Goal / mở L3  

## Liên kết

`ML-OMICS-PITFALLS` · `PITFALLS-5MIN` · `PITFALLS-EQ-5MIN` · `LEAKAGE-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · `TRIPOD-SCIENCE-CARD` · `SAP-ES-SCIENCE-CARD` · `EQ-SCIENCE-CARD` · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3`
