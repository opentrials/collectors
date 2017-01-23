# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from urllib import urlencode
from functools import partial
from collections import OrderedDict
from datetime import date, timedelta
from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from .parser import parse_record


# Module API

class Spider(CrawlSpider):

    # Public

    name = 'euctr'
    allowed_domains = ['clinicaltrialsregister.eu']

    def __init__(self, conf=None, conn=None, date_from=None, date_to=None):

        # Save conf/conn
        self.conf = conf
        self.conn = conn

        # Make start urls
        self.start_urls = _make_start_urls(
                prefix='https://www.clinicaltrialsregister.eu/ctr-search/search',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(
                LinkExtractor(
                    allow=r'ctr-search/trial/[\d-]+/[\w]+',
                    deny=r'results$'
                ),
                callback=parse_record
            ),
            Rule(
                LinkExtractor(
                    allow=r'page=\d+',
                    restrict_css='[accesskey=n]'
                ),
                process_links=partial(_process_links, self.start_urls)
            ),
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
    query['query'] = ''
    query['dateFrom'] = date_from
    query['dateTo'] = date_to
    return [prefix + '?' + urlencode(query)]


def _process_links(start_urls, links):
    result = []
    for link in links:
        link.url = '&page='.join([start_urls[0], link.url.split('=')[-1]])
        result.append(link)
    return result
