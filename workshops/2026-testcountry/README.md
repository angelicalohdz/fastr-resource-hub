# FASTR Workshop - TestCountry

**Location:** TestCity
**Date:** January 15-17, 2026
**Facilitators:** Test Facilitator

## Files

- `workshop.yaml` - Workshop configuration (modules, schedule, etc.)
- Custom slides to edit:
  - `objectives.md` - Workshop objectives
  - `country-overview.md` - Country context
  - `health-priorities.md` - Health priorities
  - `next-steps.md` - Action items

## Build Your Deck

```bash
# Build the deck (validates automatically)
python3 tools/02_build_deck.py --workshop 2026-testcountry

# Convert to PowerPoint (optional)
python3 tools/03_convert_pptx.py outputs/2026-testcountry_deck.md
```

## Country Outputs

Add your FASTR platform outputs to `media/outputs/` to include them in slides.
