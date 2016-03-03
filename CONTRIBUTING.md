# Contributing

The project follows the [Open Knowledge International coding standards](https://github.com/okfn/coding-standards).

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

## Linting

To run lint:

```
$ make lint
```

## Testing

To run tests:

```
$ make test
```

## Deploying

Automatically on CI/CD server.

Required environment variables:
- $OPENTRIALS_DOCKER_EMAIL
- $OPENTRIALS_DOCKER_USER
- $OPENTRIALS_DOCKER_PASS
- $OPENTRIALS_WAREHOUSE_URL

## Managing

To update, run and stop scrapers use Tutum's web UI.
