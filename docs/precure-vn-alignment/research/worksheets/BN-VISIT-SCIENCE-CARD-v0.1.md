# BN-VISIT — thẻ khoa học 1 trang (map StudyID→visit→Z · dọc · y tế số)

**Mã:** BN-VISIT-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `BN-VISIT-MAP-TEMPLATE` · PB-004 · CLIN_EVENT · DEID  
**Dùng khi:** T7 · Q3 #9 · sau CLIN_EVENT · rehearsal L1 dọc / y tế số  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · PHI ngoài git/Drive · synthetic ≠ BN · L3/omics CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **map visit dọc** Precure/Smart A: StudyID → visits → \(Z\)/`clin_event` — luyện y tế số L1 trước mọi AI/omics. Không họ tên/SĐT/MRN · omics mặc định CLOSED.

**Mở song song:** thẻ này · `BN-VISIT-MAP-TEMPLATE` · `CLIN_EVENT-SCIENCE-CARD` · **`CLIN-BN-SCIENCE-CARD`** · `DEID-SCIENCE-CARD` · `YTESO-EARLY-SIGNAL-SCIENCE-CARD`

## Ba SA → khung visit (giữ / bỏ)

| SA | Visits lõi | \(Z\) / event sớm | Giữ | Bỏ |
|----|------------|-------------------|-----|-----|
| **01** | D0–D7 · D21=\(Y\) | PCT/CFU/VAS/`clin_event` | StudyID + timestamp | MRN · omics trên map giấy |
| **02** | D0–D3 | VAS/CFU/adhere | Series sớm ≠ \(Y\) | VAS_D3 làm “early” feature |
| **05** | D0–D7 · D14=\(Y\) | PUSH/CFU/TURN | Cadence dọc ICU | Auto-treat vì đã map visit |

## Phương trình L1 map

```text
StudyID + Visit(t) + timestamp + Z/event  =  L1 đủ rehearsal
PHI: KHÔNG vào git / Drive public / log
Omics/specimen trên map: CLOSED  (chỉ sau G2)
SYN map ≠ kết quả lâm sàng BN
```

## Checklist 15′ (1 SA)

```text
Thứ: T7 · SA: 01|02|05 — chọn: ________
StudyID: SA-__-SYN-___ | SA-__-___ (nếu N de-ID)
Visits có: D0|D3|D7|D14|D21(Y) — tick: ________
1 Z chính ≤ cửa sổ sớm: ________ · clin_event: ________
PHI trong map? KHÔNG — vì: ________
Omics trên map? KHÔNG | CLOSED — vì: ________
1 việc ≤30′ (BN-VISIT-5MIN / CLIN_EVENT / DEID / PB004): ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / BN-VISIT map | StudyID→visit→Z |
| `CLIN_EVENT-SCIENCE-CARD` | Schema event cùng cửa sổ |
| `DEID-SCIENCE-CARD` | Deny PHI trước export |
| `AI-STACK-SCIENCE-CARD` | L1 map trước L2 M0–M3 |
| `YTESO-EARLY-SIGNAL-SCIENCE-CARD` | Y tế số sớm–dọc–AI |

## Cấm

- Paste MRN/DOB/ảnh nhận diện vào log/git  
- Coi SYN map = lâm sàng · order PEA vì “map đủ visit”  
- Agent tick DONE · đóng Goal  

## Liên kết

**`CLIN-BN-SCIENCE-CARD`** · `BN-VISIT-MAP-TEMPLATE` · `BN-VISIT-5MIN` · `BN-VISIT-EQ-5MIN` · `CLIN-BN-5MIN` · `CLIN_EVENT-SCIENCE-CARD` · `DEID-SCIENCE-CARD` · **`PB004-SCIENCE-CARD`** · `PB004-5MIN` · `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · `AI-STACK-SCIENCE-CARD` · **`BN-VISIT-EQ-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3`
