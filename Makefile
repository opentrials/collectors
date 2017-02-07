.PHONY: all build install list migrate start test up

all: list

build:
	docker build -t opentrials/collectors .

list:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

migrate:
	alembic upgrade head

start:
	python -m collectors.base.cli $(filter-out $@,$(MAKECMDGOALS))

test:
	tox

up:
	docker-compose up

%:
	@:
