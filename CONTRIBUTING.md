# Contributing

The contributing guideline.

## Getting Started

Prerequisites:
- docker
- docker-compose

To activate virtual environment, install
dependencies, add pre-commit hook to review and test code:

```
$ source activate.sh
```

## Testing

To run code review and tests:

```
$ mario test
```

The project follow the next style guides:
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Building

To build a docker image:

```
$ mario build
```

## Previewing

To run locally:

```
$ mario preview
```

Required environment variables:
- $OPENTRIALS_DATABASE_URL

## Deploying

Automatically on CI/CD server.

Required environment variables:
- $OPENTRIALS_TUTUM_EMAIL
- $OPENTRIALS_TUTUM_USER
- $OPENTRIALS_TUTUM_PASS
- $OPENTRIALS_DATABASE_URL

## Managing

To update, run and stop scrapers use Tutum's web UI.
