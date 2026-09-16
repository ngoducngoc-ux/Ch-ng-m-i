# Bridge — Zhou · Nat Med · SA-01 early-signal (1 trang)

**Mã:** EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01-v0.1  
**Ngày:** 2026-09-16  
**Dành cho:** ritual Ngày 02–03 (STREAK ≥3) · ôn lại mọi quý  
**DOI:** Zhou [10.1038/s41586-019-1236-x](https://doi.org/10.1038/s41586-019-1236-x) · Nat Med [10.1038/s41591-019-0414-6](https://doi.org/10.1038/s41591-019-0414-6)  
**Không:** claim Dx · N cohort ≈ N RCT · order omics trước G2

## Ba ý chung (multi-omics / tín hiệu sớm / dọc)

| Ý | Zhou 2019 | Nat Med 2019 | SA-01 (giữ) |
|---|-----------|--------------|-------------|
| **Dọc trong người** | Hồ sơ “khỏe” khác nhau; biến thiên theo thời gian | Profiling lặp (omics + wearable) nhiều năm | \(Z\) D0/D3/D7 trước \(Y_{D21}\) |
| **Sự kiện** | Nhiễm / tiêm làm lệch omics mạnh | “Actionable” gắn quyết định chăm sóc | `clin_event` 0–4 + AE / nhiễm cục bộ |
| **Trước endpoint** | Chữ ký phân tử trước T2D (minh họa cá thể) | Phát hiện tiền lâm sàng → hành động trong cohort | Exploratory M0–M3 → \(Y_{D21}\); primary D21 **không đổi** |

## Phương trình (1 dòng)

```text
Y_D21 ≈ f( Z(D0…D7), clin_event, C ) + [X_mol chỉ sau G2]
t' ∈ {D0,D3,D7} ≪ D21  →  early-signal exploratory (SAP ES)
```

Chi tiết: `LONGITUDINAL-EARLY-SIGNAL-SA01` · `EQ-SA01-early-warning`

## Map thao tác ritual (45′)

| Phút | Việc | Artifact |
|------|------|----------|
| 0–15 | Abstract Nat Med (hoặc Zhou nếu makeup Ngày 02) | Study sheet Nat Med / Zhou |
| 15–30 | 1 hàng actionable → ALERT **hoặc** 1 mã `clin_event` | `NATMED-ACTIONABLE-ALERT-MAP` · `CLIN_EVENT-ZHOU-MAP` |
| 30–35 | Tick DONE log + STREAK | `2026-09-19` hoặc `09-18` |
| 35–45 | 1 câu VDHN vs DOI **hoặc** 1 vignette | MEDIA · vignettes |

## Y tế số / AI (PB-009)

```text
L1: visit + Z + clin_event (REDCap)
L2: export de-ID → M0–M3 (exploratory)
L3: multi-omics X — CLOSED đến G2 data thật
```

Nat Med/Zhou minh họa **logic** L3; Smart A hiện chỉ bắt buộc L1 (+ L2 khi có N).

## Ranh giới cứng

| Được nói | Không được nói |
|----------|----------------|
| Logic dọc + sự kiện + actionable trong nghiên cứu | “Đã phát hiện sớm như Precure press” |
| ALERT nội bộ A1–A4 nháp | App đổi nhánh RCT / Dx thương mại |
| PB-008 bias adherence từ profiling | VAS tốt = sản phẩm làm lành |

## Fill-in (PI — dán log)

```text
Paper hôm nay: Zhou | Nat Med
1 insight:
1 câu hỏi SA-01:
Map: ALERT A__  hoặc  clin_event=__
```

## Liên kết

`PI-SESSION-SCRIPT-STREAK3` · `STUDY-SHEET-NATMED-PEA` · `STUDY-SHEET-ZHOU` · `alignment-map-smart-a.md` · `RITUAL-CARDS-INDEX`
