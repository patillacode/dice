
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

tailwind:
	@echo 'Running tailwind ...'
	. venv/bin/activate && \
	python manage.py tailwind start

reset-db:
	. venv/bin/activate && \
	dropdb dicedb && \
	createdb dicedb && \
	rm -rf game/migrations/*.py && \
	python manage.py migrate && \
	export DJANGO_SUPERUSER_PASSWORD='admin' && \
	export DJANGO_SUPERUSER_USERNAME='admin' && \
	export DJANGO_SUPERUSER_EMAIL='admin@admin.com' && \
	python manage.py createsuperuser --noinput && \
	python manage.py makemigrations game && \
	python manage.py migrate
