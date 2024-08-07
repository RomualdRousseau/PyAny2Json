from __future__ import annotations
from typing import Optional
from .model import TagClassifier, Model

from com.github.romualdrousseau.any2json import DocumentFactory as DocumentFactory_  # type: ignore
from com.github.romualdrousseau.any2json import Document as Document_  # type: ignore
from com.github.romualdrousseau.any2json.base import DataTable as DataTable_  # type: ignore

INTELLI_EXTRACT = Document_.Hint.INTELLI_EXTRACT
INTELLI_LAYOUT = Document_.Hint.INTELLI_LAYOUT
INTELLI_TAG = Document_.Hint.INTELLI_TAG


class HeaderTag:
    def getValue(self) -> str:
        """Get tag value"""
        ...

    def isUndefined(self) -> bool:
        """Return True if the tag is none or null otherwise False"""
        ...


class Header:
    def getName(self) -> str:
        """Get header name"""
        ...

    def getTag(self) -> HeaderTag:
        """Get header tag"""
        ...


class Cell:
    def getValue(self) -> str:
        """Toto"""
        ...


class Row:
    def cells(self) -> list[Cell]:
        """Toto"""
        ...


class Table:
    def headers(self) -> list[Header]:
        """Toto"""
        ...

    def rows(self) -> list[Row]:
        """Toto"""
        ...

    def getSheet(self) -> Sheet:
        """Toto"""
        ...

    def getNumberOfColumns(self) -> int:
        """Toto"""
        ...

    def getNumberOfRows(self) -> int:
        """Toto"""
        ...

    def getRowAt(self, rowIndex) -> Row:
        """Toto"""
        ...

    def getNumberOfHeaders(self) -> int:
        """Toto"""
        ...

    def getHeaderNames(self) -> list[str]:
        """Toto"""
        ...

    def getHeaderAt(self, i) -> Header:
        """Toto"""
        ...

    def getNumberOfHeaderTags(self) -> int:
        """Toto"""
        ...

    def headerTags(self) -> list[Header]:
        """Toto"""
        ...


class OptionalTable:

    def isPresent(self) -> bool:
        """Toto"""
        ...

    def get(self) -> Table:
        """Toto"""
        ...


class DataTable(Table):
        ...

class TableGraph:

    def getTable(self) -> Table:
        """Toto"""
        ...

    def isRoot(self) -> bool:
        """Toto"""
        ...

    def getParent(self) -> TableGraph:
        """Toto"""
        ...

    def children(self) -> list[TableGraph]:
        """Toto"""
        ...


class OptionalTableGraph:

    def isPresent(self) -> bool:
        """Toto"""
        ...

    def get(self) -> TableGraph:
        """Toto"""
        ...


class Sheet:
    def getTableGraph(self) -> OptionalTableGraph:
        """Toto"""
        ...

    def getTable(self) -> OptionalTable:
        """Toto"""
        ...


class Document:
    def setModel(self, model: Model) -> Document:
        """Toto"""
        ...

    def setHints(self, hints: list[Document_.Hint]) -> Document:
        """Toto"""
        ...

    def setRecipe(self, recipe: str) -> Document:
        """Toto"""
        ...

    def getTagClassifier(self) -> TagClassifier:
        """Toto"""
        ...

    def sheets(self) -> list[Sheet]:
        """Toto"""
        ...

    def __enter__(self) -> Document:
        """Toto"""
        ...

    def __exit__(self, exception_type, exception_value, traceback):
        """Toto"""
        ...


class DocumentFactory:
    @staticmethod
    def createInstance(
        file: str, encoding: str, password: Optional[str] = None
    ) -> Document:
        """createInstance"""
        ...


DocumentFactory = DocumentFactory_  # noqa: F811
DataTable = DataTable_  # noqa: F811