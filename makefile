install:
	poetry install

lint:
	poetry run flake8 task_manager

test:
	poetry run python3 manage.py test

test-cov:
	poetry run coverage run manage.py test