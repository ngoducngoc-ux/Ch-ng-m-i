# Bridge — Zhou · Nat Med · SA-01 early-signal (1 trang) · refresh v0.1b

**Mã:** EARLY-SIGNAL-BRIDGE-ZHOU-NATMED-SA01-v0.1  
**Ngày:** 2026-09-16 (refresh sau BRIDGE-ROTATION / EQ bank CLOSED)  
**Curriculum:** ritual Ngày 02–03 · T2 rotation · ôn lại mọi quý · bridge **#0**  
**DOI:** Zhou [10.1038/s41586-019-1236-x](https://doi.org/10.1038/s41586-019-1236-x) · Nat Med [10.1038/s41591-019-0414-6](https://doi.org/10.1038/s41591-019-0414-6)  
**Thẻ:** `NATMED-STREAK3` · `ZHOU-STREAK3` · `EQ-SIBLING-MAP` · `BRIDGE-ROTATION` (T2) · `ALERT` · `CLIN_EVENT`  
**Cờ đầu:** SA-01 · Goal **ACTIVE** · L3 **CLOSED** trừ G2 · EQ bank **CLOSED**  
**STREAK&lt;3?** Dừng · **`STREAK3-PACK`** · **`STREAK3-EQ`** · **`NATMED-STREAK3`** · FILL-AID → tick **19/09** trước  
**Không:** claim Dx · N cohort ≈ N RCT · order omics trước G2 · invent EQ mới · UpdateGoal trên PREP

## Ba ý chung (multi-omics / tín hiệu sớm / dọc)

| Ý | Zhou 2019 | Nat Med 2019 | SA-01 (giữ) |
|---|-----------|--------------|-------------|
| **Dọc trong người** | Hồ sơ “khỏe” khác nhau; biến thiên theo thời gian | Profiling lặp (omics + wearable) nhiều năm | \(Z\) D0/D3/D7 trước \(Y_{D21}\) |
| **Sự kiện** | Nhiễm / tiêm làm lệch omics mạnh | “Actionable” gắn quyết định chăm sóc | `clin_event` 0–4 + AE / nhiễm cục bộ |
| **Trước endpoint** | Chữ ký phân tử trước T2D (minh họa cá thể) | Phát hiện tiền lâm sàng → hành động trong cohort | Exploratory M0–M3 → \(Y_{D21}\); primary D21 **không đổi** |

Ôn #0 = neo ba trụ **phát hiện sớm–dọc–AI** cho Smart A — đúng mục tiêu ritual hàng ngày.

## Phương trình (1 dòng)

```text
Y_D21 ≈ f( Z(D0…D7), clin_event, C ) + [X_mol chỉ sau G2]
t' ∈ {D0,D3,D7} ≪ D21  →  early-signal exploratory (SAP ES)
```

Chi tiết: `LONGITUDINAL-EARLY-SIGNAL-SA01` · `EQ-SA01-early-warning` · **`EQ-M0M3`** / **`PB001-EQ`**

## Luồng một trang (STREAK≥3 · T2 / Ngày 02–03)

```text
STREAK <3? → STREAK3-PACK / STREAK3-EQ / NATMED-STREAK3 · dừng #0 “đủ”
        ↓ STREAK ≥3
OPENER (phiên đầu) → 1×EQ sibling (map) → #0 bridge
0–15′ Abstract Nat Med (hoặc Zhou makeup) · thẻ NATMED/ZHOU-STREAK3
15–30′ 1 hàng ALERT A1–A4 nháp · hoặc 1 mã clin_event
30–45′ 1 insight + 1 câu lệch hướng Smart A · tick DONE chỉ PI
Goal ACTIVE · G2 CLOSED · PREP ≠ DONE
```

## Map thao tác ritual (45′)

| Phút | Việc | Artifact |
|------|------|----------|
| 0–15 | Abstract Nat Med (hoặc Zhou nếu makeup Ngày 02) | Study sheet · **`NATMED-STREAK3-SCIENCE-CARD`** / **`ZHOU-STREAK3-SCIENCE-CARD`** |
| 15–30 | 1 hàng actionable → ALERT **hoặc** 1 mã `clin_event` | `NATMED-ACTIONABLE-ALERT-MAP` · `CLIN_EVENT-ZHOU-MAP` · **`ALERT-EQ`** / **`CLIN_EVENT-EQ`** |
| 30–35 | Tick DONE log + STREAK (chỉ PI) | `2026-09-19` hoặc makeup `09-18` |
| 35–45 | 1 câu VDHN vs DOI **hoặc** 1 vignette | MEDIA · **`SHIFT-EQ`** · vignettes |

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
STREAK ≥3? ________ (nếu không → STREAK3 path)
Paper hôm nay: Zhou | Nat Med
EQ sibling kèm (1): ________
1 insight:
1 câu hỏi SA-01 / lệch hướng:
Map: ALERT A__  hoặc  clin_event=__
G2: CLOSED · Goal: ACTIVE · densify ≠ DONE
```

## Liên kết

`PI-SESSION-SCRIPT-STREAK3` · **`STREAK3-PACK-SCIENCE-CARD`** · **`STREAK3-EQ-SCIENCE-CARD`** · **`NATMED-STREAK3-SCIENCE-CARD`** · **`ZHOU-STREAK3-SCIENCE-CARD`** · **`AFTER-STREAK3-OPENER-1PAGE`** · **`BRIDGE-ROTATION`** (T2=#0) · **`EQ-SIBLING-MAP-SCIENCE-CARD`** · **`SCIENCE-BRIDGES-SCIENCE-CARD`** · **`PB001-EQ-SCIENCE-CARD`** · **`EQ-M0M3-SCIENCE-CARD`** · **`ALERT-EQ-SCIENCE-CARD`** · **`CLIN_EVENT-EQ-SCIENCE-CARD`** · `STUDY-SHEET-NATMED-PEA` · `STUDY-SHEET-ZHOU` · `alignment-map-smart-a.md` · `SCIENCE-CARDS-INDEX` · `RITUAL-CARDS-INDEX` · `#1` MULTI-OMICS-PEA
