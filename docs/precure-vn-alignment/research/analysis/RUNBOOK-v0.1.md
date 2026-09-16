# Analysis runbook — Precure verify

**Khi chạy:** sau sửa `research/analysis/*.py`, CSV eCRF, hoặc trước claim PASS trên PR.

```bash
bash docs/precure-vn-alignment/research/analysis/verify.sh
```

**Kỳ vọng:** dòng cuối `PRECURE verify: PASS` · exit 0.

**Không:** coi output synthetic là bằng chứng lâm sàng (pitfall #5).

**CI:** `.github/workflows/precure-verify.yml` trên PR Precure.

**QC export (demo):**

```bash
python3 docs/precure-vn-alignment/research/analysis/redcap_import_qc.py --demo
```

**Governance:** ritual DONE = PI only — `research/RITUAL-DONE-vs-PREP.md` · catch-up `BACKLOG-RITUAL-PRIORITY-v0.1.md`.
