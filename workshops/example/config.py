"""
═══════════════════════════════════════════════════════════════════════════════
                        WORKSHOP CONFIGURATION FILE
═══════════════════════════════════════════════════════════════════════════════

Workshop: FASTR Workshop - Example Country
Location: Capital City, Country
Date: January 15-17, 2025

To build your deck, run:
    python3 tools/03_build_deck.py --workshop example

═══════════════════════════════════════════════════════════════════════════════
"""

WORKSHOP_CONFIG = {

    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 1: BASIC WORKSHOP INFO
    # ═══════════════════════════════════════════════════════════════════════

    'workshop_id': 'example',
    'name': 'FASTR Workshop - Example Country',
    'date': 'January 15-17, 2025',
    'location': 'Capital City, Country',
    'facilitators': 'Dr. Smith, Dr. Jones',

    'contact_email': 'fastr@example.org',
    'website': 'https://fastr.org',


    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 2: YOUR DECK - What slides, in what order
    # ═══════════════════════════════════════════════════════════════════════
    #
    # Use module prefixes: m0, m1, m2, m3, m4, m5, m6, m7
    # Or specific topics: m4_1, m4_2, etc.
    # Custom slides: 'objectives.md', 'country-overview.md', etc.
    #
    # Modules:
    #   m0 = Introduction to FASTR
    #   m1 = Identify Questions & Indicators
    #   m2 = Data Extraction
    #   m3 = FASTR Analytics Platform
    #   m4 = Data Quality Assessment
    #   m5 = Data Quality Adjustment
    #   m6 = Data Analysis
    #   m7 = Results Communication

    'deck_order': [
        # --- Opening ---
        'agenda',
        'objectives.md',
        'country-overview.md',

        # --- Core Modules ---
        'm0',                    # Introduction to FASTR
        'health-priorities.md',
        'm2',                    # Data Extraction
        'm4',                    # Data Quality Assessment
        'dq-findings.md',
        'm5',                    # Data Quality Adjustment
        'm6',                    # Data Analysis
        'coverage-results.md',

        # --- Closing ---
        'next-steps.md',
    ],

    # Topics to exclude (optional)
    # 'exclude': ['m4_6'],     # Example: skip "Assessing DQ in Platform"


    # ═══════════════════════════════════════════════════════════════════════
    # SECTION 3: WORKSHOP SCHEDULE
    # ═══════════════════════════════════════════════════════════════════════

    'workshop_days': 2,

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
    # Fill in your country stats here. Use {variable_name} in your slides.
    # Example: {total_facilities} becomes "2,847" in the slides.

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
