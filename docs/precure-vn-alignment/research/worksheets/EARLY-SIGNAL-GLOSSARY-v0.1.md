# Glossary — early-signal × multi-omics × Smart A

**Mã:** EARLY-SIGNAL-GLOSSARY-v0.1  
**Ngày:** 2026-09-16  
**Dùng khi:** ritual hàng ngày · slide nội bộ · tránh lệch nghĩa với press Precure.LLC  
**Hub:** `RITUAL-CARDS-INDEX.md`

## Thời gian & outcome

| Thuật ngữ | Nghĩa trong Smart A | Không nghĩa |
|-----------|---------------------|-------------|
| \(t^*\) | Mốc **primary** đã chốt (SA-01 D21 · SA-02 D3 · SA-05 D14) | “Sớm hơn triệu chứng” kiểu marketing |
| \(t'\) | Mốc **exploratory** trước/cùng cửa sổ \(t^*\) (vd. D0/D3/D7) | Thay primary |
| Early-signal | Tín hiệu trên \(Z(t')\) (sau này có thể \(X\)) dự báo \(Y(t^*)\) — **SAP ES** | App Dx / auto-treat |
| \(Y(t^*)\) | Endpoint chính RCT | AUROC sandbox |

## Dữ liệu & sự kiện

| Thuật ngữ | Nghĩa | Artifact |
|-----------|-------|----------|
| \(Z\) | Biến lâm sàng dọc (PCT, CFU, VAS, PUSH, …) | eCRF · Endpoints card |
| \(X\) / L3 | Omics/phân tử (PEA…) — **gated** | PEA card · G2-READINESS |
| `clin_event` | Sự kiện lâm sàng 0–4 (Zhou analog) · SA-02/05 = schema event riêng | `CLIN_EVENT-ZHOU-MAP` · `CLIN_EVENT-CROSS-SA-ATLAS` |
| PB-008 | Hiệu ứng tham gia / adherence bias (Nat Med) | PB-008 worksheet · **`PB008-5MIN`** |
| ALERT A1–A4 | Hành động **nội bộ nghiên cứu** | ALERT-SA01 · NatMed map · `ALERT-CROSS-SA-ATLAS` |

## AI & tầng (PB-009)

| Thuật ngữ | Nghĩa | Artifact |
|-----------|-------|----------|
| L1 | REDCap visit + ID/time + `clin_event` + \(Z\) | PB-004 · y-te-so · `CLIN_EVENT-CROSS-SA-ATLAS` |
| L2 | M0–M3 exploratory trên export de-ID | PIPELINE · EQ · TRIPOD · `LEAKAGE-CROSS-SA-ATLAS` |
| L3 | Multi-omics — chỉ sau G1–G2 data thật | PEA card · OMICS-IF-G2 · **`L1L2L3-DAILY-GATE-CARD`** |
| M0 vs M3 | Snapshot D0 vs chuỗi \(Z\) đến \(t'\) | HYP-SA01 · EQ-SAx |
| Pitfall #5 | Synthetic AUROC ≠ bằng chứng BN | `ML-OMICS-PITFALLS` · `verify.sh` = QC |
| Leakage (thời gian / trùng Y) | Predictor ≥ \(t^*\) hoặc gần định nghĩa \(Y\) trong M early | `LEAKAGE-CROSS-SA-ATLAS` · EQ-01/02/05 |

## Cổng & vận hành

| Thuật ngữ | Nghĩa |
|-----------|-------|
| G1 | Nested consent / ethics cho biospecimen — **CLOSED** mặc định |
| G2 | Signal trên \(Z\) + DSMB/PI trên **N thật** trước omics |
| PREP | Agent scaffold file — **≠** STREAK DONE |
| DONE | PI ritual 45′: insight + câu hỏi SA + tick STREAK |
| Cờ đầu | SA-01 (PROPOSED→confirmed) — SA-02/05 support |

## Một câu ôn nhanh

> Phát hiện sớm–dữ liệu dọc–AI = \(Z(t')\) + `clin_event` + M0–M3 (L1→L2) hướng tới \(Y(t^*)\); multi-omics \(X\) là L3 sau G2 — không phải điều kiện để bắt đầu ôn hàng ngày.

## Liên kết

- **5′ drill:** `GLOSSARY-5MIN-MICRO-DRILL`
- Cards: NatMed · PEA · Endpoints · DESIGN-YTESO · Tier3 · CROSS-SA · PB-009 · **`PB008-5MIN`**  
- `AI-LONGITUDINAL-STACK` · `MULTI-OMICS-GATES` · `GOAL-HEALTH`
