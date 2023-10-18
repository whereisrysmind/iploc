install: pyproject.toml
	poetry install

unittest: install
	poetry run pytest -v tests/unit

functest: install
	poetry run pytest -v tests/functional