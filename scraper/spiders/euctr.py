# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from urllib import urlencode
from datetime import date, timedelta
from collections import OrderedDict
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from .. import items
from .. import utils


# Module API

class Euctr(CrawlSpider):

    # Public

    name = 'euctr'
    allowed_domains = ['clinicaltrialsregister.eu']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Make start urls
        self.start_urls = utils.euctr.make_start_urls(
                prefix='https://www.clinicaltrialsregister.eu/ctr-search/search',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(allow=utils.euctr.make_pattern('ctr-search/search'))),
            Rule(
                LinkExtractor(allow=r'ctr-search/trial/[\d-]+/[\w]+'),
                callback='parse_item'
            ),
        ]

        # Inherit parent
        super(Euctr, self).__init__(*args, **kwargs)

    def parse_item(self, res):

        # Create item
        item = items.Euctr.create(source=res.url)

        # Get summary
        key = None
        value = None
        for sel in res.css('.cellGrey, .cellGrey+.cellLighterGrey'):
            if sel.css('.cellGrey'):
                key = None
                value = None
                elements = sel.xpath('text()').extract()
                if elements:
                    key = utils.base.slugify(elements[0].strip())
            else:
                if key is not None:
                    value = None
                    elements = sel.xpath('text()').extract()
                    if elements:
                        value = elements[0].strip()
            if key and value:
                item.add_data(key, value)

        # Get data
        key = None
        value = None
        for sel in res.css('.second, .second+.third'):
            if sel.css('.second'):
                key = None
                value = None
                elements = sel.xpath('text()').extract()
                if elements:
                    key = utils.base.slugify(elements[0].strip())
            else:
                if key is not None:
                    value = None
                    elements = sel.xpath('text()').extract()
                    if elements:
                        value = elements[0].strip()
            if key and value:
                item.add_data(key, value)

        return item
