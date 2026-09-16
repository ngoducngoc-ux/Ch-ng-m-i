# IMAGEJ — thẻ khoa học 1 trang (PCT_EPITH QA · trước AUROC)

**Mã:** IMAGEJ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `IMAGEJ-QA-5MIN` · EPI-SA01 · ENDPOINTS · LEAKAGE · ALERT · EQ  
**Dùng khi:** T2 · Ngày 10 · EPI early-window · trước claim AI trên % biểu mô  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + **`MEDIA-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · primary D21 ImageJ **không đổi** · QA trước AUROC · L3/G2 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **QA ImageJ / PCT_EPITH** Precure/Smart A: early-signal trên % biểu mô chỉ đáng tin nếu **ảnh + SOP đo** đủ QA — không train “sớm” bằng PCT D21; không bỏ qua inter-rater; không claim AUROC khi SOP ảnh chưa chuẩn.

**Mở song song:** thẻ này · `IMAGEJ-QA-5MIN` · `EPI-SA01-EARLY-WINDOW` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD`

## QA → giữ / bỏ

| Hạng mục | Vai trò | Giữ hôm nay | Bỏ |
|----------|---------|-------------|-----|
| **Primary \(t^*\)** | D21 · Y = 100% biểu mô ImageJ | Khoá | Đổi primary vì QA drill |
| **Early \(t'\)** | D0 / D3 / D7 | PCT tại \(t'\) nếu SOP OK | PCT_EPITH_D21 làm predictor early |
| **SOP ảnh** | Khoảng cách / ánh sáng / góc | Ghi thiếu nếu CHƯA | Claim đủ QA vì đã drill |
| **Blind / rater** | 2nd rater subset | CÓ\|CHƯA\|N/A | Bỏ inter-rater vì “AI sẽ sửa” |
| **AUROC** | Model sớm | Chỉ sau QA | Train trên PCT lệch đo |
| **Order PEA** | L3 | KHÔNG | Order vì “QA xong trên giấy” |

## Phương trình IMAGEJ

```text
SOP ảnh + (blind/rater)  ≥  trước  AUROC / AI trên PCT_EPITH
PCT_EPITH(D21)  ≠  early predictor
Primary D21 ImageJ  cố định
QA giấy  ≠  order omics / mở L3
```

## Checklist 15′

```text
Thứ: T2 · t*=D21 · t' ôn: D0|D3|D7 — ________
SOP ảnh đủ? CÓ|CHƯA — thiếu: ________
Blinded / 2nd rater subset? CÓ|CHƯA|N/A — ________
PCT_EPITH_D21 = early predictor? KHÔNG — vì: ________
1 rủi ro nếu AI trên % lệch đo: ________
AUROC trước QA? KHÔNG
Order PEA vì QA giấy? KHÔNG
1 việc ≤30′ (IMAGEJ-QA / EPI / EQ-SA01): ________
Đóng Goal / mở L3 vì IMAGEJ? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / IMAGEJ-QA | SOP · rater · trước AUROC |
| `ENDPOINTS-WEEK1-SCIENCE-CARD` | \(t^*\neq Z\) sớm |
| `LEAKAGE-SCIENCE-CARD` | PCT D21 leakage thời gian |
| `ALERT-SCIENCE-CARD` | A = QA ImageJ actionable |
| **`IMAGEJ-EPI-SCIENCE-CARD`** / `IMAGEJ-EPI-5MIN` | Cặp ImageJ×EPI |
| `EQ-SCIENCE-CARD` | Ladder M0–M3 |

## Cấm

- Claim AUROC trên PCT khi ảnh chưa chuẩn SOP  
- Dùng PCT D21 làm “early feature”  
- Order PEA / đóng Goal / mở L3 vì QA giấy  

## Liên kết

`IMAGEJ-QA-5MIN` · `IMAGEJ-EQ-5MIN` · **`IMAGEJ-EPI-SCIENCE-CARD`** · `IMAGEJ-EPI-5MIN` · `EPI-SA01-EARLY-WINDOW` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `ALERT-SCIENCE-CARD` · `EQ-SCIENCE-CARD` · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3` · **`INTERIM-G2-SCIENCE-CARD`** · **`EPI-SCIENCE-CARD`** · **`PB001-SCIENCE-CARD`**
