# TRIPOD-EQ — thẻ khoa học 1 trang (AI claim × ladder · demo ≠ BN)

**Mã:** TRIPOD-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `TRIPOD-EQ-5MIN-MICRO-DRILL` · TRIPOD-SCIENCE-CARD · TRIPOD-SYNTH-EQ · EQ-M0M3 · SYNTH-EQ · LEAKAGE-EQ · PB008-EQ  
**DOI:** Riley et al. [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594)  
**Dùng khi:** STREAK≥3 · Daily stack **T4 / T5** · trước claim AUROC / “early-warning” · cặp TRIPOD×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NOW · FILL-AID · NatMed · ALERT · HAWTHORNE · MEDIA → tick **19/09** trước  
**Goal:** ACTIVE · TRIPOD rút gọn trên \(Z\) · M4/\(X\) **CLOSED** · synthetic ≠ BN · PREP ≠ DONE  

## Mục đích

Ôn **cặp TRIPOD×EQ**: neo 1 SA + ladder M0–M3 trên \(Z\) — ghi **1 hàng TRIPOD** (source / outcome / predictors / validation) — **demo AUROC ≠ BN** · không đổi primary · không mở L3. Khác `TRIPOD-SCIENCE-CARD` (alone) / `TRIPOD-SYNTH-EQ` (TRIPOD×SYNTH×ladder) — thẻ này neo **reporting × ladder** chung.

**Mở song song:** thẻ này · `TRIPOD-EQ-5MIN` · `TRIPOD-SCIENCE-CARD` · `TRIPOD-SYNTH-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `SYNTH-EQ-SCIENCE-CARD` · `LEAKAGE-EQ-SCIENCE-CARD` · `PB008-EQ-SCIENCE-CARD`

## Giữ / bỏ (TRIPOD × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) sandbox / pre-spec | M4 / \(X\) · ladder = Dx |
| **Y(\(t^*\))** | Khoá primary trước claim | Đổi Y sau peek AUROC |
| **Predictors** | Pre-spec SAP ES · không \(Y(t^*)\) | Thêm feature sau data peek |
| **Validation** | Internal demo / không claim BN | AUROC sandbox = evidence BN |
| **Leak** | \(Y(t^*)\) ≠ early feature | Outcome làm predictor “early” |
| **Omics / L3** | **CLOSED** | Order PEA vì TRIPOD×EQ đủ |
| **Order / Goal** | KHÔNG từ densify | Đóng Goal / UpdateGoal trên PREP |

## Phương trình ranh giới

```text
1 SA  +  Y(t*) khoá  +  EQ ladder M0–M3 trên Z  +  1 hàng TRIPOD
≠  AUROC demo = BN  ≠  đổi primary  ≠  mở L3/G2
Ôn TRIPOD×EQ  ≠  UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T4|T5 · SA neo: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
Y(t*) primary (không đổi): ________
Predictors Z early (1 dòng · không Y(t*)): ________
Nguồn: synthetic | eCRF mock | BN thật — ________
Validation claim: internal demo | external BN | không claim — ________
AUROC sandbox = evidence lâm sàng? KHÔNG
Leakage Y(t*) làm early? KHÔNG
X / PEA / L3 hôm nay: CLOSED vì ________
Cặp **`STREAK3-EQ-SCIENCE-CARD`** / TRIPOD-SYNTH-EQ / SYNTH-EQ / LEAKAGE-EQ hôm nay? ________
1 việc ≤30′ (TRIPOD sheet / EQ Drill 10′ / SYNTH verify): ________
Đóng Goal / mở G2 vì TRIPOD×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở TRIPOD + EQ sibling thẻ riêng trước cặp? ________
TRIPOD+ladder = lý do claim BN / mở PEA? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | TRIPOD×EQ bridge 1 trang |
| `TRIPOD-EQ-5MIN` | Drill điền |
| `TRIPOD-SCIENCE-CARD` / checklist | Reporting alone |
| `TRIPOD-SYNTH-EQ` / `SYNTH-EQ` | TRIPOD×SYNTH×ladder / demo×ladder |
| `EQ-M0M3` / `LEAKAGE-EQ` | Ladder sibling / timestamp |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Báo AUROC demo như hiệu năng BN · dùng \(Y(t^*)\) làm early feature  
- Mở \(X\)/G2 / UpdateGoal trên PREP  

## Liên kết

`TRIPOD-EQ-5MIN-MICRO-DRILL` · `TRIPOD-SCIENCE-CARD` · `TRIPOD-INTERNAL-CHECKLIST` · `TRIPOD-SYNTH-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `SYNTH-EQ-SCIENCE-CARD` · `LEAKAGE-EQ-SCIENCE-CARD` · `PB008-EQ-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
