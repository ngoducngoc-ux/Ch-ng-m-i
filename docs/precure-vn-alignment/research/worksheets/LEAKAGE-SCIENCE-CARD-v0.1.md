# Leakage — thẻ khoa học 1 trang (pitfall #1 · sớm–dọc–AI) · refresh v0.1b

**Mã:** LEAKAGE-SCIENCE-CARD-v0.1b · **Ngày:** 2026-09-16  
**Goal:** ACTIVE · STREAK thật vẫn **2 DONE** · EQ bank **CLOSED** · densify ≠ DONE  
**STREAK&lt;3?** Path STREAK3 trước · **`STREAK3-PACK`** · **`STREAK3-EQ`** · NatMed → tick **19/09** · dừng OPENER/stack  
**STREAK≥3?** **`AFTER-STREAK3-OPENER`** → 1×EQ sibling → **`DAILY-STACK`** · bridges #0–14  
**Không:** agent tick DONE · UpdateGoal complete trên PREP/densify · invent EQ · densify = DONE · PHI vào git  
**Neo:** NATMED (refresh v0.1b) · ENDPOINTS · EQ · PITFALLS  
**Dùng khi:** EQ T2/T4/T6 · Ngày 20 pitfalls · Q3 L2 · sau STREAK≥3  
**Hub:** `NATMED-STREAK3-SCIENCE-CARD` (refresh v0.1b) · tip tiếp `ENDPOINTS-WEEK1-SCIENCE-CARD` · Drive keep `1Vjchf1i…`  

```text
STREAK <3? → STREAK3 (PI-NEXT) · densify ≠ DONE
        ↓ STREAK ≥3
OPENER → EQ sibling → DAILY-STACK · ritual theo Ngày N
```

## Mục đích

Ôn **leakage thời gian** — lỗi #1 khi làm early-signal Precure/Smart A: predictor nhìn \(Y\) hoặc timestamp ≥ \(t^*\) thì “AUROC đẹp” **không** phải phát hiện sớm; densify ≠ “đã chống leakage”.

**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · HAWTHORNE · MEDIA · FILL-AID → tick **19/09** trước  

**Mở song song:** thẻ này · `LEAKAGE-CROSS-SA-ATLAS` · `ENDPOINTS-WEEK1-SCIENCE-CARD` · `LEAK-CROSS-5MIN` · **`LEAK-CROSS-SCIENCE-CARD`** · **`NATMED-STREAK3-SCIENCE-CARD`**

## Ba SA → ba hình thái (giữ / bỏ)

| SA | \(t^*\) | Leakage điển hình | Giữ (early đúng) | Bỏ |
|----|---------|-------------------|------------------|-----|
| **01** | D21 | PCT D21 / `clin_event` mã hoá từ \(Y_{D21}\) | \(Z\)/`clin_event` chỉ \(t'\le D7\) | Feature ≥ \(t^*\) trong M0–M3 |
| **02** | D3 | M1 sandbox gồm `VAS_D3` ≈ định nghĩa \(Y\) | Ritual: D1/`CFU` trước; M1\* ≠ chính \(Y\) | Báo AUROC M1 synthetic = lâm sàng |
| **05** | D14 | PUSH_D14 / component sau \(t'\) làm “early” | \(t'\le D7\); ALERT ≠ Dx ICU | Auto-treat / gộp với D21 |
| **Agent densify** | Anti-forget · hub wire | ≠ “Smart A không leakage” / G2 |

## Phương trình nhắc

```text
Early hợp lệ:   feature timestamp t' ≪ t*
Leakage:        feature ≥ t*  OR  feature ≈ định nghĩa Y  OR  nhìn tương lai
verify.sh PASS ≠ “đã chứng minh early-signal”
X_mol / G2: CLOSED  — leakage sandbox không mở omics
Ôn LEAKAGE / densify  ≠  leakage-free  ≠  DONE
```

## Checklist 15′ (1 SA theo EQ rotation)

```text
Thứ: T2|T4|T6|STREAK3 · SA: 01|02|05 — chọn: ________
t* / Y: ________
1 feature SẼ leakage nếu vào M early: ________
Vì sao (thời gian / trùng Y / sau t*): ________
1 feature HỢP LỆ cho t' hôm nay: ________
1 câu cấm claim từ sandbox: ________
Densify = “đã chống leakage”? KHÔNG
1 việc ≤30′ (LEAKAGE-5MIN / ENDPOINTS / EQ / SYNTH): ________
Đóng Goal / mở G2 vì atlas? KHÔNG
```

## Y tế số / AI (3 câu kiểm)

| Trụ | Kiểm |
|-----|------|
| **Sớm** | Feature có timestamp &lt; \(t^*\) trên eCRF? |
| **Dọc** | Visit–ID–time đủ để chứng minh không nhìn tương lai? |
| **AI** | Export de-ID + deny-list trước train? · TRIPOD |

Cặp: `YTESO-EARLY-SIGNAL-SCIENCE-CARD` · tip tiếp **`ENDPOINTS-WEEK1-SCIENCE-CARD`** · `DESIGN-WEEK1-SCIENCE-CARD` (TRIPOD #1)

## Cấm

- Coi atlas/PREP/densify = STREAK DONE · dùng leakage sandbox mở G2  
- Một câu “Smart A không leakage” cho cả 3 SA  
- Agent tick DONE · đóng Goal / invent EQ  

## Liên kết

`LEAKAGE-CROSS-SA-ATLAS` · tip tiếp **`ENDPOINTS-WEEK1-SCIENCE-CARD`** · `LEAKAGE-5MIN` · `LEAK-CROSS-5MIN` · **`LEAK-CROSS-SCIENCE-CARD`** · **`VAS-LEAK-SCIENCE-CARD`** · `VAS-LEAK-5MIN` · `PITFALLS-5MIN` · **`NATMED-STREAK3-SCIENCE-CARD`** · `EQ-SA01|02|05` · **`EQ-SCIENCE-CARD`** · **`SYNTH-SCIENCE-CARD`** · **`MISSINGNESS-SCIENCE-CARD`** · **`TRIPOD-SCIENCE-CARD`** · **`LEAKAGE-EQ-SCIENCE-CARD`** · `SCIENCE-CARDS-INDEX` · `DAILY-STACK-AFTER-STREAK3` · **`SAP-ES-SCIENCE-CARD`** · **`PITFALLS-SCIENCE-CARD`** · **`IMAGEJ-SCIENCE-CARD`** · **`EPI-SCIENCE-CARD`** · **`PB002-SCIENCE-CARD`** · `STREAK3-PACK-SCIENCE-CARD` · Drive keep `1Vjchf1i…` · PREP≠DONE · densify≠DONE  
