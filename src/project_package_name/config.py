"""Central place for paths and parameters.

Every other module and pipeline script imports paths from here, so moving the
data directory (or running on another machine) only requires changing DATA_ROOT.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # reads .env at the repo root, if present

# repo root = two levels up from this file (src/project_package_name/config.py)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data lives outside git. Override with DATA_ROOT=/path/to/data in .env.
DATA_ROOT = Path(os.environ.get("DATA_ROOT", PROJECT_ROOT / "data"))
RAW_DIR = DATA_ROOT / "raw"
INTERMEDIATE_DIR = DATA_ROOT / "intermediate"
FINAL_DIR = DATA_ROOT / "final"

OUTPUT_DIR = PROJECT_ROOT / "output"
FIGURES_DIR = OUTPUT_DIR / "figures"
TABLES_DIR = OUTPUT_DIR / "tables"

# --- project parameters (examples; replace with your own) ---
# YEARS = range(2015, 2023)
