# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collectors.pubmed.spider import _make_start_urls


class TestPubmedSpider(object):
    def test_make_start_urls(self, betamax_session):
        result = _make_start_urls(
            'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/',
            'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/?db=pubmed&id={pmid}&retmode=xml',
            '2016-01-01', '2016-01-01',
            session=betamax_session)
        assert result
