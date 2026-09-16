# TRIPOD-SYNTH — thẻ khoa học 1 trang (AI claim · demo ≠ BN)

**Mã:** TRIPOD-SYNTH-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `TRIPOD-SYNTH-5MIN-MICRO-DRILL` · TRIPOD-SCIENCE-CARD · SYNTH-SCIENCE-CARD · LEAKAGE · PITFALLS  
**DOI:** TRIPOD [10.1136/bmj.g7594](https://doi.org/10.1136/bmj.g7594) · pitfall #5 synthetic  
**Dùng khi:** STREAK≥3 · Daily stack **T4 / T5** · sau `verify.sh` / EQ AUROC · trước memo “model sớm” / press · cặp TRIPOD×SYNTH  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · exploratory ≠ Dx · synthetic ≠ BN · L3/G2 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp TRIPOD×SYNTH**: khoanh Y/\(t^*\)/predictors pre-spec **và** gắn nhãn artifact (verify/CSV/AUROC sandbox) — AUROC demo **chỉ** chứng minh pipeline; không = phát hiện sớm lâm sàng / primary / mở G2. Khác `TRIPOD-SCIENCE-CARD` (báo cáo AI) / `SYNTH-SCIENCE-CARD` (demo ≠ BN alone) — thẻ này giữ **cặp bridge**.

**Mở song song:** thẻ này · `TRIPOD-SYNTH-5MIN` · `TRIPOD-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `PITFALLS-SCIENCE-CARD` · `AI-STACK-SCIENCE-CARD`

## Giữ / bỏ (TRIPOD × SYNTH)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **Y(\(t^*\))** | Khoá primary trước claim | Đổi Y sau peek AUROC |
| **Predictors** | M0–M3 pre-spec SAP ES | Thêm feature sau data peek |
| **Artifact** | verify / CSV SYN / AUROC = **pipeline** | “Early-signal đã hoạt động trên BN” |
| **Label** | Exploratory ES + limitation | Clinical Dx / RCT evidence |
| **N** | Ghi CHƯA de-ID site nếu chỉ demo | Coi `--demo` = N lâm sàng |
| **G2 / L3** | **CLOSED** | Order PEA vì demo xanh |

## Phương trình ranh giới

```text
Y(t*) khoá + predictors pre-spec + validation rõ
  +  artifact SYN gắn nhãn pipeline
≠  AUROC_SYN = evidence BN  ≠  Dx  ≠  mở G2/L3
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T4|T5 · SA: 01|02|05 — ________
Y(t*) primary khoá? CÓ|CHƯA — t* = ________
Predictors: M0–M3 pre-spec | peek sau AUROC (CẤM) — ________
Artifact: verify PASS | CSV SYN | AUROC M__ | khác: ________
N thật de-ID đã có? CHƯA|CÓ — ________
Label: exploratory ES | clinical Dx — khoanh: ________
Claim sandbox = BN / RCT? KHÔNG
G2/L3 / order PEA vì demo xanh? KHÔNG
Cặp LEAKAGE / PITFALLS / CONSORT-SPIRIT hôm nay? ________
1 việc ≤30′ (TRIPOD 1 mục / limitation 1 câu / EQ note): ________
Đóng Goal vì TRIPOD×SYNTH? KHÔNG
```

## Checklist 15′

```text
Đã mở TRIPOD + SYNTH thẻ riêng trước cặp? ________
Predictors peek sau AUROC? KHÔNG
AUROC sandbox = ES lâm sàng? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | TRIPOD×SYNTH bridge 1 trang |
| `TRIPOD-SYNTH-5MIN` | Drill điền |
| `TRIPOD-SCIENCE-CARD` | Y/predictors/validation trước claim |
| `SYNTH-SCIENCE-CARD` | Demo ≠ BN |
| `LEAKAGE-SCIENCE-CARD` | Timestamp / \(t^*\) |
| `PITFALLS-SCIENCE-CARD` | #1 + #5 |
| `AI-STACK-SCIENCE-CARD` | L1→L2 trước L3 |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Báo AUROC synthetic như kết quả lâm sàng / Dx  
- Thêm predictor sau peek AUROC  
- Mở G2/L3 / order omics vì demo xanh  
- Nhảy claim khi STREAK&lt;3 · UpdateGoal trên PREP  

## Liên kết

`TRIPOD-SYNTH-5MIN-MICRO-DRILL` · `TRIPOD-SYNTH-EQ-5MIN` · `TRIPOD-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `PITFALLS-SCIENCE-CARD` · `AI-STACK-SCIENCE-CARD` · `MEDIA-SHIFT-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
