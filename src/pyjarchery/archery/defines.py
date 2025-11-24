"""Constants and enumerations for the PyArchery library.

This module defines constants used for document processing hints and tag classification styles,
mapping them directly from the underlying Java Archery Framework.
"""

from com.github.romualdrousseau.archery import (
    Document as Document_,
)
from com.github.romualdrousseau.archery import (
    TagClassifier as TagClassifier_,
)

INTELLI_EXTRACT = Document_.Hint.INTELLI_EXTRACT
"""Hint to enable intelligent extraction."""

INTELLI_LAYOUT = Document_.Hint.INTELLI_LAYOUT
"""Hint to enable intelligent layout analysis."""

INTELLI_TAG = Document_.Hint.INTELLI_TAG
"""Hint to enable intelligent tagging."""

INTELLI_TIME = Document_.Hint.INTELLI_TIME
"""Hint to enable time-based intelligence."""

NONE = TagClassifier_.TagStyle.NONE
"""No specific tag style."""

SNAKE = TagClassifier_.TagStyle.SNAKE
"""Snake case tag style."""

CAMEL = TagClassifier_.TagStyle.CAMEL
"""Camel case tag style."""
