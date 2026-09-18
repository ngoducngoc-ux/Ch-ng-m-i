# CONTEXT_FOR_LAPTOP_CURSOR.md

> **Dán nguyên khối dưới đây** làm tin nhắn đầu cho Cursor trên laptop (hoặc `@` file này).

---

## Vai trò

Em là Cursor trên **laptop** của PGS.TS.BS. Ngô Đức Ngọc (`ngoducngoc@gmail.com`). Xưng hô em–anh. Tiếng Việt chuyên nghiệp, ngắn, có cấu trúc. Không quảng bá. Không bịa số hiệu/ngày/URL/hiệu lực.

## Nhiệm vụ đang mở

Tiếp nhận và xử lý gói **văn bản pháp luật về khám sức khỏe toàn dân** do Cloud Agent bàn giao.

- **Repo:** `github.com/ngoducngoc-ux/Ch-ng-m-i`
- **Nhánh:** `cursor/ksk-toan-dan-vbpl-4211`
- **PR:** https://github.com/ngoducngoc-ux/Ch-ng-m-i/pull/8
- **Cloud agent nguồn:** https://cursor.com/agents/bc-01a0b51b-0c5d-7509-b3e1-48b2ca3d4211
- **Project gốc:** https://cursor.com/agents/bc-157e8466-5d5a-4663-b8bc-8fd839fd06ca (Khám sức khỏe toàn dân)
- **Mốc rà soát:** 18/09/2026

## Lấy code

```bash
cd <repo-Ch-ng-m-i>
git fetch origin cursor/ksk-toan-dan-vbpl-4211
git checkout cursor/ksk-toan-dan-vbpl-4211
```

Thư mục làm việc: `docs/kham-suc-khoe-toan-dan/`

| File | Dùng để |
|------|---------|
| `van-ban-phap-luat-kham-suc-khoe-toan-dan.md` | Báo cáo chính (diff/merge) |
| `van-ban-phap-luat-kham-suc-khoe-toan-dan.docx` | Soạn / xuất cho anh |
| `phu-luc/01-luat-va-bhyt.md` | Luật khung + BHYT |
| `phu-luc/02-nhom-dan-so.md` | Trẻ em, học sinh, thai sản, NCT, NVQS |
| `phu-luc/03-lao-dong-va-ksk.md` | ATVSLĐ / KSK NLĐ / BNN |
| `phu-luc/04-chuong-trinh-va-sang-loc.md` | CTMT / chiến lược / sàng lọc |
| `NGUON_VA_GIOI_HAN.md` | Provenance + giới hạn |
| `BAN_GIAO_LAPTOP.md` | Hướng dẫn bàn giao |

## Kết luận đã chốt (đừng đảo nếu chưa có bằng chứng mới)

1. Từ **01/07/2026**, khung trực tiếp khám định kỳ / sàng lọc miễn phí = **Luật Phòng bệnh 114/2025/QH15** + **NĐ 165/2026/NĐ-CP** (Điều 69–74).
2. **Không có** “Luật Y tế dự phòng 89/2025/QH15” — `89/2025/QH15` là Luật Ngân sách nhà nước.
3. BHYT: **Luật 51/2024** + **Điều 44 Luật Phòng bệnh** + **NQ 261/2025/QH15**; không suy diễn chi trả mọi gói check-up.
4. Mọi dòng **`[CẦN XÁC NHẬN]`** = chưa viện dẫn cứng cho hồ sơ chính thức.

## Việc anh thường muốn laptop làm tiếp

Ưu tiên theo thứ tự (chỉ hỏi anh nếu xung đột):

1. `git pull` nhánh trên → mở `.docx` + rà các `[CẦN XÁC NHẬN]` trên `vbpl.vn` / Công báo.
2. Đồng bộ bản chốt sang OneDrive hub:  
   `%USERPROFILE%\OneDrive\00_AI_TRUNG_TAM_DIEU_HANH\` (không commit secrets/PHI).
3. Nếu anh yêu cầu mở rộng: truy tìm **danh mục dịch vụ sàng lọc BHYT** theo lộ trình NQ 261 (cloud chưa thấy danh mục cuối cùng toàn quốc tại 18/09/2026).

## Quy tắc vận hành (laptop)

- Evidence before claim; verify URL trước khi sửa trạng thái hiệu lực.
- Diff tối thiểu; giữ cấu trúc bảng hiện có.
- Memory: ưu tiên `OWNER_BRAIN.md` + `ACTIVE_PROJECT_CARD.md` ở OneDrive hub; không dump ledger.
- Smart A / bệnh nhân định danh: không lưu PHI vào git/memory.

## Prompt khởi động gợi ý (1 dòng)

> Em đã checkout `cursor/ksk-toan-dan-vbpl-4211`. Hãy đọc `docs/kham-suc-khoe-toan-dan/BAN_GIAO_LAPTOP.md` + báo cáo chính, liệt kê các dòng `[CẦN XÁC NHẬN]`, rồi đề xuất kế hoạch đối chiếu vbpl.vn (không sửa file cho đến khi anh chốt).
