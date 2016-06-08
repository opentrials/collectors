# How to Write a Collector (using scrapy)

This document describes how to write a new scraping collector (scraper)
for the OpenTrials scraper from scratch to a pull request.

As example we will be writing scraper for `Pfizer` clinical trials register:

http://www.pfizer.com/research/clinical_trials.

## Getting Started

To get started fork https://github.com/opentrials/collectors repository.
After it the work on a new scraper could be started (replace <user> by
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

On the last step you should set your development warehouse url
as value of `WAREHOUSE_URL` in the `.env` file
(it should be postgres url like `postgres://...`).

Now you're ready to work on you own scraper!

## Platforms to Use

- framework - [Scrapy](http://scrapy.readthedocs.org/en/latest/)
- warehouse - [PostgreSQL](http://www.postgresql.org/docs/9.4/static/index.html)

## Writing a Scraping Collector

To bootstrap a new `guide` scraping collector:

```
$ mkdir collectors/guide
$ touch collectors/guide/collector.py
$ touch collectors/guide/parser.py
$ touch collectors/guide/record.py
$ touch collectors/guide/spider.py
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

Our collector will just deligate a work to  Scrapy framework:

> `collectors/guide/collect.py`

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.crawler import CrawlerProcess
from .spider import GuideSpider


def collect(conf, conn):
    process = CrawlerProcess(conf)
    process.crawl(GuideSpider, conn=conn)
    process.start()
```

## Writing a Spider

In this step we're working on `where our spider will get the data`.

To start with a spider we need to do the first discovering
job on the target site:

- domain - `pfizer.com`
- initial urls - `http://www.pfizer.com/research/clinical_trials/find_a_trial?recr=0`
- additional urls regex - `page=\d+`
- trial page regex - `find_a_trial/NCT\d+`

Also important to set `spider` name:

> `scraper/spiders/guide/spider.py`

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from .parser import parse_record


# Module API

class GuideSpider(CrawlSpider):

    # Public

    name = 'guide'
    allowed_domains = ['pfizer.com']

    def __init__(self):

        # Make urls
        self.start_urls = [
            'http://www.pfizer.com/research/clinical_trials/find_a_trial?recr=0',
        ]

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'find_a_trial/NCT\d+',
            ), callback=parse_record),
            Rule(LinkExtractor(
                allow=r'page=\d+',
            )),
        ]

        # Inherit parent
        super(GuideSpider, self).__init__()
```

An instance of this class will call `parse_record(response)` for
every http response from trial pages. We'll write an parser a bit later.

## Writing an Record

In this step we're working on `what's data our spider will get`.

Record is a model (like `django` model) for our spider. We have to describe
records we're going to scrape.

We need to discover concrete trial page:

http://www.pfizer.com/research/clinical_trials/find_a_trial/NCT01968967 (as example)

We see sections like `trial`, `study_type` etc. OpenTrials scraping platform
provide some `Field` classes to work with common field types:

https://github.com/opentrials/collectors/blob/master/collectors/base/fields.py

Based on discovered data and available base fields an item could look like:

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

class GuideItem(base.Record):

    # Config

    table = 'guide'  # table name for warehouse
    ensure_fields = True  # auto create tables/fields (debug mode)

    # General

    nct_id = Text(primary_key=True) # set primary key
    title = Text()

    # Description

    study_type = Text()
    organization_id = Text()
    status = Text()
    study_start_date = Date('%B, %Y')
    study_end_date = Date('%B, %Y')

    # Eligibility

    eligibility_criteria = Text()
    gender = Text()
    age_range = Text()
    healthy_volunteers_allowed = Boolean('Accepts Healthy Volunteers')
```

Record is what `ectract_record` has to return to `Spider`.
Now we're ready to bring all together and write a parser.

## Writing a Parser

In this step we're working on `mapping http response to data model (record)`.

Record parser is a connecting link between `Spider` and `Record`. We get http response
from `Spider` and return `Record` (or `None` to skip the data).

Any html parsing technique could be used. We will use scrapy's built-in
css selectors. Much more about other possibilities could be found at
scrapy documentation - http://scrapy.readthedocs.org/en/latest/topics/selectors.html.

> `collectors/guide/parser.py`

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .item import GuideRecord


def parse_record(res):

    # Init data
    data = {}

    # Description

    key = 'study_type'
    path = '.field-name-field-study-type .field-item::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'organization_id'
    path = '.field-name-field-organization-id .field-item::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'nct_id'
    path = '.field-name-field-clinical-trial-id .field-item::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'status'
    path = '//label[text() = "Status"]/../text()'
    value = ''.join(res.xpath(path).extract()).strip()
    data[key] = value

    key = 'study_start_date'
    path = '.field-name-field-study-start-date .field-item span::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'study_end_date'
    path = '.field-name-field-study-end-date .field-item span::text'
    value = res.css(path).extract_first()
    data[key] = value

    # Eligibility

    key = 'eligibility_criteria'
    path = '.field-name-field-criteria .field-item *::text'
    value = ''.join(res.css(path).extract())
    data[key] = value

    key = 'gender'
    path = '.field-name-field-gender .field-item::text'
    value = res.css(path).extract_first()
    data[key] = value

    key = 'age_range'
    path = '//label[text() = "Age Range:"]/../text()'
    value = ''.join(res.xpath(path).extract()).strip()
    data[key] = value

    key = 'healthy_volunteers_allowed'
    path = '.field-name-field-healthy-volunteers-allowed .field-item::text'
    value = res.css(path).extract_first()
    data[key] = value

    # Create record
    record = GuideRecord.create(res.url, data)

    return record
```

## Start Scraping

We're ready to start an actual scraping:

```
$ make start guide
...
2016-03-01 17:38:25 [scraper.pipelines] DEBUG: Record - created: <GUIDE: NCT00440492 [None]> - 14 fields
2016-03-01 17:38:36 [scraper.pipelines] DEBUG: Record - created: <GUIDE: NCT00195234 [None]> - 14 fields
2016-03-01 17:38:44 [scraper.pipelines] DEBUG: Record - created: <GUIDE: NCT00195221 [None]> - 14 fields
2016-03-01 17:38:48 [scraper.pipelines] DEBUG: Record - created: <GUIDE: NCT00366249 [None]> - 14 fields
...
```

Scraped data will be in the warehouse's `guide` table.

> To use `scrapy` CLI tool add `collectors.guide.spider`
to `collectors.base.config.SPIDER_MODULES`.

## Sharing the Work

Now a pull request to OpenTrials could be prepared:

```
$ make test
$ git commit -am 'implemented guide spider'
$ git push origin feature/guide-spider -u
```

And sent using github web interface.

Thanks!
