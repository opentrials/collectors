# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from .. import base
from .mapper import PfizerMapper


# Module API

class PfizerSpider(base.Spider):

    # Public

    name = 'pfizer'
    allowed_domains = ['pfizer.com']

    def __init__(self, *args, **kwargs):

        # Make mapper
        self.mapper = PfizerMapper()

        # Make urls
        self.start_urls = [
            'http://www.pfizer.com/research/clinical_trials/find_a_trial?recr=0',  # noqa
        ]

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'find_a_trial/NCT\d+',
            ), callback=self.mapper.map),
            Rule(LinkExtractor(
                allow=r'page=\d+',
            )),
        ]

        # Inherit parent
        super(PfizerSpider, self).__init__(*args, **kwargs)
