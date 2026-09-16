# Bank — Precure shift (sớm–dọc–AI) × SA-01 / 02 / 05 / y tế số

**Mã:** PRECURE-SHIFT-CROSS-SA-BANK-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** drill C · daily-protocol bước 3 · PB lens #13 · EQ “1 câu Precure shift”  
**Goal:** ACTIVE · 1 câu / ngày · không overclaim · PREP ≠ DONE

## Một câu

> Mỗi ngày viết **đúng 1 câu lệch hướng** Smart A theo ba trụ — đủ để chứng tỏ đã ôn, không đủ để claim Dx / đóng Goal.

## Bank mẫu (chọn 1 · rồi tự viết lại bằng lời mình)

| Neo | Trụ chính | Câu mẫu (đúng hướng) | Cấm song song |
|-----|-----------|----------------------|---------------|
| **SA-01** | Sớm | Chuỗi \(Z\) D0–D7 + `clin_event` có thể cải thiện dự báo \(Y_{D21}\) vs chỉ D0 — exploratory. | “Đã phát hiện lành sớm như Precure press.” |
| **SA-01** | Dọc | Event 0–4 trên eCRF là analog Zhou trước mọi \(X\) PEA. | Order PEA vì đã có `clin_event`. |
| **SA-01** | AI | M0–M3 trên de-ID trước L3; ALERT A1–A4 nội bộ ≠ model claim. | AUROC sandbox = bằng chứng BN. |
| **SA-02** | Sớm | Tín hiệu D1/CFU dẫn trước \(\Delta\)VAS — không dùng VAS_D3 làm “early” khi trùng \(Y\). | Gộp Y với SA-01/05. |
| **SA-02** | Dọc | Timestamp triệu chứng / adherence = L1 event schema riêng. | Coi M1 leakage sandbox là science. |
| **SA-02** | AI | L2 support SA-02; ALERT C nội bộ; primary VAS D3 không đổi. | App TMH tự chỉ định. |
| **SA-05** | Sớm | PUSH (± component) ≤D7 exploratory trước \(Y\) D14 — không auto-treat ICU. | Component = thay primary. |
| **SA-05** | Dọc | TURN_ADHERE / AE ICU = cadence dọc; BN map de-ID không PHI. | Omics ICU vì đã có PUSH series. |
| **SA-05** | AI | L2 support; ALERT B; L3 CLOSED đến G2 N thật. | Deploy alert ra app ICU. |
| **Y tế số** | Dọc+AI | StudyID–visit–time–event–\(Z\) (PB-004) là nền trước mọi model. | Đưa PHI vào git/Drive public. |
| **Press** | Ranh giới | VDHN = tầm nhìn; DOI Nat Med = actionable **trong cohort** — Smart A = ALERT nội bộ. | Equate partnership press = evidence RCT. |

Nguồn ranh giới: `MEDIA-SMART-A-CLAIMS` · atlas `ALERT`/`LEAKAGE`/`CLIN_EVENT`.

## Drill 5′ (điền — bắt buộc đổi lời)

**Bản first-class:** `SHIFT-5MIN-MICRO-DRILL` (dùng thay khối dưới khi stack/timer gọi 5′).

```text
Neo hôm nay: SA-01|02|05|Y tế số|Press
Trụ: Sớm | Dọc | AI
1 câu lệch hướng (tự viết, ≤25 từ):
1 câu CẤM hôm nay (overclaim):
Atlas/EQ đã đụng: ________
```

## Gắn ritual

| Slot | Cách dùng bank |
|------|----------------|
| daily-protocol §3 | Thay / bổ sung “1 câu lệch hướng Precure” |
| drill C | Chọn **PB** hoặc dùng bank thay EQ cross-SA |
| PB lens #13 | Điền “1 câu lệch hướng” từ hàng PB ↔ bank |
| EQ Drill 10′ | Ô “1 câu Precure shift” — đối chiếu hàng SA |

## Cấm

- Copy nguyên câu mẫu vào log rồi coi DONE mà không tự viết lại  
- Dùng bank để đóng Goal / mở G2  
- Một câu “Smart A đã lệch hướng xong” cho cả năm  

## Liên kết

- **Thẻ khoa học:** **`SHIFT-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX`

- `alignment-map-smart-a.md` · `problem-bank.md` · `PB-EARLY-SIGNAL-LENS-BRIDGE` (#13)  
- EQ: `../equations/EQ-SA01|02|05-early-warning-v0.1.md` · **`EQ-5MIN-MICRO-DRILL`** (T2/T4/T6) · **`SHIFT-5MIN-MICRO-DRILL`** (mọi thứ)  
- `MEDIA-SMART-A-CLAIMS-v0.1.md` · atlas trio  
- Drill: `../study-sheets/STUDY-SHEET-MULTI-OMICS-ES-DRILL-v0.1.md`  
- Protocol: `../../rituals/daily-protocol.md`

- **Thẻ khoa học Press:** `SHIFT-PRESS-SCIENCE-CARD`
