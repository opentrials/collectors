# Warehouse

The document describes OpenTrials `warehouse`.

### Basics

This database stores records collected from different sources.
It's a denormalized data storage.

### Tables

Each table corresponds to a source and its schema follows the structure of data from the origin.
To see the schema of each table please check the collector-specific docs
[here](https://github.com/opentrials/collectors/tree/master/docs/collectors)

### Technology

Database engine: `postgresql-9.4+`.
