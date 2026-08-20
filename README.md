# Guidelines
[![CI](https://github.com/ruoyuch/research_project_template/actions/workflows/ci.yml/badge.svg)](https://github.com/ruoyuch/research_project_template/actions/workflows/ci.yml)

This template is designed to start a research project with an ultimate goal to write a paper.
Use this template if you want to (1) keep code, documents, and references together, (2) run analyses as a testable, reproducible pipeline, and (3) write a paper and take progress notes.

The overall file structure is:

```markdown
    project_name/
    ├── src/
    │   └── project_package_name/  # the installable package: ALL logic lives here
    │       └── config.py          # paths (DATA_ROOT → ./data) + project parameters
    │
    ├── pipeline/                  # the scripts you RUN (document run order below)
    │   └── example_step.py        # each ~50 lines: load → call src functions → save
    │
    ├── notebooks/                 # exploration only; nothing downstream depends on these
    ├── tests/                     # synthetic fixtures with known answers
    ├── data/                      # gitignored; raw/ intermediate/ final/ inside
    ├── output/                    # gitignored; figures/ + tables/ that the pipeline produces
    │
    ├── docs/                      # the writing zone, split by audience
    │   ├── private/               # gitignored work-in-progress, not meant for sharing
    │   │   ├── draft/             # LaTeX manuscript in progress
    │   │   ├── notes/             # progress notes, outlines, scratchpad (.md)
    │   │   └── references/        # background literature, by topic
    │   └── public/                # tracked, polished, safe to share
    │       ├── manuscript.tex     # the paper
    │       └── slides.tex         # beamer presentation slides
    │
    ├── .github/workflows/ci.yml   # runs ruff + pytest on every push
    ├── pyproject.toml             # dependencies + ruff + pytest config (uv-managed)
    ├── uv.lock
    ├── .pre-commit-config.yaml    # ruff, ruff-format, nbstripout before every commit
    ├── .env.example               # variable names only (real values in gitignored .env)
    ├── AGENTS.md                  # working conventions for coding agents
    └── README.md                  # overview of the project
```

## Getting started
1. Rename `src/project_package_name/` to your project's package name (also update it in `pyproject.toml`).
2. Install [uv](https://docs.astral.sh/uv/), then run `uv sync --dev` to create `.venv` and install everything from the lockfile.
3. Run `uv run prek install` to install the git hooks (ruff, ruff-format, nbstripout run before every commit).
4. Run `uv run nbdime config-git --enable` once if you want readable notebook diffs in git.
5. If you need a custom `DATA_ROOT` or any API keys, copy `.env.example` to `.env` and fill it in — `.env` stays out of git.

Day to day: `uv run prek run -a` (lint + format + hooks on demand), `uv run pytest` (tests), `uv run python pipeline/<script>.py` (a pipeline step).

## Conventions
- Environments are managed with **uv** (no conda): `pyproject.toml` declares dependencies, `uv.lock` pins them, `uv run <cmd>` executes inside the venv. Add a package with `uv add <name>` — never edit `.venv` or `uv.lock` by hand.
- All logic lives in `src/` where it can be imported and tested; `pipeline/` scripts only orchestrate (load → call src functions → save). Name scripts descriptively (`build_moves.py`, `make_figures.py`) and list their run order here in the README as the project grows.
- Git hooks run via **prek** (a fast pre-commit-compatible runner) using `.pre-commit-config.yaml`: ruff (lint + format) and nbstripout on every commit. CI re-checks ruff and runs pytest on every push and PR.
- `data/` and `output/` never enter git — both are pure pipeline products, reproducible by re-running it. Curated final figures/tables that the manuscript includes belong in `docs/public/`, as siblings of the `.tex` file.
- `docs/private/` (draft, notes, references) is gitignored — work in progress, no backup beyond your own machine. `docs/public/` is tracked — only promote a file there when it's ready to be shared.
- See `AGENTS.md` for the fuller set of conventions an AI coding agent (or a coauthor) should follow in this repo.

I use git/github to do version control (and backup) of my code, notes, and drafts, and VS Code for most edits.
