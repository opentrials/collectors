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

    name = 'gsk'
    allowed_domains = ['gsk-clinicalstudyregister.com']

    def __init__(self, conf=None, conn=None, date_from=None, date_to=None):

        # Save conf/conn
        self.conf = conf
        self.conn = conn

        # Make start urls
        self.start_urls = _make_start_urls(
                prefix='http://www.gsk-clinicalstudyregister.com/search',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'study\/\d+'
            ), callback=parse_record),
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
    query['last_updated_from'] = date_from
    query['last_updated_to'] = date_to
    return [prefix + '?' + urlencode(query)]
