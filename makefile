install:
	poetry install

lint:
	poetry run flake8 task_manager

test:
	poetry run python3 manage.py test

test-cov:
	poetry run python3 manage.py test --cov=task_manager --cov-report xml tests/