"""
DEMO Workshop Configuration

This is a demonstration workshop showing all features of the FASTR Slide Builder.
Use this to learn the system or demonstrate to your team!
"""

WORKSHOP_CONFIG = {
    # Workshop identification
    'workshop_id': 'demo-2025',
    'name': 'FASTR Slide Builder Demo Workshop',
    'date': 'December 2025',
    'location': 'Online / Your Location',
    'facilitators': 'FASTR Team',

    # Contact information (appears in closing slides)
    'contact_email': 'fastr@example.org',
    'website': 'https://github.com/FASTR-Analytics/fastr-slide-builder',

    # Break times (for break slides)
    'tea_resume_time': '10:30 AM',
    'lunch_resume_time': '2:00 PM',

    # Core sections to include (1-7)
    # This demo includes a selection to show variety
    'sections': [
        1,  # Background & Rationale - What is FASTR?
        2,  # FASTR Approach - Overview
        4,  # Data Quality Assessment
        5,  # Service Utilization
    ],

    # Optional components
    'include_breaks': True,      # Include tea and lunch break slides
    'include_agenda': True,      # Include agenda slide (needs agenda.png)
    'include_closing': True,     # Include thank you and contact slides

    # Custom slides (files in this workshop folder)
    'custom_slides': [
        'demo-features.md',      # Demonstrates markdown features
        'demo-tips.md',          # Tips and best practices
    ],

    # Agenda image filename (must be in this folder)
    'agenda_image': 'agenda.png',
}
