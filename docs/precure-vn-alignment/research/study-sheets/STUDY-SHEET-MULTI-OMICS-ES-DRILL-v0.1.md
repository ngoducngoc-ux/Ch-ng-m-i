# Study sheet — Multi-omics / early-signal daily drill (15′)

**Mã:** STUDY-MULTI-OMICS-ES-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** STREAK ≥3 · sau (hoặc thay một phần) bridge rotation #12 · **không** thay STREAK3 nếu STREAK &lt;3  
**Goal:** ACTIVE · G2/L3 **CLOSED** trừ pass thật · PREP ≠ DONE

## Mục tiêu một câu

> Mỗi ngày viết **3–5 dòng** chứng tỏ đã ôn multi-omics + tín hiệu sớm + lệch hướng Smart A / y tế số — không chỉ mở file.

## Trước drill (30″)

Chọn **1** nguồn hôm nay:
- Bridge theo thứ (`BRIDGE-ROTATION` #12), **hoặc**
- Study sheet Zhou / NatMed-PEA / Endpoints / DESIGN-YTESO / Tier3, **hoặc**
- EQ theo **rotation tuần** dưới (1 SA / ngày — không gộp)

STREAK &lt;3 → dừng · mở `PI-SESSION-SCRIPT-STREAK3`.  
STREAK ≥3 → có thể mở **`DAILY-STACK-AFTER-STREAK3`** (1 trang) thay vì chọn tay.

### EQ rotation (sau STREAK≥3 · 1 file / ngày)

| Thứ (ICT) | EQ Drill 10′ | Neo ôn |
|-----------|--------------|--------|
| **T2** | `EQ-SA01` · **`EQ-5MIN`** / **`PB007-5MIN`** / **`PB001-5MIN`** / **`GLOSSARY-5MIN`** | \(t'\ll D21\) · `EPI-SA01-EARLY-WINDOW` · **`EPI-5MIN`** · `IMAGEJ-QA-5MIN` · **`PB008-5MIN`** · PEA CLOSED |
| **T3** |Bridge #12 + **`L1L2L3-5MIN`** | PEA / L1→L2 trước L3 · `L1L2L3-DAILY-GATE-CARD` · `PEA-5MIN` / `PB009-5MIN` / **`G2-5MIN`** / **`OMICS-GATES-5MIN`** / **`AI-STACK-5MIN`** |
| **T4** | `EQ-SA02` · **`EQ-5MIN`** / **`PB007-5MIN`** / **`PB002-5MIN`** / **`CROSS-SA-5MIN`** | leakage M1 · `VAS-SCALE-HARMONIZE-SA02` · **`VAS-5MIN`** · `LEAKAGE-5MIN` / **`PITFALLS-5MIN`** / `SYNTH-5MIN` · không gộp Y |
| **T5** | Bridge #12 | DESIGN-YTESO · `TRIPOD-5MIN` **hoặc** `DEID-5MIN` **hoặc** `MISSINGNESS-5MIN` **hoặc** `SYNTH-5MIN` **hoặc** `PITFALLS-5MIN` **hoặc** `SPIRIT-5MIN` **hoặc** `CONSORT-5MIN` **hoặc** `TT43-5MIN` **hoặc** `PB004-5MIN` **hoặc** `PB005-5MIN` **hoặc** `TRANSLATION-5MIN` **hoặc** `PB006-5MIN` **hoặc** `PB009-5MIN` **hoặc** `G2-5MIN` **hoặc** `OMICS-GATES-5MIN` **hoặc** `AI-STACK-5MIN` **hoặc** `YTESO-5MIN` |
| **T6** | `EQ-SA05` · **`EQ-5MIN`** / **`PB007-5MIN`** / **`PB003-5MIN`** / **`CROSS-SA-5MIN`** | PUSH component · **`PUSH-5MIN`** · không auto-treat |
| **T7 / CN** | Tuỳ chọn 1 EQ còn thiếu trong tuần **hoặc** #13/#14 · `CLIN_EVENT-5MIN` / `BN-VISIT-5MIN` / **`PB008-5MIN`** / **`MEDIA-5MIN`** (CN) | PB lens / MISS / L1 dọc / claim |

*Quy tắc:* không làm 2 EQ cùng ngày; nếu makeup MISS → EQ của **thứ bị miss**.

## Drill A — Ba trụ (5′)

Điền **không nhìn** glossary trước; sau đó đối chiếu `EARLY-SIGNAL-GLOSSARY`.  
Hôm nay neo SA: **01** | **02** | **05** (khoanh 1).

```text
SA neo: 01|02|05
t*: ________     t' cửa sổ early: ________
Z hôm nay (1 biến eCRF): ________
Event / clin_event (nếu có): ________
X / L3: CLOSED vì ________ (G2 / chưa N thật / …)
1 câu t' ≪ t* (đúng primary SA đó):
Atlas sự kiện: `CLIN_EVENT-CROSS-SA-ATLAS` (1 hàng SA)
```

## Drill B — Multi-omics / AI (5′)

```text
L1 đủ chưa? (ID–visit–clin_event–Z): CÓ | CHƯA — thiếu: ________
Atlas L1/event: `CLIN_EVENT-CROSS-SA-ATLAS` | map: `BN-VISIT-5MIN` · `BN-VISIT-MAP-TEMPLATE`
L2 (M0–M3) trên: synthetic | N thật de-ID | chưa có
Vì sao chưa order PEA / omics hôm nay (1 câu):
PB-009: L1→L2 trước L3 — 1 rủi ro nếu đảo thứ tự:
Gate card: `L1L2L3-DAILY-GATE-CARD` (khoanh L1/L2/L3 hôm nay)
Leakage (đặc biệt SA-02 M1 sandbox): ________
Atlas đối chiếu: `LEAKAGE-CROSS-SA-ATLAS` (1 hàng SA hôm nay)
```

## Drill C — Smart A / y tế số (5′)

Chọn **1**:

| Chọn | Việc |
|------|------|
| **PB** | 1 hàng `PB-EARLY-SIGNAL-LENS` (#13) — PB-00__ · trụ Sớm\|Dọc\|AI |
| **Y tế số** | Checklist tuần `y-te-so` **hoặc** 1 hàng `CLIN_EVENT-CROSS-SA-ATLAS` / `BN-VISIT-5MIN` |
| **ALERT** | 1 hàng `ALERT-CROSS-SA-ATLAS` **hoặc** `ALERT-5MIN-MICRO-DRILL` · “actionable ≠ Dx” |
| **Shift** | **`SHIFT-5MIN`** **hoặc** 1 câu từ `PRECURE-SHIFT-CROSS-SA-BANK` (tự viết lại · ≤25 từ) |
| **EQ cross-SA** | Drill 10′ trong `EQ-SA02` hoặc `EQ-SA05` (không gộp Y) |

```text
Chọn: PB | Y tế số | ALERT | Shift | EQ-02 | EQ-05
1 insight / 1 câu lệch hướng:
1 câu cấm overclaim / cấm gộp endpoint:
```

## Sau drill → STREAK

- [ ] Ghi insight vào `daily-log/YYYY-MM-DD.md`  
- [ ] PI tick **DONE** trên `STREAK_TRACKER` (không để PREP)  
- [ ] Goal vẫn **ACTIVE**  
- [ ] Nếu MISS gần đây: `MISS-RESCUE` (#14)

## Cấm

- Coi drill PREP agent = STREAK DONE  
- AUROC sandbox / synthetic = bằng chứng BN  
- Mở G2 vì đã trả lời đủ ô fill-in  

## Liên kết

- Index: `STUDY-SHEET-INDEX.md` · Bridges: `SCIENCE-BRIDGES-INDEX` #12–14  
- EQ: `../equations/EQ-SA01|02|05-early-warning-v0.1.md` (mỗi file có Drill 10′)  
- Leakage atlas: `../worksheets/LEAKAGE-CROSS-SA-ATLAS-v0.1.md`  
- LEAKAGE 5′: `../worksheets/LEAKAGE-5MIN-MICRO-DRILL-v0.1.md` (T4)  
- IMAGEJ QA 5′: `../worksheets/IMAGEJ-QA-5MIN-MICRO-DRILL-v0.1.md` (T2)  
- BN visit 5′: `../worksheets/BN-VISIT-5MIN-MICRO-DRILL-v0.1.md` (T7)  
- Missingness 5′: `../worksheets/MISSINGNESS-5MIN-MICRO-DRILL-v0.1.md` (T5)  
- Media 5′: `../worksheets/MEDIA-5MIN-MICRO-DRILL-v0.1.md` (CN · STREAK3)   
- Synth 5′: `../worksheets/SYNTH-5MIN-MICRO-DRILL-v0.1.md` (T4/T5)  
- SPIRIT 5′: `../worksheets/SPIRIT-5MIN-MICRO-DRILL-v0.1.md` (T5)  
- CONSORT 5′: `../worksheets/CONSORT-5MIN-MICRO-DRILL-v0.1.md` (T5)  
- TT43 5′: `../worksheets/TT43-5MIN-MICRO-DRILL-v0.1.md` (T5)  
- PB-004 5′: `../worksheets/PB004-5MIN-MICRO-DRILL-v0.1.md` (T5/T7)  
- PB-009 5′: `../worksheets/PB009-5MIN-MICRO-DRILL-v0.1.md` (T3/T5)  
- EPI 5′: `../worksheets/EPI-5MIN-MICRO-DRILL-v0.1.md` (T2)  
- VAS 5′: `../worksheets/VAS-5MIN-MICRO-DRILL-v0.1.md` (T4)  
- PUSH 5′: `../worksheets/PUSH-5MIN-MICRO-DRILL-v0.1.md` (T6)  
- G2 5′: `../worksheets/G2-5MIN-MICRO-DRILL-v0.1.md` (T3/T5)  
- EQ 5′: `../worksheets/EQ-5MIN-MICRO-DRILL-v0.1.md` (T2/T4/T6)  
- SHIFT 5′: `../worksheets/SHIFT-5MIN-MICRO-DRILL-v0.1.md` (mọi thứ)  
- L1L2L3 5′: `../worksheets/L1L2L3-5MIN-MICRO-DRILL-v0.1.md` (T3/T6)  
- PB-008 5′: `../worksheets/PB008-5MIN-MICRO-DRILL-v0.1.md` (T7/T2/CN)  
- PB-007 5′: `../worksheets/PB007-5MIN-MICRO-DRILL-v0.1.md` (T2/T3/T4/T6/CN)  
- PB-001 5′: `../worksheets/PB001-5MIN-MICRO-DRILL-v0.1.md` (T2/CN · cờ đầu)  
- PB-002 5′: `../worksheets/PB002-5MIN-MICRO-DRILL-v0.1.md` (T4/CN · SA-02 support)  
- PB-003 5′: `../worksheets/PB003-5MIN-MICRO-DRILL-v0.1.md` (T6/CN · SA-05 support)  
- PB-005 5′: `../worksheets/PB005-5MIN-MICRO-DRILL-v0.1.md` (T5/CN · biofilm proxy)  
- PB-006 5′: `../worksheets/PB006-5MIN-MICRO-DRILL-v0.1.md` (T5/CN · ISO cổng)  
- OMICS-GATES 5′: `../worksheets/OMICS-GATES-5MIN-MICRO-DRILL-v0.1.md` (T3/T5)  
- AI-STACK 5′: `../worksheets/AI-STACK-5MIN-MICRO-DRILL-v0.1.md` (T3/T5/T7)  
- YTESO 5′: `../worksheets/YTESO-5MIN-MICRO-DRILL-v0.1.md` (T5/T7/CN)  
- TRANSLATION 5′: `../worksheets/TRANSLATION-5MIN-MICRO-DRILL-v0.1.md` (T5/CN)  
- STREAK3 5′: `../worksheets/STREAK3-5MIN-MICRO-DRILL-v0.1.md` (STREAK&lt;3)  
- CROSS-SA 5′: `../worksheets/CROSS-SA-5MIN-MICRO-DRILL-v0.1.md` (T4/T6/CN)  
- GLOSSARY 5′: `../worksheets/GLOSSARY-5MIN-MICRO-DRILL-v0.1.md` (mọi thứ)  
- PITFALLS 5′: `../worksheets/PITFALLS-5MIN-MICRO-DRILL-v0.1.md` (T4/T5)  
- MISS-RESCUE 5′: `../worksheets/MISS-RESCUE-5MIN-MICRO-DRILL-v0.1.md` (khi MISS · #14)  
- BACKLOG 5′: `../worksheets/BACKLOG-5MIN-MICRO-DRILL-v0.1.md` (STREAK thấp · nhiều PREP)  
- PREANALYTIC 5′: `../worksheets/PREANALYTIC-5MIN-MICRO-DRILL-v0.1.md` (T3 · PEA R1–R3)  
- PEA-PANEL 5′: `../worksheets/PEA-PANEL-5MIN-MICRO-DRILL-v0.1.md` (T3 · hẹp ≠ 96 mù)  
- INTERIM-G2 5′: `../worksheets/INTERIM-G2-5MIN-MICRO-DRILL-v0.1.md` (T3/T5 · G2 CLOSED)  
- OMICS-IF 5′: `../worksheets/OMICS-IF-5MIN-MICRO-DRILL-v0.1.md` (T3/T5 · skip L3)  
- ISO-SWAB 5′: `../worksheets/ISO-SWAB-5MIN-MICRO-DRILL-v0.1.md` (T5 · SA-04 G5)  
- HAWTHORNE 5′: `../worksheets/HAWTHORNE-5MIN-MICRO-DRILL-v0.1.md` (T2/T7/CN · ≠ primary)  
- SPIRIT-G1 5′: `../worksheets/SPIRIT-G1-5MIN-MICRO-DRILL-v0.1.md` (T5 · nested ethics trước biospecimen)  
- ICF-NEST 5′: `../worksheets/ICF-NEST-5MIN-MICRO-DRILL-v0.1.md` (T5 · consent tách)  
- AMENDMENT-ES 5′: `../worksheets/AMENDMENT-ES-5MIN-MICRO-DRILL-v0.1.md` (T5 · outline ES)  
- ALERT×Hawthorne 5′: `../worksheets/ALERT-HAWTHORNE-5MIN-MICRO-DRILL-v0.1.md` (T2/T4/T6/T7/CN)  
- SAP-ES 5′: `../worksheets/SAP-ES-5MIN-MICRO-DRILL-v0.1.md` (T5 · §7/7.1)  
- TT43×AMEND 5′: `../worksheets/TT43-AMEND-5MIN-MICRO-DRILL-v0.1.md` (T5 · số điều)  
- CONSORT×SPIRIT 5′: `../worksheets/CONSORT-SPIRIT-5MIN-MICRO-DRILL-v0.1.md` (T5 · placement)  
- TRIPOD×SYNTH 5′: `../worksheets/TRIPOD-SYNTH-5MIN-MICRO-DRILL-v0.1.md` (T4/T5 · demo ≠ BN)  
- NATMED-ALERT 5′: `../worksheets/NATMED-ALERT-5MIN-MICRO-DRILL-v0.1.md` (T2 · map)  
- EQ-M0M3 5′: `../worksheets/EQ-M0M3-5MIN-MICRO-DRILL-v0.1.md` (T2 · ladder)  
- IMAGEJ×EPI 5′: `../worksheets/IMAGEJ-EPI-5MIN-MICRO-DRILL-v0.1.md` (T2 · QA·window)  
- DEID×MISS 5′: `../worksheets/DEID-MISS-5MIN-MICRO-DRILL-v0.1.md` (T5/T7 · export)  
- VAS×LEAK 5′: `../worksheets/VAS-LEAK-5MIN-MICRO-DRILL-v0.1.md` (T4 · SA-02)  
- PUSH×ALERT 5′: `../worksheets/PUSH-ALERT-5MIN-MICRO-DRILL-v0.1.md` (T6 · SA-05)  
- CLIN×BN 5′: `../worksheets/CLIN-BN-5MIN-MICRO-DRILL-v0.1.md` (T7 · dọc)  
- EQ02-M0M3 5′: `../worksheets/EQ02-M0M3-5MIN-MICRO-DRILL-v0.1.md` (T4 · SA-02 ladder)  
- EQ05-M0M3 5′: `../worksheets/EQ05-M0M3-5MIN-MICRO-DRILL-v0.1.md` (T6 · SA-05 ladder)  
- PB007×EQ 5′: `../worksheets/PB007-EQ-5MIN-MICRO-DRILL-v0.1.md` (T2/T4/T6 · Z rồi X)  
- CROSS×EQ 5′: `../worksheets/CROSS-EQ-5MIN-MICRO-DRILL-v0.1.md` (T4/T6/CN · schema)  
- TRIPOD×EQ 5′: `../worksheets/TRIPOD-EQ-5MIN-MICRO-DRILL-v0.1.md` (T4/T5 · demo ≠ BN)  
- SHIFT×PB007 5′: `../worksheets/SHIFT-PB007-5MIN-MICRO-DRILL-v0.1.md` (mọi thứ · Z rồi X)  
- LEAK×CROSS 5′: `../worksheets/LEAK-CROSS-5MIN-MICRO-DRILL-v0.1.md` (T4/T6/CN · không gộp Y)  
- SAP×EQ 5′: `../worksheets/SAP-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5 · §7 · ladder)  
- L1L2L3×SHIFT 5′: `../worksheets/L1L2L3-SHIFT-5MIN-MICRO-DRILL-v0.1.md` (T3/T6 · gate)  
- ALERT×CROSS 5′: `../worksheets/ALERT-CROSS-5MIN-MICRO-DRILL-v0.1.md` (T2/T4/T6/CN · ≠ Dx)  
- AMENDMENT×EQ 5′: `../worksheets/AMENDMENT-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5 · outline · ladder)  
- SPIRIT×EQ 5′: `../worksheets/SPIRIT-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5 · S1–S3 · ladder)  
- MEDIA×SHIFT 5′: `../worksheets/MEDIA-SHIFT-5MIN-MICRO-DRILL-v0.1.md` (CN · press ≠ DOI)  
- CONSORT×EQ 5′: `../worksheets/CONSORT-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5 · placement · ladder)  
- ICF×EQ 5′: `../worksheets/ICF-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5 · consent · ladder)  
- TT43×EQ 5′: `../worksheets/TT43-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5 · số điều · ladder)
- DEID×EQ 5′: `../worksheets/DEID-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5/T7 · export · ladder Z)
- ISO-SWAB×EQ 5′: `../worksheets/ISO-SWAB-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5 · SKU · ladder Z)
- PEA×EQ 5′: `../worksheets/PEA-EQ-5MIN-MICRO-DRILL-v0.1.md` (T3 · L3 CLOSED · ladder Z)
- PREANALYTIC×EQ 5′: `../worksheets/PREANALYTIC-EQ-5MIN-MICRO-DRILL-v0.1.md` (T3 · R1–R3 · ladder Z)
- PEA-PANEL×EQ 5′: `../worksheets/PEA-PANEL-EQ-5MIN-MICRO-DRILL-v0.1.md` (T3 · hẹp ≤20 · ladder Z)
- INTERIM-G2×EQ 5′: `../worksheets/INTERIM-G2-EQ-5MIN-MICRO-DRILL-v0.1.md` (T3/T5 · mock · ladder Z)
- OMICS-IF×EQ 5′: `../worksheets/OMICS-IF-EQ-5MIN-MICRO-DRILL-v0.1.md` (T3/T5 · skip L3 · ladder Z)
- G2×EQ 5′: `../worksheets/G2-EQ-5MIN-MICRO-DRILL-v0.1.md` (T3/T5 · readiness · ladder Z)
- OMICS-GATES×EQ 5′: `../worksheets/OMICS-GATES-EQ-5MIN-MICRO-DRILL-v0.1.md` (T3/T5 · ma trận · ladder Z)
- PB009×EQ 5′: `../worksheets/PB009-EQ-5MIN-MICRO-DRILL-v0.1.md` (T3/T5 · AI trước omics · ladder Z)
- L1L2L3×EQ 5′: `../worksheets/L1L2L3-EQ-5MIN-MICRO-DRILL-v0.1.md` (T3/T6 · gate · ladder Z)
- AI-STACK×EQ 5′: `../worksheets/AI-STACK-EQ-5MIN-MICRO-DRILL-v0.1.md` (T3/T5/T7 · L1→L2 ladder · early≠Dx)
- CLIN-BN×EQ 5′: `../worksheets/CLIN-BN-EQ-5MIN-MICRO-DRILL-v0.1.md` (T7 · dọc L1 · ladder Z)
- YTESO×EQ 5′: `../worksheets/YTESO-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5/T7/CN · ba trụ · ladder Z)
- PB004×EQ 5′: `../worksheets/PB004-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5/T7 · StudyID→visit · ladder Z)
- BN-VISIT×EQ 5′: `../worksheets/BN-VISIT-EQ-5MIN-MICRO-DRILL-v0.1.md` (T7 · StudyID→visits · ladder Z)
- PB005×EQ 5′: `../worksheets/PB005-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5/CN · biofilm proxy · ladder Z lab)
- PB006×EQ 5′: `../worksheets/PB006-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5/CN · ISO cổng · ladder Z)
- TRANSLATION×EQ 5′: `../worksheets/TRANSLATION-EQ-5MIN-MICRO-DRILL-v0.1.md` (T5/CN · in-vitro→người · ladder Z)
- SYNTH×EQ 5′: `../worksheets/SYNTH-EQ-5MIN-MICRO-DRILL-v0.1.md` (T4/T5 · demo ≠ BN · ladder Z)
- PB008×EQ 5′: `../worksheets/PB008-EQ-5MIN-MICRO-DRILL-v0.1.md` (T7/T2/CN · Hawthorne · ladder Z)
- MEDIA×EQ 5′: `../worksheets/MEDIA-EQ-5MIN-MICRO-DRILL-v0.1.md` (CN · press ≠ DOI · ladder Z)
- HAWTHORNE×EQ 5′: `../worksheets/HAWTHORNE-EQ-5MIN-MICRO-DRILL-v0.1.md` (T2/T7/CN · participation · ladder Z)
- PB001×EQ 5′: `../worksheets/PB001-EQ-5MIN-MICRO-DRILL-v0.1.md` (T2/CN · cờ đầu · ladder Z)
- PB002×EQ 5′: `../worksheets/PB002-EQ-5MIN-MICRO-DRILL-v0.1.md` (T4/CN · SA-02 · ladder Z)
- GLOSSARY×EQ 5′: `../worksheets/GLOSSARY-EQ-5MIN-MICRO-DRILL-v0.1.md` (nghĩa đúng · ladder Z)
- ALERT atlas: `../worksheets/ALERT-CROSS-SA-ATLAS-v0.1.md`  
- ALERT 5′: `../worksheets/ALERT-5MIN-MICRO-DRILL-v0.1.md` (T2/T4/T6)    
- clin_event atlas: `../worksheets/CLIN_EVENT-CROSS-SA-ATLAS-v0.1.md`  
- Precure shift bank: `../worksheets/PRECURE-SHIFT-CROSS-SA-BANK-v0.1.md`  
- L1→L2→L3 gate: `../worksheets/L1L2L3-DAILY-GATE-CARD-v0.1.md`  
- Daily stack: `../worksheets/DAILY-STACK-AFTER-STREAK3-v0.1.md`  
- EPI SA-01: `../worksheets/EPI-SA01-EARLY-WINDOW-v0.1.md` (T2)  
- VAS SA-02: `../worksheets/VAS-SCALE-HARMONIZE-SA02-v0.1.md` (T4)  
- PUSH SA-05: `../worksheets/PUSH-SA05-COMPONENTS-v0.1.md` (T6)  
- TRIPOD 5′: `../worksheets/TRIPOD-5MIN-MICRO-DRILL-v0.1.md` (T5)  
- PEA 5′: `../worksheets/PEA-5MIN-MICRO-DRILL-v0.1.md` (T3)  
- clin_event 5′: `../worksheets/CLIN_EVENT-5MIN-MICRO-DRILL-v0.1.md` (T7)  
- Glossary: `../worksheets/EARLY-SIGNAL-GLOSSARY-v0.1.md`  
- PI: `../../PI-NEXT-45MIN.md` · Protocol: `../../rituals/daily-protocol.md`
