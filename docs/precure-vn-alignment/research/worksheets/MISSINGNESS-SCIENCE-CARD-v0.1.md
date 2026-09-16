# MISSINGNESS — thẻ khoa học 1 trang (L2 %miss · visit window · trước AUROC)

**Mã:** MISSINGNESS-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `L2-MISSINGNESS-AUDIT` · DEID · LEAKAGE · EQ · SYNTH  
**Dùng khi:** T5 · Q3 #8 · sau DEID · trước AUROC / M0–M3 trên N  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + **`ALERT-SCIENCE-CARD`** + **`HAWTHORNE-SCIENCE-CARD`** + **`MEDIA-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · `--demo` ≠ N · synthetic ≠ BN · L3 CLOSED · PREP ≠ DONE  

## Mục đích

Ôn **cổng chất lượng L2** Precure/Smart A: trước claim early-signal — biết **% miss theo visit** và **window** (vd. D3) đã rõ; QC demo xanh ≠ missingness lâm sàng.

**Mở song song:** thẻ này · `L2-MISSINGNESS-AUDIT` · **`MISSINGNESS-EQ-SCIENCE-CARD`** · `DEID-SCIENCE-CARD` · **`DEID-MISS-SCIENCE-CARD`** · `LEAKAGE-SCIENCE-CARD` · `EQ-SCIENCE-CARD`

## N / miss → giữ / bỏ

| Mục | Vai trò | Giữ hôm nay | Bỏ |
|-----|---------|-------------|-----|
| **N** | Cohort thật vs `--demo` | Ghi rõ nguồn | Coi demo = N site |
| **%miss(visit,Z)** | QC L2 | Audit theo D0/D3/D7 | Điền % giả từ sandbox |
| **Window** | Định nghĩa sớm | DM xác nhận D3=… | Train khi window mơ hồ |
| **Deny-list** | De-ID trước export | Skim DEID | AUROC trước deny/miss |

## Phương trình L2 QC

```text
N thật + %miss(visit,Z) + window rõ  ≥  trước  M0–M3 / AUROC claim
--demo PASS  ≠  missingness lâm sàng
SYN / demo  ≠  BN
```

## Checklist 15′

```text
Thứ: T5 · N: --demo | de-ID site — ________
Visit ôn: D0|D3|D7 · 1 Z: PCT|CFU|VAS|clin_event — ________
%miss (hoặc [chưa N]): ________
Window D3: bắt buộc|D1–D3|[CẦN XÁC NHẬN DM] — ________
QC: redcap_import_qc PASS? CÓ|CHƯA · deny-list? CÓ|CHƯA
AUROC khi miss cao/demo? KHÔNG — vì: ________
1 việc ≤30′ (MISSINGNESS-5MIN / **DEID-MISS-SCIENCE-CARD** / L2 audit 1 ô): ________
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** / L2 audit | %miss · window · trước AUROC |
| `DEID-SCIENCE-CARD` | Deny PHI trước export |
| `LEAKAGE-SCIENCE-CARD` | Timestamp / \(t^*\) ≠ early |
| `SYNTH-SCIENCE-CARD` | Demo ≠ BN |
| `EQ-SCIENCE-CARD` | Ladder M0–M3 sau QC |

## Cấm

- Điền %miss giả từ sandbox như N thật  
- Train M early khi miss D0–D7 chưa audit  
- Mở G2 / đóng Goal vì “QC demo PASS”  

## Liên kết

`L2-MISSINGNESS-AUDIT` · `MISSINGNESS-5MIN` · `MISSINGNESS-EQ-5MIN` · **`MISSINGNESS-EQ-SCIENCE-CARD`** · **`DEID-MISS-SCIENCE-CARD`** · `DEID-MISS-5MIN` · `DEID-SCIENCE-CARD` · `LEAKAGE-SCIENCE-CARD` · `EQ-SCIENCE-CARD` · `SYNTH-SCIENCE-CARD` · `Q3-L2-EXPORT-EARLY-SIGNAL-BRIDGE` · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3`
