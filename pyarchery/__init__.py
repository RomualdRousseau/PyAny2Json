# ruff: noqa: F401, F403, E402

import jpype
import jpype.imports

from pyarchery.config import JAR_PATH, LIB_PATH

jpype.startJVM(
    "-ea",
    "--add-opens=java.base/java.nio=ALL-UNNAMED",
    classpath=[f"{JAR_PATH}/*", f"{LIB_PATH}/*"],
)

from pyarchery.archery import (
    CAMEL,
    INTELLI_EXTRACT,
    INTELLI_LAYOUT,
    INTELLI_TAG,
    INTELLI_TIME,
    SNAKE,
    DocumentFactory,
    LayexTableParser,
    Model,
    ModelBuilder,
)
from pyarchery.wrappers import DocumentWrapper


def model_from_path(path: str):
    return ModelBuilder().fromPath(path)


def model_from_url(url: str):
    return ModelBuilder().fromURL(url)


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
            doc.getTagClassifier().setTagStyle(SNAKE)
        elif tag_case == "CAMEL":
            doc.getTagClassifier().setTagStyle(CAMEL)
    return DocumentWrapper(doc)
