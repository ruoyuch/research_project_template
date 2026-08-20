# data subfolder
Gitignored entirely (only this README is tracked).
Organize as `raw/` (never modified after download), `intermediate/` (pipeline byproducts, safe to delete and rebuild), and `final/` (analysis-ready datasets).
Paths are defined once in `src/<package>/config.py`; set `DATA_ROOT` in `.env` to keep data outside the repo.
