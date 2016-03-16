# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from .. import base
from .mapper import TakedaMapper


# Module API

class TakedaSpider(base.Spider):

    # Public

    name = 'takeda'
    allowed_domains = ['takedaclinicaltrials.com']

    def __init__(self, *args, **kwargs):

        # Make mapper
        self.mapper = TakedaMapper()

        # Make urls
        self.start_urls = [
            'http://www.takedaclinicaltrials.com/browse/?protocol_id=',
        ]

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'browse/summary/',
            ), callback=self.mapper.map_response),
            Rule(LinkExtractor(
                allow=r'browse',
            )),
        ]

        # Inherit parent
        super(TakedaSpider, self).__init__(*args, **kwargs)
