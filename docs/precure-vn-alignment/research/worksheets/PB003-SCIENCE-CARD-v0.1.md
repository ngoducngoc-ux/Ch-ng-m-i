# PB003 — thẻ khoa học 1 trang (SA-05 early alert trước PUSH xấu)

**Mã:** PB003-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `EQ-SA05` · PUSH-SA05-COMPONENTS · ALERT · L1L2L3 · PB001 · PB002 · CROSS-SA  
**Dùng khi:** T6/CN · STREAK3 · bridge #4|#8 · PB lens #13 hàng 003 · trước claim “đã có early-signal SA-05”  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + **`MEDIA-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · support SA-05 · primary ΔPUSH D14 không đổi · \(X\) CLOSED · không gộp \(Y\) · không auto-treat ICU · PREP ≠ DONE  

## Mục đích

Ôn **PB-003**: cửa sổ cảnh báo **trước** PUSH tăng hạng (exudate/TURN/`clin_event`) — **exploratory**; không đổi primary; không deploy ALERT ICU; không order omics. Khác **`ALERT-SCIENCE-CARD`** (A/C/B actionable≠Dx) — thẻ này giữ câu hỏi support SA-05 / early window trước \(Y_{D14}\).

**Mở song song:** thẻ này · `EQ-SA05` · `PUSH-SA05-COMPONENTS` · `ALERT-SCIENCE-CARD` · `PB002-SCIENCE-CARD`

## \(Y\)/\(Z\)/\(X\) → giữ / bỏ

| Thành phần | Vai trò support | Giữ hôm nay | Bỏ |
|------------|-----------------|-------------|-----|
| **\(Y(t^*)\)** | ΔPUSH D14 | Primary không đổi | Đổi primary vì ES |
| **\(t'\)** | D0 / D3 / D7 · exudate · TURN | Trước PUSH_D14 | PUSH_D14 làm “early” |
| **\(Z\)** | exudate / TURN_ADHERE / Braden / `clin_event` | 1 ứng viên + chuỗi | Snapshot đơn = đủ |
| **Component PUSH** | Subscore chăm sóc | ≠ co-primary | Component = primary |
| **ALERT B** | Nội bộ exploratory | ≠ app ICU / auto-treat | Deploy vì đã điền PB-003 |
| **\(X_{\text{mol}}\)** | Omics ICU | **CLOSED** | Order vì drill |
| **Gộp \(Y\)** | Cross-SA | **KHÔNG** với SA-01/02 | Train chung |

## Phương trình PB-003

```text
Z(t') trước PUSH xấu  ?⇒  cửa sổ cảnh báo  (exploratory)
Support = SA-05  ·  primary ΔPUSH D14 cố định  ·  X CLOSED
ALERT B  ≠  app ICU  ≠  co-primary  ≠  auto-treat
Gộp Y với SA-01/02  =  CẤM
AUROC sandbox  ≠  BN evidence  ≠  đóng PB-003
```

## Checklist 15′

```text
Thứ: T6|CN · Support SA-05 (không cờ đầu)? ĐÚNG
Y(t*): ΔPUSH D14? ĐÚNG
t' hôm nay: D0|D3|D7|exudate|TURN (không PUSH_D14) — ________
1 Z: exudate|TURN_ADHERE|Braden|clin_event — ________
X_mol CLOSED vì: ________
Component = co-primary? KHÔNG · ALERT B deploy ICU? KHÔNG
Gộp Y với SA-01/02? KHÔNG
Order omics / đóng Goal vì PB-003? KHÔNG
1 việc ≤30′ (EQ/PUSH/ALERT/L1L2L3): ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / EQ-SA05 | Early window trước PUSH · PB-003 |
| `ALERT-SCIENCE-CARD` | Actionable ≠ Dx · A/C/B |
| `PUSH-SA05-COMPONENTS` | Subscore ≠ co-primary |
| `PB001-SCIENCE-CARD` | Cờ đầu SA-01 |
| `PB002-SCIENCE-CARD` | SA-02 vs VAS |
| `CROSS-SA-SCIENCE-CARD` | Schema · không gộp Y |
| `L1L2L3-SCIENCE-CARD` | Cổng tầng |

## Cấm

- PUSH_D14 làm “early” predictor  
- Component / ALERT = co-primary hoặc app ICU  
- AUROC sandbox = bằng chứng BN / đóng PB-003  
- Gộp endpoint SA-01/02 · order \(X\) vì đã điền PB-003  

## Liên kết

`problem-bank` PB-003 · `EQ-SA05` · `PB003-5MIN` · `PB003-EQ-5MIN` · `PUSH-SA05-COMPONENTS` · `ALERT-SCIENCE-CARD` · `L1L2L3-SCIENCE-CARD` · `PB001-SCIENCE-CARD` · `PB002-SCIENCE-CARD` · `CROSS-SA-SCIENCE-CARD` · **`PB003-EQ-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3` · **`PB007-SCIENCE-CARD`**
