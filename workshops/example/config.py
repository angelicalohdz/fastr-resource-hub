"""
═══════════════════════════════════════════════════════════════════════════════
                        WORKSHOP CONFIGURATION FILE
═══════════════════════════════════════════════════════════════════════════════

This file defines all the settings for your workshop slide deck.

HOW TO USE:
1. Copy this entire 'example' folder to a new folder with your workshop name
   Example: cp -r workshops/example workshops/2025-03-kenya

2. Edit this config.py with your workshop details

3. Run: python3 tools/02_build_deck.py

═══════════════════════════════════════════════════════════════════════════════
"""

WORKSHOP_CONFIG = {

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 1: BASIC WORKSHOP INFO
    # ═══════════════════════════════════════════════════════════════════════
    # This information appears on the title slide and closing slides

    'workshop_id': 'example',                          # Folder name (no spaces!)
    'name': 'FASTR Workshop - Example Country',        # Full workshop title
    'date': 'January 15-17, 2025',                     # Workshop dates
    'location': 'Capital City, Country',               # City and country
    'facilitators': 'Dr. Smith, Dr. Jones',            # Lead facilitator names

    # Contact info (shown on closing slide)
    'contact_email': 'fastr@example.org',
    'website': 'https://fastr.org',


    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 2: YOUR DECK - What slides, in what order
    # ═══════════════════════════════════════════════════════════════════════
    #
    # List everything you want in your deck, in order.
    # - Built-in sessions: 'intro', 'extraction', 'dq_assessment', etc.
    # - Your custom slides: 'objectives.md', 'country-data.md', etc.
    #
    # Just put your .md files wherever you want them to appear!
    #
    # AVAILABLE BUILT-IN SESSIONS:
    # ┌──────────────────────────────────────────────────────────────────────┐
    # │  'agenda'        = Agenda slide (needs agenda.png in your folder)    │
    # │  'intro'         = Background & FASTR Approach (~30 min)             │
    # │  'extraction'    = Data Extraction from DHIS2 (~45 min)              │
    # │  'dq_assessment' = Data Quality Assessment (~90 min)                 │
    # │  'dq_adjustment' = Data Adjustment Methods (~60 min)                 │
    # │  'disruption'    = Service Disruption Detection (~90 min)            │
    # │  'coverage'      = Coverage Analysis (~90 min)                       │
    # │  'facility'      = Facility Assessments (~30 min)                    │
    # └──────────────────────────────────────────────────────────────────────┘
    #
    # CUSTOM SLIDES:
    # Copy templates from templates/custom_slides/ to your workshop folder,
    # customize them, then add them to deck_order where you want them.

    'deck_order': [
        # --- Opening ---
        'agenda',
        # 'objectives.md',        # ← Copy from templates/custom_slides/
        # 'country-overview.md',  # ← Copy from templates/custom_slides/

        # --- Core Content ---
        'intro',
        # 'health-priorities.md', # ← Copy from templates/custom_slides/
        'extraction',
        'dq_assessment',
        # 'dq-findings.md',       # ← Copy from templates/custom_slides/
        'dq_adjustment',
        'disruption',
        # 'disruption-local.md',  # ← Copy from templates/custom_slides/
        'coverage',
        # 'coverage-results.md',  # ← Copy from templates/custom_slides/

        # --- Closing ---
        # 'next-steps.md',        # ← Copy from templates/custom_slides/
    ],


    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 3: WORKSHOP SCHEDULE & BREAKS
    # ═══════════════════════════════════════════════════════════════════════
    # How many days? Set to None to be prompted when building.

    'workshop_days': None,  # None = prompt me, or 1, 2, 3

    # Break times (shown on break slides)
    'tea_time': '10:45 AM',
    'lunch_time': '1:00 PM',
    'afternoon_tea_time': '3:30 PM',

    # What time does each day start? (for day-end slides)
    'day_start_time': '9:00 AM',

    # Include "See you tomorrow" slides between days?
    'include_day_end_slides': True,


    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 4: CLOSING SLIDES
    # ═══════════════════════════════════════════════════════════════════════

    # Include "Thank You" and contact information slides at the end?
    'include_closing': True,

    # Agenda image filename (must be in your workshop folder)
    'agenda_image': 'agenda.png',


    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 5: COUNTRY DATA
    # ═══════════════════════════════════════════════════════════════════════
    # Fill in your country stats here. Use {{variable_name}} in your slides.
    # Example: {{total_facilities}} becomes "2,847" in the slides.

    'country_data': {
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
    },

}
