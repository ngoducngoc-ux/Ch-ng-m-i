# Micro-drill 5′ — G2 readiness (omics gate · SA-01)

**Mã:** G2-5MIN-MICRO-DRILL-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** Daily stack **T3/T5** · sau `PEA-5MIN`/`PB009-5MIN` · trước mọi “sắp lấy mẫu / order PEA”  
**Goal:** ACTIVE · G2 **CLOSED** mặc định · L3 CLOSED · synthetic ≠ pass G2 · PREP ≠ DONE  

## Một câu

> G2 = signal \(Z\) trên **N thật** + ethics G1 + logistics — **không** pass bằng `verify.sh`/AUROC sandbox; chưa đủ ba điều kiện thì **không** order omics.

## Drill (điền)

```text
G2 hôm nay: CLOSED | PREP checklist | PASS (chỉ khi PI/DSMB) — chọn: ________
Signal Z trên N thật? CHƯA | INTERIM | CÓ — ghi: ________
Ethics G1 (ICF/amendment mẫu)? CHƯA [CẦN XÁC NHẬN] | CÓ
verify.sh / AUROC sandbox pass G2? KHÔNG — vì: ________
Order PEA/omics hôm nay? KHÔNG — thiếu: ________
1 việc nhỏ ≤30′ (PB009 / PEA / TT43 / DM): ________
1 câu dán log (≤20 từ):
```

## Đối chiếu nhanh

| Bước | File |
|------|------|
| Readiness đầy đủ | `G2-READINESS` |
| AI trước omics | `PB009-5MIN` |
| Daily gate 5′ | `L1L2L3-5MIN` |
| PEA | `PEA-5MIN` · decision card |
| Ethics | `TT43-5MIN` · nested G1 |
| Bridge | `TIER3-INTERIM-G2-BRIDGE` |

## Cấm

- Synthetic AUROC / `verify.sh` PASS = G2 pass  
- Order mẫu vì đã đọc Wik/PEA/EQ  
- Coi PREP checklist = G2 đã mở  

## Liên kết

- Daily stack: `DAILY-STACK-AFTER-STREAK3` (T3 · gate L3)  
- Spec: `SPEC-SA01-BIO` · Protocol: `../../rituals/daily-protocol.md`
