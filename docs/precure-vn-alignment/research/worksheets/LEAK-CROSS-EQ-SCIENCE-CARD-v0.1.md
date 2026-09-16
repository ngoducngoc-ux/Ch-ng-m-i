# LEAK-CROSS-EQ — thẻ khoa học 1 trang (leakage×schema × ladder · ≠ gộp Y)

**Mã:** LEAK-CROSS-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `LEAK-CROSS-EQ-5MIN-MICRO-DRILL` · LEAK-CROSS-SCIENCE-CARD · LEAKAGE-EQ · CROSS-EQ · PITFALLS-EQ · EQ-M0M3 · VAS-LEAK  
**Căn cứ:** LEAKAGE-CROSS-SA-ATLAS · G2 CLOSED · L3 CLOSED  
**Dùng khi:** STREAK≥3 · Daily stack **T4/T6/CN** · trước claim “một model early chung” · cặp LEAK-CROSS×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · mỗi SA một \(Y(t^*)\) · ladder chỉ feature hợp lệ · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cặp LEAK-CROSS×EQ**: so schema \(t^*\)/\(Z\) giữa SA **và** 1 dòng ladder M0–M3 chỉ trên feature hợp lệ — không \(Y(t^*)\) early · không gộp Y · AUROC sandbox ≠ BN. Khác `LEAK-CROSS-SCIENCE-CARD` (schema alone) / `LEAKAGE-EQ` (timestamp×ladder) / `CROSS-EQ` (schema×ladder) — thẻ này neo **leak×schema × ladder**.

**Mở song song:** thẻ này · `LEAK-CROSS-EQ-5MIN` · `LEAK-CROSS-SCIENCE-CARD` · `LEAKAGE-EQ-5MIN` · `CROSS-EQ-5MIN` · `PITFALLS-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `VAS-LEAK-SCIENCE-CARD`

## Giữ / bỏ (LEAK-CROSS × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **EQ ladder** | M0–M3 trên feature hợp lệ / \(Z\) | \(Y(t^*)\) làm early feature |
| **Schema** | So \(t^*\) / \(Z\) từng SA | Gộp Y nhiều SA thành 1 model |
| **Leak** | Timestamp trước \(t^*\) | Outcome leak vào M early |
| **Cross-SA** | Map song song · không merge primary | “Một AUROC early chung” |
| **Sandbox** | Label pipeline | AUROC SYN = BN evidence |
| **Order / Goal** | KHÔNG từ densify | Order omics / đóng Goal vì đã ôn |

## Phương trình ranh giới

```text
1 schema so sánh SA (t*/Z)  +  EQ ladder M0–M3 chỉ feature hợp lệ
  =  bước anti-leak×cross hợp lệ hôm nay
Mỗi SA 1 Y(t*)  ≠  gộp Y  ≠  “model early chung”
Feature hợp lệ  ≠  evidence BN  ≠  AUROC lâm sàng
Ôn LEAK-CROSS×EQ  ≠  order omics / UpdateGoal
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T4|T6|CN · SA đang ôn (không gộp): 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
t* primary: D21|VAS_D3|PUSH_D14 — ________
1 feature LEAKAGE nếu vào M early: ________
1 feature HỢP LỆ: ________
1 dòng Z / M0→M3 (chỉ feature hợp lệ): ________
Gộp Y / AUROC SYN = BN / VAS_D3|PUSH_D14 early? KHÔNG
Cặp PITFALLS-EQ / **`CONSORT-SPIRIT-EQ-SCIENCE-CARD`** / VAS-LEAK-EQ / ALERT-CROSS-EQ hôm nay? ________
1 việc ≤30′ (atlas / CROSS map / EQ Drill 10′): ________
Đóng Goal / order omics vì LEAK-CROSS×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở LEAK-CROSS + EQ sibling thẻ riêng trước cặp? ________
Schema+ladder = lý do gộp Y / AUROC lâm sàng? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | LEAK-CROSS×EQ bridge 1 trang |
| `LEAK-CROSS-EQ-5MIN` | Drill điền |
| `LEAK-CROSS-SCIENCE-CARD` | Schema alone |
| `LEAKAGE-EQ` / `CROSS-EQ` | Timestamp / schema × ladder |
| `PITFALLS-EQ` / `VAS-LEAK-EQ` | Pitfalls / VAS×leak × ladder |
| `EQ-M0M3` | Ladder sibling |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- \(Y(t^*)\) làm early feature · gộp Y nhiều SA  
- Chọn cờ/power theo AUROC sandbox · UpdateGoal trên PREP  

## Liên kết

`LEAK-CROSS-EQ-5MIN-MICRO-DRILL` · `LEAK-CROSS-SCIENCE-CARD` · `LEAKAGE-CROSS-SA-ATLAS` · `PITFALLS-EQ-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `CROSS-SA-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `VAS-LEAK-SCIENCE-CARD` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
