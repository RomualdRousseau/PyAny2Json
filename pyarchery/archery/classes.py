# ruff: noqa: N802, N803

from __future__ import annotations

from typing import Optional

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
        """Get tag value."""
        ...

    def isUndefined(self) -> bool:
        """Return True if the tag is none or null otherwise False."""
        ...


class Header:
    def getName(self) -> str:
        """Get header name."""
        ...

    def getTag(self) -> HeaderTag:
        """Get header tag."""
        ...


class Cell:
    def getValue(self) -> str:
        """Toto."""
        ...


class Row:
    def cells(self) -> list[Cell]:
        """Toto."""
        ...


class Table:
    def headers(self) -> list[Header]:
        """Toto."""
        ...

    def rows(self) -> list[Row]:
        """Toto."""
        ...

    def getSheet(self) -> Sheet:
        """Toto."""
        ...

    def getNumberOfColumns(self) -> int:
        """Toto."""
        ...

    def getNumberOfRows(self) -> int:
        """Toto."""
        ...

    def getRowAt(self, rowIndex) -> Row:
        """Toto."""
        ...

    def getNumberOfHeaders(self) -> int:
        """Toto."""
        ...

    def getHeaderNames(self) -> list[str]:
        """Toto."""
        ...

    def getHeaderAt(self, i) -> Header:
        """Toto."""
        ...

    def getNumberOfHeaderTags(self) -> int:
        """Toto."""
        ...

    def headerTags(self) -> list[Header]:
        """Toto."""
        ...


class OptionalTable:
    def isPresent(self) -> bool:
        """Toto."""
        ...

    def get(self) -> Table:
        """Toto."""
        ...


class DataTable(Table): ...


class TableGraph:
    def getTable(self) -> Table:
        """Toto."""
        ...

    def isRoot(self) -> bool:
        """Toto."""
        ...

    def getParent(self) -> TableGraph:
        """Toto."""
        ...

    def children(self) -> list[TableGraph]:
        """Toto."""
        ...


class OptionalTableGraph:
    def isPresent(self) -> bool:
        """Toto."""
        ...

    def get(self) -> TableGraph:
        """Toto."""
        ...


class Sheet:
    def getTableGraph(self) -> OptionalTableGraph:
        """Toto."""
        ...

    def getTable(self) -> OptionalTable:
        """Toto."""
        ...


class Document:
    def setModel(self, model: Model) -> Document:
        """Toto."""
        ...

    def setHints(self, hints: list[Document_.Hint]) -> Document:
        """Toto."""
        ...

    def setRecipe(self, recipe: str) -> Document:
        """Toto."""
        ...

    def getTagClassifier(self) -> TagClassifier:
        """Toto."""
        ...

    def sheets(self) -> list[Sheet]:
        """Toto."""
        ...

    def __enter__(self) -> Document:
        """Toto."""
        ...

    def __exit__(self, exception_type, exception_value, traceback):
        """Toto."""
        ...


class DocumentFactory:
    @staticmethod
    def createInstance(file: str, encoding: str, password: Optional[str] = None) -> Document:
        """CreateInstance."""
        ...


class TableParser:
    """createInstance."""


class LayexTableParser(TableParser):
    def __init__(self, meta_layexes: list[str], data_layexes: list[str]):
        """CreateInstance."""


class TagClassifier:
    """createInstance."""

    def setTagStyle(self, mode: TagClassifier_.TagStyle) -> TagClassifier:
        """Toto."""
        ...

    def setCamelMode(self, mode: TagClassifier_.TagStyle) -> TagClassifier:
        """Toto."""
        ...


class Model:
    """createInstance."""


class ModelBuilder:
    def __init__(self):
        """CreateInstance."""

    def fromPath(self, path: str) -> ModelBuilder:
        """Toto."""
        ...

    def fromURI(self, uri: str) -> ModelBuilder:
        """Toto."""
        ...

    def fromJSON(self, data: str) -> ModelBuilder:
        """Toto."""
        ...

    def getEntityList(self) -> list:
        """Toto."""
        ...

    def setEntityList(self, entitites: list) -> ModelBuilder:
        """Toto."""
        ...

    def getPatternMap(self) -> dict:
        """Toto."""
        ...

    def setPatternMap(self, patterns: dict) -> ModelBuilder:
        """Toto."""
        ...

    def setTableParser(self, parser: TableParser) -> ModelBuilder:
        """Toto."""
        ...

    def setTagClassifier(self, tagger: TagClassifier) -> ModelBuilder:
        """Toto."""
        ...

    def build(self) -> Model:
        """Toto."""
        ...


ModelBuilder = ModelBuilder_  # noqa: F811
DocumentFactory = DocumentFactory_  # noqa: F811
DataTable = DataTable_  # noqa: F811
LayexTableParser = LayexTableParser_  # noqa: F811
