# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collectors.gsk.parser import parse_record


class TestGskParser(object):
    def test_results_url_contains_absolute_url(self, get_url):
        url = 'http://www.gsk-clinicalstudyregister.com/study/100006'
        response = get_url(url)

        record = parse_record(response)

        assert record['results_url'].startswith('http')

    def test_results_url_is_none_for_trials_without_results(self, get_url):
        url = 'http://www.gsk-clinicalstudyregister.com/study/106847'
        response = get_url(url)

        record = parse_record(response)

        assert record.get('results_url') is None

    def test_handles_all_date_formats(self, get_url):
        url = 'https://www.gsk-clinicalstudyregister.com/study/100006'

        response = get_url(url)

        record = parse_record(response)

        assert record.get('last_updated') is not None
        assert record.get('record_verification_date') is not None
        assert record.get('study_start_date') is not None
