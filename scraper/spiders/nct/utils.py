# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
import json
import logging
import xmltodict
from urllib import urlencode
from datetime import datetime, date, timedelta
from collections import OrderedDict

logger = logging.getLogger(__name__)


def make_start_urls(base, date_from=None, date_to=None):
    """ Return start_urls.
    """
    if date_from is None:
        date_from = str(date.today() - timedelta(days=1))
    if date_to is None:
        date_to = str(date.today())
    query = OrderedDict()
    date_from = datetime.strptime(date_from, '%Y-%m-%d')
    date_to = datetime.strptime(date_to, '%Y-%m-%d')
    query['lup_s'] = date_from.strftime('%m/%d/%Y')
    query['lup_e'] = date_to.strftime('%m/%d/%Y')
    return [base + '?' + urlencode(query)]


def make_pattern(base):
    """ Return pattern.
    """
    return base + r'\?lup_s=[^&]+&lup_e=[^&]+(&pg=\d+)?$'


def slugify(name):
    """Replace unwanted chars.
    """
    name = name.lower()
    name = re.sub(r'\s+', '_', name)
    name = re.sub(r'[^\w]+', '', name)
    name = '_'.join(name.split('_')[:8])
    return name


def get_text(res, path, process=None):
    """Extract text from response by path.
    """
    value = None
    try:
        nodes = res.xpath(path)
        if nodes:
            value = nodes.xpath('text()').extract_first()
            if process:
                value = process(value)
    except Exception as exception:
        logger.debug(path + ': ' + str(exception))
    return value


def get_dict(res, path, expand=None):
    """Extract dict from response by path.
    """
    value = None
    try:
        nodes = res.xpath(path)
        if nodes:
            text = nodes.extract_first()
            hash = xmltodict.parse(text)
            if expand:
                hash = hash[expand]
            value = json.dumps(hash)
    except Exception as exception:
        logger.debug(path + ': ' + str(exception))
    return value


def get_list(res, path, expand=None):
    """Extract list from response by path.
    """
    value = None
    try:
        nodes = res.xpath(path)
        if nodes:
            hashs = []
            texts = nodes.extract()
            for text in texts:
                hash = xmltodict.parse(text)
                if expand:
                    hash = hash[expand]
                hashs.append(hash)
            value = json.dumps(hashs)
    except Exception as exception:
        logger.debug(path + ': ' + str(exception))
    return value
