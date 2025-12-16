---
marp: true
theme: default
paginate: true
style: |
  @import url('../fastr-theme.css');
---

<!--
_class: title
_paginate: false
-->

# Welcome to FASTR Slide Builder

**Your Guide to Creating Professional FASTR Workshop Decks**

---

## What is FASTR Slide Builder?

A streamlined tool for creating consistent, professional workshop presentations.

**What it does:**
- Combines reusable core content with workshop-specific slides
- Maintains FASTR branding across all presentations
- Simplifies deck creation with Python automation
- Outputs beautiful PDFs with consistent styling

**Why we built it:**
- Stop copying/pasting slides between decks
- Ensure consistent messaging across workshops
- Make it easy for anyone to contribute
- Reduce time spent on formatting

---

## What You'll Learn Today

By the end of this session, you'll be able to:

1. Choose the best contribution method for your needs
2. Edit content using GitHub (no software needed!)
3. Build a complete workshop deck
4. Generate professional PDFs
5. Know where to get help

**Let's dive in!**

---

<!-- _class: section -->

# Three Ways to Contribute
### Choose Your Adventure

---

## Option 1: GitHub Web Editor

**Best for:** Quick text edits to existing content

**Time to start:** < 1 minute
**Difficulty:** Easiest
**What you can do:** Edit markdown files directly
**What you can't do:** Build decks, preview styling, run Python scripts

**When to use:**
- Fixing typos
- Updating workshop dates/details
- Minor content tweaks

---

## Option 2: GitHub Codespaces (RECOMMENDED)

**Best for:** Most contributors - full editing and building

**Time to start:** 2-3 minutes (one-time setup)
**Difficulty:** Easy
**What you can do:** Everything! Edit, build, preview, generate PDFs
**Software needed:** Just a web browser!

**Why we recommend this:**
- No installation required
- Pre-configured environment
- Full VS Code experience in your browser
- Preview FASTR theme in real-time
- Build and test locally before committing

---

## Option 3: Local Setup

**Best for:** Power users who prefer working offline

**Time to start:** 30+ minutes
**Difficulty:** Advanced
**Requirements:** Python 3.8+, Marp CLI, Git
**Benefits:** Work offline, use your preferred IDE

**When to use:**
- You already have everything installed
- You prefer working locally
- You need to work without internet

**Note:** For most people, Codespaces is faster and easier!

---

<!-- _class: section -->

# Live Demo: Web Editor
### The 1-Minute Method

---

## GitHub Web Editor: Step-by-Step

**Step 1:** Navigate to the file on GitHub
- Go to https://github.com/FASTR-Analytics/fastr-slide-builder
- Browse to the file you want to edit
- Example: `workshops/example/custom_slides.md`

**Step 2:** Click the pencil icon (Edit this file)

**Step 3:** Make your changes in the editor

**Step 4:** Scroll down and click "Commit changes"
- Add a descriptive commit message
- Click "Commit changes" button

**That's it!** Your changes are saved.

---

## What You Can Edit (Web Editor)

**Core Content** (`core_content/` folder)
- Background & rationale slides
- FASTR approach methodology
- Data extraction process
- Etc.

**Workshop Configs** (`workshops/*/config.py`)
- Workshop title, date, location
- Which core modules to include
- Custom agenda images

**Custom Slides** (`workshops/*/custom_slides.md`)
- Workshop-specific content
- Additional case studies
- Local context

---

<!-- _class: section -->

# Live Demo: Codespaces
### The Full-Featured Method (RECOMMENDED)

---

## GitHub Codespaces: Step-by-Step

**Step 1:** Open Codespaces
- Go to https://github.com/FASTR-Analytics/fastr-slide-builder
- Click the green "Code" button
- Click "Codespaces" tab
- Click "Create codespace on main"

**Step 2:** Wait ~2 minutes
- GitHub creates your personal workspace
- Installs Python, Marp, and all dependencies
- Opens VS Code in your browser

**Step 3:** Start working!
- Your browser-based VS Code is ready
- Everything is pre-configured
- No installation needed!

---

## What Happens During Setup?

While you wait, Codespaces is:

1. Creating a virtual Linux environment
2. Installing Python 3.8+
3. Installing Marp CLI for presentations
4. Installing all Python dependencies
5. Configuring VS Code extensions
6. Setting up FASTR theme preview

**First time:** ~2-3 minutes
**Next time:** ~30 seconds (it saves your workspace!)

---

## Working in Codespaces

**Editing files:**
- Click files in left sidebar to open
- Edit just like VS Code
- Save with Cmd/Ctrl+S

**Preview markdown:**
- Open any `.md` file
- Press Cmd/Ctrl+K V
- See formatted preview with FASTR styling

**Terminal access:**
- View → Terminal (or Ctrl+`)
- Run any command you need
- Build decks, generate PDFs, etc.

---

## Building Your First Deck

Open the terminal (Ctrl+`) and run:

```bash
python3 tools/02_build_deck.py --workshop example
```

**What happens:**
1. Reads `workshops/example/config.py`
2. Combines templates + core content + custom slides
3. Generates `outputs/example_deck.md`

**Check the output:**
```bash
ls -lh outputs/
# You should see example_deck.md
```

---

## Viewing Your Built Deck

**Option 1: Open in Codespaces**
- Open `outputs/example_deck.md`
- Press Cmd/Ctrl+K V to preview
- Navigate with arrow keys
- See all slides with FASTR styling!

**Option 2: Generate PDF (recommended)**
- See next slide!

---

<!-- _class: section -->

# Converting to PDF
### The Professional Output (RECOMMENDED)

---

## Why PDF?

**Consistent styling**
- FASTR theme applied perfectly
- No font issues
- No missing images
- Looks the same everywhere

**Easy sharing**
- No special software needed
- Works on any device
- Professional appearance

**Reliable**
- No conversion quirks
- No broken layouts
- What you see is what you get

---

## Generate PDF: The Command

In your Codespaces terminal, run:

```bash
marp outputs/example_deck.md \
  --theme-set fastr-theme.css \
  --pdf
```

**What it does:**
1. Reads your markdown deck
2. Applies FASTR theme (colors, fonts, layout)
3. Generates `outputs/example_deck.pdf`

**Result:** Professional PDF ready to present!

**Download it:**
- Right-click on `outputs/example_deck.pdf`
- Click "Download"
- Open on your computer

---

## Alternative: PowerPoint (Trickier)

We also have a PowerPoint converter, but it's more complex:

```bash
python3 tools/03_convert_to_pptx.py \
  outputs/example_deck.md \
  outputs/example_deck.pptx
```

**Challenges:**
- May need manual formatting fixes
- Images sometimes need adjustment
- Spacing can be inconsistent

**Recommendation:** Use PDF unless you specifically need editable PowerPoint.

---

<!-- _class: section -->

# Quick Markdown Tips
### Everything You Need to Know

---

## Essential Markdown Syntax

**Start a new slide:**
```markdown
---
```

**Headings:**
```markdown
# Main Title (H1)
## Section Heading (H2)
### Subsection (H3)
```

**Lists:**
```markdown
- Bullet point
- Another point
  - Nested point
```

**Bold and italic:**
```markdown
**bold text**
*italic text*
```

---

## Adding Images

```markdown
![Image description](path/to/image.png)
```

**Examples:**
```markdown
![FASTR Logo](assets/fastr-logo.png)
![Workshop Agenda](workshops/example/agenda.png)
```

**Tips:**
- Use relative paths from repository root
- Add images to `assets/` or your workshop folder
- Include descriptive alt text

---

## Links and Code

**Links:**
```markdown
[Link text](https://example.com)
[Documentation](docs/building-decks.md)
```

**Code blocks:**
````markdown
```python
def hello():
    print("Hello FASTR!")
```
````

**Inline code:**
```markdown
Run `python3 build_deck.py` to start
```

---

## Special FASTR Slides

**Section divider slide:**
```markdown
<!-- _class: section -->
# Major Section Title
### Optional subtitle
```

**Title slide (first slide):**
```markdown
<!--
_class: title
_paginate: false
-->
# Workshop Title
```

**Want more?** See `docs/markdown-guide.md` for complete reference!

---

<!-- _class: section -->

# Getting Help
### Resources & Support

---

## Documentation

**In the repository:**

- `README.md` - Repository overview and quick start
- `docs/markdown-guide.md` - Complete markdown reference
- `docs/building-decks.md` - How to build and customize decks
- `docs/local-setup.md` - Local installation guide
- `CONTRIBUTING.md` - Contribution guidelines

**Pro tip:** Open these in Codespaces for easy reference while you work!

---

## Quick Reference

**Build a deck:**
```bash
python3 tools/02_build_deck.py --workshop example
```

**Generate PDF:**
```bash
marp outputs/example_deck.md --theme-set fastr-theme.css --pdf
```

**Generate HTML:**
```bash
marp outputs/example_deck.md --html -o outputs/example.html
```

**Preview in Codespaces:**
- Open any `.md` file
- Press Cmd/Ctrl+K V

---

## Get Support

**Repository:**
https://github.com/FASTR-Analytics/fastr-slide-builder

**Found a bug?**
- Open an issue on GitHub
- Describe what you expected vs. what happened
- Include error messages if any

**Have a question?**
- Check the documentation first
- Ask your team lead
- Open a GitHub discussion

**Want to contribute?**
- Read `CONTRIBUTING.md`
- Fork the repository
- Submit a pull request

---

<!-- _class: section -->

# Practice Exercise
### Your Turn to Try!

---

## Let's Build Something Together!

**Your mission:**

1. Open GitHub Codespaces for the repository
2. Edit `workshops/example/custom_slides.md`
3. Add a new slide with:
   - Your name
   - Your role
   - One thing you learned today
4. Build the deck: `python3 tools/02_build_deck.py --workshop example`
5. Generate PDF: `marp outputs/example_deck.md --theme-set fastr-theme.css --pdf`
6. Download and view your creation!

**Time:** 10-15 minutes

**Need help?** Raise your hand!

---

<!--
_class: title
_paginate: false
-->

# Thank You!

**Questions?**

Remember:
- Use Codespaces for easiest experience
- Generate PDFs for professional output
- Check docs/ folder for detailed guides
- Don't hesitate to ask for help!

**Happy deck building!**
