# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from urllib import urlencode
from collections import OrderedDict


def make_start_urls(base, page_from=None):
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
    return [base + '?' + urlencode(query)]


def make_pattern(base):
    """ Return pattern.
    """
    return base + r'\?_page=\d+'


def slugify(name):
    """Replace unwanted chars.
    """
    name = name.lower()
    name = re.sub(r'\s+', '_', name)
    name = re.sub(r'[^\w]+', '', name)
    name = '_'.join(name.split('_')[:8])
    return name
