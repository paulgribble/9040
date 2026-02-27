# Exercise 2: Building a LaTeX Document

**Time**: ~15 minutes | **Files**: `exercise2.tex`, `refs.bib`, `sample_figure.pdf`

---

## Getting Started

**Option A — Overleaf (recommended for first-timers):**

1. Go to <https://www.overleaf.com/> and log in
2. Click "New Project" → "Upload Project"
3. Zip this entire `exercise2/` folder and upload it
4. Overleaf will compile it automatically

**Option B — Local:**

```bash
latexmk -pdf exercise2.tex
```

Or if you don't have `latexmk`:

```bash
pdflatex exercise2.tex
biber exercise2
pdflatex exercise2.tex
pdflatex exercise2.tex
```

## Your Tasks

Open `exercise2.tex`. There are four clearly marked task blocks
(look for lines of `===` and `TASK 1`, `TASK 2`, etc.).

### Task 1: Add a Numbered Equation

Uncomment the `equation` environment for Pearson's $r$ and add a
sentence referencing it with `Equation~\ref{eq:pearson}`.

### Task 2: Add a Table

Uncomment the `table` environment and fill in the grip strength
values. Reference it with `Table~\ref{tab:results}`.

### Task 3: Add a Figure

Uncomment the `figure` environment. Write a meaningful caption.
Reference it with `Figure~\ref{fig:grip}`.

(The file `sample_figure.pdf` is a bar chart already in the folder.)

### Task 4: Add a Citation

1. Open `refs.bib` and add a new entry (see example in the file)
2. Cite it in the Discussion with `\citep{your_key}`
3. Recompile

## Verify

After completing all tasks, recompile and check:

- [ ] The equation is numbered and the reference resolves
- [ ] The table appears with clean `booktabs` lines
- [ ] The figure is placed on the page with a caption
- [ ] Your new citation appears in the text and bibliography

## Discussion Questions

- How did the equation-writing experience compare to Word's editor?
- What happened when you changed the figure placement from `[htbp]` to `[t]` or `[b]`?
- What do the multiple compilation passes actually do?
