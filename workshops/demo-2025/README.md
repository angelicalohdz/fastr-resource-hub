# Demo Workshop - FASTR Slide Builder

This is a demonstration workshop that showcases all features of the FASTR Slide Builder system.

## Purpose

Use this demo to:
- **Learn the system** - See all features in action
- **Train your team** - Show them how it works
- **Test changes** - Try new features without affecting real workshops
- **Template for new workshops** - Copy and modify for your own use

## What's Included

### Files in this folder:

1. **config.py** - Workshop configuration
   - Shows all available options
   - Demonstrates variable substitution
   - Comments explain each setting

2. **demo-features.md** - Custom slides demonstrating markdown
   - Headings, lists, formatting
   - Images, code blocks, tables
   - Columns, callouts, emojis
   - Special formatting examples

3. **demo-tips.md** - Custom slides with best practices
   - Tips for building workshops
   - Recommended workflows
   - Version control guidance
   - Presentation day checklist

4. **agenda.png** - Placeholder agenda image
   - Replace with your own agenda for real workshops

## Building the Demo

### Quick Start

```bash
# Build the demo deck
python3 tools/build_deck.py --workshop demo-2025

# Render to PDF (recommended)
marp outputs/demo-2025_deck.md --theme-set fastr-theme.css --pdf

# Open the PDF
open outputs/demo-2025_deck.pdf
```

### What You'll Get

The built deck includes:
1. **Title slide** - "FASTR Slide Builder Demo Workshop"
2. **Agenda slide** - With placeholder image
3. **Core FASTR content** - Sections 1, 2, 4, 5
4. **Custom feature demos** - From demo-features.md
5. **Tips and best practices** - From demo-tips.md
6. **Break slides** - Tea and lunch breaks
7. **Closing slides** - Thank you and contact info

**Total:** ~50-60 slides showing everything the system can do!

## Using This for Training

### Presentation Flow

**Recommended for team training:**

1. **Introduction (5 min)**
   - Show title slide
   - Explain what FASTR Slide Builder is

2. **System Overview (10 min)**
   - Show core FASTR content slides
   - Explain how content is modular

3. **Features Demo (15 min)**
   - Walk through demo-features.md slides
   - Show markdown capabilities
   - Explain what's possible

4. **Best Practices (10 min)**
   - Walk through demo-tips.md slides
   - Emphasize workflow importance
   - Show how to avoid common mistakes

5. **Live Demo (20 min)**
   - Open Codespace together
   - Edit this demo workshop
   - Build and render
   - Commit and push changes

6. **Q&A (10 min)**
   - Answer questions
   - Help team get started

## Customizing for Your Demo

### To personalize:

1. **Edit config.py:**
   ```python
   'name': 'Your Organization - Demo Workshop',
   'location': 'Your City, Country',
   'facilitators': 'Your Name',
   ```

2. **Replace agenda.png:**
   - Create your own agenda image
   - Save as `agenda.png` in this folder

3. **Modify custom slides:**
   - Edit demo-features.md with your examples
   - Edit demo-tips.md with your organization's practices

4. **Rebuild:**
   ```bash
   python3 tools/build_deck.py --workshop demo-2025
   marp outputs/demo-2025_deck.md --theme-set fastr-theme.css --pdf
   ```

## Using as Template

### To create a new workshop from this demo:

```bash
# Copy the demo folder
cp -r workshops/demo-2025 workshops/2025-XX-country

# Edit the new config
code workshops/2025-XX-country/config.py

# Customize
# - Change workshop details
# - Select different core sections
# - Modify custom slides
# - Add your agenda image

# Build your new workshop
python3 tools/build_deck.py --workshop 2025-XX-country
```

## Technical Details

### Config Settings Used

- **Sections:** 1, 2, 4, 5 (selective, not all 7)
- **Breaks:** Enabled (shows at 10:30 AM and 2:00 PM)
- **Agenda:** Enabled (requires agenda.png)
- **Custom slides:** 2 files demonstrating features
- **Closing:** Enabled with contact information

### Variable Substitution

The config.py shows how these variables get replaced:
- `{{WORKSHOP_NAME}}` → "FASTR Slide Builder Demo Workshop"
- `{{DATE}}` → "December 2025"
- `{{LOCATION}}` → "Online / Your Location"
- `{{FACILITATORS}}` → "FASTR Team"
- `{{TEA_RESUME_TIME}}` → "10:30 AM"
- `{{LUNCH_RESUME_TIME}}` → "2:00 PM"
- `{{CONTACT_EMAIL}}` → "fastr@example.org"
- `{{WEBSITE}}` → Repository URL

## Troubleshooting

### "Image not found" error?
- Make sure you have `agenda.png` in this folder
- Or set `'include_agenda': False` in config.py

### Slides look wrong?
- Make sure you're using: `--theme-set fastr-theme.css`
- Run from repository root, not from workshops folder

### Can't build?
- Check you're in the repository root
- Verify Python 3 is installed: `python3 --version`
- Check the workshop ID matches folder name

## Next Steps

After reviewing this demo:

1. ✅ Read the documentation in `docs/`
2. ✅ Try building the demo yourself
3. ✅ Create your own workshop folder
4. ✅ Share with your team!

**Happy presenting!** 🎉
