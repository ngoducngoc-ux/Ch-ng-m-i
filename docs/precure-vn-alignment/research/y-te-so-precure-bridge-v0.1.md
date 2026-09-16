# Y tế số VN × Precure — cầu nối (không partnership)

**Mã:** YTSO-PRECURE-v0.1  
**Ngày:** 2026-09-16  
**Mục đích:** giữ hướng **phát hiện sớm – dữ liệu dọc – AI** cho Smart A và digital health VN, tách bạch với quảng bá thương mại Precure.LLC.

## 1. Học từ mô hình Precure (logic, không logo)

| Khía cạnh | Precure (tham chiếu press/VDHN) | Smart A / VN hiện tại |
|-----------|----------------------------------|------------------------|
| Dữ liệu | Multi-omics + lâm sàng dài hạn | RCT Smart A: \(Z\) dọc D0–D21; omics **gated** |
| AI | Pattern trước triệu chứng | Exploratory M0–M3 trên REDCap; không auto-diagnosis |
| Hành động | Actionable precision health | ALERT nội bộ nghiên cứu A/B/C |
| Quy mô | Cohort lớn / industry | N=80–120 — power hạn chế; ngôn ngữ trung tính |

## 2. Sản phẩm dữ liệu tối thiểu (y tế số đề tài)

1. **ID + timestamp + visit** — PB-004 architecture.  
2. **eCRF REDCap** staging → production (SA-01 v0.2 trước).  
3. **Audit trail** consent boundaries (ICF nested optional).  
4. **Export pipeline** → sandbox Python (verify.sh) trước khi claim model.  
5. **Layer omics (LIMS)** tách khỏi REDCap — chỉ sau cổng G2; xem `worksheets/G2-READINESS-v0.1.md` (Curriculum Ngày 07).

## 3. Ranh giới claim (TT 43 / ICH / đạo đức)

- Không dùng synthetic AUROC như bằng chứng lâm sàng.  
- Không triển khai app chẩn đoán sớm cho BN ngoài protocol.  
- Mọi “early signal” = **exploratory** trong SAP phụ.

## 4. Việc nhỏ quý (y tế số × early-signal)

- [ ] Map 1 workflow BN de-ID (StudyID–visit–\(Z\)) — `BN-VISIT-MAP-TEMPLATE` · bridge #9  
- [ ] **5′ de-ID deny/allow** — `DEID-5MIN-MICRO-DRILL` (T5/T7)  
- [ ] **5′ TRIPOD trước claim AI** — `TRIPOD-5MIN-MICRO-DRILL` (T5)  
- [ ] 1 hàng PB lens #13 cho PB-004 hoặc PB-009 (sớm/dọc/AI)  
- [ ] Rà claim truyền thông vs DOI — `MEDIA-SMART-A-CLAIMS` · Ngày 26  
- [ ] Checklist L1/L2: `AI-LONGITUDINAL-STACK` · `PB-009-AI-BEFORE-OMICS`  
- [ ] Nếu MISS ritual: `MISS-RESCUE-EARLY-SIGNAL-BRIDGE` (#14)

### Checklist tuần (15′) — digital health theo ba trụ

| Trụ | Câu hỏi nhanh | Pass nếu |
|-----|---------------|----------|
| **Sớm** | Visit / \(Z(t')\) có cửa sổ trước \(t^*\)? ALERT trên \(Z\) sớm? | eCRF / EQ · `ALERT-CROSS-SA-ATLAS` |
| **Dọc** | ID–timestamp–`clin_event` đủ L1? | PB-004 · `CLIN_EVENT-CROSS-SA-ATLAS` · không PHI trong git |
| **AI** | Export de-ID → QC trước model? Leakage? L3? | deny/allow · verify · `LEAKAGE-CROSS-SA-ATLAS` · `L1L2L3-DAILY-GATE-CARD` · L3 CLOSED |

## 5. Map nhanh sang stack AI (repo)

| Bước y tế số | File |
|--------------|------|
| ID + visit + event | PB-004 · eCRF `clin_event` · `CLIN_EVENT-CROSS-SA-ATLAS` |
| Export → QC | `redcap_import_qc.py` · PIPELINE-ES · `DEID-5MIN-MICRO-DRILL` |
| Exploratory AI | SAP ES M0–M3 · ML-PITFALLS · `LEAKAGE-CROSS-SA-ATLAS` |
| Omics | G2-READINESS — **CLOSED** mặc định |
| Ritual Tier 2 | `worksheets/DESIGN-YTESO-AI-RITUAL-CARD-v0.1.md` · bridge `DESIGN-YTESO-EARLY-SIGNAL-BRIDGE` |
| PB-009 AI trước omics | `worksheets/PB-009-AI-BEFORE-OMICS-v0.1.md` |
| PB lens / MISS rescue | `PB-EARLY-SIGNAL-LENS-BRIDGE` (#13) · `MISS-RESCUE-EARLY-SIGNAL-BRIDGE` (#14) |
| BN map de-ID | `BN-VISIT-MAP-TEMPLATE` · Q3 bridge #9 |

## Nguồn

- `sources/2026-precure-mayo-thermo-vdhn.md`  
- DOI Zhou 2019 · Nat Med 2019 (curriculum tuần 1)  
- `guides/AI-LONGITUDINAL-STACK-v0.1.md` · `equations/EQ-SA01|02|05-…`
