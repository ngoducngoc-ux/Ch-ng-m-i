# Pre-analytic — PEA / protein trên mẫu vết thương (SA-01, tương lai)

**Mã:** PRE-ANALYTIC-PEA-SA01-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 05 · Lundberg *NAR* 2011 DOI 10.1093/nar/gkr424  
**Trạng thái:** nháp trước cổng **G2** — **không** order lab / không lấy mẫu omics hiện tại.

## Ba rủi ro pre-analytic (ghi vào daily log 21/09)

| ID | Rủi ro | Hệ quả lên \(X_{\text{mol}}\) | Giảm thiểu (nháp SOP) |
|----|--------|-------------------------------|------------------------|
| R1 | **Phân hủy protein / thời gian room-temp** sau swab/dịch tiết | Bias giảm nồng độ cytokine; tăng missing không ngẫu nhiên | Lấy mẫu chuẩn thời điểm visit; đặt vào buffer/lạnh ≤15′; `[CẦN XÁC NHẬN]` buffer |
| R2 | **Heterogeneity dịch tiết** (vị trí swab, độ ẩm vết, thay băng) | CV cao trong người; khó so sánh D0→D7 | SOP vị trí + ghi `DRESSING_ADH` / thời điểm sau thay băng; PB-008 adherence |
| R3 | **Nhiễm flora da / môi trường** (không phải tín hiệu lành) | Protein “vi sinh” lẫn host response | Kỹ thuật lấy chuẩn; song song `CULTURE_CFU` đã có trong \(Z\) |

## Rủi ro bổ sung (theo dõi)

- **Thể tích / dilution:** PEA Lundberg validate trên serum/plasma — dịch tiết vết thương **chưa** tương đương → cần pilot analytic trước G3.  
- **Hemolysis / máu lẫn** (vết sâu): làm lệch panel — loại mẫu hoặc ghi cờ QC batch.  
- **Freeze–thaw:** tối đa 1 chu kỳ — chain-of-custody trong `SPEC-SA01-BIO`.

## Liên kết Smart A

- Cổng **G3–G5:** `SPEC-SA01-BIO-v0.1-DRAFT.md`  
- Exploratory hiện tại: chỉ \(Z\) REDCap — đúng thứ tự chi phí/bằng chứng.  
- **SA-04:** vật liệu swab/collection → ISO 10993 nếu device mới.

## Việc nhỏ
**Micro-drill 5′:** **`PREANALYTIC-5MIN-MICRO-DRILL`** (T3 · R1–R3)

## Việc nhỏ

- [ ] PI + lab partner: xác nhận matrix phù hợp PEA/Olink trên exudate `[CẦN XÁC NHẬN]`  
- [ ] DM: không thêm form omics REDCap trước G2 pass
