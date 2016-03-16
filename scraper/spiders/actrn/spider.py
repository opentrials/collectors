# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from .. import base
from . import utils
from .mapper import ActrnMapper


# Module API

class ActrnSpider(base.Spider):

    # Public

    name = 'actrn'
    allowed_domains = ['anzctr.org.au']

    def __init__(self, date_from=None, date_to=None, *args, **kwargs):

        # Create mapper
        self.mapper = ActrnMapper()

        # Make start urls
        self.start_urls = utils.make_start_urls(
                prefix='http://www.anzctr.org.au/TrialSearch.aspx',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'Trial/Registration/TrialReview.aspx',
                process_value=lambda value: value.replace('http', 'https', 1),
            ), callback=self.mapper.map),
            Rule(LinkExtractor(
                allow=r'page=\d+',
            )),
        ]

        # Inherit parent
        super(ActrnSpider, self).__init__(*args, **kwargs)
