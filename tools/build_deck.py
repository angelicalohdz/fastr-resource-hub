#!/usr/bin/env python3
"""
FASTR Slide Deck Builder

Build workshop-specific slide decks from core content + templates + custom content.

Usage:
    python3 tools/build_deck.py --workshop 2025_01_nigeria
    python3 tools/build_deck.py --workshop example --output test.md
"""

import argparse
import os
import sys
import re
import importlib.util

# Define core content sections
CORE_SECTIONS = {
    1: "01_background_rationale.md",
    2: "02_fastr_approach.md",
    3: "03_data_extraction.md",
    4: "04_data_quality_assessment.md",
    5: "05_service_utilization.md",
    6: "06_coverage_analysis.md",
    7: "07_facility_assessments.md",
}

SECTION_DESCRIPTIONS = {
    1: "Background & Rationale",
    2: "FASTR Approach",
    3: "Data Extraction",
    4: "Data Quality Assessment",
    5: "Service Utilization",
    6: "Coverage Analysis",
    7: "Facility Assessments",
}

def load_workshop_config(workshop_id, base_dir):
    """Load workshop configuration from workshops/{id}/config.py"""
    config_path = os.path.join(base_dir, "workshops", workshop_id, "config.py")

    if not os.path.exists(config_path):
        print(f"❌ Error: Workshop config not found: {config_path}")
        print(f"   Create a workshop folder: workshops/{workshop_id}/")
        print(f"   Copy from: workshops/example/")
        sys.exit(1)

    # Load config as module
    spec = importlib.util.spec_from_file_location("workshop_config", config_path)
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)

    return config_module.WORKSHOP_CONFIG

def substitute_variables(content, config):
    """Replace {{VARIABLE}} placeholders with values from config."""
    replacements = {
        'WORKSHOP_ID': config.get('workshop_id', ''),
        'WORKSHOP_NAME': config.get('name', ''),
        'DATE': config.get('date', ''),
        'LOCATION': config.get('location', ''),
        'FACILITATORS': config.get('facilitators', ''),
        'CONTACT_EMAIL': config.get('contact_email', ''),
        'WEBSITE': config.get('website', ''),
        'TEA_RESUME_TIME': config.get('tea_resume_time', ''),
        'LUNCH_RESUME_TIME': config.get('lunch_resume_time', ''),
    }

    result = content
    for var, value in replacements.items():
        pattern = f'{{{{{var}}}}}'
        result = result.replace(pattern, value)

    return result

def read_markdown_file(filepath):
    """Read a markdown file and return its content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"⚠️  Warning: File not found: {filepath}")
        return ""

def strip_frontmatter(content):
    """Remove YAML frontmatter from markdown content."""
    lines = content.split('\n')
    if lines[0].strip() == '---':
        # Find the end of frontmatter
        end_idx = None
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                end_idx = i
                break
        if end_idx:
            return '\n'.join(lines[end_idx+1:])
    return content

def build_workshop_deck(workshop_id, base_dir, output_file=None):
    """Build a complete slide deck for a workshop."""

    print("=" * 70)
    print(f"🎯 FASTR Deck Builder - Building Workshop: {workshop_id}")
    print("=" * 70)

    # Load workshop config
    config = load_workshop_config(workshop_id, base_dir)

    # Set output file
    if not output_file:
        output_file = f"{workshop_id}_deck.md"

    print(f"\n📋 Workshop: {config.get('name', 'Unknown')}")
    print(f"   Date: {config.get('date', 'Not set')}")
    print(f"   Location: {config.get('location', 'Not set')}")

    # Start with Marp frontmatter
    deck_content = """---
marp: true
theme: fastr
paginate: true
---

"""

    # 1. Add title slide
    print(f"\n📄 Adding components:")
    template_path = os.path.join(base_dir, "templates", "title_slide.md")
    title_content = read_markdown_file(template_path)
    if title_content:
        title_content = strip_frontmatter(title_content)
        title_content = substitute_variables(title_content, config)
        deck_content += title_content + "\n"
        print(f"   ✓ Title slide")

    # 2. Add agenda if enabled
    if config.get('include_agenda', False):
        agenda_path = os.path.join(base_dir, "templates", "agenda.md")
        agenda_content = read_markdown_file(agenda_path)
        if agenda_content:
            agenda_content = strip_frontmatter(agenda_content)
            agenda_content = substitute_variables(agenda_content, config)
            deck_content += agenda_content + "\n"
            print(f"   ✓ Agenda slide")

    # 3. Add core sections
    sections = config.get('sections', [])
    if sections:
        print(f"\n📚 Core content ({len(sections)} sections):")
        core_content_dir = os.path.join(base_dir, "core_content")

        for num in sorted(sections):
            if num in CORE_SECTIONS:
                filepath = os.path.join(core_content_dir, CORE_SECTIONS[num])
                content = read_markdown_file(filepath)
                if content:
                    content = strip_frontmatter(content)
                    content = substitute_variables(content, config)
                    deck_content += "\n" + content + "\n"
                    print(f"   ✓ {num}. {SECTION_DESCRIPTIONS[num]}")
            else:
                print(f"   ⚠️  Section {num} not found")

    # 4. Add breaks if enabled
    if config.get('include_breaks', False):
        breaks_path = os.path.join(base_dir, "templates", "breaks.md")
        breaks_content = read_markdown_file(breaks_path)
        if breaks_content:
            breaks_content = strip_frontmatter(breaks_content)
            breaks_content = substitute_variables(breaks_content, config)
            deck_content += breaks_content + "\n"
            print(f"\n☕ Added break slides")

    # 5. Add custom slides
    custom_slides = config.get('custom_slides', [])
    if custom_slides:
        print(f"\n📁 Custom content:")
        workshop_dir = os.path.join(base_dir, "workshops", workshop_id)

        for custom_file in custom_slides:
            custom_path = os.path.join(workshop_dir, custom_file)
            content = read_markdown_file(custom_path)
            if content:
                content = strip_frontmatter(content)
                content = substitute_variables(content, config)
                deck_content += "\n" + content + "\n"
                print(f"   ✓ {custom_file}")

    # 6. Add closing slide
    if config.get('include_closing', True):
        closing_path = os.path.join(base_dir, "templates", "closing.md")
        closing_content = read_markdown_file(closing_path)
        if closing_content:
            closing_content = strip_frontmatter(closing_content)
            closing_content = substitute_variables(closing_content, config)
            deck_content += closing_content + "\n"
            print(f"\n👋 Added closing slides")

    # Write output file
    output_dir = os.path.join(base_dir, "outputs")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_file)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(deck_content)

    print(f"\n{'=' * 70}")
    print(f"✅ Deck built successfully!")
    print(f"   📄 Output: {output_path}")
    print(f"\n💡 Next steps:")
    print(f"   Render to PDF:  marp {output_path} --theme-set fastr-theme.css --pdf")
    print(f"   Convert to PPT: python3 tools/convert_to_pptx.py {output_path}")
    print(f"   Preview:        marp --preview {output_path} --theme-set fastr-theme.css")
    print(f"{'=' * 70}\n")

    return output_path

def main():
    # Determine base directory (parent of tools/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)  # Go up one level from tools/

    parser = argparse.ArgumentParser(
        description="Build FASTR workshop slide deck from config",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Build workshop deck:
    python3 tools/build_deck.py --workshop example
    python3 tools/build_deck.py --workshop 2025_01_nigeria

  Custom output filename:
    python3 tools/build_deck.py --workshop example --output test.md

Workshop Structure:
  workshops/{id}/
    ├── config.py          # Workshop configuration
    ├── agenda.png         # Agenda image
    └── custom_slides.md   # Custom content (optional)

See workshops/example/ for a template.
        """
    )

    parser.add_argument(
        '--workshop',
        type=str,
        required=True,
        help='Workshop ID (folder name in workshops/)'
    )

    parser.add_argument(
        '--output',
        type=str,
        help='Output filename (default: {workshop_id}_deck.md)'
    )

    args = parser.parse_args()

    # Build the deck
    build_workshop_deck(args.workshop, base_dir, args.output)

if __name__ == "__main__":
    main()
