### Prerequisite

Programs:
- docker
- docker-compose

Environment variables:
- $OPENTRIALS_TUTUM_EMAIL
- $OPENTRIALS_TUTUM_USER
- $OPENTRIALS_TUTUM_PASS
- $OPENTRIALS_DATABASE_URL

### Getting Started

To activate virtual environment, install
dependencies, add pre-commit hook to review and test code:

```
$ source activate.sh
```

### Reviewing

To check the project:

```
$ mario review
```

### Testing

To run tests with coverage check:

```
$ mario test
```

Coverage data will be in the `.coverage` file.

### Deploying

Automatically using CI/CD (Travis) [under developmet].

Manual steps (not recomended):
- `mario login` - login with docker & tutum
- `mario build` - build docker images
- `mario push` - push docker images to remote index
- `mario deploy` - deploy it as tutum stack
