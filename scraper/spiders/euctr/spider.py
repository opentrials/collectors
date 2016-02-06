# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from .. import base
from . import utils
from .mapper import Mapper


# Module API

class Spider(base.Spider):

    # Public

    name = 'euctr'
    allowed_domains = ['clinicaltrialsregister.eu']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Create mapper
        self.mapper = Mapper()

        # Make start urls
        self.start_urls = utils.make_start_urls(
                prefix='https://www.clinicaltrialsregister.eu/ctr-search/search',  # noqa
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'ctr-search/trial/[\d-]+/[\w]+'
            ), callback=self.mapper.map_response),
            Rule(LinkExtractor(
                allow=r'page=\d+',
            ), process_links=self.process_links),
        ]

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)

    def process_links(self, links):
        result = []
        for link in links:
            link.url = '&page='.join(
                    [self.start_urls[0], link.url.split('=')[-1]])
            result.append(link)
        return result
