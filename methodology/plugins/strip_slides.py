"""
MkDocs plugin to strip slide content from methodology docs.

Content between <!-- SLIDE:xxx --> and <!-- /SLIDE --> markers
is extracted for slides but hidden from the mkdocs documentation.
"""

import re
from mkdocs.plugins import BasePlugin


class StripSlidesPlugin(BasePlugin):
    """Strip slide-only content from markdown files."""

    # Pattern to match <!-- SLIDE:xxx --> ... <!-- /SLIDE --> blocks
    SLIDE_PATTERN = re.compile(
        r'<!--\s*SLIDE:\w+\s*-->.*?<!--\s*/SLIDE\s*-->',
        re.DOTALL
    )

    def on_page_markdown(self, markdown, page, config, files):
        """Remove slide blocks from markdown before rendering."""
        # Remove all slide blocks
        cleaned = self.SLIDE_PATTERN.sub('', markdown)

        # Clean up excessive blank lines left behind
        cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)

        return cleaned
