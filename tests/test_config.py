"""Smoke test so CI is green from day one; replace with real tests.

Good pattern: build tiny synthetic fixtures with known answers
(e.g., 5 fake observations) and assert your src functions recover them.
"""

from project_package_name import config


def test_project_root_is_repo():
    assert (config.PROJECT_ROOT / "pyproject.toml").exists()


def test_data_dirs_are_under_data_root():
    assert config.RAW_DIR.parent == config.DATA_ROOT
    assert config.INTERMEDIATE_DIR.parent == config.DATA_ROOT
    assert config.FINAL_DIR.parent == config.DATA_ROOT
