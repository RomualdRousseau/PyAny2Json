import pyany2json

REPO_BASE_URL = "https://raw.githubusercontent.com/RomualdRousseau/Any2Json-Models/main"
MODEL_NAME = "sales-english"
FILE_PATH = "data/document with multiple tables.xlsx"
FILE_ENCODING = "UTF-8"


builder = pyany2json.model_from_uri(f"{REPO_BASE_URL}/{MODEL_NAME}/{MODEL_NAME}.json")

entities = [v for v in builder.getEntityList() if v != "PACKAGE"]
entities.append("PRODUCTNAME")

patterns = {k: v for (k, v) in builder.getPatternMap().items() if v != "PACKAGE"}
patterns["\\D+\\dml"] = "PRODUCTNAME"

parser = pyany2json.LayexTableParser(
    ["(v.$)+"], ["(()(S+$))(()([/^TOTAL/|v].+$)())+(/TOTAL/.+$)"]
)

model = (
    builder.setEntityList(entities)
    .setPatternMap(patterns)
    .setTableParser(parser)
    .build()
)


with pyany2json.load(
    FILE_PATH,
    encoding=FILE_ENCODING,
    model=model,
    hints=[pyany2json.INTELLI_LAYOUT],
    recipe=["sheet.setCapillarityThreshold(0)"],
    tag_case="SNAKE",
) as doc:
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
