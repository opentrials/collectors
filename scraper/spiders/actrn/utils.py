# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from urllib import urlencode
from collections import OrderedDict
from datetime import datetime, date, timedelta

from .. import base


# Module API

def make_start_urls(prefix, date_from=None, date_to=None):
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
    return [prefix + '?' + urlencode(query)]


def extract_definition_list(res, key_path, value_path):
    """Extract data from title-paragraph like html.
    """
    data = {}
    key = None
    value = None
    for sel in res.css('%s, %s' % (key_path, value_path)):
        if sel.css(key_path):
            key = None
            value = None
            elements = sel.xpath('text()').extract()
            if elements:
                key = base.utils.slugify(elements[0].strip())
        else:
            if key is not None:
                value = None
                elements = sel.xpath('span/text()').extract()
                if elements:
                    value = elements[0].strip()
        if key and value:
            data[key] = value
    return data
