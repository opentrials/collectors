# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from urllib import urlencode
from collections import OrderedDict
from datetime import date, timedelta
from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from .parser import parse_record


# Module API

class Spider(CrawlSpider):

    # Public

    name = 'isrctn'
    allowed_domains = ['isrctn.com']

    def __init__(self, conn=None, date_from=None, date_to=None):

        # Save conn dict
        self.conn = conn

        # Make start urls
        self.start_urls = _make_start_urls(
                prefix='http://www.isrctn.com/search',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'ISRCTN\d+',
            ), callback=parse_record),
            Rule(LinkExtractor(
                allow=r'page=\d+',
            )),
        ]

        # Inherit parent
        super(Spider, self).__init__()


# Internal

def _make_start_urls(prefix, date_from=None, date_to=None):
    """ Return start_urls.
    """
    if date_from is None:
        date_from = str(date.today() - timedelta(days=1))
    if date_to is None:
        date_to = str(date.today())
    query = OrderedDict()
    query['q'] = ''
    gtle = 'GT lastEdited:%sT00:00:00.000Z' % date_from
    lele = 'LE lastEdited:%sT00:00:00.000Z' % date_to
    query['filters'] = ','.join([gtle, lele])
    query['page'] = '1'
    query['pageSize'] = '100'
    query['searchType'] = 'advanced-search'
    return [prefix + '?' + urlencode(query)]
