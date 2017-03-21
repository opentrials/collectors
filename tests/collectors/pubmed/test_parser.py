# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import pytest
from collectors.pubmed.parser import parse_record


class TestPubmedParser(object):
    def test_bug_abstracttext_without_text(self, get_url):
        url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/?db=pubmed&id=22078490&retmode=xml'
        response = get_url(url)

        record = parse_record(response)

        assert record['article_abstract'] is not None

    def test_bug_article_with_multiple_languages_pick_first_one(self, get_url):
        url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/?db=pubmed&id=19082263&retmode=xml'
        response = get_url(url)

        record = parse_record(response)

        assert record['article_language'].lower() == 'eng'

    @pytest.mark.skip(reason='need to find an article without medline journal country')
    def test_bug_article_without_medline_journal_country(self, get_url):
        url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/?db=pubmed&id=10838360&retmode=xml'
        response = get_url(url)

        record = parse_record(response)

        assert record.get('country') is None

    def test_bug_article_without_vernacular_title(self, get_url):
        url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/?db=pubmed&id=27305424&retmode=xml'
        response = get_url(url)

        record = parse_record(response)

        assert record.get('article_vernacular_title') is None

    def test_article_date_corectly_parsed(self, get_url):
        url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/?db=pubmed&id=24165173&retmode=xml'
        response = get_url(url)

        record = parse_record(response)

        assert record.get('article_date') == datetime.date(2013, 10, 28)

    def test_multiple_ids_same_registry_collected(self, get_url):
        url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/?db=pubmed&id=22327499&retmode=xml'
        response = get_url(url)
        record = parse_record(response)

        registry_ids = [reg_id for reg_entry in record.get('registry_ids', [])
                        for reg_id in reg_entry.values()]

        nct_ids = [reg_id for reg_id in registry_ids if 'NCT' in reg_id]

        assert len(nct_ids) == 2
