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

        # Extract general (isrctn_id)
        key = 'isrctn_id'
        path = '.ComplexTitle_primary::text'
        value = res.css(path).extract_first()
        data[key] = value

        # Extract general (doi_isrctn_id)
        key = 'doi_isrctn_id'
        path = '.ComplexTitle_secondary::text'
        value = res.css(path).extract_first()
        data[key] = value

        # Extract general (title)
        key = 'title'
        path = '//h1/text()'
        value = res.xpath(path).extract_first()
        data[key] = value

        # Extract general (metadata)
        kpath = '.Meta_name'
        vpath = '.Meta_name+.Meta_value'
        subdata = utils.extract_dict(res, kpath, vpath)
        data.update(subdata)

        # Extract general (paragraph)
        tag = 'h3'
        text = 'Plain English Summary'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Extract contact information
        key = 'contacts'
        tag = 'h2'
        text = 'Contact information'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        first = 'type'
        section = utils.select_parent(res, tag, text)
        value = utils.extract_list(section, kpath, vpath, first)
        data.update({key: value})

        # Extract additional identifiers
        tag = 'h2'
        text = 'Additional identifiers'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Extract study information
        tag = 'h2'
        text = 'Study information'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Extract eligibility
        tag = 'h2'
        text = 'Eligibility'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Extract locations
        tag = 'h2'
        text = 'Locations'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Extract sponsor information
        key = 'sponsors'
        tag = 'h2'
        text = 'Sponsor information'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        first = 'organisation'
        section = utils.select_parent(res, tag, text)
        value = utils.extract_list(section, kpath, vpath, first)
        data.update({key: value})

        # Extract funders
        key = 'funders'
        tag = 'h2'
        text = 'Funders'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        first = 'funder_type'
        section = utils.select_parent(res, tag, text)
        value = utils.extract_list(section, kpath, vpath, first)
        data.update({key: value})

        # Extract results and publications
        tag = 'h2'
        text = 'Results and Publications'
        kpath = '.Info_section_title'
        vpath = '.Info_section_title+p'
        section = utils.select_parent(res, tag, text)
        subdata = utils.extract_dict(section, kpath, vpath)
        data.update(subdata)

        # Create item, map and add data
        item = Item.create(source=res.url)
        data = self.mapper.map_data(data)
        item.add_data(data)

        return item
