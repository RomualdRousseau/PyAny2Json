import os

import pandas as pd
import pyarrow as pa
import pytest

import pyarchery

DATA_DIR = os.path.join(os.path.dirname(__file__), "../examples/data")


@pytest.mark.parametrize(
    "filename",
    [
        "document with simple table.csv",
        "document with simple table.xlsx",
        "document with simple table.xls",
    ],
)
def test_conversion_simple_table(filename):
    file_path = os.path.join(DATA_DIR, filename)

    with pyarchery.load(file_path) as doc:
        sheets = list(doc.sheets)
        assert len(sheets) > 0

        # Assuming the first sheet contains the table we want to test
        sheet = sheets[0]
        table = sheet.table
        assert table is not None

        # Test to_pydict
        data_dict = table.to_pydict()
        assert isinstance(data_dict, dict)
        assert len(data_dict) > 0
        # Check if keys match headers
        assert set(data_dict.keys()) == set(table.header_names)

        # Test to_arrow
        arrow_table = table.to_arrow()
        assert isinstance(arrow_table, pa.Table)
        assert arrow_table.num_rows > 0

        # Test to_pandas
        df = table.to_arrow().to_pandas()
        assert isinstance(df, pd.DataFrame)
        assert not df.empty
        assert len(df) == arrow_table.num_rows

        # Test to_csv
        output_csv = f"test_output_{filename}.csv"
        try:
            table.to_csv(output_csv)
            assert os.path.exists(output_csv)
            # Basic check if file is not empty
            assert os.path.getsize(output_csv) > 0
        finally:
            if os.path.exists(output_csv):
                os.remove(output_csv)
