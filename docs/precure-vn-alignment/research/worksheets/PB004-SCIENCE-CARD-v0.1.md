# PB004 — thẻ khoa học 1 trang (StudyID–Visit–Obs · nền y tế số dọc)

**Mã:** PB004-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `PB-004-data-architecture` · `PB-004-DIAGRAM` · DEID · BN-VISIT  
**Dùng khi:** T5/T7 · bridge #3/#9 · Ngày 21 · trước claim “đã sẵn sàng omics/AI trên data”  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · L3/G2 CLOSED · PII không vào git/Drive public · sơ đồ ≠ hệ live · PREP ≠ DONE  

## Mục đích

Ôn **kiến trúc tối thiểu** y tế số Precure/Smart A: Participant → StudyID → Visit → ClinicalObs/Media/(Specimen) — **consent + de-ID** trước omics. Sơ đồ Git ≠ REDCap đã triển khai tại site.

**Mở song song:** thẻ này · `PB-004-data-architecture` · `PB-004-DIAGRAM` · `DEID-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD` · `YTESO-EARLY-SIGNAL-SCIENCE-CARD`

## Entity tối thiểu → giữ / bỏ

| Entity | Vai trò | Giữ hôm nay | Bỏ |
|--------|---------|-------------|-----|
| **StudyID** | Khóa nghiên cứu (SA-xx-NNN) | Đủ thay MRN trong analysis | Map ngược công khai |
| **Visit** | D0…\(t^*\) + timestamp | Chuỗi dọc audit | Snapshot baseline = “dọc” |
| **ClinicalObs** | \(Z\) / `clin_event` | L1 ES | PHI trong Obs |
| **Media** | ImageJ / ảnh vết thương | De-ID · QA | Ảnh nhận diện |
| **Specimen** | Swab / máu / PEA | **CLOSED** đến G2+consent | Order vì đã vẽ sơ đồ |

## Phương trình nền

```text
PB-004:  StudyID → Visit(t) → Obs/Media/(Specimen)
Consent nested + de-ID  trước  omics/AI claim
Git diagram ≠ site live   ·   PII ∉ git/Drive public
```

## Checklist 15′

```text
Thứ: T5|T7 · Entity hôm nay: StudyID|Visit|Obs|Media|Specimen — chọn: ________
Consent lưu mẫu / tái phân tích? CHƯA | NHÁP ICF | CÓ — version: ________
PII trong repo/Drive public? KHÔNG — vì: ________
Export analysis = StudyID+visit+Z de-ID? CÓ | CHƯA
Specimen/omics hôm nay? CLOSED — vì: ________
1 việc ≤30′ (PB-004 diagram tick / DEID / BN-VISIT / TT43): ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / PB-004 | Kiến trúc ID–time–obs |
| `BN-VISIT-SCIENCE-CARD` | Map 1 chuỗi visit trên StudyID |
| `DEID-SCIENCE-CARD` | Deny/allow export |
| `AI-STACK-SCIENCE-CARD` | L1 kiến trúc → L2 M0–M3 |
| `YTESO-EARLY-SIGNAL-SCIENCE-CARD` | Y tế số sớm–dọc–AI |

## Cấm

- Order Specimen khi consent nested chưa duyệt  
- PII vào git / memory / Drive public  
- Coi mermaid = REDCap live · đóng Goal  

## Liên kết

`PB-004-data-architecture` · `PB-004-DIAGRAM` · `PB004-5MIN` · `PB004-EQ-5MIN` · `DEID-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD` · `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · `AI-STACK-SCIENCE-CARD` · `TT43-5MIN` · **`ICF-NEST-SCIENCE-CARD`** · **`SPIRIT-G1-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3`
