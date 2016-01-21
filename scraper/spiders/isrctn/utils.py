# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from urllib import urlencode
from datetime import date, timedelta
from collections import OrderedDict


def make_start_urls(base, date_from=None, date_to=None):
    """ Return start_urls.
    """
    if date_from is None:
        date_from = str(date.today() - timedelta(days=1))
    if date_to is None:
        date_to = str(date.today())
    query = OrderedDict()
    query['q'] = ''
    gtle = 'GT lastEdited:%sT00:00:00.000Z' % date_from
    lele = 'LE lastEdited:%sT00:00:00.000Z' % date_to
    query['filters'] = ','.join([gtle, lele])
    query['page'] = '1'
    query['pageSize'] = '100'
    query['searchType'] = 'advanced-search'
    return [base + '?' + urlencode(query)]


def make_pattern(base):
    """ Return pattern.
    """
    pattern = base
    pattern += r'\?q=&filters=GT[^,]*,LE[^,]*&page=\d+&'
    pattern += r'pageSize=100&searchType=advanced-search$'
    return pattern


def slugify(name):
    """Replace unwanted chars.
    """
    name = name.lower()
    name = re.sub(r'\s+', '_', name)
    name = re.sub(r'[^\w]+', '', name)
    name = '_'.join(name.split('_')[:8])
    return name
