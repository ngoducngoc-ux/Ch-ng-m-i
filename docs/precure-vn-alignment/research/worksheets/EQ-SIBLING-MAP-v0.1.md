# EQ sibling map — densify closure (không tạo EQ trùng) · refresh v0.1b

**Mã:** EQ-SIBLING-MAP-v0.1  
**Ngày:** 2026-09-16 (refresh sau STREAK3-EQ / TRIPOD-EQ / PB008-EQ / PB007-EQ)  
**Dùng khi:** Daily stack / densify / agent continue · trước khi ship EQ mới  
**Goal:** ACTIVE · PREP ≠ DONE · STREAK thật = PI DONE · L3 CLOSED  
**Milestone:** mọi `*-EQ-5MIN-MICRO-DRILL` đã có `*-EQ-SCIENCE-CARD` khớp (0 missing)

## Mục đích

Một số token 5′ **không** có file `*-EQ-5MIN` riêng vì đã map sang sibling ×EQ đã ship.  
Tránh tạo `AMENDMENT-ES-EQ` / `CROSS-SA-EQ` / … trùng nghĩa.  
Sau ladder densify: **chọn 1 sibling/ngày** từ bank đã có — không ship EQ “cho đủ tên”.

## Bảng sibling (base → EQ đã có)

| Base / compound 5′ | Sibling ×EQ (đã có) | Ghi chú |
|--------------------|---------------------|---------|
| `AMENDMENT-ES-5MIN` | **`AMENDMENT-EQ-5MIN`** · **`AMENDMENT-EQ-SCIENCE-CARD`** | AMENDMENT-ES × EQ |
| `SAP-ES-5MIN` | **`SAP-EQ-5MIN`** · **`SAP-EQ-SCIENCE-CARD`** | SAP-ES × EQ |
| `TT43-AMEND-5MIN` | **`TT43-EQ-5MIN`** · **`TT43-EQ-SCIENCE-CARD`** | TT43×AMEND + ladder |
| `ICF-NEST-5MIN` | **`ICF-EQ-5MIN`** · **`ICF-EQ-SCIENCE-CARD`** | ICF-NEST × EQ |
| `CROSS-SA-5MIN` | **`CROSS-EQ-5MIN`** · **`CROSS-EQ-SCIENCE-CARD`** | CROSS-SA × EQ |
| `IMAGEJ-QA-5MIN` | **`IMAGEJ-EQ-5MIN`** · **`IMAGEJ-EQ-SCIENCE-CARD`** | IMAGEJ QA × EQ |
| `TRIPOD-5MIN` / `TRIPOD-SYNTH-5MIN` | **`TRIPOD-EQ-5MIN`** · **`TRIPOD-EQ-SCIENCE-CARD`** · **`TRIPOD-SYNTH-EQ`** | reporting × ladder · ≠ SYNTH pair alone |
| `PB001-5MIN` … `PB003-5MIN` | **`PB001-EQ`** · **`PB002-EQ`** · **`PB003-EQ`** (+ SCIENCE-CARD) | SA support × ladder |
| `PB007-5MIN` / framework | **`PB007-EQ-5MIN`** · **`PB007-EQ-SCIENCE-CARD`** · **`SHIFT-PB007-EQ`** | framework × ladder · ≠ shift pair |
| `PB008-5MIN` / Hawthorne | **`PB008-EQ-5MIN`** · **`PB008-EQ-SCIENCE-CARD`** · **`HAWTHORNE-EQ`** | participation × ladder |
| `STREAK3-5MIN` / PACK | **`STREAK3-EQ-5MIN`** · **`STREAK3-EQ-SCIENCE-CARD`** · **`STREAK3-EQ-5MIN-SCIENCE-CARD`** | path × ladder · ≠ DONE trên PREP |
| `EQ-5MIN` / `EQ-M0M3` / `EQ02` / `EQ05` | *(meta)* · **`EQ-M0M3-SCIENCE-CARD`** · **`EQ02-M0M3-SCIENCE-CARD`** · **`EQ05-M0M3-SCIENCE-CARD`** | bản thân là ladder — không cần ×EQ riêng |

## Singles ×EQ đã ship (1 sibling/ngày sau STREAK≥3)

`ALERT-EQ` · `BACKLOG-EQ` · `CLIN_EVENT-EQ` · `CROSS-EQ` · `DEID-EQ` · `EPI-EQ` · `G2-EQ` · `GLOSSARY-EQ` · `HAWTHORNE-EQ` · `IMAGEJ-EQ` · `L1L2L3-EQ` · `LEAKAGE-EQ` · `MEDIA-EQ` · `MISSINGNESS-EQ` · `PB001-EQ` · `PB002-EQ` · `PB003-EQ` · `PB007-EQ` · `PB008-EQ` · `PUSH-EQ` · `SHIFT-EQ` · `STREAK3-EQ` · `SYNTH-EQ` · `TRIPOD-EQ` · `VAS-EQ` · …

## Compound×EQ đã ship (không sibling trùng tên)

`SPIRIT-G1-EQ` · `DEID-MISS-EQ` · `VAS-LEAK-EQ` · `PUSH-ALERT-EQ` · `ALERT-HAWTHORNE-EQ` · `IMAGEJ-EPI-EQ` · `ALERT-CROSS-EQ` · `MEDIA-SHIFT-EQ` · `L1L2L3-SHIFT-EQ` · `SHIFT-PB007-EQ` · `TRIPOD-SYNTH-EQ` · `CONSORT-SPIRIT-EQ` · `LEAK-CROSS-EQ` · `NATMED-ALERT-EQ` · `MISS-RESCUE-EQ` · …

## Quy tắc agent

1. Trước ship EQ mới: mở map này + `ls *-EQ-5MIN*` + `ls *-EQ-SCIENCE-CARD*`  
2. Nếu base đã có sibling → **không** tạo file EQ trùng tên base  
3. STREAK&lt;3 → ưu tiên **`STREAK3-PACK`** · **`STREAK3-EQ-SCIENCE-CARD`** · NOW · FILL-AID (không tick DONE thay PI)  
4. STREAK≥3 → `AFTER-STREAK3-OPENER` → **1×** sibling từ map → `SCIENCE-BRIDGES` → `DAILY-STACK`  
5. Ladder densify từ `*-EQ-5MIN` drills: **CLOSED** — tip tiếp = refresh map / bridges · không invent EQ mới “cho đủ”

## Anti-forget (PI)

| STREAK | Mở |
|--------|-----|
| &lt;3 | `STREAK3-PACK` · `STREAK3-EQ-SCIENCE-CARD` · NOW · FILL-AID · log `2026-09-19` · tracker |
| ≥3 | OPENER · **1×EQ sibling** · `SCIENCE-BRIDGES` · `DAILY-STACK-AFTER-STREAK3` · weekly #13 · MISS #14 |

## Cấm

- Agent tick STREAK DONE · UpdateGoal complete trên PREP  
- Biospecimen trước G1–G2 · synthetic = BN  
- Ship EQ trùng sibling “cho đủ tên” · mở hết map 1 ngày  

## Liên kết

`EQ-SIBLING-MAP-SCIENCE-CARD` · `EQ-SCIENCE-CARD` · **`STREAK3-EQ-SCIENCE-CARD`** · `STREAK3-EQ-5MIN-SCIENCE-CARD` · **`TRIPOD-EQ-SCIENCE-CARD`** · **`PB008-EQ-SCIENCE-CARD`** · **`PB007-EQ-SCIENCE-CARD`** · **`SCIENCE-BRIDGES-SCIENCE-CARD`** · `RITUAL-CARDS-INDEX` · `WORKSHEET-INDEX` · `DAILY-STACK-AFTER-STREAK3` · `PI-NEXT-45MIN` · `STREAK_TRACKER`
