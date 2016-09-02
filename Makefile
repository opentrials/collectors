.PHONY: all build deploy install list migrate push start test up


all: list

build:
	docker build -t okibot/collectors .

deploy: push
	$${CI?"Deploy is avaiable only on CI/CD server"}
	# docker-cloud stack stop --sync collectors || echo 'not running'
	make migrate
	# docker-cloud stack start --sync collectors

install:
	pip install --upgrade -r requirements.dev.txt

list:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

migrate:
	alembic upgrade head

push:
	$${CI?"Push is avaiable only on CI/CD server"}
	docker login -e $$DOCKER_EMAIL -u $$DOCKER_USER -p $$DOCKER_PASS
	docker push okibot/collectors
	docker-cloud stack inspect collectors || docker-cloud stack create --sync -n collectors
	docker-cloud stack update --sync collectors

start:
	python -m collectors.base.cli $(filter-out $@,$(MAKECMDGOALS))

test:
	pylama collectors
	pylama migrations
	py.test

up:
	docker-compose up

%:
	@:
