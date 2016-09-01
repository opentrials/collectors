# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collectors.euctr.parser import parse_record


class TestEuctrParser(object):
    def test_trial_results_returns_absolute_results_url(self, get_url):
        url = 'https://www.clinicaltrialsregister.eu/ctr-search/trial/2011-005852-33/3rd'
        response = get_url(url)

        record = parse_record(response)

        assert record['trial_results'] == 'https://www.clinicaltrialsregister.eu/ctr-search/trial/2011-005852-33/results'

    def test_trial_results_is_none_if_therere_no_results(self, get_url):
        url = 'https://www.clinicaltrialsregister.eu/ctr-search/trial/2009-016529-32/EE'
        response = get_url(url)

        record = parse_record(response)

        assert record.get('trial_results') is None
