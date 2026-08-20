# notebooks subfolder
Exploration only — nothing downstream depends on these.
Once a notebook produces something worth keeping, promote the logic into `src/` and the orchestration into a `pipeline/` script.
Outputs are stripped on commit by the nbstripout pre-commit hook, so diffs stay readable and no data leaks into git.
