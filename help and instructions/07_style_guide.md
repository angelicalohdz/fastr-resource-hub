# Style guide

> **Note:** This is the current working style guide (January 2025). Follow these conventions for consistency, but they are not set in stone. If you find something that doesn't work or have suggestions for improvement, flag it for discussion and we can update the guide.

This document defines the typographic and formatting conventions for FASTR methodology documentation.

---

## Headings

### Capitalization: sentence case

Use sentence case for all headings. Only capitalize the first word and proper nouns (like FASTR, DHIS2, RMNCAH-N).

| Correct | Incorrect |
|---------|-----------|
| `## Why focus on high volume indicators?` | `## Why Focus on High Volume Indicators?` |
| `### What do we mean by answerable?` | `### What Do We Mean by Answerable?` |
| `## Data quality assessment` | `## Data Quality Assessment` |
| `### FASTR core indicators` | `### Fastr Core Indicators` |

### Heading hierarchy

| Level | Usage | Example |
|-------|-------|---------|
| `#` | Module title only (one per file) | `# Data extraction` |
| `##` | Major sections | `## Overview`, `## How it works` |
| `###` | Subsections | `### Why monthly facility level data?` |
| `####` | Technical details, sub-subsections | `#### Input file structure` |

### Questions as headings

When phrasing headings as questions, use sentence case with a question mark:

```markdown
### What do we mean by answerable?
### Why focus on high volume indicators?
### Is my question a relevant priority?
```

---

## Text formatting

### Bold

Use bold (`**text**`) for:

- **Key terms** on first introduction
- **Labels** before descriptions: `**Inputs**:`, `**Purpose**:`, `**Process**:`
- **Emphasis** on critical concepts
- **Step labels**: `**Step 1:**`, `**Step 2:**`

```markdown
**Inputs**
- Raw HMIS data (`hmis_ISO3.csv`)
- Geographic identifiers

**Purpose**: Loads and prepares data for analysis.
```

### Inline code

Use backticks (`` ` ``) for:

- Filenames: `` `hmis_data.csv` ``
- Variable names: `` `facility_id` ``, `` `period_id` ``
- Function names: `` `load_data()` ``
- Parameter values: `` `count > 0` ``
- Package names: `` `data.table` ``

### Italics

Use sparingly for:
- Emphasis within sentences
- Placeholder text: *Content to be developed*

---

## Lists

### Bullet points

- No periods for single-line items
- Add periods only when items contain multiple sentences
- Use consistent indentation for sub-bullets

**Single-line items (no periods):**
```markdown
- Raw HMIS data
- Geographic identifiers
- Standardized indicator names
```

**Multi-sentence items (with periods):**
```markdown
- Captures medium-term trends. Reduces impact of short-term fluctuations.
- Sufficient data points for stable averages. Works well with quarterly reporting.
```

### Numbered lists

Use for sequential steps or ordered information:

```markdown
1. Load and prepare data
2. Assess data quality
3. Apply adjustments
```

For sub-steps, use nested numbering:

```markdown
1. First step
   1. Sub-step A
   2. Sub-step B
2. Second step
```

---

## Tables

Use markdown pipe tables with clear headers:

```markdown
| Component | Description |
|-----------|-------------|
| **Inputs** | Raw HMIS data |
| **Outputs** | Adjusted dataset |
```

Guidelines:
- Headers in sentence case
- Use bold for emphasis when needed
- Left-align text columns

---

## Code blocks

### Inline code

Use single backticks for inline code: `` `variable_name` ``

### Code blocks

Use triple backticks with language specification:

````markdown
```r
COUNTRY_ISO3 <- "GIN"
GEOLEVEL <- "admin_area_3"
```
````

Common language tags:
- `r` for R code
- `python` for Python
- `csv` for CSV format
- `text` for plain text output

---

## Blockquotes

Use `>` for:
- Important notes or warnings
- Quoted content
- Highlighted definitions

```markdown
> **Note:** This content was hidden in the original presentation but may be useful to include.
```

---

## Expandable sections

Use `???` for collapsible technical content:

```markdown
??? "Configuration parameters"

    **Parameter**: `THRESHOLD`

    **Default**: 0.05

    **Description**: Sets the outlier detection threshold.
```

Use for:
- Technical documentation
- Function specifications
- Algorithm explanations
- Troubleshooting sections

---

## Mathematical notation

### Inline math

Use single `$` delimiters:

```markdown
The formula is $\text{MAD} = \text{median}(|x - \text{median}(x)|)$
```

### Display math

Use double `$$` on separate lines:

```markdown
$$
\text{Coverage} = \frac{\text{Numerator}}{\text{Denominator}} \times 100
$$
```

---

## Links

### Internal links

Link to other methodology files:

```markdown
See [Data quality adjustment](05_data_quality_adjustment.md) for details.
```

### External links

```markdown
Visit the [DHIS2 documentation](https://docs.dhis2.org) for more information.
```

---

## Abbreviations

Define on first use, then use abbreviation:

```markdown
The Health Management Information System (HMIS) provides routine data.
HMIS data is collected monthly at facility level.
```

Common abbreviations:
- FASTR (always capitalized)
- DHIS2
- HMIS
- RMNCAH-N
- DQA (Data Quality Assessment)

---

## Slide markers

For content that should appear in workshop slides, use:

```markdown
<!-- SLIDE:m4_1 -->
## Slide title

Slide content here.

<!-- /SLIDE -->
```

Naming convention: `m[module]_[section][subsection]`
- `m1_1` - Module 1, section 1
- `m1_2a` - Module 1, section 2, subsection a

---

## File structure

Each methodology file should include:

1. **Module title** (`#`)
2. **Overview section** (`##`) - what and why
3. **Main content sections** (`##`)
4. **ASCII separator** (for slide content)
5. **Slide content** (using `<!-- SLIDE:xxx -->` markers)

---

## Footer

End each methodology file with:

```markdown
---

**Last updated**: DD-MM-YYYY
**Contact**: FASTR Project Team

---
```

---

## Quick reference

| Element | Convention |
|---------|------------|
| Headings | Sentence case |
| Bold | Key terms, labels |
| Inline code | Filenames, variables, functions |
| Lists | No periods for single items |
| Tables | Sentence case headers |
| Code blocks | Include language tag |
| Abbreviations | Define on first use |
| Slide markers | `<!-- SLIDE:m#_# -->` |
