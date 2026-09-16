# Atlas — ALERT × early-signal (SA-01 / 02 / 05)

**Mã:** ALERT-CROSS-SA-ATLAS-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** EQ rotation T2/T4/T6 · drill C (ALERT) · Nat Med Ngày 03 · weekly y tế số  
**Goal:** ACTIVE · ALERT = **nội bộ nghiên cứu** · không Dx / không auto-treat · PREP ≠ DONE

## Một câu

> Cùng logic Nat Med “clinically actionable” — nhưng **mỗi SA một bộ ALERT**; actionable ≠ đổi primary, ≠ app BN, ≠ mở G2.

## Ma trận ALERT (ôn nhanh)

| SA | Bộ | Neo \(Z\) / sự kiện | Hành động kiểu | Cấm tuyệt đối |
|----|-----|---------------------|----------------|---------------|
| **01** | **A1–A4** | PCT/CFU/VAS/`clin_event` D0–D7 | Hội chẩn PI · AE · QA ImageJ · ghi confounder | Đổi nhánh RCT · AI tự chỉ định · gán omics |
| **02** | **C1–C3** | VAS / CFU / ADHERE_SPRAY | AE review · exploratory signal · nhắc adherence | Đổi nhánh · KS ngoài protocol · gộp Y với SA-01/05 |
| **05** | **B1–B3** | PUSH / CFU / TURN_ADHERE | Review xoay trở · exploratory · confounder SAP | Auto-treat ICU · app Dx · order omics vì alert |

Ngưỡng số = **nháp** → `[CẦN XÁC NHẬN]` pilot. Chi tiết: `ALERT-SA01|02|05`.

## Map từ Nat Med (1 hàng / lần ôn)

| Nat Med (ý) | Giữ cho Smart A | Gắn ALERT |
|-------------|-----------------|-----------|
| Tiền lâm sàng → hành động trong cohort | Tín hiệu trên \(Z(t')\) trước \(t^*\) | A1 / C2 / B2 (CFU + trajectory) |
| Insight có **hành động** rõ | ALERT có cột “làm / không làm” | A2 / C1 / B1 |
| Profiling lặp → bias tham gia | PB-008 adherence | C3 / B3 · không gán “điều trị hiệu quả” |
| Chuyển trạng thái / sự kiện | `clin_event` / AE | A3–A4 · SA-02/05 ghi event trong log |

Nguồn map đầy đủ SA-01: `NATMED-ACTIONABLE-ALERT-MAP`. Atlas này = **mở rộng cross-SA** sau STREAK≥3.

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

## Liên kết

- `../hypotheses/ALERT-SA01|02|05-v0.1.md`  
- `NATMED-ACTIONABLE-ALERT-MAP-v0.1.md` · `MEDIA-SMART-A-CLAIMS`  
- **Micro-drill 5′:** `ALERT-5MIN-MICRO-DRILL-v0.1.md` (T2/T4/T6)  
- EQ: `../equations/EQ-SA01|02|05-early-warning-v0.1.md`  
- Leakage (đừng nhầm): `LEAKAGE-CROSS-SA-ATLAS-v0.1.md`  
- clin_event atlas: `CLIN_EVENT-CROSS-SA-ATLAS-v0.1.md`  
- Drill: `../study-sheets/STUDY-SHEET-MULTI-OMICS-ES-DRILL-v0.1.md`  
- Y tế số: `../y-te-so-precure-bridge-v0.1.md` · PB lens #13
