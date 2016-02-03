# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from .. import base
from . import utils
from .item import Item
from .mapper import Mapper


# Module API

class Spider(base.Spider):

    # Public

    name = 'isrctn'
    allowed_domains = ['isrctn.com']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Create mapper
        self.mapper = Mapper()

        # Make start urls
        self.start_urls = utils.make_start_urls(
                prefix='http://www.isrctn.com/search',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(allow=utils.make_pattern('search'))),
            Rule(LinkExtractor(allow=r'ISRCTN\d+'), callback='parse_item'),
        ]

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)

    def parse_item(self, res):

        # Init data
        data = {}

        # Extract isrctn_id
        key = 'isrctn_id'
        path = '.ComplexTitle_primary::text'
        value = res.css(path).extract_first()
        data[key] = value

        # Extract doi_isrctn_id
        key = 'doi_isrctn_id'
        path = '.ComplexTitle_secondary::text'
        value = res.css(path).extract_first()
        data[key] = value

        # Extract title
        key = 'title'
        path = '//h1/text()'
        value = res.xpath(path).extract_first()
        data[key] = value

        # Extract meta data
        key_path = '.Meta_name'
        value_path = '.Meta_name+.Meta_value'
        subdata = utils.extract_definition_list(res, key_path, value_path)
        data.update(subdata)

        # Extract main data
        key_path = '.Info_section_title'
        value_path = '.Info_section_title+p'
        subdata = utils.extract_definition_list(res, key_path, value_path)
        data.update(subdata)

        # Create item, map and add data
        item = Item.create(source=res.url)
        data = self.mapper.map_data(data)
        item.add_data(data)

        return item
