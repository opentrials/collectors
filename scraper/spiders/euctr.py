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
from .. import helpers


# Module API

class Euctr(CrawlSpider):

    # Public

    name = 'euctr'
    allowed_domains = ['clinicaltrialsregister.eu']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Make start urls
        self.start_urls = _make_start_urls(
                base='https://www.clinicaltrialsregister.eu/ctr-search/search',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(allow=_make_pattern('ctr-search/search'))),
            Rule(
                LinkExtractor(allow=r'ctr-search/trial/[\d-]+/[\w]+'),
                callback='parse_item'
            ),
        ]

        # Inherit parent
        super(Euctr, self).__init__(*args, **kwargs)

    def parse_item(self, res):

        # Create item
        item = items.Euctr()

        # Get summary
        key = None
        value = None
        for sel in res.css('.cellGrey, .cellGrey+.cellLighterGrey'):
            if sel.css('.cellGrey'):
                key = None
                value = None
                elements = sel.xpath('text()').extract()
                if elements:
                    key = helpers.slugify(elements[0].strip())
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
                    key = helpers.slugify(elements[0].strip())
            else:
                if key is not None:
                    value = None
                    elements = sel.xpath('text()').extract()
                    if elements:
                        value = elements[0].strip()
            if key and value:
                item.add_data(key, value)

        return item


# Internal

def _make_start_urls(base, date_from=None, date_to=None):
    """ Return start_urls.
    """
    if date_from is None:
        date_from = str(date.today() - timedelta(days=1))
    if date_to is None:
        date_to = str(date.today())
    query = OrderedDict()
    query['query'] = ''
    query['dateFrom'] = date_from
    query['dateTo'] = date_to
    return [base + '?' + urlencode(query)]


def _make_pattern(base):
    """ Return pattern.
    """
    pattern = base
    pattern += r'\?query=&dateFrom=[^&]&dateTo=[^&]&page=\d+'
    return pattern
