# EQ sibling map — densify closure (không tạo EQ trùng)

**Mã:** EQ-SIBLING-MAP-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack / densify / agent continue · trước khi ship EQ mới  
**Goal:** ACTIVE · PREP ≠ DONE · STREAK thật = PI DONE · L3 CLOSED  

## Mục đích

Một số token 5′ **không** có file `*-EQ-5MIN` riêng vì đã map sang sibling ×EQ đã ship.  
Tránh tạo `AMENDMENT-ES-EQ` / `CROSS-SA-EQ` / … trùng nghĩa.

## Bảng sibling (base → EQ đã có)

| Base / compound 5′ | Sibling ×EQ (đã có) | Ghi chú |
|--------------------|---------------------|---------|
| `AMENDMENT-ES-5MIN` | **`AMENDMENT-EQ-5MIN`** | AMENDMENT-ES × EQ |
| `SAP-ES-5MIN` | **`SAP-EQ-5MIN`** | SAP-ES × EQ |
| `TT43-AMEND-5MIN` | **`TT43-EQ-5MIN`** | TT43×AMEND + ladder |
| `ICF-NEST-5MIN` | **`ICF-EQ-5MIN`** | ICF-NEST × EQ |
| `CROSS-SA-5MIN` | **`CROSS-EQ-5MIN`** | CROSS-SA × EQ |
| `IMAGEJ-QA-5MIN` | **`IMAGEJ-EQ-5MIN`** | IMAGEJ QA × EQ |
| `EQ-5MIN` / `EQ-M0M3` / `EQ02` / `EQ05` | *(meta)* · **`EQ-M0M3-SCIENCE-CARD`** · **`EQ02-M0M3-SCIENCE-CARD`** | bản thân là ladder — không cần ×EQ riêng |

## Compound×EQ đã ship (không sibling)

`SPIRIT-G1-EQ` · `DEID-MISS-EQ` · `VAS-LEAK-EQ` · `PUSH-ALERT-EQ` · `ALERT-HAWTHORNE-EQ` · `IMAGEJ-EPI-EQ` · `ALERT-CROSS-EQ` · `MEDIA-SHIFT-EQ` · `L1L2L3-SHIFT-EQ` · `SHIFT-PB007-EQ` · `TRIPOD-SYNTH-EQ` · `CONSORT-SPIRIT-EQ` · `LEAK-CROSS-EQ` · `NATMED-ALERT-EQ` · …

## Quy tắc agent

1. Trước ship EQ mới: mở map này + `ls *-EQ-5MIN*`  
2. Nếu base đã có sibling → **không** tạo file EQ trùng tên base  
3. STREAK&lt;3 → ưu tiên **`STREAK3-NOW-1PAGE`** · **`STREAK3-FILL-AID`** · **`STREAK3-EQ-5MIN-SCIENCE-CARD`** (không tick DONE thay PI)  
4. STREAK≥3 → `DAILY-STACK-AFTER-STREAK3` + **`EQ-SIBLING-MAP-SCIENCE-CARD`** + EQ ladders  

## Anti-forget (PI)

| STREAK | Mở |
|--------|-----|
| &lt;3 | `STREAK3-NOW-1PAGE` · `STREAK3-FILL-AID` · log `2026-09-19` · tracker |
| ≥3 | `DAILY-STACK-AFTER-STREAK3` · weekly #13 · MISS #14 |

## Cấm

- Agent tick STREAK DONE · UpdateGoal complete trên PREP  
- Biospecimen trước G1–G2 · synthetic = BN  
- Ship EQ trùng sibling “cho đủ tên”  

## Liên kết

`EQ-SIBLING-MAP-SCIENCE-CARD` · `EQ-SCIENCE-CARD` · `STREAK3-EQ-5MIN-SCIENCE-CARD` · `RITUAL-CARDS-INDEX` · `WORKSHEET-INDEX` · `DAILY-STACK-AFTER-STREAK3` · `PI-NEXT-45MIN` · `STREAK_TRACKER`
