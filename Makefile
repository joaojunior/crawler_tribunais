run_tests:
	docker-compose -f docker-compose.yml -f docker-compose.tests.yml up --build --exit-code-from api

quality:
	flake8 --filename=*.py src/ tests/
	isort **/*.py -c -vb
	radon cc . -a -s -na

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
	find . -type d -name .pytest_cache -exec rm -r {} \+
