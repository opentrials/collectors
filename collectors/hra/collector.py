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
    ENV = conf['HRA_ENV']
    URL = conf['HRA_URL']
    USER = conf['HRA_USER']
    PASS = conf['HRA_PASS']

    # Check availability
    utc_datetime = datetime.datetime.utcnow()
    available = _check_availability(utc_datetime, env=ENV)
    if not available:
        base.helpers.stop(conf, 'hra', {'reason': 'API is not available'})

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
        for item in response.json():
            try:
                record = parse_record(response.url, item)
                record.write(conf, conn)
                count += 1
                if not count % 100:
                    logger.info('Collected "%s" hra records', count)
            except Exception:
                base.config.SENTRY.captureException(extra={
                    'url': response.url,
                })
        loop_date_from = loop_date_to + datetime.timedelta(days=1)
        time.sleep(1)

    # Stop collector
    base.helpers.stop(conf, 'hra', {'collected': count})


# Internal

def _check_availability(utc_datetime, env='production'):
    if env == 'production':
        if utc_datetime.weekday() not in [0, 2, 3]:
            return False
        if utc_datetime.time() < datetime.time(6, 0):
            return False
        if utc_datetime.time() > datetime.time(8, 0):
            return False
    return True


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
