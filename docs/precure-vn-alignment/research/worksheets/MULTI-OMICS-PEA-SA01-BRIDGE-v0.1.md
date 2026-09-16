# Bridge — PEA / multi-omics → SA-01 (L1→L2→L3)

**Mã:** MULTI-OMICS-PEA-SA01-BRIDGE-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 05–07 · ôn PB-009 · Q3 omics-if  
**DOI:** Lundberg [10.1093/nar/gkr424](https://doi.org/10.1093/nar/gkr424) · Assarsson [10.1371/journal.pone.0095192](https://doi.org/10.1371/journal.pone.0095192) · Wik [10.1016/j.mcpro.2021.100168](https://doi.org/10.1016/j.mcpro.2021.100168)  
**Thẻ:** `PEA-L1L2L3-DECISION-CARD` · Gates: `MULTI-OMICS-GATES-SMART-A`  
**Không:** order assay · pass G2 bằng sandbox · claim Dx multi-omics

## Vì sao PEA thuộc “tín hiệu sớm / multi-omics”

| Paper | Ý kỹ thuật | Vai trò Precure logic | SA-01 hôm nay |
|-------|------------|----------------------|---------------|
| Lundberg 2011 | Proximity extension + qPCR | Đo \(X_{\text{protein}}\) lặp được | **L3** — chưa mở |
| Assarsson 2014 | 96-plex throughput | Scale panel; power vẫn yếu nếu N=120 mù | Panel hẹp ≤15–20 **nếu** G2 |
| Wik 2021 | PEA+NGS scale | Omics layer ≠ clinical REDCap | 2 hệ: Clinical vs LIMS |

## Phương trình — chỗ \(X\) xuất hiện

```text
Hiện tại (L1/L2):
  P(Y_D21=1) = σ( β0 + β_Z·Z(D0,D3,D7) + β_g·GROUP + β_C·C )

Sau G2 (L3 / M4 — optional):
  + β_X·X_PEA(t')     t' ∈ {D0,D3,D7}
  primary Y_D21 không đổi
```

Chi tiết: `EQ-SA01-early-warning` · H0_mol trong `HYP-SA01-H0H1`

## Ba cổng trước mọi swab/PEA

| Cổng | Câu hỏi | Artifact |
|------|---------|----------|
| **G1** | Nested biospecimen + ICF đã duyệt? | `SPIRIT-NESTED-G1-CHECKLIST` |
| **G2** | PI/DSMB pass trên **data thật** (không synthetic)? | `G2-READINESS` · `OMICS-IF-G2` |
| **Pre-analytic** | Matrix exudate ổn (R1–R3)? | `PRE-ANALYTIC-PEA-SA01` |

**Mặc định trả lời:** G1/G2 **CLOSED** · chưa order.

## Y tế số (2 layer)

```text
REDCap (Z, clin_event, ALERT)  ≠  LIMS/PEA batch (X)
Export de-ID → L2 AI        ≠  raw assay files in git
```

PB-004 · `y-te-so-precure-bridge` · PB-009 L1→L2 trước L3.

## Ritual fill-in (Ngày 05 / 06 / 07)

```text
Ngày: 05 | 06 | 07
1 insight kỹ thuật:
1 câu vì sao CHƯA order assay:
G2 status: CLOSED | …
```

## Liên kết Zhou / Nat Med

Logic “trước endpoint + dọc” đã ở `EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01`.  
PEA chỉ là **ứng viên \(X\)** sau khi \(Z\)/`clin_event` đủ — không thay Zhou/Nat Med ritual STREAK≥3.

## Cấm

- “Đã đọc PEA = đã làm multi-omics Smart A”  
- Full 96-plex discovery trên N=120 không FDR plan  
- SA-03 biofilm in-vitro = Dx BN
