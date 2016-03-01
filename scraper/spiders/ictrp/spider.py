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

from ... import settings
from .. import base
from .mapper import Mapper


# Module API

class Spider(base.Spider):

    # Public

    name = 'ictrp'
    allowed_domains = ['who.int']
    http_user = settings.ICTRP_USER
    http_pass = settings.ICTRP_PASS

    def __init__(self, *args, **kwargs):

        # Make mapper
        self.mapper = Mapper()

        # Make urls
        self.start_urls = [
            'http://apps.who.int/trialsearch/crawl/crawl0.aspx',
        ]

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'trialsearch/Trial\d+\.aspx\?trialid=.+',
            ), callback=self.mapper.map_response),
            Rule(LinkExtractor(
                allow=r'trialsearch/crawl/crawl\d+\.aspx',
            )),
        ]

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)
