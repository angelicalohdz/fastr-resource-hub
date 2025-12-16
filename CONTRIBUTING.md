# Contributing to FASTR Slide Builder

Thank you for contributing to the FASTR slide deck system! This guide will help you understand how to work with the repository effectively.

## Documentation

For detailed guides on writing slides, building decks, and local setup:

- **[Full Documentation](docs/)** - All guides and references
- **[Markdown Guide](docs/markdown-guide.md)** - Cheat sheet for writing Marp slides
- **[Building Decks](docs/building-decks.md)** - How to assemble and render presentations
- **[Local Setup](docs/local-setup.md)** - Installation instructions for working locally

---

## Quick Start (Choose Your Method)

### Option 1: 🚀 Fastest - Edit on GitHub.com (No Installation)

**Best for:** Simple content edits
**Time:** < 1 minute
**Steps:** Browse file → Click pencil → Edit → Commit

**Can edit:**
- Core content modules (`core_content/*.md`)
- Workshop configurations (`workshops/*/config.py`)
- Custom slides (`workshops/*/custom_slides.md`)

**Limitations:** Cannot build decks or preview FASTR theme locally

**Get started:** See [Editing on GitHub.com](#editing-on-githubcom) for detailed instructions

### Option 2: ⚡ Full Environment - GitHub Codespaces (No Installation)

**Best for:** Building decks, previewing FASTR theme
**Time:** 2-3 minutes
**Steps:** Code button → Codespaces tab → Create codespace → Wait 2min

**Pre-installed:**
- Python, Node.js, Marp CLI, Pandoc
- VS Code extensions
- FASTR theme ready to use

**Free tier:** 60 hours/month for personal accounts

**Get started:** See [Using GitHub Codespaces](#using-github-codespaces) for detailed instructions

### Option 3: 💻 Advanced - Local Setup (Requires Installation)

**Best for:** Local development preference
**Time:** 30+ minutes

**Requires installing:**
- Git
- Python 3.7+
- Visual Studio Code
- Node.js
- Marp CLI

**Get started:** See the **[Local Setup Guide](docs/local-setup.md)** for step-by-step installation instructions

## Table of Contents

- [Quick Start (Choose Your Method)](#quick-start-choose-your-method)
- [Editing on GitHub.com](#editing-on-githubcom)
- [Using GitHub Codespaces](#using-github-codespaces)
- [Types of Contributions](#types-of-contributions)
- [Workflow Guidelines](#workflow-guidelines)
- [Best Practices](#best-practices)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Working with Images](#working-with-images)

---

## Editing on GitHub.com

The easiest way to contribute is by editing files directly on GitHub.com - no installation required!

### Editing Existing Files

1. **Navigate to the file** you want to edit on [https://github.com/FASTR-Analytics/fastr-slide-builder](https://github.com/FASTR-Analytics/fastr-slide-builder)
   - For core content: Browse to `core_content/` and select a `.md` file
   - For workshop configs: Browse to `workshops/{workshop_id}/config.py`
   - For custom slides: Browse to `workshops/{workshop_id}/custom_slides.md`

2. **Click the pencil icon** (Edit this file) in the top right of the file view

3. **Make your changes** in the web editor
   - The editor supports markdown syntax highlighting
   - You can preview formatted markdown by clicking "Preview"

4. **Commit your changes:**
   - Scroll to the bottom "Commit changes" section
   - Write a descriptive commit message (see [Commit Message Guidelines](#commit-message-guidelines))
   - Choose "Commit directly to the main branch" for simple fixes
   - Or choose "Create a new branch" for major changes
   - Click "Commit changes"

### Creating New Workshop Folders

To create a new workshop folder on GitHub.com:

1. **Navigate to the `workshops/` folder**

2. **Click "Add file" → "Create new file"**

3. **In the filename box, type:**
   ```
   2025_01_yourcountry/config.py
   ```
   (GitHub automatically creates folders when you type `/`)

4. **Copy the example config:**
   - Open `workshops/example/config.py` in a new tab
   - Copy the contents
   - Paste into your new file
   - Update the configuration values

5. **Commit the new file**

6. **Repeat for `custom_slides.md`:**
   - Create `workshops/2025_01_yourcountry/custom_slides.md`
   - Add your custom content

### Uploading Images

1. **Navigate to your workshop folder** (e.g., `workshops/2025_01_yourcountry/`)

2. **Click "Add file" → "Upload files"**

3. **Drag and drop your image files** (e.g., `agenda.png`)

4. **Commit the upload**

### What You Can't Do on GitHub.com

- **Build decks** - Requires running Python scripts
- **Generate PDFs** - Requires Marp CLI
- **Preview with FASTR theme** - Requires local Marp setup

For these tasks, use [GitHub Codespaces](#using-github-codespaces) instead!

---

## Using GitHub Codespaces

GitHub Codespaces gives you a full development environment in your browser - no installation needed!

### First Time Setup

1. **Go to the repository:** [https://github.com/FASTR-Analytics/fastr-slide-builder](https://github.com/FASTR-Analytics/fastr-slide-builder)

2. **Click the green "Code" button**

3. **Click the "Codespaces" tab**

4. **Click "Create codespace on main"**

5. **Wait 2-3 minutes** while Codespaces:
   - Creates a cloud-based development environment
   - Installs Python, Node.js, Marp CLI, Pandoc
   - Installs VS Code extensions
   - Sets up the FASTR theme

6. **You're ready!** VS Code opens in your browser with everything configured

### Using Your Codespace

#### Editing Files

1. **Click on any file** in the Explorer sidebar to open it
2. **Make your changes** in the editor
3. **Files auto-save** (look for the dot next to filename to disappear)

#### Building a Deck

1. **Open the Terminal** (Terminal → New Terminal or press Ctrl+\`)

2. **Run the build command:**
   ```bash
   python3 tools/02_build_deck.py --workshop example
   ```

3. **Check the output** in `outputs/example_deck.md`

#### Rendering a PDF

1. **In the Terminal, run:**
   ```bash
   marp outputs/example_deck.md --theme-set fastr-theme.css --pdf
   ```

2. **Download the PDF:**
   - Right-click `outputs/example_deck.pdf` in the Explorer
   - Select "Download"

#### Previewing Slides

1. **Open any `.md` file** in the editor

2. **Open Marp preview:**
   - Click the Marp icon in the top right of the editor
   - Or use Command/Ctrl+Shift+V
   - Preview shows how slides will look

#### Committing Changes

1. **Click the Source Control icon** in the left sidebar (looks like a branch)

2. **Review your changes** - modified files are listed

3. **Stage changes:**
   - Hover over "Changes" and click the "+" icon
   - Or stage individual files

4. **Write a commit message** in the text box at the top

5. **Click "Commit"**

6. **Click "Sync Changes"** to push to GitHub

### Codespace Tips

- **Free hours:** Personal GitHub accounts get 60 hours/month free
- **Auto-save:** Files save automatically after a short delay
- **Auto-stop:** Codespaces stop after 30 minutes of inactivity (your work is saved)
- **Restart:** Click "Code" → "Codespaces" → select your codespace to reopen
- **Delete when done:** Manage codespaces at [github.com/codespaces](https://github.com/codespaces) to save hours
- **Works on tablets:** Codespaces works great on iPad/Android tablets!

### When to Use Codespaces vs Web Editor

| Task | Web Editor | Codespaces |
|------|-----------|-----------|
| Fix typos in content | ✅ Perfect | ⚠️ Overkill |
| Update workshop config | ✅ Perfect | ⚠️ Overkill |
| Add custom slides | ✅ Fine | ✅ Better (preview) |
| Build deck to test | ❌ Can't | ✅ Required |
| Generate PDF | ❌ Can't | ✅ Required |
| Preview FASTR theme | ❌ Can't | ✅ Required |
| Major refactoring | ⚠️ Difficult | ✅ Recommended |

**Rule of thumb:** Use Web Editor for quick edits, use Codespaces when you need to build/preview.

---

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
2. Test with example workshop (if using local setup or Codespaces):
   ```bash
   python3 tools/02_build_deck.py --workshop example
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
python3 tools/02_build_deck.py --workshop example

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
1. Copy example workshop (using Codespaces or local setup):
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
   python3 tools/02_build_deck.py --workshop 2025_01_yourcountry
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

---

## Workflow Guidelines

### Branch Strategy (Optional)

For major changes, use feature branches:

```bash
# Create feature branch
git checkout -b update-dqa-section

# Make changes
code core_content/04_data_quality_assessment.md

# Test
python3 tools/02_build_deck.py --workshop example

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
python3 tools/02_build_deck.py --workshop example

# Commit and push
git add core_content/01_background_rationale.md
git commit -m "Fix typo in background section"
git push
```

---

## Best Practices

### Testing

**Always test before committing:**
```bash
# Build example deck
python3 tools/02_build_deck.py --workshop example

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

---

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

---

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

---

## Questions?

- Check the [documentation](docs/) for detailed guides
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
