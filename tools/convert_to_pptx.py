#!/usr/bin/env python3
"""
Convert Markdown to Editable PowerPoint

Converts markdown files to PowerPoint presentations using pandoc.
Uses fastr-reference.pptx template for FASTR branding if available.

Usage:
    python3 tools/convert_to_pptx.py outputs/example_deck.md
    python3 tools/convert_to_pptx.py outputs/my_deck.md --reference custom_template.pptx
"""

import argparse
import os
import subprocess
import shutil
import sys

def strip_marp_frontmatter(content):
    """Remove Marp YAML frontmatter that confuses pandoc."""
    lines = content.split('\n')
    if lines[0].strip() == '---':
        # Find closing ---
        for i in range(1, min(len(lines), 20)):  # Check first 20 lines
            if lines[i].strip() == '---':
                # Remove frontmatter, keep rest
                return '\n'.join(lines[i+1:])
    return content

def convert_slide_breaks(content):
    """Convert Marp slide breaks (---) to pandoc slide breaks."""
    lines = content.split('\n')
    result = []

    for i, line in enumerate(lines):
        # If line is just --- (slide separator)
        if line.strip() == '---':
            # Add proper pandoc slide break (horizontal rule with blank lines)
            result.append('')
            result.append('---')
            result.append('')
        else:
            result.append(line)

    return '\n'.join(result)

def fix_image_paths(content, base_dir):
    """Convert relative image paths to absolute paths for pandoc."""
    import re
    # Find markdown image syntax: ![alt](path)
    def replace_path(match):
        alt_text = match.group(1)
        img_path = match.group(2)
        # If path is relative
        if img_path.startswith('../') or img_path.startswith('./') or not img_path.startswith('/'):
            # Try to find the file
            # First try relative to base_dir
            test_path = os.path.join(base_dir, img_path)
            if os.path.exists(test_path):
                abs_path = os.path.abspath(test_path)
                return f'![{alt_text}]({abs_path})'
            # If ../assets/, try just assets/
            if img_path.startswith('../assets/'):
                alt_path = img_path.replace('../assets/', 'assets/')
                test_path = os.path.join(base_dir, alt_path)
                if os.path.exists(test_path):
                    abs_path = os.path.abspath(test_path)
                    return f'![{alt_text}]({abs_path})'
        return match.group(0)

    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_path, content)

def convert_to_pptx(md_file, reference_template=None):
    """Convert markdown file to PowerPoint using pandoc."""

    # Check if pandoc is installed
    if not shutil.which('pandoc'):
        print("\n⚠️  Pandoc not found. Cannot convert to PowerPoint.")
        print("   Install: brew install pandoc (Mac) or see https://pandoc.org/installing.html")
        return False

    # Check if markdown file exists
    if not os.path.exists(md_file):
        print(f"\n❌ Error: File not found: {md_file}")
        return False

    # Read and strip Marp frontmatter
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get absolute directory for fixing paths
    md_abs = os.path.abspath(md_file)
    md_dir = os.path.dirname(md_abs)

    # Strip frontmatter, convert slide breaks, and fix image paths
    cleaned_content = strip_marp_frontmatter(content)
    cleaned_content = convert_slide_breaks(cleaned_content)
    cleaned_content = fix_image_paths(cleaned_content, md_dir)

    # Create temp file without frontmatter
    temp_file = md_file.replace('.md', '_temp.md')
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

    # Build output filename
    pptx_file = md_file.replace('.md', '.pptx')

    # Pandoc looks for images relative to the source file
    # Set resource path to the markdown file's directory
    resource_paths = md_dir

    # Build pandoc command (use temp file)
    # Note: We strip Marp frontmatter but pandoc may still see --- as YAML
    # Use --from markdown to avoid YAML parsing issues
    # Use --resource-path to find images (current dir and parent for ../assets/)
    cmd = [
        'pandoc', temp_file,
        '-f', 'markdown-yaml_metadata_block',
        '-t', 'pptx',
        '--resource-path', resource_paths,
        '-o', pptx_file
    ]

    # Determine which reference template to use
    if reference_template and os.path.exists(reference_template):
        cmd.extend(['--reference-doc', reference_template])
        print(f"\n📊 Converting to PowerPoint with custom template...")
    elif os.path.exists('fastr-reference.pptx'):
        cmd.extend(['--reference-doc', 'fastr-reference.pptx'])
        print(f"\n📊 Converting to PowerPoint with FASTR branding...")
    else:
        print(f"\n📊 Converting to PowerPoint (default styling)...")
        print(f"   💡 Tip: Create 'fastr-reference.pptx' for custom FASTR branding")

    # Run conversion
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"   ✅ Created: {pptx_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Conversion failed: {e}")
        if e.stderr:
            print(f"   Error details: {e.stderr.decode()}")
        return False
    finally:
        # Clean up temp file
        if os.path.exists(temp_file):
            os.remove(temp_file)

def main():
    parser = argparse.ArgumentParser(
        description="Convert markdown to editable PowerPoint using pandoc",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Convert a markdown file:
    python3 convert_to_pptx.py my_workshop_deck.md

  Use custom reference template:
    python3 convert_to_pptx.py my_workshop_deck.md --reference my_template.pptx

Notes:
  - Requires pandoc to be installed
  - Uses fastr-reference.pptx template if available
  - Outputs editable PowerPoint with text boxes (not images)
        """
    )

    parser.add_argument(
        'markdown_file',
        help='Markdown file to convert to PowerPoint'
    )

    parser.add_argument(
        '--reference',
        type=str,
        help='Custom PowerPoint reference template to use for styling'
    )

    args = parser.parse_args()

    # Convert the file
    success = convert_to_pptx(args.markdown_file, args.reference)

    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
