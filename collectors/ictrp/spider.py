# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from .parser import parse_record


# Module API

class Spider(CrawlSpider):

    # Public

    name = 'ictrp'
    allowed_domains = ['who.int']

    def __init__(self, conf=None, conn=None, http_user=None, http_pass=None):

        # Save conf/conn
        self.conf = conf
        self.conn = conn

        # Save creadentials
        self.http_user = http_user
        self.http_pass = http_pass

        # Make urls
        self.start_urls = [
            'http://apps.who.int/trialsearch/crawl/crawl0.aspx',
        ]

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'trialsearch/Trial\d+\.aspx\?trialid=.+',
                process_value=lambda value: value.replace('Trial3', 'Trial2'),
            ), callback=parse_record),
            Rule(LinkExtractor(
                allow=r'trialsearch/crawl/crawl\d+\.aspx',
            )),
        ]

        # Inherit parent
        super(Spider, self).__init__()
