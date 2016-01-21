# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from six.moves.urllib.parse import urlparse, parse_qs

from . import utils
from .item import Item


class Spider(CrawlSpider):

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
        self.start_urls = utils.make_start_urls(
                base='https://upload.umin.ac.jp/cgi-open-bin/ctr/ctr.cgi',
                page_from=page_from)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=utils.make_pattern('cgi-open-bin/ctr/ctr.cgi'),
                process_value=self.process_url,
            )),
            Rule(
                LinkExtractor(allow=r'cgi-open-bin/ctr/ctr.cgi\?function=brows',),
                callback='parse_item',
            ),
        ]

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)

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
        item = Item()

        # Get meta
        for sel in res.xpath('//tr'):
            columns = sel.xpath('td')
            if len(columns) == 3:
                key = ''.join(columns[0].xpath('.//text()').extract())
                key = utils.slugify(key.strip())
                value = ''.join(columns[2].xpath('.//text()').extract())
                value = value.strip()
                if key and value:
                    item.add_data(key, value)

        # Get data
        for sel in res.xpath('//tr'):
            columns = sel.xpath('td')
            if len(columns) == 2:
                key = ''.join(columns[0].xpath('.//text()').extract())
                key = utils.slugify(key.strip())
                value = ''.join(columns[0].xpath('.//text()').extract())
                value = value.strip()
                if key and value:
                    item.add_data(key, value)

        return item
