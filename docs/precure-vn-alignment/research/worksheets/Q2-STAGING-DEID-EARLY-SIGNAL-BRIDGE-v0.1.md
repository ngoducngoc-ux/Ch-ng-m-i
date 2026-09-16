# Bridge — Q2 staging / de-ID → L2 early-signal (SA-01 cờ)

**Mã:** Q2-STAGING-DEID-EARLY-SIGNAL-BRIDGE-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 61–70 · sau checkpoint 60d  
**Thẻ:** `Q2-STAGING-DEID-RITUAL-CARD` · Checklist: `REDCAP-DEID-EXPORT-CHECKLIST`  
**Cờ đầu:** SA-01 · SA-02/05 support · G2 **CLOSED** · Goal **ACTIVE**  
**Không:** PHI rời site · biospecimen · gộp endpoint · PREP = DONE · AUROC sandbox = lâm sàng

## Vì sao Q2 thuộc “phát hiện sớm–dọc–AI”

| Việc Q2 | Precure logic | Artifact |
|---------|---------------|----------|
| Deny/allow export | Y tế số: StudyID + visit + \(Z\) không PII | `REDCAP-DEID-EXPORT-CHECKLIST` · PB-004 |
| QC schema (`verify` / `redcap_import_qc`) | L2 pipeline sẵn trước model trên N thật | PIPELINE · `verify.sh` |
| Staging SA-02/05 | Cùng khung \(t'\ll t^*\) — schema only | `ENDPOINTS-CROSS-SA-BRIDGE` · EQ-02/05 |
| DM / consent boundary | L1 đủ trước “AI early” (PB-009) | DM handoff · `PI-ACTIONS-NOW` |

Bridges T1–T3 đã khai **khoa học + cổng**; Q2 = **đường dữ liệu thật tối thiểu** để L2 exploratory không còn chỉ synthetic.

## Luồng một trang

```text
Site PHI (không rời) 
  → StudyID + visit + Z + clin_event (allow)
  → export de-ID (deny D1–D7)
  → QC schema (verify / redcap_import_qc)
  → M0–M3 exploratory trên N thật (L2)  ← mục tiêu Q2
  → L3 X_mol chỉ sau G2 (CLOSED)
```

## Ba cổng trước mọi “AI early trên data thật”

| Cổng | Câu hỏi | Trả lời mặc định |
|------|---------|------------------|
| **De-ID** | Export có cột deny (PII / ICF / omics raw)? | Phải tick checklist Ngày 61–63 |
| **DM / Tier 0** | SA-01 v0.2 đã forward / review? | `[CẦN XÁC NHẬN]` PI |
| **G2** | Signal \(Z\) / DSMB trên N thật? | **CLOSED** — không order |

## SA support (66–70) — không gộp \(Y\)

| SA | Primary \(t^*\) | Việc Q2 | Cấm |
|----|----------------|---------|-----|
| **01** | D21 | Staging export + QC path | Omics raw trong CSV |
| **02** | VAS D3 | Dictionary / EQ ôn · D1 optional | Marker = primary |
| **05** | PUSH D14 | EQ gap / missingness | \(\Delta\)PUSH = Dx ICU |

## Liên hệ bridges trước

| Bridge | Vai trò còn lại ở Q2 |
|--------|----------------------|
| Zhou/Nat Med · Endpoints | \(Z\)/`clin_event` phải có trong allow list |
| PEA · Tier3 Interim/G2 | D7 deny = omics raw; interim ≠ pass G2 |
| DESIGN-YTESO | TT43/PB-004 khi đổi CRF / export policy |

## Ritual fill-in (61 / 62 / 67 — mẫu)

```text
Ngày: 61|62|67
1 cột deny hoặc 1 câu SA support:
1 câu vì sao PASS verify ≠ evidence BN:
G2: CLOSED | …
```

## Trước Ngày 61

Nếu STREAK &lt;3: ưu tiên `PI-SESSION-SCRIPT-STREAK3` — không “nuốt” Q2 PREP thay ritual nền.

## Sau Ngày 70

`Q2-AMENDMENT-INTERIM-RITUAL-CARD` (71–80) — SPIRIT/TT43 · interim **data thật** (vẫn không synthetic→G2).

## Liên kết

- Thẻ: `Q2-STAGING-DEID-RITUAL-CARD-v0.1.md`  
- `REDCAP-DEID-EXPORT-CHECKLIST` · `DATA-MANAGER-HANDOFF-REDCap-v0.2` · `REDCap-to-M0-M3-PIPELINE`  
- `PB-009-AI-BEFORE-OMICS` · `TIER3-INTERIM-G2-BRIDGE`
