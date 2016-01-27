# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from urllib import urlencode
from datetime import date, timedelta
from collections import OrderedDict
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
        self.start_urls = _make_start_urls(
                base='http://www.isrctn.com/search',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(allow=_make_pattern('search'))),
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
        data = _extract_definition_list(res, key_path, value_path)
        for key, value in data.items():
            item.add_data(key, value)

        # Add main data
        key_path = '.Info_section_title'
        value_path = '.Info_section_title+p'
        data = _extract_definition_list(res, key_path, value_path)
        for key, value in data.items():
            item.add_data(key, value)

        return item


# Internal

def _make_start_urls(base, date_from=None, date_to=None):
    """ Return start_urls.
    """
    if date_from is None:
        date_from = str(date.today() - timedelta(days=1))
    if date_to is None:
        date_to = str(date.today())
    query = OrderedDict()
    query['q'] = ''
    gtle = 'GT lastEdited:%sT00:00:00.000Z' % date_from
    lele = 'LE lastEdited:%sT00:00:00.000Z' % date_to
    query['filters'] = ','.join([gtle, lele])
    query['page'] = '1'
    query['pageSize'] = '100'
    query['searchType'] = 'advanced-search'
    return [base + '?' + urlencode(query)]


def _make_pattern(base):
    """ Return pattern.
    """
    pattern = base
    pattern += r'\?q=&filters=[^&]+&page=\d+&'
    pattern += r'pageSize=100&searchType=advanced-search$'
    return pattern


def _extract_definition_list(res, key_path, value_path):
    """Extract data from title-paragraph like html.
    """
    data = {}
    key = None
    value = None
    for sel in res.css('%s, %s' % (key_path, value_path)):
        if sel.css(key_path):
            key = None
            value = None
            elements = sel.xpath('text()').extract()
            if elements:
                key = utils.base.slugify(elements[0].strip())
        else:
            if key is not None:
                value = None
                elements = sel.xpath('text()').extract()
                if elements:
                    value = elements[0].strip()
        if key and value:
            data[key] = value
    return data
