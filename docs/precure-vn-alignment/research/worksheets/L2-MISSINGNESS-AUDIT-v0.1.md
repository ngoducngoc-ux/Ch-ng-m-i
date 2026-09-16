# L2 missingness & visit-window audit (SA-01)

**Mã:** L2-MISSINGNESS-AUDIT-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Q3 Ngày 96–97 · Ritual: `Q3-L2-EXPORT-RITUAL-CARD`  
**Chỉ điền số khi có export de-ID thật** — để trống / `[chưa N]` nếu chỉ `--demo`

## 1. Missing % theo visit (template)

| Visit | n | PCT_EPITH %miss | CFU %miss | VAS_DRESS %miss | clin_event %miss | Ghi chú |
|-------|---|-----------------|-----------|-----------------|------------------|---------|
| D0 | | | | | | baseline |
| D3 | | | | | | window `[CẦN XÁC NHẬN DM]` |
| D7 | | | | | | early cửa sổ |
| D14 | | | | | | không predictor “early→D21” nếu sau \(t'\) |
| D21 | | — | — | — | | \(Y\) only |

## 2. Visit window (DM / PI)

| Câu hỏi | Trả lời |
|---------|---------|
| D3 bắt buộc hay nằm trong D1–D3? | `[CẦN XÁC NHẬN]` |
| Visit ngoài window: exclude hay flag? | |
| `clin_event` missing = 0 hay NA? | |

## 3. QC gates trước M0–M3

- [ ] `redcap_import_qc.py` PASS trên export (hoặc `--demo` + ghi chưa N)  
- [ ] Deny list de-ID đã skim (`REDCAP-DEID-EXPORT-CHECKLIST`)  
- [ ] Không dùng biến sau cửa sổ early làm predictor early (pitfall #1)  
- [ ] Không báo AUROC synthetic như lâm sàng (pitfall #5)  

## 4. Một câu DONE (dán log)

```text
Missingness: D0=… D3=… D7=… | Window D3=… | QC=PASS/FAIL | N thật=có/chưa
```

## Liên kết

PIPELINE · DESIGN-SA01 · INTERIM-TABLE-TEMPLATE · SAP-SA01-ES · PB-009 L2.1  
**5′ drill:** `MISSINGNESS-5MIN-MICRO-DRILL`  
Bridge: `Q3-L2-EXPORT-EARLY-SIGNAL-BRIDGE` · thẻ `Q3-L2-EXPORT-RITUAL-CARD`
