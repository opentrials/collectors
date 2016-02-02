# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from .. import base
from . import utils
from .item import Item


# Module API

class Spider(base.Spider):

    # Public

    name = 'actrn'
    allowed_domains = ['anzctr.org.au']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Make start urls
        self.start_urls = utils.make_start_urls(
                prefix='http://www.anzctr.org.au/TrialSearch.aspx',
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
        item = Item.create(source=res.url)

        # Add main data
        key_path = '.review-element-name'
        value_path = '.review-element-content'
        data = utils.extract_definition_list(res, key_path, value_path)
        for key, value in data.items():
            item.add_data(key, value)

        return item
