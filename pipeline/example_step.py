"""Pipeline step template.

Keep each script ~50 lines: load inputs → call functions from src/ → save
outputs. All real logic belongs in the package so it can be imported and
tested; scripts only orchestrate.
Name scripts descriptively (build_moves.py, make_figures.py) and document
the run order in the repo README.

Run with:  uv run python pipeline/example_step.py
"""

from project_package_name import config


def main() -> None:
    config.INTERMEDIATE_DIR.mkdir(parents=True, exist_ok=True)
    # df = load_raw(config.RAW_DIR / "input.csv")
    # result = do_something(df)
    # result.to_parquet(config.INTERMEDIATE_DIR / "result.parquet")
    print(f"DATA_ROOT = {config.DATA_ROOT}")


if __name__ == "__main__":
    main()
