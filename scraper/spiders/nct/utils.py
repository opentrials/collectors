# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import xmltodict
from urllib import urlencode
from datetime import datetime, date, timedelta
from collections import OrderedDict

logger = logging.getLogger(__name__)


# Module API

def make_start_urls(prefix, date_from=None, date_to=None):
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
    return [prefix + '?' + urlencode(query)]


def extract_text(res, path):
    """Extract text from response by path.
    """
    value = None
    try:
        nodes = res.xpath(path)
        if nodes:
            value = nodes.xpath('text()').extract_first()
            value = value.strip()
    except Exception as exception:
        message = 'Extraction error: %s: %s'
        message = message % (path, repr(exception))
        logger.info(message)
    return value


def extract_dict(res, path, expand=None):
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
            value = hash
    except Exception as exception:
        message = 'Extraction error: %s: %s'
        message = message % (path, repr(exception))
        logger.info(message)
    return value


def extract_list(res, path, expand=None):
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
            value = hashs
    except Exception as exception:
        message = 'Extraction error: %s: %s'
        message = message % (path, repr(exception))
        logger.info(message)
    return value
