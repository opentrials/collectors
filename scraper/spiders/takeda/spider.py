# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from urllib import urlencode
from datetime import date, timedelta
from collections import OrderedDict
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from .. import base
from .mapper import Mapper


# Module API

class Spider(base.Spider):

    # Public

    name = 'takeda'
    allowed_domains = ['takedaclinicaltrials.com']

    def __init__(self, *args, **kwargs):

        # Make mapper
        self.mapper = Mapper()

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
        super(Spider, self).__init__(*args, **kwargs)
