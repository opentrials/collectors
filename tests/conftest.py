# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import pytest
import betamax
import requests
import dataset
from scrapy.http import Request, HtmlResponse
from collectors.base import config, helpers


with betamax.Betamax.configure() as cfg:
    cfg.cassette_library_dir = 'tests/cassettes/'

    record_mode = 'never' if os.environ.get('CI') else 'once'
    cfg.default_cassette_options['record_mode'] = record_mode
    cfg.default_cassette_options['match_requests_on'] = [
        'uri',
        'method',
        'headers',
        'body',
    ]


# Fixtures

@pytest.fixture
def conf():
    return helpers.get_variables(config, str.isupper)


@pytest.fixture
def conn():
    warehouse = dataset.connect(config.TEST_WAREHOUSE_URL)
    for table in warehouse.tables:
        warehouse[table].delete()
    return {'warehouse': warehouse}


@pytest.yield_fixture
def betamax_session(request):
    '''Setups a betamax cassette and yields a requests session using it.

    The cassette name is generated based on the calling class and method names.
    '''
    class_name = request.instance.__class__.__name__
    method_name = request.function.__name__
    cassette_name = '.'.join([class_name, method_name])
    session = requests.Session()
    recorder = betamax.Betamax(session)

    with recorder.use_cassette(cassette_name):
        yield session


@pytest.fixture
def get_url(betamax_session):
    def _get_url(url, request_kwargs={}):
        '''Returns a scrapy.html.HtmlResponse with the contents of the received
        url.

        Note that the session is kept intact among multiple calls to this
        method (i.e. cookies are passed over).
        '''
        response = betamax_session.get(url)
        scrapy_response = HtmlResponse(
            url=str(response.url),
            body=response.content,
        )
        scrapy_response.request = Request(url, **request_kwargs)

        return scrapy_response
    return _get_url
