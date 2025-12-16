# Contributing to FASTR Slide Builder

Thank you for contributing to the FASTR slide deck system! This guide will help you understand how to work with the repository effectively.

## Table of Contents

- [Getting Started](#getting-started)
- [Types of Contributions](#types-of-contributions)
- [Workflow Guidelines](#workflow-guidelines)
- [Best Practices](#best-practices)
- [Commit Message Guidelines](#commit-message-guidelines)

## Getting Started

### First Time Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd fastr-slide-builder
   ```

2. **Verify setup:**
   ```bash
   python3 tools/build_deck.py --workshop example
   ```

3. **Install optional tools:**
   ```bash
   # For PDF export (recommended)
   npm install -g @marp-team/marp-cli

   # For PowerPoint export
   brew install pandoc  # Mac
   ```

## Types of Contributions

### 1. Editing Core Content

**What:** Shared FASTR methodology modules (7 sections)

**When to edit:**
- Updating methodology
- Fixing typos or errors
- Improving explanations
- Adding/updating diagrams

**Where:** `core_content/*.md`

**Process:**
1. Edit the relevant file in `core_content/`
2. Test with example workshop:
   ```bash
   python3 tools/build_deck.py --workshop example
   marp outputs/example_deck.md --theme-set fastr-theme.css --pdf
   ```
3. Review the output
4. Commit with descriptive message
5. Push to shared repository

**Example:**
```bash
# Edit file
code core_content/04_data_quality_assessment.md

# Test
python3 tools/build_deck.py --workshop example

# Commit
git add core_content/04_data_quality_assessment.md
git commit -m "Update DQA section: add missing indicators"
git push
```

### 2. Creating Workshop-Specific Content

**What:** Custom slides for a specific workshop

**When to create:**
- New country workshop
- Specialized training session
- Custom results presentation

**Where:** `workshops/{workshop_id}/`

**Process:**
1. Copy example workshop:
   ```bash
   cp -r workshops/example workshops/2025_01_yourcountry
   ```

2. Edit configuration:
   ```bash
   code workshops/2025_01_yourcountry/config.py
   ```

3. Add custom slides (optional):
   ```bash
   code workshops/2025_01_yourcountry/custom_slides.md
   ```

4. Add agenda image (optional):
   ```bash
   # Place your agenda.png in the workshop folder
   cp ~/Desktop/agenda.png workshops/2025_01_yourcountry/
   ```

5. Build and test:
   ```bash
   python3 tools/build_deck.py --workshop 2025_01_yourcountry
   ```

6. Commit workshop folder:
   ```bash
   git add workshops/2025_01_yourcountry/
   git commit -m "Add Nigeria 2025 workshop"
   git push
   ```

### 3. Updating Templates

**What:** Reusable slide templates (title, breaks, agenda, closing)

**When to edit:**
- Changing template layout
- Adding new variables
- Updating branding

**Where:** `templates/*.md`

**Process:**
1. Edit template file
2. Test with example workshop
3. Verify variable substitution works
4. Commit changes

**Note:** Template changes affect ALL future decks. Coordinate with team first.

### 4. Improving Build Tools

**What:** Python build scripts

**When to edit:**
- Bug fixes
- New features
- Performance improvements

**Where:** `tools/*.py`

**Process:**
1. Make changes
2. Test thoroughly with multiple workshops
3. Update documentation if needed
4. Commit with detailed message

## Workflow Guidelines

### Branch Strategy (Optional)

For major changes, use feature branches:

```bash
# Create feature branch
git checkout -b update-dqa-section

# Make changes
code core_content/04_data_quality_assessment.md

# Test
python3 tools/build_deck.py --workshop example

# Commit
git add core_content/04_data_quality_assessment.md
git commit -m "Update DQA section with new indicators"

# Push branch
git push -u origin update-dqa-section

# Create pull request (if using GitHub/GitLab)
```

### Direct to Main (Simple Changes)

For small fixes (typos, minor updates):

```bash
# Make change
code core_content/01_background_rationale.md

# Test
python3 tools/build_deck.py --workshop example

# Commit and push
git add core_content/01_background_rationale.md
git commit -m "Fix typo in background section"
git push
```

## Best Practices

### Testing

**Always test before committing:**
```bash
# Build example deck
python3 tools/build_deck.py --workshop example

# Render to PDF
marp outputs/example_deck.md --theme-set fastr-theme.css --pdf

# Review the output
open outputs/example_deck.pdf
```

### Markdown Style

**Headings:**
- Use `#` for slide titles
- Use `##` for main headings
- Use `###` for subheadings

**Lists:**
- Use `-` for bullet points
- Use `1.` for numbered lists

**Images:**
```markdown
![Description](../assets/image.png)
```

**Slide Breaks:**
```markdown
---
```

### Variable Naming

When adding new template variables, use `{{UPPERCASE_WITH_UNDERSCORES}}`:

```markdown
# {{WORKSHOP_NAME}}
**Date:** {{DATE}}
**Custom Field:** {{NEW_VARIABLE}}
```

Update `build_deck.py` to support new variables:
```python
'NEW_VARIABLE': config.get('new_variable', ''),
```

### File Organization

**Core content:** Generic FASTR methodology only
**Custom slides:** Country/workshop-specific content only
**Assets:** Images used by multiple workshops
**Workshop folders:** Workshop-specific images and content

## Commit Message Guidelines

### Format

```
<type>: <short description>

<optional longer description>
<optional details>
```

### Types

- `content:` - Changes to core content
- `workshop:` - New or updated workshop
- `template:` - Changes to slide templates
- `tools:` - Updates to build scripts
- `docs:` - Documentation updates
- `fix:` - Bug fixes
- `style:` - Formatting/styling changes

### Examples

**Good:**
```
content: Update DQA section with 2025 indicators

Added new indicators for malaria and COVID-19 tracking.
Updated example visualizations.
```

```
workshop: Add Nigeria January 2025 workshop

3-day workshop in Abuja covering sections 1-6.
Includes custom slides on Nigeria DHIS2 implementation.
```

```
fix: Correct image path in coverage analysis

Changed relative path from ./assets/ to ../assets/
to match new folder structure.
```

**Avoid:**
```
updated stuff
fixed things
changes
```

## Working with Images

### Adding Images to Core Content

1. Place image in `assets/`:
   ```bash
   cp ~/Desktop/diagram.png assets/
   ```

2. Reference in markdown:
   ```markdown
   ![FASTR Approach Diagram](../assets/diagram.png)
   ```

3. Commit both:
   ```bash
   git add assets/diagram.png core_content/02_fastr_approach.md
   git commit -m "content: Add FASTR approach diagram"
   ```

### Adding Workshop-Specific Images

1. Place in workshop folder:
   ```bash
   cp ~/Desktop/nigeria_results.png workshops/2025_01_nigeria/
   ```

2. Reference in custom slides:
   ```markdown
   ![Nigeria Results](nigeria_results.png)
   ```

## Questions?

- Check the main [README.md](README.md)
- Review existing workshops in `workshops/`
- Contact the FASTR team

## Code of Conduct

- Be respectful and professional
- Test your changes before committing
- Write clear commit messages
- Coordinate with team for major changes
- Ask questions when uncertain

Thank you for contributing to FASTR!
