# ISO-SWAB — thẻ khoa học 1 trang (G5 · irritation/cytotox · trước L3)

**Mã:** ISO-SWAB-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `ISO-SWAB-CONTACT-PRIORITY` · PB-006 · G2 · OMICS-GATES · PREANALYTIC · SPIRIT-G1  
**Dùng khi:** T5 · Ngày 14 / 48 · sau PB006 · trước nested biospecimen / claim “ISO pass”  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + **`MEDIA-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · SA-04 = **cổng** · G5 SPEC-BIO · L3/G2 CLOSED · PREP ≠ DONE · không order swab vì nháp  
**Căn cứ:** ISO 10993-1:2018 · PI điền duration/SKU từ SOP thật  

## Mục đích

Ôn **cổng ISO swab** Precure/Smart A: irritation + cytotoxicity trên **SKU swab thật** trước mọi nested omics (G5). AI/REDCap **không** thay báo cáo ISO; không mở form omics trước G2; checklist nháp ≠ ISO pass.

**Mở song song:** thẻ này · `ISO-SWAB-CONTACT-PRIORITY` · `OMICS-GATES-SCIENCE-CARD` · `G2-SCIENCE-CARD` · `SPIRIT-G1-SCIENCE-CARD`

## Contact → giữ / bỏ

| Hạng mục | Vai trò | Giữ hôm nay | Bỏ |
|----------|---------|-------------|-----|
| **Intended contact** | Surface swab/exudate | Ghi loại + SOP | Coi implant mặc định |
| **Duration** | Limited / prolonged | `[CẦN XÁC NHẬN]` nếu chưa | Claim đã classify vì drill |
| **Ưu tiên hôm nay** | Irritation + cytotox | SKU đúng dự kiến | Sensitization trước khi chưa có SKU |
| **AI / REDCap** | Early warning tool | Không = ISO pass | Thay báo cáo lab |
| **Omics form** | Nested L3 | Chỉ sau G1∧G2+ICF | Mở form vì đã ôn ISO |
| **Order swab/PEA** | Logistics | KHÔNG từ PREP | Order vì checklist nháp |

## Phương trình ISO-SWAB

```text
SKU thật + irritation/cytotox pass  ≥  trước  nested omics (G5)
AI/REDCap  ≠  ISO pass
Checklist nháp  ≠  báo cáo lab
G2 CLOSED  →  không mở form omics
```

## Checklist 15′

```text
Thứ: T5 · Contact: surface swab/exudate|implant — ________
Duration: limited|prolonged|[CẦN XÁC NHẬN] — ________
Ưu tiên: irritation+cytotox|sensitization|khác — ________
SKU swab định? CHƯA[CẦN XÁC NHẬN]|CÓ — ________
AI/REDCap = ISO pass? KHÔNG — vì: ________
Mở form omics trước G2? KHÔNG
Order swab/PEA vì drill? KHÔNG
1 việc ≤30′ (ISO-SWAB / PB006 / EH-SA04 / PREANALYTIC): ________
Đóng Goal / mở L3 vì ISO-SWAB? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / ISO-SWAB priority | G5 contact · irritation/cytotox |
| `OMICS-GATES-SCIENCE-CARD` | Ma trận cổng × SA |
| `G2-SCIENCE-CARD` | Omics gate CLOSED |
| `SPIRIT-G1-SCIENCE-CARD` | Nested ethics trước mẫu |
| `PB006-5MIN` | Cổng SA-04 rộng |
| `PREANALYTIC-5MIN` | Pre-analytic trước PEA |

## Cấm

- Coi checklist nháp = ISO pass trên SKU  
- Dùng AI/REDCap thay báo cáo irritation/cytotox  
- Mở form omics / order swab / đóng Goal vì đã drill  

## Liên kết

`ISO-SWAB-CONTACT-PRIORITY` · `ISO-SWAB-5MIN` · `ISO-SWAB-EQ-5MIN` · `OMICS-GATES-SCIENCE-CARD` · `G2-SCIENCE-CARD` · `SPIRIT-G1-SCIENCE-CARD` · `PB006-5MIN` · `PREANALYTIC-5MIN` · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3` · **`PREANALYTIC-SCIENCE-CARD`** · **`OMICS-IF-SCIENCE-CARD`**
