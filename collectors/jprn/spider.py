# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from functools import partial
from urllib import urlencode
from collections import OrderedDict
from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from six.moves.urllib.parse import urlparse, parse_qs
from .parser import parse_record


# Module API

# TODO: ensure spider works
class Spider(CrawlSpider):

    # Public

    name = 'jprn'
    allowed_domains = ['upload.umin.ac.jp']

    def __init__(self, conn=None, page_from=None, page_to=None):

        # Save conn dict
        self.conn = conn

        # Default values
        if page_from is None:
            page_from = '1'
        if page_to is None:
            page_to = '1'

        # Make start urls
        self.start_urls = _make_start_urls(
                prefix='https://upload.umin.ac.jp/cgi-open-bin/ctr/ctr.cgi',
                page_from=page_from)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'cgi-open-bin/ctr/ctr.cgi\?function=brows',
            ), callback=parse_record),
            Rule(LinkExtractor(
                allow=r'page=\d+',
                process_value=partial(_process_url, page_from, page_to),
            )),
        ]

        # Inherit parent
        super(Spider, self).__init__()


# Internal

def _make_start_urls(prefix, page_from=None):
    """ Return start_urls.
    """
    if page_from is None:
        page_from = '1'
    query = OrderedDict()
    query['_page'] = page_from
    query['sort'] = '05'
    query['function'] = 'search'
    query['action'] = 'list'
    query['language'] = 'E'
    return [prefix + '?' + urlencode(query)]


def _process_url(page_from, page_to, url):

    # Get url page
    query = urlparse(url).query
    query = parse_qs(query)
    page = query.get('_page')

    # Preserve if match
    if page:
        page_from = int(page_from)
        page_to = int(page_to)
        page = int(page[0])
        if page >= page_from and page <= page_to:
            return url

    return None
