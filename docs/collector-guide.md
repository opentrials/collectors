# How to Write a Collector

This document describes how to write a new plain Python collector
for the OpenTrials platform from scratch to a pull request.

As an example we will be writing a collector template for some API
returning JSON date:

## Getting Started

To get started fork https://github.com/opentrials/collectors repository.
After it the work on a new collector could be started (replace <user> by
your github username):

```
$ git clone git@github.com:<user>/collectors.git opentrials-collectors
$ cd opentrials-collectors
$ git checkout -b feature/giude-scraper
$ virtualenv .python -p python2
$ source .python/bin/activate
$ make install
$ cp .env.example .env && editor .env
```

On the last step you should setup you develpment environment. Follow
`.evn.example` file instructions and comments.

Now you're ready to work on you own collector!

## Writing a Collector

To bootstrap a new `guide` collector:

```
$ mkdir collectors/guide
$ touch collectors/guide/collector.py
$ touch collectors/guide/parser.py
$ touch collectors/guide/record.py
```

Expose `collect` function as the only one interface
implemetation requirement:

> `collectors/guide/__init__.py`

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .collector import collect
```

In collector we have main control flow:

> `collectors/guide/collect.py`

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time
import logging
import requests
import datetime
from .. import base
from .parser import parse_record
logger = logging.getLogger(__name__)


# Module API

def collect(conf, conn):
    URL = <set API url>

    # Start collector
    date_from = <write a function to find a date to start collection>
    base.helpers.start('guide', {'date_from': date_from})

    # Collect records
    count = 0
    chunk_days = 100
    session = requests.Session()
    while True:
        if date_from > datetime.date.today():
            break
        date_to = date_from + datetime.timedelta(days=chunk_days)
        url = _make_request_url(URL, date_from, date_to)
        response = session.get(url)
        for item in response.json():
            try:
                record = parse_record(response.url, item)
                record.write(conf, conn)
                count += 1
                if not count % 100:
                    logger.info('Collected "%s" guide records', count)
            except Exception as exception:
                logger.exception('Collecting error: %s', repr(exception))
        date_from = date_to + datetime.timedelta(days=1)
        time.sleep(1)

    # Stop collector
    base.helpers.stop('guide', {'collected': count})
```

## Writing an Record

In this step we're working on `what's data our collector will get`.

Record is a model (like `django` model) for our collector. We have to describe
records we're going to collect.

> `collectors/guide/record.py`


```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Boolean


# Module API

class Record(base.Record):

    # Config

    table = 'guide'  # table name for warehouse

    # General

    guide_id = Text(primary_key=True) # set primary key
    title = Text()
    current = Boolean('Yes')
    registered_date = Date('%Y-%m-%d')
```

Record is what `parse_record` has to return to the `collect` function.
Now we're ready to bring all together and write a parser.

## Writing a Parser

In this step we're working on `mapping http response to data model (record)`.

Record parser is a connecting link between `collect` and `Record`. We get http response
from `collect` and return `Record`.

> `collectors/guide/parser.py`

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .item import Record


def parse_record(url, item):

    # Init data
    data = {}

    # General

    <map item to record data>

    # Create record
    record = Record.create(url, data)

    return record
```

## Start Scraping

We're ready to start an actual collection:

```
$ make start guide
...
2016-03-01 17:38:25 [scraper.pipelines] DEBUG: Record - created: <GUIDE: ID1> - 14 fields
2016-03-01 17:38:36 [scraper.pipelines] DEBUG: Record - created: <GUIDE: ID2> - 14 fields
2016-03-01 17:38:44 [scraper.pipelines] DEBUG: Record - created: <GUIDE: ID3> - 14 fields
2016-03-01 17:38:48 [scraper.pipelines] DEBUG: Record - created: <GUIDE: ID4> - 14 fields
...
```

Scraped data will be in the warehouse's `guide` table.

## Sharing the Work

Now a pull request to OpenTrials could be prepared:

```
$ make test
$ git commit -am 'implemented guide spider'
$ git push origin feature/guide-spider -u
```

And sent using github web interface.

Thanks!
