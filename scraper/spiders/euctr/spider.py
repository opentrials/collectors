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

        # A. Protocol Information
        ident = 'section-a'
        kpath = '.second'
        vpath = '.second+.third'
        table = utils.select_table(res, ident)
        subdata = utils.extract_dict(table, kpath, vpath)
        data.update(subdata)

        # B. Sponsor information
        key = 'sponsors'
        ident = 'section-b'
        kpath = '.second'
        vpath = '.second+.third'
        first = 'name_of_sponsor'
        table = utils.select_table(res, ident)
        value = utils.extract_list(table, kpath, vpath, first)
        data.update({key: value})

        # C. Applicant Identification
        # ...

        # D. IMP Identification
        key = 'imps'
        ident = 'section-d'
        kpath = '.second'
        vpath = '.second+.third'
        first = 'imp_role'
        table = utils.select_table(res, ident)
        value = utils.extract_list(table, kpath, vpath, first)
        data.update({key: value})

        # D8. Information on Placebo
        key = 'placebos'
        ident = 'section-d8'
        kpath = '.second'
        vpath = '.second+.third'
        first = 'is_a_placebo_used_in_this_trial'
        table = utils.select_table(res, ident)
        value = utils.extract_list(table, kpath, vpath, first)
        data.update({key: value})

        # E. General Information on the Trial
        ident = 'section-e'
        kpath = '.second'
        vpath = '.second+.third'
        prefix = 'trial_'
        table = utils.select_table(res, ident)
        subdata = utils.extract_dict(table, kpath, vpath, prefix)
        data.update(subdata)

        # F. Population of Trial Subjects
        ident = 'section-f'
        kpath = '.second'
        vpath = '.second+.third'
        prefix = 'subject_'
        table = utils.select_table(res, ident)
        subdata = utils.extract_dict(table, kpath, vpath, prefix)
        data.update(subdata)

        # G. Investigator Networks to be involved in the Trial
        # ...

        # N. Review by the Competent Authority or Ethics Committee
        ident = 'section-n'
        kpath = '.second'
        vpath = '.second+.third'
        table = utils.select_table(res, ident)
        subdata = utils.extract_dict(table, kpath, vpath)
        data.update(subdata)

        # P. End of Trial
        ident = 'section-p'
        kpath = '.second'
        vpath = '.second+.third'
        table = utils.select_table(res, ident)
        subdata = utils.extract_dict(table, kpath, vpath)
        data.update(subdata)

        # Create item, map and add data
        item = Item.create(source=res.url)
        data = self.mapper.map_data(data)
        item.add_data(data)

        return item
