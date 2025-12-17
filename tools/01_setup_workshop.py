#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════
                    FASTR WORKSHOP SETUP TOOL
═══════════════════════════════════════════════════════════════════════

Creates a new workshop folder with everything you need:
  - config.py (pre-filled with your details)
  - All custom slide templates (ready to edit)
  - Placeholder agenda image

Just run:
    python3 tools/01_setup_workshop.py

═══════════════════════════════════════════════════════════════════════
"""

import os
import sys
import shutil
import re


def get_input(prompt, default=None):
    """Get user input with optional default"""
    if default:
        result = input(f"{prompt} [{default}]: ").strip()
        return result if result else default
    else:
        while True:
            result = input(f"{prompt}: ").strip()
            if result:
                return result
            print("   This field is required.")


def create_workshop_id(name):
    """Generate a workshop ID from the name"""
    # Extract year if present, or use current year
    import datetime
    year = datetime.datetime.now().year

    # Try to find country name (last word usually)
    words = name.lower().split()
    country = words[-1] if words else "workshop"

    # Clean up
    country = re.sub(r'[^a-z0-9]', '', country)

    return f"{year}-{country}"


def main():
    # Determine base directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)

    print("\n" + "=" * 70)
    print("              FASTR WORKSHOP SETUP")
    print("=" * 70)
    print("\nThis will create a new workshop folder with all the files you need.")
    print("Just answer a few questions to get started.\n")
    print("-" * 70)

    # Gather workshop details
    print("\n1. BASIC INFORMATION\n")

    name = get_input("   Workshop name (e.g., 'FASTR Workshop - Kenya')")
    location = get_input("   Location (e.g., 'Nairobi, Kenya')")
    date = get_input("   Date (e.g., 'January 15-17, 2025')")
    facilitators = get_input("   Facilitator(s)", "TBD")

    # Generate workshop ID
    suggested_id = create_workshop_id(name)
    print(f"\n   Suggested folder name: {suggested_id}")
    workshop_id = get_input("   Workshop folder name", suggested_id)

    # Clean the workshop ID
    workshop_id = re.sub(r'[^a-z0-9_-]', '-', workshop_id.lower())

    # Check if folder exists
    workshop_dir = os.path.join(base_dir, "workshops", workshop_id)
    if os.path.exists(workshop_dir):
        print(f"\n   Warning: workshops/{workshop_id}/ already exists!")
        overwrite = input("   Overwrite? [y/N]: ").strip().lower()
        if overwrite != 'y':
            print("\n   Cancelled. Choose a different name.\n")
            sys.exit(0)
        shutil.rmtree(workshop_dir)

    # Optional details
    print("\n2. OPTIONAL DETAILS (press Enter to skip)\n")

    contact_email = get_input("   Contact email", "fastr@example.org")
    website = get_input("   Website", "https://fastr.org")

    # Workshop days
    print("\n3. WORKSHOP SCHEDULE\n")
    days_input = get_input("   How many days? (1, 2, or 3)", "2")
    try:
        workshop_days = int(days_input)
        if workshop_days not in [1, 2, 3]:
            workshop_days = 2
    except:
        workshop_days = 2

    # Create the workshop folder
    print("\n" + "-" * 70)
    print("\nCreating workshop folder...")

    os.makedirs(workshop_dir, exist_ok=True)

    # Copy custom slide templates
    templates_dir = os.path.join(base_dir, "templates", "custom_slides")
    if os.path.exists(templates_dir):
        for filename in os.listdir(templates_dir):
            if filename.endswith('.md'):
                src = os.path.join(templates_dir, filename)
                dst = os.path.join(workshop_dir, filename)
                shutil.copy2(src, dst)
                print(f"   + {filename}")

    # Create placeholder agenda
    agenda_path = os.path.join(workshop_dir, "agenda.png")
    open(agenda_path, 'w').close()  # Create empty file
    print("   + agenda.png (placeholder - replace with yours)")

    # Copy default FASTR outputs to workshop assets folder
    default_outputs_dir = os.path.join(base_dir, "assets", "fastr-outputs")
    workshop_outputs_dir = os.path.join(workshop_dir, "assets", "fastr-outputs")

    if os.path.exists(default_outputs_dir):
        os.makedirs(workshop_outputs_dir, exist_ok=True)
        copied_count = 0
        for filename in os.listdir(default_outputs_dir):
            if filename.endswith('.png'):
                src = os.path.join(default_outputs_dir, filename)
                dst = os.path.join(workshop_outputs_dir, filename)
                shutil.copy2(src, dst)
                copied_count += 1
        print(f"   + assets/fastr-outputs/ ({copied_count} default visualizations)")

        # Create README explaining these are defaults to replace
        assets_readme = '''# FASTR Visualizations

These are **default placeholder charts**. Replace them with your country's
actual FASTR outputs.

## How to update

1. Run your FASTR analysis for this country
2. Export the visualizations with the **same filenames**
3. Replace the files in this folder
4. Rebuild your deck - your charts will appear in the slides

## Files included

### Data Quality Assessment (Module 1)
- `m1_Proportion_of_completed_records.png` - Completeness by indicator
- `m1_Proportion_of_outliers.png` - Outlier detection results
- `m1_Proportion_of_sub-national_areas_meeting_consistency_criteria.png` - Consistency checks
- `m1_Overall_DQA_score.png` - Combined DQ score
- `m1_Mean_DQA_score.png` - Mean DQ score over time

### Data Adjustment (Module 2)
- `m2_Volume_change_due_to_data_quality_adjustments.png` - Impact of adjustments
- `m2_Change_in_service_volume_(Admin_area_2).png` - Service volume trends
'''
        assets_readme_path = os.path.join(workshop_outputs_dir, "README.md")
        with open(assets_readme_path, 'w') as f:
            f.write(assets_readme)
        print("   + assets/fastr-outputs/README.md")

    # Generate config.py
    config_content = f'''"""
═══════════════════════════════════════════════════════════════════════════════
                        WORKSHOP CONFIGURATION FILE
═══════════════════════════════════════════════════════════════════════════════

Workshop: {name}
Location: {location}
Date: {date}

To build your deck, run:
    python3 tools/03_build_deck.py --workshop {workshop_id}

═══════════════════════════════════════════════════════════════════════════════
"""

WORKSHOP_CONFIG = {{

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 1: BASIC WORKSHOP INFO
    # ═══════════════════════════════════════════════════════════════════════

    'workshop_id': '{workshop_id}',
    'name': '{name}',
    'date': '{date}',
    'location': '{location}',
    'facilitators': '{facilitators}',

    'contact_email': '{contact_email}',
    'website': '{website}',


    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 2: YOUR DECK - What slides, in what order
    # ═══════════════════════════════════════════════════════════════════════
    #
    # Built-in sessions: 'intro', 'extraction', 'dq_assessment', etc.
    # Your custom slides: 'objectives.md', 'country-overview.md', etc.
    #
    # Comment out any slides you don't want to include.

    'deck_order': [
        # --- Opening ---
        'agenda',
        'objectives.md',
        'country-overview.md',

        # --- Core Content ---
        'intro',
        'health-priorities.md',
        'extraction',
        'dq_assessment',
        'dq-findings.md',
        'dq_adjustment',
        'disruption',
        'disruption-local.md',
        'coverage',
        'coverage-results.md',

        # --- Closing ---
        'next-steps.md',
    ],


    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 3: WORKSHOP SCHEDULE
    # ═══════════════════════════════════════════════════════════════════════

    'workshop_days': {workshop_days},

    'tea_time': '10:45 AM',
    'lunch_time': '1:00 PM',
    'afternoon_tea_time': '3:30 PM',
    'day_start_time': '9:00 AM',

    'include_day_end_slides': True,
    'include_closing': True,
    'agenda_image': 'agenda.png',


    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 4: COUNTRY DATA
    # ═══════════════════════════════════════════════════════════════════════
    # Fill in your country stats here. Use {{variable_name}} in your slides.
    # Example: {{total_facilities}} becomes "2,847" in the slides.

    'country_data': {{
        # Health system
        'total_facilities': '[X,XXX]',
        'facilities_reporting': '[X,XXX]',
        'reporting_rate': '[XX%]',

        # Population
        'total_population': '[XX million]',
        'women_reproductive_age': '[X.X million]',
        'under5_population': '[X.X million]',
        'expected_pregnancies': '[XXX,XXX]',
        'expected_births': '[XXX,XXX]',

        # Survey data
        'last_survey': '[DHS/MICS YYYY]',
        'survey_year': '[YYYY]',

        # Coverage - Survey
        'survey_anc1': '[XX%]',
        'survey_anc4': '[XX%]',
        'survey_sba': '[XX%]',
        'survey_penta1': '[XX%]',
        'survey_penta3': '[XX%]',
        'survey_measles': '[XX%]',

        # Coverage - FASTR estimates (fill after analysis)
        'fastr_anc1': '[XX%]',
        'fastr_anc4': '[XX%]',
        'fastr_sba': '[XX%]',
        'fastr_penta1': '[XX%]',
        'fastr_penta3': '[XX%]',
        'fastr_measles': '[XX%]',

        # Data quality
        'completeness_overall': '[XX%]',
        'outliers_detected': '[XXX]',
        'consistency_pass_rate': '[XX%]',

        # Add your own variables as needed...
    }},

}}
'''

    config_path = os.path.join(workshop_dir, "config.py")
    with open(config_path, 'w') as f:
        f.write(config_content)
    print("   + config.py")

    # Create README
    readme_content = f'''# {name}

**Location:** {location}
**Date:** {date}
**Facilitators:** {facilitators}

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
python3 tools/02_check_workshop.py --workshop {workshop_id}

# Build the deck
python3 tools/03_build_deck.py --workshop {workshop_id}
```

## To convert to PowerPoint

```bash
python3 tools/04_convert_to_pptx.py outputs/{workshop_id}_deck.md
```

## Country-specific assets

To use your own FASTR outputs instead of defaults:
1. Create `assets/fastr-outputs/` in this folder
2. Copy your PNG files with the same names as the defaults
3. The build script will automatically use your versions
'''

    readme_path = os.path.join(workshop_dir, "README.md")
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    print("   + README.md")

    # Success!
    print("\n" + "=" * 70)
    print("                    SUCCESS!")
    print("=" * 70)
    print(f"\n   Workshop created: workshops/{workshop_id}/")
    print(f"\n   Next steps:")
    print(f"   1. Edit the custom slide .md files with your content")
    print(f"   2. Replace agenda.png with your agenda image")
    print(f"   3. Fill in country_data in config.py")
    print(f"   4. Check and build:")
    print(f"\n      python3 tools/02_check_workshop.py --workshop {workshop_id}")
    print(f"      python3 tools/03_build_deck.py --workshop {workshop_id}")

    print(f"\n   Country visualizations:")
    print(f"   Default charts are in assets/fastr-outputs/")
    print(f"   Replace them with your country's FASTR outputs.")

    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled.\n")
        sys.exit(0)
