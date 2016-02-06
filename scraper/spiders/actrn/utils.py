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


def extract_dict(sel, kpath, vpath):
    """Extract data from title-paragraph like html.
    """
    data = {}
    key = None
    value = None
    for sel in sel.css('%s, %s' % (kpath, vpath)):
        if sel.css(kpath):
            key = None
            value = None
            raw_texts = sel.xpath('.//text()').extract()
            texts = []
            for text in raw_texts:
                # Remove hidden int values
                try:
                    int(text)
                except Exception:
                    texts.append(text)
            if texts:
                key = base.utils.slugify(' '.join(texts).strip())
        else:
            if key is not None:
                value = None
                texts = sel.xpath('.//text()').extract()
                if texts:
                    value = ' '.join(texts).strip()
        if key and value:
            data[key] = value
    return data
