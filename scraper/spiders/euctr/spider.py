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
from . import utils
from .item import Item
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
                prefix='https://www.clinicaltrialsregister.eu/ctr-search/search',
                date_from=date_from, date_to=date_to)

        # Make rules
        self.rules = [
            Rule(LinkExtractor(allow=utils.make_pattern('ctr-search/search'))),
            Rule(
                LinkExtractor(allow=r'ctr-search/trial/[\d-]+/[\w]+'),
                callback='parse_item'
            ),
        ]

        # Inherit parent
        super(Spider, self).__init__(*args, **kwargs)

    def parse_item(self, res):

        # Init data item
        data = {}

        # Summary (main)
        kpath = '.cellGrey'
        vpath = '.cellGrey+.cellLighterGrey'
        subdata = utils.extract_dict(res, kpath, vpath)
        subdata['eudract_number_with_country'] = res.url.split('/')[-1]
        data.update(subdata)

        # Summary (eudract_number_with_country)
        key = 'eudract_number_with_country'
        value = '-'.join([data['eudract_number'], res.url.split('/')[-1]])
        data.update({key: value})

        # Protocol Information (Section A)
        ident = 'section-a'
        kpath = '.second'
        vpath = '.second+.third'
        table = utils.select_table(res, ident)
        subdata = utils.extract_dict(table, kpath, vpath)
        print(subdata.keys())
        data.update(subdata)

        # Sponsor information (Section B)
        ident = 'section-b'
        # ...


        # Applicant Identification (Section C)
        # ...

        # IMP Identification (Section D)
        ident = 'section-d'

        # Information on Placebo (Section D8)
        ident = 'section-d8'

        # General Information on the Trial (Section E)
        ident = 'section-e'

        # Population of Trial Subjects (Section F)
        ident = 'section-f'

        # Investigator Networks to be involved in the Trial (Section G)
        ident = 'section-g'

        # Review by the Competent Authority or Ethics Committee (Section N)
        ident = 'section-n'

        # End of Trial (Section P)
        ident = 'section-p'

        # Create item, map and add data
        item = Item.create(source=res.url)
        data = self.mapper.map_data(data)
        item.add_data(data)

        return item
