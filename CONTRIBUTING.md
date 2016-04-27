# Contributing

The project follows the [Open Knowledge International coding standards](https://github.com/okfn/coding-standards).

## Getting Started

```
virtualenv .python -p python2
source .python/bin/activate
make install
cp .env.example .env
editor .env # set your values
set -a; source .env
```

## Building

To build a docker image:

```
$ make build
```

## Testing

To run tests:

```
$ make test
```
