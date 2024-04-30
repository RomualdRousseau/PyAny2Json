from pyany2json import ModelBuilder, LayexTableParser, DocumentFactory, INTELLI_LAYOUT
from pyany2json.document_factory import DataTable, TableGraph


REPO_BASE_URL = "https://raw.githubusercontent.com/RomualdRousseau/Any2Json-Models/main"
MODEL_NAME = "sales-english"
FILE_PATH = "data/AG120-N-074.pdf"
FILE_ENCODING = "UTF-8"


builder = ModelBuilder().fromURI("{0}/{1}/{1}.json".format(REPO_BASE_URL, MODEL_NAME))
parser = LayexTableParser(
    [""], ["((vv$)(v+$v+$))(()(.+$)())+()", "(()(.+$))(()(.+$)())+()"]
)
model = (
    builder.setTableParser(parser)
    .build()
)

def visitTable(parent: TableGraph):
    for c in parent.children():
        table = c.getTable()
        if isinstance(table, DataTable):
            for header in table.headers():
                print(header.getName(), end=" ")
            print()
            for row in table.rows():
                for cell in row.cells():
                    print(cell.getValue(), end=" ")
                print()
        if len(c.children()) > 0:
            visitTable(c)
        
with DocumentFactory.createInstance(FILE_PATH, FILE_ENCODING) as doc:
    doc.setModel(model)
    doc.setHints([INTELLI_LAYOUT])
    for sheet in doc.sheets():
        root = sheet.getTableGraph()
        if root.isPresent():
            visitTable(root.get())
