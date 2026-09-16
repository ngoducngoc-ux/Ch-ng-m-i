# Stack AI × dữ liệu dọc × phát hiện sớm (Smart A / y tế số)

**Mã:** AI-LONG-STACK-v0.1  
**Ngày:** 2026-09-16  
**Mục đích:** giữ hướng **phát hiện sớm – dữ liệu dọc – AI** mà không overclaim; map Precure logic → pipeline repo.

## 1. Ba lớp (thứ tự bắt buộc)

```text
L1 Lâm sàng dọc (REDCap Z, clin_event, visit)  ← đang xây
L2 AI exploratory (M0–M3, QC, leakage gates) ← sandbox + verify.sh
L3 Multi-omics X (PEA/NGS…)                  ← chỉ sau G1–G2 data thật
```

| Lớp | Artifact repo | Trạng thái |
|-----|---------------|------------|
| L1 | eCRF v0.2 · DESIGN-SA01 · PB-004 | DRAFT / DM review mở |
| L2 | `REDCap-to-M0-M3-PIPELINE` · SAP ES · ML-PITFALLS | Synthetic PASS ≠ lâm sàng |
| L3 | SPEC-BIO · G2-READINESS · OMICS-IF-G2 · **PEA-L1L2L3-DECISION-CARD** | **CLOSED** mặc định |

## 2. “Early” nghĩa gì trong Smart A

| Đúng | Sai |
|------|-----|
| \(t' \ll t^*\) trên \(Z\) (và sau này \(X\)) exploratory trong SAP phụ | App chẩn đoán sớm ngoài protocol |
| ALERT A/B/C nội bộ nghiên cứu | Đổi nhánh RCT theo AUROC sandbox |
| Chuỗi visit + sự kiện (Zhou-style) | Một snapshot baseline = “Precure” |

\(t^*\): SA-01 D21 · SA-02 D3 · SA-05 D14.

## 3. Luồng AI tối thiểu (không partnership Precure.LLC)

1. Export de-ID (PB-004) → `redcap_import_qc.py`  
2. Feature sets M0–M3 theo SAP ES (pre-spec)  
3. Metrics nội bộ + FDR / multiplicity note  
4. Interim descriptive trên **N thật** (INTERIM-MOCK = rehearsal only)  
5. M4 + \(X\) chỉ nếu G2 pass ghi trong SPEC-BIO

## 4. Câu hỏi gắn PB-009

Checklist điền được: `worksheets/PB-009-AI-BEFORE-OMICS-v0.1.md` — L1→L2 đủ chưa trước khi nói “AI phát hiện sớm”? L3 chỉ khi còn gap trên N thật + G2.

## Liên kết

- `y-te-so-precure-bridge-v0.1.md` · `guides/ML-OMICS-PITFALLS-v0.1.md`  
- `equations/EQ-SA01-…` · `EQ-SA02-…` · `EQ-SA05-…`  
- `LONGITUDINAL-EARLY-SIGNAL-SA01-v0.1.md` · `PB-009-AI-BEFORE-OMICS-v0.1.md`  
- `CLIN_EVENT-ZHOU-MAP-v0.1.md` · `PEA-L1L2L3-DECISION-CARD-v0.1.md`
