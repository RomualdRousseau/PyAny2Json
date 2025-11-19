import pyarchery

REPO_BASE_URL = "https://raw.githubusercontent.com/RomualdRousseau/Archery/main/archery-models"
MODEL_NAME = "sales-english"
FILE_PATH = "data/AG120-N-074.pdf"
FILE_ENCODING = "UTF-8"


def get_model():
    builder = pyarchery.model_from_url(f"{REPO_BASE_URL}/{MODEL_NAME}/{MODEL_NAME}.json")

    parser = pyarchery.LayexTableParser([""], ["((vv$)(v+$v+$))(()(.+$)())+()", "(()(.+$))(()(.+$)())+()"])

    return builder.setTableParser(parser).build()


def visit_table(parent: pyarchery.TableGraph):
    for c in parent.children():
        table = c.getTable()
        if isinstance(table, pyarchery.DataTable):
            for header in table.headers():
                print(header.getValue(), end=" ")
            print()
            for row in table.rows():
                for cell in row.cells():
                    print(cell.getValue(), end=" ")
                print()
        if len(c.children()) > 0:
            visit_table(c)


with pyarchery.load(
    FILE_PATH,
    encoding=FILE_ENCODING,
    model=get_model(),
    hints=[pyarchery.INTELLI_LAYOUT],
) as doc:
    for sheet in doc.sheets:
        root = sheet.get_table_graph()
        if root:
            visit_table(root)
