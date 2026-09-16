# Template map 1 BN / 1 chuỗi visit (de-ID only)

**Mã:** BN-VISIT-MAP-TEMPLATE-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Q3 Ngày 117–119 · Ritual: `Q3-CROSS-SA-YTESO-RITUAL-CARD`  
**Cấm:** họ tên · SĐT · địa chỉ · MRN · DOB đầy đủ · ảnh nhận diện · ghi chú có PII

## Mục tiêu

1 trang map **StudyID → visits → Z/`clin_event`** khớp PB-004 — luyện y tế số dọc **không** đưa PHI vào git/Drive public.

## A. Định danh nghiên cứu (chỉ lớp Analysis)

| Trường | Giá trị (điền) |
|--------|----------------|
| StudyID | `SA-01-___` (không map ngược ngoài site) |
| SA / arm | SA-01 · group `[ ]` |
| Site code | `[site_code]` — không tên viện nếu nhạy |

## B. Chuỗi visit (tick có/không)

| Visit | Có? | Z chính (PCT/CFU/VAS…) | clin_event 0–4 | Missing? |
|-------|-----|------------------------|----------------|----------|
| D0 | [ ] | | | |
| D3 (hoặc D1–D3) | [ ] | | | |
| D7 | [ ] | | | |
| D14 | [ ] | | | |
| D21 \(Y\) | [ ] | primary only | — | |

## C. Ranh giới PB-004

| Lớp | Có trong map này? |
|-----|-------------------|
| Identified (tên, SĐT…) | **Không** |
| StudyID | Có |
| Analysis Z/`clin_event` | Có (scrub note) |
| Specimen / omics | Chỉ nếu G2 pass — mặc định **Không** |

## D. Một câu y tế số (dán log)

```text
StudyID=… · visits có=… · clin_event=… · PHI=không · omics=CLOSED|…
```

## E. Nếu chưa có BN thật

Điền **synthetic StudyID** (`SA-01-SYN-001`) + tick “rehearsal” — không copy số từ sandbox như kết quả lâm sàng.

## Liên kết

`PB-004-DIAGRAM` · `y-te-so-precure-bridge` · `REDCAP-DEID-EXPORT-CHECKLIST` · `CLIN_EVENT-CODING-VIGNETTES`  
Bridge: `Q3-CROSS-SA-YTESO-EARLY-SIGNAL-BRIDGE` · thẻ `Q3-CROSS-SA-YTESO-RITUAL-CARD`
