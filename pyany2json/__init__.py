from .setup import *  # noqa: F403
from .types import *  # noqa: F403
from .layex_table_parser import *  # noqa: F403

from .document_factory import (
    DocumentFactory,
    TableGraph,  # noqa: F401
    DataTable,  # noqa: F401
    INTELLI_EXTRACT,  # noqa: F401
    INTELLI_LAYOUT,  # noqa: F401
    INTELLI_TAG,  # noqa: F401
)
from .model import Model, ModelBuilder


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
