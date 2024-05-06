import pyany2json

FILE_PATHS = [
    "data/document with simple table.csv",
    "data/document with simple table.xls",
    "data/document with simple table.xlsx",
]

for file_path in FILE_PATHS:
    with pyany2json.load(file_path) as doc:
        for sheet in doc.sheets():
            table = sheet.getTable()
            if table.isPresent():
                table = table.get()
                for header in table.headers():
                    print(header.getTag().getValue(), end=" ")
                print()
                for row in table.rows():
                    for cell in row.cells():
                        print(cell.getValue(), end=" ")
                    print()
