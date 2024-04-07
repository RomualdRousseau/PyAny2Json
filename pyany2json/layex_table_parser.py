from .model import *

from com.github.romualdrousseau.any2json.parser import LayexTableParser as LayexTableParser_  # type: ignore


class LayexTableParser(TableParser):
    def __init__(self, meta_layexes: list[str], data_layexes: list[str]):
        """createInstance"""


LayexTableParser = LayexTableParser_
