# Handoff Data Manager — REDCap SA-01 early-signal v0.2

**Ngày:** 2026-09-16  
**Người gửi:** Chủ nhiệm Smart A / Precure VN Alignment  
**Mục đích:** review dictionary exploratory **trước** amendment đề cương chính thức.

## File cần import

| Phiên bản | Git | Drive |
|-----------|-----|-------|
| v0.1 | `research/worksheets/redcap_sa01_early_signal_dictionary_v0.1.csv` | [v0.1 trên Drive](https://drive.google.com/file/d/1gSu-OVLnCOuEpKqNMu4gdtQDmHEd4vFJ/view) |
| **v0.2** | `research/worksheets/redcap_sa01_early_signal_dictionary_v0.2.csv` | [v0.2 trên Drive](https://drive.google.com/file/d/1EnHP9GfGJEnDt-qs-eTbH8VayclX4gfH/view) |

## Thay đổi v0.1 → v0.2

1. Thêm **`clin_event`** — sự kiện lâm sàng kể từ visit trước (logic Zhou: tín hiệu gắn bối cảnh).  
2. Thêm **`clin_event_note`** — ghi chú khi chọn “Khác”.  
3. Không đổi primary D21 / nhánh randomization.

## Câu hỏi cần DM trả lời

1. Repeating instrument `visit_es`: D3/D7 **bắt buộc** hay optional nếu BN lỡ hẹn?  
2. Tuổi validation **18–70** (synopsis) vs 18–75 trong dictionary cũ — chốt một ngưỡng.  
3. `culture_cfu` + `culture_unit`: đơn vị thống nhất site trước go-live?  
4. Có import exploratory form **tách project** (staging REDCap) trước production không?

## Phạm vi không làm trong lần này

- Không mở biospecimen / form omics (`SPEC-SA01-BIO-v0.1-DRAFT.md` — cổng G1–G2).  
- Không claim AI chẩn đoán — chỉ biến phục vụ SAP exploratory.

## Sau review

- [ ] DM ghi ngày review vào `PROJECT_STATUS.md`  
- [ ] PI quyết định amendment vs phụ lục exploratory  
- [ ] Cập nhật `DESIGN-SA01-minimal-longitudinal-v0.1.md` nếu đổi visit map

## Liên kết khoa học

- `eCRF-SA01-early-signal-dictionary-v0.1.md` (spec human-readable)  
- `SAP-SA01-ES-v0.1-DRAFT.md` · `EH-SA01-early-signal-v0.1.md`  
- **Toàn bộ SA:** `DATA-MANAGER-REDCap-INDEX.md`
