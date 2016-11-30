# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collectors.takeda.parser import parse_record


class TestTakedaParser(object):
    def test_download_the_clinical_trial_summary_contains_absolute_url(self, get_url):
        url = 'https://www.takedaclinicaltrials.com/browse/summary/TAK-648_101'
        response = get_url(url)

        record = parse_record(response)

        assert record['download_the_clinical_trial_summary'] == 'https://www.takedaclinicaltrials.com/files2/TAK-648-101-RDS-2016-02-10.pdf'

    def test_download_the_clinical_trial_summary_prefers_english_pdf_when_available(self, get_url):
        url = 'https://www.takedaclinicaltrials.com/browse/summary/073-011'
        response = get_url(url)

        record = parse_record(response)

        assert record.get('download_the_clinical_trial_summary') == 'https://www.takedaclinicaltrials.com/files2/073-011-RDS-2015-03-27.pdf'

    def test_download_the_clinical_trial_summary_gets_japanese_pdf_if_no_english_available(self, get_url):
        url = 'https://www.takedaclinicaltrials.com/browse/summary/AG-1749/CCT-352'
        response = get_url(url)

        record = parse_record(response)

        assert record.get('download_the_clinical_trial_summary') == 'https://www.takedaclinicaltrials.com/files2/AG-1749-CCT-352-RDS-2010-10-17_JP.pdf'

    def test_download_the_clinical_trial_summary_is_none_for_trials_without_results(self, get_url):
        url = 'https://www.takedaclinicaltrials.com/browse/summary/NaltrexBuprop-4004'
        response = get_url(url)

        record = parse_record(response)

        assert record.get('download_the_clinical_trial_summary') is None

    def test_download_the_clinical_trial_summary_is_none_for_trials_with_results_unavailable_on_takeda(self, get_url):
        url = 'https://www.takedaclinicaltrials.com/browse/summary/ATS%20K023'
        response = get_url(url)

        record = parse_record(response)

        assert record.get('download_the_clinical_trial_summary') is None
