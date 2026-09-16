# Cursor sync — Precure VN Alignment (laptop + desktop)

Khi mở repo này trên **laptop hoặc desktop**, agent phải:

1. Đọc `docs/precure-vn-alignment/ACTIVE_PROJECT_CARD.md` trước mọi việc liên quan Precure / early signal / multi-omics.
2. Tôn trọng ritual ngày/tuần và problem bank; không để dự án bị quên.
3. Đồng bộ hub Drive: thư mục `00_AI_TRUNG_TAM_DIEU_HANH/CURSOR_SYNC_BRIDGE/` (Google Drive của ngoducngoc@gmail.com).
4. Nguồn tin Precure khi trích dẫn: **Mạng lưới Y tế Số Việt Nam — Vietnam Digital Health Network**.
5. Không lưu secrets / PHI / hồ sơ BN định danh.

## Source of truth

| Lớp | Nơi | Vai trò |
|-----|-----|---------|
| GitHub | `ngoducngoc-ux/Ch-ng-m-i` branch/PR Precure | Chi tiết tài liệu + log |
| Drive hub | `00_AI_TRUNG_TAM_DIEU_HANH/CURSOR_SYNC_BRIDGE` | Pointer nhanh cho mọi máy |
| Calendar | Google primary | Nhắc hàng ngày / tuần / quý |
| Cursor Goal | Cloud agent goal | Mục tiêu dài hạn runtime |

## Lệnh nhanh trên máy local

```bash
git fetch origin
git checkout cursor/precure-vn-alignment-729d   # hoặc main sau khi merge
git pull
```

Mở folder repo trong Cursor Desktop — rules trong `.cursor/rules/` sẽ được nạp.

## Pointer Git (cập nhật 2026-09-16)

| Chủ đề | Path trong repo |
|--------|-----------------|
| Hub 1 trang | `docs/precure-vn-alignment/INDEX.md` |
| DM forward | `research/worksheets/DM-FORWARD-CHECKLIST-v0.1.md` |
| Omics gates G2 | `research/worksheets/G2-READINESS-v0.1.md` |
| PEA pre-analytic | `research/worksheets/PRE-ANALYTIC-PEA-SA01-v0.1.md` |
| SA-05 PUSH | `research/worksheets/PUSH-SA05-COMPONENTS-v0.1.md` |
| SA-05 EQ gap | `research/worksheets/EQ-EH-SA05-GAP-v0.1.md` |
| SA-02 VAS scale | `research/worksheets/VAS-SCALE-HARMONIZE-SA02-v0.1.md` |
| SA-03 biofilm | `research/worksheets/SA03-BIOFILM-TRANSLATION-v0.1.md` |
| SA-04 ISO swab | `research/worksheets/ISO-SWAB-CONTACT-PRIORITY-v0.1.md` |
| SPIRIT / nested G1 | `research/worksheets/SPIRIT-SA01-MAP-v0.1.md` · `SPIRIT-NESTED-G1-CHECKLIST-v0.1.md` |
| Verify | `research/analysis/verify.sh` |

*(Drive hub: mirror các link handoff REDCap trong `worksheets/DATA-MANAGER-REDCap-INDEX.md`.)*
