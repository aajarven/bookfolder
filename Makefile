test:
	python -m pytest -v

coverage:
	python -m pytest --cov=bookfolder --cov-report=term-missing
