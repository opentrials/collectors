# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from urllib import urlencode
from collections import OrderedDict
from datetime import date, timedelta


# Module API

def make_start_urls(prefix, date_from=None, date_to=None):
    """ Return start_urls.
    """
    if date_from is None:
        date_from = str(date.today() - timedelta(days=1))
    if date_to is None:
        date_to = str(date.today())
    query = OrderedDict()
    query['query'] = ''
    query['dateFrom'] = date_from
    query['dateTo'] = date_to
    return [prefix + '?' + urlencode(query)]


def make_pattern(prefix):
    """ Return pattern.
    """
    pattern = prefix
    pattern += r'\?query=&dateFrom=[^&]&dateTo=[^&]&page=\d+'
    return pattern
