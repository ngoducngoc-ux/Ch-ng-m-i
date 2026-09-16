# VAS-LEAK-EQ — thẻ khoa học 1 trang (0–10 × leakage × ladder · ≠ VAS_D3 early)

**Mã:** VAS-LEAK-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `VAS-LEAK-EQ-5MIN-MICRO-DRILL` · VAS-LEAK-SCIENCE-CARD · VAS-EQ · LEAKAGE-EQ · EQ02-M0M3 · IMAGEJ-EPI-EQ · PB002  
**DOI:** TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594) · STPIS literature [10.1186/1745-6215-15-263](https://doi.org/10.1186/1745-6215-15-263)  
**Dùng khi:** STREAK≥3 · Daily stack **T4** · trước claim ES SA-02 · cặp VAS-LEAK×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · HAWTHORNE · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · primary ΔVAS D3 không đổi · eCRF **0–10** · ladder chỉ feature hợp lệ · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp VAS-LEAK×EQ**: thang 0–10 + 1 feature leakage + 1 feature hợp lệ **và** 1 dòng ladder M0–M3 chỉ trên feature hợp lệ — VAS_D3 trong M early = QC leakage ≠ evidence. Khác `VAS-LEAK-SCIENCE-CARD` (cặp alone) / `VAS-EQ` / `LEAKAGE-EQ` — thẻ này neo **scale×leak × ladder**.

**Mở song song:** thẻ này · `VAS-LEAK-EQ-5MIN` · `VAS-LEAK-SCIENCE-CARD` · `VAS-EQ-5MIN` · `LEAKAGE-EQ-5MIN` · `EQ02-M0M3-SCIENCE-CARD` · `IMAGEJ-EPI-EQ-SCIENCE-CARD` · `PB002-SCIENCE-CARD`

## Giữ / bỏ (VAS-LEAK × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 chỉ feature hợp lệ (`EQ02`) | Ladder = VAS_D3 early / AUROC sandbox = BN |
| **Thang eCRF** | 0–10 | Đổi 0–100 trừ amendment |
| **Primary \(t^*\)** | ΔVAS D3 | Co-primary / gộp Y SA-01/05 |
| **Early / leak** | VAS_D1 · CFU_D0 · VAS_D3 = QC leakage only | VAS_D3 = early predictor |
| **Omics / L3** | **CLOSED** | Order vì đã ôn VAS-LEAK×EQ |
| **Order / Goal** | KHÔNG từ densify | Claim ES / đóng Goal vì PREP |

## Phương trình ranh giới

```text
thang 0–10  +  1 feature hợp lệ  +  EQ ladder M0–M3 (≠ VAS_D3 early)
≠  VAS_D3 = evidence  ≠  gộp Y  ≠  sandbox AUROC = BN
Ôn VAS-LEAK×EQ  ≠  claim ES / UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T4 · eCRF thang: 0–10|0–100 — ________ (đúng = 0–10)
EQ sibling: EQ02-M0M3|EQ-M0M3 — ________ (thường EQ02)
t* = ΔVAS D3 — xác nhận? CÓ
1 feature LEAKAGE nếu vào M early: ________ (thường VAS_D3)
1 feature HỢP LỆ cho t': ________
1 dòng Z / M0→M3 (chỉ feature hợp lệ): ________
Gộp Y SA-01/05 / AUROC SYN = BN? KHÔNG
Cặp **`IMAGEJ-EPI-EQ-SCIENCE-CARD`** / LEAK-CROSS-EQ / PB002-EQ / DEID-MISS-EQ hôm nay? ________
1 việc ≤30′ (harmonize / EQ Drill 10′ / atlas 1 hàng): ________
Đóng Goal / mở L3 vì VAS-LEAK×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở VAS-LEAK + EQ sibling thẻ riêng trước cặp? ________
Scale+leak+ladder = lý do VAS_D3 early / claim BN? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | VAS-LEAK×EQ bridge 1 trang |
| `VAS-LEAK-EQ-5MIN` | Drill điền |
| `VAS-LEAK-SCIENCE-CARD` | Cặp alone |
| `VAS-EQ` / `LEAKAGE-EQ` / `EQ02-M0M3` | VAS / leak / ladder SA-02 |
| `LEAK-CROSS-EQ` / `IMAGEJ-EPI-EQ` | Leak×schema / ImageJ×EPI × EQ |
| `VAS-SCALE-HARMONIZE-SA02` | 0–10 vs mm |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- VAS_D3 làm early feature · gộp Y · đổi 0–100 vì STPIS mm  
- Báo M1 sandbox AUROC như ES lâm sàng · UpdateGoal trên PREP  

## Liên kết

`VAS-LEAK-EQ-5MIN-MICRO-DRILL` · `VAS-LEAK-SCIENCE-CARD` · `VAS-SCALE-HARMONIZE-SA02` · `EQ02-M0M3-SCIENCE-CARD` · `LEAKAGE-EQ-SCIENCE-CARD` · `IMAGEJ-EPI-EQ-SCIENCE-CARD` · `PB002-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
