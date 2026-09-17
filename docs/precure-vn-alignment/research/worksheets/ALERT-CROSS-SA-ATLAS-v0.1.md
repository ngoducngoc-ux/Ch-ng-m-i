# Atlas — ALERT × early-signal (SA-01 / 02 / 05) · refresh v0.1b

**Mã:** ALERT-CROSS-SA-ATLAS-v0.1b · **Ngày:** 2026-09-16  
**Goal:** ACTIVE · STREAK thật vẫn **2 DONE** · EQ bank **CLOSED** · densify ≠ DONE  
**STREAK&lt;3?** Path STREAK3 trước · **`STREAK3-PACK`** · **`STREAK3-EQ`** · NatMed → tick **19/09** · dừng OPENER/stack  
**STREAK≥3?** **`AFTER-STREAK3-OPENER`** → 1×EQ sibling → **`DAILY-STACK`** · bridges #0–14  
**Không:** agent tick DONE · UpdateGoal complete trên PREP/densify · invent EQ · Dx / auto-treat · mở G2 vì ALERT  
**Dùng khi:** EQ rotation T2/T4/T6 · drill C (ALERT) · Nat Med Ngày 03 · weekly y tế số  
**Hub:** `LEAKAGE` (refresh v0.1b) · tip tiếp `CLIN_EVENT` (`CLIN_EVENT-CROSS-SA-ATLAS`) · Drive keep `1Vjchf1i…`  

```text
STREAK <3? → STREAK3 (PI-NEXT) · densify ≠ DONE
        ↓ STREAK ≥3
OPENER → EQ sibling → DAILY-STACK · ritual theo Ngày N
```

## Một câu

> Cùng logic Nat Med “clinically actionable” — nhưng **mỗi SA một bộ ALERT**; actionable ≠ đổi primary, ≠ app BN, ≠ mở G2.

## Ma trận ALERT (ôn nhanh)

| SA | Bộ | Neo \(Z\) / sự kiện | Hành động kiểu | Cấm tuyệt đối |
|----|-----|---------------------|----------------|---------------|
| **01** | **A1–A4** | PCT/CFU/VAS/`clin_event` D0–D7 | Hội chẩn PI · AE · QA ImageJ · ghi confounder | Đổi nhánh RCT · AI tự chỉ định · gán omics |
| **02** | **C1–C3** | VAS / CFU / ADHERE_SPRAY | AE review · exploratory signal · nhắc adherence | Đổi nhánh · KS ngoài protocol · gộp Y với SA-01/05 |
| **05** | **B1–B3** | PUSH / CFU / TURN_ADHERE | Review xoay trở · exploratory · confounder SAP | Auto-treat ICU · app Dx · order omics vì alert |

Ngưỡng số = **nháp** → `[CẦN XÁC NHẬN]` pilot. Chi tiết: `ALERT-SA01|02|05`. densify ≠ DONE.

## Map từ Nat Med (1 hàng / lần ôn)

| Nat Med (ý) | Giữ cho Smart A | Gắn ALERT |
|-------------|-----------------|-----------|
| Tiền lâm sàng → hành động trong cohort | Tín hiệu trên \(Z(t')\) trước \(t^*\) | A1 / C2 / B2 (CFU + trajectory) |
| Insight có **hành động** rõ | ALERT có cột “làm / không làm” | A2 / C1 / B1 |
| Profiling lặp → bias tham gia | PB-008 adherence | C3 / B3 · không gán “điều trị hiệu quả” |
| Chuyển trạng thái / sự kiện | `clin_event` / AE | A3–A4 · SA-02/05 ghi event trong log |

Nguồn map đầy đủ SA-01: `NATMED-ACTIONABLE-ALERT-MAP`. Atlas này = **mở rộng cross-SA** sau STREAK≥3 (STREAK&lt;3: STREAK3 path trước).

## Drill 8′ (điền — 1 SA theo EQ rotation)

```text
Thứ: T2|T4|T6 · SA: 01|02|05 · ALERT ID: A__|C__|B__
Điều kiện (Z / event): ________
Hành động nội bộ: ________
1 việc KHÔNG làm: ________
1 câu actionable ≠ Dx / ≠ đổi primary:
Gắn trụ: Sớm | Dọc | AI (khoanh 1)
```

## Gắn y tế số (ops)

| Trụ | Câu kiểm ALERT |
|-----|----------------|
| **Sớm** | Điều kiện dùng \(Z(t')\) trước \(t^*\)? |
| **Dọc** | Có visit/timestamp đủ để audit? |
| **AI** | ALERT có trong eCRF/SOP nội bộ — **không** trong model claim? |

## Cấm

- Coi atlas PREP = STREAK DONE  
- Deploy ALERT ra BN / app ngoài protocol  
- Dùng ALERT làm lý do mở G2 / order PEA  
- UpdateGoal complete trên densify · invent EQ  

## Liên kết

- **Thẻ:** **`ALERT-SCIENCE-CARD`** · **`ALERT-EQ-SCIENCE-CARD`** · **`ALERT-CROSS-SCIENCE-CARD`** · **`NATMED-ALERT-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`  
- `../hypotheses/ALERT-SA01|02|05-v0.1.md` · `NATMED-ACTIONABLE-ALERT-MAP` · `MEDIA-SMART-A-CLAIMS`  
- **Micro-drill 5′:** `ALERT-5MIN` · **`ALERT-EQ-5MIN`** · **`ALERT-CROSS-5MIN`** · **`NATMED-ALERT-5MIN`** (T2/T4/T6)  
- EQ: `../equations/EQ-SA01|02|05-early-warning-v0.1.md`  
- Leakage (đừng nhầm): `LEAKAGE-CROSS-SA-ATLAS` (refresh v0.1b)  
- tip tiếp: `CLIN_EVENT-CROSS-SA-ATLAS` · Drive keep `1Vjchf1i…` · PREP≠DONE · densify≠DONE  
