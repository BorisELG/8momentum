VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
CURRENT_DIR = $(shell pwd)

all: venv

$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

venv: $(VENV)/bin/activate

migrate: venv
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

superuser:
	$(PYTHON) manage.py createsuperuser

.PHONY: run
run: venv
	$(PYTHON) manage.py runserver

deploy:
	fly deploy --ha=false
