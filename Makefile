.PHONY: all build install lint list migrate push test


all: list

build:
	docker build -t opentrialsrobot/collectors .

install:
	pip install --upgrade -r requirements.dev.txt

lint:
	pylama scraper

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
	tutum login \
	-u $$OPENTRIALS_DOCKER_USER \
	-p $$OPENTRIALS_DOCKER_PASS
	docker push opentrialsrobot/collectors
	python scripts/push-stacks.py

test:
	py.test
