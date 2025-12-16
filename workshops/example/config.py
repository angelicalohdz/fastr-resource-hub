"""
Example Workshop Configuration

This file defines the settings for a specific workshop.
Copy this template to create new workshops.
"""

WORKSHOP_CONFIG = {
    # Workshop metadata
    'workshop_id': 'example',
    'name': 'FASTR Workshop - Example Country',
    'date': 'January 15-17, 2025',
    'location': 'Capital City, Country',
    'facilitators': 'Dr. Smith, Dr. Jones',

    # Contact information
    'contact_email': 'fastr@example.org',
    'website': 'https://fastr.org',

    # Break times
    'tea_resume_time': '10:45 AM',
    'lunch_resume_time': '2:00 PM',

    # Core sections to include (1-7)
    # 1: Background & Rationale
    # 2: FASTR Approach
    # 3: Data Extraction
    # 4: Data Quality Assessment
    # 5: Service Utilization
    # 6: Coverage Analysis
    # 7: Facility Assessments
    'sections': [1, 2, 3, 4, 5, 6],

    # Include optional components
    'include_breaks': True,
    'include_agenda': True,
    'include_closing': True,

    # Custom slides (relative to workshop folder)
    # Example: ['custom_intro.md', 'country_results.md']
    'custom_slides': [],

    # Agenda image (place in workshop folder)
    'agenda_image': 'agenda.png',
}
