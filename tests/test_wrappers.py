import os

import pandas as pd
import pyarrow as pa

import pyarchery

DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
CSV_FILE = os.path.join(DATA_DIR, "document with simple table.csv")


def test_load_and_wrappers():
    with pyarchery.load(CSV_FILE) as doc:
        sheets = list(doc.sheets)
        assert len(sheets) > 0

        sheet = sheets[0]
        table = sheet.table
        assert table is not None

        # Test headers
        headers = table.headers
        assert len(headers) > 0
        print(f"Headers: {table.header_names}")

        # Test rows
        rows = list(table.rows)
        assert len(rows) > 0

        # Test to_arrow
        arrow_table = table.to_arrow()
        assert isinstance(arrow_table, pa.Table)
        assert arrow_table.num_rows == len(rows)
        assert arrow_table.num_columns == len(headers)
        print("Arrow Table Schema:", arrow_table.schema)

        # Test to_pandas
        df = table.to_pandas()
        assert isinstance(df, pd.DataFrame)
        assert len(df) == len(rows)

        # Test to_csv
        output_csv = "test_output.csv"
        table.to_csv(output_csv)
        assert os.path.exists(output_csv)

        # Verify CSV content
        with open(output_csv, "r") as f:
            lines = f.readlines()
            assert len(lines) == len(rows) + 1  # header + rows

        os.remove(output_csv)
