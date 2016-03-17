# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from .. import base
from . import utils
from .parser import GskParser


# Module API

class GskSpider(base.Spider):

    # Public

    name = 'gsk'
    allowed_domains = ['gsk-clinicalstudyregister.com']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Create parser
        self.parser = GskParser()

        # Make start urls
        self.start_urls = utils.make_start_urls(
                prefix='http://www.gsk-clinicalstudyregister.com/search',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'study\/\d+'
            ), callback=self.parser.parse),
        ]

        # Inherit parent
        super(GskSpider, self).__init__(*args, **kwargs)
