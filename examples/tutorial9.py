import pyany2json


REPO_BASE_URL = "https://raw.githubusercontent.com/RomualdRousseau/Any2Json-Models/main"
MODEL_NAME = "sales-english"
FILE_PATH = "data/AG120-N-074.pdf"
FILE_ENCODING = "UTF-8"


builder = pyany2json.model_from_uri(f"{REPO_BASE_URL}/{MODEL_NAME}/{MODEL_NAME}.json")

parser = pyany2json.LayexTableParser(
    [""], ["((vv$)(v+$v+$))(()(.+$)())+()", "(()(.+$))(()(.+$)())+()"]
)

model = builder.setTableParser(parser).build()

def visitTable(parent: pyany2json.TableGraph):
    for c in parent.children():
        table = c.getTable()
        if isinstance(table, pyany2json.DataTable):
            for header in table.headers():
                print(header.getName(), end=" ")
            print()
            for row in table.rows():
                for cell in row.cells():
                    print(cell.getValue(), end=" ")
                print()
        if len(c.children()) > 0:
            visitTable(c)
        
with pyany2json.load(
    FILE_PATH,
    encoding=FILE_ENCODING,
    model=model,
    hints=[pyany2json.INTELLI_LAYOUT],
) as doc:
    for sheet in doc.sheets():
        root = sheet.getTableGraph()
        if root.isPresent():
            visitTable(root.get())
