# SAP-ES — thẻ khoa học 1 trang (§7 blind/leakage · 7.1 · ≠ primary)

**Mã:** SAP-ES-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `SAP-SA01-ES-v0.1-DRAFT` · AMENDMENT-ES · LEAKAGE · HAWTHORNE · TRIPOD · SYNTH  
**Dùng khi:** T5 · sau AMENDMENT-ES / SPIRIT · trước claim AUROC / interim / “SAP CLOSED”  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + **`MEDIA-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · SAP ES = exploratory · primary D21/ΔVAS/ΔPUSH không đổi · L3/G2 CLOSED · PREP ≠ DONE  
**DOI khung:** SPIRIT 2013 [10.7326/0003-4819-158-3-201302050-00583](https://doi.org/10.7326/0003-4819-158-3-201302050-00583) · Nat Med PB-008 [10.1038/s41591-019-0414-6](https://doi.org/10.1038/s41591-019-0414-6)

## Mục đích

Ôn **SAP exploratory early-signal** Precure/Smart A: predictors chỉ trước/cùng D7; ImageJ mù PROBE; §7.1 Hawthorne/compliance **không** giải thích primary; AUROC synthetic ≠ bằng chứng BN; không adaptive RCT vì ES; không \(X_{\text{mol}}\) trước G1–G2.

**Mở song song:** thẻ này · `SAP-SA01-ES` · `AMENDMENT-ES-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `HAWTHORNE-SCIENCE-CARD` · `TRIPOD-SCIENCE-CARD`

## §7 / 7.1 → giữ / bỏ

| Hạng mục | Vai trò | Giữ hôm nay | Bỏ |
|----------|---------|-------------|-----|
| **Primary** | D21 / ΔVAS / ΔPUSH | Khoá \(t^*\) trong SAP ES | Đổi primary vì AUROC ES |
| **Predictors** | D0–D7 pre-spec | Chỉ trước/cùng D7 | Biến sau D7 vào “early” |
| **Blind** | ImageJ mù PROBE | Ghi [CẦN XÁC NHẬN] nếu chưa | Claim đã mù vì đã drill |
| **§7.1** | Compliance / CLIN_EVENT subset | Sensitivity exploratory | Diễn giải = hiệu quả sản phẩm |
| **Sandbox** | verify.sh / synthetic AUROC | Methods/tech appendix | Bằng chứng BN / Results lâm sàng |
| **\(X_{\text{mol}}\)** | Omics | Ngoài v0.1 · sau G1–G2 | Nhét vào SAP ES trước cổng |

## Phương trình SAP-ES

```text
Primary(t*) cố định  +  predictors ≤D7  +  §7 no leakage
  ≥  trước  claim AUROC / interim
§7.1 sensitivity  ≠  primary  ≠  “tín hiệu Precure”
Synthetic AUROC  ≠  bằng chứng BN
Adaptive / đổi nhánh vì ES  =  KHÔNG
```

## Checklist 15′

```text
Thứ: T5 · SA: 01|02|05 — primary: D21|ΔVAS|ΔPUSH — ________
Primary đổi trong SAP ES? KHÔNG — nếu lệch: ________
Predictors sau D7 vào model early? KHÔNG — ________
ImageJ mù PROBE? CÓ|CHƯA[CẦN XÁC NHẬN]|N/A — ________
§7.1 = primary / hiệu quả sản phẩm? KHÔNG — vì: ________
Adaptive / dừng sớm vì ES? KHÔNG
AUROC synthetic = BN? KHÔNG
X_mol trong v0.1? KHÔNG (trước G1–G2)
1 việc ≤30′ (SAP §7 skim / visit map DM / AMENDMENT S2): ________
Đóng Goal / coi SAP CLOSED vì drill? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / SAP-ES draft | §7 leakage · 7.1 · ≠ primary |
| `AMENDMENT-ES-SCIENCE-CARD` | Outline ES · không đổi primary |
| `LEAKAGE-SCIENCE-CARD` | Pitfall thời gian · predictors |
| `HAWTHORNE-SCIENCE-CARD` | PB-008 bias tham gia |
| `TRIPOD-SCIENCE-CARD` | Y/predictors/validation trước claim AI |
| `SYNTH-SCIENCE-CARD` | Sandbox ≠ BN |
| `CONSORT-SCIENCE-CARD` | Placement ES trên báo cáo |

## Cấm

- Đưa biến sau D7 vào model “early”  
- Diễn giải ΔAUROC 7.1 = hiệu quả sản phẩm / primary  
- Adaptive RCT hoặc đổi primary vì ES  
- Claim sandbox = bằng chứng lâm sàng · order omics · đóng Goal  

## Liên kết

`SAP-SA01-ES` · `SAP-ES-5MIN` · `SAP-EQ-5MIN` · `AMENDMENT-ES-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `HAWTHORNE-SCIENCE-CARD` · `TRIPOD-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · `CONSORT-SCIENCE-CARD` · `TT43-SCIENCE-CARD` · `SCIENCE-CARDS-INDEX` · **`PB008-SCIENCE-CARD`** · `DAILY-STACK-AFTER-STREAK3` · **`ISO-SWAB-SCIENCE-CARD`** · **`PITFALLS-SCIENCE-CARD`**
