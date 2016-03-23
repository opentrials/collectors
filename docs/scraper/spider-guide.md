# How to Write a Spider Guide

This document describes how to write a new spider for the OpenTrials scraper
from scratch to a pull request.

As example we will be writing spider for `Pfizer` clinical trials register:

http://www.pfizer.com/research/clinical_trials.


## Getting Started

To get started fork https://github.com/opentrials/scraper repository.
After it the work on a new spider could be started (replace <user> by
your github username):

```
$ git clone git@github.com:<user>/scraper.git opentrials-scraper
$ cd opentrials-scraper
$ git checkout -b feature/giude-spider
$ virtualenv .python -p python2
$ source .python/bin/activate
$ make develop
$ cp .env.example .env && editor .env
```

On the last step you should set your development warehouse url
as value of `OPENTRIALS_WAREHOUSE_URL` in the `.env` file
(it should be postgres url like `postgres://...`).

Now you're ready to work on you own spider!

## Scraping Platform

- framework - [Scrapy](http://scrapy.readthedocs.org/en/latest/)
- warehouse - [PostgreSQL](http://www.postgresql.org/docs/9.4/static/index.html)

Directory named `scraper` is a `scrapy` project - everything written in
this framework documentation is applicable to the project.

## Bootstrapping a Spider

To bootstrap a new `guide` spider:

```
$ mkdir scraper/spiders/guide
$ touch scraper/spiders/guide/item.py
$ touch scraper/spiders/guide/parser.py
$ touch scraper/spiders/guide/spider.py
```

Expose `GuideSpider` (as `Guide`) class in `spiders` module
as the only one `scrapy` interface implemetation requirement:

> `scraper/spiders/__inint__.py`

```python
...
from .guide import GuideSpider as Guide
...
```

> `scraper/spiders/guide/__init__.py`

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .spider import GuideSpider
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
from scrapy.linkextractors import LinkExtractor

from .. import base
from .parser import GuideParser


# Module API

class GuideSpider(base.Spider):

    # Public

    name = 'guide'
    allowed_domains = ['pfizer.com']

    def __init__(self, *args, **kwargs):

        # Make parser
        self.parser = GuideParser()

        # Make urls
        self.start_urls = [
            'http://www.pfizer.com/research/clinical_trials/find_a_trial?recr=0',  # noqa
        ]

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'find_a_trial/NCT\d+',
            ), callback=self.parser.parse),
            Rule(LinkExtractor(
                allow=r'page=\d+',
            )),
        ]

        # Inherit parent
        super(GuideSpider, self).__init__(*args, **kwargs)
```

An instance of this class will call `parser.parse(response)` for
every http response from trial pages. We'll write a parser a bit later.

## Writing an Item

In this step we're working on `what's data our spider will get`.

Item is a model (like `django` model) for our spider. We have to describe
records we're going to scrape.

We need to discover concrete trial page:

http://www.pfizer.com/research/clinical_trials/find_a_trial/NCT01968967 (as example)

We see sections like `trial`, `study_type` etc. OpenTrials scraping platform
provide some `Field` classes to work with common field types:

https://github.com/opentrials/scraper/blob/master/scraper/spiders/base/fields.py

Based on discovered data and available base fields an item could look like:

> `scraper/spiders/guide/item.py`


```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from ..base.fields import Text, Date, Boolean, Integer, Json, Array  # noqa


# Module API

class GuideItem(base.Item):

    # Config

    table = 'guide'  # table name for warehouse
    primary_key = 'nct_id'  # primary key for warehouse
    updated_key = None  # key showing last updated date
    ensure_fields = True  # auto create tables/fields (debug mode)

    # General

    title = Text()

    # Description

    study_type = Text()
    organization_id = Text()
    nct_id = Text()
    status = Text()
    study_start_date = Date('%B, %Y')
    study_end_date = Date('%B, %Y')

    # Eligibility

    eligibility_criteria = Text()
    gender = Text()
    age_range = Text()
    healthy_volunteers_allowed = Boolean('Accepts Healthy Volunteers')
```

Item is what `parser.parse(response)` has to return to `Spider`.
Now we're ready to bring all together and write a parser.

## Writing a Parser

In this step we're working on `mapping http response to data model (item)`.

Parser is a connecting link between `Spider` and `Item`. We get http response
from `Spider` and return `Item` (or `None` to skip the data).

Any html parsing technique could be used. We will use scrapy's built-in
css selectors. Much more about other possibilities could be found at
scrapy documentation - http://scrapy.readthedocs.org/en/latest/topics/selectors.html.

> `scraper/spiders/guide/parser.py`

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .. import base
from .item import GuideItem


# Module API

class GuideParser(base.Parser):

    # Public

    def map(self, res):

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

        # Create item
        item = GuideItem.create(res.url, data)

        return item
```

## Start Scraping

We're ready to see our spider in scrapy list:

```
$ scrapy list
...
guide
...
```

And start an actual scraping:

```
$ scrapy crawl guide -L INFO
...
2016-03-01 17:38:25 [scraper.pipelines] INFO: Created item: <GUIDE: NCT00440492 [None]> - 14 fields
2016-03-01 17:38:36 [scraper.pipelines] INFO: Created item: <GUIDE: NCT00195234 [None]> - 14 fields
2016-03-01 17:38:44 [scraper.pipelines] INFO: Created item: <GUIDE: NCT00195221 [None]> - 14 fields
2016-03-01 17:38:48 [scraper.pipelines] INFO: Created item: <GUIDE: NCT00366249 [None]> - 14 fields
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
