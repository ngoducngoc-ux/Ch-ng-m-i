# EQ02-M0M3 — thẻ khoa học 1 trang (SA-02 ladder · M1+VAS_D3 = leakage)

**Mã:** EQ02-M0M3-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `EQ02-M0M3-5MIN-MICRO-DRILL` · EQ-SCIENCE-CARD · EQ-SIBLING-MAP · PB002 · VAS-LEAK · LEAKAGE  
**Dùng khi:** STREAK≥3 · Daily stack **T4** · trước AUROC M1/M3 SA-02 · sibling SA-02  
**Ưu tiên STREAK&lt;3:** **`STREAK3-EQ-5MIN-SCIENCE-CARD`** · NOW · FILL-AID → tick **19/09** · **không** mở ladder  
**Goal:** ACTIVE · \(Y_{\text{prim}}\) VAS D3 / ΔVAS không đổi · M1* = D1/CFU · M1+VAS_D3 = QC leakage · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **ladder SA-02**: M0(VAS_D0+C) → M1* (VAS_D1 hoặc CFU_D0) → M2/M3 (CFU+ADHERE) — **M1 sandbox + VAS_D3 = leakage QC**, không phải evidence early. Khác `EQ-M0M3-SCIENCE-CARD` (SA-01) — thẻ này chỉ **SA-02 · leakage VAS**.

**Mở song song:** thẻ này · `EQ02-M0M3-5MIN` · `EQ-SCIENCE-CARD` · `EQ-SIBLING-MAP-SCIENCE-CARD` · `PB002-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `VAS-LEAK-5MIN`

## M0–M3 → giữ / bỏ

| Bậc | Predictors (ý) | Giữ | Bỏ |
|-----|----------------|-----|-----|
| **M0** | VAS_D0 + AGE + DX_CAT + GROUP | Baseline early | Claim baseline = Dx |
| **M1\*** | + VAS_D1 `[CẦN XÁC NHẬN]` hoặc CFU_D0 | True early trước \(Y\) | VAS_D3 trong feature “early” |
| **M1 sandbox** | + VAS_D3 | **QC leakage only** | AUROC M1 = evidence BN |
| **M2** | + CFU_D0 / CFU_D3 | Vi sinh vs triệu chứng | Gộp \(Y\) với SA-01/05 |
| **M3** | + CFU_D1 + ADHERE | Full early window | Marker niêm mạc / L3 |
| **M4 / \(X\)** | Mucosa | **CLOSED** đến G1–G2 | Order omics vì đã viết ladder |

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Y_prim: VAS D3 / ΔVAS — không đổi? CÓ
eCRF thang 0–10? CÓ | lệch: ________
M0|M1*|M2|M3 (1 dòng mỗi): ________
M1 sandbox + VAS_D3 = leakage? CÓ — vì: ________
AUROC M1 sandbox = claim BN? KHÔNG
Gộp Y với SA-01/05? KHÔNG
Marker / L3: CLOSED vì ________
Sibling SA-01/05 hôm nay? EQ-M0M3|EQ05|không — ________
1 việc ≤30′ (EQ-SA02 / VAS-LEAK / EH-SA02): ________
Đóng Goal / mở L3? KHÔNG
```

## Checklist 15′

```text
Đã mở EQ-SIBLING-MAP chọn sibling SA-02? ________
Leakage t* (VAS_D3) trong feature early? KHÔNG (trừ sandbox QC)
Z rồi X (PB-007)? CÓ · X CLOSED hôm nay
Thang 0–100 / đổi primary? KHÔNG trừ amendment
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | SA-02 M0–M3 + leakage 1 trang |
| `EQ02-M0M3-5MIN` | Drill điền |
| `EQ-M0M3-SCIENCE-CARD` | Sibling SA-01 |
| `EQ05-M0M3-5MIN` | Sibling SA-05 |
| `EQ-SCIENCE-CARD` | 3 SA ladder |
| `EQ-SIBLING-MAP-SCIENCE-CARD` | Chọn sibling |
| `PB002-SCIENCE-CARD` | Primary SA-02 |
| `LEAKAGE` / `VAS-LEAK` | Pitfall thời gian |
| `STREAK3-EQ-5MIN-SCIENCE-CARD` | Cổng trước ≥3 |

## Cấm

- Báo M1+VAS_D3 AUROC như early-signal lâm sàng  
- Đổi primary / thang 0–100 trừ amendment  
- Marker niêm mạc / L3 / G2 vì đã viết ladder  
- Nhảy ladder khi STREAK&lt;3 · UpdateGoal trên PREP  

## Liên kết

`EQ02-M0M3-5MIN-MICRO-DRILL` · `EQ-SCIENCE-CARD` · `EQ-SIBLING-MAP-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ05-M0M3-5MIN` · `PB002-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `VAS-LEAK-5MIN` · `VAS-5MIN` · `STREAK3-EQ-5MIN-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
