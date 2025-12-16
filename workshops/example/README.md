# Example Workshop

This is a template workshop folder. Copy this folder to create a new workshop.

## Files in this folder:

- `config.py` - Workshop configuration (edit this!)
- `agenda.png` - Agenda image (replace with your own)
- `custom_slides.md` (optional) - Add country-specific content

## To create a new workshop:

1. Copy this folder:
   ```bash
   cp -r workshops/example workshops/2025_01_yourcountry
   ```

2. Edit `config.py` with your workshop details

3. Replace `agenda.png` with your agenda image

4. Add custom slides if needed

5. Build your deck:
   ```bash
   python3 tools/build_deck.py --workshop 2025_01_yourcountry
   ```
