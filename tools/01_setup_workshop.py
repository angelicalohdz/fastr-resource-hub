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


# ═══════════════════════════════════════════════════════════════════════
# MODULE DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════
# These define the available core content modules and their topics

MODULES = {
    0: {
        'name': 'Introduction to FASTR',
        'folder': 'm0_introduction',
        'topics': [
            ('m0_1', 'Introduce FASTR approach'),
            ('m0_2', 'Overview of resources'),
            ('m0_3', 'Models of implementation'),
        ],
        'default': True,
    },
    1: {
        'name': 'Identify Questions & Indicators',
        'folder': 'm1_identify_questions_indicators',
        'topics': [
            ('m1_1', 'FASTR gaps and challenges'),
            ('m1_2', 'Development of data use case'),
            ('m1_3', 'Defining priority questions'),
            ('m1_4', 'Preparing for data extraction'),
        ],
        'default': False,
    },
    2: {
        'name': 'Data Extraction',
        'folder': 'm2_data_extraction',
        'topics': [
            ('m2_1', 'Why extract data'),
            ('m2_2', 'Tools for data extraction'),
        ],
        'default': True,
    },
    3: {
        'name': 'FASTR Analytics Platform',
        'folder': 'm3_fastr_analytics_platform',
        'topics': [
            ('m3_1', 'Overview of platform'),
            ('m3_2', 'Accessing platform'),
            ('m3_3', 'Setting up structure'),
            ('m3_4', 'Importing dataset'),
            ('m3_5', 'Installing and running modules'),
            ('m3_6', 'Creating new project'),
            ('m3_7', 'Creating visualizations'),
            ('m3_8', 'Creating reports'),
        ],
        'default': False,
    },
    4: {
        'name': 'Data Quality Assessment',
        'folder': 'm4_data_quality_assessment',
        'topics': [
            ('m4_1', 'Approach to DQA'),
            ('m4_2', 'Indicator completeness'),
            ('m4_3', 'Outliers'),
            ('m4_4', 'Internal consistency'),
            ('m4_5', 'Overall DQA score'),
            ('m4_6', 'Assessing DQ in platform'),
        ],
        'default': True,
    },
    5: {
        'name': 'Data Quality Adjustment',
        'folder': 'm5_data_quality_adjustment',
        'topics': [
            ('m5_1', 'Approach to DQ adjustment'),
            ('m5_2', 'Adjustment for outliers'),
            ('m5_3', 'Adjustment for completeness'),
            ('m5_4', 'Adjusting DQ in platform'),
        ],
        'default': True,
    },
    6: {
        'name': 'Data Analysis',
        'folder': 'm6_data_analysis',
        'topics': [
            ('m6_1', 'Service utilization'),
            ('m6_2', 'Surplus and disruption analyses'),
            ('m6_3', 'Service coverage'),
        ],
        'default': True,
    },
    7: {
        'name': 'Results Communication & Data Use',
        'folder': 'm7_results_communication',
        'topics': [
            ('m7_1', 'Analytical thinking & interpretation'),
            ('m7_2', 'Data visualization & communication'),
            ('m7_3', 'Using data for decision-making'),
            ('m7_4', 'Stakeholder engagement & advocacy'),
            ('m7_5', 'Practice: quarterly reporting'),
        ],
        'default': False,
    },
}


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


def select_modules():
    """Display modules and let user select which to include"""
    print("\n4. CORE CONTENT MODULES\n")
    print("   Select which modules to include in your workshop.")
    print("   Enter module numbers separated by commas (e.g., 0,2,4,5,6)")
    print("")

    # Show all modules with defaults marked
    defaults = []
    for num, module in MODULES.items():
        default_mark = "*" if module['default'] else " "
        topic_count = len(module['topics'])
        print(f"   [{default_mark}] {num}. {module['name']} ({topic_count} topics)")
        if module['default']:
            defaults.append(str(num))

    default_str = ",".join(defaults)
    print(f"\n   (* = included by default)")

    # Get selection
    selection = input(f"\n   Enter selection [{default_str}]: ").strip()
    if not selection:
        selection = default_str

    # Parse selection
    selected = []
    for item in selection.split(","):
        item = item.strip()
        if item.isdigit() and int(item) in MODULES:
            selected.append(int(item))

    if not selected:
        print("   No valid modules selected, using defaults.")
        selected = [int(d) for d in defaults]

    return sorted(selected)


def select_topics(module_num):
    """For a given module, let user select specific topics or all"""
    module = MODULES[module_num]
    topics = module['topics']

    print(f"\n   Module {module_num}: {module['name']}")
    print("   Select topics (press Enter for all, or enter numbers):\n")

    for i, (prefix, name) in enumerate(topics, 1):
        print(f"      {i}. {name} ({prefix})")

    all_nums = ",".join(str(i) for i in range(1, len(topics) + 1))
    selection = input(f"\n   Enter selection [{all_nums}]: ").strip()

    if not selection:
        # Return all topics for this module
        return [prefix for prefix, _ in topics]

    # Parse selection
    selected_topics = []
    for item in selection.split(","):
        item = item.strip()
        if item.isdigit():
            idx = int(item) - 1
            if 0 <= idx < len(topics):
                selected_topics.append(topics[idx][0])

    if not selected_topics:
        # Return all if invalid selection
        return [prefix for prefix, _ in topics]

    return selected_topics


def select_content():
    """Main content selection flow: modules then topics"""
    selected_modules = select_modules()

    print("\n" + "-" * 70)
    print("\n5. TOPIC SELECTION (optional)\n")
    print("   For each module, you can include all topics or select specific ones.")

    # Ask if they want to customize topics
    customize = input("\n   Customize topics within modules? [y/N]: ").strip().lower()

    deck_items = []

    if customize == 'y':
        for mod_num in selected_modules:
            topics = select_topics(mod_num)
            if len(topics) == len(MODULES[mod_num]['topics']):
                # All topics selected, use module prefix
                deck_items.append(f"m{mod_num}")
            else:
                # Specific topics selected
                deck_items.extend(topics)
    else:
        # Include all topics for each module
        for mod_num in selected_modules:
            deck_items.append(f"m{mod_num}")

    return deck_items


def format_deck_order(deck_content):
    """Format deck_order list for config.py with comments"""
    lines = []
    lines.append("        # --- Opening ---")
    lines.append("        'agenda',")
    lines.append("        'objectives.md',")
    lines.append("        'country-overview.md',")
    lines.append("")
    lines.append("        # --- Core Content (selected modules) ---")

    # Group items by module number for comments
    current_module = None
    for item in deck_content:
        # Extract module number
        if item.startswith('m'):
            parts = item.split('_')
            mod_num = int(parts[0][1:])  # m0 -> 0, m4_1 -> 4

            # Add module comment if new module
            if mod_num != current_module:
                current_module = mod_num
                mod_name = MODULES[mod_num]['name']
                lines.append(f"        # M{mod_num}: {mod_name}")

            lines.append(f"        '{item}',")

    # Add custom slides based on modules included
    lines.append("")
    lines.append("        # --- Custom slides (edit these) ---")

    # Check what modules are included to suggest relevant custom slides
    mod_nums = set()
    for item in deck_content:
        if item.startswith('m'):
            mod_nums.add(int(item.split('_')[0][1:]))

    lines.append("        'health-priorities.md',")
    if 4 in mod_nums or 5 in mod_nums:
        lines.append("        'dq-findings.md',")
    if 6 in mod_nums:
        lines.append("        'disruption-local.md',")
        lines.append("        'coverage-results.md',")
    lines.append("")
    lines.append("        # --- Closing ---")
    lines.append("        'next-steps.md',")

    return "\n".join(lines)


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

    # Content selection
    deck_content = select_content()

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
    # Modules use prefix notation: 'm0', 'm1', 'm2', etc.
    # Individual topics: 'm0_1', 'm4_2', etc.
    # Custom slides: 'objectives.md', 'country-overview.md', etc.
    #
    # Comment out any slides you don't want to include.

    'deck_order': [
{format_deck_order(deck_content)}
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
