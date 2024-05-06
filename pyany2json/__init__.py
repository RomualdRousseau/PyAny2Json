from .setup import *
from .types import *
from .document_factory import *
from .layex_table_parser import *


def model_from_path(path: str):
    return ModelBuilder().fromPath(path)


def model_from_uri(uri: str):
    return ModelBuilder().fromURI(uri)


def model_from_json(data: str):
    return ModelBuilder().fromJSON(data)


def load(
    file_path: str,
    encoding: str = "UTF-8",
    model: Model | None = None,
    hints: list | None = None,
    recipe: list[str] | None = None,
    tag_case: str | None = None,
):
    doc = DocumentFactory.createInstance(file_path, encoding)
    if model:
        doc.setModel(model)
    if hints:
        doc.setHints(hints)
    if recipe:
        doc.setRecipe("\n".join(recipe))
    if tag_case:
        if tag_case == "SNAKE":
            doc.getTagClassifier().setSnakeMode(True)
        elif tag_case == "CAMEL":
            doc.getTagClassifier().setCamelMode(True)
    return doc
