# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from urllib import urlencode
from datetime import datetime
from collections import OrderedDict


def make_start_urls(base, date_from, date_to):
    """ Return start_urls.
    """
    query = OrderedDict()
    date_from = datetime.strptime(date_from, '%Y-%m-%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d')
    query['lup_s'] = date_from.strftime('%m/%d/%Y')
    query['lup_e'] = date_to.strftime('%m/%d/%Y')
    return [base + '?' + urlencode(query)]


def make_pattern(base):
    """ Return pattern.
    """
    return base + r'\?lup_s=[^&]+&lup_e=[^&]+(&pg=\d+)?$'
