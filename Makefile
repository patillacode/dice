
python-install:
	@echo 'Installing venv and requirements ...' && \
	python3 -m venv venv && \
	. venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

pre-commit-install:
	@echo 'Installing pre-commit ...' && \
	pre-commit install

requirements:
	@echo 'Creating requirements.txt file and syncing/installing (if needed)'
	. venv/bin/activate && \
	pip-compile --output-file=requirements.txt requirements.in && \
	pip-sync --pip-args="--no-cache-dir" requirements.txt

run:
	@echo 'Running server ...'
	. venv/bin/activate && \
	python manage.py runserver
