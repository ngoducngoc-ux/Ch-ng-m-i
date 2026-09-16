# Multi-omics & early-signal — cổng theo đề tài Smart A

**Mã:** OMICS-GATES-SA-v0.1  
**Ngày:** 2026-09-16  
**Mục đích:** tránh mở omics người / AI overclaim; giữ logic Precure **phân tầng**.

## Ma trận cổng

| SA | Lớp dữ liệu “sớm” hiện tại | Omics / phân tử người | Cổng bắt buộc |
|----|----------------------------|------------------------|---------------|
| **01** (cờ đầu) | \(Z\) D0–D7 · `clin_event` | PEA/panel \(X\) | G1 nested consent · **G2** DSMB/PI · ISO liên quan sản phẩm |
| **02** | VAS + khám · CFU? | Marker niêm mạc \(X\) | G2 · harmonize VAS worksheet |
| **03** | In-vitro biofilm ATCC | **Không** RCT người | Không map trực tiếp sang Dx BN; translation worksheet |
| **04** | ISO 10993 tiền lâm sàng | Omics người **sau** contact profile | EH-SA04 gates trước mọi L3 |
| **05** | PUSH dọc · Braden · adherence | Proteomics dịch tiết (tương lai) | G2 · ICU burden sampling |

## Thứ tự mở (y tế số VN)

```text
PB-004 ID/time → eCRF L1 → export QC → L2 AI M0–M3 (SAP ES)
→ interim descriptive N thật → (optional) L3 X sau G2 pass
```

## Cấm (mọi SA)

- AUROC synthetic = bằng chứng lâm sàng (`verify.sh` chỉ QC pipeline).  
- SA-03 in-vitro → claim “phát hiện sớm” trên BN không qua RCT.  
- Mở lấy mẫu omics vì curriculum PREP — chỉ PI/DSMB + data thật.

## Liên kết

- `alignment-map-smart-a.md` · `AI-LONGITUDINAL-STACK-v0.1.md`  
- **`MULTI-OMICS-PEA-SA01-BRIDGE-v0.1.md`** · `EQ-SA01-early-warning-v0.1.md`  
- `OMICS-IF-G2-v0.1.md` · `SPEC-SA01-BIO-v0.1-DRAFT.md`  
- `SA03-BIOFILM-TRANSLATION-v0.1.md` · `EH-SA04-gates.md`

- **5′ drill:** `../worksheets/OMICS-GATES-5MIN-MICRO-DRILL-v0.1.md`
