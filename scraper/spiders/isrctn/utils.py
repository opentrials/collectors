# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging
import xmltodict
from urllib import urlencode
from collections import OrderedDict

logger = logging.getLogger(__name__)


def make_start_urls(base, date_from, date_to):
    """ Return start_urls.
    """
    query = OrderedDict()
    query['q'] = ''
    gtle = 'GT lastEdited:%sT00:00:00.000Z' % date_from
    lele = 'LE lastEdited:%sT00:00:00.000Z' % date_to
    query['filters'] = ','.join([gtle, lele])
    query['page'] = '1'
    query['pageSize'] = '100'
    query['searchType'] = 'advanced-search'
    return [base + '?' + urlencode(query)]


def make_pattern(base):
    """ Return pattern.
    """
    pattern = base
    pattern += r'\?q=&filters=GT[^,]*,LE[^,]*&page=\d+&'
    pattern += 'pageSize=100&searchType=advanced-search$'
    return pattern


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
