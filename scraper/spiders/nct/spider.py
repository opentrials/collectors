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

    name = 'nct'
    allowed_domains = ['clinicaltrials.gov']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Create mapper
        self.mapper = Mapper()

        # Make start urls
        self.start_urls = utils.make_start_urls(
                prefix='https://www.clinicaltrials.gov/ct2/results',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'ct2/show/NCT\d+',
                process_value=lambda value: value+'&resultsxml=true',
            ), callback=self.mapper.map_response),
            Rule(LinkExtractor(
                allow=r'pg=\d+$',
            )),
        ]

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)
