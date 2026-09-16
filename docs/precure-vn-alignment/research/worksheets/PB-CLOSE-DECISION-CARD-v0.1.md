# Decision card — đóng / PARK problem-bank (Q2)

**Mã:** PB-CLOSE-DECISION-CARD-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 81–83 · Ritual: `Q2-CHECKPOINT-RITUAL-CARD`  
**Chỉ PI** đổi trạng thái trong `problem-bank.md` (agent không CLOSED thay PI)

## Khi nào CLOSED

| Điều kiện | Ví dụ |
|-----------|--------|
| Câu hỏi đã trả lời đủ mức đề tài **hoặc** chuyển thành SAP/eCRF đã version | PB-001 → SAP ES + eCRF v0.2 + EQ đã có, câu hỏi còn lại = follow-up mới |
| Có **pointer** artifact + 1 câu lý do trong log | `EQ-SA01` · `EH-SA01` · DOI |
| Không còn việc nhỏ blocking Tier 0 | DM/cờ SA-01 vẫn mở → thường **không** CLOSED cờ đầu |

## Khi nào PARKED

| Điều kiện | Ví dụ |
|-----------|--------|
| Đúng hướng nhưng **thiếu data thật / thiếu số điều / thiếu N** | PB-009 L2 chờ export de-ID |
| Phụ thuộc G1–G2 CLOSED | PB omics / nested |
| Hạ ưu tiên sau khi chọn cờ SA-01 | PB-002/005 hỗ trợ — PARK đến sau staging SA-01 |

## Không CLOSED nếu

- Chỉ vì agent đã tạo worksheet PREP  
- Chỉ vì `verify.sh` PASS (sandbox)  
- Muốn “cho đủ ≥2 PB” trước Ngày 90 mà không có lý do  

## Gợi ý cặp đóng sớm (PI chọn — không bắt buộc)

| Ưu tiên xem xét | Lý do có thể PARK/CLOSED | Giữ OPEN nếu |
|-----------------|--------------------------|--------------|
| **PB-004** | Diagram + de-ID checklist + architecture đã có | Consent omics chưa tick / DM chưa staging |
| **PB-008** | Worksheet + NatMed map + media claims | Chưa 1 câu trong SAP ES sensitivity |
| **PB-006** | ISO gates worksheet đủ cổng đọc | Intended contact chưa `[CẦN XÁC NHẬN]` |
| **PB-001** | Thường **giữ OPEN** (cờ đầu) đến có export/interim thật | — |
| **PB-009** | PARK đến L2 trên data thật | Đừng CLOSED vì chỉ có checklist |

## Template 1 dòng (dán vào problem-bank + log)

```text
PB-00X → CLOSED|PARKED (YYYY-MM-DD) — lý do: … — pointer: …
```

## Mục tiêu Q2

≥**2** quyết định CLOSED hoặc PARKED trước Ngày 90 (checkpoint bảng).  
CLOSED/PARK PB ≠ hoàn thành Goal 12 tháng.
