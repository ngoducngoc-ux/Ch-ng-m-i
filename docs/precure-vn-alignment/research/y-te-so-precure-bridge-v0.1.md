# Y tế số VN × Precure — cầu nối (không partnership)

**Mã:** YTSO-PRECURE-v0.1  
**Ngày:** 2026-09-16  
**Mục đích:** giữ hướng **phát hiện sớm – dữ liệu dọc – AI** cho Smart A và digital health VN, tách bạch với quảng bá thương mại Precure.LLC.

## 1. Học từ mô hình Precure (logic, không logo)

| Khía cạnh | Precure (tham chiếu press/VDHN) | Smart A / VN hiện tại |
|-----------|----------------------------------|------------------------|
| Dữ liệu | Multi-omics + lâm sàng dài hạn | RCT Smart A: \(Z\) dọc D0–D21; omics **gated** |
| AI | Pattern trước triệu chứng | Exploratory M0–M3 trên REDCap; không auto-diagnosis |
| Hành động | Actionable precision health | ALERT nội bộ nghiên cứu A/B/C |
| Quy mô | Cohort lớn / industry | N=80–120 — power hạn chế; ngôn ngữ trung tính |

## 2. Sản phẩm dữ liệu tối thiểu (y tế số đề tài)

1. **ID + timestamp + visit** — PB-004 architecture.  
2. **eCRF REDCap** staging → production (SA-01 v0.2 trước).  
3. **Audit trail** consent boundaries (ICF nested optional).  
4. **Export pipeline** → sandbox Python (verify.sh) trước khi claim model.

## 3. Ranh giới claim (TT 43 / ICH / đạo đức)

- Không dùng synthetic AUROC như bằng chứng lâm sàng.  
- Không triển khai app chẩn đoán sớm cho BN ngoài protocol.  
- Mọi “early signal” = **exploratory** trong SAP phụ.

## 4. Việc nhỏ quý

- [ ] Map 1 workflow BN thật (SA-01 visit) lên sơ đồ PB-004  
- [ ] Rà soát curriculum Ngày 26 (claim truyền thông vs DOI)

## Nguồn

- `sources/2026-precure-mayo-thermo-vdhn.md`  
- DOI Zhou 2019 · Nat Med 2019 (curriculum tuần 1)
