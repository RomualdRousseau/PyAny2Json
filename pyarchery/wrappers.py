import tempfile
from typing import Any, Iterator, List, Optional

import pandas as pd
import pyarrow
import pyarrow as pa

from pyarchery.archery import (
    Cell as JCell,
)
from pyarchery.archery import (
    Document as JDocument,
)
from pyarchery.archery import (
    Header as JHeader,
)
from pyarchery.archery import (
    OptionalTable as JOptionalTable,
)
from pyarchery.archery import (
    Row as JRow,
)
from pyarchery.archery import (
    Sheet as JSheet,
)
from pyarchery.archery import (
    Table as JTable,
)


class CellWrapper:
    def __init__(self, cell: JCell):
        self._cell = cell

    @property
    def value(self) -> str:
        return self._cell.getValue()

    def __repr__(self):
        return f"Cell(value={self.value})"


class RowWrapper:
    def __init__(self, row: JRow):
        self._row = row

    @property
    def cells(self) -> List[CellWrapper]:
        return [CellWrapper(cell) for cell in self._row.cells()]

    def __iter__(self) -> Iterator[CellWrapper]:
        return iter(self.cells)


class HeaderWrapper:
    def __init__(self, header: JHeader):
        self._header = header

    @property
    def name(self) -> str:
        return self._header.getName()

    @property
    def tag_value(self) -> Optional[str]:
        tag = self._header.getTag()
        if tag and not tag.isUndefined():
            return tag.getValue()
        return None


class TableWrapper:
    def __init__(self, table: JTable):
        self._table = table

    @property
    def headers(self) -> List[HeaderWrapper]:
        return [HeaderWrapper(h) for h in self._table.headers()]

    @property
    def rows(self) -> Iterator[RowWrapper]:
        for row in self._table.rows():
            yield RowWrapper(row)

    @property
    def header_names(self) -> List[str]:
        return [h.name for h in self.headers]

    def to_pydict(self) -> dict[str, List[Any]]:
        """Convert the table to a python dictionary of lists (column-oriented)."""
        data = {name: [] for name in self.header_names}
        headers = self.headers

        for row in self.rows:
            cells = row.cells
            # Handle potential mismatch in cell count vs header count
            # We assume cells align with headers by index
            for i, header in enumerate(headers):
                if i < len(cells):
                    data[header.name].append(cells[i].value)
                else:
                    data[header.name].append(None)
        return data

    def to_arrow(self) -> pa.Table:
        """Convert the table to a PyArrow Table."""
        with tempfile.NamedTemporaryFile() as temp:
            file_path = temp.name
            self._table.to_arrow(file_path)
            with pyarrow.ipc.open_stream(file_path) as reader:
                return reader.read_all()

    def to_pandas(self) -> pd.DataFrame:
        """Convert the table to a Pandas DataFrame."""
        return self.to_arrow().to_pandas()

    def to_csv(self, path: str):
        """Write the table to a CSV file."""
        self._table.to_csv(path)


class SheetWrapper:
    def __init__(self, sheet: JSheet):
        self._sheet = sheet

    @property
    def table(self) -> Optional[TableWrapper]:
        opt_table: JOptionalTable = self._sheet.getTable()
        if opt_table.isPresent():
            return TableWrapper(opt_table.get())
        return None

    def add_sheet_listener(self, listener):
        self._sheet.addSheetListener(listener)


class DocumentWrapper:
    def __init__(self, document: JDocument):
        self._document = document

    @property
    def sheets(self) -> Iterator[SheetWrapper]:
        for sheet in self._document.sheets():
            yield SheetWrapper(sheet)

    def __enter__(self):
        self._document.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._document.__exit__(exc_type, exc_val, exc_tb)
