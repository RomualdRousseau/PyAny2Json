from __future__ import annotations

from com.github.romualdrousseau.any2json import ModelBuilder as ModelBuilder_  # type: ignore

class TagClassifier:
    """createInstance"""
    
    def setSnakeMode(snakeMode: bool):
        """Toto"""
        
    def setCamelMode(camelMode: bool):
        """Toto"""


class TableParser:
    """createInstance"""


class Model:
    """createInstance"""


class ModelBuilder:
    def __init__(self):
        """createInstance"""
        
    def fromURI(self, uri: str) -> ModelBuilder:
        """Toto"""
        
    def fromJSON(self, data: str) -> ModelBuilder:
        """Toto"""

    def getEntityList(self) -> list:
        """Toto"""
        
    def setEntityList(self, entitites: list) -> ModelBuilder:
        """Toto"""

    def getPatternMap(self) -> dict:
        """Toto"""
        
    def setPatternMap(self, patterns: dict) -> ModelBuilder:
        """Toto"""

    def setTableParser(self, parser: TableParser) -> ModelBuilder:
        """Toto"""

    def build(self) -> Model:
        """Toto"""


ModelBuilder = ModelBuilder_
