# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from urllib import urlencode
from collections import OrderedDict


# Module API

def make_start_urls(prefix, page_from=None):
    """ Return start_urls.
    """
    if page_from is None:
        page_from = '1'
    query = OrderedDict()
    query['_page'] = page_from
    query['sort'] = '05'
    query['function'] = 'search'
    query['action'] = 'list'
    query['language'] = 'E'
    return [prefix + '?' + urlencode(query)]


def make_pattern(prefix):
    """ Return pattern.
    """
    return prefix + r'\?_page=\d+'
