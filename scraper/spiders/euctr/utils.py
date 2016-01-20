# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from urllib import urlencode
from collections import OrderedDict


def make_start_urls(base, date_from, date_to):
    """ Return start_urls.
    """
    query = OrderedDict()
    query['query'] = ''
    query['dateFrom'] = date_from
    query['dateTo'] = date_to
    return [base + '?' + urlencode(query)]


def make_pattern(base):
    """ Return pattern.
    """
    pattern = base
    pattern += r'\?query=&dateFrom=[^&]&dateTo=[^&]&page=\d+'
    return pattern


def slugify(name):
    """Replace unwanted chars.
    """
    name = name.lower()
    name = re.sub(r'\s+', '_', name)
    name = re.sub(r'[^\w]+', '', name)
    name = '_'.join(name.split('_')[:8])
    return name
