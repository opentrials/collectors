# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from ... import settings
from .. import base
from .parser import IctrpParser


# Module API

class IctrpSpider(base.Spider):

    # Public

    name = 'ictrp'
    allowed_domains = ['who.int']
    http_user = settings.ICTRP_USER
    http_pass = settings.ICTRP_PASS

    def __init__(self, *args, **kwargs):

        # Make parser
        self.parser = IctrpParser()

        # Make urls
        self.start_urls = [
            'http://apps.who.int/trialsearch/crawl/crawl0.aspx',
        ]

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'trialsearch/Trial\d+\.aspx\?trialid=.+',
            ), callback=self.parser.parse),
            Rule(LinkExtractor(
                allow=r'trialsearch/crawl/crawl\d+\.aspx',
            )),
        ]

        # Inherit parent
        super(IctrpSpider, self).__init__(*args, **kwargs)
