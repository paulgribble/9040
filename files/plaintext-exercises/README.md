# Plaintext Authoring Exercises — Setup & Instructions

## Prerequisites

Before class, please install the following:

### 1. Pandoc

- **macOS** (with Homebrew): `brew install pandoc`
- **Windows (WSL/Ubuntu)**: `sudo apt update && sudo apt install pandoc`
- Or download from: <https://pandoc.org/installing.html>

Verify: `pandoc --version`

### 2. A LaTeX Distribution

- **macOS**: `brew install --cask mactex` (full, ~4 GB) or `brew install --cask basictex` (smaller, ~300 MB)
- **WSL/Ubuntu**: `sudo apt install texlive-latex-recommended texlive-fonts-recommended texlive-latex-extra texlive-bibtex-extra biber latexmk`

Verify: `pdflatex --version` and `latexmk --version`

> **Note for BasicTeX (macOS) users**: You may need to install extra packages with:
> ```
> sudo tlmgr update --self
> sudo tlmgr install booktabs biblatex biber logreq xstring collection-fontsrecommended
> ```

### 3. A Text Editor

Any plain text editor works. Recommendations:
- **VS Code** (free, cross-platform): <https://code.visualstudio.com/>
  - Install the "LaTeX Workshop" extension for LaTeX support
- **Sublime Text**: <https://www.sublimetext.com/>
- Or even `nano` / `vim` in the terminal if you prefer

### 4. Overleaf Account (for Exercise 2)

Create a free account at <https://www.overleaf.com/>

---

## Downloading the APA Citation Style

The exercises use the APA 7th edition citation style. Run the setup script to download it:

```bash
cd exercise-pack
bash setup.sh
```

This downloads `apa.csl` from the Zotero citation styles repository and copies it into each exercise folder.

If the download fails, you can manually download it from:
<https://www.zotero.org/styles/apa>

Save it as `apa.csl` and copy it into each exercise folder.

---

## Exercise Overview

### Exercise 1: Your First Pandoc Document (Lecture 1)

**Folder**: `exercise1/`

You're given a Markdown paper (`exercise1.md`) and a BibTeX bibliography (`refs.bib`). Your tasks:

1. Compile to PDF: `pandoc exercise1.md --citeproc -o exercise1.pdf`
2. Compile to Word: `pandoc exercise1.md --citeproc -o exercise1.docx`
3. Add a new subsection, a citation, and an inline equation
4. Recompile and verify

### Exercise 2: Building a LaTeX Document (Lecture 2)

**Folder**: `exercise2/`

You're given a LaTeX document (`exercise2.tex`) with placeholder comments marking where you need to add content. Your tasks:

1. Open in Overleaf (upload the folder) or compile locally
2. Add a numbered equation (Pearson's r)
3. Add a table with `booktabs` formatting
4. Add a figure (a sample plot `sample_figure.pdf` is included)
5. Add a citation
6. Compile and verify cross-references

Local compilation: `latexmk -pdf exercise2.tex`

### Exercise 3: The Full Pipeline (Lecture 2)

**Folder**: `exercise3/`

You're given a complete Markdown paper. Your tasks:

1. Compile to PDF, Word, and LaTeX with Pandoc
2. Inspect all three outputs
3. Edit the generated `.tex` file to fine-tune something
4. Recompile the LaTeX to PDF
5. Reflect on the workflow

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `pandoc: command not found` | Reinstall Pandoc or check your PATH |
| `pdflatex: command not found` | Install a LaTeX distribution (see above) |
| PDF compilation fails with missing package | Install it: `sudo tlmgr install <packagename>` (macOS) or `sudo apt install texlive-latex-extra` (Ubuntu) |
| Citations show as `[?]` or `[@key]` | Make sure you used `--citeproc` with Pandoc, or ran `biber` for LaTeX |
| Overleaf won't compile | Check the log for missing packages; Overleaf usually has everything pre-installed |
| Figure not found | Make sure the image file is in the same directory and the filename matches exactly (case-sensitive on Linux/macOS) |
