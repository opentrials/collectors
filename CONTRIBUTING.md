# Contributing

The contributing guideline.

## Getting Started

Prerequisites:
- docker
- docker-compose

Recommended way to get started is to create and activate a project virtual environment.
To install package and development dependencies into active environment:

```
$ make develop
```

## Building

To build a docker image:

```
$ make build
```

## Testing

To run code review and tests:

```
$ make test
```

The project follow the next style guides:
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Deploying

Automatically on CI/CD server.

Required environment variables:
- $OPENTRIALS_DOCKER_EMAIL
- $OPENTRIALS_DOCKER_USER
- $OPENTRIALS_DOCKER_PASS
- $OPENTRIALS_WAREHOUSE_URL
- $OPENTRIALS_ICTRP_USER
- $OPENTRIALS_ICTRP_PASS

## Managing

To update, run and stop scrapers use Tutum's web UI.
