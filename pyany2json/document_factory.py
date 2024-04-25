from __future__ import annotations
from .model import *

from com.github.romualdrousseau.any2json import DocumentFactory as DocumentFactory_  # type: ignore
from com.github.romualdrousseau.any2json import Document as Document_  # type: ignore

INTELLI_LAYOUT = Document_.Hint.INTELLI_LAYOUT
INTELLI_TAG = Document_.Hint.INTELLI_TAG


class HeaderTag:
    def getValue(self) -> str:
        """Get tag value"""

    def isUndefined(self) -> bool:
        """Return True if the tag is none or null otherwise False"""


class Header:
    def getName(self) -> str:
        """Get header name"""

    def getTag(self) -> HeaderTag:
        """Get header tag"""


class Cell:
    def getValue(self) -> str:
        """Toto"""


class Row:
    def cells(self) -> list[Cell]:
        """Toto"""


class Table:
    def headers(self) -> list[Header]:
        """Toto"""

    def rows(self) -> list[Row]:
        """Toto"""


class OptionalTable:

    def isPresent(self) -> bool:
        """Toto"""

    def get(self) -> Table:
        """Toto"""


class TableGraph:

    def getTable(self) -> Table:
        """Toto"""

    def isRoot(self) -> bool:
        """Toto"""

    def getParent(self) -> TableGraph:
        """Toto"""

    def children() -> list[TableGraph]:
        """Toto"""


class OptionalTableGraph:

    def isPresent(self) -> bool:
        """Toto"""

    def get(self) -> TableGraph:
        """Toto"""


class Sheet:
    def getTableGraph(self) -> OptionalTableGraph:
        """Toto"""

    def getTable(self) -> OptionalTable:
        """Toto"""


class Document:
    def setModel(model: Model) -> Document:
        """Toto"""

    def setHints(hints: list[Document_.Hint]) -> Document:
        """Toto"""

    def setRecipe(recipe: str) -> Document:
        """Toto"""

    def getTagClassifier() -> TagClassifier:
        """Toto"""

    def sheets(self) -> list[Sheet]:
        """Toto"""

    def __enter__(self) -> Document:
        """Toto"""

    def __exit__(self, exception_type, exception_value, traceback):
        """Toto"""


class DocumentFactory:
    @staticmethod
    def createInstance(file: str, encoding: str, password: str = None) -> Document:
        """createInstance"""


DocumentFactory = DocumentFactory_
