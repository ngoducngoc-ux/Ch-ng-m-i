# CONSORT-EQ — thẻ khoa học 1 trang (placement ES · ladder Z · ≠ primary)

**Mã:** CONSORT-EQ-SCIENCE-CARD-v0.1  
**Ngày:** 2026-09-16  
**Neo:** `CONSORT-EQ-5MIN-MICRO-DRILL` · CONSORT-SCIENCE-CARD · CONSORT-SPIRIT · SPIRIT-EQ · EQ-M0M3 / EQ02 / EQ05  
**Căn cứ:** CONSORT 2010 DOI 10.1136/bmj.c332 · CONSORT-ES-PLACEMENT  
**Dùng khi:** STREAK≥3 · Daily stack **T5** · trước claim “đã báo ES đúng chỗ” · cặp CONSORT×EQ  
**Ưu tiên STREAK&lt;3:** **`STREAK3-PACK-SCIENCE-CARD`** · NATMED · ALERT · FILL-AID → tick **19/09** trước  
**Goal:** ACTIVE · ES = exploratory · primary không đổi · M0–M3 / AUROC demo ≠ hàng primary · L3 **CLOSED** · PREP ≠ DONE  

## Mục đích

Ôn **cặp CONSORT×EQ**: neo 1 SA + ladder M0–M3 trên \(Z\) → **đặt** ES ở Methods/Results exploratory — **không** cùng hàng primary; sandbox/`verify.sh` **không** vào Results lâm sàng. Khác `CONSORT-SCIENCE-CARD` (placement alone) / `EQ-*-SCIENCE-CARD` (ladder alone) — thẻ này giữ **cặp bridge**.

**Mở song song:** thẻ này · `CONSORT-EQ-5MIN` · `CONSORT-SCIENCE-CARD` · `CONSORT-SPIRIT-SCIENCE-CARD` · `SPIRIT-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `TRIPOD-SYNTH-SCIENCE-CARD`

## Giữ / bỏ (CONSORT × EQ)

| Khối | Giữ | Bỏ |
|------|-----|-----|
| **Primary hàng** | D21 / ΔVAS / ΔPUSH | ES / AUROC cùng hàng |
| **EQ ladder** | M0–M3 trên \(Z\) exploratory | PCT_D21 early · M4/X |
| **Placement** | Methods/Results exploratory | PRIMARY / Results lâm sàng |
| **Sandbox** | Methods/tech appendix | = bằng chứng BN |
| **CONSORT-AI** | [CẦN XÁC NHẬN] nếu chưa | Claim extension đủ vì drill |

## Phương trình ranh giới

```text
Primary CONSORT cố định  +  EQ ladder M0–M3 (exploratory only)
  ≥  trước  claim “báo ES đúng chỗ”
Sandbox / verify.sh  ≠  Results lâm sàng
ES / AUROC demo  ≠  hàng primary
```

## Điền 15′

```text
STREAK≥3? ________ (nếu không → STREAK3 path)
Thứ: T5 · SA neo: 01|02|05 — ________
EQ sibling: EQ-M0M3|EQ02|EQ05 — ________
Primary CONSORT hàng: D21|ΔVAS|ΔPUSH — ________
1 dòng Z / M0→M3 (exploratory only): ________
M0–M3 / AUROC demo đặt ở: SECONDARY|EXPLORATORY|KHÔNG BÁO (không PRIMARY) — ________
Sandbox / verify.sh vào Results lâm sàng? KHÔNG — vì: ________
CONSORT-AI extension cần ngay? CHƯA|[CẦN XÁC NHẬN]
Cặp SPIRIT-EQ / CONSORT-SPIRIT / SAP-EQ / TRIPOD hôm nay? ________
1 việc ≤30′ (placement sheet / EQ Drill 10′ / SAP ES): ________
Đóng Goal / coi báo cáo CLOSED vì CONSORT×EQ? KHÔNG
```

## Checklist 15′

```text
Đã mở CONSORT + EQ sibling thẻ riêng trước cặp? ________
ES cùng hàng primary? KHÔNG
PREP densify = DONE? KHÔNG
```

## Đừng nhầm atlas

| Thẻ / atlas | Việc |
|-------------|------|
| **thẻ này** | CONSORT×EQ bridge 1 trang |
| `CONSORT-EQ-5MIN` | Drill điền |
| `CONSORT-SCIENCE-CARD` | Placement alone |
| `CONSORT-SPIRIT-SCIENCE-CARD` | Khai+đặt ES |
| `SPIRIT-EQ-SCIENCE-CARD` | S1–S3 × ladder |
| `TRIPOD-SYNTH` / SYNTH | AI claim / sandbox |
| `STREAK3-PACK` / NatMed | Ưu tiên nếu STREAK&lt;3 |

## Cấm

- Đặt ES / AUROC sandbox cùng hàng primary  
- Coi Git/`verify.sh` = Results lâm sàng · UpdateGoal trên PREP  
- Nhảy claim khi STREAK&lt;3  

## Liên kết

`CONSORT-EQ-5MIN-MICRO-DRILL` · `CONSORT-SCIENCE-CARD` · `CONSORT-SPIRIT-SCIENCE-CARD` · `SPIRIT-EQ-SCIENCE-CARD` · `EQ-M0M3-SCIENCE-CARD` · `EQ02-M0M3-SCIENCE-CARD` · `EQ05-M0M3-SCIENCE-CARD` · `TRIPOD-SYNTH-SCIENCE-CARD` · `SAP-EQ-SCIENCE-CARD` · **`SPIRIT-G1-EQ-SCIENCE-CARD`** · `DAILY-STACK-AFTER-STREAK3` · `SCIENCE-CARDS-INDEX`
