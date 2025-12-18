# Start Here

Welcome! This guide explains how the FASTR slide builder works.

---

## The One Thing You Need to Know

**All your work happens in the `methodology/` folder.**

That's it. You edit files there, and two things happen:

1. Your content becomes part of the **documentation website**
2. Parts you mark become **workshop slides**

---

## The 9 Module Files

There are 9 files in `methodology/`. Each one corresponds to a module in the **FASTR RMNCAH-N Service Use Monitoring Resource Package**:

| File | Module |
|------|--------|
| `00_introduction.md` | Module 0: Introduction to FASTR |
| `01_identify_questions_indicators.md` | Module 1: Identify Questions & Indicators |
| `02_data_extraction.md` | Module 2: Data Extraction |
| `03_fastr_analytics_platform.md` | Module 3: FASTR Analytics Platform |
| `04_data_quality_assessment.md` | Module 4: Data Quality Assessment |
| `05_data_quality_adjustment.md` | Module 5: Data Quality Adjustment |
| `06a_service_utilization.md` | Module 6a: Service Utilization Analysis |
| `06b_coverage_estimates.md` | Module 6b: Coverage Estimates |
| `07_results_communication.md` | Module 7: Results Communication |

**To update content:** Open the file and edit it. Save. Done.

---

## How Content Becomes Two Things

When you edit a file in `methodology/`, it serves two purposes:

```
methodology/04_data_quality_assessment.md
        │
        ├──→ Full text appears on the documentation website
        │    https://fastr-analytics.github.io/fastr-slide-builder/
        │
        └──→ SLIDE-marked sections become workshop slides
             (for presenting in person)
```

### What are SLIDE markers?

They're special comments that say "this part should become a slide":

```markdown
This text is documentation only.

<!-- SLIDE:m4_1 -->
## Data Quality Assessment

This text will become a slide!

- Bullet point
- Another point

![Chart](resources/default_outputs/chart.png)
<!-- /SLIDE -->

This text is documentation only again.
```

**The rule:** Content between `<!-- SLIDE:xxx -->` and `<!-- /SLIDE -->` becomes a slide. Everything else is just documentation.

---

## The Simple Workflow

### If you're just editing content:

1. Open a file in `methodology/`
2. Make your changes
3. Save
4. Push to GitHub
5. The website updates automatically

### If you want to update slides too:

1. Edit files in `methodology/`
2. Run: `python3 tools/00_extract_slides.py`
3. The slides in `core_content/` are updated

### If you're building a workshop presentation:

1. Run: `python3 tools/01_new_workshop.py`
2. Edit your workshop config
3. Run: `python3 tools/03_build_deck.py`
4. Export: `marp outputs/YOUR_deck.md --theme-set fastr-theme.css --pdf`

---

## Other Guides

| Guide | When to read it |
|-------|-----------------|
| [01 Editing Content](01_editing_content.md) | Markdown syntax & SLIDE markers |
| [02 Building Workshops](02_building_workshops.md) | Creating workshop presentations |
| [03 Local Setup](03_local_setup.md) | Setting up your computer |
| [04 Codespaces Setup](04_codespaces_setup.md) | Working in browser (no install needed) |

---

## Quick Reference

### Where is everything?

| Folder | What's in it |
|--------|--------------|
| `methodology/` | The 9 module files you edit |
| `core_content/` | Auto-generated slides (don't edit directly) |
| `workshops/` | Workshop configurations |
| `tools/` | Build scripts |
| `outputs/` | Generated presentations |

### The tools

| Command | What it does |
|---------|--------------|
| `python3 tools/00_extract_slides.py` | Extract slides from methodology |
| `python3 tools/01_new_workshop.py` | Create new workshop |
| `python3 tools/02_check_workshop.py` | Check workshop for errors |
| `python3 tools/03_build_deck.py` | Build the slide deck |
| `python3 tools/04_convert_pptx.py` | Convert to PowerPoint |

---

## Need Help?

- **Documentation website:** https://fastr-analytics.github.io/fastr-slide-builder/
- **Example workshop:** Look at `workshops/example/`
- **Questions:** Contact the FASTR team
