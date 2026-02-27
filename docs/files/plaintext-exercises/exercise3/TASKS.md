# Exercise 3: The Full Pipeline

**Time**: ~10 minutes | **Files**: `exercise3.md`, `refs.bib`, `search_figure.pdf`

---

This exercise demonstrates the full power of the plaintext workflow:
one source file, multiple outputs, with the option to "eject" to
LaTeX for fine-tuning.

## Step 1: Compile to Three Formats

Run these three commands:

```bash
# PDF (via LaTeX)
pandoc exercise3.md --citeproc -o exercise3.pdf

# Word
pandoc exercise3.md --citeproc -o exercise3.docx

# LaTeX source
pandoc exercise3.md --citeproc -s -o exercise3.tex
```

Open all three outputs and compare them.

## Step 2: Inspect the Generated LaTeX

Open `exercise3.tex` in your text editor. This is the LaTeX that
Pandoc generated from your Markdown. Notice:

- Pandoc chose a `\documentclass` and loaded packages for you
- Your YAML metadata became `\title{}`, `\author{}`, etc.
- Your Markdown headings became `\section{}`, `\subsection{}`
- Your citations were resolved and a bibliography was generated
- Your table became a `tabular` environment

## Step 3: Edit the LaTeX

Make at least one change to `exercise3.tex`. Suggestions:

- Change the figure placement preference (e.g., `[htbp]` → `[t]`)
- Add `\usepackage{booktabs}` to the preamble and upgrade the
  table rules to `\toprule`, `\midrule`, `\bottomrule`
- Add a `\pagebreak` before the References
- Change the font size in `\documentclass[12pt]{article}`
- Add `\linespread{1.5}` to the preamble for 1.5 line spacing

## Step 4: Compile the Edited LaTeX

```bash
latexmk -pdf exercise3.tex
```

Compare the new PDF to the original Pandoc PDF. Your LaTeX edits
should be reflected.

## Step 5: Reflect

Ask yourself:

- You just produced a PDF, a Word doc, and a LaTeX source from
  **one Markdown file** in under a minute. Could you do that in Word?
- When a journal asks for a `.docx`, you have it. When a journal
  provides a LaTeX template, you can paste your content in. When
  you want a polished PDF, you have fine-grained control.
- Your Markdown source file is 5 KB of plain text. It will be
  readable on any computer, in any text editor, 50 years from now.

## Discussion Questions

- What are the trade-offs of staying in Markdown vs. moving to LaTeX?
- At what point in a project would you "eject" from Markdown to LaTeX?
- How does this workflow fit with version control (Git)?
