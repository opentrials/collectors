# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import mock
import pytest
import datetime
import requests
from collections import defaultdict
from collectors.hra.collector import collect, _make_request_url


class TestHRACollector(object):
    def test_make_request_url(self):
        date_from = datetime.date(2015, 1, 1)
        date_to = datetime.date(2015, 12, 31)
        actual = _make_request_url('prefix', date_from, date_to)
        expect = 'prefix?datePublishedFrom=2015-01-01&datePublishedTo=2015-12-31'
        assert actual == expect

    @mock.patch('requests.Session.get')
    def test_collect_skips_deffered_records(self, session_get_mock, conn, conf, deferred_item_stub):
        response_mock = mock.Mock()
        response_mock.json.return_value = [
            deferred_item_stub
        ]
        session_get_mock.return_value = response_mock
        collect(conf, conn, '2015-01-01', '2015-01-01')

        hra_id = ('HRA%s' % deferred_item_stub['ApplicationID'])
        assert conn['warehouse']['hra'].find_one(hra_id=hra_id) is None


@pytest.fixture
def deferred_item_stub():
    deferred_item = defaultdict(lambda: None)
    attributes = {
        'ApplicationID': '323854',
        'PublicationDate': 'Publication of this data is currently deferred.',
        'UpdatedDate': '2017-01-05T14:01:03.41',
        'Decision': 'Publication of this data is currently deferred.',
        'DecisionDate': 'Publication of this data is currently deferred.',
    }
    deferred_item.update(attributes)
    return deferred_item
