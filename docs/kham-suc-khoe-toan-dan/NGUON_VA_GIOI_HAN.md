# Nguồn, provenance và giới hạn

**Mốc rà soát:** 18/09/2026  
**Chủ sở hữu yêu cầu:** PGS.TS.BS. Ngô Đức Ngọc  
**Repo:** `github.com/ngoducngoc-ux/Ch-ng-m-i`

## Chuỗi agent

| Vai trò | Agent | Trạng thái khi bàn giao |
|---------|-------|-------------------------|
| Project gốc | [Khám sức khỏe toàn dân](https://cursor.com/agents/bc-157e8466-5d5a-4663-b8bc-8fd839fd06ca) | IDLE — đã giao nhiệm vụ thu thập VBPL |
| Thu thập + soạn báo cáo chính | [Thu thập văn bản pháp luật](https://cursor.com/agents/bc-9fcc51bc-dcc5-5e8e-807f-957b6c2ec823) | Có deliverable trong store riêng; bản MD/DOCX được khôi phục từ transcript và đẩy vào git |
| Phụ lục luật + BHYT | [Rà luật và BHYT](https://cursor.com/agents/bc-847f2cc4-098f-56eb-97f9-e2d6f0ffcdd1) | IDLE — hoàn tất |
| Phụ lục dân số đặc thù | [Rà nhóm dân số đặc thù](https://cursor.com/agents/bc-9911b652-ca2b-526d-9a50-63109c996fa0) | IDLE — hoàn tất |
| Phụ lục lao động | Agent gốc treo transcript rỗng; bổ sung bởi cloud worker | Đã ghi `03-lao-dong-va-ksk.md` |
| Phụ lục chương trình/sàng lọc | Agent gốc treo transcript rỗng; bổ sung bởi cloud worker | Đã ghi `04-chuong-trinh-va-sang-loc.md` |
| Đóng gói bàn giao laptop | [Kết quả cho cursor](https://cursor.com/agents/bc-01a0b51b-0c5d-7509-b3e1-48b2ca3d4211) | Agent này |

## Phương pháp

- Ưu tiên URL chính thức: `vbpl.vn`, `vanban.chinhphu.vn`, `congbao.chinhphu.vn`, cổng Tư liệu Đảng (với NQ TW).
- Không bịa số hiệu / ngày / hiệu lực / URL.
- Điểm chưa chứng minh được ghi **[CẦN XÁC NHẬN]** hoặc tách sang bảng lịch sử.
- Báo cáo chính khôi phục từ transcript (read + các edit tuần tự sau khi file gốc chỉ nằm trong store agent khác, không chia sẻ cross-VM).

## Giới hạn đã biết

- Không liệt kê văn bản triển khai cấp tỉnh/ngành/đơn vị.
- Không trích nguyên văn dài (bản quyền); chỉ tóm tắt + điều khoản + link.
- Một số agent phụ (lao động / chương trình) bản gốc cloud bị treo không sinh transcript — phụ lục tương ứng được làm lại độc lập và cần anh/laptop rà nhanh nếu dùng cho hồ sơ chính thức.
- Danh mục dịch vụ sàng lọc BHYT “cuối cùng toàn quốc” theo lộ trình NQ 261: **chưa thấy** tại thời điểm rà soát.
