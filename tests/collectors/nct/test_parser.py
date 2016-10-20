# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pytest
import io
from collectors.nct.parser import parse_record


class TestNctParser(object):
    @pytest.fixture
    def get_record(self, get_url):
        def _get_record(nct_id):
            url = 'https://clinicaltrials.gov/show/{nct_id}?displayxml=true'.format(nct_id=nct_id)
            response = io.BytesIO(get_url(url).body)
            return parse_record(response)

        return _get_record

    def test_parser_parse_text(self, get_record):
        record = get_record('NCT02931214')
        assert record['url'] == 'https://clinicaltrials.gov/show/NCT02931214'

    def test_parser_parse_list(self, get_record):
        primary_outcomes = [
            {
                'measure': 'Treatment related adverse events',
                'time_frame': '15 days',
                'description': 'Treatment related adverse events as a measure of safety and tolerability of GMI-1359',
                'safety_issue': 'Yes'
            }
        ]
        record = get_record('NCT02931214')
        assert record['primary_outcomes'] == primary_outcomes

    def test_parser_parse_dict(self, get_record):
        contact = {
            'phone': '402-476-2811',
            'last_name': 'Laura Sterling, MD'
        }
        record = get_record('NCT02931214')
        assert record['overall_contact'] == contact
