# Overview

This system is responsible for data collecting to `warehouse`.

## Stacks

The system provides the following stacks:
- `make-initial-collecting` - collect anything initially
- `collectors` - continuous collecting of updated sources

About Docker Cloud deployment see -
https://github.com/respect31/docker-cloud-example.

## Warehouse

See more about `warehouse` - [warehouse](warehouse.md).

## Collectors

The system's processors are independent python modules
compatible to the following signature:

```python
def collect(conf, conn, *args):
    pass
```

Where arguments are:
- `conf` - config dict
- `conn` - connections dict
- `args` - processor arguments

To run one of collectors from command line:
```
make start <name> [<args>]
```

This code will trigger `collectors.<name>.collect(conf, conn, *args)` call.

### Scraping Collectors

Many of `collectors` are scrapers. Scraping is based on
Scrapy framework. In a `collect` call those `collectors` use
this framrwork programmaticly:

```python
from scrapy.crawler import CrawlerProcess
from .spider import <name>Spider

def collect(conf, conn, <args>):
    process = CrawlerProcess(conf)
    process.crawl(<name>Spider, conn=conn, <args>)
    process.start()
```

More about Scrapy - https://scrapy.readthedocs.io/en/latest/

## Base library

For developers convenient in a `collectors.base` module
there are shared library of reusable components to write collectors.

See documentation in source code to use it.
