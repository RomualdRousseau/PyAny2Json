set dotenv-load

install:
    poetry install

update:
    poetry update
    
build:
    poetry build
    mkdocs build
    
deploy: deploy-doc
    poetry publish --username __token__ --password $POETRY_PYPI_TOKEN --skip-existing

deploy-doc:
    mkdocs gh-deploy

serve-doc:
    mkdocs serve
