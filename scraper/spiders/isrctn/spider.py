# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from datetime import date, timedelta
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from . import utils
from .item import Item


class Spider(CrawlSpider):

    # Public

    name = 'isrctn'
    allowed_domains = ['isrctn.com']
    rules = [
        Rule(LinkExtractor(allow=utils.make_pattern('search'))),
        Rule(LinkExtractor(allow=r'ISRCTN\d+'), callback='parse_item'),
    ]

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)

        # Defaul values
        if date_from is None:
            date_from = str(date.today() - timedelta(days=1))
        if date_to is None:
            date_to = str(date.today())

        # Make start urls
        self.start_urls = utils.make_start_urls(
                base='http://www.isrctn.com/search',
                date_from=date_from, date_to=date_to)

    def parse_item(self, res):

        # Create item
        item = Item()

        # Get isrctn_id
        path = '.ComplexTitle_primary::text'
        item['isrctn_id'] = res.css(path).extract_first()

        # Get meta
        key = None
        value = None
        for sel in res.css('.Meta_name, .Meta_name+.Meta_value'):
            if sel.css('.Meta_name'):
                key = None
                value = None
                items = sel.xpath('text()').extract()
                if items:
                    key = utils.slugify(items[0].strip())
            else:
                if key is not None:
                    value = None
                    items = sel.xpath('text()').extract()
                    if items:
                        value = items[0].strip()
            if key and value:
                item.add_data(key, value)

        # Get data
        key = None
        value = None
        for sel in res.css('.Info_section_title, .Info_section_title+p'):
            if sel.css('.Info_section_title'):
                key = None
                value = None
                items = sel.xpath('text()').extract()
                if items:
                    key = utils.slugify(items[0].strip())
            else:
                if key is not None:
                    value = None
                    items = sel.xpath('text()').extract()
                    if items:
                        value = items[0].strip()
            if key and value:
                item.add_data(key, value)

        return item
