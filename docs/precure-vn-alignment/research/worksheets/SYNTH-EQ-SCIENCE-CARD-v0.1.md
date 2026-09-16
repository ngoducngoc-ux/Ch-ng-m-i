# SYNTH-EQ — thẻ khoa học 1 trang (demo ≠ BN × ladder · ≠ AUROC lâm sàng)

**Mã:** SYNTH-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `SYNTH-EQ-5MIN-MICRO-DRILL` · SYNTH-SCIENCE-CARD · TRIPOD-SYNTH · EQ-M0M3 · TRANSLATION-EQ · LEAKAGE · PITFALLS  
**Căn cứ:** pitfall #5 · `verify.sh` · G2 CLOSED · L3 CLOSED  
**Dùng khi:** STREAK≥3 · Daily stack **T4/T5** · trước claim “early-signal hoạt động” · cặp SYNTH×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · sandbox ≠ N thật · M0–M3 trên \(Z\) demo chỉ = pipeline · L3/G2 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp SYNTH×EQ**: 1 artifact demo (`verify` / CSV SYN / AUROC M__) **và** 1 dòng ladder M0–M3 trên \(Z\) sandbox — chứng minh pipeline chạy, **không** tín hiệu sớm trên BN; ladder demo ≠ AUROC lâm sàng. Khác `SYNTH-SCIENCE-CARD` (demo alone) / `TRIPOD-SYNTH` (reporting×demo) / `TRANSLATION-EQ` (in-vitro→người×ladder) — thẻ này neo **sandbox × ladder**.

**Mở song song:** thẻ này · `SYNTH-EQ-5MIN` · `SYNTH-SCIENCE-CARD` · `TRIPOD-SYNTH-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `TRANSLATION-EQ-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `PITFALLS-SCIENCE-CARD`

## Giữ / bỏ (SYNTH × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên \(Z\) sandbox / SYN | M4 / \(X\) người / AUROC = RCT |
| **Pipeline** | `verify.sh` PASS · schema CSV | “Early-signal đã hoạt động” |
| **Model demo** | AUROC M0–M3 sandbox = code path | AUROC SYN = evidence BN |
| **N thật** | de-ID site khi có | Coi SYN = N lâm sàng |
| **G2 / L3** | **CLOSED** | Pass / mở vì demo xanh |
| **Order / Goal** | KHÔNG từ densify | Đóng Goal / UpdateGoal trên PREP |

## Phương trình ranh giới

```text
1 artifact demo  +  EQ ladder M0–M3 trên Z_sandbox
  =  bước pipeline hợp lệ hôm nay
SYN / sandbox  ≠  N thật de-ID  ≠  BN lâm sàng
verify PASS    ≠  G2 pass       ≠  Goal complete
AUROC_SYN(M_k) ≠  evidence early-signal trên BN
Ladder demo    ≠  AUROC lâm sàng
Viết SYNTH×EQ  ≠  order PEA / mở biospecimen
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T4|T5 · Artifact: verify|CSV SYN|AUROC M__|khác — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
N thật de-ID đã có? CHƯA|CÓ (site) — ________
1 dòng Z / M0→M3 trên demo (chỉ pipeline): ________
Claim đúng 1 câu: ________
Claim SAI dễ nói: ________
Báo AUROC SYN = ES lâm sàng? KHÔNG
G2/L3 / đóng Goal vì demo xanh? KHÔNG
Cặp TRIPOD-SYNTH-EQ / TRANSLATION-EQ / LEAK-CROSS / PITFALLS-EQ hôm nay? ________
1 việc ≤30′ (verify skim / EQ Drill 10′ / deny-list): ________
Đóng Goal / UpdateGoal vì SYNTH×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở SYNTH + EQ sibling thẻ riêng trước cặp? ________
Demo+ladder = lý do G2 pass / AUROC lâm sàng? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | SYNTH×EQ bridge 1 trang |
| `SYNTH-EQ-5MIN` | Drill điền |
| `SYNTH-SCIENCE-CARD` | Demo alone |
| `TRIPOD-SYNTH` / `TRIPOD-SYNTH-EQ` | Reporting × demo / × ladder |
| `EQ-M0M3` | Ladder sibling (sandbox = rehearsal) |
| `TRANSLATION-EQ` / `LEAKAGE` / `PITFALLS` | Translation / leak / pitfalls |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Báo AUROC synthetic như RCT / ES lâm sàng  
- Coi PREP + verify xanh = Goal complete  
- Order PEA / mở G2 vì demo xanh · UpdateGoal trên PREP  

## Liên kết

`SYNTH-EQ-5MIN-MICRO-DRILL` · `SYNTH-SCIENCE-CARD` · `../analysis/verify.sh` · `TRIPOD-SYNTH-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `TRANSLATION-EQ-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `PITFALLS-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
