.PHONY: all build install list migrate push start test


all: list

build:
	docker build -t okibot/collectors .

install:
	pip install --upgrade -r requirements.dev.txt

list:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

migrate:
	alembic upgrade head

push:
	$${CI?"Push is avaiable only on CI/CD server"}
	docker login \
    -e $$OPENTRIALS_DOCKER_EMAIL \
    -u $$OPENTRIALS_DOCKER_USER \
    -p $$OPENTRIALS_DOCKER_PASS
	docker push okibot/collectors
	python scripts/push-stacks.py

start:
	python -m collectors.base.cli $(filter-out $@,$(MAKECMDGOALS))

test:
	pylama collectors
	pylama migrations
	py.test

%:
	@:
