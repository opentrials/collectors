# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
from urllib import urlencode
from datetime import datetime, date, timedelta
from collections import OrderedDict


def make_start_urls(base, date_from=None, date_to=None):
    """ Return start_urls.
    """
    if date_from is None:
        date_from = str(date.today() - timedelta(days=1))
    if date_to is None:
        date_to = str(date.today())
    query = OrderedDict()
    date_from = datetime.strptime(date_from, '%Y-%m-%d').strftime('%d/%m/%Y')
    date_to = datetime.strptime(date_to, '%Y-%m-%d').strftime('%d/%m/%Y')
    query['searchTxt'] = ''
    query['dateOfRegistrationFrom'] = date_from
    query['dateOfRegistrationTo'] = date_to
    query['registry'] = 'ANZCTR'
    query['isBasic'] = 'False'
    return [base + '?' + urlencode(query)]


def make_pattern(base):
    """ Return pattern.
    """
    return base + r'.*&page=\d+'


def slugify(name):
    """Replace unwanted chars.
    """
    name = name.lower()
    name = re.sub(r'\s+', '_', name)
    name = re.sub(r'[^\w]+', '', name)
    name = '_'.join(name.split('_')[:8])
    return name
