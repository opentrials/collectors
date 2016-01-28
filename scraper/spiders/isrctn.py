# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from .. import items
from .. import utils


# Module API

class Isrctn(CrawlSpider):

    # Public

    name = 'isrctn'
    allowed_domains = ['isrctn.com']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Make start urls
        self.start_urls = utils.isrctn.make_start_urls(
                prefix='http://www.isrctn.com/search',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(allow=utils.isrctn.make_pattern('search'))),
            Rule(LinkExtractor(allow=r'ISRCTN\d+'), callback='parse_item'),
        ]

        # Inherit parent
        super(Isrctn, self).__init__(*args, **kwargs)

    def parse_item(self, res):

        # Create item
        item = items.Isrctn.create(source=res.url)

        # Add isrctn_id
        key = 'isrctn_id'
        path = '.ComplexTitle_primary::text'
        value = res.css(path).extract_first()
        item.add_data(key, value)

        # Add doi_isrctn_id
        key = 'doi_isrctn_id'
        path = '.ComplexTitle_secondary::text'
        value = res.css(path).extract_first()
        item.add_data(key, value)

        # Add title
        key = 'title'
        path = '//h1/text()'
        value = res.xpath(path).extract_first()
        item.add_data(key, value)

        # Add meta data
        key_path = '.Meta_name'
        value_path = '.Meta_name+.Meta_value'
        data = utils.isrctn.extract_definition_list(res, key_path, value_path)
        for key, value in data.items():
            item.add_data(key, value)

        # Add main data
        key_path = '.Info_section_title'
        value_path = '.Info_section_title+p'
        data = utils.isrctn.extract_definition_list(res, key_path, value_path)
        for key, value in data.items():
            item.add_data(key, value)

        return item
