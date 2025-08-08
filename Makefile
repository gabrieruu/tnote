IMAGE_NAME := tnote_dev
DOCKER ?= docker

.PHONY: fmt

fmt:
	black tnote/*.py
	black tnote/commands/*.py
	black tests/

cleanse:
	python3 tests/cleanse.py

populate:
	python3 tests/populate.py

dev:
	$(DOCKER)-compose run --rm dev
	$(DOCKER) rmi ${IMAGE_NAME} || true

mypy:
	@python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip install -q -r requirements.txt && \
	mypy tnote
