VENV_NAME = db_flask
PYTHON = $(VENV_NAME)/bin/python3
PIP = $(VENV_NAME)/bin/pip
FLASK_APP = app/run.py

.PHONY: all venv run clean

all: venv run

venv:
	python3 -m venv $(VENV_NAME)
	$(PIP) install -r requirements.txt

run:
	FLASK_APP=$(FLASK_APP) $(PYTHON) -m flask run --debug -p 5000

# test: venv/bin/python
# 	venv/bin/python app.py &
# 	sleep 1 # give app a second to startup
# 	-venv/bin/python test_client.py
# 	pkill -in python # hope that the newest python process is the app
	
clean:
	rm -rf $(VENV_NAME)
	rm -rf __pycache__
	rm -f *.db
	rm -f *.pyc