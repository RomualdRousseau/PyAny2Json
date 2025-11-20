# ruff: noqa: N802, N803

from __future__ import annotations

from typing import Any, Optional

from com.github.romualdrousseau.archery import (
    Document as Document_,
)
from com.github.romualdrousseau.archery import (
    DocumentFactory as DocumentFactory_,
)
from com.github.romualdrousseau.archery import (
    TagClassifier as TagClassifier_,
)
from com.github.romualdrousseau.archery.base import (
    DataTable as DataTable_,
)
from com.github.romualdrousseau.archery.modeldata import (
    JsonModelBuilder as ModelBuilder_,
)
from com.github.romualdrousseau.archery.parser import (
    LayexTableParser as LayexTableParser_,
)


class HeaderTag:
    def getValue(self) -> str:
        """Get tag value.

        Returns:
            str: The value of the tag.

        """
        ...

    def isUndefined(self) -> bool:
        """Return True if the tag is none or null otherwise False.

        Returns:
            bool: True if the tag is undefined, False otherwise.

        """
        ...


class Header:
    def getName(self) -> str:
        """Get header name.

        Returns:
            str: The name of the header.

        """
        ...

    def getTag(self) -> HeaderTag:
        """Get header tag.

        Returns:
            HeaderTag: The tag associated with this header.

        """
        ...


class Cell:
    def getValue(self) -> str:
        """Get the value of the cell as a string.

        Returns:
            str: The value of the cell.

        """
        ...


class Row:
    def cells(self) -> list[Cell]:
        """Get the list of cells in this row.

        Returns:
            list[Cell]: A list of cells in the row.

        """
        ...


class Table:
    def headers(self) -> list[Header]:
        """Get the list of headers in this table.

        Returns:
            list[Header]: A list of headers in the table.

        """
        ...

    def rows(self) -> list[Row]:
        """Get the list of rows in this table.

        Returns:
            list[Row]: A list of rows in the table.

        """
        ...

    def getSheet(self) -> Sheet:
        """Get the sheet this table belongs to.

        Returns:
            Sheet: The sheet containing this table.

        """
        ...

    def getNumberOfColumns(self) -> int:
        """Get the number of columns in this table.

        Returns:
            int: The number of columns.

        """
        ...

    def getNumberOfRows(self) -> int:
        """Get the number of rows in this table.

        Returns:
            int: The number of rows.

        """
        ...

    def getRowAt(self, rowIndex: int) -> Row:
        """Get the row at the specified index.

        Args:
            rowIndex: The index of the row to retrieve.

        Returns:
            Row: The row at the specified index.

        """
        ...

    def getNumberOfHeaders(self) -> int:
        """Get the number of headers in this table.

        Returns:
            int: The number of headers.

        """
        ...

    def getHeaderNames(self) -> list[str]:
        """Get the list of header names.

        Returns:
            list[str]: A list of header names.

        """
        ...

    def getHeaderAt(self, i: int) -> Header:
        """Get the header at the specified index.

        Args:
            i: The index of the header to retrieve.

        Returns:
            Header: The header at the specified index.

        """
        ...

    def getNumberOfHeaderTags(self) -> int:
        """Get the number of header tags.

        Returns:
            int: The number of header tags.

        """
        ...

    def headerTags(self) -> list[Header]:
        """Get the list of header tags.

        Returns:
            list[Header]: A list of header tags.

        """
        ...


class OptionalTable:
    def isPresent(self) -> bool:
        """Return True if the table is present, False otherwise.

        Returns:
            bool: True if the table is present, False otherwise.

        """
        ...

    def get(self) -> Table:
        """Get the table if present.

        Returns:
            Table: The table instance.

        """
        ...


class DataTable(Table): ...


class TableGraph:
    def getTable(self) -> Table:
        """Get the table associated with this graph node.

        Returns:
            Table: The table associated with this node.

        """
        ...

    def isRoot(self) -> bool:
        """Return True if this is the root of the graph.

        Returns:
            bool: True if this is the root node, False otherwise.

        """
        ...

    def getParent(self) -> TableGraph:
        """Get the parent graph node.

        Returns:
            TableGraph: The parent graph node.

        """
        ...

    def children(self) -> list[TableGraph]:
        """Get the list of child graph nodes.

        Returns:
            list[TableGraph]: A list of child graph nodes.

        """
        ...


class OptionalTableGraph:
    def isPresent(self) -> bool:
        """Return True if the table graph is present, False otherwise.

        Returns:
            bool: True if the table graph is present, False otherwise.

        """
        ...

    def get(self) -> TableGraph:
        """Get the table graph if present.

        Returns:
            TableGraph: The table graph instance.

        """
        ...


class Sheet:
    def getTableGraph(self) -> OptionalTableGraph:
        """Get the table graph for this sheet.

        Returns:
            OptionalTableGraph: An optional containing the table graph if present.

        """
        ...

    def getTable(self) -> OptionalTable:
        """Get the table for this sheet.

        Returns:
            OptionalTable: An optional containing the table if present.

        """
        ...


class Document:
    def setModel(self, model: Model) -> Document:
        """Set the model for the document.

        Args:
            model: The model to set.

        Returns:
            Document: This document instance.

        """
        ...

    def setHints(self, hints: list[Document_.Hint]) -> Document:
        """Set processing hints for the document.

        Args:
            hints: A list of hints to set.

        Returns:
            Document: This document instance.

        """
        ...

    def setRecipe(self, recipe: str) -> Document:
        """Set the extraction recipe for the document.

        Args:
            recipe: The recipe string.

        Returns:
            Document: This document instance.

        """
        ...

    def getTagClassifier(self) -> TagClassifier:
        """Get the tag classifier for the document.

        Returns:
            TagClassifier: The tag classifier.

        """
        ...

    def sheets(self) -> list[Sheet]:
        """Get the list of sheets in the document.

        Returns:
            list[Sheet]: A list of sheets.

        """
        ...

    def __enter__(self) -> Document:
        """Enter the context manager.

        Returns:
            Document: This document instance.

        """
        ...

    def __exit__(
        self, exception_type: Optional[type], exception_value: Optional[BaseException], traceback: Optional[Any]
    ):
        """Exit the context manager.

        Args:
            exception_type: The type of the exception.
            exception_value: The value of the exception.
            traceback: The traceback of the exception.

        """
        ...


class DocumentFactory:
    @staticmethod
    def createInstance(file: str, encoding: str, password: Optional[str] = None) -> Document:
        """Create a new Document instance from a file.

        Args:
            file: The path to the file.
            encoding: The encoding of the file.
            password: The password for the file, if encrypted.

        Returns:
            Document: A new Document instance.

        """
        ...


class TableParser:
    """Base class for table parsers."""


class LayexTableParser(TableParser):
    def __init__(self, meta_layexes: list[str], data_layexes: list[str]):
        """Initialize the LayexTableParser with layex expressions.

        Args:
            meta_layexes: A list of meta layex expressions.
            data_layexes: A list of data layex expressions.

        """


class TagClassifier:
    """Class for classifying tags in the document."""

    def setTagStyle(self, mode: TagClassifier_.TagStyle) -> TagClassifier:
        """Set the tag style for classification.

        Args:
            mode: The tag style mode.

        Returns:
            TagClassifier: This tag classifier instance.

        """
        ...

    def setCamelMode(self, mode: TagClassifier_.TagStyle) -> TagClassifier:
        """Set the camel case mode for classification.

        Args:
            mode: The camel case mode.

        Returns:
            TagClassifier: This tag classifier instance.

        """
        ...


class Model:
    """Class representing the data model."""


class ModelBuilder:
    def __init__(self):
        """Initialize a new ModelBuilder."""

    def fromPath(self, path: str) -> ModelBuilder:
        """Load the model configuration from a file path.

        Args:
            path: The path to the model configuration file.

        Returns:
            ModelBuilder: This model builder instance.

        """
        ...

    def fromURI(self, uri: str) -> ModelBuilder:
        """Load the model configuration from a URI.

        Args:
            uri: The URI of the model configuration.

        Returns:
            ModelBuilder: This model builder instance.

        """
        ...

    def fromJSON(self, data: str) -> ModelBuilder:
        """Load the model configuration from a JSON string.

        Args:
            data: The JSON string containing the model configuration.

        Returns:
            ModelBuilder: This model builder instance.

        """
        ...

    def getEntityList(self) -> list:
        """Get the list of entities in the model.

        Returns:
            list: A list of entities.

        """
        ...

    def setEntityList(self, entitites: list) -> ModelBuilder:
        """Set the list of entities in the model.

        Args:
            entitites: A list of entities to set.

        Returns:
            ModelBuilder: This model builder instance.

        """
        ...

    def getPatternMap(self) -> dict:
        """Get the pattern map for the model.

        Returns:
            dict: The pattern map.

        """
        ...

    def setPatternMap(self, patterns: dict) -> ModelBuilder:
        """Set the pattern map for the model.

        Args:
            patterns: The pattern map to set.

        Returns:
            ModelBuilder: This model builder instance.

        """
        ...

    def setTableParser(self, parser: TableParser) -> ModelBuilder:
        """Set the table parser for the model.

        Args:
            parser: The table parser to set.

        Returns:
            ModelBuilder: This model builder instance.

        """
        ...

    def setTagClassifier(self, tagger: TagClassifier) -> ModelBuilder:
        """Set the tag classifier for the model.

        Args:
            tagger: The tag classifier to set.

        Returns:
            ModelBuilder: This model builder instance.

        """
        ...

    def build(self) -> Model:
        """Build and return the Model instance.

        Returns:
            Model: The built Model instance.

        """
        ...


ModelBuilder = ModelBuilder_  # noqa: F811
DocumentFactory = DocumentFactory_  # noqa: F811
DataTable = DataTable_  # noqa: F811
LayexTableParser = LayexTableParser_  # noqa: F811
