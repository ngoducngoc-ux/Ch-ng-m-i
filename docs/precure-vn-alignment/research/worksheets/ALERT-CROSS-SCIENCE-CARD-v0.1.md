# ALERT-CROSS — thẻ khoa học 1 trang (actionable × schema · ≠ Dx · không gộp \(Y\))

**Mã:** ALERT-CROSS-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `ALERT-CROSS-5MIN-MICRO-DRILL` · ALERT-SCIENCE-CARD · CROSS-SA-SCIENCE-CARD · ALERT-CROSS-SA-ATLAS · NatMed  
**DOI:** Nat Med 2019 [10.1038/s41591-019-0414-6](https://doi.org/10.1038/s41591-019-0414-6)  
**Dùng khi:** STREAK≥3 · Daily stack **T2 / T4 / T6 / CN** · trước deploy “app cảnh báo Smart A chung” · cặp ALERT×CROSS-SA  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · **`ALERT-SCIENCE-CARD`** · HAWTHORNE · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · ALERT nội bộ theo SA · ≠ Dx · mỗi SA một \(Y\) · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp ALERT×CROSS**: 1 hàng ALERT (A/C/B) **theo SA** + so schema \(t^*\)/\(Z\) — không gộp \(Y\) · không deploy app Dx · Hawthorne/ALERT ≠ primary. Khác `ALERT-SCIENCE-CARD` (3 SA A/C/B) / `CROSS-SA-SCIENCE-CARD` (schema alone) / `ALERT-HAWTHORNE-SCIENCE-CARD` (participation) / `PUSH-ALERT-SCIENCE-CARD` (SA-05 alone) — thẻ này giữ **cặp bridge**.

**Mở song song:** thẻ này · `ALERT-CROSS-5MIN` · `ALERT-SCIENCE-CARD` · `CROSS-SA-SCIENCE-CARD` · `ALERT-CROSS-SA-ATLAS` · `LEAK-CROSS-SCIENCE-CARD` · `ALERT-HAWTHORNE-SCIENCE-CARD`

## Giữ / bỏ (ALERT × CROSS-SA)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **ALERT** | Cột làm/không · hội chẩn/AE/QA nội bộ **theo SA** | App BN · auto-treat · “cảnh báo chung” 3 SA |
| **Schema** | Mỗi SA một \(Y(t^*)\) · so \(t'≪t^*\) | Gộp Y · một model alert |
| **Primary** | D21 / VAS_D3 / PUSH_D14 giữ | ALERT / Hawthorne = primary |
| **\(Z\) ALERT** | Tín hiệu early ≠ \(Y(t^*)\) | Outcome primary làm trigger “early” |
| **Omics / L3** | **CLOSED** | Order vì đã ôn ALERT×CROSS |

## Ba SA → một hàng cặp

| SA | ALERT bộ | \(t^*\) bảo vệ | \(Z\) / tín hiệu ALERT |
|----|----------|----------------|------------------------|
| **01** | A1–A4 | D21 biểu mô | PCT/CFU/VAS/`clin_event` D0–D7 |
| **02** | C1–C3 | VAS relief D3 | VAS/CFU/ADHERE trước D3 |
| **05** | B1–B3 | PUSH D14 | PUSH/CFU/TURN ≤D7 · ≠ app ICU |

## Phương trình ranh giới

```text
ALERT theo SA trên Z(t')  →  hành động nội bộ (≠ Dx)
+ so schema t*/Z giữa SA  →  học khung (≠ train chung)
≠  gộp Y  ≠  app cảnh báo chung  ≠  mở G2/L3
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T2|T4|T6|CN · SA đang ôn (không gộp): 01|02|05 — ________
ALERT hàng (A__/C__/B__ · 1 dòng atlas): ________
t* primary: D21|VAS_D3|PUSH_D14 — ________
1 Z / tín hiệu ALERT (≠ Y(t*)): ________
ALERT = Dx / app / đổi primary? KHÔNG
Gộp Y nhiều SA / model cảnh báo chung? KHÔNG
Hawthorne / compliance = primary? KHÔNG
Omics vì ALERT×CROSS? KHÔNG
Cặp LEAK-CROSS / HAWTHORNE / PUSH-ALERT hôm nay? ________
1 việc ≤30′ (atlas / CROSS map / ALERT hàng): ________
Đóng Goal / deploy? KHÔNG
```

## Checklist 15′

```text
Đã mở ALERT + CROSS-SA thẻ riêng trước cặp? ________
ALERT gắn đúng SA (không copy A→B→C)? ________
Một app / một Y cho nhiều SA? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | ALERT×CROSS bridge 1 trang |
| `ALERT-CROSS-5MIN` | Drill điền |
| `ALERT-SCIENCE-CARD` | A/C/B · actionable ≠ Dx |
| `CROSS-SA-SCIENCE-CARD` | Schema · không gộp Y |
| `ALERT-CROSS-SA-ATLAS` | Atlas chi tiết |
| `ALERT-HAWTHORNE-SCIENCE-CARD` | Participation bias |
| `LEAK-CROSS-SCIENCE-CARD` | Leakage × schema |
| `PUSH-ALERT-SCIENCE-CARD` | SA-05 PUSH×ALERT |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Deploy ALERT ra app Dx / auto-treat / “cảnh báo Smart A chung”  
- Gộp endpoint / một model alert cho nhiều SA  
- Coi ALERT hoặc Hawthorne = primary / đóng Goal  
- Nhảy deploy khi STREAK&lt;3 · UpdateGoal trên PREP  

## Liên kết

`ALERT-CROSS-5MIN-MICRO-DRILL` · `ALERT-CROSS-EQ-5MIN` · `ALERT-SCIENCE-CARD` · `CROSS-SA-SCIENCE-CARD` · `ALERT-CROSS-SA-ATLAS` · `ALERT-HAWTHORNE-SCIENCE-CARD` · `LEAK-CROSS-SCIENCE-CARD` · `PUSH-ALERT-SCIENCE-CARD` · `NATMED-STREAK3-SCIENCE-CARD` · `CROSS-SA-EARLY-SIGNAL-MAP` · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
