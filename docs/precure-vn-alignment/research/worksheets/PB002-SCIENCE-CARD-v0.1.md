# PB002 — thẻ khoa học 1 trang (SA-02 early biological vs VAS)

**Mã:** PB002-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `EQ-SA02` · VAS-SCALE-HARMONIZE · LEAKAGE · ENDPOINTS · PB001 · CROSS-SA  
**Dùng khi:** T4/CN · STREAK3 · bridge #2 · PB lens #13 hàng 002 · trước claim “đã có early-signal SA-02”  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + **`MEDIA-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · support SA-02 · primary ΔVAS D3 không đổi · \(X\) CLOSED · không gộp \(Y\) · synthetic ≠ BN · PREP ≠ DONE  

## Mục đích

Ôn **PB-002**: ΔVAS D0→D3 có đồng bộ marker/\(Z\) sớm không — **exploratory**; không đổi primary; không gộp \(Y\) với SA-01/05; không order omics. Khác **`ENDPOINTS-WEEK1-SCIENCE-CARD`** (khung \(t^*\neq Z\)) — thẻ này giữ câu hỏi support SA-02 / biological vs symptom lag.

**Mở song song:** thẻ này · `EQ-SA02` · `VAS-SCALE-HARMONIZE-SA02` · `LEAKAGE-SCIENCE-CARD` · `PB001-SCIENCE-CARD`

## \(Y\)/\(Z\)/\(X\) → giữ / bỏ

| Thành phần | Vai trò support | Giữ hôm nay | Bỏ |
|------------|-----------------|-------------|-----|
| **\(Y(t^*)\)** | ΔVAS D3 / VAS_D3 | Primary không đổi | Đổi primary vì ES |
| **\(t'\)** | D0 / D1 / CFU_D0 | Trước VAS_D3 | VAS_D3 làm “early” predictor |
| **\(Z\)** | VAS_D0/D1 · CFU · fever_clear · throat_score | 1 ứng viên + chuỗi | Snapshot đơn = đủ |
| **Marker / \(X\)** | Niêm mạc / omics | **CLOSED** | Order vì đã điền PB-002 |
| **Gộp \(Y\)** | Cross-SA | **KHÔNG** với SA-01/05 | Train chung / gộp endpoint |
| **Thang VAS** | Harmonize eCRF | Giữ scale đã chốt | Đổi 0–10↔0–100 vì STPIS |

## Phương trình PB-002

```text
Z(t') sớm  ? đồng bộ  ΔVAS D0→D3  (exploratory · symptom có thể trễ)
Support = SA-02  ·  primary ΔVAS D3 cố định  ·  X CLOSED
Gộp Y với SA-01/05  =  CẤM
AUROC sandbox  ≠  BN evidence  ≠  đóng PB-002
```

## Checklist 15′

```text
Thứ: T4|CN · Support SA-02 (không cờ đầu)? ĐÚNG
Y(t*): ΔVAS D3? ĐÚNG
t' hôm nay: D0|D1|CFU_D0 (không VAS_D3) — ________
1 Z: VAS_D0/D1|CFU|fever_clear|throat_score — ________
X_mol CLOSED vì: ________
Gộp Y với SA-01/05? KHÔNG
Order omics / đóng Goal vì PB-002? KHÔNG
1 việc ≤30′ (EQ/VAS/LEAKAGE/SYNTH): ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / EQ-SA02 | Biological vs VAS · PB-002 |
| `ENDPOINTS-WEEK1-SCIENCE-CARD` | \(t^*\neq Z\) sớm |
| `LEAKAGE-SCIENCE-CARD` | Pitfall thời gian |
| `PB001-SCIENCE-CARD` | Cờ đầu SA-01 |
| `CROSS-SA-SCIENCE-CARD` | Schema · không gộp Y |
| `SYNTH-SCIENCE-CARD` | Sandbox ≠ BN |

## Cấm

- VAS_D3 làm “early” predictor  
- Đổi eCRF 0–10 → 0–100 vì STPIS  
- AUROC sandbox = bằng chứng BN / đóng PB-002  
- Gộp endpoint SA-01/05 · order \(X\) vì đã điền PB-002  

## Liên kết

`problem-bank` PB-002 · `EQ-SA02` · `PB002-5MIN` · `PB002-EQ-5MIN` · `VAS-SCALE-HARMONIZE-SA02` · `LEAKAGE-SCIENCE-CARD` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `PB001-SCIENCE-CARD` · `CROSS-SA-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3` · **`PB003-SCIENCE-CARD`** · **`PB007-SCIENCE-CARD`**
