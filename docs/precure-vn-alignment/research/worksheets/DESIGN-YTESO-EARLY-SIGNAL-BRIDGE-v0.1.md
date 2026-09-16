# Bridge — Design · y tế số · AI → early-signal SA-01 (Tier 2)

**Mã:** DESIGN-YTESO-EARLY-SIGNAL-BRIDGE-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 15–30 · checkpoint MONTH-1 16/10  
**Thẻ:** `DESIGN-YTESO-AI-RITUAL-CARD` · Study sheet: `STUDY-SHEET-DESIGN-YTESO-AI`  
**Cờ đầu:** SA-01 · G2 **CLOSED** · Primary D21 **không đổi**  
**Không:** bypass TT43 bằng Git · claim Dx từ sandbox · mở biospecimen

## Vì sao Tier 2 thuộc “phát hiện sớm–dọc–AI”

| Trụ Precure logic | Việc Tier 2 | Artifact |
|-------------------|-------------|----------|
| Tín hiệu sớm = exploratory **khai trước** | SPIRIT map ES vào protocol | `SPIRIT-SA01-MAP` S1–S3 · **`SPIRIT-5MIN`** |
| Dữ liệu **dọc** có ID–visit–time–consent | PB-004 entity + REDCap v0.2 | `PB-004` · `y-te-so-precure-bridge` |
| AI trung thực (L1→L2 trước L3) | TRIPOD + pitfalls · PB-009 | `TRIPOD-INTERNAL-CHECKLIST` · `ML-OMICS-PITFALLS` |
| Phê duyệt VN trước omics | TT43 hooks `[CẦN XÁC NHẬN]` | `TT43-AMENDMENT-HOOKS` |

Logic khoa học tuần B (Zhou/Nat Med/PEA/Endpoints) **không thay** — Tier 2 **protocol hóa + hạ tầng số** để không “lạc” khi STREAK tăng.

## Luồng một trang (SA-01)

```text
Zhou/Nat Med / Endpoints / EQ M0–M3
        ↓ khai trong protocol (SPIRIT S1–S3)
DESIGN-SA01 + SAP ES + eCRF v0.2 + clin_event
        ↓ y tế số (PB-004)
StudyID → Visit(t) → Z / ALERT  |  Specimen/X chỉ sau G1+G2+TT43
        ↓ báo cáo AI (TRIPOD)
L2 exploratory AUROC nội bộ ≠ Dx app ≠ press VDHN
```

## Ba cổng trước mọi “early AI / omics”

| Cổng | Câu hỏi | Trả lời mặc định |
|------|---------|------------------|
| **SPIRIT/CONSORT** | ES đã khai + đặt đúng chỗ (≠ primary)? | Nháp Git — amendment `[CẦN XÁC NHẬN]` · **`SPIRIT-5MIN`** · **`CONSORT-5MIN`** |
| **TT43 + HĐĐĐ** | Đổi CRF / nested mẫu đã qua luồng VN? | Hook trống — **PI điền số điều** |
| **G2 / PB-009** | L1+L2 đủ trên \(Z\) trước \(X\)? | G2 **CLOSED** · không order |

## Map trụ → EQ / bridge đã có

| Trụ | Gắn early-signal | Không làm |
|-----|------------------|-----------|
| Protocol | `EQ-SA01` M0–M3 trong SAP ES; CONSORT-ES placement · **`CONSORT-5MIN`** | Báo ES như primary D21 |
| Y tế số | `clin_event` + export de-ID → `verify.sh` | PII trong git / Drive public |
| AI | TRIPOD #7/#9 · pitfall leakage (#1) + synthetic (#5) · **`TRIPOD-5MIN`** | AUROC sandbox = evidence BN |

Bridges trước: `EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01` · `MULTI-OMICS-PEA-SA01-BRIDGE` · `ENDPOINTS-CROSS-SA-BRIDGE`.

## Ritual fill-in (Ngày 15 / 19 / 20 / 21 — mẫu)

```text
Ngày: 15|19|20|21
Trụ: SPIRIT | TT43 | TRIPOD | PB-004
1 câu vì sao ES vẫn exploratory:
1 câu Tier 0 blocker còn mở (DM/cờ/TT43 số điều):
G2: CLOSED
```

## Tier 0 trước pass Ngày 30

`PI-ACTIONS-NOW` — DM SA-01 v0.2 · cờ SA-01 · TT43 số điều · STREAK **DONE thật** tại checkpoint.

## Cấm

- “Đã có DESIGN-YTESO card = đã pass tháng 1”  
- Bịa số điều TT43  
- Đóng Cursor Goal sau checkpoint Tháng 1  

## Liên kết

- Thẻ: `DESIGN-YTESO-AI-RITUAL-CARD-v0.1.md` · Handoff: `TIER-2-30DAY-HANDOFF.md`  
- Checkpoint: `checkpoints/MONTH-1-2026-10-16.md`  
- Nested: `SPIRIT-NESTED-G1-CHECKLIST` · Drill: `SPIRIT-5MIN` · `CONSORT-5MIN` · `TT43-5MIN` · `PB004-5MIN` · Media: `MEDIA-SMART-A-CLAIMS`  
- **TRIPOD 5′:** `TRIPOD-5MIN-MICRO-DRILL-v0.1.md` (T5) · De-ID: `DEID-5MIN-MICRO-DRILL`
