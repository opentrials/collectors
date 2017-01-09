# Overview

This system is responsible for managing the schema of OpenTrials `warehouse` database and collecting
data to populate it.

## Stack

Collectors are fully compatible with Python2.7.

We use PostgreSQL for our database and [Alembic](http://alembic.zzzcomputing.com/en/latest/) for migrations.

Collectors are deployed and run in production with [DockerCloud](https://github.com/respect31/docker-cloud-example).

## Collectors

The system's collectors are independent python modules that share the following signature:

```python
def collect(conf, conn, *args):
    pass
```

Where arguments are:
- `conf` - config dict
- `conn` - connections dict
- `args` - collector arguments

To run a collector from command line:
```
$ make start <name> [<args>]
```

This code will trigger `collectors.<name>.collect(conf, conn, *args)` call.

*NOTE*: Most collectors need `date_from` and `date_to` arguments that define a
time range from which we want to extract resources. For example:

```
$ make start nct 2013-11-31 2013-12-01
```

To check if that is the case, see the `collect` function of the collector you are interested in.

### Scraping Collectors

Many collectors are scrapers. Scraping is based on
[Scrapy](https://scrapy.readthedocs.io/en/latest/intro/overview.html) framework. Here is
an example of how to use Scrapy in the `collect` function:

```python
from scrapy.crawler import CrawlerProcess
from .spider import <name>Spider

def collect(conf, conn, <args>):
    process = CrawlerProcess(conf)
    process.crawl(<name>Spider, conn=conn, <args>)
    process.start()
```

For more details check the tutorial [How to Write a Collector using Scrapy](https://github.com/opentrials/collectors/blob/master/docs/collector-scrapy-guide.md)

### Working with the database

The folder `collectors/base` contains multiple reusable components and
helpers including the [base class for a database record](https://github.com/opentrials/collectors/blob/master/collectors/base/record.py)
and the [base class for a record's field](https://github.com/opentrials/collectors/blob/master/collectors/base/fields.py).
Each collector that has a corresponding table in the `warehouse` database has to
define the schema for that table in a class that inherits from the base class for record.

For example the following class defines the schema for table `colors`. This table has
2 fields of type `Text`, one of which is a primary key:

```python
class ColorRecord(base.Record):
    table = 'colors'

    # Fields

    id = Text(primary_key=True)
    color = Text()
```

To see how this connects to the other parts of the collector check the [How to Write a Collector](https://github.com/opentrials/collectors/blob/master/docs/collector-guide.md) tutorial.
#### Altering the database schema

1. Define the table/field in the collector's record class as explained above.
2. Create a migration for it (more details in [Alembic docs](http://alembic.zzzcomputing.com/en/latest/tutorial.html#create-a-migration-script)).
