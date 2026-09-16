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
