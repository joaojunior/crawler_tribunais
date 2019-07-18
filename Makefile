run_tests:
	env PYTHONPATH=src pytest

quality:
	flake8 --filename=*.py src/ tests/
	isort **/*.py -c -vb
