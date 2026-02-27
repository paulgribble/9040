# Exercise 1: Your First Pandoc Document

**Time**: ~15 minutes | **Files**: `exercise1.md`, `refs.bib`, `apa.csl`

---

## Step 1: Look at the Source

Open `exercise1.md` in your text editor and read through it. Notice:

- The YAML metadata block at the top (between `---` markers)
- The section headings (`#`, `##`)
- The citations (`[@fredholm1999actions]`)
- The inline math (`$t(29) = 2.18$`)

This is just a text file. You could read it without compiling it.

## Step 2: Compile to PDF

```bash
pandoc exercise1.md --citeproc -o exercise1.pdf
```

Open `exercise1.pdf`. Notice:

- The title, author, and date are formatted automatically
- Citations are rendered in APA format
- A bibliography appears at the end
- Math is typeset beautifully

## Step 3: Compile to Word

```bash
pandoc exercise1.md --citeproc -o exercise1.docx
```

Open the `.docx` file. Compare it to the PDF.

## Step 4: Add Content

Find the comment block in `exercise1.md` (marked with `<!-- ... -->`). Your tasks:

### 4a. Add a subsection

Below the Procedure subsection, add:

```markdown
### Data Analysis
```

Write 2–3 sentences about how you'd analyze this data (e.g., paired-samples t-test on the change scores).

### 4b. Add an inline equation

Include the formula for a t-statistic in your paragraph:

```markdown
$t = \frac{\bar{X} - \mu}{s / \sqrt{n}}$
```

### 4c. Add a citation

1. Open `refs.bib` and add a new BibTeX entry (see the example in the file)
2. In your Data Analysis paragraph, cite it: `[@your_new_key]`

### 4d. Recompile

```bash
pandoc exercise1.md --citeproc -o exercise1.pdf
```

Verify: Does your new subsection appear? Is the equation rendered? Is the new citation in the bibliography?

## Discussion Questions

- How did the PDF compare to the Word output?
- How did adding a citation compare to Word/Zotero plugins?
- What happens if you misspell a citation key?
