# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from . import utils
from .item import Item


class Spider(CrawlSpider):

    # Public

    name = 'actrn'
    allowed_domains = ['anzctr.org.au']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Make start urls
        self.start_urls = utils.make_start_urls(
                base='http://www.anzctr.org.au/TrialSearch.aspx',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(allow=utils.make_pattern('TrialSearch.aspx'))),
            Rule(
                LinkExtractor(
                    allow=r'Trial/Registration/TrialReview.aspx',
                    process_value=lambda value: value.replace('http', 'https', 1),
                ),
                callback='parse_item'
            ),
        ]

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)

    def parse_item(self, res):

        # Create item
        item = Item()

        # Get data
        key = None
        value = None
        for sel in res.css('.review-element-name, .review-element-content'):
            if sel.css('.review-element-name'):
                key = None
                value = None
                items = sel.xpath('text()').extract()
                if items:
                    key = utils.slugify(items[0].strip())
            else:
                if key is not None:
                    value = None
                    items = sel.xpath('span/text()').extract()
                    if items:
                        value = items[0].strip()
            if key and value:
                item.add_data(key, value)

        return item
