# Analysis sandbox — SA-01 early-signal

Script:

- `sa01_early_signal_synthetic_m0_m3.py` — vết thương/bỏng, \(Y\)=biểu mô D21  
- `sa05_early_signal_synthetic_m0_m3.py` — ICU/PUSH, \(Y\)=cải thiện PUSH D14 (Δ≤−2)  
- `sa02_early_signal_synthetic_m0_m3.py` — TMH/VAS, \(Y\)=giảm VAS ≥2 điểm tại D3

```bash
pip install -r docs/precure-vn-alignment/research/analysis/requirements.txt
python3 docs/precure-vn-alignment/research/analysis/sa01_early_signal_synthetic_m0_m3.py
python3 docs/precure-vn-alignment/research/analysis/sa05_early_signal_synthetic_m0_m3.py
python3 docs/precure-vn-alignment/research/analysis/sa02_early_signal_synthetic_m0_m3.py
python3 docs/precure-vn-alignment/research/analysis/redcap_import_qc.py --demo
```

**Cảnh báo:** output không phải bằng chứng lâm sàng; chỉ để kiểm pipeline trước khi có export REDCap.

Pipeline export thật: [`REDCap-to-M0-M3-PIPELINE-v0.1.md`](REDCap-to-M0-M3-PIPELINE-v0.1.md)
