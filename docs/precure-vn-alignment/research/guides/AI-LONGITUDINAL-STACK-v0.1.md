# Stack AI × dữ liệu dọc × phát hiện sớm (Smart A / y tế số) · refresh v0.1b

**Mã:** AI-LONG-STACK-v0.1b · **Ngày:** 2026-09-16  
**Goal:** ACTIVE · STREAK thật vẫn **2 DONE** · EQ bank **CLOSED** · densify ≠ DONE  
**STREAK&lt;3?** Path STREAK3 trước · **`STREAK3-PACK`** · **`STREAK3-EQ`** · NatMed → tick **19/09** · dừng OPENER/stack  
**STREAK≥3?** **`AFTER-STREAK3-OPENER`** → 1×EQ sibling → **`DAILY-STACK`** · bridges #0–14  
**Không:** agent tick DONE · UpdateGoal complete trên PREP/densify · invent EQ mới · biospecimen trước G1–G2 · L3 CLOSED  
**Mục đích:** giữ hướng **phát hiện sớm – dữ liệu dọc – AI** mà không overclaim; map Precure logic → pipeline repo.  
**Hub:** `CURRICULUM-MONTHS-4-12-OUTLINE` (refresh v0.1b) · tip tiếp `MULTI-OMICS-GATES-SMART-A` · Drive keep `1Vjchf1i…`  

```text
STREAK <3? → STREAK3 (PI-NEXT) · densify ≠ DONE
        ↓ STREAK ≥3
OPENER → EQ sibling → DAILY-STACK · ritual theo Ngày N
```

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

- **Thẻ khoa học:** **`../worksheets/AI-STACK-SCIENCE-CARD-v0.1.md`** · `SCIENCE-CARDS-INDEX` (refresh v0.1b) · **`AI-STACK-EQ-SCIENCE-CARD`**
- `y-te-so-precure-bridge-v0.1.md` · `guides/ML-OMICS-PITFALLS-v0.1.md` · next tip `MULTI-OMICS-GATES-SMART-A-v0.1.md`  
- `equations/EQ-SA01-…` · `EQ-SA02-…` · `EQ-SA05-…` · EQ bank CLOSED · không invent EQ  
- `LONGITUDINAL-EARLY-SIGNAL-SA01-v0.1.md` · `PB-009-AI-BEFORE-OMICS-v0.1.md`  
- `CLIN_EVENT-ZHOU-MAP-v0.1.md` · `PEA-L1L2L3-DECISION-CARD-v0.1.md`  
- **5′ drill:** `../worksheets/AI-STACK-5MIN-MICRO-DRILL-v0.1.md` · PREP≠DONE · densify≠DONE  
- Drive keep `1Vjchf1i…` · Goal ACTIVE 12 tháng
