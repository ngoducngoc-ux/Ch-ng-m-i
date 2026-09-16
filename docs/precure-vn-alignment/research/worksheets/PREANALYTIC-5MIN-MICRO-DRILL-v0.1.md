# Micro-drill 5′ — Pre-analytic PEA (R1–R3 · trước G2)

**Mã:** PREANALYTIC-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T3** · sau/cùng `PEA-5MIN` · Ngày 05 · trước mọi “swab/exudate → protein”  
**Goal:** ACTIVE · G2 **CLOSED** · không order lab · matrix exudate ≠ serum validated · PREP ≠ DONE  
**DOI:** Lundberg [10.1093/nar/gkr424](https://doi.org/10.1093/nar/gkr424)

## Một câu

> PREANALYTIC 5′ = chọn **1 trong 3** rủi ro (phân hủy · heterogeneity · flora) và ghi 1 hàng giảm thiểu SOP — **không** lấy mẫu / không thêm form omics REDCap trước G2.

## Drill (điền)

```text
Rủi ro hôm nay: R1 phân hủy/time | R2 heterogeneity swab | R3 flora/môi trường — chọn: ________
1 hàng giảm thiểu SOP (≤15 từ): ________
Matrix hiện tại validate PEA: serum/plasma | exudate SA-01 — đúng cho SA-01 hôm nay? CHƯA [CẦN XÁC NHẬN]
Order swab/PEA vì đã ôn R1–R3? KHÔNG
Thêm form omics REDCap trước G2? KHÔNG
Panel nếu G2 sau này: hẹp ≤20 | 96 mù — chọn: ________
Cặp đã đụng: PEA-5MIN | G2-5MIN | OMICS-GATES | PB009 | PANEL feasibility — ghi: ________
1 việc nhỏ ≤30′ (PRE-ANALYTIC / PEA card / PB006 ISO): ________
Đóng Goal / mở L3 vì PREANALYTIC? KHÔNG
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| # | File cặp |
|---|----------|
| R1–R3 đầy đủ | `PRE-ANALYTIC-PEA-SA01` |
| PEA L3 CLOSED | `PEA-5MIN` · `PEA-L1L2L3-DECISION-CARD` |
| Panel hẹp | `PEA-PANEL-FEASIBILITY-SA01` |
| Panel 5′ | **`PEA-PANEL-5MIN`** · `PEA-PANEL-FEASIBILITY-SA01` |
| G2 / cổng | `G2-5MIN` · `OMICS-GATES-5MIN` |
| Bridge | `MULTI-OMICS-PEA-SA01-BRIDGE` |
| SA-04 device | `PB006-5MIN` nếu swab mới |

## Cấm

- Order kit / swab / PEA vì đã điền drill  
- Coi serum/plasma literature = exudate SA-01 đã validate  
- Discovery 96-plex mù trên N=120  

## Liên kết

- Spec: `PRE-ANALYTIC-PEA-SA01-v0.1.md` · Daily stack: `DAILY-STACK-AFTER-STREAK3` (T3)  
- Protocol: `../../rituals/daily-protocol.md` · Guide gates: `../guides/MULTI-OMICS-GATES-SMART-A-v0.1.md`
