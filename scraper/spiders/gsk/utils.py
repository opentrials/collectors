# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from urllib import urlencode
from collections import OrderedDict
from datetime import date, timedelta

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
    query['last_updated_from'] = date_from
    query['last_updated_to'] = date_to
    return [prefix + '?' + urlencode(query)]


def extract_data(sel, kpath, vpath):
    data = []
    name = None
    value = None
    for sel in sel.css('%s, %s' % (kpath, vpath)):
        text = extract_text(sel)
        if sel.css(kpath):
            name = base.utils.slugify(text)
        else:
            value = text
            if name and value:
                data.append((name, value))
            name = None
            value = None
    return data


def extract_text(sel):
    text = ''
    texts = sel.xpath('.//text()').extract()
    if texts:
        text = ' '.join(texts).strip()
    return text
