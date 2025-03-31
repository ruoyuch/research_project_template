# research_project_template
This template is designed to start a research project with an ultimate goal to write a paper.
Use this template if you want to (1) keep codes, documents, and references together, (2) perform analyses with different coding languages, and (3) write a paper and take progress notes.

The overall file structure is:

```markdown
    project_name/
    ├── analysis/         # All code & data processing
    │   ├── code/         # Python, Stata scripts, R codes, and notebooks
    │   └── data/         # Raw or processed data (could add raw/processed split)
    │
    ├── document/         # The writing zone
    │   ├── asset/        # Figures, tables, and images for the manuscript
    │   ├── draft/        # LaTeX or Word files (your actual paper)
    │   └── note/         # Personal notes, outlines, scratchpad (use .md to take notes)
    │
    ├── reference/        # Background literature, citations
    │   ├── topic1/       # Method-related PDFs, papers, bib entries
    │   ├── topic2/       # Topic-specific references (e.g., urban econ)
    │   └── ...           
    └── README.md         # Overview of the project
```

I use this file structure to manage my projects.
I use git/github to do version control (and backup) of my codes, notes, and drafts.
I use VS Code to do most of my edits.
Specifically, .do files can be editted and ran with the StataRun extension.
LaTex works well with the LaTex Workshop extension.