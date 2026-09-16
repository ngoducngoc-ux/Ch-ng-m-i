# Leakage — thẻ khoa học 1 trang (pitfall #1 · sớm–dọc–AI)

**Mã:** LEAKAGE-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** EQ T2/T4/T6 · Ngày 20 pitfalls · Q3 L2 · sau STREAK≥3  
**Ưu tiên STREAK&lt;3:** **`NATMED-STREAK3-SCIENCE-CARD`** + FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · G2/L3 **CLOSED** · sandbox ≠ BN · PREP ≠ DONE  

## Mục đích

Ôn **leakage thời gian** — lỗi #1 khi làm early-signal Precure/Smart A: predictor nhìn \(Y\) hoặc timestamp ≥ \(t^*\) thì “AUROC đẹp” **không** phải phát hiện sớm.

**Mở song song:** thẻ này · `LEAKAGE-CROSS-SA-ATLAS` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `LEAK-CROSS-5MIN`

## Ba SA → ba hình thái (giữ / bỏ)

| SA | \(t^*\) | Leakage điển hình | Giữ (early đúng) | Bỏ |
|----|---------|-------------------|------------------|-----|
| **01** | D21 | PCT D21 / `clin_event` mã hoá từ \(Y_{D21}\) | \(Z\)/`clin_event` chỉ \(t'\le D7\) | Feature ≥ \(t^*\) trong M0–M3 |
| **02** | D3 | M1 sandbox gồm `VAS_D3` ≈ định nghĩa \(Y\) | Ritual: D1/`CFU` trước; M1\* ≠ chính \(Y\) | Báo AUROC M1 synthetic = lâm sàng |
| **05** | D14 | PUSH_D14 / component sau \(t'\) làm “early” | \(t'\le D7\); ALERT ≠ Dx ICU | Auto-treat / gộp với D21 |

## Phương trình nhắc

```text
Early hợp lệ:   feature timestamp t' ≪ t*
Leakage:        feature ≥ t*  OR  feature ≈ định nghĩa Y  OR  nhìn tương lai
verify.sh PASS ≠ “đã chứng minh early-signal”
X_mol / G2: CLOSED  — leakage sandbox không mở omics
```

## Checklist 15′ (1 SA theo EQ rotation)

```text
Thứ: T2|T4|T6 · SA: 01|02|05 — chọn: ________
t* / Y: ________
1 feature SẼ leakage nếu vào M early: ________
Vì sao (thời gian / trùng Y / sau t*): ________
1 feature HỢP LỆ cho t' hôm nay: ________
1 câu cấm claim từ sandbox: ________
```

## Y tế số / AI (3 câu kiểm)

| Trụ | Kiểm |
|-----|------|
| **Sớm** | Feature có timestamp &lt; \(t^*\) trên eCRF? |
| **Dọc** | Visit–ID–time đủ để chứng minh không nhìn tương lai? |
| **AI** | Export de-ID + deny-list trước train? · TRIPOD |

Cặp: `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · `DESIGN-WEEK1-SCIENCE-CARD` (TRIPOD #1)

## Cấm

- Coi atlas/PREP = STREAK DONE · dùng leakage sandbox mở G2  
- Một câu “Smart A không leakage” cho cả 3 SA  
- Agent tick DONE · đóng Goal  

## Liên kết

`LEAKAGE-CROSS-SA-ATLAS` · `LEAKAGE-5MIN` · `LEAK-CROSS-5MIN` · `VAS-LEAK-5MIN` · `PITFALLS-5MIN` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `EQ-SA01|02|05` · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3`
