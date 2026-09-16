# L1→L2→L3 — thẻ khoa học 1 trang (cổng AI trước omics · sớm–dọc–AI)

**Mã:** L1L2L3-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** PB-009 · `L1L2L3-DAILY-GATE-CARD` · PEA = L3  
**Dùng khi:** T3 · T6 · CN PB-009 · EQ gate · sau STREAK≥3 · mọi lúc nói “omics / AI”  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · L3 **CLOSED** mặc định · G2 **CLOSED** · synthetic ≠ pass · PREP ≠ DONE  

## Mục đích

Ôn **thứ tự tầng** Precure/Smart A: tín hiệu sớm sống trên **L1** (\(Z\)+event) → exploratory **L2** (M0–M3 trên N thật) → omics **L3** (\(X\)) chỉ sau G2 — **không** đảo vì đã ôn PEA/EQ/atlas.

**Mở song song:** thẻ này · `L1L2L3-DAILY-GATE-CARD` · `PEA-WEEK1-SCIENCE-CARD` · `PB-009-AI-BEFORE-OMICS`

## Ba tầng → giữ / bỏ

| Tầng | Đủ khi | Giữ hôm nay | Bỏ |
|------|--------|-------------|-----|
| **L1** | ID–visit–time–event–\(Z\) (không PHI public) | Schema `clin_event` · ALERT nội bộ · BN-VISIT | Coi abstract = L1 đủ · PHI vào git |
| **L2** | M0–M3 pre-spec + de-ID; metrics trên **N thật** = L2.4 | Leakage check · EQ ladder · TRIPOD mock | `verify.sh` PASS trên SYN = L2.4 |
| **L3** | G2 + ethics G1 + \(X\) thêm giá trị | Ghi **CLOSED** + lý do | Order PEA / mở G2 vì đã điền gate |

## Phương trình cổng

```text
L1:  Z(t'), clin_event     ·  t' ≪ t*
L2:  M0–M3(Z) trên N thật  ·  leakage OFF
L3:  + X_omics             ·  chỉ sau G2
Hôm nay: L3 = CLOSED       ·  ALERT ≠ mở L3
```

## Checklist 15′ (1 SA)

```text
Thứ: T3|T6|CN · SA: 01|02|05 — chọn: ________
L1: CHƯA | SYN | N thật — thiếu: ________
L2: CHƯA | SYN QC | N thật — leakage? CÓ|CHƯA
L3: CLOSED vì ________ (G2 / chưa N / ethics / …)
1 rủi ro nếu đảo L3 trước L1/L2: ________
1 câu PB-009 (AI dọc không cần omics hôm nay): ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / gate card | Thứ tự tầng · L3 CLOSED |
| `PEA-WEEK1-SCIENCE-CARD` | PEA = \(X\) L3 · panel hẹp |
| `CLIN_EVENT-SCIENCE-CARD` | Schema event = **L1** |
| `LEAKAGE-SCIENCE-CARD` | L2 pitfall #1 thời gian |
| `ALERT-SCIENCE-CARD` | Hành động nội bộ trên L1 — **≠** mở L3 |

## Cấm

- Tick L2.4 / pass G2 bằng synthetic  
- Order omics vì PREP / densify / ALERT  
- Agent tick DONE · đóng Goal  

## Liên kết

`L1L2L3-DAILY-GATE-CARD` · `L1L2L3-5MIN` · `PB009-5MIN` · `G2-5MIN` · `OMICS-GATES-5MIN` · `PEA-WEEK1-SCIENCE-CARD` · `CLIN_EVENT-SCIENCE-CARD` · **`G2-SCIENCE-CARD`** · **`EQ-SCIENCE-CARD`** · **`OMICS-GATES-SCIENCE-CARD`** · **`AI-STACK-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3` · **`GLOSSARY-SCIENCE-CARD`**
