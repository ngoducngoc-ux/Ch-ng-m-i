# G2 — thẻ khoa học 1 trang (omics gate · CLOSED mặc định · sớm–dọc–AI)

**Mã:** G2-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `G2-READINESS` · Wik MCP [10.1016/j.mcpro.2021.100168](https://doi.org/10.1016/j.mcpro.2021.100168) · PB-009  
**Dùng khi:** T3/T5 · trước mọi “sắp lấy mẫu / order PEA” · INTERIM-G2 · OMICS-IF  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · G2 **CLOSED** mặc định · L3 CLOSED · synthetic ≠ pass · không biospecimen trước G1–G2 · PREP ≠ DONE  

## Mục đích

Ôn **cổng mở omics** Smart A: ba điều kiện trên **N thật** + ethics + logistics — **không** pass bằng `verify.sh`/AUROC sandbox. Chưa đủ → không order mẫu / PEA.

**Mở song song:** thẻ này · `G2-READINESS` · `L1L2L3-SCIENCE-CARD` · `PEA-WEEK1-SCIENCE-CARD`

## Ba điều kiện → giữ / bỏ

| # | Điều kiện | Giữ hôm nay | Bỏ |
|---|-----------|-------------|-----|
| **1 Signal \(Z\)** | ΔAUROC M1/M2 vs M0 pre-spec **hoặc** quyết định PI/DSMB từ interim trên N thật | Ghi CLOSED + thiếu gì | Pass G2 bằng SYN AUROC |
| **2 Ethics G1** | ICF/amendment cho phép lưu & phân tích mẫu | `[CẦN XÁC NHẬN]` HĐĐĐ | Coi Git PREP = ethics xong |
| **3 Logistics** | SOP pre-analytic + chuỗi lạnh + LIMS tách REDCap | R1–R3 / pipeline map | Order lab vì đã ôn Wik |

## Phương trình cổng

```text
G2 = Signal_Z(N thật) ∧ Ethics_G1 ∧ Logistics
Hôm nay: G2 = CLOSED
L3/X_omics: CLOSED  ·  ALERT ≠ mở G2
verify.sh / AUROC sandbox ≠ pass G2
```

## Checklist 15′ (SA-01 cờ đầu)

```text
Thứ: T3|T5 · G2 hôm nay: CLOSED | PREP checklist | PASS (chỉ PI/DSMB)
Signal Z trên N thật? CHƯA | INTERIM | CÓ — ghi: ________
Ethics G1? CHƯA [CẦN XÁC NHẬN] | CÓ
Logistics / pre-analytic? CHƯA | PREP | CÓ — thiếu: ________
verify/AUROC sandbox pass G2? KHÔNG — vì: ________
Order PEA/omics hôm nay? KHÔNG
1 việc ≤30′ (G2-READINESS tick / PB009 / PREANALYTIC / OMICS-IF skip): ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / `G2-READINESS` | Ba điều kiện mở omics |
| `L1L2L3-SCIENCE-CARD` | Thứ tự tầng — G2 nằm giữa L2→L3 |
| `PEA-WEEK1-SCIENCE-CARD` | PEA = \(X\) sau G2 |
| `EQ-SCIENCE-CARD` | M0–M3 trên \(Z\) — **trước** G2 |
| `INTERIM-G2` / `OMICS-IF` | Mock interim · skip L3 khi CLOSED |

## Cấm

- Synthetic / densify / ALERT = pass G2  
- Biospecimen / order omics trước G1–G2  
- Agent tick DONE · đóng Goal  

## Liên kết

`G2-READINESS` · `G2-5MIN` · `G2-EQ-5MIN` · `INTERIM-G2-5MIN` · `OMICS-IF-5MIN` · `OMICS-GATES-5MIN` · `PB009-5MIN` · `L1L2L3-SCIENCE-CARD` · `PEA-WEEK1-SCIENCE-CARD` · `EQ-SCIENCE-CARD` · **`SHIFT-SCIENCE-CARD`** · **`SYNTH-SCIENCE-CARD`** · **`OMICS-GATES-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3`
