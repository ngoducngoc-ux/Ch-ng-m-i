# TT43 — thẻ khoa học 1 trang (amendment hooks VN · Git ≠ duyệt)

**Mã:** TT43-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `TT43-AMENDMENT-HOOKS` · AMENDMENT-ES · SPIRIT-G1 · CONSORT · PB004  
**Dùng khi:** T5 · Ngày 19 · bridge #3 · sau SPIRIT/CONSORT · trước claim “đã duyệt đổi CRF/ES”  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + **`MEDIA-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · ES = exploratory · L3/G2 CLOSED · PREP ≠ DONE · agent **không** thay tư vấn pháp lý  
**Căn cứ:** TT 43/2024/TT-BYT · PI điền số điều từ PDF chính thức  

## Mục đích

Ôn **luồng phê duyệt VN** Precure/Smart A: đổi early-signal / `clin_event` / omics trên REDCap = **TT43 + HĐĐĐ**, không chỉ merge Git. Ô số điều còn `[CẦN XÁC NHẬN]` thì chưa “đã duyệt”.

**Mở song song:** thẻ này · `TT43-AMENDMENT-HOOKS` · `AMENDMENT-ES-SCIENCE-CARD` · `SPIRIT-G1-SCIENCE-CARD` · `CONSORT-5MIN`

## Thay đổi → giữ / bỏ

| Thay đổi | Vai trò | Giữ hôm nay | Bỏ |
|----------|---------|-------------|-----|
| **CRF clin_event** | Schema dọc L1 | Hooks + số điều | Merge Git = duyệt |
| **Nested omics** | Specimen path | Chỉ sau G1–G2+ICF | Order vì đã có hooks |
| **Data security** | De-ID / PII | Deny-list | PII vào git/Drive public |
| **AE / safety** | Báo cáo | Theo protocol | Coi ES = primary safety |

## Phương trình TT43

```text
Đổi CRF/ES/omics  →  TT43 hooks + HĐĐĐ  ≥  trước  “đã duyệt”
Merge Git  ≠  phê duyệt VN
[CẦN XÁC NHẬN] số điều  =  chưa CLOSED
```

## Checklist 15′

```text
Thứ: T5 · Thay đổi: CRF clin_event|nested omics|data security|AE — ________
Số điều TT43 trong hooks? CHƯA[CẦN XÁC NHẬN]|CÓ — số: ________
Merge Git = duyệt VN? KHÔNG — vì: ________
Omics/G2 trước amendment+ICF? KHÔNG — vì: ________
1 việc ≤30′ (PI dán số điều / AMENDMENT-ES / SPIRIT-G1): ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / TT43 hooks | Số điều · Git ≠ duyệt |
| `AMENDMENT-ES-SCIENCE-CARD` | Outline ES · không đổi primary |
| `SPIRIT-G1-SCIENCE-CARD` | N1–N5 nested ethics |
| `CONSORT-5MIN` | Placement ES ≠ primary |
| `PB004-SCIENCE-CARD` | Data arch · consent |

## Cấm

- Claim “đã duyệt” khi số điều còn `[CẦN XÁC NHẬN]`  
- Coi merge Git = HĐĐĐ/TT43 pass  
- Order omics / đóng Goal / agent tư vấn pháp lý thay PI  

## Liên kết

`TT43-AMENDMENT-HOOKS` · `TT43-5MIN` · `TT43-EQ-5MIN` · `TT43-AMEND-5MIN` · `AMENDMENT-ES-SCIENCE-CARD` · `SPIRIT-G1-SCIENCE-CARD` · `CONSORT-5MIN` · `PB004-SCIENCE-CARD` · **`CONSORT-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3` · **`SAP-ES-SCIENCE-CARD`**
