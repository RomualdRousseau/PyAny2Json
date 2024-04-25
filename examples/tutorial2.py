from pyany2json import ModelBuilder, LayexTableParser, DocumentFactory, INTELLI_LAYOUT

REPO_BASE_URL = "https://raw.githubusercontent.com/RomualdRousseau/Any2Json-Models/main"
MODEL_NAME = "sales-english"
FILE_PATH = "data/document with multiple tables.xlsx"
FILE_ENCODING = "UTF-8"


builder = ModelBuilder().fromURI("{0}/{1}/{1}.json".format(REPO_BASE_URL, MODEL_NAME))
parser = LayexTableParser(["(v.$)+"], ["(()(S+$))(()([/^TOTAL/|v].+$)())+(/TOTAL/.+$)"])
entities = builder.getEntityList()
entities.append("PRODUCTNAME")
entities = [v for v in builder.getEntityList() if v != "PACKAGE"]
patterns = builder.getPatternMap()
patterns["\\D+\\dml"] = "PRODUCTNAME"
patterns = {k: v for (k, v) in builder.getPatternMap().items() if v != "PACKAGE"}
model = (
    builder.setTableParser(parser)
    .setEntityList(entities)
    .setPatternMap(patterns)
    .build()
)

with DocumentFactory.createInstance(FILE_PATH, FILE_ENCODING) as doc:
    doc.setModel(model)
    doc.setHints([INTELLI_LAYOUT])
    doc.setRecipe("sheet.setCapillarityThreshold(0)")
    doc.getTagClassifier().setSnakeMode(True)
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
