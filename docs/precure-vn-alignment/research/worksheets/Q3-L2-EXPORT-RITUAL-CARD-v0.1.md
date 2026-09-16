# Q3 — Export thật · AI L2 (Ngày 91–105)

**Mã:** Q3-L2-EXPORT-RITUAL-CARD-v0.1  
**Ngày:** 2026-09-16  
**Mở sau** pass/fail Q2 · Curriculum: `curriculum-days-91-120.md`  
**Hub:** `RITUAL-CARDS-INDEX.md` · Audit: `L2-MISSINGNESS-AUDIT-v0.1.md` · Stack: `AI-LONGITUDINAL-STACK`  
**Cờ đầu:** SA-01 · L3 **CLOSED** mặc định · Goal **ACTIVE**

## Một câu (tuần 14–15)

> Export de-ID thật → QC → M0–M3 **exploratory** trên N thật (nếu có) · leakage/TRIPOD nội bộ — cấm AUROC synthetic = lâm sàng · cấm mở L3 vì L2 sandbox xanh.

## Hai khối

| Khối | Ngày N | Việc | Artifact |
|------|--------|------|----------|
| **Export → L2** | 91–98 | QC bước · feature M0–M3 · missingness · weekly | `REDCAP-DEID` · PIPELINE · `redcap_import_qc` · `L2-MISSINGNESS-AUDIT` |
| **Leakage / TRIPOD** | 99–105 | Pitfall #1–2 · hold-out plan · TRIPOD nội bộ | `ML-OMICS-PITFALLS` · `TRIPOD-INTERNAL-CHECKLIST` |

## Ritual tối thiểu (1 câu DONE)

| N | Log | Quyết định / việc |
|---|-----|-------------------|
| **91** | `2026-12-17.md` | Có export thật? Nếu không → rehears QC trên `--demo` + ghi “chưa N” |
| **92** | `2026-12-18.md` | Deny list de-ID D1–D7 trên header export (hoặc demo) |
| **93** | `2026-12-19.md` | `redcap_import_qc` PASS/FAIL + 1 missing column nếu có |
| **94** | `2026-12-20.md` | Map cột export ↔ REQUIRED pipeline (1 dòng) |
| **95** | `2026-12-21.md` | M0–M3: chỉ exploratory; không claim Dx |
| **96** | `2026-12-22.md` | 1 % missing theo visit (template; trống nếu chưa N) |
| **97** | `2026-12-23.md` | Window D3: bắt buộc vs D1–D3 `[CẦN XÁC NHẬN]` |
| **98** | `2026-12-24.md` | Weekly: 1 ưu tiên L2 trước leakage tuần |
| **99** | `2026-12-25.md` | Pitfall #1: biến nào sau \(t^*\) cấm làm predictor early |
| **100** | `2026-12-26.md` | SAP ES §7: 1 câu non-leakage |
| **101** | `2026-12-27.md` | Peek vs pre-spec: không thêm predictor sau peek |
| **102** | `2026-12-28.md` | Pitfall #5: verify PASS ≠ evidence BN |
| **103** | `2026-12-29.md` | Hold-out site plan 1 câu (hoặc `[CẦN data]`) |
| **104** | `2026-12-30.md` | TRIPOD nội bộ: tick ≥2 mục |
| **105** | `2026-12-31.md` | TRIPOD: limitations + exploratory label |

## Stack nhắc

```text
L1 Z+clin_event → L2 M0–M3 trên export de-ID → L3 X chỉ sau G2
Synthetic/demo = schema rehearsal only
```

## Nếu chưa có export thật

Vẫn tick DONE khi: chạy `--demo` + ghi rõ **chưa N** + 1 câu việc site/DM còn mở.  
Không điền số synthetic vào interim/Q3 như kết quả BN.

## Checklist DONE (PI)

- [ ] 1 câu QC hoặc leakage trong log  
- [ ] STREAK PREP → **DONE**  
- [ ] Goal ACTIVE · L3 CLOSED  

## Trước khi nuốt Q3

STREAK <3 → `PI-SESSION-SCRIPT-STREAK3`.  
Chưa pass Q2 → `Q2-CHECKPOINT` trước claim L2 trên N thật.

## Sau Ngày 105

Tuần 16–17 (`curriculum-days-91-120.md` 106–120): SA-02/05 L2 · cross-SA · PB-004 prod · checkpoint Q3.

## Cấm

- Publish AUROC sandbox  
- Gộp endpoint SA  
- UpdateGoal complete · biospecimen trước G2
