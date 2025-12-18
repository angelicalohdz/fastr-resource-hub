# FASTR Slide Builder

Build customized FASTR workshop presentations from reusable content modules.

**Repository:** https://github.com/FASTR-Analytics/fastr-slide-builder

**Methodology Documentation:** https://fastr-analytics.github.io/fastr-slide-builder/

---

## Content Workflow: Single Source of Truth

All FASTR methodology content lives in **one place**: the `methodology/` folder. This folder serves two purposes:

1. **Full Documentation** - Readable as a complete MkDocs website
2. **Slide Content Source** - Sections marked with `<!-- SLIDE -->` tags are extracted for workshop presentations

### How It Works

```
methodology/                    ← ALWAYS work here
├── 00_introduction.md          ← Full module with slide markers inside
├── 04_data_quality_assessment.md
├── 05_data_quality_adjustment.md
├── 06a_service_utilization.md
├── 06b_coverage_estimates.md
└── ...

    ↓ Extract slides (tools/00_extract_slides.py)

core_content/                   ← Auto-generated, don't edit directly
├── 01_background_rationale/
│   ├── m0_1.md                 ← Extracted slide content
│   ├── m0_2.md
│   └── ...
└── ...
```

### Marking Content as Slides

In any methodology file, wrap slide content with markers:

```markdown
## Some Section Title

This is regular documentation text that appears in the full docs.

<!-- SLIDE:m4_1 -->
## Data Quality Assessment

This content will be extracted as a slide.

- Key point 1
- Key point 2

![Chart](resources/default_outputs/dq_chart.png)
<!-- /SLIDE -->

More regular documentation continues here...
```

**Slide ID Format:** `m{module}_{section}` (e.g., `m4_1`, `m4_2`, `m6a_1`)

### Extracting Slides

After editing methodology files, regenerate the core slides:

```bash
python3 tools/00_extract_slides.py
```

This scans all `methodology/*.md` files and extracts slide-marked content into `core_content/`.

---

## Quick Start: Building a Workshop

### 4-Step Workflow

```bash
# 1. Set up a new workshop (interactive)
python3 tools/01_new_workshop.py

# 2. Check your setup (optional but recommended)
python3 tools/02_check_workshop.py

# 3. Build the slide deck
python3 tools/03_build_deck.py

# 4. Export to PDF (recommended)
marp outputs/YOUR-WORKSHOP_deck.md --theme-set fastr-theme.css --pdf
```

---

## Key Features

### Flexible Slide Ordering

Use `deck_order` in `config.py` to control exactly which slides appear and in what order:

```python
'deck_order': [
    'agenda',                    # Built-in agenda slide
    'objectives.md',             # Your custom slide
    'intro',                     # Built-in FASTR intro session
    'dq_assessment',             # Built-in data quality session
    'dq-findings.md',            # Your country-specific findings
    'coverage',                  # Built-in coverage session
    'next-steps.md',             # Your action items
]
```

### Smart Variable Substitution

Define country data once in `config.py`, use everywhere with `{{variable}}`:

```python
'country_data': {
    'total_facilities': '2,847',
    'reporting_rate': '92%',
    'survey_anc1': '87%',
}
```

Then in any slide: "Coverage: {{survey_anc1}}" becomes "Coverage: 87%"

### Automatic Break Placement

The builder intelligently adds tea, lunch, and afternoon breaks based on your workshop duration (1, 2, or 3 days).

---

## Folder Structure

```
fastr-slide-builder/
├── methodology/            # ⭐ SINGLE SOURCE - Edit content HERE
│   ├── 00_introduction.md      # Module 0: Introduction (with slide markers)
│   ├── 01_identify_questions_indicators.md
│   ├── 02_data_extraction.md
│   ├── 03_fastr_analytics_platform.md
│   ├── 04_data_quality_assessment.md  # Module 4: DQA (with slide markers)
│   ├── 05_data_quality_adjustment.md  # Module 5: Adjustment (with slide markers)
│   ├── 06a_service_utilization.md     # Module 6a: Utilization (with slide markers)
│   ├── 06b_coverage_estimates.md      # Module 6b: Coverage (with slide markers)
│   ├── 07_results_communication.md
│   ├── mkdocs.yml              # MkDocs configuration
│   ├── references.bib          # Bibliography
│   └── resources/              # Images, diagrams, outputs
│
├── tools/                  # Build scripts
│   ├── 00_extract_slides.py    # Extract slides from methodology
│   ├── 01_new_workshop.py      # Create new workshop (interactive)
│   ├── 02_check_workshop.py    # Validate setup before building
│   ├── 03_build_deck.py        # Assemble markdown deck
│   └── 04_convert_pptx.py      # Export to PowerPoint (optional)
│
├── core_content/           # Auto-generated from methodology (don't edit)
│   ├── 01_background_rationale/
│   ├── 02_fastr_approach/
│   └── ...
│
├── workshops/              # Workshop-specific content
│   ├── example/                # Reference implementation
│   └── YOUR-WORKSHOP/
│       ├── config.py           # Workshop settings & country data
│       ├── objectives.md       # Custom slide: workshop goals
│       └── ...
│
├── resources/              # Shared assets (logos, diagrams)
└── outputs/                # Generated decks (gitignored)
```

---

## Built-in Sessions

Use these session IDs in your `deck_order`:

| Session ID | Description | Duration |
|------------|-------------|----------|
| `intro` | Background & FASTR approach | ~30 min |
| `extraction` | Data extraction from DHIS2 | ~45 min |
| `dq_assessment` | Data quality assessment | ~90 min |
| `dq_adjustment` | Data adjustment methods | ~60 min |
| `disruption` | Service disruption detection | ~90 min |
| `coverage` | Coverage analysis | ~90 min |
| `facility` | Facility assessments | ~30 min |

---

## Installation Options

### Option 1: GitHub Codespaces (Zero Setup)

1. Open https://github.com/FASTR-Analytics/fastr-slide-builder
2. Click **Code** → **Codespaces** → **Create codespace on main**
3. Everything is pre-installed and ready to use

Free tier: 60 hours/month.

### Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/FASTR-Analytics/fastr-slide-builder.git
cd fastr-slide-builder

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Additional tools for rendering:**
- Marp CLI: `npm install -g @marp-team/marp-cli` (for PDF export)
- Pandoc: `brew install pandoc` (for PowerPoint export)

---

## Common Commands

```bash
# Extract slides from methodology (after editing content)
python3 tools/00_extract_slides.py

# Create new workshop (interactive wizard)
python3 tools/01_new_workshop.py

# Check workshop setup (catches common issues)
python3 tools/02_check_workshop.py

# Build deck (interactive - shows all workshops)
python3 tools/03_build_deck.py

# Build specific workshop (non-interactive)
python3 tools/03_build_deck.py --workshop 2025-nigeria

# Export to PDF (recommended)
marp outputs/2025-nigeria_deck.md --theme-set fastr-theme.css --pdf

# Build methodology docs locally
source .venv/bin/activate
mkdocs serve -f methodology/mkdocs.yml
```

---

## PDF vs PowerPoint

**PDF (Recommended):**
- Perfect FASTR styling out-of-the-box
- Consistent across all platforms
- Smaller file size
- Ready to present immediately

**PowerPoint:**
- Allows post-export editing
- Useful for last-minute changes
- May require font/layout adjustments

---

## Contributing

### Updating Methodology Content

1. **Edit files in `methodology/`** - This is the single source of truth
2. **Add slide markers** around content that should become slides
3. **Run extraction** - `python3 tools/00_extract_slides.py`
4. **Commit changes** - Both methodology and generated core_content

### Creating Workshop Content

1. Run `python3 tools/01_new_workshop.py`
2. Edit generated files in `workshops/YOUR-WORKSHOP/`
3. Build and test with `python3 tools/03_build_deck.py`

---

## Support

1. Check [Methodology Documentation](https://fastr-analytics.github.io/fastr-slide-builder/)
2. Review the example workshop: `workshops/example/`
3. Contact the FASTR team

---

## License

FASTR methodology and content - see your organization's license.
