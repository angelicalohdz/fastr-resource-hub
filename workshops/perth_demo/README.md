# Demo Workshop

**Location:** Perth, Australia
**Date:** December 17
**Facilitators:** claire

## Files in this folder

- `config.py` - Workshop configuration
- `agenda.png` - Replace with your agenda image
- Custom slides (edit these with your content):
  - `objectives.md` - Workshop objectives
  - `country-overview.md` - Country context
  - `health-priorities.md` - Health priorities
  - `dq-findings.md` - Data quality findings
  - `disruption-local.md` - Disruption analysis
  - `coverage-results.md` - Coverage results
  - `next-steps.md` - Action items

## To build your deck

```bash
# Optional: Check setup first
python3 tools/02_check_workshop.py --workshop perth_demo

# Build the deck
python3 tools/03_build_deck.py --workshop perth_demo
```

## To convert to PowerPoint

```bash
python3 tools/04_convert_to_pptx.py outputs/perth_demo_deck.md
```

## Country-specific assets

To use your own FASTR outputs instead of defaults:
1. Create `assets/fastr-outputs/` in this folder
2. Copy your PNG files with the same names as the defaults
3. The build script will automatically use your versions
