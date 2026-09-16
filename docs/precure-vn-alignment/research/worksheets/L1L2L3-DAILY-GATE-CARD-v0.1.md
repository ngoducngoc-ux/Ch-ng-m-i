# Card — L1→L2→L3 daily gate (PB-009 · anti-forget)

**Mã:** L1L2L3-DAILY-GATE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** sau STREAK≥3 · T3 (bridge #1) · drill B · bất kỳ ngày muốn nói “AI / omics”  
**Goal:** ACTIVE · L3 **CLOSED** mặc định · sandbox ≠ N thật · PREP ≠ DONE

## Một câu

> Mỗi ngày **xác nhận cổng**: L1 dọc → L2 exploratory → L3 omics chỉ sau G2 — không đảo thứ tự vì đã ôn atlas/EQ.

## Gate nhanh (30″ đọc)

| Tầng | Đủ khi | Hôm nay (khoanh) | Artifact |
|------|--------|------------------|----------|
| **L1** | ID–visit–time–event–\(Z\) (không PHI public) | CHƯA · SYN · N thật | `CLIN_EVENT-CROSS-SA-ATLAS` · `BN-VISIT-MAP` · PB-004 |
| **L2** | M0–M3 pre-spec + de-ID QC; metrics trên **N thật** mới = L2.4 | SYN only · CHƯA · N thật | `REDCAP-DEID` · EQ · `LEAKAGE-CROSS-SA-ATLAS` · TRIPOD |
| **L3** | G2 pass + ethics G1 + câu hỏi \(X\) thêm giá trị | **CLOSED** · (hiếm) OPEN | `G2-READINESS` · PEA card · `PB-009` |

**Quy tắc cứng:** SYN / PREP / verify PASS → vẫn **L3 CLOSED**. ALERT nội bộ ≠ lý do mở L3.

## Drill 5′ (điền)

**Bản first-class:** `L1L2L3-5MIN-MICRO-DRILL` (dùng thay khối dưới khi stack/timer gọi 5′).

```text
SA neo: 01|02|05
L1 hôm nay: CHƯA | SYN | N thật — thiếu gì: ________
L2 hôm nay: CHƯA | SYN QC | N thật — leakage check? CÓ|CHƯA
L3: CLOSED vì ________ (G2 / chưa N / ethics / …)
1 rủi ro nếu đảo L3 trước L1/L2:
1 câu PB-009 (AI dọc không cần omics hôm nay):
```

## Gắn thứ trong tuần

| Thứ | Gate nhấn | File cặp |
|-----|-----------|----------|
| **T2** | L1 event + ALERT A | EQ-SA01 · clin_event atlas |
| **T3** | **L1→L2 trước L3** (ngày PEA) | bridge #1 · card này · **`L1L2L3-5MIN`** · PEA card |
| **T4** | L2 leakage | EQ-SA02 · leakage atlas |
| **T6** | L3 ICU CLOSED | EQ-SA05 · ALERT B |
| **CN** | PB-009 lens | PB lens #13 · card này |

## Cấm

- Tick L2.4 vì `verify.sh` PASS trên synthetic  
- Order PEA / mở G2 vì đã điền đủ ô gate  
- Coi card PREP = STREAK DONE  

## Liên kết

- **Thẻ khoa học:** **`L1L2L3-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`
- Checklist đầy đủ: `PB-009-AI-BEFORE-OMICS-v0.1.md`  
- Stack: `../guides/AI-LONGITUDINAL-STACK-v0.1.md` · `MULTI-OMICS-GATES-SMART-A-v0.1.md`  
- PEA: `PEA-L1L2L3-DECISION-CARD-v0.1.md` · **`PEA-5MIN-MICRO-DRILL`** · `G2-READINESS`  
- De-ID: `REDCAP-DEID-EXPORT-CHECKLIST-v0.1.md`  
- Atlas trio · `PRECURE-SHIFT-CROSS-SA-BANK` · drill: `STUDY-SHEET-MULTI-OMICS-ES-DRILL`

- **5′ sibling:** `L1L2L3-5MIN-MICRO-DRILL` · `PB009-5MIN-MICRO-DRILL` (AI trước omics) · `G2-5MIN-MICRO-DRILL`
