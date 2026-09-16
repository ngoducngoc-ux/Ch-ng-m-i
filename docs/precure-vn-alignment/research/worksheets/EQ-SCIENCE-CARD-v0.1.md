# EQ — thẻ khoa học 1 trang (ladder M0–M3 · \(Z\) trước \(X\) · sớm–dọc–AI)

**Mã:** EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** PB-007 · `EQ-SA01|02|05` · SAP ES M0–M3  
**Dùng khi:** T2/T4/T6 · EQ Drill 10′ · mọi ×EQ sibling · sau STREAK≥3  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · \(Y(t^*)\) không đổi · M0–M3 trên \(Z\) · M4/L3 **CLOSED** · synthetic ≠ BN · PREP ≠ DONE  

## Mục đích

Ôn **phương trình early-signal** Precure/Smart A: ladder M0→M3 chỉ dùng \(Z(t')\) với \(t'\ll t^*\) — **rồi** mới hỏi \(X\) sau G2. AUROC sandbox ≠ bằng chứng BN.

**Mở song song:** thẻ này · `PB-007-equation-framework` · `EQ-5MIN` · `EQ-M0M3-5MIN` / `EQ02-M0M3` / `EQ05-M0M3`

## Ba SA → ba ladder (giữ / bỏ)

| SA | \(Y(t^*)\) | Ladder \(Z(t')\) | Giữ | Bỏ |
|----|------------|------------------|-----|-----|
| **01** | D21 biểu mô | M0 D0 → M1 D3 → M2 Δ → M3 D0–D7+`clin_event` | PCT/CFU/VAS early | PCT_D21 làm early · M4/PEA trước G2 |
| **02** | VAS relief D3 | M0–M3 ưu tiên D1/CFU/Δ trước D3 | Series sớm | VAS_D3 trong feature early (= leakage) |
| **05** | PUSH D14 | PUSH/CFU/TURN ≤D7 | Component exploratory | Auto-treat ICU · gộp Y với 01/02 |

## Phương trình

```text
P(Y=1) = σ( β0 + β_Zᵀ Z(t') + … )
         rồi (chỉ sau G2): + β_Xᵀ X(t')
M0–M3: Z only     ·     M4/X: CLOSED hôm nay
AUROC sandbox ≠ evidence BN
```

## Checklist 15′ (1 SA)

```text
Thứ: T2|T4|T6 · SA: 01|02|05 — chọn: ________
Y(t*) xác nhận không đổi? CÓ | ghi: ________
t' early hôm nay: ________
M0 | M1 | M2 | M3 (1 dòng mỗi bước đang ôn): ________
1 feature KHÔNG dùng (leakage / t*): ________
M4/X/L3: CLOSED vì ________
1 câu PB-007 (Z rồi X): ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / PB-007 | Ladder EQ · \(Z\) trước \(X\) |
| `ENDPOINTS-WEEK1-SCIENCE-CARD` | \(t^*\neq Z\) sớm · không gộp \(Y\) |
| `LEAKAGE-SCIENCE-CARD` | Feature sau \(t^*\) / trùng \(Y\) → không vào M early |
| `L1L2L3-SCIENCE-CARD` | Tầng cổng — EQ sống ở L1/L2 |
| `ALERT-SCIENCE-CARD` | Hành động nội bộ trên \(Z\) — ≠ đổi \(Y\) |

## Cấm

- Đổi primary / train chung 3 SA / mở M4 vì đã viết σ(…+X)  
- Coi AUROC SYN = lâm sàng  
- Agent tick DONE · đóng Goal  

## Liên kết

`PB-007-equation-framework` · `EQ-5MIN` · `EQ-M0M3-5MIN` · `EQ02-M0M3-5MIN` · `EQ05-M0M3-5MIN` · `PB007-EQ-5MIN` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `L1L2L3-SCIENCE-CARD` · **`G2-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3`
