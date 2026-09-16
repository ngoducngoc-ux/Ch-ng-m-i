# Nat Med “actionable” → ALERT SA-01 (nội bộ nghiên cứu)

**Mã:** NATMED-ACTIONABLE-ALERT-MAP-v0.1  
**Ngày:** 2026-09-16  
**Curriculum:** Ngày 03 (Nat Med) · ôn lại Ngày 32  
**Dùng với:** `STUDY-SHEET-NATMED-PEA` · `ALERT-SA01-v0.1.md` · `MEDIA-SMART-A-CLAIMS-v0.1.md`  
**Không:** thiết bị Dx · auto-treat · claim sản phẩm Precure.LLC

## Mục đích (15′)

Đọc abstract Nat Med 2019 rồi **map 1 khái niệm “clinically actionable”** sang 1 alert nội bộ SA-01 — đủ để tick DONE log `2026-09-19.md` mà không overclaim.

**DOI:** [10.1038/s41591-019-0414-6](https://doi.org/10.1038/s41591-019-0414-6)

## Bảng map (chọn 1 hàng khi ritual)

| Nat Med (ý paper) | Analog Smart A (giữ) | ALERT SA-01 | Không suy diễn |
|-------------------|----------------------|-------------|----------------|
| Phát hiện tiền lâm sàng → hành động chăm sóc trong cohort | Tín hiệu sớm trên \(Z\) dọc trước \(Y_{D21}\) | **A1** PCT_EPITH đứng + CFU không giảm → hội chẩn / cấy lại SOP | N=109 ≈ N=120; “đã phát hiện sớm như Precure press” |
| Insight gắn quyết định lâm sàng (không chỉ dashboard) | ALERT nội bộ có **hành động** rõ | **A2** VAS↑ + AE_LOCAL → đánh giá AE / Ch.7 | App bệnh nhân tự đổi nhánh RCT |
| Profiling lặp → đổi lifestyle (hiệu ứng tham gia) | **PB-008** adherence / VAS bias | Ghi confounder; không gán “điều trị hiệu quả” | Press “sản phẩm làm lành vì VAS tốt” |
| Sự kiện / chuyển trạng thái khỏe→bệnh | `clin_event` + quỹ đạo PCT | **A3** PCT lùi D0→D7 · **A4** CLIN_EVENT + PCT đứng | Train AI cá thể từ 1 event giả |

Ngưỡng số trong ALERT là **nháp** — chốt sau pilot/`[CẦN XÁC NHẬN]`.

## Một câu press vs DOI (copy vào log Ngày 03 / 26)

> VDHN/Precure.LLC mô tả **tầm nhìn** multi-omics + AI nhận diện tín hiệu sớm; Smart A SA-01 hiện chỉ có ALERT **nội bộ nghiên cứu** trên \(Z\) REDCap (A1–A4) — DOI Nat Med minh họa logic “actionable trong cohort”, **không** chứng minh sản phẩm Dx đã sẵn sàng.

Nguồn press: `sources/2026-precure-mayo-thermo-vdhn.md` · bảng claim: `MEDIA-SMART-A-CLAIMS-v0.1.md`

## Checklist DONE (PI)

- [ ] Đã mở abstract / study sheet Nat Med  
- [ ] Chọn **1 hàng** bảng map → ghi ≤2 dòng vào insight log `2026-09-19.md`  
- [ ] 1 câu hỏi SA-01 (cadence D0–D7 **hoặc** “actionable” trước D21)  
- [ ] (Tuỳ chọn 10′) dán 1 câu press vs DOI ở trên vào “Việc nhỏ”  
- [ ] Tick **DONE** + `STREAK_TRACKER.md` — **không** order omics / không đóng Goal

## Stack nhắc

L1 \(Z\) REDCap + ALERT → L2 M0–M3 exploratory → L3 \(X\) PEA **CLOSED** đến G2 thật.  
`guides/AI-LONGITUDINAL-STACK-v0.1.md` · `MULTI-OMICS-GATES-SMART-A-v0.1.md`

## Liên kết

- Notes: `reading-notes/2026-09-19-natmed-longitudinal-precision-health.md`  
- PB-008: `PB-008-participation-effects-v0.1.md`  
- Design dọc: `hypotheses/DESIGN-SA01-minimal-longitudinal-v0.1.md`  
- Ritual: `../../PI-NEXT-45MIN.md`
