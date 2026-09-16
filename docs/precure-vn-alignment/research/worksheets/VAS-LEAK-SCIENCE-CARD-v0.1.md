# VAS-LEAK — thẻ khoa học 1 trang (SA-02 · 0–10 · VAS_D3 ≠ early)

**Mã:** VAS-LEAK-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `VAS-LEAK-5MIN-MICRO-DRILL` · LEAKAGE-SCIENCE-CARD · EQ02-M0M3 · PB002 · VAS-SCALE-HARMONIZE  
**DOI:** STPIS [10.1186/1745-6215-15-263](https://doi.org/10.1186/1745-6215-15-263) (literature only) · TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594)  
**Dùng khi:** STREAK≥3 · Daily stack **T4** · trước claim ES SA-02 · cặp VAS×leakage  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · primary ΔVAS D3 không đổi · eCRF **0–10** · M1+VAS_D3 = leakage QC · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp VAS×LEAK SA-02**: thang **0–10** + early chỉ D1/CFU trước D3 — **VAS_D3 trong M early = QC leakage**, không phải evidence; không gộp \(Y\) với SA-01/05 · không đổi 0–100 vì STPIS mm. Khác `LEAKAGE-SCIENCE-CARD` (3 SA) / `EQ02-M0M3-SCIENCE-CARD` (ladder) — thẻ này giữ **cặp VAS↔leakage**.

**Mở song song:** thẻ này · `VAS-LEAK-5MIN` · `LEAKAGE-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `PB002-SCIENCE-CARD` · `VAS-SCALE-HARMONIZE-SA02` · `TRIPOD-SCIENCE-CARD`

## Giữ / bỏ (VAS × Leakage)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **Thang eCRF** | 0–10 | Đổi 0–100 trừ amendment |
| **Primary \(t^*\)** | ΔVAS / VAS D3 | Co-primary khác thang |
| **Early \(t'\)** | VAS_D1 `[CẦN XÁC NHẬN]` · CFU_D0 | VAS_D3 làm early feature |
| **M1 sandbox** | VAS_D3 = **QC leakage only** | AUROC M1 = evidence BN |
| **Cross-SA** | Schema riêng | Gộp \(Y\) với SA-01/05 |
| **L3 / omics** | **CLOSED** | Order vì đã ôn VAS-LEAK |

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
eCRF thang: 0–10? CÓ | lệch: ________
t* primary: ΔVAS D3 — không đổi? CÓ
t' early: D1|CFU_D0 — ________ (không VAS_D3)
M1 + VAS_D3 = leakage? CÓ — vì: ________
1 feature HỢP LỆ cho t' hôm nay: ________
Gộp Y SA-01/05? KHÔNG
Sandbox AUROC “đẹp” = claim BN? KHÔNG
Cặp EQ02 / LEAKAGE / PB002 hôm nay? ________
1 việc ≤30′ (harmonize / EQ-SA02 / atlas): ________
Đóng Goal / mở L3? KHÔNG
```

## Checklist 15′

```text
Đã mở LEAKAGE + EQ02 thẻ trước cặp? ________
VAS_D3 trong feature early (trừ sandbox QC)? KHÔNG
Thang literature mm → đổi eCRF? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | VAS×LEAK SA-02 1 trang |
| `VAS-LEAK-5MIN` | Drill điền |
| `LEAKAGE-SCIENCE-CARD` | Pitfall #1 · 3 SA |
| `EQ02-M0M3-SCIENCE-CARD` | Ladder SA-02 |
| `PB002-SCIENCE-CARD` | Primary SA-02 |
| `VAS-SCALE-HARMONIZE-SA02` | 0–10 vs mm |
| `TRIPOD` / `SYNTH` | Không claim từ sandbox |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- VAS_D3 = early predictor / claim ES lâm sàng  
- Đổi eCRF 0–100 trừ amendment `[CẦN XÁC NHẬN]`  
- Báo M1 sandbox AUROC như bằng chứng BN  
- Nhảy claim khi STREAK&lt;3 · UpdateGoal trên PREP  

## Liên kết

`VAS-LEAK-5MIN-MICRO-DRILL` · `VAS-LEAK-EQ-5MIN` · `LEAKAGE-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `PB002-SCIENCE-CARD` · `VAS-SCALE-HARMONIZE-SA02` · `VAS-5MIN` · `LEAKAGE-5MIN` · `TRIPOD-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · **`LEAK-CROSS-SCIENCE-CARD`** · **`VAS-LEAK-EQ-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`
