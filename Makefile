.PHONY: all build deploy install lint list migrate test


all: list

build:
	docker build -t opentrialsrobot/collectors .

deploy:
	$${CI?"Deployment is avaiable only on CI/CD server"}
	docker login \
    -e $$OPENTRIALS_DOCKER_EMAIL \
    -u $$OPENTRIALS_DOCKER_USER \
    -p $$OPENTRIALS_DOCKER_PASS
	tutum login \
	-u $$OPENTRIALS_DOCKER_USER \
	-p $$OPENTRIALS_DOCKER_PASS
	docker push opentrialsrobot/collectors
	python scripts/deploy-stacks.py

install:
	pip install --upgrade -r requirements.dev.txt

lint:
	pylama scraper

list:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

migrate:
	alembic upgrade head

test:
	py.test
