# PB004 — thẻ khoa học 1 trang (StudyID–Visit–Obs · nền y tế số dọc) · refresh v0.1b

**Mã:** PB004-SCIENCE-CARD-v0.1b · **Ngày:** 2026-09-16  
**Goal:** ACTIVE · STREAK thật vẫn **2 DONE** · EQ bank **CLOSED** · densify ≠ DONE  
**STREAK&lt;3?** Path STREAK3 trước · **`STREAK3-PACK`** · **`STREAK3-EQ`** · NatMed → tick **19/09** · dừng OPENER/stack  
**STREAK≥3?** **`AFTER-STREAK3-OPENER`** → 1×EQ sibling → **`DAILY-STACK`** · bridges #0–14  
**Không:** agent tick DONE · UpdateGoal complete trên PREP/densify · invent EQ · densify = DONE · PII vào git  
**Neo:** MEDIA (refresh v0.1b) · `PB-004-data-architecture` · `PB-004-DIAGRAM` · DEID · BN-VISIT  
**Dùng khi:** T5/T7 · bridge #3/#9 · Ngày 21 · STREAK3 · trước claim “đã sẵn sàng omics/AI trên data”  
**Hub:** `MEDIA-SCIENCE-CARD` (refresh v0.1b) · tip tiếp `BN-VISIT-SCIENCE-CARD` · Drive keep `1Vjchf1i…`  
**Căn cứ:** TT 43/2024/TT-BYT · ICH E6(R3) · L3/G2 CLOSED  

```text
STREAK <3? → STREAK3 (PI-NEXT) · densify ≠ DONE
        ↓ STREAK ≥3
OPENER → EQ sibling → DAILY-STACK · ritual theo Ngày N
```

## Mục đích

Ôn **kiến trúc tối thiểu** y tế số Precure/Smart A: Participant → StudyID → Visit → ClinicalObs/Media/(Specimen) — **consent + de-ID** trước omics. Sơ đồ Git / densify ≠ REDCap đã triển khai tại site.

**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · HAWTHORNE · MEDIA · FILL-AID → tick **19/09** trước  

**Mở song song:** thẻ này · `PB-004-data-architecture` · tip **`BN-VISIT-SCIENCE-CARD`** · **`MEDIA-SCIENCE-CARD`** (refresh v0.1b) · `PB-004-DIAGRAM` · `DEID-SCIENCE-CARD` · `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · **`ICF-NEST-SCIENCE-CARD`**

## Entity tối thiểu → giữ / bỏ

| Entity | Vai trò | Giữ hôm nay | Bỏ |
|--------|---------|-------------|-----|
| **StudyID** | Khóa nghiên cứu (SA-xx-NNN) | Đủ thay MRN trong analysis | Map ngược công khai |
| **Visit** | D0…\(t^*\) + timestamp | Chuỗi dọc audit | Snapshot baseline = “dọc” |
| **ClinicalObs** | \(Z\) / `clin_event` | L1 ES | PHI trong Obs |
| **Media** | ImageJ / ảnh vết thương | De-ID · QA | Ảnh nhận diện |
| **Specimen** | Swab / máu / PEA | **CLOSED** đến G2+consent | Order vì đã vẽ sơ đồ |
| **Agent densify** | Anti-forget | Hub wire | = site live / omics ready |

## Phương trình nền

```text
PB-004:  StudyID → Visit(t) → Obs/Media/(Specimen)
Consent nested + de-ID  trước  omics/AI claim
Git diagram / densify ≠ site live   ·   PII ∉ git/Drive public
Ôn PB004 / densify  ≠  REDCap live  ≠  DONE
```

## Checklist 15′

```text
Thứ: T5|T7|STREAK3 · Entity hôm nay: StudyID|Visit|Obs|Media|Specimen — chọn: ________
Đã mở PB004 + MEDIA + BN-VISIT thẻ? ________
Consent lưu mẫu / tái phân tích? CHƯA | NHÁP ICF | CÓ — version: ________
PII trong repo/Drive public? KHÔNG — vì: ________
Export analysis = StudyID+visit+Z de-ID? CÓ | CHƯA
Specimen/omics hôm nay? CLOSED — vì: ________
Densify = REDCap live? KHÔNG
1 việc ≤30′ (PB-004 diagram tick / DEID / BN-VISIT / TT43): ________
Đóng Goal / order Specimen vì sơ đồ? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / PB-004 | Kiến trúc ID–time–obs |
| tip **`BN-VISIT-SCIENCE-CARD`** | Map 1 chuỗi visit trên StudyID · densify tiếp |
| `DEID-SCIENCE-CARD` | Deny/allow export |
| `AI-STACK-SCIENCE-CARD` | L1 kiến trúc → L2 M0–M3 |
| `YTESO-EARLY-SIGNAL-SCIENCE-CARD` | Y tế số sớm–dọc–AI |
| **`MEDIA-SCIENCE-CARD`** (refresh v0.1b) | Hub trước · VDHN≠DOI |
| `ICF-NEST` (refresh v0.1b) | Consent tách |

## Cấm

- Order Specimen khi consent nested chưa duyệt  
- PII vào git / memory / Drive public  
- Coi mermaid / densify = REDCap live · đóng Goal / invent EQ · densify = DONE  

## Liên kết

`PB-004-data-architecture` · tip tiếp **`BN-VISIT-SCIENCE-CARD`** · **`MEDIA-SCIENCE-CARD`** (refresh v0.1b) · `PB-004-DIAGRAM` · `PB004-5MIN` · `PB004-EQ-5MIN` · `DEID-SCIENCE-CARD` · `BN-VISIT-SCIENCE-CARD` · `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · `AI-STACK-SCIENCE-CARD` · `TT43-5MIN` · **`ICF-NEST-SCIENCE-CARD`** · **`SPIRIT-G1-SCIENCE-CARD`** · **`TT43-SCIENCE-CARD`** · **`PB004-EQ-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · **`PB009-SCIENCE-CARD`** · `DAILY-STACK-AFTER-STREAK3` · `STREAK3-PACK-SCIENCE-CARD` · Drive keep `1Vjchf1i…` · PREP≠DONE · densify≠DONE  
