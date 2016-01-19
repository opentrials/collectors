# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from urllib import urlencode
from collections import OrderedDict


def make_start_urls(base, date_from, date_to):
    """ Return start_urls.
    """
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
    pattern += 'pageSize=100&searchType=advanced-search$'
    return pattern
