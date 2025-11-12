.PHONY: all check run check.pip clean
.SILENT: all check run check.pip

VENV_NAME := .venv
VENV_PYTHON := $(VENV_NAME)/bin/python3
VENV_STREAMLIT := $(VENV_NAME)/bin/streamlit

LOG_INFO := echo "- "

all: check run

run:
	$(LOG_INFO) "Running application..."
	$(VENV_STREAMLIT) run src/main.py

check: check.pip

check.pip:
	$(LOG_INFO) "Checking pip ($(CVENV_PYTHON))..."
	@if [ ! -d "$(VENV_NAME)" ]; then \
		$(LOG_INFO) "Creating virtual environment..."; \
		python3 -m venv $(VENV_NAME); \
		$(LOG_INFO) "Installing dependencies..."; \
		$(VENV_PYTHON) -m pip install -r requirements.txt; \
	fi

clean:
	rm -rf $(VENV_NAME)
