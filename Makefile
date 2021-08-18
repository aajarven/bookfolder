test:
	python -m pytest -v

coverage:
	python -m pytest --cov=bookfolder --cov-report=term-missing

clean:
	rm -rf dist

build:
	python -m build

upload: build
	python -m twine upload dist/*
