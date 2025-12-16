# Example Workshop

This is a template workshop folder. Copy this folder to create a new workshop.

## Files in this folder:

- `config.py` - Workshop configuration (edit this!)
- `agenda.png` - Agenda image (replace with your own)

## To create a new workshop:

1. Copy this folder:
   ```bash
   cp -r workshops/example workshops/2025-01-yourcountry
   ```

2. Edit `config.py` with your workshop details

3. Replace `agenda.png` with your agenda image

4. Add custom slides (optional but recommended):
   ```bash
   # Copy the templates you need
   cp templates/custom_slides/objectives.md workshops/2025-01-yourcountry/
   cp templates/custom_slides/country-overview.md workshops/2025-01-yourcountry/
   cp templates/custom_slides/next-steps.md workshops/2025-01-yourcountry/
   # ... add more as needed
   ```

5. Edit the custom slides with your country-specific content

6. Uncomment the slides in your `config.py` deck_order list

7. Build your deck:
   ```bash
   python3 tools/02_build_deck.py --workshop 2025-01-yourcountry
   ```

## Available custom slide templates:

See `templates/custom_slides/` for starter templates:
- `objectives.md` - Workshop learning objectives
- `country-overview.md` - Country health system context
- `health-priorities.md` - National health priorities
- `dq-findings.md` - Data quality findings
- `disruption-local.md` - Local disruption patterns
- `coverage-results.md` - Coverage analysis results
- `next-steps.md` - Action items and follow-up
