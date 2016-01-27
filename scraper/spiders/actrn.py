# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from urllib import urlencode
from datetime import datetime, date, timedelta
from collections import OrderedDict
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from .. import items
from .. import utils


# Module API

class Actrn(CrawlSpider):

    # Public

    name = 'actrn'
    allowed_domains = ['anzctr.org.au']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Make start urls
        self.start_urls = _make_start_urls(
                base='http://www.anzctr.org.au/TrialSearch.aspx',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(allow=_make_pattern('TrialSearch.aspx'))),
            Rule(
                LinkExtractor(
                    allow=r'Trial/Registration/TrialReview.aspx',
                    process_value=lambda value: value.replace('http', 'https', 1),
                ),
                callback='parse_item'
            ),
        ]

        # Inherit parent
        super(Actrn, self).__init__(*args, **kwargs)

    def parse_item(self, res):

        # Create item
        item = items.Actrn.create(source=res.url)

        # Get data
        key = None
        value = None
        for sel in res.css('.review-element-name, .review-element-content'):
            if sel.css('.review-element-name'):
                key = None
                value = None
                elements = sel.xpath('text()').extract()
                if elements:
                    key = utils.base.slugify(elements[0].strip())
            else:
                if key is not None:
                    value = None
                    elements = sel.xpath('span/text()').extract()
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
    date_from = datetime.strptime(date_from, '%Y-%m-%d').strftime('%d/%m/%Y')
    date_to = datetime.strptime(date_to, '%Y-%m-%d').strftime('%d/%m/%Y')
    query['searchTxt'] = ''
    query['dateOfRegistrationFrom'] = date_from
    query['dateOfRegistrationTo'] = date_to
    query['registry'] = 'ANZCTR'
    query['isBasic'] = 'False'
    return [base + '?' + urlencode(query)]


def _make_pattern(base):
    """ Return pattern.
    """
    return base + r'.*&page=\d+'
