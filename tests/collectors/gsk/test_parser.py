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

        assert record['results_url'] == 'http://www.gsk-clinicalstudyregister.com/files2/19890.pdf'

    def test_results_url_is_none_for_trials_without_results(self, get_url):
        url = 'http://www.gsk-clinicalstudyregister.com/study/106847'
        response = get_url(url)

        record = parse_record(response)

        assert record.get('results_url') is None
