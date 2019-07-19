run_tests:
	env PYTHONPATH=src pytest

quality:
	flake8 --filename=*.py src/ tests/
	isort **/*.py -c -vb

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
	find . -type d -name .pytest_cache -exec rm -r {} \+
