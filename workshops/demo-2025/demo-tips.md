---

# Tips for Building Great Workshops

Quick tips for creating effective FASTR workshop presentations

---

# Tip 1: Start Simple

**For your first workshop:**
- Use the example workshop as template
- Copy and modify the config.py
- Don't add too many custom slides initially
- Build and test frequently

```bash
# Quick build to test
python3 tools/build_deck.py --workshop your-workshop
```

---

# Tip 2: Organize Your Content

**Recommended workshop structure:**

1. **Title slide** (automatic)
2. **Agenda** (automatic if you add agenda.png)
3. **Core FASTR content** (select 3-5 sections)
4. **Break slides** (automatic if enabled)
5. **Custom content** (your specific examples)
6. **Closing** (automatic)

---

# Tip 3: Use Custom Slides Wisely

**Good uses for custom slides:**
- Country-specific examples
- Recent results or case studies
- Local context and challenges
- Q&A or discussion prompts

**Keep them focused** - one topic per slide!

---

# Tip 4: Managing Images

**Best practices:**

✅ **Do:**
- Save shared images in `assets/`
- Save workshop-specific images in your workshop folder
- Use descriptive filenames: `nigeria-results-2024.png`
- Keep images reasonably sized (< 2 MB)

❌ **Don't:**
- Use huge image files (slows everything down)
- Use spaces in filenames (use dashes instead)

---

# Tip 5: Building Process

**Recommended workflow:**

```bash
# 1. Create workshop folder
cp -r workshops/example workshops/2025-01-kenya

# 2. Edit config
code workshops/2025-01-kenya/config.py

# 3. Add custom slides if needed
code workshops/2025-01-kenya/custom-slides.md

# 4. Build
python3 tools/build_deck.py --workshop 2025-01-kenya

# 5. Render to PDF (recommended!)
marp outputs/2025-01-kenya_deck.md --theme-set fastr-theme.css --pdf

# 6. Review the PDF
open outputs/2025-01-kenya_deck.pdf
```

---

# Tip 6: Testing Your Deck

**Before your workshop:**

1. ✅ Build the deck
2. ✅ Generate PDF
3. ✅ Review every slide
4. ✅ Check images load correctly
5. ✅ Test on presentation computer
6. ✅ Have backup (USB drive with PDF)

---

# Tip 7: Version Control

**Save your work properly:**

```bash
# After creating/editing your workshop
git add workshops/2025-01-kenya/
git commit -m "Add Kenya January 2025 workshop"
git push origin main
```

**Don't commit:**
- Generated files (outputs/*.md, outputs/*.pdf)
- These are gitignored automatically

---

# Tip 8: Collaboration

**Working with teammates:**

1. **Always pull first:**
   ```bash
   git pull origin main
   ```

2. **Make your changes**

3. **Commit and push:**
   ```bash
   git add workshops/your-workshop/
   git commit -m "Update workshop slides"
   git push origin main
   ```

4. **Communicate** - Tell team what you changed!

---

# Tip 9: Presentation Day

**Checklist:**

- [ ] PDF generated and tested
- [ ] Backup copy on USB drive
- [ ] Laptop charged
- [ ] HDMI/display adapters ready
- [ ] Presentation mode tested
- [ ] Agenda slide reflects actual timing
- [ ] Contact info on closing slide is correct

---

# Tip 10: Getting Help

**Resources:**

📚 **Documentation:**
- [Markdown Guide](../../docs/markdown-guide.md)
- [Building Decks](../../docs/building-decks.md)
- [Codespaces Workflow](../../docs/codespaces-workflow.md)

💬 **Ask your team:**
- Share your workshop folder for review
- Get feedback before presenting

🔧 **Technical issues:**
- Check troubleshooting sections in docs
- Review example workshop for reference

---

# Ready to Build Your Own?

**Next steps:**

1. Copy the `demo-2025` or `example` folder
2. Rename to your workshop: `2025-XX-country`
3. Edit `config.py` with your details
4. Add your custom content
5. Build and test!

**Good luck with your workshop!** 🚀

---
