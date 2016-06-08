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

def collect(conf, conn):

    # Start collector
    date_from = _get_date_from(conn)
    base.helpers.start('hra', {'date_from': date_from})

    # Get parameters
    ENV = conf['HRA_ENV']
    URL = conf['HRA_URL']
    USER = conf['HRA_USER']
    PASS = conf['HRA_PASS']

    # Check availability
    utc_datetime = datetime.datetime.utcnow()
    available = _check_availability(utc_datetime, env=ENV)
    if not available:
        base.helpers.stop('hra', {'reason': 'API is not available'})

    count = 0
    chunk_days = 100
    session = requests.Session()
    while True:
        if date_from > datetime.date.today():
            break
        date_to = date_from + datetime.timedelta(days=chunk_days)
        url = _make_request_url(URL, date_from, date_to)
        response = session.get(url, auth=(USER, PASS))
        for item in response.json():
            try:
                record = parse_record(response.url, item)
                record.write(conf, conn)
                count += 1
                if not count % 100:
                    logger.info('Collected "%s" hra records', count)
            except Exception as exception:
                logger.exception('Collecting error: %s', repr(exception))
        date_from = date_to + datetime.timedelta(days=1)
        time.sleep(1)

    # Stop collector
    base.helpers.stop('hra', {'collected': count})


# Internal

def _check_availability(utc_datetime, env='PRODUCTION'):
    if env == 'PRODUCTION':
        if utc_datetime.weekday() not in [0, 2, 3]:
            return False
        if utc_datetime.time() < datetime.time(6, 0):
            return False
        if utc_datetime.time() > datetime.time(8, 0):
            return False
    return True


def _get_date_from(conn):
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


def _make_request_url(prefix, date_from, date_to):
    query = OrderedDict()
    query['datePublishedFrom'] = date_from.strftime('%Y-%m-%d')
    query['datePublishedTo'] = date_to.strftime('%Y-%m-%d')
    url = '%s?%s' % (prefix, urlencode(query))
    return url
