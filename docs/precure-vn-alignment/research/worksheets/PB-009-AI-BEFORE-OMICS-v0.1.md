# PB-009 — AI trên dữ liệu dọc **trước** multi-omics (checklist)

**Mã:** PB-009-AI-BEFORE-OMICS-v0.1  
**Ngày:** 2026-09-16  
**Problem bank:** `problem-bank.md` §PB-009 · Stack: `AI-LONGITUDINAL-STACK-v0.1.md`  
**Ritual:** DESIGN-YTESO Ngày 21/20 · Tier3 governance · **không** mở L3 để “có AI”

## Câu hỏi PB-009

Kiến trúc tối thiểu nào (visit + `clin_event` + export de-ID + M0–M3 pre-spec) đủ để nói **“AI trên dữ liệu dọc / tín hiệu sớm”** mà **không** cần L3 multi-omics — và khi nào L3 thật sự thêm giá trị dự báo \(Y(t^*)\)?

## Checklist L1 (y tế số / REDCap) — đủ chưa?

| # | Điều kiện tối thiểu | Artifact | Tick (PI khi có data/DM) |
|---|---------------------|----------|--------------------------|
| L1.1 | Visit + timestamp + ID (PB-004) | `PB-004-DIAGRAM` · eCRF | [ ] |
| L1.2 | `clin_event` 0–4 trên visit ES | `CLIN_EVENT-ZHOU-MAP` · CSV v0.2 | [ ] |
| L1.3 | \(Z\) sớm theo SA (PCT/CFU/VAS hoặc PUSH/VAS) | Endpoints card · EQ-SA0x | [ ] |
| L1.4 | Consent / de-ID boundary rõ | PB-004 · ICF | [ ] |
| L1.5 | DM review staging SA-01 v0.2 | `DM-FORWARD-CHECKLIST` | [ ] |

**L1 đủ để nói “có dữ liệu dọc”** khi L1.1–L1.3 có trên N thật (không chỉ PREP).

## Checklist L2 (AI exploratory) — đủ chưa?

| # | Điều kiện tối thiểu | Artifact | Tick |
|---|---------------------|----------|------|
| L2.1 | Export de-ID → QC (`redcap_import_qc`) | PIPELINE · `verify.sh` | [ ] sandbox only |
| L2.2 | M0–M3 pre-spec trong SAP ES | `SAP-SA01-ES` · H0/H1 | [ ] |
| L2.3 | Pitfalls #1 leakage · #5 synthetic ghi trong báo cáo | `ML-OMICS-PITFALLS` · TRIPOD | [ ] |
| L2.4 | Metrics nội bộ trên **N thật** (không claim Dx) | Interim descriptive | [ ] chưa có N thật |
| L2.5 | ALERT nội bộ gắn quyết định nghiên cứu | `ALERT-SA01` · NatMed map | [ ] draft |

**L2 đủ để nói “AI exploratory trên chuỗi \(Z\)”** khi L2.2 + L2.4 trên data thật — **sandbox PASS ≠ L2.4**.

## Khi nào L3 (PEA/omics) thêm giá trị?

Chỉ khi **đồng thời**:

1. G2 pass trên signal \(Z\) / DSMB (không synthetic) — `G2-READINESS`  
2. Matrix / pre-analytic chốt — `PRE-ANALYTIC-PEA` · ISO nếu device mới  
3. Câu hỏi rõ: \(X(t')\) cải thiện M3→M4 trên \(Y(t^*)\) (H0_mol) — `HYP-SA01` · PEA card  
4. Ethics G1 + LIMS tách REDCap — DESIGN-YTESO / y-te-so §2  

Nếu L1–L2 chưa đủ → **không** order assay để “có omics AI”.

## Một câu (copy vào log / slide)

> Smart A có thể nói “AI × dữ liệu dọc × tín hiệu sớm” trên **L1+L2** (REDCap \(Z\) + `clin_event` + M0–M3 exploratory) mà **không** cần multi-omics; L3 chỉ sau G2 khi còn khoảng trống dự báo trên N thật.

## Việc nhỏ (PI / agent)

- [ ] PI: tick L1.5 (DM) + nhắc L2.4 cần N thật tại checkpoint 16/10  
- [ ] Agent: giữ G2 CLOSED · không claim verify.sh = L2.4  
- [ ] Hàng ngày (sau STREAK≥3): `L1L2L3-DAILY-GATE-CARD-v0.1.md` (5′)  
- [ ] Ôn kèm: `PEA-L1L2L3-DECISION-CARD` · `y-te-so-precure-bridge`

## Liên kết

- Daily gate: `L1L2L3-DAILY-GATE-CARD-v0.1.md`  
- `problem-bank.md` PB-009 · `MULTI-OMICS-GATES` · `RITUAL-CARDS-INDEX`  
- EQ: `EQ-SA01|02|05` · Media: không copy claim Precure.LLC

- **5′ drill:** `PB009-5MIN-MICRO-DRILL`
