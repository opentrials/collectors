# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time
import logging
import requests
import datetime
from urllib import urlencode
from collections import OrderedDict
from .. import base
from .parser import parse_record
logger = logging.getLogger(__name__)


# Module API

def collect(conf, conn, date_from=None, date_to=None):

    # Start collector
    date_from = _get_date_from(conn, date_from)
    date_to = _get_date_to(conn, date_to)
    base.helpers.start(conf, 'hra', {'date_from': date_from, 'date_to': date_to})

    # Get parameters
    URL = conf['HRA_URL']
    USER = conf['HRA_USER']
    PASS = conf['HRA_PASS']

    count = 0
    chunk_days = 100
    session = requests.Session()
    loop_date_from = date_from
    while True:
        if loop_date_from > date_to:
            break
        loop_date_to = min(loop_date_from + datetime.timedelta(days=chunk_days), date_to)
        url = _make_request_url(URL, loop_date_from, loop_date_to)
        response = session.get(url, auth=(USER, PASS))
        response.raise_for_status()
        base.config.SENTRY.extra_context({
            'url': response.url,
        })
        for item in response.json():
            record = parse_record(response.url, item)
            if not record:
                continue
            record.write(conf, conn)
            count += 1
            if not count % 100:
                logger.info('Collected "%s" hra records', count)
        loop_date_from = loop_date_to + datetime.timedelta(days=1)
        time.sleep(1)

    # Stop collector
    base.helpers.stop(conf, 'hra', {'collected': count})


# Internal

def _get_date_from(conn, date_from):
    if date_from is not None:
        return datetime.datetime.strptime(date_from, '%Y-%m-%d')
    date_from = datetime.date(2008, 1, 1)
    if 'hra' in conn['warehouse'].tables:
        rows = conn['warehouse'].query("""
            SELECT least(max(publication_date), max(updated_date)) as latest
            FROM hra
        """)
        latest = list(rows)[0]['latest']
        if latest:
            date_from = latest
    return date_from


def _get_date_to(conn, date_to):
    if date_to is not None:
        return datetime.datetime.strptime(date_to, '%Y-%m-%d')
    return datetime.date.today()


def _make_request_url(prefix, date_from, date_to):
    query = OrderedDict()
    query['datePublishedFrom'] = date_from.strftime('%Y-%m-%d')
    query['datePublishedTo'] = date_to.strftime('%Y-%m-%d')
    url = '%s?%s' % (prefix, urlencode(query))
    return url
