# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from urllib import urlencode
from datetime import datetime, date, timedelta
from collections import OrderedDict
from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from .parser import parse_record


# Module API

class NctSpider(CrawlSpider):

    # Public

    name = 'nct'
    allowed_domains = ['clinicaltrials.gov']

    def __init__(self, conn=None, date_from=None, date_to=None):

        # Save conn dict
        self.conn = conn

        # Make start urls
        self.start_urls = _make_start_urls(
                prefix='https://www.clinicaltrials.gov/ct2/results',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'ct2/show/NCT\d+',
                process_value=lambda value: value+'&resultsxml=true',
            ), callback=parse_record),
            Rule(LinkExtractor(
                allow=r'pg=\d+$',
            )),
        ]

        # Inherit parent
        super(NctSpider, self).__init__()


# Internal

def _make_start_urls(prefix, date_from=None, date_to=None):
    """ Return start_urls.
    """
    if date_from is None:
        date_from = str(date.today() - timedelta(days=1))
    if date_to is None:
        date_to = str(date.today())
    query = OrderedDict()
    date_from = datetime.strptime(date_from, '%Y-%m-%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d')
    query['lup_s'] = date_from.strftime('%m/%d/%Y')
    query['lup_e'] = date_to.strftime('%m/%d/%Y')
    return [prefix + '?' + urlencode(query)]
