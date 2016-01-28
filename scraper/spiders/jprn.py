# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from urllib import urlencode
from collections import OrderedDict
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from six.moves.urllib.parse import urlparse, parse_qs

from .. import items
from .. import utils


# Module API

class Jprn(CrawlSpider):

    # Public

    name = 'jprn'
    allowed_domains = ['upload.umin.ac.jp']

    def __init__(self, page_from=None, page_to=None, *args, **kwargs):

        # Default values
        if page_from is None:
            page_from = '1'
        if page_to is None:
            page_to = '1'

        # Save attributes
        self.__page_from = page_from
        self.__page_to = page_to

        # Make start urls
        self.start_urls = utils.jprn.make_start_urls(
                prefix='https://upload.umin.ac.jp/cgi-open-bin/ctr/ctr.cgi',
                page_from=page_from)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=utils.jprn.make_pattern('cgi-open-bin/ctr/ctr.cgi'),
                process_value=self.process_url,
            )),
            Rule(
                LinkExtractor(allow=r'cgi-open-bin/ctr/ctr.cgi\?function=brows',),
                callback='parse_item',
            ),
        ]

        # Inherit parent
        super(Jprn, self).__init__(*args, **kwargs)

    def process_url(self, url):

        # Get url page
        query = urlparse(url).query
        query = parse_qs(query)
        page = query.get('_page')

        # Preserve if match
        if page:
            page_from = int(self.__page_from)
            page_to = int(self.__page_to)
            page = int(page[0])
            if page >= page_from and page <= page_to:
                return url

        return None

    def parse_item(self, res):

        # Create item
        item = items.Jprn.create(source=res.url)

        # Get meta
        data = utils.jprn.extract_table(res, key_index=0, value_index=2)
        for key, value in data.items():
            item.add_data(key, value)

        # Get data
        data = utils.jprn.extract_table(res, key_index=0, value_index=1)
        for key, value in data.items():
            item.add_data(key, value)

        return item
