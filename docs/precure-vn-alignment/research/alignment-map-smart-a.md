# Alignment map — Precure logic × Chương trình Smart A

Ngôn ngữ: khoa học trung tính. Precure = **tham chiếu mô hình**, không phải đối tác thương mại của đề tài.

## Logic Precure (rút gọn vận hành)

```
Trạng thái khỏe → biến đổi phân tử sớm → tín hiệu phát hiện được
        ↑ dữ liệu dọc lâm sàng + omics
        ↑ AI/pattern ở quy mô lớn
        ↓
Chẩn đoán sớm hơn / đích điều trị rõ hơn / chăm sóc cá thể hóa hơn
(trong khuôn khổ bằng chứng & đạo đức nghiên cứu)
```

**Bridge DOI → SA-01 (1 trang):** `worksheets/EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01-v0.1.md`  
(Zhou *Nature* 2019 · Nat Med 2019 · \(Z\)/`clin_event`/M0–M3 · L3 gated)

## Ánh xạ đề tài SA

| Đề tài | Endpoint / đặc điểm hiện có | Góc lệch hướng kiểu Precure (câu hỏi nghiên cứu) |
|--------|-----------------------------|---------------------------------------------------|
| **SA-01** | RCT vết thương/bỏng; primary D21 biểu mô hóa; N=120 | Có tín hiệu phân tử/vi môi trường vết thương nào **trước** mốc lâm sàng D21 dự báo lành chậm? Cần lớp nào (protein cục bộ, viêm, microbiome) + thời điểm lấy mẫu? |
| **SA-02** | RCT hô hấp trên/khoang miệng-họng; VAS D3; N=100 | Triệu chứng VAS có trễ so với marker viêm/miễn dịch niêm mạc không? Có thể định nghĩa “tín hiệu sớm đáp ứng điều trị” trước D3? |
| **SA-03** | In-vitro biofilm/ATCC (không RCT) | Mô hình biofilm như proxy “giai đoạn sớm” trước biểu hiện lâm sàng nhiễm trùng; liên hệ proteomics/kháng biofilm với tín hiệu chuyển pha. |
| **SA-04** | Độc học ISO 10993 tiền lâm sàng | An toàn vật liệu là điều kiện tiên quyết trước mọi pipeline “early detection / device-linked diagnostics”; giữ cửa ISO trước khi mở rộng omics người. |
| **SA-05** | RCT loét tỳ đè ICU; PUSH D14; N=80 | Loét tỳ đè: tín hiệu sớm (vi tuần hoàn, viêm, proteomics dịch tiết) trước khi PUSH xấu đi? Thiết kế lấy mẫu dọc trong ICU có khả thi không? |

## Cầu nối y tế số VN (VDHN)

- Chuẩn hóa dữ liệu lâm sàng dọc + đồng thuận / khử định danh.
- AI chỉ sau khi có **câu hỏi sinh học rõ** và kế hoạch xác thực (không AI-first rỗng).
- Truyền thông: luôn ghi nguồn VDHN khi dùng bản tin Precure; tránh ngôn ngữ “diệt 100% / an toàn tuyệt đối”.

## Ưu tiên học kỹ thuật (12 tháng)

1. Longitudinal clinical design + missingness → `DESIGN-SA01` · `LONGITUDINAL-EARLY-SIGNAL-SA01-v0.1.md` · **bridge Zhou/Nat Med**
2. Proteomics discovery vs targeted (Olink-class thinking; không bắt buộc cùng platform) → PEA worksheets
3. Multi-omics integration pitfalls → `guides/ML-OMICS-PITFALLS-v0.1.md` · **`guides/MULTI-OMICS-GATES-SMART-A-v0.1.md`**
4. Translational path → SPIRIT/CONSORT/TT43 · **`guides/AI-LONGITUDINAL-STACK-v0.1.md`** · months 4–12 card

## Phương trình & stack

- `equations/EQ-SA01|02|05-early-warning-v0.1.md` · `problem-bank.md` PB-001…009  
- Ritual: `EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01` · `RITUAL-CARDS-INDEX`
