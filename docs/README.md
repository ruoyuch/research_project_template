# docs subfolder
All writing and documentation lives here, split by audience:

- `private/` — gitignored work-in-progress, not meant for sharing:
  - `draft/` — the manuscript in progress (LaTeX or Word)
  - `notes/` — progress notes, outlines, scratchpad (.md)
  - `references/` — background literature (PDFs etc.), organized by topic
- `public/` — tracked, polished, safe to share:
  - `manuscript.tex` — the paper
  - `slides.tex` — beamer presentation slides
  - `references.bib` — the per-project bibliography both files read
  - final figures/tables the `.tex` files include live here too, as siblings

I use .md to take notes and .tex to write papers; .tex works well with the LaTeX Workshop VS Code extension.
You can even work collaboratively by being in the same github repo, but it is not as good as overleaf or gdoc.
