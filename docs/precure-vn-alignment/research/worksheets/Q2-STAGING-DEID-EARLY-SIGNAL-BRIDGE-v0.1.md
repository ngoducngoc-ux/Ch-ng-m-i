# Bridge — Q2 staging / de-ID → L2 early-signal (SA-01 cờ) · refresh v0.1b

**Mã:** Q2-STAGING-DEID-EARLY-SIGNAL-BRIDGE-v0.1  
**Ngày:** 2026-09-16 (refresh sau TIER3-INTERIM-G2 / EQ bank CLOSED)  
**Curriculum:** Ngày 61–70 · sau checkpoint 60d · T7 rotation (#5/#9) · bridge **#5**  
**Thẻ:** `Q2-STAGING-DEID-RITUAL-CARD` · `REDCAP-DEID-EXPORT-CHECKLIST` · **`DEID-EQ`** · **`DEID-MISS-EQ`** · **`PB004-EQ`** · **`PB009-EQ`**  
**Cờ đầu:** SA-01 · SA-02/05 support · G2 **CLOSED** · Goal **ACTIVE** · EQ bank **CLOSED**  
**STREAK&lt;3?** Dừng · **`STREAK3-PACK`** · **`STREAK3-EQ`** · NOW · FILL-AID → tick **19/09** trước  
**Không:** PHI rời site · biospecimen · gộp endpoint · PREP = DONE · AUROC sandbox = lâm sàng · invent EQ mới

## Vì sao Q2 thuộc “phát hiện sớm–dọc–AI”

| Việc Q2 | Precure logic | Artifact |
|---------|---------------|----------|
| Deny/allow export | Y tế số: StudyID + visit + \(Z\) không PII | `REDCAP-DEID-EXPORT-CHECKLIST` · PB-004 · **`DEID-EQ`** |
| QC schema (`verify` / `redcap_import_qc`) | L2 pipeline sẵn trước model trên N thật | PIPELINE · `verify.sh` |
| Staging SA-02/05 | Cùng khung \(t'\ll t^*\) — schema only | `#2` ENDPOINTS · EQ-02/05 · **`CROSS-EQ`** |
| DM / consent boundary | L1 đủ trước “AI early” (PB-009) | DM handoff · **`PB009-EQ`** |

Bridges #0–#4 đã khai **khoa học + cổng**; #5 = **đường dữ liệu thật tối thiểu** để L2 exploratory không còn chỉ synthetic — anti-forget y tế số.

## Luồng một trang

```text
STREAK <3? → STREAK3-PACK / STREAK3-EQ · dừng #5
        ↓ STREAK ≥3
OPENER → 1×EQ sibling (DEID-EQ / DEID-MISS-EQ / PB004-EQ) → #5
Site PHI (không rời) 
  → StudyID + visit + Z + clin_event (allow)
  → export de-ID (deny D1–D7)
  → QC schema (verify / redcap_import_qc)
  → M0–M3 exploratory trên N thật (L2)  ← mục tiêu Q2
  → L3 X_mol chỉ sau G2 (CLOSED)
Goal ACTIVE · PREP ≠ DONE
```

## Ba cổng trước mọi “AI early trên data thật”

| Cổng | Câu hỏi | Trả lời mặc định |
|------|---------|------------------|
| **De-ID** | Export có cột deny (PII / ICF / omics raw)? | Phải tick checklist Ngày 61–63 · **`DEID-EQ`** |
| **DM / Tier 0** | SA-01 v0.2 đã forward / review? | `[CẦN XÁC NHẬN]` PI |
| **G2** | Signal \(Z\) / DSMB trên N thật? | **CLOSED** — không order · **`G2-EQ`** |

## SA support (66–70) — không gộp \(Y\)

| SA | Primary \(t^*\) | Việc Q2 | Cấm |
|----|----------------|---------|-----|
| **01** | D21 | Staging export + QC path | Omics raw trong CSV |
| **02** | VAS D3 | Dictionary / EQ ôn · D1 optional | Marker = primary |
| **05** | PUSH D14 | EQ gap / missingness | \(\Delta\)PUSH = Dx ICU |

## Liên hệ bridges trước

| Bridge | Vai trò còn lại ở Q2 |
|--------|----------------------|
| `#0` Zhou/NatMed · `#2` Endpoints | \(Z\)/`clin_event` phải có trong allow list |
| `#1` PEA · `#4` Tier3 Interim/G2 | D7 deny = omics raw; interim ≠ pass G2 |
| `#3` DESIGN-YTESO | TT43/PB-004 khi đổi CRF / export policy |

## Ritual fill-in (61 / 62 / 67 — mẫu)

```text
STREAK ≥3? ________ (nếu không → STREAK3 path)
Ngày: 61|62|67 | T7 rotation (#5)
EQ sibling kèm (1): ________
1 cột deny hoặc 1 câu SA support:
1 câu vì sao PASS verify ≠ evidence BN:
G2: CLOSED · Goal: ACTIVE · densify ≠ DONE
```

## Trước Ngày 61

Nếu STREAK &lt;3: ưu tiên `PI-SESSION-SCRIPT-STREAK3` — không “nuốt” Q2 PREP thay ritual nền.

## Sau Ngày 70

`#6` `Q2-AMENDMENT-INTERIM-EARLY-SIGNAL-BRIDGE` (71–80) — SPIRIT/TT43 · interim **data thật** (vẫn không synthetic→G2).

## Liên kết

`Q2-STAGING-DEID-RITUAL-CARD` · `REDCAP-DEID-EXPORT-CHECKLIST` · **`DEID-EQ-SCIENCE-CARD`** · **`DEID-MISS-EQ-SCIENCE-CARD`** · **`PB004-EQ-SCIENCE-CARD`** · **`PB009-EQ-SCIENCE-CARD`** · **`AFTER-STREAK3-OPENER-1PAGE`** · **`BRIDGE-ROTATION`** (T7=#5) · `#4` TIER3-INTERIM-G2 · `#6` Q2-AMENDMENT-INTERIM · `SCIENCE-BRIDGES-SCIENCE-CARD` · `SCIENCE-CARDS-INDEX` · `STREAK_TRACKER` · `DATA-MANAGER-HANDOFF-REDCap-v0.2` · `PB-009-AI-BEFORE-OMICS`
