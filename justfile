set dotenv-load

install:
    poetry install

update:
    poetry update
    
build:
    poetry build
    mkdocs build
    
deploy:
    poetry publish --username __token__ --password $POETRY_PYPI_TOKEN --skip-existing 
    mkdocs gh-deploy

serve-doc:
    mkdocs serve
