# ruff: noqa: F401, E402

"""PyArchery: Python binding to the Archery document parsing library.

This module provides a Pythonic interface to the Java-based Archery library,
allowing for efficient document parsing and data extraction.
"""

import jpype
import jpype.imports

from . import setup_java
from .archery import (
    CAMEL,
    INTELLI_EXTRACT,
    INTELLI_LAYOUT,
    INTELLI_TAG,
    INTELLI_TIME,
    SNAKE,
    DataTable,
    DocumentFactory,
    LayexTableParser,
    Model,
    ModelBuilder,
    TableGraph,
)
from .wrappers import DocumentWrapper


def model_from_path(path: str) -> ModelBuilder:
    """Create a ModelBuilder from a file path.

    Args:
        path (str): The path to the model configuration file.

    Returns:
        ModelBuilder: A ModelBuilder instance initialized from the file.

    """
    return ModelBuilder().fromPath(path)


def model_from_url(url: str) -> ModelBuilder:
    """Create a ModelBuilder from a URL.

    Args:
        url (str): The URL of the model configuration.

    Returns:
        ModelBuilder: A ModelBuilder instance initialized from the URL.

    """
    return ModelBuilder().fromURL(url)


def model_from_json(data: str) -> ModelBuilder:
    """Create a ModelBuilder from a JSON string.

    Args:
        data (str): The JSON string containing the model configuration.

    Returns:
        ModelBuilder: A ModelBuilder instance initialized from the JSON data.

    """
    return ModelBuilder().fromJSON(data)


def load(
    file_path: str,
    encoding: str = "UTF-8",
    model: Model | None = None,
    hints: list | None = None,
    recipe: list[str] | None = None,
    tag_case: str | None = None,
) -> DocumentWrapper:
    """Load a document and create a DocumentWrapper.

    Args:
        file_path (str): The path to the document file.
        encoding (str, optional): The encoding of the file. Defaults to "UTF-8".
        model (Model | None, optional): The model to use for parsing. Defaults to None.
        hints (list | None, optional): A list of hints for processing. Defaults to None.
        recipe (list[str] | None, optional): A list of recipe strings. Defaults to None.
        tag_case (str | None, optional): The tag case style ("SNAKE" or "CAMEL"). Defaults to None.

    Returns:
        DocumentWrapper: A wrapper around the loaded document.

    """
    doc = DocumentFactory.createInstance(file_path, encoding)
    if model:
        doc.setModel(model)
    if hints:
        doc.setHints(hints)
    if recipe:
        doc.setRecipe("\n".join(recipe))
    if tag_case:
        if tag_case == "SNAKE":
            doc.getTagClassifier().setTagStyle(SNAKE)
        elif tag_case == "CAMEL":
            doc.getTagClassifier().setTagStyle(CAMEL)
    return DocumentWrapper(doc)
